"""Stochastic workload utilities."""

import numpy as np

def seeded_normal_sample(n: int, seed: int, mean: float = 0.0, std: float = 1.0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.normal(mean, std, size=n)
