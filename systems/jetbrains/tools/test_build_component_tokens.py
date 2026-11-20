"""raw/component-tokens.json must rebuild from the raw readings, and every value labelled as a
computed reading must be that reading.

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
            if not k.startswith("_"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((RAW / "component-tokens.json").read_text()), bct.SPEC)

    def test_computed_values_are_the_readings(self):
        n = 0
        for path, leaf in leaves(bct.SPEC):
            m = re.match(r"computed (\w+) of (\S+) (\S+) \(raw/components-computed\.json\)", leaf.get("source", ""))
            if not m:
                continue
            prop, comp, state = m.groups()
            raw = bct.C[comp]["states"][state]["style"][prop]
            self.assertEqual(str(leaf["value"]), str(raw), path)
            n += 1
        self.assertGreaterEqual(n, 12)

    def test_measured_button_and_nav(self):
        comp = bct.SPEC["component"]
        self.assertEqual(comp["button"]["padding-x"]["value"], "24px")
        self.assertEqual(comp["nav"]["height"]["value"], "72px")

    def test_no_literal_claims_a_measurement(self):
        for path, leaf in leaves(bct.SPEC):
            src = leaf.get("source", "")
            if "value" in leaf and src.startswith("measured"):
                self.fail(f"{path}: a literal labelled measured: {src}")


if __name__ == "__main__":
    unittest.main()
