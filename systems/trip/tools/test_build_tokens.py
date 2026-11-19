"""The Trip token builder keeps measured colours and does not invent a dark theme."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_brand_aliases_to_blue6(self):
        data = build_tokens.build()
        self.assertEqual(data["light"]["color"]["bg-brand"]["$value"], "{core.color.blue6}")
        self.assertEqual(data["core"]["color"]["blue6"]["$value"].lower(), "#2c61fe")
        self.assertEqual(data["light"]["color"]["text-primary"]["$value"], "{core.color.neutral10}")

    def test_no_dark_set(self):
        data = build_tokens.build()
        self.assertEqual(set(data) - {"$themes"}, {"core", "light"})
        self.assertEqual(data["$themes"][0]["id"], "light")

    def test_body_m_matches_the_shorthand(self):
        data = build_tokens.build()
        body = data["core"]["typography"]["body-m"]["$value"]
        self.assertEqual(body["fontSize"], "14px")
        self.assertEqual(body["fontWeight"], 400)
        self.assertEqual(body["lineHeight"], 1.5)
        self.assertIn("Trip Geom", body["fontFamily"])

    def test_written_file_matches_builder(self):
        written = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(written["light"]["color"]["bg-brand"]["$value"], "{core.color.blue6}")
        self.assertIn("search-card", written["light"]["shadow"])


if __name__ == "__main__":
    unittest.main()
