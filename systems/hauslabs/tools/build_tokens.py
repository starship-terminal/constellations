#!/usr/bin/env python3
"""Check Haus Labs tokens against the live readings. Does not recapture the site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())


def rgb_of(value):
    text = str(value)
    start = text.find("rgb")
    if start < 0:
        return text
    end = text.find(")", start)
    return text[start : end + 1]


expect = {
    "core.color.ink": readings["body"]["color"],
    "core.color.on-ink": readings["promo"]["color"],
    "core.color.promo": readings["promo"]["bg"],
    "core.color.header": readings["header"]["bg"],
    "core.color.page": readings["body"]["bg"],
    "core.color.bag": readings["product"]["addToBag"]["bg"],
    "core.color.notify": readings["notify"]["bg"],
}

want_hex = {
    "core.color.ink": "#000000",
    "core.color.on-ink": "#ffffff",
    "core.color.promo": "#000000",
    "core.color.header": "#ffffff",
    "core.color.page": "#ffffff",
    "core.color.bag": "#000000",
    "core.color.notify": "#424344",
}

rgb_for = {
    "#000000": "rgb(0, 0, 0)",
    "#ffffff": "rgb(255, 255, 255)",
    "#424344": "rgb(66, 67, 68)",
}

hexes = {key: tokens["core"]["color"][key.split(".")[-1]]["$value"] for key in want_hex}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb_of(rgb)} token {hexes[key]}")
        failed = True
    if rgb_of(rgb) != rgb_for[want_hex[key]]:
        print(f"reading drifted {key}: {rgb}")
        failed = True

if "SuisseIntl" not in readings["body"]["font"]:
    print("mismatch font", readings["body"]["font"])
    failed = True
if "SuisseIntl" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if readings["product"]["addToBag"]["radius"] != "0px":
    print("mismatch button radius", readings["product"]["addToBag"]["radius"])
    failed = True
if tokens["core"]["radius"]["button"]["$value"] != readings["product"]["addToBag"]["radius"]:
    print("mismatch button token", tokens["core"]["radius"]["button"]["$value"])
    failed = True
if readings["promo"]["pngSample"] != "#000000":
    print("mismatch promo sample", readings["promo"]["pngSample"])
    failed = True
if tokens["core"]["color"]["hero"]["$value"] != readings["hero"]["bgSample"]:
    print("mismatch hero", tokens["core"]["color"]["hero"]["$value"])
    failed = True
if tokens["core"]["color"]["muted"]["$value"] != readings["hero"]["titleSample"]:
    print("mismatch muted", tokens["core"]["color"]["muted"]["$value"])
    failed = True

if failed:
    sys.exit(1)
print("tokens match readings")
