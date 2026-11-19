"""Supercut tokens keep the measured public marketing colours."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_dark_page_and_cream_button(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["color"]["page"]["$value"], "#100e0e")
        self.assertEqual(data["dark"]["color"]["foreground"]["$value"], "#fdfff0")
        self.assertEqual(data["dark"]["color"]["muted"]["$value"], "#969692")
        self.assertEqual(data["dark"]["color"]["cream"]["$value"], "#fdfff0")
        self.assertEqual(data["dark"]["color"]["primary"]["$value"], "#ff0055")
        self.assertNotIn("light", data)
        self.assertEqual(data["core"]["typography"]["hero"]["$value"]["fontSize"], "60px")
        self.assertEqual(data["core"]["space"]["header"]["$value"], "64px")


if __name__ == "__main__":
    unittest.main()
