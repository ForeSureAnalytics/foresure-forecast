from __future__ import annotations

import pandas as pd


def load_sales(path: str) -> pd.DataFrame:
    """Load sales CSV data."""
    return pd.read_csv(path, parse_dates=["day_key"])
