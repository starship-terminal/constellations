#!/usr/bin/env python3
"""Check tokens.json against raw/readings.json. Does not recapture the site."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
readings = json.loads((HERE / "raw" / "readings.json").read_text())

expect = {
    "core.color.page.$value": "#ffffff",
    "core.color.ink.$value": "#222222",
    "core.color.sale.$value": "#d83604",
    "core.color.promo.$value": "#3a8700",
    "core.color.buy.$value": "#222222",
    "core.color.on-buy.$value": "#ffffff",
    "core.font.ui.$value": "Helvetica, Arial, sans-serif",
    "core.size.header.$value": "207px",
    "core.size.search.$value": "45px",
    "core.fontSize.nav.$value": "12px",
}

def get(path):
    node = tokens
    for part in path.split("."):
        node = node[part]
    return node

failed = False
for path, want in expect.items():
    got = get(path)
    if got != want:
        print(f"mismatch {path}: {got!r} != {want!r}", file=sys.stderr)
        failed = True

ink = readings["cssVars"]["--text-dark"]
if ink != "rgb(34, 34, 34)":
    print("readings ink drifted", file=sys.stderr)
    failed = True

if failed:
    sys.exit(1)
print("urbanoutfitters tokens match readings")
