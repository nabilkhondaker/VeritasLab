"""Reporting utilities."""

from pathlib import Path
import json
from typing import Any, Dict

def write_json_report(data: Dict[str, Any], path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def write_markdown_summary(results: list, path: str | Path) -> None:
    lines = ["# Experiment Summary", ""]
    for r in results:
        lines.append(f"- nx={r.get('nx')}: python L2={r.get('python_l2'):.3e}, faulty L2={r.get('faulty_l2'):.3e}")
    Path(path).write_text("\n".join(lines))
