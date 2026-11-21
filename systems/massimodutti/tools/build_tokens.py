"""Check that tokens.json still matches the storefront readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
color = tokens["core"]["color"]
size = tokens["core"]["size"]
radius = tokens["core"]["radius"]

assert color["ink"]["$value"] == "#000000"
assert readings["navButton"]["color"] == "rgb(0, 0, 0)"
assert color["page"]["$value"] == "#ffffff"
assert readings["menuPanel"]["backgroundColor"] == "rgb(255, 255, 255)"
assert color["muted"]["$value"] == "#737373"
assert readings["fieldLabel"]["color"] == "rgb(115, 115, 115)"
assert color["on-ink"]["$value"] == "#ffffff"
assert readings["marketContinue"]["color"] == "rgb(255, 255, 255)"
assert readings["marketContinue"]["backgroundColor"] == "rgb(0, 0, 0)"
assert size["button"]["$value"] == "32px"
assert readings["addToBasket"]["height"] == 32
assert readings["addToBasket"]["backgroundColor"] == "rgb(255, 255, 255)"
assert radius["none"]["$value"] == readings["addToBasket"]["borderRadius"]
assert readings["addToBasket"]["clicked"] is False
print("massimodutti tokens match readings")
