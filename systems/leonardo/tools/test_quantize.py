"""quantize.py stitches a tile set only when its completion record matches the tiles on disk."""
import importlib.util
import json
import pathlib
import tempfile
import unittest
from unittest import mock

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent


class QuantizeCoverageTest(unittest.TestCase):
    def stitch(self, raw):
        # The script reads argv and stitches on import. Each call gets a fresh
        # module, and argv is patched only for the import, then restored.
        out = raw.parent / "screenshots"
        name = "leonardo_quantize_" + str(id(raw))
        spec = importlib.util.spec_from_file_location(name, HERE / "capture" / "quantize.py")
        mod = importlib.util.module_from_spec(spec)
        with mock.patch("sys.argv", ["quantize.py", str(raw), str(out)]):
            spec.loader.exec_module(mod)
        return mod

    def test_partial_tiles_are_not_stitched(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            raw.mkdir()
            Image.new("RGB", (4, 3), (1, 2, 3)).save(raw / "page.part0.png")
            Image.new("RGB", (4, 2), (4, 5, 6)).save(raw / "page.part1.png")
            # A previous full page that a partial set must not replace.
            Image.new("RGB", (4, 9), (9, 9, 9)).save(raw / "page.png")
            self.stitch(raw)
            with Image.open(raw / "page.png") as im:
                self.assertEqual(im.size, (4, 9))

    def test_matching_record_stitches(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp) / "raw"
            raw.mkdir()
            Image.new("RGB", (4, 3), (1, 2, 3)).save(raw / "page.part0.png")
            Image.new("RGB", (4, 2), (4, 5, 6)).save(raw / "page.part1.png")
            (raw / "page.parts.json").write_text(json.dumps({"tiles": ["page.part0.png", "page.part1.png"]}))
            self.stitch(raw)
            with Image.open(raw / "page.png") as im:
                self.assertEqual(im.size, (4, 5))


if __name__ == "__main__":
    unittest.main()
