"""Checks on cofounder's committed tokens against raw/components-computed.json."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
T = json.loads((ROOT / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_glass_tint_cites_a_reading_that_holds_it(self):
        leaf = T["light"]["surface"]["glass"]
        self.assertIn("raw/components-computed.json", leaf["$extensions"]["source"])
        paint = [p.get("bgImage", "") for p in C["header"]["states"]["default"]["paint"]]
        self.assertTrue(any(g.startswith("linear-gradient(%s 0%%" % leaf["$value"]) for g in paint), paint)


if __name__ == "__main__":
    unittest.main()
