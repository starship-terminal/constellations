"""Tests for the parts this package added to the native kit. Run: python3 -m unittest discover -s tools

measure.run reads a box per theme when an R entry gives one, op_diag takes a fixed tolerance, and
build_components_md.crop_cells marks a light-only crop as dark not captured. Fixtures are tiny PNGs
written with tools/capture/native/sample.py, so the tests need no captures and no Pillow."""
import pathlib
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "capture" / "native"))
import build_components_md  # noqa: E402
import measure  # noqa: E402
import sample  # noqa: E402

BLACK, WHITE, GREY, PAGE = (0, 0, 0, 255), (255, 255, 255, 255), (198, 198, 198, 255), (252, 252, 252, 255)


def flat(colour, w=4, h=4):
    return [[colour] * w for _ in range(h)]


class PerThemeReadingTest(unittest.TestCase):
    def test_each_theme_reads_its_own_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = pathlib.Path(tmp)
            for theme, name, colour in (("dark", "a", BLACK), ("light", "b", WHITE)):
                (raw / theme).mkdir()
                sample.write_png(raw / theme / f"{name}.png", flat(colour))
            saved = measure.R
            measure.R = {"x": {"dark": ("a", "fill", (0, 0, 2, 2)), "light": ("b", "fill", (0, 0, 2, 2)), "note": "n"}}
            try:
                out = measure.run(raw)
            finally:
                measure.R = saved
        self.assertEqual(out["x"]["dark"]["value"], "#000000")
        self.assertEqual(out["x"]["dark"]["capture"], "screenshots/dark/a.png")
        self.assertEqual(out["x"]["light"]["value"], "#FFFFFF")
        self.assertEqual(out["x"]["light"]["capture"], "screenshots/light/b.png")


class DiagToleranceTest(unittest.TestCase):
    def rows(self):
        """A light fill whose top meets a grey strip (rows 2-11) under black, and whose left meets black (x < 5)."""
        return [[BLACK if x < 5 or y < 2 else GREY if y < 12 else PAGE for x in range(40)] for y in range(40)]

    def test_fixed_tolerance_stops_at_the_strip(self):
        self.assertEqual(measure.op_diag(self.rows(), 30, 30, 20, 30, 20)["corner"], [5, 12])

    def test_default_tolerance_runs_through_the_strip(self):
        self.assertEqual(measure.op_diag(self.rows(), 30, 30, 20, 30)["corner"], [5, 2])


class CropCellsTest(unittest.TestCase):
    def test_light_only_crop_says_dark_not_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            crops = pathlib.Path(tmp)
            for f in ("both.png", "both-light.png", "only-light.png"):
                (crops / f).write_bytes(b"")
            cells = build_components_md.crop_cells("X", [("a", "both"), ("b", "only")], crops)
        self.assertEqual(cells, ["[a (dark)](components/crops/both.png)", "[a (light)](components/crops/both-light.png)",
                                 "[b (light; dark not captured)](components/crops/only-light.png)"])

    def test_missing_crop_stops_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                build_components_md.crop_cells("X", [("a", "none")], pathlib.Path(tmp))


if __name__ == "__main__":
    unittest.main()
