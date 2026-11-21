#!/usr/bin/env python3
"""Check Nordstrom tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": "rgb(25, 26, 27)",
    "core.color.sale": "rgb(184, 0, 9)",
    "core.color.search": "rgb(240, 243, 245)",
    "core.color.price": "rgb(216, 37, 8)",
    "core.color.on-ink": "rgb(255, 255, 255)",
}

got = {
    "core.color.ink": readings["readings"]["body"]["color"],
    "core.color.sale": readings["readings"]["saleBtn"]["color"],
    "core.color.search": readings["readings"]["search"]["bg"],
    "core.color.price": readings["productExtra"]["sale"]["color"],
    "core.color.on-ink": readings["chrome"]["promo"]["color"],
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.sale": tokens["core"]["color"]["sale"]["$value"],
    "core.color.search": tokens["core"]["color"]["search"]["$value"],
    "core.color.price": tokens["core"]["color"]["price"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
}

want_hex = {
    "core.color.ink": "#191a1b",
    "core.color.sale": "#b80009",
    "core.color.search": "#f0f3f5",
    "core.color.price": "#d82508",
    "core.color.on-ink": "#ffffff",
}

failed = False
for key, rgb in expect.items():
    if got[key] != rgb or hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {got[key]} token {hexes[key]}")
        failed = True

font = readings["readings"]["body"]["font"]
if "Brandon Text" not in font:
    print("mismatch font", font)
    failed = True

if readings["product"]["bag"]["radius"] != "4px":
    print("mismatch bag radius", readings["product"]["bag"]["radius"])
    failed = True

if failed:
    sys.exit(1)
print("nordstrom tokens match raw/readings.json")
