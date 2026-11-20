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

    def test_element_readings_raw_does_not_hold_are_not_measured(self):
        # raw/computed.json keeps capture metadata only; an element's computed style is a hand entry.
        built = build_tokens.build()
        self.assertEqual(built["light"]["text"]["nav"]["$extensions"]["source"]["evidence"], "Reconstruction")
        self.assertEqual(built["core"]["color"]["brand"]["leapin-blue"]["$extensions"]["source"]["evidence"], "Measured")

    def test_check_refuses_a_measured_element_reading(self):
        built = build_tokens.build()
        built["light"]["text"]["nav"]["$extensions"]["source"]["evidence"] = "Measured"
        with self.assertRaisesRegex(SystemExit, "raw/ does not hold"):
            build_tokens.check(built)

    def test_durations_are_typed_duration(self):
        built = build_tokens.build()
        for key, token in built["core"]["motion"]["duration"].items():
            self.assertEqual(token["$type"], "duration", key)
        built["core"]["motion"]["duration"]["100"]["$type"] = "dimension"
        with self.assertRaisesRegex(SystemExit, "duration typed dimension"):
            build_tokens.check(built)


if __name__ == "__main__":
    unittest.main()
