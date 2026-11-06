"""capture/quantize.py publishes only shots with a current reading and writes nothing when a linked run frame
is missing. Needs Pillow."""
import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent


def load(raw):
    argv, sys.argv = sys.argv, ["quantize.py", str(raw)]
    try:
        spec = importlib.util.spec_from_file_location("quantize_under_test", HERE / "capture" / "quantize.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


def png(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (4, 4), (20, 20, 20)).save(path)


class QuantizeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(self.tmp.name)
        self.raw, self.pkg = root / "raw-shots", root / "pkg"
        (self.pkg / "raw").mkdir(parents=True)
        self.q = load(self.raw)
        self.q.PKG = self.pkg

    def tearDown(self):
        self.tmp.cleanup()

    def test_shot_without_reading_is_not_published(self):
        self.q.RUN_FRAMES = {}
        dark = self.raw / "dark"
        png(dark / "home.png")
        png(dark / "failed.png")
        (dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
        self.q.main()
        self.assertEqual(sorted(p.name for p in (self.pkg / "screenshots" / "dark").glob("*.png")), ["home.png"])

    def test_missing_run_frame_writes_nothing(self):
        self.q.RUN_FRAMES = {"dark": {"step-00": "run-started"}}
        dark = self.raw / "dark"
        png(dark / "home.png")
        (dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
        committed = self.pkg / "screenshots" / "dark" / "run-started.png"
        png(committed)
        with self.assertRaises(SystemExit):
            self.q.main()
        self.assertTrue(committed.exists())
        self.assertFalse((self.pkg / "screenshots" / "dark" / "home.png").exists())


if __name__ == "__main__":
    unittest.main()
