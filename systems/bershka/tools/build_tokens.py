#!/usr/bin/env python3
"""Check systems/bershka/tokens.json against raw/readings.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw/readings.json").read_text())

checks = {
    "core.color.page": (tokens["core"]["color"]["page"]["$value"], "#ffffff"),
    "core.color.ink": (tokens["core"]["color"]["ink"]["$value"], "#000000"),
    "core.color.promo": (tokens["core"]["color"]["promo"]["$value"], "#d72b2b"),
    "core.color.focus": (tokens["core"]["color"]["focus"]["$value"], readings["tokens"]["--bds-color-border-focus"]),
    "core.fontSize.nav": (tokens["core"]["fontSize"]["nav"]["$value"], readings["header"]["nav"]["fontSize"]),
    "core.fontSize.title": (tokens["core"]["fontSize"]["title"]["$value"], readings["category"]["headingFontSize"]),
    "core.size.button": (tokens["core"]["size"]["button"]["$value"], f"{readings['product']['addToBag']['height']}px"),
    "core.radius.none": (tokens["core"]["radius"]["none"]["$value"], readings["product"]["addToBag"]["borderRadius"]),
}

failed = []
for name, (got, want) in checks.items():
    if got != want:
        failed.append(f"{name}: {got} != {want}")

if failed:
    raise SystemExit("\n".join(failed))
print("tokens match readings")
