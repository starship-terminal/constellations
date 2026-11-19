"""Tests for the generic ops in measure.py. Run: python3 -m unittest discover -s tools (from this package)."""
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# In a package, measure.py finds sample.py under tools/capture/native; in the kit it sits beside native/.
sys.path.insert(0, str(HERE.parent / "capture" / "native"))
import measure  # noqa: E402

BG, FILL = (0, 0, 0, 255), (200, 200, 200, 255)


class DiagTest(unittest.TestCase):
    def test_a_box_against_the_left_edge_raises_instead_of_wrapping(self):
        # A fill that runs to x = 0: the walk left must stop at the edge, not read
        # rows[y][-1] from the far side of the capture.
        rows = [[FILL] * 8 + [BG] * 4 for _ in range(10)]
        with self.assertRaisesRegex(ValueError, "walked off the capture"):
            measure.op_diag(rows, 2, 5, 4, 5)

    def test_at_rejects_negative_and_overflowing_coordinates(self):
        rows = [[BG] * 3 for _ in range(2)]
        self.assertEqual(measure.at(rows, 2, 1), BG)
        for x, y in ((-1, 0), (0, -1), (3, 0), (0, 2)):
            with self.assertRaises(ValueError):
                measure.at(rows, x, y)


if __name__ == "__main__":
    unittest.main()
