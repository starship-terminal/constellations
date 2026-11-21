"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["ink"]["$value"] == "#000000"
assert readings["utilityBar"]["backgroundColor"] == "rgb(0, 0, 0)"
assert tokens["core"]["color"]["accent"]["$value"] == "#000000"
assert readings["product"]["addToBag"]["backgroundColor"] == "rgb(0, 0, 0)"
assert readings["product"]["addToBag"]["clicked"] is False
assert readings["login"]["email"]["value"] == ""
assert readings["login"]["submit"]["clicked"] is False
assert readings["signup"]["submit"]["clicked"] is False
assert readings["signup"]["captchaSolved"] is False
print("patagonia tokens match readings")
