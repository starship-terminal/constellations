"""Conductor public package: tokens match the readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_themes_and_roles():
    tokens = json.loads((ROOT / "tokens.json").read_text())
    assert set(tokens) >= {"core", "dark", "light", "$themes"}
    for theme in ("dark", "light"):
        for role in ("page", "surface", "text", "muted", "accent", "border"):
            assert tokens[theme][role]["$value"].startswith("#")
            assert "source" in tokens[theme][role]["$extensions"]
    assert tokens["dark"]["page"]["$value"] == "#141110"
    assert tokens["light"]["page"]["$value"] == "#ffffff"
    assert tokens["core"]["typography"]["display"]["$value"]["fontSize"] == "36px"


def test_site_tree_and_login_boundary():
    tree = (ROOT / "site-tree.md").read_text()
    assert "Download Conductor" in tree
    assert "not-started" in (ROOT / "README.md").read_text()
    assert "conductor-desktop" in (ROOT / "README.md").read_text()
    assert (ROOT / "screenshots" / "login-wall-dark-desktop.png").exists()
    assert (ROOT / "screenshots" / "site-tree" / "phone-menu.png").exists()


def test_no_catalog_edit_in_package():
    assert not (ROOT / "catalog.json").exists()
