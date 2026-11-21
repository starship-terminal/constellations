#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
c = readings["computed"]

expect = {
    "core.color.ink": "#111111",
    "core.color.page": "#ffffff",
    "core.color.ink-soft": "#2b2b2b",
    "core.color.muted": "#656565",
    "core.color.line": "#cbcbcb",
    "core.color.chip-line": "#e5e5e5",
    "core.color.on-ink": "#ffffff",
}
got = {k: tokens["core"]["color"][k.split(".")[-1]]["$value"] for k in expect}
bad = [k for k in expect if expect[k] != got[k]]
if c["header"]["backgroundColor"] != "rgb(17, 17, 17)":
    bad.append("header background drifted")
if c["addToBag"]["clicked"] is not False:
    bad.append("add to bag must stay unclicked")
if c["shopNow"]["clicked"] is not False:
    bad.append("shop now click was not part of the reading")
if c["signUp"]["clicked"] is not False:
    bad.append("sign up must stay unclicked")
if c["email"]["typed"] is not False:
    bad.append("email must stay empty")
if bad:
    print("mismatch:", bad)
    raise SystemExit(1)
print("tokens match readings")
