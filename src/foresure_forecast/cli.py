# src/foresure_forecast/cli.py

from __future__ import annotations
from pathlib import Path

import typer
from foresure_forecast import orchestration

app = typer.Typer()

@app.command()
def run(
    sales: Path = typer.Option(
        Path("data/fact_forecast_input.csv"),
        "--sales", "-s",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="Path to your fact_forecast_input CSV"
    )
):
    orchestration.run(str(sales))
    """
    Run the full forecasting pipeline.
    If you don’t supply --sales, it defaults to data/fact_forecast_input.csv
    """
    orchestration.run(str(sales))

if __name__ == "__main__":
    app()
