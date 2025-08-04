import pandas as pd

from foresure_forecast.preprocessing.clean_demand import clean_demand
from foresure_forecast.config.loader import Settings


def test_clean_demand():
    df = pd.DataFrame({"qty_sold": [1, None]})
    cfg = Settings(1, 1, 1, ["SES"])
    cleaned = clean_demand(df, cfg)
    assert cleaned["qty_sold"].isna().sum() == 0
