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


def sidecar(name, w, h, **extra):
    return {"schemaVersion": 1, "screenshot": name, "capture": {"mode": "viewport", "scale": "device",
            "clip": {"x": 0, "y": 0, "width": w, "height": h}}, "png": {"width": w, "height": h},
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

    def test_stitched_sidecar_is_rebuilt_from_parts(self):
        for i, h in enumerate((6, 4)):
            Image.new("RGB", (8, h), (10 * i, 0, 0)).save(self.raw / f"long.part{i}.png")
            (self.raw / f"long.part{i}.png.capture.json").write_text(json.dumps(sidecar(f"long.part{i}.png", 8, h)))
        out = self.run_quantize()
        meta = json.loads((out / "long.png.capture.json").read_text())
        self.assertEqual(meta["screenshot"], "long.png")
        self.assertEqual(meta["png"], {"width": 8, "height": 10})
        self.assertEqual(meta["capture"]["mode"], "stitchedParts")
        self.assertEqual(meta["capture"]["clip"]["height"], 10)
        self.assertEqual(meta["stitchedFrom"], ["long.part0.png", "long.part1.png"])
        self.assertEqual(len(meta["partClip"]), 2)
        self.assertEqual(meta["dimensionCheck"]["status"], "pass")

    def test_stitched_dimension_check_fails_when_clips_disagree(self):
        Image.new("RGB", (8, 6), (0, 0, 0)).save(self.raw / "long.part0.png")
        (self.raw / "long.part0.png.capture.json").write_text(json.dumps(sidecar("long.part0.png", 8, 20)))
        out = self.run_quantize()
        check = json.loads((out / "long.png.capture.json").read_text())["dimensionCheck"]
        self.assertEqual(check["status"], "fail")
        self.assertIn("expected 8x20", check["error"])


if __name__ == "__main__":
    unittest.main()
