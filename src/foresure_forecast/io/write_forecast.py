from __future__ import annotations

from pathlib import Path
from datetime import datetime
import pandas as pd


def save_forecasts(df: pd.DataFrame, cfg) -> Path:
    """Save forecasts to timestamped output directory."""
    output_dir = Path("output") / datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "forecast.csv"
    df.to_csv(out_path, index=False)
    return out_path
