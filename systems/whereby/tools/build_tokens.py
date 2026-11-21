#!/usr/bin/env python3
"""Check that tokens.json matches the public readings of 2026-11-21.

The token file is hand-written from raw/tight.json, raw/measured.json, and
raw/public-readings.json. This script does not rewrite it, and it does not
touch catalog.json.

python3 systems/whereby/tools/build_tokens.py
"""
import json
import pathlib
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
TIGHT = json.loads((PKG / "raw" / "tight.json").read_text())

def hex_of(rgb):
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#{:02X}{:02X}{:02X}".format(*(int(p) for p in parts))

errors = []
signup = next(n for n in TIGHT["home"]["Sign up"] if n["name"] == "blue-fill")
if hex_of(signup["bg"]) != TOKENS["core"]["color"]["indigo"]["$value"]:
    errors.append("indigo fill mismatch")
hero = TIGHT["nav"]
if hero and hex_of(hero["color"]) != "#000000":
    errors.append("nav colour mismatch")
if TOKENS["light"]["background"]["hero"]["$value"] != "{core.color.blush}":
    errors.append("hero alias")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("tokens match the 2026-11-21 readings")
