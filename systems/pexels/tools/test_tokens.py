"""Pexels tokens match the colours measured on pexels.com."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_inks(self):
        self.assertEqual(self.data["core"]["color"]["shadow"]["$value"], "#191919")
        self.assertEqual(self.data["core"]["color"]["alien"]["$value"], "#54ca84")
        self.assertEqual(self.data["core"]["color"]["grey200"]["$value"], "#f7f7f7")
        self.assertEqual(self.data["core"]["color"]["grey400"]["$value"], "#ededed")

    def test_light_roles(self):
        self.assertEqual(self.data["light"]["page"]["$value"], "{color.white}")
        self.assertEqual(self.data["light"]["accent"]["$value"], "{color.shadow}")
        self.assertEqual(self.data["light"]["action"]["$value"], "{color.alien}")
        self.assertEqual(self.data["light"]["text"]["$value"], "{color.black}")

    def test_control(self):
        self.assertEqual(self.data["core"]["radius"]["control"]["$value"], "12px")
        self.assertEqual(self.data["core"]["size"]["control"]["$value"], "48px")
        self.assertEqual(self.data["core"]["typography"]["hero"]["$value"]["fontSize"], "48px")


if __name__ == "__main__":
    unittest.main()
