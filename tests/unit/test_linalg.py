"""Additional unit tests."""

import numpy as np
from veritaslab.problems.linear_algebra.residuals import residual_norm, normalized_backward_error

def test_residual_zero():
    A = np.eye(2)
    x = np.array([1.0, 2.0])
    b = x.copy()
    assert residual_norm(A, x, b) == 0.0
    assert normalized_backward_error(A, x, b) == 0.0
