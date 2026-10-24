"""Logging configuration for the study planner package."""

import logging
from pathlib import Path

LOG_FILE = Path("study_planner.log")


def get_logger(name: str = "study_planner") -> logging.Logger:
    """Configure and return a logger that writes events to study_planner.log."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger