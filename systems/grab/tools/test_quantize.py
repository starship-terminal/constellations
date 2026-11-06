"""capture/quantize.py refuses to write anything when masks.json names a capture that does not exist (a
mistyped key would otherwise publish the real capture unmasked), and rejects a box outside the image.
Needs Pillow."""
import importlib.util
import pathlib
import sys
import tempfile
import unittest
import unittest.mock

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("grab_quantize_under_test", HERE / "capture" / "quantize.py")
quantize = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quantize)


class QuantizeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(self.tmp.name)
        self.raw, self.pkg = root / "raw-shots", root / "pkg"
        (self.raw / "light").mkdir(parents=True)
        Image.new("RGB", (8, 8), (250, 250, 250)).save(self.raw / "light" / "01-home.png")
        self.masks = quantize.MASKS

    def tearDown(self):
        quantize.MASKS = self.masks
        self.tmp.cleanup()

    def stored(self):
        return sorted(p.name for p in (self.pkg / "screenshots" / "light").glob("*.png"))

    def test_mistyped_mask_key_writes_nothing(self):
        quantize.MASKS = {"01-hmoe": [[1, 1, 2, 2]]}
        with self.assertRaises(SystemExit):
            quantize.main(self.raw, self.pkg)
        self.assertFalse((self.pkg / "screenshots").exists())

    def test_masked_capture_is_painted(self):
        im = Image.new("RGB", (8, 8), (250, 250, 250))
        im.paste((10, 10, 10), (2, 2, 5, 5))
        im.save(self.raw / "light" / "01-home.png")
        quantize.MASKS = {"01-home": [[2, 2, 3, 3]]}
        with unittest.mock.patch("builtins.print"):
            quantize.main(self.raw, self.pkg)
        self.assertEqual(self.stored(), ["01-home.png"])
        out = Image.open(self.pkg / "screenshots" / "light" / "01-home.png").convert("RGB")
        self.assertEqual(out.getpixel((3, 3)), (250, 250, 250))

    def test_box_outside_capture_is_rejected(self):
        with self.assertRaises(ValueError):
            quantize.ring_colour(Image.new("RGB", (8, 8)), 20, 20, 4, 4)


if __name__ == "__main__":
    unittest.main()
