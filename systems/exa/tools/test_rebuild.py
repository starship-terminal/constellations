"""Rebuild checks for the Exa builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
"""
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
COMPUTED = re.compile(r"^computed (\w+) of (\S+) (\S+) \(raw/components-computed\.json\)")


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        spec = importlib.util.spec_from_file_location("exa_bct", root / "tools" / "build_component_tokens.py")
        cls.B = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.B)  # re-runs the builder inside the temp copy
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        cls.core = dict(flat(cls.built["core"]))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def resolve(self, v):
        while isinstance(v, str) and v.startswith("{"):
            v = self.core[v[1:-1]]["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_computed_colour_leaves_equal_the_reading(self):
        n = 0
        for theme in ("light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = COMPUTED.match(leaf["$extensions"]["source"])
                if not m or leaf["$type"] != "color":
                    continue
                prop, comp, state = m.groups()
                raw = self.C[comp]["states"][state]["style"][prop]
                self.assertEqual(self.resolve(leaf["$value"]), self.B.css_color(raw), f"{theme}.{path}")
                n += 1
        self.assertGreater(n, 20)

    def test_no_surface_is_transparent(self):
        for theme in ("light", "dark"):
            for path, leaf in flat(self.built[theme]):
                if leaf["$type"] == "color":
                    self.assertFalse(self.B.transparent(self.resolve(leaf["$value"])), f"{theme}.{path}")
        gaps = {g["token"] for g in self.spec["_gaps"]}
        for t in ("light.signin.card", "light.docs.field", "dark.docs.code-bg", "light.marketing.focus"):
            self.assertIn(t, gaps)

    def test_focus_rings_are_the_painted_shadow(self):
        for theme, comp in (("light", "docs-search"), ("dark", "d-docs-search")):
            sty = self.C[comp]["states"]["focus-visible"]["style"]
            self.assertEqual(sty["outlineStyle"], "none")
            ring = re.match(r"(rgba?\([^)]*\))", sty["boxShadow"]).group(1)
            self.assertEqual(self.resolve(self.built[theme]["docs"]["focus"]["$value"]), self.B.css_color(ring))

    def test_transition_pairs_each_property_with_its_timing(self):
        sty = self.C["mkt-nav-link"]["states"]["default"]["style"]
        props = [p.strip() for p in sty["transitionProperty"].split(",")]
        items = re.split(r",\s*(?![^()]*\))", self.core["motion.control"]["$value"])
        self.assertEqual([i.split()[0] for i in items], props)
        for i in items:
            self.assertEqual(i.split(" ", 1)[1], f"{sty['transitionDuration']} {sty['transitionTimingFunction']}")

    def test_font_sizes_are_dimensions(self):
        for path, leaf in flat(self.built["core"]["font"]["size"]):
            self.assertEqual(leaf["$type"], "dimension", path)


if __name__ == "__main__":
    unittest.main()
