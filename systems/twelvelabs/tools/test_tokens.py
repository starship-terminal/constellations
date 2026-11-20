"""TwelveLabs tokens keep the measured paper page and ink actions."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_light_page_and_ink(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "{core.color.paper}")
        self.assertEqual(data["core"]["color"]["paper"]["$value"], "#f4f3f3")
        self.assertEqual(data["core"]["color"]["ink"]["$value"], "#1d1c1b")
        self.assertEqual(data["light"]["accent"]["$value"], "{core.color.ink}")
        self.assertEqual(data["core"]["radius"]["heroButton"]["$value"], "18px")
        self.assertEqual(data["core"]["radius"]["field"]["$value"], "6px")
        self.assertNotIn("dark", data)
        self.assertIn("Milling Duplex 1mm", data["core"]["font"]["family"]["display"]["$value"])


if __name__ == "__main__":
    unittest.main()
