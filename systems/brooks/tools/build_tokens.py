#!/usr/bin/env python3
"""Check Brooks tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.banner": readings["banner"]["backgroundColor"],
    "core.color.navy": readings["navy"]["backgroundColor"],
    "core.color.on-ink": readings["nav"]["color"],
    "core.color.muted": readings["muted"],
    "core.color.chip-border": "#cdcdcd",
    "core.color.badge-ink": readings["category"]["badge"]["color"],
    "core.color.well": readings["category"]["cardWell"],
}

failed = False
for key, hex_value in expect.items():
    token = tokens
    for part in key.split("."):
        token = token[part]
    if token["$value"] != hex_value:
        print(f"mismatch {key}: reading {hex_value} token {token['$value']}")
        failed = True

font = readings["body"]["fontFamily"]
if "GT America" not in font:
    print("mismatch font", font)
    failed = True
if "GT America" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if "Condensed" not in tokens["core"]["font"]["condensed"]["$value"]:
    print("mismatch condensed font")
    failed = True
if readings["logo"]["fill"] != "#ffffff":
    print("mismatch logo fill", readings["logo"]["fill"])
    failed = True
if readings["search"]["borderRadius"] != "0px":
    print("mismatch search radius", readings["search"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["none"]["$value"] != "0px":
    print("mismatch radius token")
    failed = True
if readings["category"]["promo"]["backgroundColor"] != readings["banner"]["backgroundColor"]:
    print("mismatch promo and banner")
    failed = True

if failed:
    sys.exit(1)
print("brooks tokens match raw/readings.json")
