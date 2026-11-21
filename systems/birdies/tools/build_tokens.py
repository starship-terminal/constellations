#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
c = readings["computed"]

expect = {
    "core.color.ink": "#000000",
    "core.color.page": "#ffffff",
    "core.color.warm": "#f6f4f1",
    "core.color.ink-soft": "#222222",
    "core.color.line": "#d9d9d9",
    "core.color.gold": "#c9a66b",
    "core.color.on-ink": "#ffffff",
    "core.color.sale": "#e32c2b",
}
got = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.warm": tokens["core"]["color"]["warm"]["$value"],
    "core.color.ink-soft": tokens["core"]["color"]["ink-soft"]["$value"],
    "core.color.line": tokens["core"]["color"]["line"]["$value"],
    "core.color.gold": tokens["core"]["color"]["gold"]["$value"],
    "core.color.on-ink": tokens["core"]["color"]["on-ink"]["$value"],
    "core.color.sale": tokens["core"]["color"]["sale"]["$value"],
}
bad = [k for k in expect if expect[k] != got[k]]
if c["body"]["backgroundColor"] != "rgb(255, 255, 255)":
    bad.append("body background drifted")
if c["addToBag"]["clicked"] is not False:
    bad.append("add to bag must stay unclicked")
if c["heroButton"]["clicked"] is not False:
    bad.append("hero button click was not part of the reading")
if bad:
    print("mismatch:", bad)
    sys.exit(1)
print("tokens match readings")
