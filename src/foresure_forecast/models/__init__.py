# src/foresure_forecast/models/__init__.py

# Import the registry and BaseModel so modules can see it
from .base import BaseModel, MODEL_REGISTRY

# Import each model class so its top‐level registration code runs
from .ses import SESModel
from .des import DESModel
from .tes import TESModel

# (Optionally) expose them on the package level
__all__ = ["SESModel", "DESModel", "TESModel", "BaseModel", "MODEL_REGISTRY"]
