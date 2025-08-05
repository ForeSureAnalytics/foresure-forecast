# ForeSure-Forecast

A modular, extensible forecasting engine for SKU-level demand predictions. Start with minimal inputs (sales data) and layer on features as data quality improves.

## Features

- Automatic model selection (SES, DES, TES)
- Parameter optimization for smoothing constants
- Modular pipeline: preprocessing, feature extraction, modeling, evaluation
- CLI interface for quick forecasts
- Extensible architecture for adding custom models

## Requirements

- Python 3.8 or newer
- pip

## Installation

```bash
pip install foresure-forecast
```

> **Developer mode**
```bash
git clone https://github.com/ForeSureAnalytics/foresure-forecast.git
cd foresure-forecast
pip install -e .
```

## Quickstart

1. Prepare a CSV with columns: `date`, `sku`, `quantity`.
2. Place it in `data/` (e.g., `data/fact_forecast_input.csv`).
3. Run forecasting:
   ```bash
   python -m foresure_forecast.cli \
     --sales data/fact_forecast_input.csv \
     --output output/
   ```
4. Check `output/<timestamp>/` for:
   - `forecasts.csv`
   - `metrics.json`
   - `plots/`

## Configuration

Defaults are in `src/foresure_forecast/config/default.yml`. To override:

```bash
python -m foresure_forecast.cli run \
  --sales data/fact_forecast_input.csv \
  --config path/to/config.yml
```

### Sample `config.yml`

```yaml
models:
  - SES
  - DES
  - TES
seasonality_periods: [7, 30]
evaluation_metrics: [MAE, MAPE]
```

## Project Layout

```
.
├── data/                      # input CSVs and sample data
├── output/                    # forecast outputs
├── src/foresure_forecast/
│   ├── config/               # default settings and schemas
│   ├── io/                   # data loading and writing
│   ├── preprocessing/        # cleaning and transforms
│   ├── features/             # feature engineering
│   ├── models/               # forecasting implementations
│   ├── evaluation/           # metrics and plotting
│   ├── orchestration.py      # pipeline management
│   └── cli.py                # CLI commands
├── tests/                     # unit and integration tests
├── .github/                   # CI workflows
├── Makefile                   # common developer commands
├── pyproject.toml             # package metadata
└── README.md                  # this file
```

## Development

Install dev dependencies and run tasks:

```bash
make install      # install dev dependencies
make format       # run Black and isort
make lint         # run flake8 and mypy
make test         # run pytest suite
```

## Contributing

We welcome improvements! Please:
1. Fork and create a branch.
2. Write tests for new features or fixes.
3. Run `make format` and `make lint`.
4. Open a PR with a clear description and link issues.
5. Ensure CI checks pass.

For detailed guidelines, see `.github/CONTRIBUTING.md` if present.

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

## Contact

Maintainer: Douglas Davis (<doug@foresureanalytics.com>)  
Repo: https://github.com/ForeSureAnalytics/foresure-forecast