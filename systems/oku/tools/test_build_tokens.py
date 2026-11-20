#!/usr/bin/env python3
"""The measured values this package is not allowed to drift from, and the builder that makes them.

build_tokens.build() runs in memory; nothing here writes tokens.json."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if not key.startswith("$"):
                yield from walk(value)


class Tokens(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_the_outline_ring_keeps_its_measured_alpha(self):
        # raw/readings.json: inset ring rgba(224, 225, 228, 0.22); 0.22 * 255 rounds to 0x38
        self.assertEqual(TOKENS["dark"]["color"]["border-strong"]["$value"], "#E0E1E438")

    def test_roles_that_were_not_painted_are_not_labelled_measured(self):
        for theme in ("light", "dark"):
            for name, token in TOKENS[theme]["color"].items():
                source = token["$extensions"]["source"]
                if "Declared" in source.split(". ")[1] or "not remeasured" in source:
                    self.assertFalse(source.startswith("Measured"), f"{theme}.{name}")
        self.assertTrue(TOKENS["light"]["color"]["link"]["$extensions"]["source"].startswith("Observed"))

    def test_durations_are_typed_duration(self):
        for key in ("duration-switch", "duration-short"):
            self.assertEqual(TOKENS["core"]["motion"][key]["$type"], "duration")

    def test_the_style_guide_fetches_no_web_font(self):
        guide = (HERE / "style-guide.html").read_text()
        self.assertNotIn("fonts.googleapis.com", guide)
        self.assertNotIn("fonts.gstatic.com", guide)

    def test_every_token_names_a_source(self):
        missing = [token for token in walk(TOKENS) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_dark_page_is_the_painted_milk(self):
        self.assertEqual(TOKENS["dark"]["color"]["page"]["$value"], "#131314")

    def test_light_page_is_white(self):
        self.assertEqual(TOKENS["light"]["color"]["page"]["$value"], "#FFFFFF")

    def test_display_is_fabric_serif(self):
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontFamily"], "FabricSerifWeb")
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "48px")

    def test_control_radius_is_8(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "8px")


if __name__ == "__main__":
    unittest.main()
