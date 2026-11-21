"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]

assert core["color"]["page"]["$value"] == "#fdfbf8"
assert readings["body"]["backgroundColor"] == "rgb(253, 251, 248)"
assert core["color"]["ink"]["$value"] == "#000914"
assert readings["body"]["color"] == "rgb(0, 9, 20)"
assert core["color"]["promo"]["$value"] == "#fdf6f0"
assert readings["promo"]["backgroundColor"] == "rgb(253, 246, 240)"
assert core["color"]["burgundy"]["$value"] == "#6f0936"
assert readings["nav"]["color"] == "rgb(111, 9, 54)"
assert readings["productButton"]["backgroundColor"] == "rgb(111, 9, 54)"
assert core["color"]["on-burgundy"]["$value"] == "#ffffff"
assert readings["heroHeading"]["color"] == "rgb(255, 255, 255)"
assert core["fontSize"]["hero"]["$value"] == readings["heroHeading"]["fontSize"]
assert core["fontSize"]["product"]["$value"] == readings["productTitle"]["fontSize"]
assert core["fontSize"]["nav"]["$value"] == readings["nav"]["fontSize"]
assert core["size"]["promo"]["$value"] == readings["promo"]["height"]
assert core["size"]["header"]["$value"] == readings["header"]["height"]
assert core["size"]["button"]["$value"] == readings["productButton"]["height"]
print("rarebeauty tokens match readings")
