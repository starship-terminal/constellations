"""Nothing tokens stay tied to the capture readings."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text())


class TokenTests(unittest.TestCase):
    def test_measured_colours_match_readings(self):
        tokens = load("tokens.json")
        readings = load("raw/readings.json")
        self.assertEqual(tokens["light"]["background"]["page"]["$value"], "#f4f4f4")
        self.assertEqual(tokens["light"]["action"]["accent"]["$value"], "#ffc700")
        self.assertEqual(tokens["light"]["surface"]["footer"]["$value"], "#040404")
        self.assertEqual(tokens["dark"]["background"]["page"]["$value"], "#181818")
        declared = readings["declaredRoot"]
        self.assertEqual(declared["greyscale-100"], "244 244 244")
        self.assertEqual(declared["accent-yellow"], "255 199 0")
        self.assertEqual(declared["greyscale-black"], "4 4 4")
        self.assertEqual(declared["greyscale-dm-light"], "24 24 24")

    def test_radius_and_type_are_the_computed_ones(self):
        tokens = load("tokens.json")
        self.assertEqual(tokens["core"]["radius"]["default"]["$value"], "4px")
        self.assertEqual(tokens["core"]["radius"]["md"]["$value"], "6px")
        self.assertEqual(tokens["core"]["typography"]["display-xl"]["$value"]["fontSize"], "48px")
        self.assertEqual(tokens["core"]["font"]["family"]["ui"]["$value"], "NType82-Regular, sans-serif")

    def test_screenshot_gap_is_recorded(self):
        readings = load("raw/readings.json")
        self.assertIn("not producing screenshot frames", readings["viewport"]["note"])


if __name__ == "__main__":
    unittest.main()
