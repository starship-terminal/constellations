"""The committed tokens.json must rebuild from the raw readings and pass check()."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        built = build_tokens.build()
        build_tokens.check(built)
        committed = json.loads(TOKENS.read_text())
        self.assertEqual(committed, built)

    def test_brand_blue_is_the_measured_hex(self):
        built = build_tokens.build()
        self.assertEqual(built["core"]["color"]["brand"]["leapin-blue"]["$value"], "#2545ff")
        self.assertEqual(built["light"]["text"]["primary"]["$value"], "#171417")
        self.assertEqual(built["light"]["background"]["login-page"]["$value"], "#f8f6f3")


if __name__ == "__main__":
    unittest.main()
