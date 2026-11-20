"""Checks the Scape token file still names the colours measured on www.scape.com."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


class TokensTest(unittest.TestCase):
    def test_page_and_accent_match_the_live_computed_colours(self):
        self.assertEqual(TOKENS["light"]["bg"]["page"]["$value"], "#fef5f0")
        self.assertEqual(TOKENS["light"]["accent"]["default"]["$value"], "#ec6ce7")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "100px")
        self.assertIn("Measured", TOKENS["light"]["bg"]["page"]["$extensions"]["source"])

    def test_no_dark_theme_was_invented(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
