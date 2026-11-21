import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TokenTests(unittest.TestCase):
    def test_every_token_has_a_source(self):
        data = json.loads((ROOT / "tokens.json").read_text())

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                source = node["$extensions"]["source"]
                self.assertTrue(source["evidence"])
                self.assertIn("amazon.com", source["capture"])
                return
            if isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value)

        walk(data)

    def test_brand_matches_readings(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        readings = json.loads((ROOT / "raw" / "measured-hex.json").read_text())
        self.assertEqual(
            tokens["light"]["color"]["brand"]["$value"],
            readings["customProperties"]["--nav-desktop-header-tbg"],
        )

    def test_login_was_not_extracted(self):
        review = json.loads((ROOT / "login-review.json").read_text())
        self.assertEqual(review["loginExtracted"], "not-started")
        self.assertFalse(review["typed"])
        self.assertFalse(review["submitted"])


if __name__ == "__main__":
    unittest.main()
