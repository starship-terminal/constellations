"""Local checks for the 2026-11-22 public Amplitude capture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "screenshots"


def test_site_tree_dated():
    text = (ROOT / "site-tree.md").read_text()
    assert "2026-11-22" in text
    assert "https://amplitude.com/" in text
    assert "catalog.json was left alone" in text


def test_login_not_started():
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login_extracted"] == "not-started"
    assert review["signed_in"] is False
    assert review["typed"] is False


def test_required_shots():
    for name in [
        "home-desktop.png",
        "home-phone.png",
        "pricing-desktop.png",
        "login-desktop.png",
        "signup-desktop.png",
    ]:
        path = SHOTS / name
        assert path.exists(), name
        assert path.stat().st_size > 8000, name


def test_no_oauth_urls():
    for path in SHOTS.glob("*.capture.json"):
        text = path.read_text()
        assert "oauth" not in text.lower()
        assert "id_token" not in text
