"""CLI smoke test."""

from veritaslab.cli.main import main
import sys

def test_version(capsys):
    sys.argv = ["veritaslab", "version"]
    try:
        main()
    except SystemExit:
        pass
    # version command prints and may exit; basic import success is sufficient for smoke
