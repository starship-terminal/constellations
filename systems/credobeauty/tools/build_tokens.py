#!/usr/bin/env python3
"""Check Credo tokens against the live readings. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

want = {
    "page": "#ffffff",
    "ink": "#001922",
    "brand": "#023e55",
    "link": "#0b788e",
    "timer": "#cb4b10",
    "sale": "#c0392b",
}

failed = False
for name, hex_value in want.items():
    got = tokens["core"]["color"][name]["$value"]
    if got != hex_value:
        print(f"mismatch color {name}: {got}")
        failed = True

if tokens["core"]["radius"]["control"]["$value"] != "4px":
    print("mismatch radius")
    failed = True
if tokens["core"]["size"]["bag"]["$value"] != "38px":
    print("mismatch bag size")
    failed = True
if "urw-din" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch body font")
    failed = True
if "Mercury Display" not in tokens["core"]["font"]["display"]["$value"]:
    print("mismatch display font")
    failed = True
if readings["product"]["bag"]["backgroundColor"] != "rgb(2, 62, 85)":
    print("mismatch bag reading", readings["product"]["bag"]["backgroundColor"])
    failed = True
if readings["product"]["bag"]["clicked"] is not False:
    print("bag was clicked")
    failed = True

if failed:
    raise SystemExit(1)
print("tokens match readings")
