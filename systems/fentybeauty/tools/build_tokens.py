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
    "ink": "#2d2929",
    "muted": "#666666",
    "promo": "#000000",
    "on-promo": "#ffffff",
    "hero": "#fdcbd4",
    "danger": "#bd0100",
}
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if readings["promo"]["backgroundColor"] != "rgb(0, 0, 0)":
    bad.append("promo fill drifted")
if readings["body"]["color"] != "rgb(45, 41, 41)":
    bad.append("ink drifted")
if readings["cta"]["backgroundColor"] != "rgb(0, 0, 0)":
    bad.append("cta fill drifted")
if readings["cta"]["borderRadius"] != "0px":
    bad.append("cta radius drifted")
if readings["hero"]["backgroundColor"] != "rgb(253, 203, 212)":
    bad.append("hero fill drifted")
if readings["product"]["sale"]["color"] != "rgb(189, 1, 0)":
    bad.append("compare price drifted")
if readings["landedUrl"] != "https://fentybeauty.com/en-sg":
    bad.append("region drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
