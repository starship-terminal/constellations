"""Tests for the capture kit's scripts (tools/kit/capture/) that need no product: colour
conversion and argument checks. Run with `make test`; skipped without node (and, for the
measure.mjs check, without the capture Playwright, $PLAYWRIGHT or ~/.design-systems/pw)."""
import json
import re
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

    def test_one_colour_in_every_notation_and_a_missing_component(self):
        # CSS Color 4's worked example, rgb(125 35 41), written in each notation (lch and oklch with plain
        # and percentage chroma, display-p3 from the inverse matrices); `none` converts as zero.
        mod = (CAPTURE / "css-colour.mjs").as_uri()
        same = ["lab(29.2345% 39.3825 20.0664)", "lch(29.2345% 44.2 27)", "lch(29.2345% 29.4667% 27)",
                "oklab(40.101% 0.1147 0.0453)", "oklch(40.101% 0.12332 21.555)", "oklch(40.101% 30.83% 21.555)",
                "color(display-p3 0.45124 0.16432 0.1715)"]
        other = ["oklch(0 0 none / 0.85)", "lch(none none none)", "color(srgb none 0.5 1)"]
        res = subprocess.run([NODE, "--input-type=module", "-e",
                              f"import {{ hex }} from {json.dumps(mod)}; console.log(JSON.stringify({json.dumps(same + other)}.map(hex)))"],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(json.loads(res.stdout), ["#7d2329"] * len(same) + ["#000000 @ 0.85", "#000000", "#0080ff"])


# Node test files with a runner of their own elsewhere under tools/ (test_capture_screenshot.py, test_kit_motion.py).
NODE_RUN_ELSEWHERE = {"test_screenshot.mjs", "test_motion.mjs"}


@unittest.skipIf(NODE is None, "node is not on PATH")
class KitNodeTests(unittest.TestCase):
    def test_every_other_kit_node_test_file_passes(self):
        # Any tools/kit/**/test_*.mjs, so a new one runs under `make test` without its own runner.
        files = sorted(p for p in (HERE / "kit").rglob("test_*.mjs") if p.name not in NODE_RUN_ELSEWHERE)
        self.assertIn(CAPTURE / "test_readings.mjs", files)
        for f in files:
            res = subprocess.run([NODE, "--test", str(f)], capture_output=True, text=True, timeout=120)
            self.assertEqual(res.returncode, 0, f"{f.relative_to(HERE.parent)}\n{res.stdout[-3000:]}{res.stderr[-1000:]}")
        for name in NODE_RUN_ELSEWHERE:
            self.assertTrue((CAPTURE / name).is_file(), name)


@unittest.skipIf(NODE is None, "node is not on PATH")
class IconRefs(unittest.TestCase):
    def test_every_id_an_icon_points_at_is_kept(self):
        # icons.mjs strips every id but the ones the icon refers to; it knew only url(#x), so a <use href="#x">
        # lost its target and the saved icon drew nothing.
        line = next(l.strip() for l in (CAPTURE / "icons.mjs").read_text().splitlines() if l.strip().startswith("const refsOf = "))
        svg = ('<svg><defs><symbol id="s1"><path d="M0 0"/></symbol><linearGradient id="g1"/><clipPath id="c-2"/></defs>'
               '<use href="#s1"/><use xlink:href="#s2"/><rect fill="url(#g1)" clip-path="url(&quot;#c-2&quot;)"/>'
               '<rect mask="url(\'#m3\')"/><a href="https://x.test/#nope"></a></svg>')
        res = subprocess.run([NODE, "-e", line + f"\nconsole.log(JSON.stringify([...refsOf({json.dumps(svg)})].sort()))"],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(json.loads(res.stdout), ["c-2", "g1", "m3", "s1", "s2"])


def icons_collect():
    """The in-page collect() from icons.mjs, as source."""
    lines = (CAPTURE / "icons.mjs").read_text().splitlines()
    i = lines.index("function collect() {")
    return "\n".join(lines[i:lines.index("}", i) + 1])


@unittest.skipIf(NODE is None or not Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class IconPaint(unittest.TestCase):
    def test_a_shared_gradient_keeps_its_styled_stop_colours(self):
        # Greptile on PR 1004: a gradient imported from the page whose stops are coloured by a class or a
        # style lost those colours when the copy's classes and styles were stripped, and drew black.
        page = ("<style>.a{stop-color:#ff0000}.b{stop-color:rgba(0,0,255,0.5)}</style>"
                "<svg width='0' height='0' style='position:absolute'><defs><linearGradient id='g'>"
                "<stop offset='0' class='a'/><stop offset='1' style='stop-color:#00ff00;stop-opacity:0.4'/>"
                "<stop offset='1' class='b'/><stop offset='1' stop-color='#123456'/></linearGradient></defs></svg>"
                "<button aria-label='Go'><svg width='24' height='24' viewBox='0 0 24 24'><rect width='24' height='24' fill='url(#g)'/></svg></button>")
        script = (f"const pw = await import({json.dumps(PLAYWRIGHT)}); const {{ chromium }} = pw.default ?? pw;\n"
                  f"{icons_collect()}\n"
                  "const b = await chromium.launch(); const p = await b.newPage();\n"
                  f"await p.setContent({json.dumps(page)});\n"
                  "const list = await p.evaluate(collect); await b.close();\n"
                  "console.log(JSON.stringify(list.map((x) => x.html)));")
        res = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        (html,) = json.loads(res.stdout)
        stops = re.findall(r"<stop[^>]*>", html)
        self.assertEqual(len(stops), 4, html)
        self.assertIn('stop-color="#ff0000"', stops[0])
        self.assertIn('stop-color="#00ff00"', stops[1])
        self.assertIn('stop-opacity="0.4"', stops[1])
        self.assertIn('stop-color="#0000ff"', stops[2])
        self.assertIn('stop-opacity="0.5"', stops[2])
        self.assertIn('stop-color="#123456"', stops[3])
        self.assertNotIn("class=", html)
        self.assertNotIn("style=", html)


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


class OneLightSwitch(unittest.TestCase):
    def test_renders_and_readings_share_the_light_switch(self):
        # render.mjs carried its own switch (every [data-mode] to light) while measure.mjs used lib.setLight
        # (dark/light/system only), so a product using data-mode for density rendered differently in the
        # light PNGs than in the light readings. Only lib.mjs may set data-mode now.
        signed = CAPTURE / "signed-in"
        own = [f.name for f in sorted(signed.glob("*.mjs")) if f.name != "lib.mjs" and "setAttribute('data-mode'" in f.read_text()]
        self.assertEqual(own, [])
        for f in ("render.mjs", "measure.mjs"):
            # a call, not the import or a comment: code lines only, and an awaited call with an argument
            code = "\n".join(l for l in (signed / f).read_text().splitlines() if not l.lstrip().startswith("//"))
            self.assertRegex(code, r"\bawait setLight\(\w+\)", f)


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
