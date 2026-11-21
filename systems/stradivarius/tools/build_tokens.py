"""Check that tokens.json still matches the live readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
size = tokens["core"]["size"]

assert color["black"]["$value"] == "#000000"
assert readings["body"]["color"] == "rgb(0, 0, 0)"
assert color["white"]["$value"] == "#ffffff"
assert color["ink"]["$value"] == "#1d1d1d"
assert readings["product"]["h1"]["color"] == "rgb(29, 29, 29)"
assert color["red-dark"]["$value"] == readings["namedColors"]["--colors-red-dark"]
assert size["category-title"]["$value"] == readings["category"]["h1"]["fontSize"]
assert size["product-title"]["$value"] == readings["product"]["h1"]["fontSize"]
assert size["product-price"]["$value"] == readings["product"]["price"]["fontSize"]
assert readings["product"]["addClicked"] is False
assert readings["login"]["submitted"] is False
assert readings["cart"]["addClicked"] is False
print("stradivarius tokens match readings")
