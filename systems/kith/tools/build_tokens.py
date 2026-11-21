#!/usr/bin/env python3
"""Check that tokens.json still matches raw/readings.json. Does not rewrite tokens."""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
readings = json.loads((root / "raw" / "readings.json").read_text())
tokens = json.loads((root / "tokens.json").read_text())


def hex_of(rgb):
    if rgb.startswith("#"):
        return rgb.lower()
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p) for p in parts))


body = next(r for r in readings["readings"] if r["role"] == "body")
footer = next(r for r in readings["readings"] if r["role"] == "footer")
button = next(r for r in readings["readings"] if r["role"] == "select-a-size")
colors = tokens["core"]["color"]
errors = []
if hex_of(body["color"]) != colors["ink"]["$value"]:
    errors.append("ink")
if hex_of(footer["background"]) != colors["footer"]["$value"]:
    errors.append("footer")
if hex_of(button["background"]) != colors["muted"]["$value"]:
    errors.append("muted")
if tokens["core"]["size"]["header"]["$value"] != "66px":
    errors.append("header")
if errors:
    print("mismatch:", ", ".join(errors))
    sys.exit(1)
print("tokens match readings")
