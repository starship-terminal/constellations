"""Checks on clay-earth's committed outputs against raw/components-computed.json."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
T = json.loads((ROOT / "tokens.json").read_text())


class Outputs(unittest.TestCase):
    def test_a_token_read_from_a_hidden_panel_says_so(self):
        self.assertEqual(C["menu-panel"]["states"]["default"]["style"]["opacity"], "0")
        leaf = T["core"]["component"]["menuPanel"]["width"]
        self.assertIn("recapture needed", leaf["$extensions"]["source"])

    def test_the_cta_glow_is_the_reading(self):
        glow = T["dark"]["shadow"]["ctaGlow"]["$value"][0]
        self.assertEqual(C["cta"]["states"]["default"]["style"]["boxShadow"],
                         "%s %s %s %s %s" % (glow["color"], glow["offsetX"], glow["offsetY"], glow["blur"], glow["spread"]))

    def test_a_failed_focus_is_not_published_as_a_state(self):
        md = (ROOT / "components.md").read_text()
        for key, c in C.items():
            for state, v in c.get("states", {}).items():
                if "failed" in str(v.get("via", "")):
                    self.assertNotIn(f"components/crops/{key}-{state}.png", md, key)


if __name__ == "__main__":
    unittest.main()
