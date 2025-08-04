from pathlib import Path
import csv
import sys

# Ensure project root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import orchestration


def test_run_creates_forecast_file(tmp_path):
    input_csv = Path("data/fact_forecast_input.csv")
    forecast_file = Path("output/forecasted_quantities.csv")
    summary_file = Path("output/best_model_per_sku.csv")

    backup_forecast = forecast_file.read_bytes() if forecast_file.exists() else None
    backup_summary = summary_file.read_bytes() if summary_file.exists() else None

    if forecast_file.exists():
        forecast_file.unlink()
    if summary_file.exists():
        summary_file.unlink()

    try:
        orchestration.run(input_csv)
        assert forecast_file.exists()
        with forecast_file.open() as f:
            reader = csv.DictReader(f)
            expected_cols = {"sku", "location_id", "forecast_date", "forecast_qty", "forecast_horizon"}
            assert reader.fieldnames is not None
            assert expected_cols.issubset(set(reader.fieldnames))
    finally:
        if forecast_file.exists():
            forecast_file.unlink()
        if summary_file.exists():
            summary_file.unlink()
        if backup_forecast is not None:
            forecast_file.write_bytes(backup_forecast)
        if backup_summary is not None:
            summary_file.write_bytes(backup_summary)
