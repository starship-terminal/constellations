#!/usr/bin/env python3
"""Check the hand-written Dia tokens against the CSS readings.

ADAPTED_FOR = "Dia"
The tokens file is written from measured CSS variables and computed styles.
This script does not rewrite tokens.json. It fails if a declared swatch in
raw/css-vars.json disagrees with the token that names it.
"""
ADAPTED_FOR = "Dia"

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
vars_doc = json.loads((ROOT / "raw" / "css-vars.json").read_text())
kept = vars_doc["kept"]

checks = {
    "core.color.paper": ("--background", tokens["core"]["color"]["paper"]["$value"]),
    "core.color.ink": ("--black", tokens["core"]["color"]["ink"]["$value"]),
    "core.color.blue": ("--blue", tokens["core"]["color"]["blue"]["$value"]),
    "core.color.yellow": ("--yellow", tokens["core"]["color"]["yellow"]["$value"]),
    "core.color.white": ("--white", tokens["core"]["color"]["white"]["$value"]),
}
failed = 0
for name, (var, value) in checks.items():
    declared = kept.get(var, "").lower()
    if declared != value.lower():
        print(f"mismatch {name}: token {value} vs {var} {declared}")
        failed += 1
if tokens["light"]["color"]["action"]["fill"]["$value"] != "{core.color.ink}":
    print("action fill drifted")
    failed += 1
if failed:
    sys.exit(1)
print("dia tokens match the named CSS readings")
