#!/usr/bin/env python3
"""Check systems/coros colour tokens against raw/readings.json."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expected = {
    "page": readings["homepage"]["bodyBg"],
    "promo": readings["homepage"]["promo"]["bg"],
    "on-promo": readings["homepage"]["promo"]["color"],
    "ink": readings["homepage"]["products"]["color"],
    "near-black": readings["product"]["buySticky"]["bg"],
    "buy-ink": readings["product"]["buySticky"]["color"],
}


def rgb_to_hex(value):
    inner = value[value.find("(") + 1 : value.find(")")]
    parts = [int(float(p)) for p in inner.split(",")[:3]]
    return "#{:02x}{:02x}{:02x}".format(*parts)


failed = False
for name, raw in expected.items():
    got = tokens["core"]["color"][name]["$value"]
    want = rgb_to_hex(raw)
    if got != want:
        print(f"{name}: token {got} readings {want}")
        failed = True

if failed:
    sys.exit(1)
print("coros colour tokens match readings")
