#!/usr/bin/env python3
"""Check Strava tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.page": readings["home"]["body"]["backgroundColor"],
    "core.color.ink": readings["home"]["h1"]["color"],
    "core.color.orange": readings["home"]["emailButton"]["backgroundColor"],
    "core.color.on-orange": readings["home"]["emailButton"]["color"],
    "core.color.ink-soft": readings["home"]["loginButton"]["color"],
    "core.color.google": readings["home"]["googleButton"]["backgroundColor"],
    "core.color.footer": readings["home"]["footer"]["backgroundColor"],
    "core.color.muted": readings["features"]["bodyColor"],
}

want_hex = {
    "core.color.page": "#ffffff",
    "core.color.ink": "#000000",
    "core.color.orange": "#fc5200",
    "core.color.on-orange": "#ffffff",
    "core.color.ink-soft": "#21211f",
    "core.color.google": "#fafafa",
    "core.color.footer": "#f9f8f5",
    "core.color.muted": "#666666",
}

want_rgb = {
    "core.color.page": "rgb(255, 255, 255)",
    "core.color.ink": "rgb(0, 0, 0)",
    "core.color.orange": "rgb(252, 82, 0)",
    "core.color.on-orange": "rgb(255, 255, 255)",
    "core.color.ink-soft": "rgb(33, 33, 31)",
    "core.color.google": "rgb(250, 250, 250)",
    "core.color.footer": "rgb(249, 248, 245)",
    "core.color.muted": "rgb(102, 102, 102)",
}

hexes = {
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.orange": tokens["core"]["color"]["orange"]["$value"],
    "core.color.on-orange": tokens["core"]["color"]["on-orange"]["$value"],
    "core.color.ink-soft": tokens["core"]["color"]["ink-soft"]["$value"],
    "core.color.google": tokens["core"]["color"]["google"]["$value"],
    "core.color.footer": tokens["core"]["color"]["footer"]["$value"],
    "core.color.muted": tokens["core"]["color"]["muted"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if rgb != want_rgb[key] or hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

if readings["home"]["customProperties"]["--color-coreo3"] != "#fc5200":
    print("mismatch --color-coreo3")
    failed = True

if "Boathouse" not in readings["home"]["body"]["fontFamily"]:
    print("mismatch font", readings["home"]["body"]["fontFamily"])
    failed = True

if readings["home"]["emailButton"]["borderRadius"] != "4px":
    print("mismatch signup radius")
    failed = True

if readings["features"]["cta"]["backgroundColor"] != "rgb(252, 82, 0)":
    print("mismatch features cta")
    failed = True

if failed:
    sys.exit(1)
print("strava tokens match raw/readings.json")
