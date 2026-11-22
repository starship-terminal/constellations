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

def node(name):
    group, key = name.split(".", 1)
    return tokens["core"][group][key]


failed = False
for name, want in expected.items():
    item = node(name)
    got = item["$value"]
    if name.startswith("color."):
        want = want if want.startswith("#") else (
            "#" + "".join(f"{int(p):02x}" for p in want.replace("rgb(", "").replace(")", "").split(",")[:3])
        )
    elif isinstance(want, (int, float)):
        got = got.removesuffix("px")
        want = str(want)
    if str(got).lower() != str(want).lower():
        print(f"mismatch {name}: token {got!r} reading {want!r}")
        failed = True
    source = item.get("$extensions", {}).get("source")
    if not source:
        print(f"missing source {name}")
        failed = True

if failed:
    sys.exit(1)
print(f"ok {len(expected)} tokens match raw/readings.json")
