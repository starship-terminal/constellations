#!/usr/bin/env python3
"""Check measured END. tokens against raw/readings.json. Does not recapture the site."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
tokens = json.loads((ROOT / "tokens.json").read_text())

expected = {
    "page": readings["colors"]["page"]["value"],
    "ink": readings["colors"]["ink"]["value"],
    "announcement": readings["colors"]["announcement"]["value"],
    "accent": readings["colors"]["accent"]["value"],
    "border": readings["colors"]["border"]["value"],
}
failed = False
for name, value in expected.items():
    got = tokens["core"]["color"][name]["$value"]
    if got != value:
        print(f"{name}: token {got} != reading {value}")
        failed = True
if readings["viewport"]["innerWidth"] != 1440:
    print("viewport width is not 1440")
    failed = True
if failed:
    sys.exit(1)
print("endclothing tokens match readings")
