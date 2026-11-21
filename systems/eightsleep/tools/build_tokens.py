#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_to_hex(value):
    parts = value.removeprefix("rgb(").removesuffix(")").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


expect = {
    "page": rgb_to_hex(readings["body"]["backgroundColor"]),
    "ink": rgb_to_hex(readings["body"]["color"]),
    "on-ink": rgb_to_hex(readings["promoEmphasis"]["color"]),
    "gold": rgb_to_hex(readings["promo"]["color"]),
    "hero": rgb_to_hex(readings["hero"]["backgroundColor"]),
    "compare": rgb_to_hex(readings["compare"]["color"]),
    "badge": rgb_to_hex(readings["badge"]["backgroundColor"]),
}
core = tokens["core"]["color"]
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if tokens["core"]["radius"]["button"]["$value"] != readings["shop"]["borderRadius"]:
    bad.append("button radius drifted")
if tokens["core"]["size"]["promo"]["$value"] != readings["promo"]["height"]:
    bad.append("promo height drifted")
if readings["compare"]["textDecoration"] != "line-through":
    bad.append("compare decoration drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
