"""Every committed output must rebuild from the package's inputs, byte for byte.

The builders run on a temporary copy of the package with the outputs removed first, so a builder
that writes nothing, or a committed file that went stale (raw/measurements.md was once written from
an earlier components-computed.json, with another route list and no crops), fails here. Nothing
committed is rewritten.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "style-guide.html", "components.md"]
NODE = shutil.which("node")


def run(cmd, cwd):
    """Run a builder; on failure, fail with its stdout and stderr instead of only the exit code."""
    done = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if done.returncode:
        raise AssertionError(f"{' '.join(map(str, cmd))} exited {done.returncode}\n{done.stdout}\n{done.stderr}")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        for out in OUTPUTS + ["raw/measurements.md"]:
            (cls.copy / out).unlink()
        if NODE:
            run([NODE, str(cls.copy / "tools" / "capture" / "public" / "build-measurements.mjs")], cls.copy)
        for b in BUILDERS:
            run([sys.executable, str(cls.copy / "tools" / b)], cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_bytes(), (PKG / out).read_bytes())

    @unittest.skipUnless(NODE, "node is not installed")
    def test_measurements_match_committed(self):
        out = "raw/measurements.md"
        self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
        self.assertEqual((self.copy / out).read_bytes(), (PKG / out).read_bytes())

    @unittest.skipUnless(NODE, "node is not installed")
    def test_failed_focus_is_skipped_in_measurements(self):
        # The kit's not-captured rule: a focus-visible reading taken where focus never landed is the
        # element at rest, so it is marked Skipped and its crop is not listed.
        import json
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        failed = [k for k, c in raw.items() if (c["states"].get("focus-visible") or {}).get("via") == "focus failed"]
        self.assertTrue(failed)
        text = (self.copy / "raw" / "measurements.md").read_text()
        for k in failed:
            with self.subTest(component=k):
                self.assertNotIn(f"`{k}-focus-visible.png`", text)
                section = text.split(f"#### {k}\n", 1)[1].split("\n#### ", 1)[0]
                self.assertIn("| Skipped |", section)


if __name__ == "__main__":
    unittest.main()
