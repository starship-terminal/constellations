"""Check the Relume tokens against the readings this capture wrote."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
HOME = json.loads((ROOT / "raw" / "home-1440.json").read_text())


def find(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node


class Tokens(unittest.TestCase):
    def test_page_matches_body(self):
        self.assertEqual(HOME["body"]["bg"], "rgb(241, 240, 238)")
        self.assertEqual(find("light.surface.page")["$value"], "#f1f0ee")

    def test_accent_matches_button(self):
        ai = next(b for b in HOME["buttons"] if b["text"] == "Start for free")
        self.assertEqual(ai["bg"], "rgb(255, 0, 244)")
        self.assertEqual(find("light.action.primary")["$value"], "#ff00f4")

    def test_hero_size(self):
        self.assertEqual(HOME["h1"]["size"], "56px")
        self.assertEqual(find("core.typography.hero")["$value"]["fontSize"], "56px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                ext = node.get("$extensions") or {}
                if "$extensions" not in node and isinstance(node["$value"], str) and node["$value"].startswith("{"):
                    return
                if "source" not in ext:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, f"{path}.{key}" if path else key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        self.assertEqual(missing, [])

    def test_no_dark_theme(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
