"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["page"]["$value"] == "#000000"
assert readings["body"]["backgroundColor"] == "rgb(0, 0, 0)"
assert tokens["core"]["color"]["text"]["$value"] == "#f2f2f2"
assert readings["body"]["color"] == "rgb(242, 242, 242)"
assert tokens["core"]["color"]["brand"]["$value"] == "#e50010"
assert readings["logoFill"] == "#E50010"
assert tokens["core"]["color"]["button"]["$value"] == "#f2f2f2"
assert readings["addToBag"]["backgroundColor"] == "rgb(242, 242, 242)"
assert readings["login"]["continueBackground"] == "rgb(242, 242, 242)"
assert tokens["core"]["size"]["button"]["$value"] == "56px"
print("hm tokens match readings")
