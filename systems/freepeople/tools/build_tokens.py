#!/usr/bin/env python3
"""Check that tokens.json matches the readings saved with this capture."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]["color"]
assert core["page"]["$value"] == "#FEFBFA"
assert core["promo"]["$value"] == "#EDE6E0"
assert core["ink"]["$value"] == "#252423"
assert core["pink"]["$value"] == "#D52975"
assert readings["computed"]["addToBag"]["clicked"] is False
assert readings["computed"]["promoBarHeight"] == 44
print("freepeople tokens match readings")
