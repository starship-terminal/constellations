#!/usr/bin/env python3
"""Check Komoot tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expect = {
    "core.color.page": readings["home"]["htmlBg"],
    "core.color.ink": readings["home"]["body"]["color"],
    "core.color.green": readings["home"]["login"]["backgroundColor"],
    "core.color.on-green": readings["home"]["login"]["color"],
    "core.color.footer": readings["home"]["footer"]["backgroundColor"],
    "core.color.orange": readings["home"]["app"]["color"],
    "core.color.orange-wash": readings["home"]["app"]["backgroundColor"],
    "core.color.white": readings["home"]["signup"]["backgroundColor"],
    "core.color.nav-on-photo": readings["home"]["nav"]["color"],
}

want_hex = {
    "core.color.page": "#f5f3ec",
    "core.color.ink": "#1c1a18",
    "core.color.green": "#4f6814",
    "core.color.on-green": "#f5f3ec",
    "core.color.footer": "#212512",
    "core.color.orange": "#ee6b17",
    "core.color.orange-wash": "#fce1d1",
    "core.color.white": "#ffffff",
    "core.color.nav-on-photo": "#faf9f4",
}

want_rgb = {
    "core.color.page": "rgb(245, 243, 236)",
    "core.color.ink": "rgb(28, 26, 24)",
    "core.color.green": "rgb(79, 104, 20)",
    "core.color.on-green": "rgb(245, 243, 236)",
    "core.color.footer": "rgb(33, 37, 18)",
    "core.color.orange": "rgb(238, 107, 23)",
    "core.color.orange-wash": "rgb(252, 225, 209)",
    "core.color.white": "rgb(255, 255, 255)",
    "core.color.nav-on-photo": "rgb(250, 249, 244)",
}

hexes = {
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.green": tokens["core"]["color"]["green"]["$value"],
    "core.color.on-green": tokens["core"]["color"]["on-green"]["$value"],
    "core.color.footer": tokens["core"]["color"]["footer"]["$value"],
    "core.color.orange": tokens["core"]["color"]["orange"]["$value"],
    "core.color.orange-wash": tokens["core"]["color"]["orange-wash"]["$value"],
    "core.color.white": tokens["core"]["color"]["white"]["$value"],
    "core.color.nav-on-photo": tokens["core"]["color"]["nav-on-photo"]["$value"],
}

failed = False
for key, rgb in expect.items():
    if rgb != want_rgb[key] or hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb} token {hexes[key]}")
        failed = True

if readings["home"]["vars"]["--theme-ui-colors-primitives-green-400"] != "#4f6814":
    print("mismatch green-400")
    failed = True

if "Satoshi" not in readings["home"]["body"]["fontFamily"]:
    print("mismatch font", readings["home"]["body"]["fontFamily"])
    failed = True

if readings["home"]["login"]["borderRadius"] != "16px":
    print("mismatch login radius")
    failed = True

if readings["help"]["h2"]["fontSize"] != "36px":
    print("mismatch help heading")
    failed = True

if readings["featuresAccent"]["accent"]["color"] != "rgb(238, 107, 23)":
    print("mismatch features accent")
    failed = True

if failed:
    sys.exit(1)
print("komoot tokens match raw/readings.json")
