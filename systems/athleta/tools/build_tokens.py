"""Check that tokens.json still matches the homepage and product readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
size = tokens["core"]["size"]
radius = tokens["core"]["radius"]

assert color["ink"]["$value"] == "#000000"
assert readings["universalBar"]["backgroundColor"] == "rgb(0, 0, 0)"
assert color["ink-soft"]["$value"] == "#0c0c0c"
assert readings["addToBag"]["backgroundColor"] == "rgb(12, 12, 12)"
assert color["promo"]["$value"] == "#2c3c68"
assert readings["promoBar"]["backgroundColor"] == "rgb(44, 60, 104)"
assert color["lime"]["$value"] == "#f4ff7e"
assert readings["display"]["limeSampled"] == "rgb(244, 255, 126)"
assert color["sister"]["$value"] == "#bfbfbf"
assert readings["sisterLink"]["color"] == "rgb(191, 191, 191)"
assert size["add-to-bag"]["$value"] == "44px"
assert readings["addToBag"]["height"] == 44
assert size["shop-now"]["$value"] == "52px"
assert readings["shopNow"]["height"] == 52
assert radius["pill"]["$value"] == readings["shopNow"]["borderRadius"]
assert readings["addToBag"]["clicked"] is False
print("athleta tokens match readings")
