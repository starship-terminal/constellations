"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["navy"]["$value"] == "#05274c"
assert readings["universalBar"]["backgroundColor"] == "rgb(5, 39, 76)"
assert tokens["core"]["color"]["promo"]["$value"] == "#0b6ab3"
assert readings["promoBar"]["backgroundColor"] == "rgb(11, 106, 179)"
assert readings["product"]["addToBag"]["backgroundColor"] == "rgb(5, 39, 76)"
assert readings["product"]["addToBag"]["clicked"] is False
assert readings["login"]["email"]["value"] == ""
assert readings["login"]["continue"]["clicked"] is False
assert readings["emailField"]["submitted"] is False
print("oldnavy tokens match readings")
