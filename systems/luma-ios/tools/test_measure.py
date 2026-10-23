"""Tests for this package's additions to the native kit's measure.py: the `mean` op and reading-table
entries that take a different box per theme. Synthetic pixels only; no capture is read.

    python3 -m unittest discover -s tools
"""
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import measure  # noqa: E402


def rows_of(w, h, colour):
    return [[colour + (255,) for _ in range(w)] for _ in range(h)]


class MeanTest(unittest.TestCase):
    def test_average_and_spread(self):
        rows = rows_of(4, 2, (10, 20, 30))
        rows[0][0] = (14, 20, 26, 255)      # +4 red, -4 blue: the mean is unchanged, the spread is 8
        rows[1][3] = (6, 20, 34, 255)
        r = measure.op_mean(rows, 0, 0, 4, 2)
        self.assertEqual(r["value"], "#0A141E")
        self.assertEqual(r["spread"], 8)
        self.assertEqual(r["evidence"], "Derived")

    def test_only_the_box_counts(self):
        rows = rows_of(6, 6, (0, 0, 0))
        for y in range(2, 4):
            for x in range(2, 4):
                rows[y][x] = (200, 100, 50, 255)
        r = measure.op_mean(rows, 2, 2, 2, 2)
        self.assertEqual((r["value"], r["spread"]), ("#C86432", 0))


class PerThemeEntryTest(unittest.TestCase):
    def test_each_theme_reads_its_own_box(self):
        dark = rows_of(10, 10, (0, 0, 0))
        dark[1][1] = (255, 255, 255, 255)
        light = rows_of(10, 10, (255, 255, 255))
        light[8][8] = (17, 17, 17, 255)
        table = {
            "border.selected": {"dark": ("cap", "fill", (1, 1, 1, 1)), "light": ("cap", "fill", (8, 8, 1, 1)), "note": "n"},
            "bg.page": ("cap", "fill", (5, 5, 1, 1), "plain entry, both themes"),
        }
        with tempfile.TemporaryDirectory() as raw:
            for theme in ("dark", "light"):
                (pathlib.Path(raw) / theme).mkdir()
                (pathlib.Path(raw) / theme / "cap.png").write_bytes(b"")
            read = lambda png: (10, 10, dark if png.parent.name == "dark" else light)
            with mock.patch.object(measure, "R", table), mock.patch.object(measure.sample, "read_png", read):
                out = measure.run(raw)
        self.assertEqual(out["border.selected"]["dark"]["value"], "#FFFFFF")
        self.assertEqual(out["border.selected"]["light"]["value"], "#111111")
        self.assertEqual(out["border.selected"]["light"]["args"], [8, 8, 1, 1])
        self.assertEqual(out["border.selected"]["dark"]["note"], "n")
        self.assertEqual((out["bg.page"]["dark"]["value"], out["bg.page"]["light"]["value"]), ("#000000", "#FFFFFF"))

    def test_a_theme_left_out_is_not_read(self):
        table = {"x": {"dark": ("cap", "fill", (0, 0, 1, 1)), "note": "dark only"}}
        with tempfile.TemporaryDirectory() as raw:
            for theme in ("dark", "light"):
                (pathlib.Path(raw) / theme).mkdir()
                (pathlib.Path(raw) / theme / "cap.png").write_bytes(b"")
            read = lambda png: (1, 1, rows_of(1, 1, (1, 2, 3)))
            with mock.patch.object(measure, "R", table), mock.patch.object(measure.sample, "read_png", read):
                out = measure.run(raw)
        self.assertEqual(list(out["x"]), ["dark"])


if __name__ == "__main__":
    unittest.main()
