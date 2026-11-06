"""Tests for measure.py's op guards: a scan that finds nothing or walks off the image raises a named
ValueError instead of an IndexError or a value read from the far edge. Run: python3 -m unittest discover -s tools."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import measure  # noqa: E402

PAGE, CARD = (0, 0, 0, 255), (200, 200, 200, 255)


def card(size=60, box=(10, 10, 50, 50)):
    """rows[y][x]: a square card (no rounding) on a flat page."""
    x0, y0, x1, y1 = box
    return [[CARD if x0 <= x < x1 and y0 <= y < y1 else PAGE for x in range(size)] for y in range(size)]


class GuardTest(unittest.TestCase):
    def test_extent_with_no_hit_is_named(self):
        with self.assertRaisesRegex(ValueError, "extent: nothing"):
            measure.op_extent(card(), "row", 5, 0, 60, (0, 0), 10)

    def test_extent_reads_a_card_inside_the_scan(self):
        self.assertEqual(measure.op_extent(card(), "row", 30, 0, 60, (0, 0), 10)["from"], 10)

    def test_extent_running_to_the_scan_end_is_refused(self):
        with self.assertRaisesRegex(ValueError, "scan limit"):
            measure.op_extent(card(), "row", 30, 20, 40, (0, 0), 10)

    def test_diag_reads_a_square_corner(self):
        self.assertEqual(measure.op_diag(card(), 30, 30, 30, 30)["inset"], 0)

    def test_diag_on_a_fill_that_reaches_the_image_edge_is_named(self):
        with self.assertRaisesRegex(ValueError, "diag:"):
            measure.op_diag(card(box=(0, 10, 50, 50)), 30, 30, 30, 30)
        with self.assertRaisesRegex(ValueError, "diag:"):
            measure.op_diag(card(box=(10, 0, 50, 50)), 30, 30, 30, 30)

    def test_diag_with_its_background_sample_off_the_image_is_named(self):
        with self.assertRaisesRegex(ValueError, "diag: no edge with background"):
            measure.op_diag(card(box=(3, 10, 50, 50)), 30, 30, 30, 30)

    def test_diag_whose_diagonal_never_meets_the_fill_is_named(self):
        rows = [[PAGE] * 60 for _ in range(60)]
        for y in range(40, 46):              # a bar the row walk finds ...
            for x in range(10, 31):
                rows[y][x] = CARD
        for y in range(5, 21):               # ... and a separate one the column walk finds
            for x in range(50, 56):
                rows[y][x] = CARD
        with self.assertRaisesRegex(ValueError, "diag: no fill on the diagonal"):
            measure.op_diag(rows, 52, 15, 20, 42)

    def test_empty_boxes_are_named(self):
        rows = card()
        with self.assertRaisesRegex(ValueError, "cap: no ink"):
            measure.op_cap(rows, 0, 0, 5, 5)
        with self.assertRaisesRegex(ValueError, "lines: no ink"):
            measure.op_lines(rows, 0, 0, 5, 5)
        with self.assertRaisesRegex(ValueError, "bbox: no pixel"):
            measure.op_bbox(rows, (30, 30), (0, 0, 5, 5), 3)


class ThemeTest(unittest.TestCase):
    """lacking() is what stops measure.py writing when a reading misses a theme it needs."""

    @unittest.skipUnless((pathlib.Path(__file__).resolve().parent.parent / "raw" / "readings.json").exists(), "no readings")
    def test_committed_readings_lack_nothing_and_a_dropped_theme_is_caught(self):
        import copy
        import json
        readings = json.loads((pathlib.Path(__file__).resolve().parent.parent / "raw" / "readings.json").read_text())
        self.assertEqual(measure.lacking(readings), [])   # covers the single-theme entries as committed
        rid = sorted(readings)[0]
        cut = copy.deepcopy(readings)
        cut[rid].pop(sorted(cut[rid])[0])
        self.assertEqual(measure.lacking(cut), [rid])


if __name__ == "__main__":
    unittest.main()
