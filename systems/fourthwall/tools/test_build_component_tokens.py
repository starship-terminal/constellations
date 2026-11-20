"""raw/component-tokens.json must rebuild from the raw readings, commit no
transparent fill, write valid transition shorthands and alias text roles to
text names.

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
            if not k.startswith("_") or k in ("_primitives", "_surface", "_rhythm"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((RAW / "component-tokens.json").read_text()), bct.SPEC)

    def test_no_transparent_measured_fill(self):
        for path, leaf in leaves(bct.SPEC):
            if leaf["type"] != "color" or "value" not in leaf:
                continue
            self.assertIsNone(bct.TRANSPARENT.fullmatch(str(leaf["value"])), path)
            m = re.fullmatch(r"\{(.+)\}", str(leaf["value"]))
            if m and "computed backgroundColor" in leaf["source"]:
                theme = path.split(".")[0]
                self.assertIsNone(bct.TRANSPARENT.fullmatch(bct.PATHVAL[theme].get(m.group(1), "")),
                                  f"{path} aliases a transparent name")

    def test_transition_is_valid_shorthand(self):
        v = bct.SPEC["core"]["motion"]["control"]["value"]
        self.assertEqual(v, "background-color 0.32s ease 0.18s, color 0.32s ease 0.18s")
        for part in v.split(", "):
            self.assertRegex(part, r"^[a-z-]+ [\d.]+m?s \S+( [\d.]+m?s)?$")

    def test_text_roles_alias_text_names(self):
        for theme in ("help", "helpDark"):
            self.assertEqual(bct.SPEC[theme]["text"]["ink"]["value"], "{fw.text.primary}")

    def test_sets_keep_their_own_paths(self):
        # every set's emitted path exists in that set's own tree
        for setname in bct.SETS:
            for name, path in bct.E(setname).items():
                node = bct.SPEC[setname]
                for p in path.split("."):
                    node = node[p]
                self.assertEqual(node.get("var"), name, f"{setname}: {name} -> {path}")


if __name__ == "__main__":
    unittest.main()
