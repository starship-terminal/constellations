#!/usr/bin/env python3
"""Check Béis tokens against the saved readings. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    readings = json.loads((ROOT / "raw" / "readings.json").read_text())
    tokens = json.loads((ROOT / "tokens.json").read_text())
    color = tokens["core"]["color"]
    assert color["page"]["$value"] == "#ffffff"
    assert color["header"]["$value"] == "#f2f1ec"
    assert color["accent"]["$value"] == "#2c2c2e"
    assert color["ink"]["$value"] == "#000000"
    assert readings["header"]["backgroundColor"] == "rgb(242, 241, 236)"
    assert readings["hero"]["heading"]["fontSize"] == "30px"
    assert readings["product"]["addToCart"]["clicked"] is False
    assert readings["hero"]["cta"]["clicked"] is False
    assert tokens["core"]["font"]["body"]["$value"].startswith("Helvetica")
    assert tokens["core"]["radius"]["button"]["$value"] == "9px"
    print("beis tokens match readings")


if __name__ == "__main__":
    main()
