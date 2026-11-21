"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]

assert core["color"]["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert core["color"]["ink"]["$value"] == "#191919"
assert readings["body"]["color"] == "rgb(25, 25, 25)"
assert readings["nav"]["backgroundColor"] == "rgb(25, 25, 25)"
assert core["color"]["sale"]["$value"] == "#ba2b20"
assert readings["salePrice"]["color"] == "rgb(186, 43, 32)"
assert core["color"]["disabled"]["$value"] == "#bdc1c5"
assert readings["disabledButton"]["backgroundColor"] == "rgb(189, 193, 197)"
assert core["size"]["add-to-cart"]["$value"] == readings["addToCart"]["height"]
assert core["size"]["login"]["$value"] == readings["disabledButton"]["height"]
assert core["size"]["nav"]["$value"] == readings["nav"]["height"]
assert core["fontSize"]["hero"]["$value"] == readings["hero"]["fontSize"]
assert core["fontSize"]["account"]["$value"] == readings["accountTitle"]["fontSize"]
print("puma tokens match readings")
