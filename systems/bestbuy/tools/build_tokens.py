"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["header"]["$value"] == "#0046be"
assert readings["headerBar"]["backgroundColor"] == "rgb(0, 70, 190)"
assert tokens["core"]["color"]["tag"]["$value"] == "#fff200"
assert readings["logoFills"][0] == "#fff200"
assert tokens["core"]["color"]["text"]["$value"] == "#040c13"
assert readings["body"]["color"] == "rgb(4, 12, 19)"
assert tokens["core"]["color"]["cart"]["$value"] == "#ffe200"
assert readings["addToCart"]["backgroundColor"] == "rgb(255, 226, 0)"
print("bestbuy tokens match readings")
