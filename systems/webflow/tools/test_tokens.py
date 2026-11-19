"""Webflow token file has the measured roles and does not invent a login surface."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_themes(self):
        self.assertIn("light", self.data)
        self.assertIn("dark", self.data)
        self.assertEqual(self.data["light"]["background"]["accent"]["$value"], "#146ef5")
        self.assertEqual(self.data["dark"]["background"]["page"]["$value"], "#080808")
        self.assertEqual(self.data["light"]["background"]["accent-hover"]["$value"], "#0055d4")

    def test_button_radius(self):
        self.assertEqual(self.data["core"]["radius"]["button"]["$value"], "4px")
        self.assertEqual(self.data["core"]["size"]["button-height"]["$value"], "51px")

    def test_sources(self):
        accent = self.data["light"]["background"]["accent"]
        self.assertIn("Measured", accent["$extensions"]["source"])
        self.assertNotIn("login.webflow", json.dumps(self.data).lower())


if __name__ == "__main__":
    unittest.main()
