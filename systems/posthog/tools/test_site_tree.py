"""Local checks for the 2026-11-22 public PostHog capture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "screenshots"


def test_site_tree_dated():
    text = (ROOT / "site-tree.md").read_text()
    assert "2026-11-22" in text
    assert "November 2026" in text
    assert "https://posthog.com/" in text
    assert "catalog.json was left alone" in text


def test_login_not_started():
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["loginExtracted"] == "not-started"
    assert review["typed"] is False
    assert review["submitted"] is False


def test_required_shots():
    for name in [
        "home-light-1440.png",
        "home-light-390.png",
        "pricing-light-1440.png",
        "login-light-1440.png",
        "signup-light-1440.png",
        "signup-light-390.png",
    ]:
        path = SHOTS / name
        assert path.exists(), name
        assert path.stat().st_size > 8000, name


def test_no_oauth_urls():
    for path in SHOTS.glob("*.capture.json"):
        text = path.read_text().lower()
        assert "oauth" not in text
        assert "id_token" not in text
        assert "access_token" not in text
