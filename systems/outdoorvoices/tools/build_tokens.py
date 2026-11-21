#!/usr/bin/env python3
"""Check that the written tokens still match the readings file."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
light = tokens["outdoorvoices"]["light"]["color"]

expected = {
    "page": "#ffffff",
    "ink": "#202020",
    "promo": "#2b54ab",
    "button": "#202020",
    "badge": "#6c2932",
    "field": "#efefef",
    "shop": "#5433eb",
}
problems = []
for name, value in expected.items():
    got = light[name]["$value"]
    if got.lower() != value:
        problems.append(f"{name}: {got} != {value}")

if readings["viewport"]["innerWidth"] != 1440:
    problems.append("viewport width drifted")
if readings["productPage"]["addToBag"]["clicked"] is not False:
    problems.append("add to bag was clicked")
if readings["loginWall"]["shopButton"]["clicked"] is not False:
    problems.append("shop was clicked")
if readings["footer"]["email"]["submitted"] is not False:
    problems.append("subscribe was submitted")
if readings["typed"] is not False:
    problems.append("something was typed")

if problems:
    raise SystemExit("\n".join(problems))
print("outdoorvoices tokens match readings")
