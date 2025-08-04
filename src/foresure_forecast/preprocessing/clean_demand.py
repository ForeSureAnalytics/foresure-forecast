from __future__ import annotations

import pandas as pd


def clean_demand(df: pd.DataFrame, cfg) -> pd.DataFrame:
    """Basic demand cleaning: fill missing quantities with zero."""
    cleaned = df.copy()
    if "qty_sold" in cleaned.columns:
        cleaned["qty_sold"] = cleaned["qty_sold"].fillna(0)
    return cleaned
