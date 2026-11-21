#!/usr/bin/env python3
"""Check that tokens.json still names the readings this capture measured.

The file is the reading. This script does not invent values. It fails if a
required measured key is missing.
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
required = [
    ("core", "color", "ink"),
    ("core", "color", "page"),
    ("core", "color", "pink"),
    ("core", "font", "display"),
    ("light", "color", "text"),
    ("light", "component", "button-primary", "bg"),
]
missing = []
for path in required:
    node = tokens
    for key in path:
        if not isinstance(node, dict) or key not in node:
            missing.append(".".join(path))
            break
        node = node[key]
    else:
        if "$value" not in node:
            missing.append(".".join(path))
if missing:
    print("missing tokens:", ", ".join(missing))
    sys.exit(1)
print("milk tokens.json has the measured keys")
