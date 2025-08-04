"""Orchestrator for forecasting models."""

# Ensure all model modules are imported so their side effects register.
import foresure_forecast.models  # noqa: F401
from foresure_forecast.models.base import MODEL_REGISTRY


def get_model(name: str):
    """Retrieve a model class from the registry by name."""
    return MODEL_REGISTRY[name]


if __name__ == "__main__":
    # Example: list available models
    print("Registered models:", sorted(MODEL_REGISTRY))
