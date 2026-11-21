#!/usr/bin/env python3
"""Check Withings tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.promo": readings["announcement"]["backgroundColor"],
    "core.color.on-ink": readings["announcement"]["color"],
    "core.color.nav": readings["header"]["backgroundColor"],
    "core.color.bag": readings["product"]["bag"]["backgroundColor"],
    "core.color.on-bag": readings["product"]["bag"]["color"],
}

want_hex = {
    "core.color.ink": "#0f0f0f",
    "core.color.page": "#ffffff",
    "core.color.promo": "#000000",
    "core.color.on-ink": "#ffffff",
    "core.color.nav": "#ffffff",
    "core.color.bag": "#6784fe",
    "core.color.on-bag": "#ffffff",
}

hexes = {key: tokens["core"]["color"][key.split(".")[-1]]["$value"] for key in want_hex}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

font = readings["body"]["fontFamily"]
if "aeonik" not in font.lower():
    print("mismatch font", font)
    failed = True
if "Aeonik" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True

if readings["product"]["bag"]["borderRadius"] != "16px":
    print("mismatch bag radius", readings["product"]["bag"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["button"]["$value"] != "16px":
    print("mismatch button token")
    failed = True
if readings["announcement"]["borderRadius"] != "6px":
    print("mismatch promo radius")
    failed = True

if failed:
    sys.exit(1)
print("withings tokens match raw/readings.json")
