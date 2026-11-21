"""Obsidian public package: tokens match the readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_themes_and_roles():
    tokens = json.loads((ROOT / "tokens.json").read_text())
    assert set(tokens) >= {"core", "dark", "$themes"}
    for role in ("page", "text", "muted", "accent", "onAccent"):
        assert tokens["dark"][role]["$value"].startswith("#")
        assert "source" in tokens["dark"][role]["$extensions"]
    assert tokens["dark"]["page"]["$value"] == "#0f0f0f"
    assert tokens["dark"]["text"]["$value"] == "#eeeeee"
    assert tokens["dark"]["accent"]["$value"] == "#7c3aed"
    assert tokens["core"]["typography"]["display"]["$value"]["fontSize"] == "60px"
    assert "light" not in tokens


def test_site_tree_and_login_boundary():
    tree = (ROOT / "site-tree.md").read_text()
    assert "https://obsidian.md" in tree
    assert "2026-11-22" in tree
    readme = (ROOT / "README.md").read_text()
    assert "not-started" in readme
    assert "catalog.json" in readme
    assert (ROOT / "screenshots" / "login-wall-dark-desktop.png").exists()
    assert (ROOT / "screenshots" / "signup-wall-dark-desktop.png").exists()
    assert (ROOT / "screenshots" / "home-dark-phone.png").exists()
    assert (ROOT / "screenshots" / "site-tree" / "phone-menu.png").exists()
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login-extracted"] == "not-started"


def test_no_catalog_edit_in_package():
    assert not (ROOT / "catalog.json").exists()
