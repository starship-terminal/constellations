"""The committed token files must rebuild from the raw readings, and the font stacks must be the
computed ones. The builders run on a temporary copy of the package, so nothing committed is
rewritten."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class BuildersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in ("raw/component-tokens.json", "tokens.json"):
            with self.subTest(out=out):
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_font_families_are_the_computed_stacks(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        fam = json.loads((self.copy / "tokens.json").read_text())["core"]["font"]["family"]
        self.assertEqual(fam["legacy"]["$value"], raw["promo-strip"]["states"]["default"]["style"]["fontFamily"])
        self.assertEqual(fam["primary"]["$value"], raw["pdp-price"]["states"]["default"]["style"]["fontFamily"])


if __name__ == "__main__":
    unittest.main()
