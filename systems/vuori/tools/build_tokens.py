#!/usr/bin/env python3
"""Check that the written tokens still match the readings file."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
light = tokens["vuori"]["light"]["color"]

expected = {
    "page": "#ffffff",
    "ink": "#333333",
    "muted": "#727272",
    "promo": "#f8f8f8",
    "gifting": "#811b28",
    "button": "#333333",
    "heroButton": "#ffffff",
}
problems = []
for name, value in expected.items():
    got = light[name]["$value"]
    if got.lower() != value:
        problems.append(f"{name}: {got} != {value}")

if readings["viewport"]["innerWidth"] != 1440:
    problems.append("viewport width drifted")
if readings["productPage"]["selectSize"]["clicked"] is not False:
    problems.append("select size was clicked")
if readings["loginWall"]["shopButton"]["clicked"] is not False:
    problems.append("shop was clicked")
if readings["loginWall"]["googleButton"]["clicked"] is not False:
    problems.append("google was clicked")
if readings["footer"]["email"]["submitted"] is not False:
    problems.append("subscribe was submitted")
if readings["typed"] is not False:
    problems.append("something was typed")

if problems:
    raise SystemExit("\n".join(problems))
print("vuori tokens match readings")
