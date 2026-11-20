"""Rebuild checks for the Enode builders. Run from this folder, or via tools/package_tests.py.

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
MEASURED = re.compile(r"^(computed|measured) (\w+) of ([\w-]+) ([\w-]+)[ ;(]")


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
        for theme in ("core", "light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = MEASURED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m or m.group(2) == "transition":
                    continue
                kind, prop, comp, state = m.groups()
                rd = self.C[comp]["states"][state]
                if kind == "measured":
                    raw = "%gpx" % rd["rect"][prop]
                else:
                    # The builder reads the first text node only where the source says so.
                    first = "first text node" in leaf["$extensions"]["source"]
                    raw = ((rd.get("textStyle") or {}).get(prop) if first else None) or rd["style"][prop]
                got = self.resolve(theme, leaf["$value"])
                if leaf["$type"] == "color":
                    self.assertEqual(norm(got), norm(raw), path)
                elif prop == "fontWeight":
                    self.assertEqual(got, int(float(raw)), path)
                elif str(got).endswith("px") and raw.endswith("px"):
                    self.assertAlmostEqual(float(str(got)[:-2]), float(raw[:-2]), places=2, msg=path)
                else:
                    self.assertEqual(str(got), raw, path)
                checked += 1
        self.assertGreater(checked, 35)

    def test_transition_pairs_each_property_with_its_own_timing(self):
        transition = builder_fn("transition", "\ndef st(", first="_list")
        s = self.C["nav-cta"]["states"]["default"]["style"]
        self.assertEqual(self.built["core"]["motion"]["control"]["$value"], transition(s))
        two = transition({"transitionProperty": "color, opacity", "transitionDuration": "0.1s, 0.3s",
                          "transitionTimingFunction": "ease, cubic-bezier(0.4, 0, 0.2, 1)", "transitionDelay": "0s"})
        self.assertEqual(two, "color 0.1s ease, opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1)")
        # A 0s entry overriding an earlier `all` is kept, and linear() keeps its stops.
        self.assertEqual(transition({"transitionProperty": "all, opacity", "transitionDuration": "0.2s, 0s",
                                     "transitionTimingFunction": "linear(0, 0.8 50%, 1)", "transitionDelay": "0s"}),
                         "all 0.2s linear(0, 0.8 50%, 1), opacity 0s linear(0, 0.8 50%, 1)")
        self.assertEqual(transition({"transitionProperty": "all", "transitionDuration": "0s"}), "")

    def test_focus_ring_is_read_from_a_painted_ring(self):
        ring = builder_fn("painted_ring", "\ndef transition(", first="split_shadow")
        leaf = self.built["light"]["border"]["focus-ring"]
        self.assertNotIn("nav-menu-btn", leaf["$extensions"]["source"])
        s = self.C["nav-link"]["states"]["focus-visible"]["style"]
        self.assertEqual(norm(ring(s)[0]), norm(self.resolve("light", leaf["$value"])))
        # nav-menu-btn's focus-visible outline is none/0px with no shadow: no ring.
        with self.assertRaises(KeyError):
            ring(self.C["nav-menu-btn"]["states"]["focus-visible"]["style"])

    def test_no_named_row_was_dropped(self):
        self.assertNotIn("_gaps", self.spec)


if __name__ == "__main__":
    unittest.main()
