"""Every committed output must rebuild from the package's inputs, byte for byte.

The builders run on a temporary copy of the package with the committed outputs removed first, so a
builder that writes nothing, or one whose output drifted from the committed file, fails here.
Nothing committed is rewritten. (test_typed_roles.py covers the token builders on their own.)
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
# In the order the README's Rebuild section runs them: components.md reads tokens.json.
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md", "style-guide.html"]
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
                self.assertEqual((self.copy / out).read_bytes(), (PKG / out).read_bytes())

    @unittest.skipUnless(NODE, "node is not installed")
    def test_measurements_match_committed(self):
        out = "raw/measurements.md"
        self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
        self.assertEqual((self.copy / out).read_bytes(), (PKG / out).read_bytes())

    def test_table_rows_have_as_many_cells_as_their_header(self):
        # A pipe inside a value (a Relume "<deleted|...>" variable name, say) would split its cell.
        width = None
        for n, line in enumerate((self.copy / "components.md").read_text().splitlines(), 1):
            if not line.startswith("|"):
                width = None
                continue
            cells = len(re.findall(r"(?<!\\)\|", line)) - 1
            if width is None:
                width = cells
            with self.subTest(line=n):
                self.assertEqual(cells, width, line[:120])


if __name__ == "__main__":
    unittest.main()
