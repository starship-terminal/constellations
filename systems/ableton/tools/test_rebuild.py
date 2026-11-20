"""The committed outputs must rebuild from the package's inputs, byte for byte.

The builders run on a temporary copy of the package with the committed outputs removed first, so a
builder that writes nothing, or one whose output drifted from the committed file, fails here.
Nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
# In the order the README's Rebuild section runs them: components.md reads tokens.json.
BUILDERS = ["build_tokens.py", "build_style_guide.py", "build_components_md.py"]
OUTPUTS = ["tokens.json", "style-guide.html", "components.md"]
NODE = shutil.which("node")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        for out in OUTPUTS + ["raw/measurements.md"]:
            (cls.copy / out).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True, cwd=cls.copy)
        if NODE:
            subprocess.run([NODE, str(cls.copy / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           check=True, capture_output=True, cwd=cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    @unittest.skipUnless(NODE, "node is not installed")
    def test_measurements_match_committed(self):
        out = "raw/measurements.md"
        self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
        self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_failed_focus_is_not_published_as_a_reading(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        failed = [k for k, c in raw.items() if (c.get("states", {}).get("focus-visible") or {}).get("via") == "focus failed"]
        self.assertTrue(failed, "expected at least one focus-failed state in the raw readings")
        text = (self.copy / "components.md").read_text()
        focus = next(line for line in text.splitlines() if line.startswith("**Focus.**"))
        for k in failed:
            with self.subTest(component=k):
                self.assertNotIn(f"crops/{k}-focus-visible.png", text)
                self.assertNotIn(f"`{k}`", focus.split("draw none")[1].split("Focus could not be captured")[0])
                self.assertIn(f"`{k}`", focus.split("Focus could not be captured")[1])


if __name__ == "__main__":
    unittest.main()
