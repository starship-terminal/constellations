"""Sana tokens stay inside the colours that were measured or declared on the public pages."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())

MEASURED = {
    "#0a1217", "#0a121799", "#686d70", "#0a121766", "#ffffff", "#fafafa",
    "#131314", "#1e1f20", "#242628", "#353536", "#17181a", "#e8e8e8",
    "#e8e8e899", "#8b8b8b", "#e8e8e866", "#5d5d5d", "#cdfe00", "#00dd00",
    "#ff3b30", "#ff3b300f", "#ffa82f", "#fd2d55", "#e59700", "#0a121780",
    "#0a12171a", "#00000008", "#00000014", "#e8e8e826", "#e8e8e80a",
    "#e8e8e899",
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

    def test_both_themes(self):
        self.assertIn("light", TOKENS)
        self.assertIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light", "dark"])

    def test_cover_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "home-light-default.png").is_file())
        self.assertTrue((ROOT / "screenshots" / "mobile-home-light-default.png").is_file())
        self.assertFalse((ROOT / "screenshots").joinpath("signin-dark-default.png").exists())


if __name__ == "__main__":
    unittest.main()
