"""build_tokens.py writes the measured sunset values as hex and refuses a guessed colour."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.build())

    def test_dark_page_and_button_match_the_computed_read(self):
        doc = json.loads(build_tokens.build())
        dark = doc["dark"]["color"]
        self.assertEqual(dark["background"]["primary"]["$value"], "#000000")  # rgb(0 0 0)
        self.assertEqual(dark["text"]["primary"]["$value"], "#ffffff")  # rgb(255 255 255)
        self.assertEqual(dark["control"]["button-background"]["$value"], "#ffffff")  # rgb(255, 255, 255)
        self.assertEqual(dark["control"]["button-text"]["$value"], "#000000")  # rgb(0, 0, 0)
        self.assertEqual(dark["text"]["secondary"]["$value"], "#ffffff99")  # hsla(0,0%,100%,.6)
        self.assertEqual(doc["light"]["color"]["background"]["primary"]["$value"], "#ffffff")
        self.assertEqual(doc["light"]["color"]["text"]["primary"]["$value"], "#191919")  # rgb(25 25 25)
        self.assertEqual(doc["core"]["radius"]["xl"]["$value"], "12px")
        self.assertEqual(doc["dark"]["component"]["button"]["height"]["$value"], "36px")
        self.assertIn("Measured", dark["background"]["primary"]["$extensions"]["source"])
        self.assertIn("--bg-primary: 0 0 0", dark["background"]["primary"]["$extensions"]["source"])

    def test_every_colour_is_hex_and_durations_are_durations(self):
        doc = json.loads(build_tokens.build())
        for theme in ("light", "dark"):
            for group in doc[theme]["color"].values():
                for name, token in group.items():
                    self.assertRegex(token["$value"], r"^#[0-9a-f]{6}([0-9a-f]{2})?$", name)
        for name, token in doc["core"]["motion"]["duration"].items():
            self.assertEqual(token["$type"], "duration", name)

    def test_hsl_and_rgb_forms_convert(self):
        self.assertEqual(build_tokens.to_hex("hsl(240 10% 3.9%)"), "#09090b")
        self.assertEqual(build_tokens.to_hex("rgba(25,25,25,.5)"), "#19191980")
        self.assertEqual(build_tokens.to_hex("#fff"), "#ffffff")

    def test_a_guessed_colour_is_refused(self):
        for value in ("black-ish", "var(--bg-primary)", "rgb(1 2)"):
            with self.assertRaises(ValueError):
                build_tokens.to_hex(value)


if __name__ == "__main__":
    unittest.main()
