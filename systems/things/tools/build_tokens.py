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

back = measure["missing"]["back"]
body = measure["home"]["body"]
search = measure["support"]["search"]

checks = [
    (tokens["core"]["typography"]["button"]["$value"]["fontSize"], back["size"], "button size"),
    (tokens["core"]["typography"]["button"]["$value"]["fontWeight"], back["weight"], "button weight"),
    (tokens["core"]["radius"]["button"]["$value"], back["radius"], "button radius"),
    (tokens["core"]["color"]["button-blue"]["$value"], "#4f91fb", "button blue"),
    (tokens["light"]["page"]["$value"], "#f2f5f7", "page"),
    (tokens["core"]["typography"]["body"]["$value"]["fontSize"], body["size"], "body size"),
    (tokens["core"]["typography"]["search"]["$value"]["fontSize"], search["size"], "search size"),
    (tokens["core"]["radius"]["search"]["$value"], search["radius"], "search radius"),
]
failed = 0
for got, want, label in checks:
    if got != want:
        print(f"mismatch {label}: tokens {got} reading {want}", file=sys.stderr)
        failed += 1
if failed:
    sys.exit(1)
print("tokens match the recorded readings")
