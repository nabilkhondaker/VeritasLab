"""End-to-end smoke test and result generation."""

import numpy as np
import json
from pathlib import Path
from veritaslab.problems.pde.heat import heat_fd_python, heat_analytic
from veritaslab.analysis.errors import compute_errors, observed_order
from veritaslab.verification.adversarial.faulty import faulty_heat_skip_boundary

def run_smoke():
    results = []
    L = 1.0
    alpha = 0.1
    T = 0.1
    for nx in [11, 21, 41]:
        dx = L / (nx - 1)
        x = np.linspace(0, L, nx)
        u0 = np.sin(np.pi * x)
        dt = 0.4 * dx * dx / alpha  # stable
        n_steps = max(1, int(T / dt))
        u_py = heat_fd_python(u0, dx, dt, alpha, n_steps)
        u_faulty = faulty_heat_skip_boundary(u0, dx, dt, alpha, n_steps)
        u_ref = heat_analytic(x, T, L, alpha)
        err_py = compute_errors(u_py, u_ref)
        err_faulty = compute_errors(u_faulty, u_ref)
        results.append({
            "nx": nx,
            "dx": dx,
            "python_l2": err_py["l2"],
            "faulty_l2": err_faulty["l2"],
            "faulty_bc_violation": abs(u_faulty[0]) + abs(u_faulty[-1]),
        })
    return results

if __name__ == "__main__":
    res = run_smoke()
    Path("/workspace/artifacts/VeritasLab/reports/examples").mkdir(parents=True, exist_ok=True)
    with open("/workspace/artifacts/VeritasLab/reports/examples/smoke_results.json", "w") as f:
        json.dump(res, f, indent=2)
    print(json.dumps(res, indent=2))
