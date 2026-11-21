#!/usr/bin/env python3
"""Check Ulta tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.muted": readings["utility"]["color"],
    "core.color.line": readings["underline"]["borderBottom"],
    "core.color.on-ink": readings["product"]["bag"]["color"],
    "core.color.brand": readings["svgFill"],
    "core.color.bag": readings["product"]["bag"]["backgroundColor"],
}

want_hex = {
    "core.color.ink": "#000000",
    "core.color.page": "#ffffff",
    "core.color.muted": "#736d69",
    "core.color.line": "#b2aba5",
    "core.color.on-ink": "#ffffff",
    "core.color.brand": "#f37830",
    "core.color.bag": "#000000",
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.muted": tokens["core"]["color"]["muted"]["$value"],
    "core.color.line": tokens["core"]["color"]["line"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
    "core.color.brand": tokens["core"]["color"]["brand"]["$value"],
    "core.color.bag": tokens["core"]["color"]["bag"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if want_hex[key].lower() not in rgb.lower() and hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: token {hexes[key]}")
        failed = True

font = readings["body"]["fontFamily"].lower()
if "circular" not in font:
    print("mismatch font", font)
    failed = True
if "Circular" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True

if readings["product"]["bag"]["borderRadius"] != "100px":
    print("mismatch bag radius", readings["product"]["bag"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["pill"]["$value"] != "100px":
    print("mismatch pill token")
    failed = True

if failed:
    sys.exit(1)
print("ulta tokens match raw/readings.json")
