#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]["color"]
expect = {
    "page": "#ffffff",
    "ink": "#000000",
    "cream": "#f9f8f5",
    "promo": "#5b2128",
    "on-promo": "#f9f8f5",
    "muted": "#62605e",
    "atc": "#62605e",
    "shade-pill": "#f8f8f8",
}
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if readings["promo"]["backgroundColor"] != "rgb(91, 33, 40)":
    bad.append("promo fill drifted")
if readings["promo"]["color"] != "rgb(249, 248, 245)":
    bad.append("promo type drifted")
if readings["header"]["backgroundColor"] != "rgb(249, 248, 245)":
    bad.append("header fill drifted")
if readings["header"]["navColor"] != "rgb(91, 33, 40)":
    bad.append("nav color drifted")
if readings["body"]["backgroundColor"] != "rgb(255, 255, 255)":
    bad.append("page fill drifted")
if readings["cta"]["borderRadius"] != "0px":
    bad.append("cta radius drifted")
if readings["cta"]["backgroundColor"] != "rgba(0, 0, 0, 0)":
    bad.append("cta fill drifted")
if readings["product"]["atcBackgroundColor"] != "rgb(98, 96, 94)":
    bad.append("atc fill drifted")
if readings["product"]["atcBorderRadius"] != "0px":
    bad.append("atc radius drifted")
if readings["product"]["atcColor"] != "rgb(255, 255, 255)":
    bad.append("atc type drifted")
if readings["category"]["priceColor"] != "rgb(0, 0, 0)":
    bad.append("price color drifted")
if readings["category"]["subtitleColor"] != "rgb(98, 96, 94)":
    bad.append("subtitle color drifted")
if readings["product"]["shadeToggleBackgroundColor"] != "rgb(248, 248, 248)":
    bad.append("shade pill drifted")
if readings["landedUrl"] != "https://www.meritbeauty.com/":
    bad.append("region drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
