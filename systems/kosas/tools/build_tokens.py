#!/usr/bin/env python3
"""Check Kosas colour tokens against raw/readings.json. Does not recapture the site."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expected = {
    "page": readings["colors"]["page"],
    "ink": readings["colors"]["ink"],
    "promo": readings["colors"]["promo"],
    "chip": readings["colors"]["chip"],
    "note": readings["colors"]["note"],
    "button": readings["colors"]["button"],
    "on-button": readings["colors"]["on-button"],
    "accent": readings["colors"]["accent"],
    "accent-25": readings["colors"]["accent-25"],
}

failed = False
for name, want in expected.items():
    got = tokens["core"]["color"][name]["$value"]
    if got.lower() != want.lower():
        print(f"{name}: token {got} != reading {want}")
        failed = True

if failed:
    sys.exit(1)
print("tokens match readings")
