"""C++ heat kernel source (compilable with g++)."""

// Simple 1D heat equation explicit step for verification against Python.
// Compile: g++ -shared -fPIC -O3 -o heat_kernel.so heat_kernel.cpp

#include <vector>
#include <cmath>
#include <stdexcept>

extern "C" {
void heat_step_cpp(double* u, int n, double r, int n_steps) {
    if (n < 3) return;
    std::vector<double> u_new(n);
    for (int step = 0; step < n_steps; ++step) {
        for (int i = 1; i < n - 1; ++i) {
            u_new[i] = u[i] + r * (u[i + 1] - 2.0 * u[i] + u[i - 1]);
        }
        u_new[0] = 0.0;
        u_new[n - 1] = 0.0;
        for (int i = 0; i < n; ++i) u[i] = u_new[i];
    }
}
}
