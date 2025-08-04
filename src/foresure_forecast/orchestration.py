from __future__ import annotations

from foresure_forecast.config.loader import load as load_cfg
from foresure_forecast.io.load_csv import load_sales
from foresure_forecast.preprocessing.clean_demand import clean_demand
from foresure_forecast.features.build_features import add_features
from foresure_forecast.models import base
from foresure_forecast.evaluation.metrics import rank_models
from foresure_forecast.io.write_forecast import save_forecasts


def run(path_to_sales: str) -> None:
    cfg = load_cfg()
    sales = load_sales(path_to_sales)
    sales = clean_demand(sales, cfg)
    sales = add_features(sales, cfg)

    forecasts = [
        base.MODEL_REGISTRY[name](cfg).fit_forecast(sales) for name in cfg.models_to_run
    ]

    best = rank_models(forecasts)
    save_forecasts(best, cfg)
