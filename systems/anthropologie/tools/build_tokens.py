"""Check that tokens.json still matches the public-page readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
assert color["page"]["$value"] == "#fdfdf9"
assert readings["body"]["backgroundColor"] == "rgb(253, 253, 249)"
assert color["ink"]["$value"] == "#26262c"
assert readings["nav"]["color"] == "rgb(38, 38, 44)"
assert color["teal"]["$value"] == "#167a92"
assert readings["utility"]["color"] == "rgb(22, 122, 146)"
assert color["red"]["$value"] == "#c33d3d"
assert readings["holiday"]["color"] == "rgb(195, 61, 61)"
assert color["slate"]["$value"] == "#4b5666"
assert readings["addToBasket"]["backgroundColor"] == "rgb(75, 86, 102)"
assert tokens["core"]["size"]["add-to-basket"]["$value"] == readings["addToBasket"]["height"]
assert tokens["core"]["radius"]["none"]["$value"] == readings["addToBasket"]["borderRadius"]
print("anthropologie tokens match readings")
