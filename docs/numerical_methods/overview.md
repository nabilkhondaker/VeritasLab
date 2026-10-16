# Numerical methods

## ODE
Explicit Euler (first-order) and classical RK4 (fourth-order) are implemented for scalar ODEs with known analytic solutions.

## PDE
Explicit finite-difference discretization of the one-dimensional heat equation with Dirichlet boundaries. Stability is enforced by checking the CFL condition \( r = \alpha \Delta t / \Delta x^2 \le 1/2 \).
