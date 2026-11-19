"""Pitch tokens stay inside the colours that were measured on the public pages."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())

MEASURED = {
    "#5318eb", "#280f62", "#0c021c", "#363636", "#c6a5ff", "#ebe3fe",
    "#f9f6ff", "#c4ee87", "#ff2344", "#ffffff", "#6b53ff", "#2b2a35",
    "#1e1d28", "#939da8", "#3f4250", "#dddfe5", "#da615d", "#5dce89",
    "#ffbb5c", "#5216eb",
}


def colours(node):
    if isinstance(node, dict):
        if node.get("$type") == "color" and isinstance(node.get("$value"), str):
            if node["$value"].startswith("#"):
                yield node["$value"].lower()
        for child in node.values():
            yield from colours(child)


class Tokens(unittest.TestCase):
    def test_every_literal_colour_was_measured(self):
        found = set(colours(TOKENS))
        self.assertTrue(found, "no colour tokens")
        self.assertEqual(found - MEASURED, set())

    def test_light_theme_only(self):
        self.assertIn("light", TOKENS)
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])

    def test_cover_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "home-light-default.png").is_file())
        self.assertTrue((ROOT / "screenshots" / "login-light-default.png").is_file())


if __name__ == "__main__":
    unittest.main()
