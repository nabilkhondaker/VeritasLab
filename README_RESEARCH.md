# Research methodology for VeritasLab

## Motivation

Independent verification of numerical implementations is essential because implementation defects, convention mismatches, and correlated errors can produce plausible but incorrect results.

## Research questions

See README.md section on research questions.

## Hypotheses

- Independent analytic references detect defects that cross-implementation agreement misses.
- Observed convergence order is a sensitive indicator of incorrect discretization or boundary treatment.
- Explicit recording of seeds, versions, and environment metadata enables tolerance-based reproduction.

## Results actually produced

The smoke experiment (`scripts/validation/run_smoke.py`) was executed. Results are in `reports/examples/smoke_results.json`. The correct solver shows decreasing error; the faulty boundary-skipping solver does not and exhibits large boundary residuals.

## Open research questions

How to automatically quantify reference uncertainty for non-analytic problems, and how to extend the framework to nonlinear conservation laws without silently changing problem assumptions.
