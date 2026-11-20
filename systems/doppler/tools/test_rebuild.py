"""Rebuild checks for the Doppler builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
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
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from flat(v, p)


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
        for b in ("build_component_tokens.py", "build_tokens.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.md = (root / "components.md").read_text()
        cls.tok = dict(flat(cls.built))
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_font_stacks_and_weights_are_the_readings(self):
        fam = {k: self.tok[f"core.font.family.{k}"]["$value"] for k in ("sans", "mono", "inter")}
        for k, comp in (("sans", "header"), ("mono", "code-chip"), ("inter", "check-item")):
            self.assertEqual(fam[k], self.C[comp]["states"]["default"]["style"]["fontFamily"], k)
        for k, comp in (("regular", "hero-sub"), ("mid", "hero-title"), ("medium", "search-field"), ("bold", "nav-link")):
            self.assertEqual(self.tok[f"core.font.weight.{k}"]["$value"], int(self.C[comp]["states"]["default"]["style"]["fontWeight"]), k)

    def test_stale_and_wrong_readings_say_so(self):
        self.assertIn("recaptureMissed", self.tok["dark.component.control.gap"]["$extensions"]["source"])
        self.assertIn("wrong element", self.tok["dark.component.control.heightButton"]["$extensions"]["source"])
        self.assertIn("**Known wrong; recapture needed.**", self.md.split("Read as `hero-cta`")[1].split("####")[0])

    def test_tailwind_opacity_fallback_is_kept(self):
        import runpy
        ns = runpy.run_path(str(pathlib.Path(self.tmp.name) / "tools" / "build_component_tokens.py"))
        self.assertEqual(ns["norm_color"]("rgb(28 22 36/var(--tw-bg-opacity,1))"), "#1c1624")
        self.assertEqual(ns["norm_color"]("rgb(28 22 36/var(--tw-bg-opacity,0.5))"), "rgba(28, 22, 36, 0.5)")


    def test_measurements_rebuild_matches(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        root = pathlib.Path(self.tmp.name)
        (root / "tools" / "capture" / "public").mkdir(parents=True, exist_ok=True)
        shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", root / "tools" / "capture")
        shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", root / "tools" / "capture" / "public")
        subprocess.run([node, str(root / "tools" / "capture" / "public" / "build-measurements.mjs")], cwd=root, check=True, capture_output=True)
        built = (root / "raw" / "measurements.md").read_text()
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), built)

    def rebuild_with(self, edit_utilities=None, edit_components=None):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d)
        root = pathlib.Path(d)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d_ in ("screenshots", "components/crops"):
            (root / d_).mkdir(parents=True)
        for name, edit in (("utility-classes.json", edit_utilities), ("components-computed.json", edit_components)):
            if edit:
                f = root / "raw" / name
                j = json.loads(f.read_text())
                edit(j)
                f.write_text(json.dumps(j))
        for b in ("build_component_tokens.py", "build_tokens.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        return root

    def test_tailwind_opacity_reaches_tokens_json(self):
        def half(j):
            for r in j["classes"]:
                if r["selector"] == ".bg-warm-black":
                    r["properties"]["background-color"] = "rgb(28 22 36/var(--tw-bg-opacity,0.5))"
        root = self.rebuild_with(edit_utilities=half)
        out = json.loads((root / "tokens.json").read_text())
        self.assertEqual(out["core"]["color"]["warm"]["black"]["$value"], "rgba(28, 22, 36, 0.5)")

    def test_failed_focus_is_left_out(self):
        # doppler's own readings have no failed focus: plant one and a skipped state.
        def plant(j):
            j["components"]["nav-cta"]["states"]["focus-visible"]["via"] = "focus failed"
            j["components"]["nav-link"]["states"]["focus-visible"] = {"skipped": "focus failed: keyboard focus did not reach the element"}
        root = self.rebuild_with(edit_components=plant)
        md = (root / "components.md").read_text()
        self.assertIn("Focus could not be captured on 2 more", md)
        rings = re.search(r"\*\*Focus\.\*\* .*", md).group(0).split("Focus could not be captured")[0]
        self.assertNotIn("`nav-cta`", rings)
        node = shutil.which("node")
        if node:
            subprocess.run([node, str(root / "tools" / "capture" / "public" / "build-measurements.mjs")], cwd=root, check=True, capture_output=True)
            m = (root / "raw" / "measurements.md").read_text()
            for k in ("nav-cta", "nav-link"):
                self.assertIn("| Skipped |", m.split(f"#### {k}\n")[1].split("\n#### ")[0], k)

if __name__ == "__main__":
    unittest.main()
