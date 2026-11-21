#!/usr/bin/env python3
"""Check Arc'teryx tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["main"]["backgroundColor"],
    "core.color.promo": readings["promo"]["backgroundColor"],
    "core.color.on-ink": readings["promo"]["color"],
    "core.color.search": readings["search"]["backgroundColor"],
    "core.color.bag": readings["product"]["bag"]["backgroundColor"],
    "core.color.line": readings["cta"]["border"].split()[-1],
}

want_hex = {
    "core.color.ink": "#1a1a1a",
    "core.color.page": "#ffffff",
    "core.color.promo": "#000000",
    "core.color.on-ink": "#ffffff",
    "core.color.search": "#f5f5f5",
    "core.color.bag": "#1a1a1a",
    "core.color.line": "#b2b2b2",
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.promo": tokens["core"]["color"]["promo"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
    "core.color.search": tokens["core"]["color"]["search"]["$value"],
    "core.color.bag": tokens["core"]["color"]["bag"]["$value"],
    "core.color.line": tokens["core"]["color"]["line"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

if "helvetica-now-display" not in readings["body"]["fontFamily"]:
    print("mismatch font", readings["body"]["fontFamily"])
    failed = True
if "helvetica-now-display" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if "elan-itc-pro" not in readings["hero"]["fontFamily"]:
    print("mismatch display", readings["hero"]["fontFamily"])
    failed = True
if tokens["core"]["radius"]["search"]["$value"] != readings["search"]["borderRadius"]:
    print("mismatch search radius")
    failed = True
if tokens["core"]["radius"]["none"]["$value"] != readings["product"]["bag"]["borderRadius"]:
    print("mismatch bag radius")
    failed = True
if readings["product"]["price"]["text"] != "$1,150.00":
    print("mismatch price", readings["product"]["price"]["text"])
    failed = True

if failed:
    sys.exit(1)
print("arcteryx tokens match raw/readings.json")
