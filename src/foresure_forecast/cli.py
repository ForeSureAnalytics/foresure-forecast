# src/foresure_forecast/cli.py

from __future__ import annotations
from pathlib import Path

import typer
from foresure_forecast import orchestration

app = typer.Typer()

@app.command()
def run(
    sales: Path = typer.Argument(
        Path("data/fact_forecast_input.csv"),
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="Path to your fact_forecast_input CSV"
    )
):
    """
    Run the full forecasting pipeline.
    If you don’t supply --sales, it defaults to data/fact_forecast_input.csv
    """
    orchestration.run(str(sales))

if __name__ == "__main__":
    app()
