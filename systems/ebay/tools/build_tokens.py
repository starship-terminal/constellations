"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["accent"]["$value"] == "#0968f6"
assert readings["searchButton"]["backgroundColor"] == "rgb(9, 104, 246)"
print("ebay tokens match readings")
