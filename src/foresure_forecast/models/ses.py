from __future__ import annotations

import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

from .base import BaseModel, MODEL_REGISTRY
from .utils import rmse, mape


class SESModel(BaseModel):
    name = "SES"

    def fit_forecast(self, df: pd.DataFrame) -> dict:
        series = df["qty_sold"].fillna(0)
        model = SimpleExpSmoothing(series).fit()
        fitted = model.fittedvalues
        rmse_val = rmse(series, fitted)
        mape_val = mape(series, fitted)
        forecast_vals = model.forecast(self.cfg.forecast_horizon_days)
        future_dates = pd.date_range(
            start=df["day_key"].max() + pd.Timedelta(days=1),
            periods=self.cfg.forecast_horizon_days,
            freq="D",
        )
        forecast = pd.DataFrame(
            {"day_key": future_dates, "forecast_qty": forecast_vals}
        )
        return {
            "name": self.name,
            "rmse": rmse_val,
            "mape": mape_val,
            "forecast": forecast,
        }


MODEL_REGISTRY[SESModel.name] = SES
