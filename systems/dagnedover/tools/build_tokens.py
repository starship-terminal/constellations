"""Check that tokens.json still matches the public-page readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
assert color["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert color["ink"]["$value"] == "#333333"
assert readings["addToBag"]["backgroundColor"] == "rgb(51, 51, 51)"
assert color["orange"]["$value"] == "#ff3600"
assert readings["promoHome"]["backgroundColor"] == "rgb(255, 54, 0)"
assert color["lime"]["$value"] == "#edff2c"
assert readings["heroPill"]["backgroundColor"] == "rgb(237, 255, 44)"
assert tokens["core"]["size"]["add-to-bag"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["radius"]["pill"]["$value"] == readings["addToBag"]["borderRadius"]
print("dagnedover tokens match readings")
