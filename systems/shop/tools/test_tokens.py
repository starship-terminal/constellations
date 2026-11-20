"""Shop tokens keep the page, surface, action, text, border, button and poster values, light only."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_light_page_and_action(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["background"]["page"]["$value"], "#fcfcfc")
        self.assertEqual(data["light"]["background"]["surface"]["$value"], "#ffffff")
        self.assertEqual(data["light"]["background"]["action"]["$value"], "#5433eb")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#000000")
        self.assertEqual(data["light"]["text"]["muted"]["$value"], "#0000008f")
        self.assertEqual(data["light"]["border"]["stroke"]["$value"], "#0000001a")
        self.assertEqual(data["light"]["component"]["button"]["height"]["$value"], "52px")
        self.assertEqual(data["light"]["component"]["button"]["radius"]["$value"], "999px")
        self.assertEqual(data["core"]["typography"]["poster"]["$value"]["fontSize"], "64px")
        self.assertNotIn("dark", data)


if __name__ == "__main__":
    unittest.main()
