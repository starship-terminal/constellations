#!/usr/bin/env python3
"""Check therealreal tokens against the live readings. Does not recapture."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
color = tokens["therealreal"]["color"]
assert color["page"]["$value"] == readings["body"]["backgroundColor"]
assert color["ink"]["$value"] == readings["body"]["color"]
assert color["announcement"]["$value"] == readings["promo"]["backgroundColor"]
assert color["announcementText"]["$value"] == readings["promo"]["color"]
assert color["sell"]["$value"] == readings["sell"]["backgroundColor"]
assert color["sellText"]["$value"] == readings["sell"]["color"]
assert color["searchBorder"]["$value"] == "#666666"
assert color["link"]["$value"] == readings["rootTokens"]["--color-teal-link"]
assert color["footer"]["$value"] == readings["footer"]["backgroundColor"]
assert color["footerText"]["$value"] == readings["footerLink"]["color"]
assert readings["rootTokens"]["--color-sell-300"] == "#e6f0a5"
assert readings["viewport"]["innerWidth"] == 1440
assert readings["png"]["width"] == 2880
print("therealreal tokens match readings")
