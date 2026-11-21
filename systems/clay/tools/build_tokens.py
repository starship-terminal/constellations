#!/usr/bin/env python3
"""Check the hand-written Clay tokens against the CSS readings.

ADAPTED_FOR = "Clay"
The tokens file is written from measured CSS variables and computed styles.
This script does not rewrite tokens.json. It fails if a declared swatch in
raw/css-vars.json disagrees with the token that names it.
"""
ADAPTED_FOR = "Clay"

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
vars_doc = json.loads((ROOT / "raw" / "css-vars.json").read_text())
kept = vars_doc["kept"]

checks = {
    "core.color.paper": ("--loam---web-library---colors--background", tokens["core"]["color"]["paper"]["$value"]),
    "core.color.ink": ("--_swatches---color--black", tokens["core"]["color"]["ink"]["$value"]),
    "core.color.blueberry.500": ("--_swatches---color--blueberry-500", tokens["core"]["color"]["blueberry"]["500"]["$value"]),
    "core.color.oat.100": ("--_swatches---color--oat-100", tokens["core"]["color"]["oat"]["100"]["$value"]),
}
failed = 0
for name, (var, value) in checks.items():
    declared = kept.get(var, "").lower()
    if declared in ("#000", "#000000") and value.lower() in ("#000", "#000000"):
        continue
    if declared != value.lower():
        print(f"mismatch {name}: token {value} vs {var} {declared}")
        failed += 1
if tokens["light"]["color"]["action"]["fill"]["$value"] != "#000000":
    print("nav trial fill drifted")
    failed += 1
if failed:
    sys.exit(1)
print("clay tokens match the named CSS readings")
