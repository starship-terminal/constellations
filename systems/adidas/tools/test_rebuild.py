"""The committed outputs must rebuild from the package's inputs.

The builders run on a temporary copy of the package, so nothing committed is rewritten.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ['build_components_md.py']
OUTPUTS = ['components.md']


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        # Remove the committed outputs from the copy first, so a builder that
        # writes nothing cannot pass by leaving the committed file in place.
        for out in OUTPUTS:
            (cls.copy / out).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True, cwd=cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_failed_focus_is_not_published_as_a_reading(self):
        import json
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        failed = [k for k, c in raw.items() if (c.get("states", {}).get("focus-visible") or {}).get("via") == "focus failed"]
        text = (self.copy / "components.md").read_text()
        for k in failed:
            with self.subTest(component=k):
                self.assertNotIn(f"crops/{k}-focus-visible.png", text)


class OtherMarkersTest(unittest.TestCase):
    """A focus-visible state marked skipped, or with focus.matches false, is left out the same way.
    Each case marks one captured focus-visible state on a temporary copy and rebuilds."""

    def rebuild_with(self, mark):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            raw_path = copy / "raw" / "components-computed.json"
            data = json.loads(raw_path.read_text())
            key = next(k for k, c in data["components"].items()
                       if "style" in (c.get("states", {}).get("focus-visible") or {})
                       and (c["states"]["focus-visible"].get("via") != "focus failed")
                       and c["states"]["focus-visible"].get("crop"))
            mark(data["components"][key]["states"]["focus-visible"])
            raw_path.write_text(json.dumps(data))
            subprocess.run([sys.executable, str(copy / "tools" / "build_components_md.py")], check=True, capture_output=True, cwd=copy)
            return key, (copy / "components.md").read_text()

    def test_skipped_state_is_left_out(self):
        key, text = self.rebuild_with(lambda s: s.__setitem__("skipped", "focus could not be captured"))
        self.assertNotIn(f"crops/{key}-focus-visible.png", text)

    def test_focus_not_matching_is_left_out(self):
        key, text = self.rebuild_with(lambda s: s.__setitem__("focus", {"matches": False}))
        self.assertNotIn(f"crops/{key}-focus-visible.png", text)


if __name__ == "__main__":
    unittest.main()
