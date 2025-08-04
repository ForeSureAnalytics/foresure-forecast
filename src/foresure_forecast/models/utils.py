from __future__ import annotations

import numpy as np
import pandas as pd


def rmse(actual: pd.Series, predicted: pd.Series) -> float:
    """Root mean squared error."""
    actual_arr = actual.to_numpy(dtype=float)
    pred_arr = predicted.to_numpy(dtype=float)
    return float(np.sqrt(np.mean((actual_arr - pred_arr) ** 2)))


def mape(actual: pd.Series, predicted: pd.Series) -> float:
    """Mean absolute percentage error.

    Any zero values in ``actual`` are replaced with a small epsilon to avoid
    division by zero.
    """
    actual_arr = actual.to_numpy(dtype=float)
    pred_arr = predicted.to_numpy(dtype=float)
    denom = np.where(actual_arr == 0, np.finfo(float).eps, actual_arr)
    return float(np.mean(np.abs((actual_arr - pred_arr) / denom)))
