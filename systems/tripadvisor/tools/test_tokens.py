"""The published tokens match the computed readings in raw/computed.json."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = json.loads((HERE / "raw" / "computed.json").read_text())


def lookup(node, path):
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class TokensMatchReadings(unittest.TestCase):
    def test_light_page_is_measured_white(self):
        self.assertEqual(lookup(TOKENS, "light.color.background.page"), "#fff")
        self.assertEqual(RAW["light"]["--background-base"], "#fff")

    def test_brand_green_is_the_computed_action(self):
        self.assertEqual(lookup(TOKENS, "light.color.action.brand.background"), "#00eb5b")
        self.assertEqual(RAW["light"]["--interactive-action-background-brand"], "#00eb5b")

    def test_text_is_trip_pine(self):
        self.assertEqual(lookup(TOKENS, "light.color.text.primary"), "#002b11")

    def test_radius_full_is_the_pill(self):
        self.assertEqual(lookup(TOKENS, "core.radius.full"), "1000px")

    def test_dark_was_not_applied(self):
        self.assertFalse(RAW["meta"]["darkThemeApplied"])
        self.assertFalse(TOKENS["dark"]["$extensions"]["applied"])

    def test_body_family_starts_with_trip_sans_vf(self):
        self.assertEqual(lookup(TOKENS, "core.font.family.sans")[0], "Trip Sans VF")


if __name__ == "__main__":
    unittest.main()
