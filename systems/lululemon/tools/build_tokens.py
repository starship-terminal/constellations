"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["page"]["$value"] == "#fafafa"
assert readings["body"]["backgroundColor"] == "rgb(250, 250, 250)"
assert tokens["core"]["color"]["ink"]["$value"] == "#140f0f"
assert readings["nav"]["linkColor"] == "rgb(20, 15, 15)"
assert tokens["core"]["color"]["quiet"]["$value"] == "#f4f3f2"
assert readings["shopButton"]["backgroundColor"] == "rgb(244, 243, 242)"
assert tokens["core"]["color"]["ink"]["$value"] == "#140f0f"
assert readings["addToBag"]["backgroundColor"] == "rgb(20, 15, 15)"
assert readings["login"]["continueBackground"] == "rgb(20, 15, 15)"
assert tokens["core"]["size"]["button"]["$value"] == readings["addToBag"]["height"]
assert tokens["core"]["size"]["button"]["$value"] == readings["login"]["continueHeight"]
assert tokens["core"]["size"]["button"]["$value"] == readings["shopButton"]["height"]
assert tokens["core"]["radius"]["button"]["$value"] == readings["addToBag"]["borderRadius"]
print("lululemon tokens match readings")
