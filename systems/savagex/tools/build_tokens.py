#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expected = {
    "page": readings["colors"]["page"]["value"],
    "ink": readings["colors"]["ink"]["value"],
    "quiz": readings["colors"]["quiz"]["value"],
    "member": readings["colors"]["member"]["value"],
    "search": readings["colors"]["search"]["value"],
}
failed = False
for name, value in expected.items():
    got = tokens["core"]["color"][name]["$value"]
    if got != value:
        print(f"{name}: token {got} != reading {value}")
        failed = True
if tokens["core"]["font"]["ui"]["$value"] != readings["type"]["ui"]:
    print("ui font mismatch")
    failed = True
if failed:
    sys.exit(1)
print("tokens match readings")
