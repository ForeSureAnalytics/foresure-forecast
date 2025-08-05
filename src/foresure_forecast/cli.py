#!/usr/bin/env python3
from pathlib import Path
import typer
from foresure_forecast.orchestration import run as orchestration_run

app = typer.Typer(add_completion=False)  # no subcommands, just one interface

# Default path is always resolved from your project root
DEFAULT_SALES_PATH = Path.cwd() / "data" / "fact_forecast_input.csv"

@app.callback(
    invoke_without_command=True,
    help="Run the full forecasting pipeline."
)
def main(
    sales: Path = typer.Option(
        DEFAULT_SALES_PATH,
        "--sales", "-s",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="Path to fact_forecast_input.csv"
    )
):
    """
    Load your sales file and run the entire forecasting pipeline.
    """
    orchestration_run(str(sales))

if __name__ == "__main__":
    app()
