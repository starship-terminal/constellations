"""tools/kit/capture/crop.mjs: one size rule for every route's component crops. Needs node and Pillow;
skipped without them. Run with `make test`."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

CAPTURE = Path(__file__).resolve().parent / "kit" / "capture"
NODE = shutil.which("node")


@unittest.skipIf(NODE is None or Image is None, "node or Pillow is not installed")
class CropRule(unittest.TestCase):
    def test_both_routes_halve_by_the_same_rule(self):
        sizes = {"small.png": (400, 300), "wide.png": (1700, 40), "big.png": (1200, 1100), "edge.png": (1600, 750)}
        with tempfile.TemporaryDirectory() as d:
            for name, wh in sizes.items():
                Image.new("RGB", wh, (200, 40, 40)).save(Path(d) / name)
            files = [str(Path(d) / n) for n in sizes]
            res = subprocess.run([NODE, "--input-type=module", "-e",
                                  f"import {{ quantizeCrop }} from {json.dumps((CAPTURE / 'crop.mjs').as_uri())};"
                                  f"console.log(JSON.stringify({json.dumps(files)}.map((f) => quantizeCrop(f, {json.dumps(sys.executable)}))))"],
                                 capture_output=True, text=True, timeout=60)
            self.assertEqual(res.returncode, 0, res.stderr)
            self.assertEqual(json.loads(res.stdout), [False, True, True, False])
            got = {n: Image.open(Path(d) / n).size for n in sizes}
        self.assertEqual(got, {"small.png": (400, 300), "wide.png": (850, 20), "big.png": (600, 550), "edge.png": (1600, 750)})

    def test_every_route_uses_the_shared_rule(self):
        for rel in ("public/lib.mjs", "signed-in/measure.mjs"):
            src = (CAPTURE / rel).read_text()
            self.assertIn("quantizeCrop(", src, rel)
            self.assertNotIn("im.resize(", src, rel)


if __name__ == "__main__":
    unittest.main()
