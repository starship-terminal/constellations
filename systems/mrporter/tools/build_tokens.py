#!/usr/bin/env python3
"""Check that tokens.json matches the readings written on 2026-11-22."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())

checks = [
    (tokens["core"]["color"]["ink"]["$value"], "#000000"),
    (tokens["core"]["color"]["page"]["$value"], "#ffffff"),
    (tokens["core"]["color"]["promo"]["$value"], "#cbcbcb"),
    (tokens["core"]["color"]["muted"]["$value"], "#656565"),
    (tokens["core"]["radius"]["control"]["$value"], "2px"),
    (tokens["core"]["space"]["promo"]["$value"], "32px"),
    (readings["addToBag"]["background"], "rgb(0, 0, 0)"),
    (readings["viewport"]["innerWidth"], 1440),
]
failed = [pair for pair in checks if pair[0] != pair[1]]
if failed:
    print("mismatch", failed)
    sys.exit(1)
print("tokens match readings")
