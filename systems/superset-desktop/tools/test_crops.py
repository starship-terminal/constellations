"""crops.py stops, and deletes nothing, when a screenshot it needs is missing. Needs Pillow."""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crops  # noqa: E402


class MissingScreenshotTest(unittest.TestCase):
    def test_missing_screenshot_keeps_committed_crops(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp)
            (pkg / "raw").mkdir()
            (pkg / "raw" / "components.dark.json").write_text(json.dumps(
                {"home": {"state": "default", "parts": {"button": {"box": [10, 10, 40, 20]}}}}))
            out = pkg / "components" / "crops"
            out.mkdir(parents=True)
            (out / "button-default.png").write_bytes(b"committed")
            saved = crops.PKG, crops.OUT
            crops.PKG, crops.OUT = pkg, out
            try:
                with self.assertRaises(SystemExit):
                    crops.main()
            finally:
                crops.PKG, crops.OUT = saved
            self.assertTrue((out / "button-default.png").exists())


if __name__ == "__main__":
    unittest.main()
