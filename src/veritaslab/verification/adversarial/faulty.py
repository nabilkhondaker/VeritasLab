"""Faulty solver fixtures for testing detection of incorrect implementations."""

import numpy as np

def faulty_heat_skip_boundary(u0: np.ndarray, dx: float, dt: float, alpha: float, n_steps: int) -> np.ndarray:
    """Intentionally incorrect: applies interior update and then sets boundaries to an incorrect value."""
    n = len(u0)
    u = u0.copy()
    r = alpha * dt / (dx * dx)
    for _ in range(n_steps):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        # Deliberately incorrect boundary values
        u_new[0] = 0.1
        u_new[-1] = 0.1
        u = u_new
    return u
