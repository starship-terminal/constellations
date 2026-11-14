"""Smoke tests for tools/make_icons.py: it derives the Glass icon set from a
master render. The tests run it on a small synthetic master and write only to a
temporary folder, never to docs/assets/. Run with `make test`; skipped when
Pillow is missing."""
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
try:
    from PIL import Image
except ImportError:  # Pillow is optional for `make test`
    make_icons = None
else:
    import make_icons  # a broken import in the script itself must fail, not skip

EXPECTED = {"favicon-16.png": (16, 16), "favicon-32.png": (32, 32), "favicon-48.png": (48, 48),
            "apple-touch-icon.png": (180, 180), "icon-192.png": (192, 192),
            "icon-512.png": (512, 512), "icon-maskable-512.png": (512, 512)}
TILE = (8, 9, 10)


def synthetic_master(path):
    """A 1024 px render: pure black, with a white block inside the crop."""
    img = Image.new("RGB", (1024, 1024), (0, 0, 0))
    img.paste((255, 255, 255), (400, 400, 624, 624))
    img.save(path)


@unittest.skipIf(make_icons is None, "Pillow is not installed")
class MakeIconsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.master = root / "hero-ai.png"
        synthetic_master(cls.master)
        cls.out = root / "glass"
        cls.run_it()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    @classmethod
    def run_it(cls):
        root = Path(cls.tmp.name)
        with mock.patch.object(make_icons, "MASTER", cls.master), \
             mock.patch.object(make_icons, "OUT", cls.out), \
             mock.patch.object(make_icons, "ROOT", root), \
             mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            make_icons.main()
        return out.getvalue()

    def test_the_full_set_is_written_with_the_flat_sets_names_and_sizes(self):
        self.assertEqual(sorted(p.name for p in self.out.iterdir()),
                         sorted(list(EXPECTED) + ["favicon.ico"]))
        for name, size in EXPECTED.items():
            with Image.open(self.out / name) as img:
                self.assertEqual(img.size, size, name)

    def test_the_ico_bundles_the_three_favicon_sizes(self):
        with Image.open(self.out / "favicon.ico") as ico:
            self.assertEqual(sorted(ico.info["sizes"]), [(16, 16), (32, 32), (48, 48)])

    def test_the_summary_line_counts_the_icons(self):
        self.assertIn("wrote 8 icons to glass", self.run_it())

    def test_black_in_the_render_becomes_the_tile_colour(self):
        with mock.patch.object(make_icons, "MASTER", self.master):
            tile = make_icons.tile(64)
        self.assertEqual(tile.getpixel((2, 2)), TILE)
        self.assertEqual(tile.getpixel((32, 32)), (255, 255, 255))

    def test_rounded_tiles_clear_their_corners_and_keep_the_centre(self):
        with Image.open(self.out / "icon-512.png") as img:
            rgba = img.convert("RGBA")
        self.assertEqual(rgba.getpixel((0, 0))[3], 0)
        self.assertEqual(rgba.getpixel((511, 511))[3], 0)
        self.assertEqual(rgba.getpixel((256, 256))[3], 255)

    def test_the_apple_touch_icon_is_square_cornered_for_ios_to_round(self):
        with Image.open(self.out / "apple-touch-icon.png") as img:
            self.assertEqual(img.convert("RGBA").getpixel((0, 0))[3], 255)

    def test_the_maskable_icon_pads_the_tile_to_the_safe_zone(self):
        with Image.open(self.out / "icon-maskable-512.png") as img:
            rgb = img.convert("RGB")
        self.assertEqual(rgb.getpixel((0, 0)), TILE)
        self.assertEqual(rgb.getpixel((511, 511)), TILE)
        self.assertEqual(rgb.getpixel((256, 256)), (255, 255, 255))
        pad = (512 - round(512 * make_icons.SAFE)) // 2
        self.assertEqual(rgb.getpixel((pad - 1, 256)), TILE)

    def test_a_rerun_over_an_unchanged_master_rewrites_identical_bytes(self):
        before = {p.name: p.read_bytes() for p in self.out.iterdir()}
        self.run_it()
        self.assertEqual({p.name: p.read_bytes() for p in self.out.iterdir()}, before)

    def test_the_real_master_is_where_the_script_expects_it(self):
        self.assertEqual(make_icons.MASTER.name, "hero-ai.png")
        self.assertEqual(make_icons.OUT.parts[-3:], ("assets", "icons", "glass"))


if __name__ == "__main__":
    unittest.main()
