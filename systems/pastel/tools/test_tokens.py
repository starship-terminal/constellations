"""Pastel tokens stay tied to the capture readings."""

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
        self.assertEqual(tokens["light"]["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["action"]["primary"]["$value"], "#165dfb")
        self.assertEqual(tokens["light"]["action"]["pricing"]["$value"], "#12b981")
        self.assertEqual(tokens["light"]["action"]["app"]["$value"], "#4f77ff")
        self.assertEqual(tokens["light"]["background"]["app"]["$value"], "#f5f5f4")
        home = readings["computed"]["home"]
        self.assertEqual(home["trial"]["backgroundColor"], "rgb(22, 93, 251)")
        self.assertEqual(home["signup"]["backgroundColor"], "rgb(69, 71, 69)")
        self.assertEqual(readings["computed"]["login"]["submit"]["backgroundColor"], "rgb(79, 119, 255)")

    def test_radius_and_type_are_the_computed_ones(self):
        tokens = load("tokens.json")
        self.assertEqual(tokens["core"]["radius"]["button"]["$value"], "10px")
        self.assertEqual(tokens["core"]["radius"]["field"]["$value"], "6px")
        self.assertEqual(tokens["core"]["typography"]["display"]["$value"]["fontSize"], "52.605px")
        self.assertEqual(tokens["core"]["font"]["family"]["sans"]["$value"], "Figtree, sans-serif")

    def test_screenshot_gap_is_recorded(self):
        readings = load("raw/readings.json")
        self.assertIn("not producing screenshot frames", readings["viewport"]["note"])
        self.assertIn("password", " ".join(readings["notEntered"]))


if __name__ == "__main__":
    unittest.main()
