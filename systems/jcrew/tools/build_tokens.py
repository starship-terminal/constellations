#!/usr/bin/env python3
"""Check measured J.Crew tokens against raw/readings.json. Does not recapture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

checks = {
    "core.color.ink": (tokens["core"]["color"]["ink"]["$value"], "#000000"),
    "core.color.gifts": (tokens["core"]["color"]["gifts"]["$value"], "#d0021b"),
    "core.color.story": (tokens["core"]["color"]["story"]["$value"], "#294691"),
    "core.color.footer": (tokens["core"]["color"]["footer"]["$value"], "#f0f1f2"),
    "core.size.announcement": (tokens["core"]["size"]["announcement"]["$value"], "55px"),
    "core.radius.search": (tokens["core"]["radius"]["search"]["$value"], "70px"),
    "core.radius.button": (tokens["core"]["radius"]["button"]["$value"], "0px"),
}
failed = []
for name, (got, want) in checks.items():
    if got != want:
        failed.append(f"{name}: {got} != {want}")

if readings["viewport"]["innerWidth"] != 1440:
    failed.append("viewport width")
if readings["product"]["addToBag"]["clicked"] is not False:
    failed.append("add to bag was clicked")

if failed:
    raise SystemExit("\n".join(failed))
print("tokens match readings")
