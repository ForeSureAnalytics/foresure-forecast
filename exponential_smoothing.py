# forecast_engine.py

import pandas as pd
import numpy as np
from pathlib import Path
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

from config.forecast_config import generate_forecast_config

# === Load Data ===
def load_forecast_input(filepath):
    df = pd.read_csv(filepath, parse_dates=["day_key"])
    df.sort_values(by=["sku", "location_id", "day_key"], inplace=True)
    return df

# === Forecasting Models ===
def run_ses(series):
    clean = series.fillna(0).reset_index(drop=True)
    m = SimpleExpSmoothing(clean).fit()
    return m.fittedvalues, m

def run_des(series):
    clean = series.fillna(0).reset_index(drop=True)
    m = ExponentialSmoothing(clean, trend="add").fit()
    return m.fittedvalues, m

def run_tes(series, seasonal_periods):
    clean = series.fillna(0).reset_index(drop=True)
    m = ExponentialSmoothing(
        clean,
        trend="add",
        seasonal="add",
        seasonal_periods=seasonal_periods
    ).fit()
    return m.fittedvalues, m

# === Evaluation ===
def evaluate_forecast(true, pred):
    t = true.fillna(0).reset_index(drop=True)
    p = pred[:len(t)]
    rmse = np.sqrt(mean_squared_error(t, p))
    mape = mean_absolute_percentage_error(t, p)
    return rmse, mape

# === Main Loop: selection + future forecast ===
def process_forecasts(df):
    summary_rows = []
    forecast_rows = []

    for (sku, loc), grp in df.groupby(["sku", "location_id"]):
        # --- Build config kwargs ---
        cfg_kwargs = {"sku_history": grp}
        if "lead_time_days" in grp.columns and pd.notna(grp["lead_time_days"].iloc[0]):
            cfg_kwargs["lead_time_days"] = int(grp["lead_time_days"].iloc[0])
        if "reorder_cycle_days" in grp.columns and pd.notna(grp["reorder_cycle_days"].iloc[0]):
            cfg_kwargs["reorder_cycle_days"] = int(grp["reorder_cycle_days"].iloc[0])
        if "category" in grp.columns and pd.notna(grp["category"].iloc[0]):
            cfg_kwargs["category"] = grp["category"].iloc[0]

        config = generate_forecast_config(**cfg_kwargs)
        y = grp["qty_sold"]

        # --- Decide which methods to run ---
        methods = {}
        if len(y) >= config["min_obs_required"]["SES"]:
            methods["SES"] = run_ses(y)
        if config["allow_DES"] and len(y) >= config["min_obs_required"]["DES"]:
            methods["DES"] = run_des(y)
        if config["allow_TES"] and len(y) >= config["min_obs_required"]["TES"]:
            methods["TES"] = run_tes(y, config["seasonal_periods"])

        if not methods:
            print(f"Skipping {sku}@{loc}: insufficient history")
            continue

        # --- Evaluate & pick best ---
        evals = {m: evaluate_forecast(y, fcast) for m, (fcast, _) in methods.items()}
        best = min(evals, key=lambda k: evals[k][0])
        best_model, best_rmse, best_mape = best, evals[best][0], evals[best][1]

        # --- Summarize selection + config ---
        row = {
            "sku": sku,
            "location_id": loc,
            "best_model": best_model,
            "rmse": round(best_rmse, 4),
            "mape": round(best_mape, 4),
            **config
        }
        summary_rows.append(row)

        # --- Generate future forecast ---
        # 1) Determine horizon: override if present in CSV
        if "forecast_horizon_days" in grp.columns and pd.notna(grp["forecast_horizon_days"].iloc[0]):
            horizon = int(grp["forecast_horizon_days"].iloc[0])
        else:
            horizon = config["horizon_days"]

        # 2) Build date index
        last_date = grp["day_key"].max()
        future_dates = pd.date_range(
            start=last_date + pd.Timedelta(days=1),
            periods=horizon,
            freq="D"
        )

        # 3) Forecast with best model’s fitted object
        model_obj = methods[best][1]
        forecast_vals = model_obj.forecast(horizon)

        # 4) Record one row per future date
        for dt, qty in zip(future_dates, forecast_vals):
            # how many days ahead is this forecast?
            horizon_offset = (dt - last_date).days

            forecast_rows.append({
                "sku": sku,
                "location_id": loc,
                "forecast_date": dt.date().isoformat(),
                "forecast_qty": int(round(qty)),
                # of daysahead (1 = tomorrow, 2 = day after, etc.)
                "forecast_horizon": horizon_offset
            })

    summary_df = pd.DataFrame(summary_rows)
    forecast_df = pd.DataFrame(forecast_rows)

    return summary_df, forecast_df

# === Script Entry Point ===
if __name__ == "__main__":
    input_path  = Path("data/fact_forecast_input.csv")
    out_summary = Path("output/best_model_per_sku.csv")
    out_fore    = Path("output/forecasted_quantities.csv")

    df = load_forecast_input(input_path)
    summary_df, forecast_df = process_forecasts(df)

    out_summary.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(out_summary, index=False)
    forecast_df.to_csv(out_fore, index=False)

    print("✅ Selection saved to", out_summary)
    print("✅ Forecasts saved to", out_fore)
