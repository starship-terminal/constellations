#!/usr/bin/env python3
"""Check Peloton tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": (readings["home"]["nav"]["bg"], "#181a1d"),
    "core.color.red": (readings["home"]["promo"]["bg"], "#df1c2f"),
    "core.color.deals": (readings["home"]["deals"]["color"], "#ff5a5a"),
    "core.color.on-ink": (readings["home"]["h1"]["color"], "#ffffff"),
    "core.color.page": (readings["home"]["shopDeals"]["bg"], "#ffffff"),
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.red": tokens["core"]["color"]["red"]["$value"],
    "core.color.deals": tokens["core"]["color"]["deals"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
}

failed = False
for key, (rgb, want) in expect.items():
    if hexes[key] != want:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]} want {want}")
        failed = True

if "Inter" not in readings["home"]["body"]["font"]:
    print("mismatch font", readings["home"]["body"]["font"])
    failed = True

if readings["bike"]["shopNow"]["bg"] != "rgb(223, 28, 47)":
    print("mismatch shop now", readings["bike"]["shopNow"]["bg"])
    failed = True

if readings["home"]["shopDeals"]["radius"] != "28px":
    print("mismatch pill radius", readings["home"]["shopDeals"]["radius"])
    failed = True

if failed:
    sys.exit(1)
print("peloton tokens match raw/readings.json")
