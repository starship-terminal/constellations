"""Tests for measure.op_rimdiag on synthetic outlined shapes. Run: python3 -m unittest discover -s tools.

Each fixture is a rounded rectangle drawn as a two-pixel rim on a flat fill, the way Notion's outlined
Settings controls look; the reading must recover its corner radius within the 2 pt the label allows."""
import math
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import measure  # noqa: E402


def inside(x, y, box, radius):
    """Whether pixel (x, y)'s centre lies in the rounded rectangle box = (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = box
    px, py = x + 0.5, y + 0.5
    if not (x0 <= px <= x1 and y0 <= py <= y1):
        return False
    cx = min(max(px, x0 + radius), x1 - radius)
    cy = min(max(py, y0 + radius), y1 - radius)
    return math.hypot(px - cx, py - cy) <= radius


def outlined(radius, fill, rim, size=200, box=(40, 40, 160, 140)):
    """rows[y][x] of a rounded rectangle drawn as a two-pixel rim (1 pt at 2x) on a flat fill; radius in px."""
    x0, y0, x1, y1 = box
    inner = (x0 + 2, y0 + 2, x1 - 2, y1 - 2)
    return [[(rim if inside(x, y, box, radius) and not inside(x, y, inner, max(radius - 2, 0)) else fill) + (255,)
             for x in range(size)] for y in range(size)]


def pt(reading):
    return float(reading["value"].rstrip("pt"))


class RimDiagTest(unittest.TestCase):
    def test_dark_rim(self):
        rows = outlined(16, (32, 32, 32), (53, 53, 53))
        self.assertAlmostEqual(pt(measure.op_rimdiag(rows, 50, 90, 100, 60, 6)), 8, delta=2)

    def test_light_rim(self):
        rows = outlined(24, (250, 248, 248), (226, 224, 225))
        self.assertAlmostEqual(pt(measure.op_rimdiag(rows, 50, 90, 100, 70, 6)), 12, delta=2)

    def test_square_corner_reads_near_zero(self):
        rows = outlined(1, (32, 32, 32), (53, 53, 53))
        self.assertLessEqual(pt(measure.op_rimdiag(rows, 50, 90, 100, 60, 6)), 2)

    def test_missing_rim_raises(self):
        rows = [[(32, 32, 32, 255)] * 200 for _ in range(200)]
        with self.assertRaisesRegex(ValueError, "no rim"):
            measure.op_rimdiag(rows, 50, 90, 100, 60, 6)


if __name__ == "__main__":
    unittest.main()
