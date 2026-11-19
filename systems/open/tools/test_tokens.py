"""The Open tokens resolve to the colours measured on o-p-e-n.com."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_cream_and_black(self):
        self.assertEqual(self.data["core"]["color"]["cream"]["$value"], "#eeece7")
        self.assertEqual(self.data["core"]["color"]["black"]["$value"], "#000000")
        self.assertEqual(self.data["core"]["color"]["copper"]["$value"], "#bf7d41")

    def test_themes(self):
        self.assertEqual(self.data["dark"]["text"]["$value"], "{color.cream}")
        self.assertEqual(self.data["light"]["page"]["$value"], "{color.cream}")
        self.assertEqual(self.data["dark"]["page"]["$value"], "{color.black}")

    def test_pill(self):
        self.assertEqual(self.data["core"]["radius"]["pill"]["$value"], "999px")
        self.assertEqual(self.data["core"]["size"]["control"]["$value"], "60px")


if __name__ == "__main__":
    unittest.main()
