import logging

logger = logging.getLogger("foresure")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

__all__ = ["logger"]

# Import these so their top‐level registration runs
from .ses import SESModel
from .des import DESModel
from .tes import TESModel
