from __future__ import annotations

from pathlib import Path
import typer

from foresure_forecast import orchestration

app = typer.Typer()


@app.command()
def run(sales: Path):
    """Run the full forecasting pipeline."""
    orchestration.run(str(sales))


if __name__ == "__main__":
    app()
