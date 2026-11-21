#!/usr/bin/env python3
"""Check the hand-written Devin tokens against the CSS readings.

ADAPTED_FOR = "Devin"
The tokens file is written from measured CSS variables and computed styles.
This script does not rewrite tokens.json. It fails if a named reading disagrees.
"""
ADAPTED_FOR = "Devin"

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
doc = json.loads((ROOT / "raw" / "css-vars.json").read_text())
kept = doc["kept"]


def norm(value):
    return value.replace(" ", "").replace(",", "").lower()


checks = {
    "paper": (kept["--color-bg-page"], "rgb(252252252)"),
    "ink": (kept["--color-text-primary"], "rgb(25"),
    "accent": (kept["--color-accent"], "rgb(49124255)"),
    "font": (kept["--font-body"], "skandia"),
}
failed = 0
for name, (declared, needle) in checks.items():
    if needle not in norm(declared):
        print(f"mismatch {name}: {declared}")
        failed += 1
if tokens["core"]["color"]["paper"]["$value"] != "#fcfcfc":
    print("paper token drifted")
    failed += 1
if tokens["core"]["color"]["accent"]["$value"] != "#317cff":
    print("accent token drifted")
    failed += 1
if tokens["light"]["color"]["action"]["fill"]["$value"] != "{core.color.black}":
    print("action fill drifted")
    failed += 1
if doc["h1"]["size"] != "36px":
    print("home h1 size drifted", doc["h1"]["size"])
    failed += 1
if failed:
    sys.exit(1)
print("devin tokens match the named CSS readings")
