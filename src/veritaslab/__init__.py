"""VeritasLab: Scientific computing verification and benchmarking framework."""

__version__ = "0.1.0"
__author__ = "Nabil Khondaker"

from .api import run_experiment, load_config

__all__ = ["run_experiment", "load_config", "__version__"]
