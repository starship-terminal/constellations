#!/usr/bin/env python3
"""Check that tokens.json matches the readings saved with this capture."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]["color"]
assert core["page"]["$value"] == "#FBFBFB"
assert core["ink"]["$value"] == "#121212"
assert core["burgundy"]["$value"] == "#610722"
assert core["live"]["$value"] == "#BA4E41"
assert readings["computed"]["login"]["clicked"] is False
assert readings["computed"]["search"]["submitted"] is False
assert readings["computed"]["header"]["height"] == 116
assert readings["viewport"]["innerWidth"] == 1440
print("poshmark tokens match readings")
