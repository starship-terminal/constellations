#!/usr/bin/env python3
"""Check that tokens.json still matches the 2026-11-22 readings.

This capture did not rewrite catalog.json. The token file is hand-written
from raw/measure.json and from pixels sampled before quantize. Running this
script confirms those values are still the ones in tokens.json. It does not
fetch the site again.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
measure = json.loads((ROOT / "raw" / "measure.json").read_text())

checks = [
    (tokens["core"]["typography"]["h1"]["$value"]["fontSize"], measure["h1"]["size"], "h1 size"),
    (tokens["core"]["typography"]["button"]["$value"]["fontSize"], measure["download"]["size"], "button size"),
    (tokens["core"]["radius"]["button"]["$value"], measure["download"]["radius"], "button radius"),
    (tokens["dark"]["page"]["$value"], "#141519", "dark page"),
]
failed = 0
for got, want, label in checks:
    if got != want:
        print(f"mismatch {label}: tokens {got} reading {want}", file=sys.stderr)
        failed += 1
if failed:
    sys.exit(1)
print("tokens match the recorded readings")
