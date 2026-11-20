"""Rebuild checks for the District builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots/, components/ and icons/ are
linked read-only), so nothing committed is rewritten.
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
BUILDERS = ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py")
OUTPUTS = ("tokens.json", "raw/component-tokens.json", "style-guide.html", "components.md")


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
        cls.root = root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components", "icons"):
            if (PKG / d).exists():
                (root / d).symlink_to(PKG / d)
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for f in OUTPUTS:
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_page_field_and_dark_ink_are_read_not_typed(self):
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())
        page = spec["light"]["background"]["page"]
        self.assertTrue(page["source"].startswith("declared --color-background-primary"), page["source"])
        self.assertEqual(V["resolved"]["light"]["--color-background-primary"]["value"], "#ffffff")
        ink = spec["dark"]["text"]["ink"]
        self.assertTrue(ink["source"].startswith("computed color of dk-nav default"), ink["source"])
        self.assertEqual(self.C["dk-nav"]["states"]["default"]["style"]["color"], "rgb(247, 247, 247)")

    def test_page_field_and_dark_ink_follow_their_inputs(self):
        """Change the declaration and the reading on a temp copy: a builder that typed the old
        constants back would still pass the label checks above, not this one."""
        root = pathlib.Path(self.tmp.name) / "moved"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        vp = root / "raw" / "css-vars.json"
        V = json.loads(vp.read_text())
        V["resolved"]["light"]["--color-background-primary"] = {"raw": "#fafafa", "kind": "color", "value": "#fafafa"}
        vp.write_text(json.dumps(V))
        cp = root / "raw" / "components-computed.json"
        J = json.loads(cp.read_text())
        J["components"]["dk-nav"]["states"]["default"]["style"]["color"] = "rgb(240, 241, 242)"
        cp.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, check=True, capture_output=True)
        spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        # it aliases the declaration it read; the old typed #ffffff would not match #fafafa
        self.assertEqual(spec["light"]["background"]["page"]["value"], "{color.background.primary}")
        self.assertEqual(spec["dark"]["text"]["ink"]["value"].lower(), "#f0f1f2")

    def test_wrong_element_reading_is_flagged(self):
        src = self.built["core"]["font"]["size"]["measured"]["display"]["$extensions"]["source"]
        self.assertIn("read from the wrong element; recapture needed", src)
        self.assertLess(self.C["ev-h1"]["states"]["default"]["rect"]["x"], 0)

    def test_recaptured_heading_clears_the_flag(self):
        root = pathlib.Path(self.tmp.name) / "recaptured"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        path = root / "raw" / "components-computed.json"
        J = json.loads(path.read_text())
        J["components"]["ev-h1"]["states"]["default"]["rect"].update({"x": 80, "y": 120})
        path.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, check=True, capture_output=True)
        spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        self.assertNotIn("wrong element", spec["core"]["font"]["size"]["measured"]["display"]["source"])

    def test_dark_theme_comes_from_the_page(self):
        md = (PKG / "tools" / "build_components_md.py").read_text()
        self.assertNotIn("Server discovery", md)
        self.assertEqual({c["page"] for c in self.C.values() if c.get("group", "").startswith("Dark theme")}, {"homeDark"})

    def test_colours_are_named_from_their_theme_before_core(self):
        # A colour a theme role shares with a core step is named by the theme role: the dark
        # page #131316 is dark background.primary, not the core button-outline-text step.
        T = json.loads((PKG / "tokens.json").read_text())
        names = {s: {} for s in ("light", "dark")}
        for s in names:
            for n, t in flat(T[s]):
                if t.get("$type") == "color" and isinstance(t["$value"], str) and t["$value"].startswith("#"):
                    names[s].setdefault(t["$value"].lower(), set()).add(n)
        md = (self.root / "components.md").read_text()
        dark = md[md.index("### Dark theme (data-theme=dark)"):]
        dark = dark[:dark.index("\n### ", 1)] if "\n### " in dark[1:] else dark
        self.assertIn("background #131316 `color.background.primary`", dark)
        for section, theme in ((md[:md.index("### Dark theme (data-theme=dark)")], "light"), (dark, "dark")):
            for hexv, name in re.findall(r"(#[0-9a-f]{6}) `([^`]+)`", section):
                if hexv in names[theme]:
                    self.assertIn(name, names[theme][hexv], f"{theme} {hexv} named {name}")


if __name__ == "__main__":
    unittest.main()
