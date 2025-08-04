"""Model package that ensures all models are imported for registration."""

# Import models so that they register themselves in MODEL_REGISTRY.
from . import ses  # noqa: F401
from . import des  # noqa: F401
from . import tes  # noqa: F401

__all__ = ["ses", "des", "tes"]
