"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert tokens["core"]["color"]["ink"]["$value"] == "#333132"
assert readings["header"]["backgroundColor"] == "rgb(51, 49, 50)"
assert readings["addToCart"]["backgroundColor"] == "rgb(51, 49, 50)"
assert tokens["core"]["color"]["quiet"]["$value"] == "#f3f3f3"
assert readings["promoBar"]["backgroundColor"] == "rgb(243, 243, 243)"
assert tokens["core"]["color"]["sale"]["$value"] == "#cc4428"
assert readings["saleLink"]["color"] == "rgb(204, 68, 40)"
assert tokens["core"]["size"]["add-to-cart"]["$value"] == "60px"
assert readings["addToCart"]["height"] == 60
assert tokens["core"]["radius"]["add-to-cart"]["$value"] == readings["addToCart"]["borderRadius"]
print("outdoorresearch tokens match readings")
