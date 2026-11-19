"""Tests for the capture kit's scripts (tools/kit/capture/) that need no product: colour
conversion and argument checks. Run with `make test`; skipped without node (and, for the
measure.mjs check, without the capture Playwright, $PLAYWRIGHT or ~/.design-systems/pw)."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAPTURE = HERE / "kit" / "capture"
NODE = shutil.which("node")
PLAYWRIGHT = os.environ.get("PLAYWRIGHT") or str(Path.home() / ".design-systems/pw/node_modules/playwright/index.mjs")


@unittest.skipIf(NODE is None, "node is not on PATH")
class CssColour(unittest.TestCase):
    def test_both_measurement_builders_read_lab_and_oklab(self):
        mod = (CAPTURE / "css-colour.mjs").as_uri()
        values = ["rgb(255, 0, 0)", "rgba(0, 0, 0, 0.5)", "color(srgb 1 1 1)", "oklab(62.8% 0.2249 0.1258)",
                  "oklab(0.5 0 0 / 0.3)", "lab(50 0 0)", "1px solid oklab(1 0 0)"]
        res = subprocess.run([NODE, "--input-type=module", "-e",
                              f"import {{ hex }} from {json.dumps(mod)}; console.log(JSON.stringify({json.dumps(values)}.map(hex)))"],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(json.loads(res.stdout), ["#ff0000", "#000000 @ 0.5", "#ffffff", "#ff0000", "#636363 @ 0.3",
                                                  "#777777", "1px solid #ffffff"])
        for rel in ("public/build-measurements.mjs", "signed-in/build-measurements.mjs"):
            self.assertIn("from '../css-colour.mjs'", (CAPTURE / rel).read_text(), rel)

    def test_lch_oklch_display_p3_and_out_of_range_srgb(self):
        # Chromium keeps oklch()/lch()/color(display-p3) as computed (Tailwind 4's palette is oklch), and
        # color(srgb) can hold a value over 1, below 0 or in e-notation; 1.02 used to become a 3-digit byte.
        mod = (CAPTURE / "css-colour.mjs").as_uri()
        values = ["oklch(62.8% 0.2577 29.23)", "oklch(0.5 0 0 / 50%)", "lch(50 0 0)", "lch(50 0 0deg)",
                  "color(display-p3 1 0 0)", "color(display-p3 0.5 0.5 0.5)", "color(srgb 1.02 0 0)",
                  "color(srgb 1e-3 0 0)", "color(srgb -0.1 0.5 0.5)", "color(srgb 0.2 0.4 0.6 / 0.25)",
                  "0 1px 2px oklch(0 0 0 / 0.1)"]
        res = subprocess.run([NODE, "--input-type=module", "-e",
                              f"import {{ hex }} from {json.dumps(mod)}; console.log(JSON.stringify({json.dumps(values)}.map(hex)))"],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(json.loads(res.stdout), ["#ff0000", "#636363 @ 0.5", "#777777", "#777777", "#ff0000", "#7f7f7f",
                                                  "#ff0000", "#000000", "#008080", "#336699 @ 0.25", "0 1px 2px #000000 @ 0.1"])


@unittest.skipIf(NODE is None or not Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class MeasureArgs(unittest.TestCase):
    def test_a_bad_jobs_count_stops_instead_of_running_no_workers(self):
        with tempfile.TemporaryDirectory() as d:
            for bad in ("x", "0", "-2", "1.5"):
                res = subprocess.run([NODE, str(CAPTURE / "signed-in/measure.mjs"), "--jobs", bad], capture_output=True,
                                     text=True, timeout=60, env={**os.environ, "SNAPS": d, "PLAYWRIGHT": PLAYWRIGHT})
                self.assertEqual(res.returncode, 2, (bad, res.stderr))
                self.assertIn("--jobs needs a whole number", res.stderr)


if __name__ == "__main__":
    unittest.main()
