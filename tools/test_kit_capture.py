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


class Templates(unittest.TestCase):
    def test_icon_names_header_is_the_columns_icons_mjs_reads(self):
        # icons.mjs reads hash<TAB>name and skips the header row; a name<TAB>role header filled in as
        # documented never matched a hash.
        rows = [r.split("\t") for r in (CAPTURE / "icon-names.tsv").read_text().splitlines() if r and not r.startswith("#")]
        self.assertEqual(rows[0], ["hash", "name"])

    @unittest.skipIf(NODE is None, "node is not on PATH")
    def test_render_refuses_a_scroll_flag_it_cannot_read(self):
        with tempfile.TemporaryDirectory() as d:
            for flag in ("scroll=main:120", "scroll=", "scroll=top"):
                res = subprocess.run([NODE, str(CAPTURE / "signed-in/render.mjs"), d, "home-dark", flag], capture_output=True,
                                     text=True, timeout=60, env={**os.environ, "KIT_EXAMPLE": "1"})
                self.assertEqual(res.returncode, 2, (flag, res.stderr))
                self.assertIn("scroll= takes a pixel offset, max or auto", res.stderr)
        head = (CAPTURE / "signed-in/shots.tsv").read_text().splitlines()[0]
        self.assertNotIn("<selector>", head)


@unittest.skipIf(NODE is None, "node is not on PATH")
class CheckoutPaths(unittest.TestCase):
    def test_measurement_builders_find_the_package_under_a_path_with_a_space(self):
        # new URL(import.meta.url).pathname is not decoded, so "a b" became "a%20b" and raw/ was not found.
        computed = {"_meta": {"read": "2026-01-02", "snapshots": {}}, "components": {}}
        for route in ("public", "signed-in"):
            with tempfile.TemporaryDirectory() as d:
                pkg = Path(d) / "a checkout é" / "pkg"
                (pkg / "tools/capture" / route).mkdir(parents=True)
                (pkg / "raw").mkdir()
                shutil.copy(CAPTURE / "css-colour.mjs", pkg / "tools/capture/css-colour.mjs")
                shutil.copy(CAPTURE / route / "build-measurements.mjs", pkg / "tools/capture" / route / "build-measurements.mjs")
                (pkg / "raw/components-computed.json").write_text(json.dumps(computed))
                res = subprocess.run([NODE, str(pkg / "tools/capture" / route / "build-measurements.mjs")], capture_output=True,
                                     text=True, timeout=60, env={**os.environ, "KIT_EXAMPLE": "1"})
                self.assertEqual(res.returncode, 0, (route, res.stderr[-1000:]))
                self.assertTrue((pkg / "raw/measurements.md").is_file(), route)

    def test_no_kit_script_reads_a_path_from_an_undecoded_url(self):
        bad = [f"{p.relative_to(CAPTURE)}:{n}" for p in sorted(CAPTURE.rglob("*.mjs")) if not p.name.startswith("test_")
               for n, line in enumerate(p.read_text().splitlines(), 1) if "import.meta.url" in line and ".pathname" in line]
        self.assertEqual(bad, [])


class ReadDates(unittest.TestCase):
    def test_no_kit_script_records_a_fixed_read_date(self):
        # signed-in/measure.mjs wrote read: '2026-10-04' (the example's capture day) on every run, and the
        # builders print it as the day the styles were read.
        import re
        bad = [f"{p.relative_to(CAPTURE)}:{n}" for p in sorted(CAPTURE.rglob("*.mjs")) if not p.name.startswith("test_")
               for n, line in enumerate(p.read_text().splitlines(), 1) if re.search(r"\bread: ['\"`]\d{4}-\d\d-\d\d", line)]
        self.assertEqual(bad, [])


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
