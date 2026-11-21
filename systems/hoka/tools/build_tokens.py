#!/usr/bin/env python3
"""Check Hoka tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.page": readings["body"]["backgroundColor"],
    "core.color.utility": readings["utility"]["backgroundColor"],
    "core.color.on-ink": readings["utility"]["color"],
    "core.color.mark": readings["logo"]["fill"],
    "core.color.muted": readings["category"]["was"]["color"],
    "core.color.sale": readings["category"]["off"]["color"],
    "core.color.ask": readings["ask"]["backgroundColor"],
}

failed = False
for key, rgb in expect.items():
    parts = key.split(".")
    token = tokens
    for part in parts:
        token = token[part]
    if token["$value"] != rgb:
        print(f"mismatch {key}: reading {rgb} token {token['$value']}")
        failed = True

font = readings["body"]["fontFamily"]
if "the-future" not in font:
    print("mismatch font", font)
    failed = True
if "the-future" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True

if readings["search"]["borderRadius"] != "52px":
    print("mismatch search radius", readings["search"]["borderRadius"])
    failed = True
if tokens["core"]["radius"]["pill"]["$value"] != "52px":
    print("mismatch pill token")
    failed = True
if readings["shopNow"]["borderRadius"] != "52px":
    print("mismatch shop now radius", readings["shopNow"]["borderRadius"])
    failed = True

if failed:
    sys.exit(1)
print("hoka tokens match raw/readings.json")
