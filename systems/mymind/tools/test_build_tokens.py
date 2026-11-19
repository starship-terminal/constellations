"""Checks for the committed MyMind tokens. Run from this package's tools/."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        data = json.loads(TOKENS.read_text())
        self.assertGreater(build_tokens.check(data), 40)

    def test_accent_is_the_measured_orange(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["core"]["color"]["orange"]["$value"], "#ff5924")
        self.assertEqual(data["light"]["color"]["page"]["$value"], "{color.canvas}")


if __name__ == "__main__":
    unittest.main()
