"""The Pixso token file keeps the colours that were computed, and no invented dark set."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_light_only(self):
        self.assertEqual(set(self.data) - {"$description", "$themes"}, {"core", "light"})
        self.assertNotIn("dark", self.data)

    def test_brand_matches_login_button(self):
        brand = self.data["light"]["background"]["brand"]["$value"]
        self.assertEqual(brand, "#336fff")
        self.assertIn("source", self.data["light"]["background"]["brand"]["$extensions"])

    def test_marketing_button_is_not_the_login_blue(self):
        button = self.data["light"]["background"]["button"]["$value"]
        self.assertIn("0.84", button)
        self.assertNotEqual(button, "#336fff")


if __name__ == "__main__":
    unittest.main()
