"""raw/measurements.md must rebuild from raw/components-computed.json and name avnier's own source.

build-measurements.mjs runs on a temporary copy of the package with the committed file removed, so
nothing committed is rewritten. Its intro once said the readings came from asos.com in headed
Chrome past an Akamai wall, text copied from the asos package's builder.
"""
import pathlib
import shutil
import subprocess
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
NODE = shutil.which("node")
OUT = "raw/measurements.md"


@unittest.skipUnless(NODE, "node is not installed")
class MeasurementsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
        (copy / OUT).unlink()
        subprocess.run([NODE, str(copy / "tools" / "capture" / "public" / "build-measurements.mjs")],
                       check=True, capture_output=True, cwd=copy)
        cls.rebuilt = copy / OUT

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_matches_committed(self):
        self.assertTrue(self.rebuilt.exists(), f"{OUT} was not rebuilt")
        self.assertEqual(self.rebuilt.read_bytes(), (PKG / OUT).read_bytes())

    def test_names_avnier_as_the_source(self):
        text = self.rebuilt.read_text()
        self.assertIn("Computed styles read from avnier.com", text)
        for word in ("asos", "onetrust", "akamai", "headed chrome"):
            self.assertNotIn(word, text.lower())


if __name__ == "__main__":
    unittest.main()
