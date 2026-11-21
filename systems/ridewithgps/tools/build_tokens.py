#!/usr/bin/env python3
"""Check Ride with GPS tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.ink": readings["home"]["h2"]["color"],
    "core.color.white": readings["home"]["getStarted"]["color"],
    "core.color.orange": readings["home"]["getStarted"]["backgroundColor"],
    "core.color.on-orange": readings["home"]["getStarted"]["color"],
    "core.color.nav": readings["home"]["nav"]["backgroundColor"],
    "core.color.yellow": readings["planner"]["see"]["color"],
}

want_hex = {
    "core.color.ink": "#0b1c1c",
    "core.color.white": "#ffffff",
    "core.color.orange": "#fa6400",
    "core.color.on-orange": "#ffffff",
    "core.color.nav": "#0b1c1ccc",
    "core.color.yellow": "#ffd771",
}

want_rgb = {
    "core.color.ink": "rgb(11, 28, 28)",
    "core.color.white": "rgb(255, 255, 255)",
    "core.color.orange": "rgb(250, 100, 0)",
    "core.color.on-orange": "rgb(255, 255, 255)",
    "core.color.nav": "rgba(11, 28, 28, 0.8)",
    "core.color.yellow": "rgb(255, 215, 113)",
}

hexes = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.white": tokens["core"]["color"]["white"]["$value"],
    "core.color.orange": tokens["core"]["color"]["orange"]["$value"],
    "core.color.on-orange": tokens["core"]["color"]["on-orange"]["$value"],
    "core.color.nav": tokens["core"]["color"]["nav"]["$value"],
    "core.color.yellow": tokens["core"]["color"]["yellow"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if rgb != want_rgb[key] or hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

vars_ = readings["home"]["vars"]
if vars_.get("--color-orange") != "#fa6400":
    print("mismatch --color-orange", vars_.get("--color-orange"))
    failed = True
if vars_.get("--color-text") != "#0b1c1c":
    print("mismatch --color-text", vars_.get("--color-text"))
    failed = True
if "aktiv-grotesk" not in readings["home"]["getStarted"]["fontFamily"]:
    print("mismatch font", readings["home"]["getStarted"]["fontFamily"])
    failed = True
if readings["home"]["getStarted"]["borderRadius"] != "3px":
    print("mismatch radius")
    failed = True
if readings["planner"]["plan"]["bg"] != "rgb(250, 100, 0)":
    print("mismatch plan button")
    failed = True
if readings["home"]["metrics"]["innerWidth"] != 1440:
    print("mismatch width")
    failed = True

if failed:
    sys.exit(1)
print("tokens match readings")
