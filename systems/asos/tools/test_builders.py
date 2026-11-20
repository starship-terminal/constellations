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
        # Remove the committed outputs from the copy first, so a builder that
        # writes nothing cannot pass by leaving the committed file in place.
        for out in ("raw/component-tokens.json", "tokens.json"):
            (cls.copy / out).unlink()
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in ("raw/component-tokens.json", "tokens.json"):
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_font_families_are_the_computed_stacks(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        fam = json.loads((self.copy / "tokens.json").read_text())["core"]["font"]["family"]
        self.assertEqual(fam["legacy"]["$value"], raw["promo-strip"]["states"]["default"]["style"]["fontFamily"])
        self.assertEqual(fam["primary"]["$value"], raw["pdp-price"]["states"]["default"]["style"]["fontFamily"])


class BadReadingsTest(unittest.TestCase):
    """The font rows refuse a missing family and weights that disagree, instead of typing a value."""

    def build_with(self, mutate):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
            raw = copy / "raw" / "components-computed.json"
            data = json.loads(raw.read_text())
            mutate(data["components"])
            raw.write_text(json.dumps(data))
            return subprocess.run([sys.executable, str(copy / "tools" / "build_component_tokens.py")], capture_output=True, text=True)

    def test_missing_font_family_is_refused(self):
        def drop(c):
            del c["promo-strip"]["states"]["default"]["style"]["fontFamily"]
        run = self.build_with(drop)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("promo-strip", run.stderr)

    def test_disagreeing_weights_are_refused(self):
        def change(c):
            c["load-more"]["states"]["default"]["style"]["fontWeight"] = "700"
        run = self.build_with(change)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("fontWeight readings differ", run.stderr)


if __name__ == "__main__":
    unittest.main()
