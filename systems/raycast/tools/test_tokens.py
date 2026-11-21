"""Raycast public package: tokens match the readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_themes_and_roles():
    tokens = json.loads((ROOT / "tokens.json").read_text())
    assert set(tokens) >= {"core", "dark", "$themes"}
    for role in ("page", "surface", "text", "muted", "accent", "border", "button"):
        assert tokens["dark"][role]["$value"].startswith("#")
        assert "source" in tokens["dark"][role]["$extensions"]
    assert tokens["dark"]["page"]["$value"] == "#07080a"
    assert tokens["dark"]["button"]["$value"] == "#e6e6e6"
    assert tokens["core"]["typography"]["display"]["$value"]["fontSize"] == "64px"
    assert "light" not in tokens


def test_site_tree_and_login_boundary():
    tree = (ROOT / "site-tree.md").read_text()
    assert "Install via Homebrew" in tree
    assert "not-started" in (ROOT / "README.md").read_text()
    assert "raycast-desktop" in (ROOT / "README.md").read_text()
    assert (ROOT / "screenshots" / "login-wall-dark-desktop.png").exists()
    assert (ROOT / "screenshots" / "signup-wall-dark-desktop.png").exists()
    assert (ROOT / "screenshots" / "home-dark-phone.png").exists()
    assert (ROOT / "screenshots" / "site-tree" / "homebrew-dialog.png").exists()
    review = json.loads((ROOT / "login-review.json").read_text())
    assert review["login-extracted"] == "not-started"


def test_no_catalog_edit_in_package():
    assert not (ROOT / "catalog.json").exists()
