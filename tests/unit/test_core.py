"""Unit tests for error analysis and solvers."""

import numpy as np
import pytest
from veritaslab.analysis.errors import l2_error, observed_order, compute_errors
from veritaslab.problems.ode.solvers import integrate_ode, exponential_decay_analytic
from veritaslab.problems.pde.heat import heat_fd_python, heat_analytic

def test_l2_error_identical():
    a = np.array([1.0, 2.0, 3.0])
    assert l2_error(a, a) == 0.0

def test_observed_order_first():
    # Euler is first order
    errors = [0.1, 0.05]
    h = [0.1, 0.05]
    order = observed_order(errors, h)
    assert order is not None
    assert abs(order - 1.0) < 0.1

def test_ode_euler_decay():
    def f(t, y): return -1.0 * y
    t, y = integrate_ode(f, 1.0, (0, 1), 0.01, method="euler")
    y_exact = exponential_decay_analytic(t, 1.0, 1.0)
    err = l2_error(y, y_exact)
    assert err < 0.05

def test_heat_stability():
    u0 = np.sin(np.pi * np.linspace(0, 1, 11))
    with pytest.raises(ValueError):
        heat_fd_python(u0, 0.1, 0.1, 1.0, 1)  # unstable
