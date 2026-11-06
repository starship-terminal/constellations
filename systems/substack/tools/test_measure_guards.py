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

    def test_empty_boxes_are_named(self):
        rows = card()
        with self.assertRaisesRegex(ValueError, "cap: no ink"):
            measure.op_cap(rows, 0, 0, 5, 5)
        with self.assertRaisesRegex(ValueError, "lines: no ink"):
            measure.op_lines(rows, 0, 0, 5, 5)
        with self.assertRaisesRegex(ValueError, "bbox: no pixel"):
            measure.op_bbox(rows, (30, 30), (0, 0, 5, 5), 3)


if __name__ == "__main__":
    unittest.main()
