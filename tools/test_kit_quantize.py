"""tools/kit/capture/quantize.py stitches name.partN.png tiles and skips a name that only looks like one
(x.partial.png) instead of crashing. Needs Pillow; skipped without it."""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

KIT = pathlib.Path(__file__).resolve().parent / "kit" / "capture" / "quantize.py"


@unittest.skipIf(Image is None, "Pillow is not installed")
class KitQuantizeTest(unittest.TestCase):
    def test_a_partial_name_is_not_a_tile(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            # The script writes screenshots/ three levels above itself, so run a copy in a scratch package.
            script = tmp / "pkg" / "tools" / "capture" / "quantize.py"
            script.parent.mkdir(parents=True)
            shutil.copy(KIT, script)
            raw = tmp / "raw"
            raw.mkdir()
            Image.new("RGB", (4, 3), (10, 20, 30)).save(raw / "page.part0.png")
            Image.new("RGB", (4, 5), (40, 50, 60)).save(raw / "page.part1.png")
            Image.new("RGB", (4, 4), (70, 80, 90)).save(raw / "x.partial.png")
            done = subprocess.run([sys.executable, str(script), str(raw)], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr[-500:])
            with Image.open(raw / "page.png") as im:
                self.assertEqual(im.size, (4, 8))
            self.assertEqual(sorted(p.name for p in (tmp / "pkg" / "screenshots").iterdir()), ["page.png"])


if __name__ == "__main__":
    unittest.main()
