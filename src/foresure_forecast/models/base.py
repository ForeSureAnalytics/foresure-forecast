"""Model registry utilities."""

MODEL_REGISTRY = {}


def register_model(name):
    """Decorator to register models in :data:`MODEL_REGISTRY`."""
    def decorator(obj):
        MODEL_REGISTRY[name] = obj
        return obj
    return decorator
