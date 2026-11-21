"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
assert tokens["core"]["color"]["accent"]["$value"] == "#f1641e"
assert readings["searchButtonAfter"]["backgroundColor"] == "rgb(241, 100, 30)"
assert tokens["core"]["color"]["page"]["$value"] == "#faf8f5"
assert readings["body"]["backgroundColor"] == "rgb(250, 248, 245)"
print("etsy tokens match readings")
