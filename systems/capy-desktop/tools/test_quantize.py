"""capture/quantize.py writes nothing when a theme's readings are missing, and publishes only shots with a
current reading. Needs Pillow."""
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
        self.dark = self.raw / "dark"

    def tearDown(self):
        self.tmp.cleanup()

    def shots(self):
        return sorted(p.name for p in (self.pkg / "screenshots" / "dark").glob("*.png"))

    def test_shot_without_reading_is_not_published(self):
        png(self.dark / "home.png")
        png(self.dark / "failed.png")
        (self.dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
        self.q.main()
        self.assertEqual(self.shots(), ["home.png"])

    def test_missing_captures_json_writes_nothing(self):
        png(self.dark / "home.png")
        committed = self.pkg / "screenshots" / "dark" / "home.png"
        png(committed)
        with self.assertRaises(SystemExit):
            self.q.main()
        self.assertTrue(committed.exists())

    def test_missing_frames_json_keeps_the_run_screenshots(self):
        png(self.dark / "home.png")
        (self.dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
        (self.pkg / "raw" / "run.dark.json").write_text(json.dumps({"run-done": {"frame": "list-files-done"}}))
        committed = self.pkg / "screenshots" / "dark" / "run-done.png"
        png(committed)
        with self.assertRaises(SystemExit):
            self.q.main()
        self.assertTrue(committed.exists())
        self.assertFalse((self.pkg / "screenshots" / "dark" / "home.png").exists())

    def test_a_later_incomplete_theme_leaves_an_earlier_one_alone(self):
        # dark sorts before light: a check made inside the theme loop would rewrite dark before it saw light.
        for missing in ("captures", "frames"):
            with self.subTest(missing=missing):
                png(self.dark / "home.png")
                (self.dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
                light = self.raw / "light"
                png(light / "home.png")
                if missing == "frames":
                    (light / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
                    (self.pkg / "raw" / "run.light.json").write_text("{}")
                committed = self.pkg / "screenshots" / "dark" / "old.png"
                png(committed)
                with self.assertRaises(SystemExit):
                    self.q.main()
                self.assertTrue(committed.exists())
                self.assertFalse((self.pkg / "screenshots" / "dark" / "home.png").exists())
                self.assertFalse((self.pkg / "raw" / "components.dark.json").exists())

    def test_theme_without_run_readings_needs_no_frames(self):
        png(self.dark / "home.png")
        (self.dark / "captures.json").write_text(json.dumps({"home": {"state": "default", "parts": {}}}))
        self.q.main()
        self.assertEqual(self.shots(), ["home.png"])
        self.assertFalse((self.pkg / "raw" / "run.dark.json").exists())


if __name__ == "__main__":
    unittest.main()
