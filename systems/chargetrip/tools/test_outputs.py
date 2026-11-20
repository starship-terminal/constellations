"""Checks on chargetrip's committed outputs against raw/components-computed.json."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
T = json.loads((ROOT / "tokens.json").read_text())


class Outputs(unittest.TestCase):
    def test_muted_text_cites_a_text_reading(self):
        leaf = T["light"]["text"]["muted"]
        self.assertIn("of footer default", leaf["$extensions"]["source"])
        self.assertNotIn("status-pill", leaf["$extensions"]["source"])

    def test_a_failed_focus_is_not_published_as_a_state(self):
        md = (ROOT / "components.md").read_text()
        for key, c in C.items():
            for state, v in c.get("states", {}).items():
                if "failed" in str(v.get("via", "")):
                    self.assertNotIn(f"components/crops/{key}-{state}.png", md, key)


if __name__ == "__main__":
    unittest.main()
