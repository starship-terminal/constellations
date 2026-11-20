"""The Prime Video tokens match the computed readings in raw/computed.json.

tokens.json has no builder; this test compares its roles with the readings.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "computed.json").read_text())


def hex_of(rgb: str) -> str:
    parts = [int(n) for n in rgb.removeprefix("rgb(").removesuffix(")").split(", ")]
    return "#{:02x}{:02x}{:02x}".format(*parts)


class TokensMatchReadings(unittest.TestCase):
    def test_page_and_footer(self):
        marketing = RAW["pages"]["marketing"]
        self.assertEqual(TOKENS["dark"]["background"]["page"]["$value"], hex_of(marketing["body"]["backgroundColor"]))
        self.assertEqual(TOKENS["dark"]["background"]["surface"]["$value"], hex_of(marketing["footer"]["backgroundColor"]))
        self.assertEqual(TOKENS["dark"]["text"]["secondary"]["$value"], hex_of(marketing["footer"]["color"]))

    def test_trial_button(self):
        button = RAW["pages"]["marketing"]["trialButton"]
        self.assertEqual(TOKENS["dark"]["background"]["action"]["$value"], hex_of(button["backgroundColor"]))
        self.assertEqual(TOKENS["dark"]["text"]["on-action"]["$value"], hex_of(button["color"]))
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], button["borderRadius"])
        self.assertEqual(TOKENS["dark"]["component"]["button"]["height"]["$value"], button["height"])

    def test_amazon_wall(self):
        wall = RAW["pages"]["signupWall"]
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], hex_of(wall["continue"]["backgroundColor"]))
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], hex_of(wall["body"]["color"]))
        card_border = wall["card"]["border"]  # "1px solid rgb(213, 217, 217)": the .a-box card
        self.assertEqual(TOKENS["light"]["border"]["stroke"]["$value"], hex_of(card_border[card_border.index("rgb("):]))
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], wall["continue"]["borderRadius"])

    def test_spacing_scale_comes_from_custom_properties(self):
        for name, value in RAW["customProperties"]["spacing"].items():
            step = name.removeprefix("--fable-spacing-")
            self.assertEqual(TOKENS["core"]["spacing"][step]["$value"], value)

    def test_signup_was_not_submitted(self):
        self.assertFalse(RAW["pages"]["signupWall"]["entered"])
        self.assertFalse(RAW["pages"]["signupWall"]["submitted"])


if __name__ == "__main__":
    unittest.main()
