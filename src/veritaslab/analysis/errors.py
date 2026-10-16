"""Error metrics and analysis."""

import numpy as np
from typing import Dict

def l2_error(approx: np.ndarray, reference: np.ndarray) -> float:
    if approx.shape != reference.shape:
        raise ValueError("Shape mismatch")
    return float(np.sqrt(np.mean((approx - reference)**2)))

def linf_error(approx: np.ndarray, reference: np.ndarray) -> float:
    return float(np.max(np.abs(approx - reference)))

def observed_order(errors: list[float], h_values: list[float]) -> float | None:
    if len(errors) < 2:
        return None
    # Use last two for simplicity
    e1, e2 = errors[-2], errors[-1]
    h1, h2 = h_values[-2], h_values[-1]
    if e1 <= 0 or e2 <= 0 or h1 == h2:
        return None
    return float(np.log(e1 / e2) / np.log(h1 / h2))

def compute_errors(approx: np.ndarray, reference: np.ndarray) -> Dict[str, float]:
    return {
        "l2": l2_error(approx, reference),
        "linf": linf_error(approx, reference),
        "max_abs": float(np.max(np.abs(approx - reference))),
    }
