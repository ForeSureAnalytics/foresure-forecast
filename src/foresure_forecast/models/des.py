from __future__ import annotations

import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from .base import BaseModel, MODEL_REGISTRY


class DESModel(BaseModel):
    name = "DES"

    def fit_forecast(self, df: pd.DataFrame) -> dict:
        series = df["qty_sold"].fillna(0)
        model = ExponentialSmoothing(series, trend="add").fit()
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


MODEL_REGISTRY[DESModel.name] = DESModel
