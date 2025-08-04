#!/usr/bin/env python3
# src/foresure_forecast/cli.py

from pathlib import Path
import typer
from foresure_forecast.orchestration import run as orchestration_run

app = typer.Typer()

# two levels up from this file is your repo root; adjust if your layout changes
DEFAULT_SALES_PATH = Path(__file__).parents[2] / "data" / "fact_forecast_input.csv"

@app.command()
def run(
    sales: Path = typer.Option(
        DEFAULT_SALES_PATH,
        "--sales", "-s",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help=(
            "Path to fact_forecast_input.csv "
            "(defaults to project_root/data/fact_forecast_input.csv)"
        )
    )
):
    """
    Run the full forecasting pipeline.
    """
    orchestration_run(str(sales))

if __name__ == "__main__":
    app()
