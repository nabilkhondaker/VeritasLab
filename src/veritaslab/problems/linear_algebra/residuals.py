"""Linear algebra utilities for residual checks."""

import numpy as np

def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float:
    r = A @ x - b
    return float(np.linalg.norm(r))

def normalized_backward_error(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float:
    num = np.linalg.norm(A @ x - b)
    den = np.linalg.norm(A) * np.linalg.norm(x) + np.linalg.norm(b)
    if den == 0:
        return float("inf") if num > 0 else 0.0
    return float(num / den)
