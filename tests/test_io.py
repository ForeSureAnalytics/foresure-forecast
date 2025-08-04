from foresure_forecast.io.load_csv import load_sales


def test_load_sales():
    df = load_sales("tests/fixtures/sales.csv")
    assert list(df.columns) == [
        "sku",
        "location_id",
        "category",
        "day_key",
        "qty_sold",
    ]
    assert df.shape[0] == 14
