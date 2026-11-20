"""raw/component-tokens.json must rebuild from the raw readings: no transparent fill is
committed, gradient-faced buttons carry their gradient, and the focus ring is the ring painted.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_component_tokens as bct  # noqa: E402

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"


def leaves(node):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        yield node
    elif isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("_"):
                yield from leaves(v)


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((RAW / "component-tokens.json").read_text()), bct.SPEC)

    def test_no_transparent_fill(self):
        for leaf in leaves(bct.SPEC):
            if leaf["type"] == "color" and "value" in leaf:
                self.assertIsNone(bct.TRANSPARENT.fullmatch(str(leaf["value"])), leaf["source"])

    def test_gradient_buttons(self):
        fill = bct.SPEC["dark"]["action"]["heroCtaFill"]
        self.assertEqual(fill["type"], "gradient")
        self.assertEqual(fill["value"], [{"color": "#adadad", "position": 0.2}, {"color": "#cacaca", "position": 0.8}])
        self.assertEqual(fill["angle"], "0deg")

    def test_focus_ring_is_the_painted_ring(self):
        # nav-cta focus-visible: outline none 0px, ring drawn as a 2px box-shadow spread.
        ring = bct.SPEC["dark"]["border"]["focusRing"]
        self.assertIn("boxShadow ring", ring["source"])


if __name__ == "__main__":
    unittest.main()
