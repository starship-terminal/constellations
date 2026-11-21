#!/usr/bin/env python3
"""Check Aritzia tokens against the saved readings. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    readings = json.loads((ROOT / "raw" / "readings.json").read_text())
    tokens = json.loads((ROOT / "tokens.json").read_text())
    color = tokens["core"]["color"]
    assert color["page"]["$value"] == "#000000"
    assert color["accent"]["$value"] == "#d89f71"
    assert color["ink"]["$value"] == "#000000"
    assert readings["header"]["color"] == "rgb(216, 159, 113)"
    assert readings["hero"]["fontSize"] == "48px"
    assert readings["product"]["addToBag"]["clicked"] is False
    assert tokens["core"]["font"]["body"]["$value"].startswith('"Non-Seasonal Geo"')
    print("aritzia tokens match readings")


if __name__ == "__main__":
    main()
