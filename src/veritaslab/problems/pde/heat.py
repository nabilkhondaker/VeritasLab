"""1D heat equation solvers."""

import numpy as np

def heat_analytic(x: np.ndarray, t: float, L: float = 1.0, alpha: float = 0.1, n_modes: int = 1) -> np.ndarray:
    """Exact solution for u(x,0) = sin(pi x / L), u(0,t)=u(L,t)=0."""
    return np.sin(np.pi * x / L) * np.exp(-alpha * (np.pi / L)**2 * t)

def heat_fd_python(u0: np.ndarray, dx: float, dt: float, alpha: float, n_steps: int, bc: str = "dirichlet") -> np.ndarray:
    """Explicit finite-difference heat equation."""
    n = len(u0)
    u = u0.copy()
    r = alpha * dt / (dx * dx)
    if r > 0.5:
        raise ValueError(f"Unstable CFL: r={r} > 0.5")
    for _ in range(n_steps):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        if bc == "dirichlet":
            u_new[0] = 0.0
            u_new[-1] = 0.0
        u = u_new
    return u
