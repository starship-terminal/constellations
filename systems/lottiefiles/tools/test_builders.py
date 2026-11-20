"""Checks for the LottieFiles builders. Run from this folder, or via tools/package_tests.py.

Each builder runs in a scratch folder that links the package's inputs, so a fresh build is
compared with the committed file without rewriting it.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def run(builder, raw=None, extra=("screenshots", "components", "tokens.json")):
    """Run tools/<builder> in a scratch package; return (process, scratch root kept open by caller)."""
    d = tempfile.mkdtemp()
    root = pathlib.Path(d)
    (root / "tools").mkdir()
    for name in ("build_tokens.py", "build_components_md.py", "build_style_guide.py", "style-guide.template.html"):
        shutil.copy(PKG / "tools" / name, root / "tools" / name)
    for name in extra:
        if (PKG / name).exists():
            os.symlink(PKG / name, root / name)
    os.symlink(raw or PKG / "raw", root / "raw")
    proc = subprocess.run([sys.executable, str(root / "tools" / builder)], capture_output=True, text=True)
    return proc, root


def scratch_raw(edit):
    d = pathlib.Path(tempfile.mkdtemp()) / "raw"
    shutil.copytree(PKG / "raw", d)
    v = json.loads((d / "css-vars.json").read_text())
    edit(v["resolved"]["light"])
    (d / "css-vars.json").write_text(json.dumps(v))
    return d


class Builders(unittest.TestCase):
    def tearDown(self):
        for root in getattr(self, "roots", []):
            shutil.rmtree(root, ignore_errors=True)

    def build(self, builder, **kw):
        proc, root = run(builder, **kw)
        self.roots = getattr(self, "roots", []) + [root]
        return proc, root

    def test_tokens_match_the_build(self):
        proc, root = self.build("build_tokens.py", extra=())
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual((root / "tokens.json").read_text(), (PKG / "tokens.json").read_text())

    def test_components_md_matches_the_build(self):
        proc, root = self.build("build_components_md.py")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual((root / "components.md").read_text(), (PKG / "components.md").read_text())

    def test_style_guide_matches_the_build(self):
        proc, root = self.build("build_style_guide.py")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual((root / "style-guide.html").read_text(), (PKG / "style-guide.html").read_text())

    def test_every_declared_shadow_is_an_elevation_token(self):
        elevation = json.loads((PKG / "tokens.json").read_text())["core"]["elevation"]
        self.assertEqual(sorted(elevation), ["lg", "md", "sm"])
        self.assertEqual(elevation["md"]["$value"][0]["spread"], "-1px")

    def test_an_inset_layer_keeps_inset(self):
        raw = scratch_raw(lambda light: light.__setitem__("--shadow-sm", {"value": "0 1px 2px 0 #0000000d inset", "raw": ""}))
        proc, root = self.build("build_tokens.py", raw=raw, extra=())
        self.assertEqual(proc.returncode, 0, proc.stderr)
        layer = json.loads((root / "tokens.json").read_text())["core"]["elevation"]["sm"]["$value"][0]
        self.assertTrue(layer["inset"])
        self.assertEqual(layer["offsetX"], "0px")

    def test_a_missing_reading_fails_instead_of_a_literal(self):
        raw = scratch_raw(lambda light: light.pop("--font-sans"))
        proc, _ = self.build("build_tokens.py", raw=raw, extra=())
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--font-sans missing", proc.stderr)

    def test_style_guide_script_reads_the_slim_tree(self):
        html = (PKG / "style-guide.html").read_text()
        script = html.split("<script>", 1)[1]
        self.assertNotIn("$value", script)
        self.assertIn("t.v", script)


if __name__ == "__main__":
    unittest.main()
