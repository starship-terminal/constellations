#!/usr/bin/env python3
"""Check luisaviaroma tokens against the live readings. Does not recapture."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
color = tokens["luisaviaroma"]["color"]
assert color["page"]["$value"] == readings["body"]["backgroundColor"]
assert color["ink"]["$value"] == readings["body"]["color"]
assert color["announcement"]["$value"] == readings["promo"]["backgroundColor"]
assert color["primary"]["$value"] == "#000000"
assert readings["rootTokens"]["--bs-primary"] == "#000"
assert color["button"]["$value"] == readings["product"]["addToBag"]["backgroundColor"]
assert readings["viewport"]["innerWidth"] == 1440
assert readings["png"]["width"] == 2880
print("luisaviaroma tokens match readings")
