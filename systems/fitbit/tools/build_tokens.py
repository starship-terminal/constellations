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
    "page": "#f9f9f9",
    "surface": "#ffffff",
    "ink": "#191c1d",
    "promo": "#050505",
    "on-promo": "#ffffff",
    "primary": "#0b57d0",
    "primary-ink": "#0842a0",
    "primary-soft": "#d3e3fd",
    "save": "#beefbb",
    "save-ink": "#00522c",
    "stage": "#e6ebe5",
    "chip": "#eff1f2",
}
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if readings["promo"]["backgroundColor"] != "rgb(5, 5, 5)":
    bad.append("promo fill drifted")
if readings["signIn"]["borderRadius"] != "100px":
    bad.append("sign-in radius drifted")
if readings["buy"]["afterBackgroundColor"] != "rgb(11, 87, 208)":
    bad.append("buy fill drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
