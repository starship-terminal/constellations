"""capture/quantize.py carries .capture.json sidecars to screenshots/: a plain capture's sidecar is copied,
a stitched image's is rebuilt from its part tiles with a fresh dimensionCheck. The script is copied into
a throwaway package tree and run as a subprocess, so the committed screenshots/ is never touched.
Needs Pillow. Run: python3 -m unittest discover -s tools."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

from PIL import Image

SCRIPT = pathlib.Path(__file__).resolve().parent / "capture" / "quantize.py"


def sidecar(name, w, h, dpr=1, **extra):
    """A tile sidecar: the clip is CSS pixels, the PNG is device pixels (clip x dpr)."""
    return {"schemaVersion": 1, "screenshot": name, "requested": {"deviceScaleFactor": dpr},
            "actual": {"devicePixelRatio": dpr}, "capture": {"mode": "clip", "scale": "device",
            "clip": {"x": 0, "y": 0, "width": w, "height": h}}, "png": {"width": w * dpr, "height": h * dpr},
            "dimensionCheck": {"status": "pass"}, **extra}


class QuantizeSidecarTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(self.tmp.name)
        self.pkg, self.raw = root / "pkg", root / "raw"
        (self.pkg / "tools" / "capture").mkdir(parents=True)
        self.raw.mkdir()
        shutil.copyfile(SCRIPT, self.pkg / "tools" / "capture" / "quantize.py")

    def tearDown(self):
        self.tmp.cleanup()

    def run_quantize(self):
        subprocess.run([sys.executable, str(self.pkg / "tools" / "capture" / "quantize.py"), str(self.raw)],
                       check=True, capture_output=True)
        return self.pkg / "screenshots"

    def test_plain_capture_sidecar_is_copied(self):
        Image.new("RGB", (8, 6), (250, 250, 250)).save(self.raw / "home.png")
        meta = sidecar("home.png", 8, 6, capturedAt="2026-01-01T00:00:00Z")
        (self.raw / "home.png.capture.json").write_text(json.dumps(meta))
        out = self.run_quantize()
        self.assertEqual(json.loads((out / "home.png.capture.json").read_text()), meta)

    def test_capture_without_sidecar_writes_none(self):
        Image.new("RGB", (8, 6), (250, 250, 250)).save(self.raw / "home.png")
        out = self.run_quantize()
        self.assertTrue((out / "home.png").exists())
        self.assertFalse((out / "home.png.capture.json").exists())

    def tiles(self, heights, dpr=1, claimed=None, write_sidecars=True):
        for i, h in enumerate(heights):
            Image.new("RGB", (8 * dpr, h * dpr), (10 * i, 0, 0)).save(self.raw / f"long.part{i}.png")
            if write_sidecars:
                meta = sidecar(f"long.part{i}.png", 8, (claimed or heights)[i], dpr)
                (self.raw / f"long.part{i}.png.capture.json").write_text(json.dumps(meta))

    def test_stitched_sidecar_is_rebuilt_from_parts(self):
        self.tiles((6, 4))
        meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
        self.assertEqual(meta["screenshot"], "long.png")
        self.assertEqual(meta["png"], {"width": 8, "height": 10})
        self.assertEqual(meta["capture"]["mode"], "stitchedParts")
        self.assertEqual(meta["capture"]["clip"], {"x": 0, "y": 0, "width": 8, "height": 10})
        self.assertEqual(meta["stitchedFrom"], ["long.part0.png", "long.part1.png"])
        self.assertEqual(len(meta["partClip"]), 2)
        self.assertEqual(meta["dimensionCheck"]["status"], "pass")

    def test_stitched_2x_capture_keeps_css_clip_and_passes(self):
        self.tiles((6, 4), dpr=2)
        meta = json.loads((self.run_quantize() / "long.png.capture.json").read_text())
        self.assertEqual(meta["png"], {"width": 16, "height": 20})
        self.assertEqual(meta["capture"]["clip"], {"x": 0, "y": 0, "width": 8, "height": 10})
        self.assertEqual(meta["dimensionCheck"]["expected"], {"width": 16, "height": 20})
        self.assertEqual(meta["dimensionCheck"]["status"], "pass")

    def test_stitched_dimension_check_fails_when_clips_disagree(self):
        self.tiles((6,), claimed=(20,))
        check = json.loads((self.run_quantize() / "long.png.capture.json").read_text())["dimensionCheck"]
        self.assertEqual(check["status"], "fail")
        self.assertIn("expected 8x20", check["error"])

    def test_stitched_without_tile_sidecars_writes_none(self):
        self.tiles((6, 4), write_sidecars=False)
        out = self.run_quantize()
        self.assertTrue((out / "long.png").exists())
        self.assertFalse((out / "long.png.capture.json").exists())

    def test_stitched_with_one_missing_tile_sidecar_writes_none(self):
        self.tiles((6, 4))
        (self.raw / "long.part1.png.capture.json").unlink()
        self.assertFalse((self.run_quantize() / "long.png.capture.json").exists())

    def test_rerun_without_sidecar_drops_the_old_one(self):
        Image.new("RGB", (8, 6), (250, 250, 250)).save(self.raw / "home.png")
        (self.raw / "home.png.capture.json").write_text(json.dumps(sidecar("home.png", 8, 6)))
        out = self.run_quantize()
        self.assertTrue((out / "home.png.capture.json").exists())
        (self.raw / "home.png.capture.json").unlink()
        out = self.run_quantize()
        self.assertTrue((out / "home.png").exists())
        self.assertFalse((out / "home.png.capture.json").exists())


if __name__ == "__main__":
    unittest.main()
