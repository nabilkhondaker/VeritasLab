"""Public API for VeritasLab."""

from pathlib import Path
from typing import Any, Dict, Optional
import yaml
from pydantic import BaseModel, Field, ValidationError

class ExperimentConfig(BaseModel):
    experiment_id: str
    problem_type: str
    solvers: list[str]
    resolutions: list[float] = Field(default_factory=list)
    seed: int = 42
    tolerances: Dict[str, float] = Field(default_factory=lambda: {"absolute": 1e-6, "relative": 1e-4})
    repetitions: int = 1

def load_config(path: str | Path) -> ExperimentConfig:
    with open(path) as f:
        data = yaml.safe_load(f)
    try:
        return ExperimentConfig(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid experiment configuration: {e}") from e

def run_experiment(config: ExperimentConfig | str | Path, output_dir: Optional[str] = None) -> Dict[str, Any]:
    if isinstance(config, (str, Path)):
        config = load_config(config)
    # Core orchestration will be expanded
    return {"status": "configured", "experiment_id": config.experiment_id, "solvers": config.solvers}
