.PHONY: install format format-check lint test

install:
	pip install -e .[dev]

format:
	black .
	ruff check --fix .

format-check:
	black --check .
	ruff check .

lint:
	ruff check .

test:
	pytest -q
