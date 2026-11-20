"""Sidecar handling in tools/kit/capture/quantize.py and in every package copy that rebuilds a stitched
sidecar (grep stitched_sidecar). A plain capture's .capture.json is copied; a stitched image's is rebuilt
from its tiles with a fresh dimensionCheck. Each script is copied into a throwaway package tree and run as
a subprocess, so the committed screenshots/ is never touched. Needs Pillow; skipped without it."""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "tools" / "kit" / "capture" / "quantize.py"

def distinct(paths):
    """One script per distinct body: byte-identical copies behave identically, and every run is a
    subprocess (about 3,000 per make test when each of 400 copies ran), so each body is tested once."""
    seen, out = set(), []
    for p in paths:
        h = hashlib.sha1(p.read_bytes()).hexdigest()
        if h not in seen:
            seen.add(h)
            out.append(p)
    return out


COPIES = sorted(p for p in ROOT.glob("systems/*/tools/capture/quantize.py") if "def stitched_sidecar" in p.read_text())
SCRIPTS = distinct([KIT] + COPIES)
# designmodo judges a sheet by the tiles' own recorded dimensionCheck and writes a failing sidecar for a
# tile it cannot vouch for, instead of none; that is deliberate, so its tests expect "fail" where the rest expect no file.
RECORDED = [s for s in SCRIPTS if "recorded checks" in s.read_text()]
# Copies that refuse an incomplete or unmeasured tile set outright (the kit's check_tiles, and the
# package copies that carried it first); the rest write no sidecar for a set they cannot vouch for.
CHECKED = [s for s in SCRIPTS if "def check_tiles" in s.read_text()]
UNMEASURED_NONE = [s for s in SCRIPTS if s not in CHECKED and s not in RECORDED]


def sidecar(name, w, h, y=0, dpr=1):
    """A tile sidecar: the clip is CSS pixels, the PNG is device pixels (clip x dpr)."""
    return {"schemaVersion": 1, "screenshot": name, "requested": {"deviceScaleFactor": dpr},
            "actual": {"devicePixelRatio": dpr}, "capture": {"mode": "clip", "scale": "device",
            "clip": {"x": 0, "y": y, "width": w, "height": h}}, "png": {"width": w * dpr, "height": h * dpr},
            "dimensionCheck": {"status": "pass", "expected": {"width": w * dpr, "height": h * dpr}}}


@unittest.skipIf(Image is None, "Pillow is not installed")
class QuantizeSidecarTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def stage(self, source):
        root = pathlib.Path(self.tmp.name)
        self.pkg, self.raw = root / "pkg", root / "raw"
        script = self.pkg / "tools" / "capture" / "quantize.py"
        script.parent.mkdir(parents=True)
        self.raw.mkdir()
        shutil.copyfile(source, script)
        self.script, self.source = script, source.read_text()

    def run_quantize(self):
        done = subprocess.run([sys.executable, str(self.script), str(self.raw)], capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr[-500:])
        return self.pkg / "screenshots"

    def tiles(self, heights, dpr=1, sidecars=True, css_sized=False, doc_h=None, clip=True):
        """Write the tile PNGs and sidecars. css_sized: the PNG is CSS-sized although dpr is 2 (capture.scale
        'css'); doc_h records actual.documentSize; clip=False leaves capture.clip out."""
        y = 0
        px = 1 if css_sized else dpr
        for i, h in enumerate(heights):
            Image.new("RGB", (8 * px, h * px), (10 * i, 0, 0)).save(self.raw / f"long.part{i}.png")
            if sidecars:
                meta = sidecar(f"long.part{i}.png", 8, h, y, dpr)
                meta["png"] = {"width": 8 * px, "height": h * px}
                meta["dimensionCheck"]["expected"] = {"width": 8 * px, "height": h * px}
                if css_sized:
                    meta["capture"]["scale"] = "css"
                if doc_h:
                    meta["actual"]["documentSize"] = {"width": 8, "height": doc_h}
                if not clip:
                    del meta["capture"]["clip"]
                (self.raw / f"long.part{i}.png.capture.json").write_text(json.dumps(meta))
            y += h

    def run_refused(self):
        done = subprocess.run([sys.executable, str(self.script), str(self.raw)], capture_output=True, text=True)
        self.assertNotEqual(done.returncode, 0, "an incomplete tile set was stitched")
        self.assertIn("quantize:", done.stderr)
        self.assertFalse((self.pkg / "screenshots" / "long.png").exists())
        return done.stderr

    def each(self, body, scripts=SCRIPTS):
        """Run body() once per script, each in a fresh scratch package, reporting each script apart."""
        self.assertTrue(scripts, "the filter that picks these scripts matched none")
        for source in scripts:
            with self.subTest(script=str(source.relative_to(ROOT))):
                shutil.rmtree(self.tmp.name, ignore_errors=True)
                pathlib.Path(self.tmp.name).mkdir()
                self.stage(source)
                body()

    def test_stitched_1x_sidecar_is_rebuilt_and_passes(self):
        def body():
            self.tiles((6, 4))
            meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
            self.assertEqual(meta["png"], {"width": 8, "height": 10})
            self.assertEqual(meta["capture"]["mode"], "stitchedParts")
            self.assertEqual(meta["stitchedFrom"], ["long.part0.png", "long.part1.png"])
            self.assertEqual(meta["dimensionCheck"]["status"], "pass")
        self.each(body)

    def test_stitched_2x_capture_keeps_css_clip_and_passes(self):
        def body():
            self.tiles((6, 4), dpr=2)
            meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
            self.assertEqual(meta["png"], {"width": 16, "height": 20})
            self.assertEqual(meta["capture"]["clip"]["width"], 8)
            self.assertEqual(meta["capture"]["clip"]["height"], 10)
            self.assertEqual(meta["dimensionCheck"]["expected"], {"width": 16, "height": 20})
            self.assertEqual(meta["dimensionCheck"]["status"], "pass")
        self.each(body)

    def test_stitched_css_sized_capture_at_dpr_2_passes(self):
        # capture.scale 'css': the PNG is the clip's CSS size even though devicePixelRatio is 2.
        def body():
            self.tiles((6, 4), dpr=2, css_sized=True)
            meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
            self.assertEqual(meta["png"], {"width": 8, "height": 10})
            self.assertEqual(meta["dimensionCheck"]["expected"], {"width": 8, "height": 10})
            self.assertEqual(meta["dimensionCheck"]["status"], "pass")
        # factory's copy scales by devicePixelRatio alone and never reads capture.scale.
        self.each(body, [s for s in SCRIPTS if "'css'" in s.read_text()])

    def test_stitched_with_recorded_document_height_scales_the_intended_height(self):
        # Copies that check coverage against actual.documentSize (check_tiles, epidemicsound) take the
        # intended height in CSS px and scale it to the PNG, so a complete 2x sheet still passes.
        def body():
            self.tiles((6, 4), dpr=2, doc_h=10)
            meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
            self.assertEqual(meta["dimensionCheck"]["expected"], {"width": 16, "height": 20})
            self.assertEqual(meta["dimensionCheck"]["status"], "pass")
            self.assertEqual(meta["capture"]["clip"]["height"], 10)
        self.each(body)

    def test_stitched_with_a_tile_missing_its_clip_writes_none(self):
        def body():
            self.tiles((6, 4))
            meta = json.loads((self.raw / "long.part1.png.capture.json").read_text())
            del meta["capture"]["clip"]
            (self.raw / "long.part1.png.capture.json").write_text(json.dumps(meta))
            self.assertFalse((self.run_quantize() / "long.png.capture.json").exists())
        self.each(body, UNMEASURED_NONE)

    def test_stitched_dimension_check_fails_when_sheet_disagrees(self):
        def body():
            self.tiles((6, 4))
            for i, h in enumerate((6, 4)):   # the sidecar claims taller tiles than the PNGs hold
                (self.raw / f"long.part{i}.png.capture.json").write_text(
                    json.dumps(sidecar(f"long.part{i}.png", 8, h, 0 if i == 0 else 6, 1) | {"png": {"width": 8, "height": h}}))
            Image.new("RGB", (8, 30), (1, 1, 1)).save(self.raw / "long.part1.png")
            check = json.loads((self.run_quantize() / "long.png.capture.json").read_text())["dimensionCheck"]
            self.assertEqual(check["status"], "fail")
        self.each(body)

    def test_stitched_without_tile_sidecars_writes_none(self):
        # Copies that refuse an unmeasured tile set (check_tiles) stop with an error instead.
        def body():
            self.tiles((6, 4), sidecars=False)
            out = self.run_quantize()
            self.assertTrue((out / "long.png").exists())
            self.assertFalse((out / "long.png.capture.json").exists())
        self.each(body, UNMEASURED_NONE)

    def test_stitched_with_one_missing_tile_sidecar_writes_none(self):
        def body():
            self.tiles((6, 4))
            (self.raw / "long.part1.png.capture.json").unlink()
            self.assertFalse((self.run_quantize() / "long.png.capture.json").exists())
        self.each(body, UNMEASURED_NONE)

    def test_recorded_check_copies_fail_a_sheet_whose_tile_has_no_sidecar(self):
        def body():
            self.tiles((6, 4), sidecars=False)
            check = json.loads((self.run_quantize() / "long.png.capture.json").read_text())["dimensionCheck"]
            self.assertEqual(check["status"], "fail")
        self.each(body, RECORDED)

    def test_rerun_without_sidecar_drops_the_old_one(self):
        def body():
            Image.new("RGB", (8, 6), (250, 250, 250)).save(self.raw / "home.png")
            (self.raw / "home.png.capture.json").write_text(json.dumps(sidecar("home.png", 8, 6)))
            out = self.run_quantize()
            self.assertTrue((out / "home.png.capture.json").exists())
            (self.raw / "home.png.capture.json").unlink()
            out = self.run_quantize()
            self.assertTrue((out / "home.png").exists())
            self.assertFalse((out / "home.png.capture.json").exists())
        self.each(body)

    def test_rerun_of_a_stitched_image_drops_the_old_sidecar(self):
        def body():
            self.tiles((6, 4))
            out = self.run_quantize()
            self.assertTrue((out / "long.png.capture.json").exists())
            for f in self.raw.glob("*.capture.json"):
                f.unlink()
            self.assertFalse((self.run_quantize() / "long.png.capture.json").exists())
        self.each(body, UNMEASURED_NONE)

    def test_the_script_groups_are_what_the_tests_assume(self):
        self.assertIn(KIT, CHECKED)
        self.assertEqual(len(RECORDED), 1, RECORDED)
        self.assertTrue(UNMEASURED_NONE)

    def test_an_incomplete_tile_set_is_refused(self):
        # A run that lost a tile used to publish the tiles that survived as a shorter sheet marked pass.
        def missing_sidecar():
            self.tiles((6, 4)); (self.raw / "long.part1.png.capture.json").unlink()
            self.assertIn("no .capture.json", self.run_refused())

        def gap_in_the_run():
            self.tiles((6, 4, 5)); (self.raw / "long.part1.png").unlink(); (self.raw / "long.part1.png.capture.json").unlink()
            self.assertIn("not a contiguous run", self.run_refused())

        def failed_tile():
            self.tiles((6, 4))
            meta = json.loads((self.raw / "long.part1.png.capture.json").read_text())
            meta["dimensionCheck"] = {"status": "fail", "error": "png 8x3, expected 8x4"}
            (self.raw / "long.part1.png.capture.json").write_text(json.dumps(meta))
            self.assertIn("own dimension check", self.run_refused())

        def clips_do_not_join():
            self.tiles((6, 4))
            meta = json.loads((self.raw / "long.part1.png.capture.json").read_text())
            meta["capture"]["clip"]["y"] = 9
            (self.raw / "long.part1.png.capture.json").write_text(json.dumps(meta))
            self.assertIn("butt-join", self.run_refused())

        def short_of_the_page():
            self.tiles((6, 4), doc_h=30)   # the document was 30px; 10px of it was tiled
            self.assertIn("intended", self.run_refused())

        def first_tile_never_wrote():
            # screenshotWithMetadata threw on part0: only its failed sidecar is left, and the previous
            # run's stitched long.png still sits in raw/, so a PNG-only scan stitched nothing and published it.
            self.tiles((6, 4))
            meta = json.loads((self.raw / "long.part0.png.capture.json").read_text())
            meta["dimensionCheck"] = {"status": "fail", "error": "screenshot threw"}
            (self.raw / "long.part0.png.capture.json").write_text(json.dumps(meta))
            (self.raw / "long.part0.png").unlink()
            (self.raw / "long.part1.png").unlink(); (self.raw / "long.part1.png.capture.json").unlink()
            Image.new("RGB", (8, 10)).save(self.raw / "long.png")
            self.assertIn("long.part0.png: the tile never wrote its PNG (its sidecar records 'fail')", self.run_refused())

        def last_tile_never_wrote():
            self.tiles((6, 4)); (self.raw / "long.part1.png").unlink()   # no document height to fall short of
            self.assertIn("long.part1.png: the tile never wrote its PNG", self.run_refused())

        # The kit only: package copies that carried a check first refuse in their own ways, and some
        # miss a case (listed for the package wave); each is ported from the kit, then can join.
        for case in (missing_sidecar, gap_in_the_run, failed_tile, clips_do_not_join, short_of_the_page,
                     first_tile_never_wrote, last_tile_never_wrote):
            with self.subTest(case=case.__name__):
                self.each(case, [KIT])


if __name__ == "__main__":
    unittest.main()
