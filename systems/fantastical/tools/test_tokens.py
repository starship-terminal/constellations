"""Fantastical public package: tokens match the readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_themes_and_roles():
    tokens = json.loads((ROOT / "tokens.json").read_text())
    assert set(tokens) >= {"core", "light", "$themes"}
    for role in ("page", "text", "accent", "onAccent"):
        assert tokens["light"][role]["$value"].startswith("#")
        assert "source" in tokens["light"][role]["$extensions"]
    assert tokens["light"]["page"]["$value"] == "#ffffff"
    assert tokens["light"]["text"]["$value"] == "#1d1e1f"
    assert tokens["light"]["accent"]["$value"] == "#408fff"
    assert tokens["core"]["typography"]["display"]["$value"]["fontSize"] == "40px"
    assert "dark" not in tokens


def test_site_tree_and_login_boundary():
    tree = (ROOT / "site-tree.md").read_text()
    assert "https://flexibits.com/fantastical" in tree
    assert "November 2026" in tree or "2026-11-22" in tree
    readme = (ROOT / "README.md").read_text()
    assert "not-started" in readme
    assert "catalog.json" in readme
    assert (ROOT / "screenshots" / "login-wall-light-desktop.png").exists()
    assert (ROOT / "screenshots" / "signup-wall-light-desktop.png").exists()
    assert (ROOT / "screenshots" / "home-light-phone.png").exists()
    assert (ROOT / "screenshots" / "site-tree" / "phone-menu.png").exists()
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login-extracted"] == "not-started"


def test_no_catalog_edit_in_package():
    assert not (ROOT / "catalog.json").exists()
