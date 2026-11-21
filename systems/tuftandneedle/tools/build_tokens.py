#!/usr/bin/env python3
"""Check measured Tuft & Needle tokens against raw/readings.json."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
raw = json.loads((ROOT / "raw" / "readings.json").read_text())

checks = {
    "core.color.page": raw["computed"]["body"]["backgroundColor"],
    "core.color.ink": raw["computed"]["body"]["color"],
    "core.color.deep": raw["computed"]["toolbar"]["backgroundColor"],
    "core.color.mint": raw["computed"]["heroH1"]["color"],
    "core.color.sand": raw["computed"]["startSaving"]["backgroundColor"],
    "core.color.sale": raw["computed"]["saleNav"]["color"],
    "core.color.price": raw["computed"]["salePrice"]["color"],
    "core.radius.pill": raw["computed"]["addToCart"]["borderRadius"],
    "core.size.button": f"{raw['computed']['addToCart']['height']}px",
}

failed = 0
for path, expected in checks.items():
    node = tokens
    for part in path.split("."):
        node = node[part]
    got = node["$value"]
    if got != expected:
        print(f"mismatch {path}: token {got} reading {expected}")
        failed += 1
    else:
        print(f"ok {path} {got}")

if failed:
    sys.exit(1)
print("tokens match readings")
