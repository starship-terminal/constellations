"""Checks on curater's committed tokens."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from leaves(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_colours_are_srgb(self):
        # tools/catalog.py cannot parse oklab/oklch, so an unconverted value is never contrast-checked.
        for s, tree in T.items():
            if s.startswith("$"):
                continue
            for name, t in leaves(tree):
                if t["$type"] == "color":
                    self.assertNotRegex(str(t["$value"]), r"^(ok)?(lab|lch)\(|^color-mix\(", f"{s}.{name}")

    def test_an_alias_cites_the_state_that_equals_it(self):
        leaf = T["light"]["color"]["background"]["hover-fill"]
        m = re.match(r"computed (\w+) of (\S+) (\S+) equals", leaf["$extensions"]["source"])
        prop, comp, state = m.groups()
        self.assertEqual(C[comp]["states"][state]["style"][prop], "rgb(242, 242, 242)")


if __name__ == "__main__":
    unittest.main()
