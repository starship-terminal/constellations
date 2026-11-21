#!/usr/bin/env python3
"""Check Boll & Branch tokens against the live readings. Does not recapture the site."""

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
    "core.color.page": readings["body"]["bg"],
    "core.color.promo": readings["promo"]["bg"],
    "core.color.on-ink": readings["promo"]["color"],
    "core.color.header": readings["headerCategory"]["backgroundColor"],
    "core.color.band": readings["band"]["bg"],
    "core.color.sale": readings["product"]["sale"]["color"],
    "core.color.muted": readings["product"]["price"]["color"],
    "core.color.bag": readings["product"]["addToBag"]["bg"],
    "core.color.count": readings["category"]["count"]["color"],
}

want_hex = {
    "core.color.ink": "#1d1d1c",
    "core.color.page": "#f9f8f3",
    "core.color.promo": "#77202e",
    "core.color.on-ink": "#ffffff",
    "core.color.header": "#fffdfb",
    "core.color.band": "#facddd",
    "core.color.sale": "#bd2828",
    "core.color.muted": "#616161",
    "core.color.bag": "#434a57",
    "core.color.count": "#646464",
}

hexes = {key: tokens["core"]["color"][key.split(".")[-1]]["$value"] for key in want_hex}

failed = False
for key, rgb in expect.items():
    if hexes[key] != want_hex[key]:
        print(f"mismatch {key}: reading {rgb_of(rgb)} token {hexes[key]}")
        failed = True
    if rgb_of(rgb) != {
        "#1d1d1c": "rgb(29, 29, 28)",
        "#f9f8f3": "rgb(249, 248, 243)",
        "#77202e": "rgb(119, 32, 46)",
        "#ffffff": "rgb(255, 255, 255)",
        "#fffdfb": "rgb(255, 253, 251)",
        "#facddd": "rgb(250, 205, 221)",
        "#bd2828": "rgb(189, 40, 40)",
        "#616161": "rgb(97, 97, 97)",
        "#434a57": "rgb(67, 74, 87)",
        "#646464": "rgb(100, 100, 100)",
    }[want_hex[key]]:
        print(f"reading drifted {key}: {rgb}")
        failed = True

if "fakt" not in readings["body"]["font"].lower():
    print("mismatch font", readings["body"]["font"])
    failed = True
if "fakt" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch token font")
    failed = True
if "louize" not in tokens["core"]["font"]["display"]["$value"]:
    print("mismatch display font")
    failed = True
if readings["product"]["seeIt"]["radius"] != "999px":
    print("mismatch pill", readings["product"]["seeIt"]["radius"])
    failed = True
if tokens["core"]["radius"]["none"]["$value"] != "0px":
    print("mismatch square radius")
    failed = True
if readings["product"]["addToBag"]["text"] != "ADD TO BAG":
    print("mismatch add label", readings["product"]["addToBag"]["text"])
    failed = True

if failed:
    sys.exit(1)
print("bollandbranch tokens match raw/readings.json")
