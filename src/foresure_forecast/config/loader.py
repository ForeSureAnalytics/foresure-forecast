from dataclasses import dataclass, field
from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).with_suffix(".yaml")


@dataclass
class Settings:
    lead_time_days: int
    reorder_cycle_days: int
    forecast_horizon_days: int
    models_to_run: list[str]
    default_seasonal_period: int = 7
    category_seasonal_periods: dict[str, int] = field(default_factory=dict)


def load() -> Settings:
    """Load settings from the YAML config file."""
    with CONFIG_PATH.open() as fh:
        raw = yaml.safe_load(fh)

    return Settings(
        lead_time_days=raw["lead_time_days"],
        reorder_cycle_days=raw["reorder_cycle_days"],
        forecast_horizon_days=raw["forecast_horizon_days"],
        models_to_run=raw["models_to_run"],
        default_seasonal_period=raw.get("default_seasonal_period", 7),
        category_seasonal_periods=raw.get("category_seasonal_periods", {}),
    )
