# ForeSure Forecast

A small, modular forecasting package.

## Installation

```bash
pip install -e .
```

## Running a forecast

Place your sales CSV in `data/` and run:

```bash
python -m foresure_forecast.cli run --sales data/fact_forecast_input.csv
```

Outputs are written to `output/<timestamp>/`.

## Project layout

```
src/foresure_forecast/
  config/
  io/
  preprocessing/
  features/
  models/
  evaluation/
  orchestration.py
  cli.py
```

## Development

```bash
make install
make format
make test
```

## Contributing

Pull requests are welcome. Please run the tests and formatters before submitting.
