"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert tokens["core"]["color"]["ink"]["$value"] == "#0d1012"
assert readings["addToBag"]["backgroundColor"] == "rgb(13, 16, 18)"
assert tokens["core"]["color"]["ocean"]["$value"] == "#004aa2"
assert readings["usp"]["backgroundColor"] == "rgb(0, 74, 162)"
assert tokens["core"]["color"]["sale"]["$value"] == "#dc0428"
assert readings["product"]["struckPriceColor"] == "rgb(220, 4, 40)"
assert tokens["core"]["size"]["add-to-bag"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["radius"]["control"]["$value"] == readings["addToBag"]["borderRadius"]
print("gymshark tokens match readings")
