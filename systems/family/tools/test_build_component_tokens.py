"""raw/component-tokens.json must rebuild from the raw readings; no role is a transparent
fill and no size carries the non-DTCG type "fontSize".

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
                self.assertIsNone(bct.TRANSPARENT.fullmatch(str(leaf["value"])), leaf.get("source"))

    def test_field_sits_on_the_declared_input_fill(self):
        self.assertEqual(bct.SPEC["light"]["background"]["field"]["value"], "{color.input.background.default}")

    def test_emit_collision_raises_value_error(self):
        root = {}
        bct.emit(root, "--zz-a", {"var": "--zz-a", "type": "color"})
        bct.emit(root, "--zz-a-b", {"var": "--zz-a-b", "type": "color"})
        for k in ("base", "self"):
            root["zz"]["a"][k] = {"value": "#000000", "type": "color"}
        with self.assertRaises(ValueError):
            bct.emit(root, "--zz-a", {"var": "--zz-a", "type": "color"})

    def test_no_fontsize_type(self):
        self.assertNotIn("fontSize", {leaf["type"] for leaf in leaves(bct.SPEC)})


if __name__ == "__main__":
    unittest.main()
