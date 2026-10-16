"""VeritasLab command-line interface."""

import argparse
import sys
from pathlib import Path
from ..api import load_config, run_experiment

def main():
    parser = argparse.ArgumentParser(prog="veritaslab", description="Scientific computing verification framework")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-problems", help="List available problem families")
    sub.add_parser("list-solvers", help="List registered solvers")

    val = sub.add_parser("validate-config", help="Validate an experiment configuration")
    val.add_argument("config", type=str)

    run = sub.add_parser("run", help="Run an experiment")
    run.add_argument("config", type=str)
    run.add_argument("--output", type=str, default="runs")

    sub.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "list-problems":
        print("Available problems: ode.exponential_decay, ode.harmonic_oscillator, pde.heat_1d, pde.advection_1d, linalg.dense_solve")
    elif args.command == "list-solvers":
        print("Available solvers: python.euler, python.rk4, python.heat_fd, cpp.heat_kernel (when built)")
    elif args.command == "validate-config":
        try:
            cfg = load_config(args.config)
            print(f"Configuration valid: {cfg.experiment_id}")
        except Exception as e:
            print(f"Validation failed: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "run":
        result = run_experiment(args.config, args.output)
        print(f"Experiment {result['experiment_id']} status: {result['status']}")
    elif args.command == "version":
        from .. import __version__
        print(__version__)

if __name__ == "__main__":
    main()
