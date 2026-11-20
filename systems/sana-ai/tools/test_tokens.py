"""Sana tokens stay inside the colours that were measured or declared on the public pages."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def raw_colours():
    """Every colour the raw readings hold: hex as written (short forms expanded), rgb()/rgba() as
    #rrggbb or #rrggbbaa. The test compares tokens with this, not with a list typed into the test."""
    seen = set()
    for f in sorted((ROOT / "raw").iterdir()):
        text = f.read_text(errors="replace")
        for h in re.findall(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b", text):
            seen.add("#" + ("".join(c * 2 for c in h) if len(h) in (3, 4) else h).lower())
        for body in re.findall(r"rgba?\(([^)]*)\)", text):
            parts = [p for p in re.split(r"[\s,/]+", body.strip()) if p]
            try:
                hx = "#%02x%02x%02x" % tuple(round(float(p)) for p in parts[:3])
            except ValueError:
                continue
            if len(parts) > 3:
                a = float(parts[3][:-1]) / 100 if parts[3].endswith("%") else float(parts[3])
                hx += "%02x" % round(a * 255) if a < 1 else ""
            seen.add(hx)
    return seen


MEASURED = raw_colours()


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
