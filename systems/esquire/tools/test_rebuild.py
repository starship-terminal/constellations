"""Rebuild checks for the Esquire builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
"""
import contextlib
import importlib.util
import io
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
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        spec = importlib.util.spec_from_file_location("esquire_bt", root / "tools" / "build_tokens.py")
        cls.T = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(cls.T)  # re-runs build_tokens.py inside the temp copy

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_measurements_md_matches_rebuild(self):
        if not shutil.which("node"):
            self.skipTest("node is not installed")
        (self.root / "tools" / "capture" / "public").mkdir(parents=True, exist_ok=True)
        shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", self.root / "tools" / "capture")
        shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", self.root / "tools" / "capture" / "public")
        subprocess.run(["node", str(self.root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                       cwd=self.root, check=True, capture_output=True)
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), (self.root / "raw" / "measurements.md").read_text())

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_css_color_4_converts_or_stops(self):
        n = self.T.norm_color
        self.assertEqual(n("oklab(1 0 0)"), "#ffffff")
        self.assertEqual(n("oklab(0 0 0 / 0.5)"), "rgba(0, 0, 0, 0.5)")
        self.assertEqual(n("oklch(1 0 0)"), "#ffffff")
        self.assertEqual(n("color(srgb 1 0 0)"), "#ff0000")
        for v in ("lab(50 10 10)", "color-mix(in srgb, red, blue)"):
            with self.assertRaises(ValueError):
                n(v)
        for path, leaf in flat(self.built):
            if leaf.get("$type") == "color":
                self.assertFalse(str(leaf["$value"]).startswith(("oklab", "oklch", "lab(", "lch(", "color")), path)

    def test_two_rows_on_one_path_stop_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            b = root / "tools" / "build_component_tokens.py"
            src = b.read_text()
            marker = "\n# ------------------------------------------------------------------- fonts\n"
            self.assertIn(marker, src)
            b.write_text(src.replace(marker, marker + 'put({}, ("x",), {"v": 1})\n_t = {}\nput(_t, ("x",), {"v": 1})\nput(_t, ("x",), {"v": 2})\n', 1))
            r = subprocess.run([sys.executable, str(b)], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("two rows write this token", r.stderr)

    def test_docs_cite_only_existing_tokens(self):
        names = set()
        for theme in ("core", "light", "dark"):
            names |= {f"{theme}.{n}" for n, _ in flat(self.built[theme])}
        for doc in ("patterns.md", "components.md"):
            for m in set(re.findall(r"`((?:core|light|dark)\.[A-Za-z0-9._-]+)`", (PKG / doc).read_text())):
                self.assertTrue(m in names or any(n.startswith(m + ".") for n in names), f"{doc} cites {m}")


if __name__ == "__main__":
    unittest.main()
