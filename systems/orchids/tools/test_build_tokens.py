"""The Orchids token build copies measured readings and does not invent a ramp."""

import json
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parents[1]


class BuildTokensTest(unittest.TestCase):
    def test_primary_is_the_measured_amber(self):
        build_tokens.main()
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["primary"]["$value"], "#fcaa26")
        self.assertEqual(tokens["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["dark"]["page"]["$value"], "#0e0c0c")
        self.assertIn("source", tokens["core"]["color"]["primary"]["$extensions"])

    def test_paused_colours_stay_out_of_the_product_accent(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["paused"]["link"]["$value"], "rgb(0, 112, 243)")
        self.assertNotEqual(tokens["light"]["accent"]["$value"], "rgb(0, 112, 243)")


if __name__ == "__main__":
    unittest.main()
