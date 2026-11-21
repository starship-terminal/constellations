"""Local checks for the 2026-11-22 public beehiiv capture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "screenshots"


def test_site_tree_dated():
    text = (ROOT / "site-tree.md").read_text()
    assert "2026-11-22" in text
    assert "https://www.beehiiv.com/" in text
    assert "catalog.json was left alone" in text


def test_login_not_started():
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login_extracted"] == "not-started"
    assert review["signed_in"] is False


def test_required_shots():
    for name in [
        "home-desktop.png",
        "home-phone.png",
        "pricing-desktop.png",
        "login-preview-desktop.png",
        "signup-captcha-desktop.png",
    ]:
        path = SHOTS / name
        assert path.exists(), name
        assert path.stat().st_size > 8000, name


def test_no_prefilled_demo():
    assert not (SHOTS / "demo-desktop.png").exists()
