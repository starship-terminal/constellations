"""Check that tokens.json still matches the homepage and product readings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / "tokens.json").read_text())
readings = json.loads((root / "raw" / "readings.json").read_text())
core = tokens["core"]

assert core["color"]["ink"]["$value"] == "#121212"
assert readings["body"]["color"] == "rgb(18, 18, 18)"
assert readings["product"]["titleColor"] == "rgb(18, 18, 18)"
assert core["color"]["blueprint"]["$value"] == "#1050d0"
assert readings["heroButtons"]["shop"]["backgroundColor"] == "rgb(16, 80, 208)"
assert readings["selectLenses"]["backgroundColor"] == "rgb(16, 80, 208)"
assert readings["login"]["continueBackground"] == "rgb(16, 80, 208)"
assert core["color"]["ink-blue"]["$value"] == "#072369"
assert readings["heroButtons"]["learn"]["backgroundColor"] == "rgb(7, 35, 105)"
assert core["color"]["chalk"]["$value"] == "#f6f7f5"
assert readings["login"]["pageBackground"] == "rgb(246, 247, 245)"
assert core["color"]["classroom-green"]["$value"] == "#09624d"
assert readings["product"]["extraPairsColor"] == "rgb(9, 98, 77)"
assert core["radius"]["button"]["$value"] == "100px"
assert readings["selectLenses"]["borderRadius"] == "100px"
assert readings["heroButtons"]["shop"]["borderRadius"] == "100px"
assert core["size"]["button"]["$value"] == readings["selectLenses"]["height"]
assert core["size"]["button"]["$value"] == readings["login"]["continueHeight"]
assert core["size"]["field"]["$value"] == readings["newsletter"]["fieldHeight"]
assert readings["login"]["photographed"] is False
assert readings["signup"]["photographed"] is False
assert readings["login"]["queryCarriesState"] is True
print("warbyparker tokens match readings")
