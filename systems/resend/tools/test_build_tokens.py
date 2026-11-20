"""Resend token file keeps the measured marketing page and accent."""
import json
import pathlib
import sys
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
sys.path.insert(0, str(TOKENS.parent / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class TokensTest(unittest.TestCase):
    def test_dark_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(data["dark"]["accent"]["$value"], "#ffffff")
        self.assertEqual(data["dark"]["text"]["primary"]["$value"], "#f0f0f0")
        self.assertEqual(data["dark"]["text"]["secondary"]["$value"], "#a1a4a5")
        self.assertNotIn("light", data)
        self.assertEqual(data["core"]["color"]["gray"]["12"]["$value"], "#f0f0f0")
        self.assertEqual(data["core"]["radius"]["2xl"]["$value"], "16px")


    def test_committed_file_matches_builder(self):
        self.assertEqual(TOKENS.read_text(), build_tokens.build())

    def test_button_fill_is_not_white_under_white_text(self):
        button = json.loads(build_tokens.build())["dark"]["component"]["button"]
        self.assertEqual(button["text"]["$value"], "#ffffff")
        self.assertEqual(button["bg"]["$value"], "#fdfdfd0d")  # the gradient's first stop, 5% white

    def test_first_stop_must_be_the_rgba(self):
        saved = build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"]
        try:
            build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"] = (
                "linear-gradient(104deg, rgb(253, 253, 253) 5%, rgba(240, 240, 228, 0.1) 100%)")
            with self.assertRaises(SystemExit):
                build_tokens.gradient_base("getStartedHero")
        finally:
            build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"] = saved

    def test_unreadable_gradient_fails(self):
        saved = build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"]
        try:
            build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"] = "none"
            with self.assertRaises(SystemExit):
                build_tokens.gradient_base("getStartedHero")
        finally:
            build_tokens.RAW["components"]["getStartedHero"]["backgroundImage"] = saved


if __name__ == "__main__":
    unittest.main()
