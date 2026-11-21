"""Check that tokens.json still matches the signed-out readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
assert color["text"]["$value"] == "#000000"
assert readings["body"]["color"] == "rgb(0, 0, 0)"
assert color["red"]["$value"] == "#ee0000"
assert readings["promoBar"]["backgroundColor"] == "rgb(238, 0, 0)"
assert readings["sale"]["color"] == "rgb(238, 0, 0)"
assert color["ink"]["$value"] == "#000000"
assert readings["loginButton"]["backgroundColor"] == "rgb(0, 0, 0)"
assert color["field-border"]["$value"] == "#1b1b1b"
assert readings["loginField"]["borderColor"] == "rgb(27, 27, 27)"
assert tokens["core"]["radius"]["pill"]["$value"] == "999px"
assert readings["loginButton"]["borderRadius"] == "999px"
assert readings["viewport"]["innerWidth"] == 1440
print("uniqlo tokens match readings")
