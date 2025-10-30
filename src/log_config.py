import logging
import os

logger = logging.getLogger("utils")
log = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs/utils.log"),
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
