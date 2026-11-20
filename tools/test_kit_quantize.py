"""tools/kit/capture/quantize.py, and every package copy that stitches tiles, stitches name.partN.png
tiles and skips a name that only looks like one (x.partial.png) instead of crashing. Needs Pillow;
skipped without it."""
import hashlib
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


# Package copies that stitch .partN tiles (the rest of the packages' quantize.py never glob for them),
# one per distinct body.
COPIES = distinct(sorted(p for p in ROOT.glob("systems/*/tools/capture/quantize.py") if "*.part*.png" in p.read_text()))


@unittest.skipIf(Image is None, "Pillow is not installed")
class KitQuantizeTest(unittest.TestCase):
    def run_copy(self, source):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            # The script writes screenshots/ three levels above itself, so run a copy in a scratch package.
            script = tmp / "pkg" / "tools" / "capture" / "quantize.py"
            script.parent.mkdir(parents=True)
            shutil.copy(source, script)
            raw = tmp / "raw"
            raw.mkdir()
            Image.new("RGB", (4, 3), (10, 20, 30)).save(raw / "page.part0.png")
            Image.new("RGB", (4, 5), (40, 50, 60)).save(raw / "page.part1.png")
            Image.new("RGB", (4, 4), (70, 80, 90)).save(raw / "x.partial.png")
            # Copies whose public.mjs writes a completion manifest only stitch a
            # marked set; give this complete two-tile set its manifest.
            if "parts.json" in source.read_text():
                (raw / "page.parts.json").write_text('{"tiles": ["page.part0.png", "page.part1.png"]}')
            # Stricter copies also require each tile's .capture.json sidecar:
            # a passed dimension check and a butt-joined clip.
            if "sidecar_for" in source.read_text():
                import json as _json
                (raw / "page.part0.png.capture.json").write_text(_json.dumps(
                    {"dimensionCheck": {"status": "pass"},
                     "capture": {"clip": {"x": 0, "y": 0, "width": 4, "height": 3}}}))
                (raw / "page.part1.png.capture.json").write_text(_json.dumps(
                    {"dimensionCheck": {"status": "pass"},
                     "capture": {"clip": {"x": 0, "y": 3, "width": 4, "height": 5}}}))
            done = subprocess.run([sys.executable, str(script), str(raw)], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr[-500:])
            with Image.open(raw / "page.png") as im:
                self.assertEqual(im.size, (4, 8))
            # Newer copies carry the capture sidecars through to screenshots/ and
            # write a stitched sidecar for tiled images; older copies quantize only.
            expected = ["page.png"] + (["page.png.capture.json"] if "stitchedParts" in source.read_text() else [])
            # The kit (and a copy that took its fix) keeps x.partial.png as the screenshot it is; older
            # copies drop it from screenshots/ without a word (finding 05-12, left for the package wave).
            if "TILE.match(f.name)" in source.read_text():
                expected.append("x.partial.png")
            self.assertEqual(sorted(p.name for p in (tmp / "pkg" / "screenshots").iterdir()), sorted(expected))
            return expected

    def test_a_partial_name_is_not_a_tile(self):
        self.assertIn("x.partial.png", self.run_copy(KIT))

    def test_every_package_copy_skips_a_partial_name(self):
        self.assertTrue(COPIES)
        for source in COPIES:
            with self.subTest(package=source.parts[-4]):
                self.run_copy(source)


if __name__ == "__main__":
    unittest.main()
