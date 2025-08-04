from __future__ import annotations

from typing import Sequence


def rank_models(results: Sequence[dict]):
    """Select the model result with the lowest RMSE."""
    best = min(results, key=lambda r: r["rmse"])
    return best["forecast"]
