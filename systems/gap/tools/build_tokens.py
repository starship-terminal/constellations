"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["ink"]["$value"] == "#000000"
assert readings["universalBar"]["backgroundColor"] == "rgb(0, 0, 0)"
assert tokens["core"]["color"]["accent"]["$value"] == "#031ba1"
assert readings["product"]["addToBag"]["backgroundColor"] == "rgb(3, 27, 161)"
assert readings["product"]["addToBag"]["clicked"] is False
assert readings["login"]["email"]["value"] == ""
assert readings["login"]["continue"]["clicked"] is False
print("gap tokens match readings")
