"""Check that tokens.json still matches the homepage and product readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
assert color["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert color["text"]["$value"] == "#000000"
assert readings["body"]["color"] == "rgb(0, 0, 0)"
assert color["brand"]["$value"] == "#cf0a2c"
assert readings["logoFill"] == "#cf0a2c"
assert readings["blackFridayLabel"]["color"] == "rgb(207, 10, 44)"
assert color["ink"]["$value"] == "#151415"
assert readings["shopNow"]["backgroundColor"] == "rgb(21, 20, 21)"
assert readings["addToBag"]["backgroundColor"] == "rgb(21, 20, 21)"
assert readings["loginSubmit"]["backgroundColor"] == "rgb(21, 20, 21)"
assert tokens["core"]["size"]["button"]["$value"] == "54px"
assert readings["addToBag"]["height"] == "54px"
assert tokens["core"]["radius"]["button"]["$value"] == "2px"
print("newbalance tokens match readings")
