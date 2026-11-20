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
        # --bs-link-color-rgb is saved as the channels 26,26,26
        self.assertEqual(raw_check.missing({"$type": "color", "$value": "#1a1a1a"}, seen), [])
        # one colour, two spellings
        self.assertEqual(raw_check.missing({"$type": "color", "$value": "rgba(255, 255, 255, 0.5)"}, {"#ffffff80"}), [])
        self.assertEqual(raw_check.missing({"$type": "color", "$value": "#ffffff80"}, raw_check.forms("rgba(255, 255, 255, 0.5)")), [])
        # a shadow list is checked layer by layer, and an easing list as its cubic-bezier()
        shadow = {"$type": "shadow", "$value": [{"color": "#fcfda1", "offsetX": "0px", "inset": True}]}
        self.assertEqual(raw_check.missing(shadow, seen), ["#fcfda1"])
        self.assertEqual(raw_check.missing({"$type": "cubicBezier", "$value": [0.4, 0, 0.2, 1]}, seen), [])
        self.assertEqual(raw_check.missing({"$type": "cubicBezier", "$value": [0.1, 0.2, 0.3, 0.4]}, seen), ["cubic-bezier(0.1,0.2,0.3,0.4)"])


if __name__ == "__main__":
    unittest.main()
