# Architecture

VeritasLab separates configuration validation, workload generation, solver execution, independent reference evaluation, numerical analysis, storage, and report generation.

Adapters normalize input construction and output extraction so that Python functions, classes, and optional native kernels can be compared under the same protocol.
