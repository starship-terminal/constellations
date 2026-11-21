#!/usr/bin/env python3
"""Check Summer Fridays tokens against the live readings. Does not recapture the site."""

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
    "core.color.header": readings["header"]["interiorParentBg"],
    "core.color.card-button": readings["cardAdd"]["bg"],
    "core.color.bag": readings["product"]["addToBag"]["bg"],
    "core.color.page": readings["header"]["interiorParentBg"],
}

want_hex = {
    "core.color.ink": "#000418",
    "core.color.on-ink": "#ffffff",
    "core.color.promo": "#481f18",
    "core.color.header": "#ffffff",
    "core.color.card-button": "#eeedec",
    "core.color.bag": "#5c7899",
    "core.color.page": "#ffffff",
}

rgb_for = {
    "#000418": "rgb(0, 4, 24)",
    "#ffffff": "rgb(255, 255, 255)",
    "#481f18": "rgb(72, 31, 24)",
    "#eeedec": "rgb(238, 237, 236)",
    "#5c7899": "rgb(92, 120, 153)",
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

if "futura-pt" not in readings["body"]["font"].lower():
    print("mismatch font", readings["body"]["font"])
    failed = True
if "futura-pt" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if readings["product"]["addToBag"]["radius"] != "3px":
    print("mismatch button radius", readings["product"]["addToBag"]["radius"])
    failed = True
if tokens["core"]["radius"]["button"]["$value"] != readings["product"]["addToBag"]["radius"]:
    print("mismatch button token", tokens["core"]["radius"]["button"]["$value"])
    failed = True
if readings["product"]["buyOnce"]["radius"] != "100px":
    print("mismatch pill", readings["product"]["buyOnce"]["radius"])
    failed = True
if tokens["core"]["radius"]["pill"]["$value"] != readings["product"]["buyOnce"]["radius"]:
    print("mismatch pill token", tokens["core"]["radius"]["pill"]["$value"])
    failed = True
if readings["promo"]["pngSample"] != "#481f18":
    print("mismatch promo sample", readings["promo"]["pngSample"])
    failed = True
if readings["footer"]["bg"] != readings["product"]["addToBag"]["bg"]:
    print("footer and bag diverged", readings["footer"]["bg"])
    failed = True

if failed:
    sys.exit(1)
print("tokens match readings")
