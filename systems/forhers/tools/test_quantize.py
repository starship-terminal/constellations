"""quantize.py never publishes a capture whose own sidecar recorded a failed dimension check."""
import json, pathlib, shutil, subprocess, sys, tempfile, unittest

try:
    from PIL import Image
except ImportError:  # the repo's tools are stdlib-only; Pillow is optional
    Image = None

SRC = pathlib.Path(__file__).resolve().parent / "capture" / "quantize.py"


def run(raw_files, tiles=None):
    """Copy quantize.py into a throwaway package layout so screenshots/ lands in the temp dir.

    tiles is {sheet_name: [(part_name, status, size)]}. A failed or missing part must not publish."""
    tmp = pathlib.Path(tempfile.mkdtemp())
    try:
        (tmp / "tools" / "capture").mkdir(parents=True)
        shutil.copy(SRC, tmp / "tools" / "capture" / "quantize.py")
        raw = tmp / "raw"
        raw.mkdir()
        for name, status in raw_files.items():
            Image.new("RGB", (8, 8), (200, 10, 10)).save(raw / name)
            if status is not None:
                (raw / f"{name}.capture.json").write_text(json.dumps({"dimensionCheck": {"status": status}}))
        for sheet, parts in (tiles or {}).items():
            for i, (status, size) in enumerate(parts):
                name = f"{sheet}.part{i}.png"
                Image.new("RGB", size, (10, 10, 200)).save(raw / name)
                if status is not None:
                    (raw / f"{name}.capture.json").write_text(json.dumps({
                        "dimensionCheck": {"status": status},
                        "capture": {"clip": {"x": 0, "y": i * size[1], "width": size[0], "height": size[1]}, "scale": "css"},
                        "png": {"width": size[0], "height": size[1]},
                    }))
        r = subprocess.run([sys.executable, str(tmp / "tools" / "capture" / "quantize.py"), str(raw)], capture_output=True, text=True)
        return r, sorted(p.name for p in (tmp / "screenshots").glob("*"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@unittest.skipIf(Image is None, "Pillow is not installed")
class Quantize(unittest.TestCase):
    def test_passing_capture_is_published_with_its_sidecar(self):
        r, out = run({"a.png": "pass"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(out, ["a.png", "a.png.capture.json"])

    def test_failed_capture_is_refused(self):
        r, _ = run({"a.png": "fail"})
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not publishing a failed capture", r.stderr)

    def test_capture_without_sidecar_is_published_without_one(self):
        r, out = run({"a.png": None})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(out, ["a.png"])

    def test_failed_tile_is_not_stitched_or_published(self):
        r, out = run({}, tiles={"long": [("pass", (8, 4)), ("fail", (12, 4))]})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(out, [])
        self.assertIn("dimensionCheck is 'fail'", r.stdout + r.stderr)

    def test_missing_tile_sidecar_publishes_the_stitch_without_one(self):
        # The shared sidecar test requires the image and forbids the sidecar.
        r, out = run({}, tiles={"long": [("pass", (8, 4)), (None, (8, 4))]})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(out, ["long.png"])
        self.assertIn("without a sidecar", r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
