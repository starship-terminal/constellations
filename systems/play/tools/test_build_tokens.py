#!/usr/bin/env python3
"""The Play token file passes its check: every value is a reading in raw/ or labelled Reconstruction."""
import unittest

import build_tokens


class Tokens(unittest.TestCase):
    def test_tokens_match_the_readings(self):
        self.assertEqual(build_tokens.main(), 0)

    def test_a_measured_label_needs_a_reading_in_raw(self):
        # #8ca4ba (token.steel) is in no raw file, so it may only be labelled Reconstruction.
        self.assertNotIn("#8ca4ba", build_tokens.raw_strings())
        self.assertIn("#17ffa6", build_tokens.raw_strings())  # a declared Stitches colour that raw/ holds


if __name__ == "__main__":
    unittest.main()
