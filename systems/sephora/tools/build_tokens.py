#!/usr/bin/env python3
"""Check Sephora tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.promo": readings["promo"]["backgroundColor"],
    "core.color.on-ink": readings["promo"]["color"],
    "core.color.nav": readings["nav"]["backgroundColor"],
    "core.color.search": readings["search"]["backgroundColor"],
    "core.color.bag": readings["product"]["bag"]["backgroundColor"],
}

want_hex = {
    "core.color.ink": "#000000",
    "core.color.page": "#ffffff",
    "core.color.promo": "#510282",
    "core.color.on-ink": "#ffffff",
    "core.color.nav": "#000000",
    "core.color.search": "#f6f6f8",
    "core.color.bag": "#cf112c",
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.promo": tokens["core"]["color"]["promo"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
    "core.color.nav": tokens["core"]["color"]["nav"]["$value"],
    "core.color.search": tokens["core"]["color"]["search"]["$value"],
    "core.color.bag": tokens["core"]["color"]["bag"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

font = readings["body"]["fontFamily"]
if "helvetica neue" not in font:
    print("mismatch font", font)
    failed = True
if "Helvetica Neue" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True

if readings["product"]["bag"]["borderRadius"] != "99999px":
    print("mismatch bag radius", readings["product"]["bag"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["pill"]["$value"] != "9999px":
    print("mismatch pill token")
    failed = True
if readings["search"]["borderRadius"] != "9999px":
    print("mismatch search radius")
    failed = True

if failed:
    sys.exit(1)
print("sephora tokens match raw/readings.json")
