"""Checks for the Lovable builders. Run from this folder, or via tools/package_tests.py.

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

    def test_a_failed_focus_is_not_a_reading(self):
        # A fixture, not the committed readings: a recapture that fixes the focus must not fail this.
        with tempfile.TemporaryDirectory() as d:
            raw = pathlib.Path(d) / "raw"
            shutil.copytree(PKG / "raw", raw)
            v = json.loads((raw / "components-computed.json").read_text())
            v["components"]["nav-link"]["states"]["focus-visible"]["via"] = "focus failed"
            (raw / "components-computed.json").write_text(json.dumps(v))
            proc, root = self.build("build_components_md.py", raw=raw)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            md = (root / "components.md").read_text()
        focus = md.split("**Focus.**", 1)[1].split("\n", 1)[0]
        shown, not_captured = focus.split("Focus could not be captured", 1)
        self.assertNotIn("`nav-link`", shown)
        self.assertIn("`nav-link`", not_captured)
        self.assertNotIn("components/crops/nav-link-focus-visible.png", md)

    def test_aliases_carry_no_set_name(self):
        text = (PKG / "tokens.json").read_text()
        self.assertNotIn("{core.", text)
        self.assertNotIn("{light.", text)

    def test_glow_tints_are_not_named_as_fills(self):
        light = json.loads((PKG / "tokens.json").read_text())["light"]
        self.assertNotIn("accentHover", light)
        self.assertEqual(light["accentHoverGlow"]["$extensions"]["source"].split()[1], "--glow-accent-hover")


if __name__ == "__main__":
    unittest.main()
