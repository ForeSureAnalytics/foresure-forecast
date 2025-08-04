install:
pip install -e .[dev]

format:
black .
ruff --fix .

test:
pytest -q
