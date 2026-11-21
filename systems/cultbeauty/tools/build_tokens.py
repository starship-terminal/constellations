#!/usr/bin/env python3
"""Check Cult Beauty tokens against the live readings. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
readings = json.loads((ROOT / "raw" / "readings.json").read_text())


def hex_of(rgb):
    parts = rgb.removeprefix("rgb(").removesuffix(")").split(",")
    return "#{:02x}{:02x}{:02x}".format(*(int(p.strip()) for p in parts))


pairs = {
    "page": readings["body"]["backgroundColor"],
    "ink": readings["promo"]["backgroundColor"],
    "utility": readings["utility"]["backgroundColor"],
    "search": "rgb(140, 140, 140)",
    "muted": readings["product"]["brand"]["color"],
    "title": readings["product"]["title"]["color"],
    "save": readings["product"]["save"]["color"],
    "panel": readings["heroPanel"]["backgroundColor"],
    "mark": "rgb(35, 31, 32)",
    "on-ink": readings["promo"]["color"],
}

failed = False
for name, rgb in pairs.items():
    got = tokens["core"]["color"][name]["$value"]
    want = hex_of(rgb)
    if got != want:
        print(f"mismatch color {name}: token {got}, reading {want}")
        failed = True

if tokens["core"]["size"]["bag"]["$value"] != readings["product"]["bag"]["height"]:
    print("mismatch bag size")
    failed = True
if tokens["core"]["size"]["promo"]["$value"] != readings["promo"]["height"]:
    print("mismatch promo size")
    failed = True
if tokens["core"]["radius"]["none"]["$value"] != readings["product"]["bag"]["radius"]:
    print("mismatch radius")
    failed = True
if "Inter" not in tokens["core"]["font"]["body"]["$value"]:
    print("mismatch body font")
    failed = True
if readings["product"]["bag"]["clicked"] is not False:
    print("bag was clicked")
    failed = True
if readings["typed"] is not False or readings["submitted"] is not False:
    print("a form was submitted")
    failed = True
if readings["loginExtracted"] != "not-started":
    print("login-extracted was flipped")
    failed = True

if failed:
    raise SystemExit(1)
print("tokens match readings")
