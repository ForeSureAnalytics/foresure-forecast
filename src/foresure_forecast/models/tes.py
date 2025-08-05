from __future__ import annotations
 
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
 
from .base import BaseModel, MODEL_REGISTRY
 
 
 class TESModel(BaseModel):
     name = "TES"
 
     def fit_forecast(self, df: pd.DataFrame) -> dict:
         series = df["qty_sold"].fillna(0)

         category = (
             df["category"].iloc[0]
             if "category" in df.columns and not df["category"].empty
             else None
         )
         seasonal_period = self.cfg.category_seasonal_periods.get(
             category, self.cfg.default_seasonal_period
         )
 
         model = ExponentialSmoothing(
             series,
             trend="add",
             seasonal="add",
             seasonal_periods=seasonal_period,
         ).fit()
         fitted = model.fittedvalues
         rmse = mean_squared_error(series, fitted, squared=False)
         mape = mean_absolute_percentage_error(series, fitted)
         forecast_vals = model.forecast(self.cfg.forecast_horizon_days)
         future_dates = pd.date_range(
             start=df["day_key"].max() + pd.Timedelta(days=1),
             periods=self.cfg.forecast_horizon_days,
             freq="D",
         )
         forecast = pd.DataFrame(
             {"day_key": future_dates, "forecast_qty": forecast_vals}
         )
         return {"name": self.name, "rmse": rmse, "mape": mape, "forecast": forecast}


MODEL_REGISTRY[TESModel.name] = TES

