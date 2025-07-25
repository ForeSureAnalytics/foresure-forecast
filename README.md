# ForeSure-Forecast

> A scalable forecasting engine built for small business reality — start simple, layer complexity, and let the data speak.

---

## Table of Contents

- [Overview](#overview)
- [Core Principles](#core-principles)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Forecasting Logic](#forecasting-logic)
- [Modules & Inputs](#modules--inputs)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

**ForeSure-Forecast** is a flexible forecasting engine designed to meet small business owners where they are — starting with just historical sales and expanding as cleaner, richer data becomes available.

Each forecasting run:
- Tests **all applicable models** based on available inputs
- Scores each model for **historical accuracy**
- Returns a ranked output per SKU so you can choose the best-performing method

Whether you're running a Shopify store or a warehouse-backed brand, ForeSure-Forecast grows with you.

---

## Core Principles

- **Start Minimal**: Requires only SKU and historical sales
- **Scale Logically**: Inventory, lead times, seasonality, and supplier behavior can be toggled in
- **Run Everything**: When more models are unlocked, all prior models are still executed
- **Trust Data, Not Assumptions**: Best-fit model is chosen based on past performance, not guesswork

---

## Features

- ✅ Plug-and-play with CSVs or backend data sources
- 📈 Supports SES, DES, TES, and modular extensions
- 🔁 Auto-tunes smoothing constants for each model via grid search
- 🧠 SKU-level ranking of models by forecast accuracy
- 🧮 Optionally incorporates inventory, lead times, and supplier constraints

---

## License

This project is currently licensed under the **MIT License** — see [`LICENSE.md`](./LICENSE.md) for details.

> ⚖️ **License Note**: ForeSure-Forecast is released under the permissive MIT License to encourage adoption and collaboration. We may consider upgrading to the Apache 2.0 License in the future to introduce additional legal protections, particularly around patent use. Any such change would only apply to future versions, and all previously released versions will remain under MIT.

---

## Getting Started

```bash
# Clone this repository
git clone https://github.com/yourusername/ForeSure-Forecast.git
cd ForeSure-Forecast

# (Recommended) Create a virtual environment
conda create -n forecast_env python=3.11
conda activate forecast_env

# Install dependencies
pip install -r requirements.txt

# Run your first forecast
python forecast_engine.py --sales ./data/sales_history.csv
