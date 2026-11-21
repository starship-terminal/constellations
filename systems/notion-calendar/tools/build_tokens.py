"""Check tokens.json colour values against raw/css-vars.json. Does not rewrite tokens."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())
vars_ = raw["vars"]

checks = {
    "#191918": "--tatami-color-gray-900",
    "#097fe8": "--tatami-color-blue-500",
    "#f9f9f8": "--tatami-color-gray-100",
    "#dfdcd9": "--tatami-color-gray-300",
    "#78736f": "--tatami-color-gray-500",
}
failed = 0
for hex_value, name in checks.items():
    declared = vars_.get(name, "")
    if declared.lower() != hex_value:
        print(f"mismatch {name}: raw {declared!r} token {hex_value}")
        failed += 1
if raw["h1"]["fontSize"] != "64px":
    print("h1 size drifted", raw["h1"]["fontSize"])
    failed += 1
if failed:
    sys.exit(1)
print("tokens match raw readings")
