"""Checks for the Lulu and Georgia builders. Run from this folder, or via tools/package_tests.py.

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
    v = json.loads((d / "components-computed.json").read_text())
    edit(v)
    (d / "components-computed.json").write_text(json.dumps(v))
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

    def test_button_type_is_the_reading(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]["atc"]["states"]["default"]
        button = json.loads((PKG / "tokens.json").read_text())["core"]["typography"]["button"]["$value"]
        self.assertEqual((button["fontSize"], button["lineHeight"], button["letterSpacing"]),
                         (raw["fontSize"], raw["lineHeight"], raw["letterSpacing"]))

    def test_colours_with_no_reading_say_so(self):
        light = json.loads((PKG / "tokens.json").read_text())["light"]["color"]
        for tok in (light["promo"], light["cream"], light["info"], light["border"]["strong"]):
            self.assertTrue(tok["$extensions"]["source"].startswith("Reconstruction"), tok)

    def test_a_missing_reading_fails_instead_of_a_literal(self):
        raw = scratch_raw(lambda v: v["components"]["atc"]["states"].pop("default"))
        proc, _ = self.build("build_tokens.py", raw=raw, extra=())
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("atc default", proc.stderr)

    def test_style_guide_script_reads_the_slim_tree(self):
        script = (PKG / "style-guide.html").read_text().split("<script>", 1)[1]
        self.assertNotIn("$value", script)
        self.assertIn("v.v", script)


if __name__ == "__main__":
    unittest.main()
