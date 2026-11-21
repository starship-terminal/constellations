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
    "on-ink": "#ffffff",
    "steel": "#3b526c",
    "steel-end": "#5c7fa8",
    "compare": "#808080",
    "card": "#f3f5f9",
}
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if readings["promo"]["backgroundImage"] != "linear-gradient(90deg, rgb(59, 82, 108), rgb(92, 127, 168))":
    bad.append("promo gradient drifted")
if readings["join"]["borderRadius"] != "16px":
    bad.append("join radius drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
