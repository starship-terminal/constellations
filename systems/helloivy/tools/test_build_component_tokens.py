"""raw/component-tokens.json must rebuild from the raw readings, and every value whose source
names a computed reading must be that reading.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_component_tokens as bct  # noqa: E402

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"


def leaves(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from leaves(v, f"{path}.{k}" if path else k)


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((RAW / "component-tokens.json").read_text()), bct.TREE)

    def test_computed_values_are_the_readings(self):
        n = 0
        for path, leaf in leaves(bct.TREE):
            m = re.match(r"computed (\w+) of (\S+) (\S+) on ", leaf.get("source", ""))
            if not m:
                continue
            prop, comp, state = m.groups()
            self.assertEqual(str(leaf["value"]), str(bct.reading(comp, prop, state)).split(".")[0] if prop == "fontWeight" else bct.reading(comp, prop, state), path)
            n += 1
        self.assertGreaterEqual(n, 20)

    def test_plan_card_size_and_unmeasured_bold(self):
        core = bct.TREE["core"]["font"]
        self.assertEqual(core["size"]["xl"]["value"], "20px")
        self.assertTrue(core["weight"]["bold"]["source"].startswith("Reconstruction"))


if __name__ == "__main__":
    unittest.main()
