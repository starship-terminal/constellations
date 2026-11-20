"""Every committed output must rebuild from the package's inputs, byte for byte.

The builders run on a temporary copy of the package with the outputs removed first, so a builder
that writes nothing, or a committed file that went stale (components.md once listed 39 icons, one
of them a file icons/ no longer has, where icons/INDEX.tsv holds 49), fails here. Nothing committed
is rewritten.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
# In the order the README's Rebuild section runs them.
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

    def test_icon_links_resolve(self):
        links = re.findall(r"\]\((icons/[^)]+\.svg)\)", (PKG / "components.md").read_text())
        self.assertTrue(links)
        for link in links:
            with self.subTest(link=link):
                self.assertTrue((PKG / link).exists())


if __name__ == "__main__":
    unittest.main()
