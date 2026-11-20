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


# Node test files with a runner of their own elsewhere under tools/, and that runner.
NODE_RUN_ELSEWHERE = {"test_screenshot.mjs": "test_capture_screenshot.py", "test_motion.mjs": "test_kit_motion.py"}


TAP_OK = re.compile(r"^(\s*)ok \d+ - (.*?)(?: # (SKIP|TODO)\b.*)?$")
TAP_TYPE = re.compile(r"^\s*type: '(\w+)'")


def node_tests_ran(f):
    """Run one node test file with the TAP reporter: (exit code, output, the names of the tests that ran).
    Counted: a passing entry of type 'test', at any depth (inside a describe too). Not counted: a skipped or
    todo test, a suite (type 'suite', empty or not), and the one entry node prints, named after the file,
    for a file that registers no test."""
    res = subprocess.run([NODE, "--test", "--test-reporter=tap", str(f)], capture_output=True, text=True, timeout=120)
    lines, names = res.stdout.splitlines(), []
    for i, line in enumerate(lines):
        m = TAP_OK.match(line)
        if not m or m.group(3) or m.group(2).strip() == str(f):
            continue
        kind = next((t.group(1) for t in map(TAP_TYPE.match, lines[i + 1:i + 8]) if t), None)
        if kind == "test":
            names.append(m.group(2).strip())
    return res.returncode, res.stdout + res.stderr, names


@unittest.skipIf(NODE is None, "node is not on PATH")
class KitNodeTests(unittest.TestCase):
    def test_every_other_kit_node_test_file_passes(self):
        # Any tools/kit/**/test_*.mjs, so a new one runs under `make test` without its own runner. The TAP
        # reporter is named (node picks its spec reporter on CI) so a file whose tests never ran is caught too.
        files = sorted(p for p in (HERE / "kit").rglob("test_*.mjs") if p.name not in NODE_RUN_ELSEWHERE)
        for must in (CAPTURE / "test_readings.mjs", CAPTURE / "public/test_pin.mjs"):
            self.assertIn(must, files)
        for f in files:
            with self.subTest(file=str(f.relative_to(HERE.parent))):
                code, out, names = node_tests_ran(f)
                self.assertEqual(code, 0, out[-4000:])
                self.assertRegex(out, r"(?m)^# fail 0$")
                self.assertTrue(names, f"no test ran:\n{out[-2000:]}")

    def test_a_file_that_registers_no_test_is_not_counted_as_run(self):
        # node reports an empty file as "ok 1 - <the file>" and "# pass 1"
        with tempfile.TemporaryDirectory() as d:
            empty, one = Path(d) / "test_empty.mjs", Path(d) / "test_one.mjs"
            empty.write_text("import test from 'node:test';\n")
            one.write_text("import test from 'node:test';\ntest('one', () => {});\n")
            self.assertEqual(node_tests_ran(empty)[2], [])
            self.assertEqual(node_tests_ran(one)[2], ["one"])

    def test_skipped_and_todo_tests_and_suites_are_not_counted_as_run(self):
        # Train 25's review of PR 1351: a skipped or todo test, or an empty describe, still counted
        with tempfile.TemporaryDirectory() as d:
            only_skips = Path(d) / "test_skips.mjs"
            only_skips.write_text("import { test, describe } from 'node:test';\n"
                                  "test('s', { skip: true }, () => {});\ntest.todo('t');\ndescribe('empty suite', () => {});\n")
            mixed = Path(d) / "test_mixed.mjs"
            mixed.write_text("import { test, describe } from 'node:test';\n"
                             "test('s', { skip: true }, () => {});\ndescribe('suite', () => { test('inner', () => {}); });\n")
            self.assertEqual(node_tests_ran(only_skips)[2], [])
            self.assertEqual(node_tests_ran(mixed)[2], ["inner"])

    def test_every_kit_node_test_file_has_a_runner(self):
        # the ones left out above are run by their own wrapper, which must exist and name the file
        for name, runner in NODE_RUN_ELSEWHERE.items():
            with self.subTest(file=name):
                self.assertTrue((CAPTURE / name).is_file(), name)
                self.assertIn(f"kit/capture/{name}", (HERE / runner).read_text(), runner)


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
    def collect(self, page):
        """collect() run in Chromium on one page: the saved html of each icon, or None for one left out."""
        script = (f"const pw = await import({json.dumps(PLAYWRIGHT)}); const {{ chromium }} = pw.default ?? pw;\n"
                  f"{icons_collect()}\n"
                  "const b = await chromium.launch(); const p = await b.newPage();\n"
                  f"await p.setContent({json.dumps(page)});\n"
                  "const list = await p.evaluate(collect); await b.close();\n"
                  "console.log(JSON.stringify(list.map((x) => x && x.html)));")
        res = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        return json.loads(res.stdout)

    def test_paint_a_group_inside_a_sprite_symbol_sets_is_kept(self):
        # Train 20's review: a path in an imported symbol with no class or style of its own was left to
        # inherit from the <use>, but a group around it supplied the paint through its class, and the cleanup
        # dropped that class, so the line vanished. A shape that inherits from the sprite sheet stays
        # recolourable (no paint written).
        page = ("<style>.line{fill:none;stroke:#ff0000;stroke-width:2px}.dot{fill:#00ff00}</style>"
                "<svg width='0' height='0' style='position:absolute'><symbol id='a' viewBox='0 0 24 24'>"
                "<g class='line'><path d='M2 12h20'/></g><g style='fill:#0000ff'><circle cx='4' cy='4' r='2'/></g>"
                "<path class='dot' d='M0 0h1v1z'/><path d='M3 3h1v1z'/></symbol></svg>"
                "<button aria-label='Go' style='color:#333'><svg width='24' height='24'><use href='#a'/></svg></button>")
        (html,) = self.collect(page)
        paths = re.findall(r"<(?:path|circle)[^>]*>", html)
        self.assertEqual(len(paths), 4, html)
        self.assertIn('stroke="#ff0000"', paths[0])
        self.assertIn('fill="none"', paths[0])
        self.assertIn('stroke-width="2"', paths[0])
        self.assertIn('fill="#0000ff"', paths[1])
        self.assertIn('fill="#00ff00"', paths[2])
        self.assertNotIn("fill=", paths[3])   # inherits from the <use>, so the icon can still be recoloured
        self.assertNotIn("class=", html)
        self.assertNotIn("style=", html)

    def test_a_group_that_sets_only_a_stroke_leaves_the_fill_alone(self):
        # Greptile on PR 1353: one differing property opened the whole copy, so the sprite sheet's default
        # black fill was written onto an outline whose group set only a stroke, and the outline came out filled.
        page = ("<svg width='0' height='0' style='position:absolute'><symbol id='s' viewBox='0 0 24 24'>"
                "<g style='stroke:#ff0000'><path d='M2 12h20'/></g><g style='fill:#00ff00'><path d='M0 0h4v4z'/></g></symbol></svg>"
                "<button aria-label='Go'><svg width='24' height='24' fill='none'><use href='#s'/></svg></button>")
        (html,) = self.collect(page)
        outline, box = re.findall(r"<path[^>]*>", html)
        self.assertIn('stroke="#ff0000"', outline)
        self.assertNotIn("fill=", outline)   # the <use>'s fill="none" still applies
        self.assertIn('fill="#00ff00"', box)
        self.assertNotIn("stroke=", box)

    def test_a_fill_in_the_icons_own_colour_still_follows_it(self):
        # Greptile on 9d4bd6843: with the fill judged apart, an explicit fill="#000000" equal to the icon's
        # colour (black text) under a stroke-only group stopped becoming currentColor, so it no longer recoloured
        page = ("<svg width='0' height='0' style='position:absolute'><symbol id='s' viewBox='0 0 24 24'>"
                "<g style='stroke:#ff0000'><path fill='#000000' d='M2 12h20'/></g></symbol></svg>"
                "<button aria-label='Go' style='color:#000000'><svg width='24' height='24'><use href='#s'/></svg></button>")
        (html,) = self.collect(page)
        (path,) = re.findall(r"<path[^>]*>", html)
        self.assertIn('fill="currentColor"', path)
        self.assertIn('stroke="#ff0000"', path)

    def test_a_width_set_inside_leaves_the_stroke_colour_to_the_use(self):
        # Train 25's review: a group that set only stroke-width counted as permission to copy the stroke
        # colour too, so the sheet's red stroke was written where the <use> supplies blue
        page = ("<svg width='0' height='0' style='position:absolute;stroke:#ff0000'><symbol id='s' viewBox='0 0 24 24'>"
                "<g style='stroke-width:2px'><path d='M2 12h20'/></g></symbol></svg>"
                "<button aria-label='Go'><svg width='24' height='24' fill='none' stroke='#0000ff'><use href='#s'/></svg></button>")
        (html,) = self.collect(page)
        (path,) = re.findall(r"<path[^>]*>", html)
        self.assertIn('stroke-width="2"', path)
        self.assertNotIn("stroke=", path.replace("stroke-width=", ""))   # the colour still comes from the <use>

    def test_a_group_fill_equal_to_the_sheets_default_is_kept(self):
        # Train 25's review: a group that sets the hidden sheet's default fill on purpose (black, by style or
        # by class) looked like inherited paint, its paths got no fill, and the cleanup dropped the group's
        # style, so under <svg fill="none"> the parts disappeared
        page = ("<style>.ink{fill:#000000}</style>"
                "<svg width='0' height='0' style='position:absolute'><symbol id='s' viewBox='0 0 24 24'>"
                "<g style='fill:#000000'><path d='M0 0h4v4z'/></g><g class='ink'><path d='M5 5h4v4z'/></g>"
                "<path d='M9 9h1v1z'/></symbol></svg>"
                "<button aria-label='Go' style='color:#333333'><svg width='24' height='24' fill='none'><use href='#s'/></svg></button>")
        (html,) = self.collect(page)
        styled, classed, plain = re.findall(r"<path[^>]*>", html)
        self.assertIn('fill="#000000"', styled)
        self.assertIn('fill="#000000"', classed)
        self.assertNotIn("fill=", plain)   # nothing inside sets it, so the <use>'s fill="none" applies

    def test_an_icon_drawn_from_another_files_sprite_is_left_out(self):
        # finding 20-8: <use href="/icons/sprite.svg#x"> draws nothing in the saved file, so it was saved blank
        page = ("<svg width='0' height='0' style='position:absolute'><symbol id='s' viewBox='0 0 24 24'><path d='M0 0h24v24z'/></symbol></svg>"
                "<button aria-label='A'><svg width='24' height='24'><use href='/icons/icon_definitions.svg#add'/></svg></button>"
                "<button aria-label='B'><svg width='24' height='24'><use xlink:href='https://cdn.example.test/s.svg#x'/></svg></button>"
                "<button aria-label='C'><svg width='24' height='24'><use href='#s'/></svg></button>")
        got = self.collect(page)
        self.assertEqual(len(got), 3)
        self.assertIsNone(got[0])
        self.assertIsNone(got[1])
        self.assertIn('<symbol id="s"', got[2])

    def test_a_shared_gradient_keeps_its_styled_stop_colours(self):
        # Greptile on PR 1004: a gradient imported from the page whose stops are coloured by a class or a
        # style lost those colours when the copy's classes and styles were stripped, and drew black.
        page = ("<style>.a{stop-color:#ff0000}.b{stop-color:rgba(0,0,255,0.5)}</style>"
                "<svg width='0' height='0' style='position:absolute'><defs><linearGradient id='g'>"
                "<stop offset='0' class='a'/><stop offset='1' style='stop-color:#00ff00;stop-opacity:0.4'/>"
                "<stop offset='1' class='b'/><stop offset='1' stop-color='#123456'/></linearGradient></defs></svg>"
                "<button aria-label='Go'><svg width='24' height='24' viewBox='0 0 24 24'><rect width='24' height='24' fill='url(#g)'/></svg></button>")
        (html,) = self.collect(page)
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
                                     text=True, timeout=60, env={**os.environ, "SNAPS": d, "PLAYWRIGHT": PLAYWRIGHT, "KIT_EXAMPLE": "1"})
                self.assertEqual(res.returncode, 2, (bad, res.stderr))
                self.assertIn("--jobs needs a whole number", res.stderr)


if __name__ == "__main__":
    unittest.main()
