"""Check that tokens.json still matches the live readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
size = tokens["core"]["size"]

assert color["ink"]["$value"] == "#000000"
assert readings["body"]["color"] == "rgb(0, 0, 0)"
assert color["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert color["muted"]["$value"] == "#5a5a5a"
assert readings["company"]["body"]["color"] == "rgb(90, 90, 90)"
assert color["promo"]["$value"] == readings["promoBar"]["hex"]
assert color["sale"]["$value"] == readings["sale"]["hex"]
assert size["display"]["$value"] == readings["company"]["display"]["fontSize"]
assert size["kicker"]["$value"] == readings["company"]["kicker"]["fontSize"]
assert size["promo-bar"]["$value"] == f"{readings['promoBar']['cssHeight']}px"
assert readings["add"]["clicked"] is False
assert readings["login"]["opened"] is False
print("pullandbear tokens match readings")
