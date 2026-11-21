"""The X package tokens resolve, and every colour came from a reading."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
READINGS = json.loads((ROOT / "raw" / "readings.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class TokenTests(unittest.TestCase):
    def test_readings_exist(self):
        self.assertIn("login", READINGS)
        self.assertEqual(READINGS["login"]["page"]["background"], "rgb(0, 0, 0)")

    def test_brand_matches_css_variable(self):
        brand = TOKENS["dark"]["color"]["text"]["brand"]["$value"]
        self.assertEqual(brand, READINGS["loggedOutShell"]["tokens"]["--color-brand"])

    def test_every_token_has_a_source(self):
        missing = [path for path, node in walk(TOKENS) if "source" not in node.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_screenshots_are_the_public_pages(self):
        shots = sorted(p.name for p in (ROOT / "screenshots").glob("*.png"))
        self.assertEqual(shots, [
            "about-dark-1440.png",
            "about-light-1440.png",
            "download-dark-390.png",
            "home-dark-390.png",
            "home-login-dark-1440.png",
            "login-dark-1440.png",
            "missing-dark-1440.png",
            "news-dark-1440.png",
            "news-dark-390.png",
            "privacy-light-1440.png",
            "privacy-light-390.png",
            "signup-dark-1440.png",
            "tos-light-1440.png",
            "tos-light-390.png",
        ])


if __name__ == "__main__":
    unittest.main()
