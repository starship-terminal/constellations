"""Check the Relume tokens against the readings this capture wrote."""
import json
import re
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

    def test_style_guide_colours_are_tokens(self):
        # style-guide.html is hand-written (no builder here can run, see the README), so nothing
        # regenerates it from tokens.json: every colour it declares must still be a token value.
        values = set()

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                if node.get("$type") == "color":
                    values.add(str(node["$value"]).lower())
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child)

        walk(TOKENS)
        html = (ROOT / "style-guide.html").read_text()
        root = re.search(r":root \{(.*?)\}", html, re.S).group(1)
        # Every custom property on :root, whatever its form: a colour written as rgb() or a name
        # must not slip past the check, so anything that is not a hex is a failure.
        declared = re.findall(r"--([\w-]+):\s*([^;]+);", root)
        self.assertTrue(declared)
        for name, value in declared:
            with self.subTest(var=name):
                self.assertRegex(value.strip(), r"^#[0-9a-fA-F]+$")
                self.assertIn(value.strip().lower(), values)

    def test_no_dark_theme(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
