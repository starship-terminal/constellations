"""Checks that the public Reddit tokens name the values that were read."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_light_page_and_accent():
    tokens = json.loads((ROOT / "tokens.json").read_text())
    assert tokens["light"]["page"]["$value"] == "#FFFFFF"
    assert tokens["light"]["accent"]["$value"] == "#D93900"
    assert tokens["light"]["link"]["$value"] == "#115BCA"
    assert tokens["core"]["size"]["header"]["$value"] == "56px"


def test_login_extracted_stays_not_started():
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login_extracted"] == "not-started"
    assert review["signed_in"] is False
