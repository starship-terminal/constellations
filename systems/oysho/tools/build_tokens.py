#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

checks = {
    "core.color.page": (tokens["core"]["color"]["page"]["$value"], "#fefefe"),
    "core.color.ink": (tokens["core"]["color"]["ink"]["$value"], "#000000"),
    "core.color.on-ink": (tokens["core"]["color"]["on-ink"]["$value"], "#f5f4f1"),
    "core.color.muted": (tokens["core"]["color"]["muted"]["$value"], "#3d3d3d"),
    "core.size.button": (tokens["core"]["size"]["button"]["$value"], "56px"),
    "core.radius.none": (tokens["core"]["radius"]["none"]["$value"], "0px"),
    "readings.page": (readings["body"]["backgroundColor"], "rgb(254, 254, 254)"),
    "readings.add": (readings["product"]["addToBasket"]["backgroundColor"], "rgb(0, 0, 0)"),
    "readings.add.height": (readings["product"]["addToBasket"]["height"], 56),
}

failed = 0
for name, (got, want) in checks.items():
    if got != want:
        print(f"mismatch {name}: {got!r} != {want!r}")
        failed += 1
if failed:
    sys.exit(1)
print("tokens match readings")
