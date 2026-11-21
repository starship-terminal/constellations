#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_to_hex(value):
    nums = value[value.find("(") + 1 : value.find(")")].split(",")
    parts = [int(part.strip()) for part in nums[:3]]
    return "#{:02x}{:02x}{:02x}".format(*parts)


core = tokens["core"]["color"]
expect = {
    "page": rgb_to_hex(readings["page"]),
    "ink": rgb_to_hex(readings["ink"]),
    "ship": rgb_to_hex(readings["ship"]["backgroundColor"]),
    "on-ink": rgb_to_hex(readings["hero"]["color"]),
    "brand": rgb_to_hex(readings["shop"]["backgroundColor"]),
    "graphite": rgb_to_hex(readings["productTitle"]["color"]),
    "card-rule": rgb_to_hex(readings["card"]["border"]),
    "footer": rgb_to_hex(readings["footer"]["backgroundColor"]),
}
bad = []
for name, hex_value in expect.items():
    got = core[name]["$value"].lower()
    if got != hex_value:
        bad.append(f"{name}: {got} != {hex_value}")
if tokens["core"]["radius"]["control"]["$value"] != readings["shop"]["borderRadius"]:
    bad.append("control radius drifted")
if tokens["core"]["radius"]["card"]["$value"] != readings["card"]["borderRadius"]:
    bad.append("card radius drifted")
if tokens["core"]["size"]["header"]["$value"] != readings["header"]["height"]:
    bad.append("header height drifted")
if tokens["core"]["size"]["ship"]["$value"] != readings["ship"]["height"]:
    bad.append("ship height drifted")
if tokens["core"]["size"]["shop"]["$value"] != readings["shop"]["height"]:
    bad.append("shop height drifted")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print("tokens match readings")
