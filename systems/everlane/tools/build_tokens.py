#!/usr/bin/env python3
"""Check that the written tokens still match the readings file."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
light = tokens["everlane"]["light"]["color"]

expected = {
    "page": "#ffffff",
    "ink": "#000000",
    "sale": "#d0021b",
    "button": "#262626",
    "announcement": "#c8c0b8",
    "shop": "#5433eb",
}
problems = []
for name, value in expected.items():
    got = light[name]["$value"]
    if got.lower() != value:
        problems.append(f"{name}: {got} != {value}")

if readings["viewport"]["innerWidth"] != 1440:
    problems.append("viewport width drifted")
if readings["product"]["soldOut"]["clicked"] is not False:
    problems.append("sold out was clicked")
if readings["loginWall"]["shopButton"]["clicked"] is not False:
    problems.append("shop was clicked")

if problems:
    raise SystemExit("\n".join(problems))
print("everlane tokens match readings")
