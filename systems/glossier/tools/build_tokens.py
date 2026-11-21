"""Check that tokens.json still matches the homepage readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]

assert core["color"]["page"]["$value"] == "#ffffff"
assert readings["body"]["backgroundColor"] == "rgb(255, 255, 255)"
assert core["color"]["ink"]["$value"] == "#000000"
assert readings["body"]["color"] == "rgb(0, 0, 0)"
assert core["color"]["shipping"]["$value"] == "#333333"
assert readings["shippingBar"]["backgroundColor"] == "rgb(51, 51, 51)"
assert core["color"]["grey"]["$value"] == "#e8e8e8"
assert readings["shopNow"]["backgroundColor"] == "rgb(232, 232, 232)"
assert core["color"]["field-fill"]["$value"] == "#f7f7f7"
assert readings["signIn"]["backgroundColor"] == "rgb(247, 247, 247)"
assert core["color"]["muted"]["$value"] == "#666666"
assert readings["loginField"]["labelColor"] == "rgb(102, 102, 102)"
assert core["size"]["header"]["$value"] == readings["header"]["height"]
assert core["size"]["button"]["$value"] == readings["shopNow"]["height"]
assert core["size"]["field"]["$value"] == readings["loginField"]["height"]
assert core["fontSize"]["wordmark"]["$value"] == readings["wordmark"]["fontSize"]
assert core["fontSize"]["product"]["$value"] == readings["productTitle"]["fontSize"]
assert core["fontSize"]["account"]["$value"] == readings["loginTitle"]["fontSize"]
print("glossier tokens match readings")
