"""The Nextdoor token file matches the declared readings."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
DECLARED = json.loads((ROOT / "raw" / "tokens-declared.json").read_text())


class Tokens(unittest.TestCase):
    def test_brand_and_text(self):
        self.assertEqual(TOKENS["light"]["color"]["accent"]["$value"], "#1B8751")
        self.assertEqual(TOKENS["light"]["color"]["text"]["$value"], "#232F46")
        self.assertEqual(TOKENS["light"]["color"]["page"]["$value"], "#FFFFFF")
        self.assertEqual(TOKENS["dark"]["color"]["page"]["$value"], "#262626")

    def test_type_and_control(self):
        body = TOKENS["core"]["typography"]["body"]["$value"]
        self.assertEqual(body["fontSize"], "16px")
        self.assertEqual(body["fontWeight"], 420)
        self.assertEqual(TOKENS["light"]["component"]["buttonBrand"]["height"]["$value"], "48px")
        self.assertEqual(TOKENS["light"]["component"]["field"]["height"]["$value"], "56px")

    def test_declared_light_matches(self):
        self.assertEqual(
            TOKENS["light"]["color"]["muted"]["$value"],
            DECLARED["light"]["--nd-color-fgSecondary"],
        )


if __name__ == "__main__":
    unittest.main()
