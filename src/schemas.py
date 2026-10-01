"""Data models, schemas, and structural definitions for the project.

This module centralizes all Pydantic schemas and Python dataclasses used 
across the application for data validation, settings, and type safety.
"""

from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class ReportConfig:
    input_dir: Path = PROJECT_ROOT / "data"
    log_dir: Path = PROJECT_ROOT / "logs"

    def ensure_directories(self) -> None:
        """Create data and log folder if they do not exist."""
        self.input_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)