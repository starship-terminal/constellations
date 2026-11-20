"""raw/component-tokens.json must rebuild from the raw readings, weight keys
must name a role (never an assumed weight), and every token read from an
overwritten component must say so.

Run from the package root: python3 -m unittest discover -s tools
"""
import contextlib
import io
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
with contextlib.redirect_stdout(io.StringIO()):
    import build_component_tokens as bct  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent


def leaves(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("_"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((HERE / "raw" / "component-tokens.json").read_text()), bct.SPEC)

    def test_weight_keys_are_roles(self):
        names = {"thin": 100, "light": 300, "regular": 400, "medium": 500, "semibold": 600, "bold": 700, "black": 900}
        for key, leaf in bct.SPEC["core"]["font"]["weight"].items():
            if key in names:
                self.assertEqual(int(leaf["value"]), names[key], key)
        self.assertNotIn("bold", bct.SPEC["core"]["font"]["weight"])

    def test_overwritten_readings_are_flagged(self):
        for path, leaf in leaves(bct.SPEC):
            for comp in bct.OVERWRITTEN:
                if f" {comp} " in leaf["source"]:
                    self.assertIn("recapture needed", leaf["source"], path)

    def test_icons_have_their_use_targets(self):
        import re
        for svg in (HERE / "icons").glob("*.svg"):
            s = svg.read_text()
            ids = set(re.findall(r'id="([^"]+)"', s))
            for ref in re.findall(r'href="#([^"]+)"', s):
                self.assertIn(ref, ids, svg.name)


if __name__ == "__main__":
    unittest.main()
