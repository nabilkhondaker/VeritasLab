"""ODE solvers and problems."""

import numpy as np
from typing import Callable, Tuple

def exponential_decay_analytic(t: np.ndarray, y0: float, k: float) -> np.ndarray:
    """Exact solution for y' = -k y."""
    return y0 * np.exp(-k * t)

def euler_step(y: float, dt: float, f: Callable[[float, float], float], t: float) -> float:
    return y + dt * f(t, y)

def rk4_step(y: float, dt: float, f: Callable[[float, float], float], t: float) -> float:
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
    k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2)
    k4 = f(t + dt, y + dt * k3)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

def integrate_ode(f: Callable, y0: float, t_span: Tuple[float, float], dt: float, method: str = "euler") -> Tuple[np.ndarray, np.ndarray]:
    t0, tf = t_span
    n_steps = int(np.ceil((tf - t0) / dt))
    t = np.linspace(t0, tf, n_steps + 1)
    y = np.zeros_like(t)
    y[0] = y0
    stepper = euler_step if method == "euler" else rk4_step
    for i in range(n_steps):
        y[i + 1] = stepper(y[i], t[i + 1] - t[i], f, t[i])
    return t, y
