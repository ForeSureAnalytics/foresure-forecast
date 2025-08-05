# AGENTS.md for ForeSure-Forecast

## Setup
- **Python:** 3.8 or newer
- **Clone & install:**
  ```bash
  git clone https://github.com/ForeSureAnalytics/foresure-forecast.git
  cd foresure-forecast
  pip install -e .
  ```
- **Environment variables:** copy `.env.example` → `.env` and configure:
  - `FORECAST_OUTPUT_DIR` (default: `output/`)
  - `LOG_LEVEL` (default: `INFO`)

## Build & Run
- **Build package:**
  ```bash
  python -m build
  ```
- **Run CLI:**
  ```bash
  python -m foresure_forecast.cli run \
    --sales data/fact_forecast_input.csv \
    --output "$FORECAST_OUTPUT_DIR"
  ```

## Tests
- **Install dev dependencies:**
  ```bash
  make install
  ```
- **Unit tests:**
  ```bash
  pytest tests/ --maxfail=1 --disable-warnings -q
  ```
- **Integration tests:**
  - Place sample CSV in `tests/fixtures/`
  - Run: `pytest tests/integration/`

## Lint & Format
- **Format code:**
  ```bash
  make format    # black . && isort .
  ```
- **Lint:**
  ```bash
  make lint      # flake8 src/foresure_forecast tests/
  ```
- **Type-check:**
  ```bash
  mypy src/foresure_forecast
  ```

## Architecture Overview
- **config/**: default settings & YAML schemas
- **io/**: data loading/writing abstractions
- **preprocessing/**: data cleaning & transforms
- **features/**: feature engineering modules
- **models/**: forecasting classes (SES, DES, TES)
- **evaluation/**: metrics (MAE, MAPE) & plotting
- **orchestration.py**: pipeline runner
- **cli.py**: user-facing commands

## Task Boundaries
- **Safe:** refactor pure functions, add tests, fix lint issues in `src/` or `tests/`
- **Needs approval:** dependency upgrades, CI workflow changes, schema migrations
- **Prohibited:** altering `LICENSE.md`, rotating secrets, modifying `.env.example` without review

## File Scope
- **Editable:** `src/`, `tests/`, `Makefile`, `pyproject.toml`, `README.md`
- **Do not touch:** `.github/workflows/ci.yml`, `LICENSE.md`, large data files

## CI/CD
- **Local check:**
  ```bash
  make format --check && make lint && pytest
  ```
- **Pipeline:** runs format check, lint, then tests under GitHub Actions
- **Coverage:** target ≥ 80%; configure `coverage` in CI to `--fail-under=80`

## PR Guidance
- **Branch naming:** `feat/<short-desc>` or `fix/<short-desc>`
- **Commit messages:** follow Conventional Commits
- **Checklist:** all checks pass, tests added, descriptive PR title & description

## Security & Secrets
- Never commit secrets. Use `.env` + `.env.example`
- Sensitive paths: `.env`, private keys, API tokens

## Troubleshooting
- **Tests fail:** ensure `tests/fixtures/sample_sales.csv` exists or skip integration tests
- **Lint errors:** run `make format` then `make lint`
- **Type errors:** run `mypy src/` to diagnose

## Contacts
- **Maintainer:** Douglas Davis (<doug@example.com>)
