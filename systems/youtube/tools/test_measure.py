"""Tests for the two additions to the kit's measure.py: per-theme boxes and the corner op.
Run: python3 -m unittest discover -s tools (from this package).

The images are small synthetic rows, so these tests need neither Pillow nor the full-colour
captures kept outside the repository."""
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import measure  # noqa: E402

PAGE, INK = (15, 15, 15, 255), (200, 40, 40, 255)


def rounded(w, h, x0, y0, side, r):
    """A page with a side x side square at x0, y0 whose corners are rounded to r pixels."""
    rows = [[PAGE] * w for _ in range(h)]
    for y in range(y0, y0 + side):
        for x in range(x0, x0 + side):
            cx = min(max(x, x0 + r), x0 + side - 1 - r)
            cy = min(max(y, y0 + r), y0 + side - 1 - r)
            if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                rows[y][x] = INK
    return rows


def flat(colour, w=20, h=20):
    return [[colour] * w for _ in range(h)]


class CornerTest(unittest.TestCase):
    def test_reads_the_radius_of_a_rounded_picture(self):
        for r in (8, 16, 24):        # 4, 8 and 12 pt at 2 px per pt
            res = measure.op_corner(rounded(80, 80, 10, 10, 60, r), 10, 10, (2, 2), 12)
            self.assertAlmostEqual(float(res["value"].rstrip("pt")), r / 2, delta=1)
            self.assertEqual(res["evidence"], "Derived")

    def test_a_square_corner_reads_zero(self):
        res = measure.op_corner(rounded(40, 40, 10, 10, 20, 0), 10, 10, (2, 2), 12)
        self.assertEqual(res["value"], "0.0pt")


class PerThemeBoxTest(unittest.TestCase):
    def run_with(self, table, images):
        """Run measure.run over a fake raw-shots folder whose PNGs are the given rows."""
        with tempfile.TemporaryDirectory() as raw:
            for key in images:
                p = pathlib.Path(raw, key + ".png")
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(b"")
            fake = lambda path: (0, 0, images[f"{path.parent.name}/{path.stem}"])
            with mock.patch.object(measure, "R", table), mock.patch.object(measure.sample, "read_png", fake):
                return measure.run(raw)

    def test_each_theme_reads_its_own_capture_and_box(self):
        dark = flat((10, 10, 10, 255))
        dark[15][15] = (250, 0, 0, 255)
        light = flat((240, 240, 240, 255))
        light[2][2] = (0, 0, 250, 255)
        table = {"x": {"dark": ("a", "fill", (15, 15, 1, 1)), "light": ("b", "fill", (2, 2, 1, 1)), "note": "n"}}
        out = self.run_with(table, {"dark/a": dark, "light/b": light})
        self.assertEqual(out["x"]["dark"]["value"], "#FA0000")
        self.assertEqual(out["x"]["light"]["value"], "#0000FA")
        self.assertEqual(out["x"]["light"]["capture"], "screenshots/light/b.png")

    def test_a_tuple_entry_still_reads_both_themes(self):
        table = {"y": ("a", "fill", (0, 0, 4, 4), "n"), "z": ("dark/a", "fill", (0, 0, 4, 4), "n")}
        out = self.run_with(table, {"dark/a": flat((1, 2, 3, 255)), "light/a": flat((9, 8, 7, 255))})
        self.assertEqual(out["y"]["dark"]["value"], "#010203")
        self.assertEqual(out["y"]["light"]["value"], "#090807")
        self.assertEqual(sorted(out["z"]), ["dark"])


if __name__ == "__main__":
    unittest.main()
