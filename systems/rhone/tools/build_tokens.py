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
    "core.color.ink": "#1c1519",
    "core.color.page": "#fbf9f9",
    "core.color.courtesy": "#efedea",
    "core.color.line": "#e3dfd9",
    "core.color.olive": "#617259",
}
got = {
    "core.color.ink": tokens["core"]["color"]["ink"]["$value"],
    "core.color.page": tokens["core"]["color"]["page"]["$value"],
    "core.color.courtesy": tokens["core"]["color"]["courtesy"]["$value"],
    "core.color.line": tokens["core"]["color"]["line"]["$value"],
    "core.color.olive": tokens["core"]["color"]["olive"]["$value"],
}
bad = [k for k in expect if expect[k] != got[k]]
if c["body"]["backgroundColor"] != "rgb(251, 249, 249)":
    bad.append("body background drifted")
if c["addToBag"]["clicked"] is not False:
    bad.append("add to bag must stay unclicked")
if bad:
    print("mismatch:", bad)
    sys.exit(1)
print("tokens match readings")
