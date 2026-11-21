#!/usr/bin/env python3
"""Check Tower 28 tokens against the live readings. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

want = {
    "page": "#ffffff",
    "ink": "#872626",
    "brand": "#d74015",
    "mark": "#ee542f",
    "badge": "#efe3f3",
}

failed = False
for name, hex_value in want.items():
    got = tokens["core"]["color"][name]["$value"]
    if got != hex_value:
        print(f"mismatch color {name}: {got}")
        failed = True

if tokens["core"]["radius"]["button"]["$value"] != "40px":
    print("mismatch radius")
    failed = True
if tokens["core"]["size"]["add"]["$value"] != "44px":
    print("mismatch add size")
    failed = True
if "Scto Grotesk" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch body font")
    failed = True
if "Cooper" not in tokens["core"]["font"]["display"]["$value"]:
    print("mismatch display font")
    failed = True
if readings["home"]["shopNow"]["backgroundColor"] != "rgb(215, 64, 21)":
    print("mismatch shop now", readings["home"]["shopNow"]["backgroundColor"])
    failed = True
if readings["product"]["add"]["backgroundColor"] != "rgb(215, 64, 21)":
    print("mismatch add", readings["product"]["add"]["backgroundColor"])
    failed = True

if failed:
    raise SystemExit(1)
print("tokens match readings")
