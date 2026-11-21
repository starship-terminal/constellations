#!/usr/bin/env python3
"""Check that tokens.json values match raw/readings.json."""

import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())


def rgb_to_hex(value):
    match = re.fullmatch(r"rgb\((\d+), (\d+), (\d+)\)", value)
    if not match:
        return None
    return "#{:02x}{:02x}{:02x}".format(*(int(n) for n in match.groups()))


checks = [
    (tokens["core"]["color"]["sale"]["$value"], rgb_to_hex(readings["homepage"]["promo"]["background"])),
    (tokens["core"]["color"]["on-sale"]["$value"], rgb_to_hex(readings["homepage"]["promo"]["color"])),
    (tokens["core"]["color"]["ink"]["$value"], rgb_to_hex(readings["homepage"]["department"]["color"])),
    (tokens["core"]["color"]["page"]["$value"], rgb_to_hex(readings["homepage"]["pageBackground"])),
    (tokens["core"]["color"]["muted"]["$value"], rgb_to_hex(readings["product"]["unavailableSize"]["color"])),
    (tokens["core"]["color"]["promo"]["$value"], rgb_to_hex(readings["about"]["promo"]["background"])),
    (tokens["core"]["color"]["tab"]["$value"], rgb_to_hex(readings["about"]["tabSelected"]["background"])),
    (tokens["core"]["typography"]["hero"]["$value"]["fontSize"], readings["homepage"]["heroTitle"]["size"]),
    (tokens["core"]["typography"]["button"]["$value"]["fontSize"], readings["product"]["addToBag"]["size"]),
    (tokens["core"]["space"]["header"]["$value"], f"{readings['homepage']['headerHeight']}px"),
    (tokens["core"]["space"]["add-to-bag"]["$value"], f"{readings['product']['addToBag']['height']}px"),
]

failed = 0
for got, expected in checks:
    if got != expected:
        print(f"mismatch: {got} != {expected}")
        failed += 1

if failed:
    sys.exit(1)
print(f"{len(checks)} checks passed")
