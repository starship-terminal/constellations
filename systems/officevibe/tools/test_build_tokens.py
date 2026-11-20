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

    def test_stylesheet_rules_and_their_aliases_are_not_measured(self):
        built = build_tokens.build()
        for key in ("display", "h1", "h2", "h3", "h4", "h5"):
            self.assertEqual(built["core"]["typography"][key]["$extensions"]["source"]["evidence"], "Reconstruction", key)
        # component.button.text aliases text.on-accent, an element reading raw/ does not hold
        self.assertEqual(built["light"]["component"]["button"]["text"]["$extensions"]["source"]["evidence"], "Reconstruction")

    def test_every_measured_root_token_names_a_property_the_dump_holds(self):
        dumps = {build_tokens.MKT: build_tokens.M, build_tokens.LOGIN: build_tokens.H}

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                yield node["$extensions"]["source"]
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from walk(v)

        built = build_tokens.build()
        for src in walk({"core": built["core"], "light": built["light"]}):
            if src["evidence"] == "Measured" and src["from"] in dumps:
                self.assertEqual(src["selector"], ":root", src)
                self.assertIn(src["property"], dumps[src["from"]], src)

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
