"""Rebuild checks for the Endless builders. Run from this folder, or via tools/package_tests.py.

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
sys.path.insert(0, str(PKG / "tools"))


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def norm(v):
    """The builder's own colour normaliser, imported without running the build."""
    src = (PKG / "tools" / "build_component_tokens.py").read_text()
    start = src.index("def _gam(")
    end = src.index("\ndef have(")
    ns = {"re": re}
    exec(src[start:end], ns)
    return ns["norm_color"](v)


COMPUTED = re.compile(r"^computed (\w+) of ([\w-]+) ([\w-]+) \(raw/components-computed\.json\)$")


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
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        cls.V = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]["light"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for f in ("tokens.json", "raw/component-tokens.json", "components.md", "style-guide.html"):
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_computed_leaves_equal_their_reading(self):
        checked = 0
        for theme in ("core", "light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = COMPUTED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m:
                    continue
                prop, comp, state = m.groups()
                rd = self.C[comp]["states"][state]
                if prop == "type":
                    s = rd["style"]
                    v = leaf["$value"]
                    self.assertEqual(v["fontFamily"], s["fontFamily"], path)
                    self.assertEqual(v["fontSize"], s["fontSize"], path)
                    self.assertEqual(v["lineHeight"], s["lineHeight"], path)
                    self.assertEqual(v["fontWeight"], int(float(s["fontWeight"])), path)
                elif prop in ("boxShadow", "transition"):
                    continue  # parsed values; covered by their own tests
                elif path == "radius.pill":
                    # rounded-full computes as 3.35544e+07px; the description says it is stored as 9999px
                    self.assertTrue(rd["style"][prop].startswith("3.35544e+07"), path)
                else:
                    raw = (rd.get("textStyle") or {}).get(prop) or rd["style"][prop]
                    want = norm(raw) if leaf["$type"] == "color" else raw
                    self.assertEqual(leaf["$value"], want, path)
                checked += 1
        self.assertGreater(checked, 30)

    def test_dark_components_are_labelled_from_the_dark_set(self):
        md = (PKG / "components.md").read_text()
        dark = md.split("### Dark theme (system dark)", 1)[1].split("\n### ", 1)[0]
        self.assertNotIn("`light.", dark)
        self.assertIn("#fafafa `dark.foreground`", dark)

    def test_quoted_font_family_cannot_close_the_style_attribute(self):
        tpl = (PKG / "tools" / "style-guide.template.html").read_text()
        self.assertNotRegex(tpl, r'style="[^"`]*\$\{v\.fontFamily\}')
        self.assertTrue(any('"' in t["$value"]["fontFamily"] for _, t in flat(self.built["core"]["font"]["type"])))

    def test_icon_button_size_is_not_read_from_the_attach_button(self):
        leaf = self.built["light"]["component"]["icon-button"]["size"]
        self.assertNotIn("composer-send", leaf["$extensions"]["source"])
        self.assertEqual(self.C["m-menu-button"]["states"]["default"]["style"]["height"], leaf["$value"])

    def test_focus_ring_cites_only_components_that_paint_it(self):
        src = self.built["core"]["measured"]["focus-ring"]["$extensions"]["source"]
        names = re.search(r"borderTopColor of (.+) == --ring", src).group(1).split(", ")
        ring = self.V["--ring"]["value"]
        for k in names:
            st = self.C[k]["states"]["focus-visible"]
            self.assertNotEqual(st.get("via"), "focus failed", k)
            self.assertEqual(norm(st["style"]["borderTopColor"]), ring, k)
        spread = self.built["core"]["measured"]["focus-ring-width"]["$value"]
        self.assertIn(f"0px {spread}", self.C["nav-signin"]["states"]["focus-visible"]["style"]["boxShadow"])

    def test_missing_reading_stops_the_build(self):
        """A recapture that loses a declared variable or a component reading
        must fail the build, not drop the token, and leave the spec as it was."""
        for drop in ("var", "component"):
            with tempfile.TemporaryDirectory() as d:
                root = pathlib.Path(d)
                shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
                shutil.copytree(PKG / "raw", root / "raw")
                if drop == "var":
                    f = root / "raw" / "css-vars.json"
                    v = json.loads(f.read_text())
                    del v["resolved"]["light"]["--spacing"]
                else:
                    f = root / "raw" / "components-computed.json"
                    v = json.loads(f.read_text())
                    del v["components"]["m-menu-button"]
                f.write_text(json.dumps(v))
                before = (root / "raw" / "component-tokens.json").read_text()
                r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)
                self.assertNotEqual(r.returncode, 0, drop)
                self.assertIn("missing readings", r.stderr, drop)
                self.assertEqual((root / "raw" / "component-tokens.json").read_text(), before, drop)

    def test_no_named_row_was_dropped(self):
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())
        self.assertNotIn("_gaps", spec)


if __name__ == "__main__":
    unittest.main()
