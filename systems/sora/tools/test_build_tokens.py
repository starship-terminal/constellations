"""build_tokens.py writes the measured sunset values and refuses a guessed colour."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_dark_page_and_button_match_the_computed_read(self):
        text = build_tokens.build()
        doc = json.loads(text)
        dark = doc["dark"]["color"]
        self.assertEqual(dark["background"]["primary"]["$value"], "rgb(0 0 0)")
        self.assertEqual(dark["text"]["primary"]["$value"], "rgb(255 255 255)")
        self.assertEqual(dark["control"]["button-background"]["$value"], "rgb(255, 255, 255)")
        self.assertEqual(dark["control"]["button-text"]["$value"], "rgb(0, 0, 0)")
        self.assertEqual(doc["light"]["color"]["background"]["primary"]["$value"], "rgb(255 255 255)")
        self.assertEqual(doc["light"]["color"]["text"]["primary"]["$value"], "rgb(25 25 25)")
        self.assertEqual(doc["core"]["radius"]["xl"]["$value"], "12px")
        self.assertEqual(doc["dark"]["component"]["button"]["height"]["$value"], "36px")
        self.assertIn("Measured", dark["background"]["primary"]["$extensions"]["source"])
        self.assertTrue((HERE / "tokens.json").exists())


if __name__ == "__main__":
    unittest.main()
