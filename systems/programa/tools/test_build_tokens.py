#!/usr/bin/env python3
"""The Programa token file passes its check: every value is a reading in raw/ or labelled Reconstruction."""
import unittest
from pathlib import Path

import build_tokens
import raw_check


class Tokens(unittest.TestCase):
    def test_tokens_match_the_readings(self):
        self.assertEqual(build_tokens.main(), 0)

    def test_a_value_with_no_reading_is_caught(self):
        seen = raw_check.reading_forms(Path(build_tokens.HERE) / "raw")
        self.assertEqual(raw_check.missing({"$type": "color", "$value": "#fcfda1"}, seen), ["#fcfda1"])
        self.assertEqual(raw_check.missing({"$type": "color", "$value": "#ffffff00"}, seen), [])  # --color-alpha-white-0 #fff0
        self.assertEqual(raw_check.missing({"$type": "dimension", "$value": "-0.2px"}, seen), [])  # declared -.2px


if __name__ == "__main__":
    unittest.main()
