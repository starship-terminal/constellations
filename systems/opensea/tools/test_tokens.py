#!/usr/bin/env python3
"""OpenSea package: every token has a source, and the probe colours match."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_package  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "css-vars.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict) and "$value" in value:
            yield here, value
        elif isinstance(value, dict):
            yield from walk(value, here)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_dark_page_and_accent_match_the_probe(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#080808")
        self.assertEqual(TOKENS["dark"]["surface"]["$value"], "#0c0c0c")
        self.assertEqual(TOKENS["dark"]["text"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["muted"]["$value"], "#acacac")
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#0086ff")
        self.assertEqual(TOKENS["dark"]["border"]["$value"], "#202020")

    def test_light_pair_matches_the_probe(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#fafafa")
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#171717")
        self.assertEqual(TOKENS["light"]["muted"]["$value"], "#666666")
        self.assertEqual(TOKENS["light"]["link"] if False else TOKENS["light"]["foreground"]["link"]["$value"], "#0086ff")

    def test_raw_pairs_cover_both_themes(self):
        self.assertGreaterEqual(len(RAW["colors"]), 30)
        for name, pair in RAW["colors"].items():
            if name == "frosted":
                continue
            self.assertIn("dark", pair, name)
            self.assertIn("light", pair, name)

    def test_focus_ring_is_the_measured_blue(self):
        self.assertEqual(TOKENS["core"]["color"]["focus"]["$value"], "#99c8ff")
        self.assertEqual(RAW["focus"]["input-focus-outline"], "none 1px #99c8ff")


class BuilderTest(unittest.TestCase):
    """The committed tokens.json and style-guide.html are what build_package makes; both built in memory."""

    def test_committed_tokens_are_what_the_builder_makes(self):
        self.assertEqual(TOKENS, build_package.tokens())

    def test_committed_style_guide_is_rendered_from_the_tokens(self):
        self.assertEqual((ROOT / "style-guide.html").read_text(), build_package.style_guide(TOKENS))

    def test_the_guide_palette_follows_the_tokens(self):
        doc = json.loads(json.dumps(TOKENS))
        doc["dark"]["page"]["$value"] = "#123456"
        self.assertIn("--page: #123456;", build_package.style_guide(doc))

    def test_measured_sizes_come_from_the_readings(self):
        self.assertEqual(TOKENS["core"]["size"]["dialog"]["$value"], "%dpx" % build_package.C("dialog.box.w"))
        with self.assertRaises(SystemExit):
            build_package.C("dialog.nope")

    def test_values_with_no_reading_are_not_labelled_measured(self):
        self.assertTrue(TOKENS["core"]["spacing"]["24"]["$extensions"]["source"].startswith("Reconstruction."))
        self.assertTrue(TOKENS["core"]["radius"]["pill"]["$extensions"]["source"].startswith("Derived."))

    def test_motion_is_typed(self):
        motion = TOKENS["core"]["motion"]
        self.assertEqual(motion["duration"]["nav"]["$type"], "duration")
        self.assertEqual(motion["easing"]["standard"]["$value"], [0.4, 0, 0.2, 1])


if __name__ == "__main__":
    unittest.main()
