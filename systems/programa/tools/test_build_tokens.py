#!/usr/bin/env python3
"""The Programa token file only holds measured or declared values."""
import unittest

import build_tokens


class Tokens(unittest.TestCase):
    def test_tokens_match_the_readings(self):
        self.assertEqual(build_tokens.main(), 0)


if __name__ == "__main__":
    unittest.main()
