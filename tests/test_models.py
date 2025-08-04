import pandas as pd

from foresure_forecast.config.loader import Settings
from foresure_forecast.models.ses import SESModel
from foresure_forecast.models.des import DESModel
from foresure_forecast.models.tes import TESModel


def load_df():
    return pd.read_csv("tests/fixtures/sales.csv", parse_dates=["day_key"])


def test_ses_model_forecast():
    df = load_df()
    cfg = Settings(14, 30, 3, ["SES"])
    result = SESModel(cfg).fit_forecast(df)
    assert len(result["forecast"]) == 3


def test_des_model_forecast():
    df = load_df()
    cfg = Settings(14, 30, 2, ["DES"])
    result = DESModel(cfg).fit_forecast(df)
    assert len(result["forecast"]) == 2


def test_tes_model_forecast():
    df = load_df()
    cfg = Settings(14, 30, 4, ["TES"])
    result = TESModel(cfg).fit_forecast(df)
    assert len(result["forecast"]) == 4
