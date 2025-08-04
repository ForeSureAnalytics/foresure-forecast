from dataclasses import dataclass
from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).with_suffix(".yaml")


@dataclass
class Settings:
    lead_time_days: int
    reorder_cycle_days: int
    forecast_horizon_days: int
    models_to_run: list[str]


def load() -> Settings:
    with CONFIG_PATH.open() as fh:
        raw = yaml.safe_load(fh)
    return Settings(**raw)
