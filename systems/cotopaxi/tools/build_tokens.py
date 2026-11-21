#!/usr/bin/env python3
"""Check cotopaxi tokens against the live readings. Does not recapture."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
color = tokens["cotopaxi"]["color"]
assert color["page"]["$value"] == "#ffffff"
assert color["ink"]["$value"] == "#25282a"
assert color["announcement"]["$value"] == "#ebdbff"
assert color["primary"]["$value"] == readings["rootTokens"]["--bs-primary"]
assert readings["viewport"]["innerWidth"] == 1440
assert readings["png"]["width"] == 2880
print("cotopaxi tokens match readings")
