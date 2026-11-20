"""Checks on calm's committed components.md against raw/components-computed.json."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]


class Outputs(unittest.TestCase):
    def test_a_bot_check_is_not_published_as_the_product(self):
        md = (ROOT / "components.md").read_text()
        entry = md.split("#### Signup page", 1)[1].split("\n#### ", 1)[0].split("\n### ", 1)[0]
        self.assertIn("bot check", entry)
        self.assertNotIn("**Values", entry)
        self.assertNotIn("px-captcha", md)

    def test_the_reading_really_is_the_challenge(self):
        text = C["signup-page"]["states"]["default"].get("text", "")
        self.assertTrue(re.search(r"press ?& ?hold", text, re.I), text[:80])


if __name__ == "__main__":
    unittest.main()
