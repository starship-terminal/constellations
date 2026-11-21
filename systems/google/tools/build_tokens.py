"""Check that tokens.json still matches the measured homepage readings.

Run from the package: python3 tools/build_tokens.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())

assert tokens["core"]["color"]["blue"]["$value"] == "#0b57d0"
assert tokens["core"]["color"]["page"]["$value"] == "#ffffff"
assert tokens["light"]["color"]["action"]["fill"]["$value"] == "{core.color.blue}"
assert raw["computed"]["signIn"]["backgroundColor"] == "rgb(11, 87, 208)"
assert raw["loginWall"]["next"]["backgroundColor"] == "rgb(26, 115, 232)"
print("tokens match raw/css-vars.json")
