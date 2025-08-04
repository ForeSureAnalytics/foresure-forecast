"""Orchestration utilities for foresure_forecast models."""

# Import models package to trigger model registration.
import foresure_forecast.models  # noqa: F401
from foresure_forecast.models import MODEL_REGISTRY


def get_model(name: str):
    """Retrieve a model class from the registry by name."""
    return MODEL_REGISTRY[name]
