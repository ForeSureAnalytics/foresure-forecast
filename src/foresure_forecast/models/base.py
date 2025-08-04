from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict
import pandas as pd


class BaseModel(ABC):
    name: str

    def __init__(self, cfg):
        self.cfg = cfg

    @abstractmethod
    def fit_forecast(self, df: pd.DataFrame) -> dict:
        """Fit model and return forecast information."""
        raise NotImplementedError


MODEL_REGISTRY: Dict[str, type[BaseModel]] = {}
