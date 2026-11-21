#!/usr/bin/env python3
"""Check tokens.json against the live readings. Does not recapture the site."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())

expected = {
    "color.ink": readings["body"]["color"],
    "color.page": readings["body"]["background"],
    "color.deepSea": readings["promoBar"]["background"],
    "color.onDeepSea": readings["promoBar"]["type"]["color"],
    "color.muted": readings["search"]["borderBottom"].removeprefix("1px solid "),
    "color.link": readings["department"]["giftGuideColor"],
    "color.chipRest": readings["chipRest"]["background"],
    "font.body": readings["body"]["fontFamily"],
    "font.display": readings["categoryTitle"]["fontFamily"],
    "size.promoBarHeight": readings["promoBar"]["height"],
    "size.searchWidth": readings["search"]["width"],
    "size.addToBagHeight": readings["product"]["addToBag"]["height"],
}

by_name = {item["name"]: item for item in tokens["tokens"]}
failed = False
for name, want in expected.items():
    got = by_name[name]["value"]
    if got != want:
        print(f"mismatch {name}: token {got!r} reading {want!r}")
        failed = True
    source = by_name[name].get("source")
    if not source:
        print(f"missing source {name}")
        failed = True

if failed:
    sys.exit(1)
print(f"ok {len(expected)} tokens match raw/readings.json")
