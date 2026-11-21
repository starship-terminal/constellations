#!/usr/bin/env python3
"""Check ink, page, and promo in tokens.json against raw/readings.json.

Only those three colours are compared. Type sizes, radii, and the other
colours are not checked. Does not rewrite tokens."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())
ink = tokens["core"]["color"]["ink"]["$value"].lower()
page = tokens["core"]["color"]["page"]["$value"].lower()
promo = tokens["core"]["color"]["promo"]["$value"].lower()
body = next(r for r in readings["readings"] if r["role"] == "body")
bar = next(r for r in readings["readings"] if r["role"] == "promo bar")


def hex_of(rgb):
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p) for p in parts))


errors = []
if hex_of(body["color"]) != ink:
    errors.append("ink")
if hex_of(body["background"]) != page:
    errors.append("page")
if hex_of(bar["background"]) != promo:
    errors.append("promo")
if errors:
    print("mismatch:", ", ".join(errors))
    sys.exit(1)
print("ink, page, and promo match readings")
