#!/usr/bin/env python3
"""The measured WhatsApp tokens stay put."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_green_is_the_measured_download_fill(self):
        self.assertEqual(self.data["core"]["color"]["green"]["$value"], "#25d366")

    def test_dark_set_stays_empty(self):
        self.assertEqual(self.data["dark"], {})

    def test_checker_passes_and_refuses_an_unread_colour(self):
        import sys
        sys.path.insert(0, str(TOKENS.parent / "tools"))
        import build_tokens
        seen = build_tokens.raw_colours()
        self.assertEqual(build_tokens.problems(self.data, seen), [])
        bad = json.loads(TOKENS.read_text())
        bad["core"]["color"]["green"]["$value"] = "#123456"
        self.assertIn("core.color.green: Measured #123456 is in no raw/ reading", build_tokens.problems(bad, seen))
        del bad["core"]["color"]["ink"]["$extensions"]
        self.assertIn("core.color.ink: no source", build_tokens.problems(bad, seen))

    def test_checker_follows_aliases(self):
        """A Measured alias whose target no raw/ file holds is refused, and so is a dead alias."""
        import sys
        sys.path.insert(0, str(TOKENS.parent / "tools"))
        import build_tokens
        seen = build_tokens.raw_colours()
        bad = json.loads(TOKENS.read_text())
        bad["light"]["text"]["muted"]["$extensions"]["source"] = "Measured: test"
        self.assertIn("light.text.muted: Measured #5e5e5e (through {color.muted}) is in no raw/ reading",
                      build_tokens.problems(bad, seen))
        bad["light"]["text"]["muted"]["$value"] = "{color.nope}"
        self.assertIn("light.text.muted: alias {color.nope} does not resolve", build_tokens.problems(bad, seen))

    def test_display_size_is_the_desktop_h1(self):
        self.assertEqual(self.data["core"]["typography"]["display"]["$value"]["fontSize"], "80px")


if __name__ == "__main__":
    unittest.main()
