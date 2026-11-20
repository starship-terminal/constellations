"""Rebuild checks for the Epic Games builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ (without capture/) and raw/, with
empty stand-ins for the screenshot and crop files (only their names are read),
so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def builder_fn(name, end, first=None):
    """A helper from the token builder, loaded without running the build
    (the source from `def first` or `def name` up to `end`)."""
    src = (PKG / "tools" / "build_component_tokens.py").read_text()
    start = src.index(f"def {first or name}(")
    ns = {"re": re}
    exec(src[start:src.index(end, start)], ns)
    return ns[name]


norm = builder_fn("norm_color", "\ndef have(")
MEASURED = re.compile(r"^(computed|measured) (\w+) of ([\w-]+) ([\w-]+) \(raw/components-computed\.json\)")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components/crops"):
            (root / d).mkdir(parents=True)
            for f in (PKG / d).glob("*.png"):
                (root / d / f.name).touch()
        for b in ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def resolve(self, theme, v):
        while isinstance(v, str) and v.startswith("{"):
            node = None
            for s in (theme, "core"):
                node = self.built[s]
                for part in v[1:-1].split("."):
                    node = node.get(part) if isinstance(node, dict) else None
                if node:
                    break
            v = node["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        for f in ("tokens.json", "raw/component-tokens.json", "components.md", "style-guide.html"):
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_measured_leaves_equal_their_reading(self):
        checked = 0
        for theme in ("core", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = MEASURED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m or m.group(2) == "transition":
                    continue
                kind, prop, comp, state = m.groups()
                rd = self.C[comp]["states"][state]
                if kind == "measured":
                    raw = "%gpx" % rd["rect"][prop]
                else:
                    raw = (rd.get("textStyle") or {}).get(prop) or rd["style"][prop]
                got = self.resolve(theme, leaf["$value"])
                if leaf["$type"] == "color":
                    self.assertEqual(norm(got), norm(raw), path)
                elif prop == "fontWeight":
                    self.assertEqual(got, int(float(raw)), path)
                else:
                    self.assertEqual(str(got), raw, path)
                checked += 1
        self.assertGreater(checked, 40)

    def test_transition_pairs_each_property_with_its_own_timing(self):
        s = self.C["nav-signin"]["states"]["default"]["style"]
        self.assertEqual(s["transitionProperty"], "color, background-color")
        self.assertEqual(self.built["core"]["motion"]["control"]["$value"],
                         "color 0.12s cubic-bezier(0.65, 0, 0.35, 1), background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1)")

    def test_focus_ring_is_a_painted_ring(self):
        ring = builder_fn("painted_ring", "\ndef transition(", first="split_shadow")
        s = self.C["store-tab"]["states"]["focus-visible"]["style"]
        self.assertEqual(norm(ring(s)[0]), norm(self.resolve("dark", self.built["dark"]["border"]["focus"]["$value"])))
        # An outline colour under outline-style none is not a ring.
        with self.assertRaises(KeyError):
            ring({"outlineStyle": "none", "outlineWidth": "0px", "outlineColor": "rgb(1, 2, 3)", "boxShadow": "none"})
        with self.assertRaises(KeyError):
            ring({"outlineStyle": "auto", "outlineWidth": "1px", "outlineColor": "rgb(1, 2, 3)", "boxShadow": "none"})

    def test_font_sizes_use_a_dtcg_type(self):
        for path, leaf in flat(self.built["core"]["font"]["size"]):
            self.assertEqual(leaf["$type"], "dimension", path)

    def test_missing_rows_are_listed_not_dropped(self):
        self.assertEqual(len(self.spec["_gaps"]), 4)
        self.assertNotIn("drawer", self.built["core"]["shadow"])

    def test_failed_focus_is_not_published_as_a_reading(self):
        md = (PKG / "raw" / "measurements.md").read_text()
        block = md.split("#### nav-signin", 1)[1].split("\n#### ", 1)[0]
        self.assertIn("| Skipped |", block)
        comp = (PKG / "components.md").read_text()
        self.assertIn("**Known-wrong reading.**", comp.split("Read as `m-hamburger`", 1)[1].split("\n#### ", 1)[0])


if __name__ == "__main__":
    unittest.main()
