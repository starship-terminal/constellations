"""Tests for tools/redact_images.py. Run with `make test`; skipped when Pillow or numpy is missing."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

try:
    import numpy as np
    from PIL import Image
    import redact_images as R
except ImportError:  # the Makefile needs only python3; this tool needs Pillow and numpy
    R = None


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class Fill(unittest.TestCase):
    def test_rows_keeps_a_highlighted_row(self):
        a = np.zeros((60, 100, 3), np.uint8) + 30
        a[20:40, :] = 70                                   # a hover-highlighted list row
        a[22:38, 30:70] = 255                              # text inside it
        R.paint(a, (30, 10, 70, 50, "rows"))
        self.assertTrue((a[25, 30:70] == 70).all())        # the row keeps its highlight
        self.assertTrue((a[5, 30:70] == 30).all() and (a[45, 30:70] == 30).all())
        self.assertTrue((a[12, 30:70] == 30).all())        # text gone

    def test_rows_blends_a_gradient(self):
        a = np.zeros((10, 100, 3), np.uint8)
        a[:, :] = np.linspace(0, 200, 100, dtype=np.uint8)[None, :, None]
        a[3:7, 40:60] = 255
        R.paint(a, (40, 0, 60, 10, "rows"))
        self.assertTrue(abs(int(a[5, 50, 0]) - 100) < 12)

    def test_pixelate_flattens_text_and_refuses_fine_blocks(self):
        a = np.zeros((96, 96, 3), np.uint8)
        a[::2] = 255                                       # one-pixel stripes, like small text
        R.paint(a, (0, 0, 96, 96, "pixelate:48"))
        self.assertLess(int(a.std()), 4)
        with self.assertRaises(SystemExit):
            R.paint(a, (0, 0, 96, 96, "pixelate:4"))

    def test_solid_uses_the_ring_colour(self):
        a = np.full((40, 40, 3), 9, np.uint8)
        a[10:30, 10:30] = 200
        R.paint(a, (10, 10, 30, 30, "solid"))
        self.assertTrue((a == 9).all())


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class Rules(unittest.TestCase):
    RULES = {"families": [
        {"files": ["screenshots/*.png"], "skip": ["screenshots/mobile-*"], "size": [[100, 80]],
         "rects": [[10, 10, -10, -10], [5, 5, 20, 20, "solid"]],
         "ocr_lines": [{"rect": [0, 0, -1, -1], "keep": ["^ok$"]}]}]}

    def test_globs_skip_size_and_negative_edges(self):
        rects, regions = R.rules_for(self.RULES, "screenshots/home.png", (100, 80))
        self.assertEqual(rects, [(10, 10, 90, 70, "rows"), (5, 5, 20, 20, "solid")])
        self.assertEqual(len(regions), 1)
        self.assertEqual(R.rules_for(self.RULES, "screenshots/mobile-home.png", (100, 80)), ([], []))
        self.assertEqual(R.rules_for(self.RULES, "screenshots/home.png", (101, 80)), ([], []))

    def test_stems_match_whole_components_only(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            crops = pkg / "components/crops"
            crops.mkdir(parents=True)
            names = ["file-row-default.png", "file-row-light-hover.png", "file-row-light.png",
                     "file-row-title-default.png", "file-row-icon-light.png", "file-row-menu-open.png"]
            for n in names:
                (crops / n).write_bytes(b"")
            got = sorted(f.name for f in R.stem_files(pkg, ["file-row"]))
            self.assertEqual(got, ["file-row-default.png", "file-row-light-hover.png", "file-row-light.png"])

    def test_stems_reach_crops_in_subfolders(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            sub = pkg / "components/crops/signed-in"
            sub.mkdir(parents=True)
            (sub / "goal-card-default.png").write_bytes(b"")
            (sub / "goal-card-title-default.png").write_bytes(b"")
            got = [f.name for f in R.stem_files(pkg, ["goal-card"])]
            self.assertEqual(got, ["goal-card-default.png"])


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class Commands(unittest.TestCase):
    def test_a_failed_tesseract_read_stops_the_run(self):
        import subprocess
        from unittest import mock
        failed = subprocess.CompletedProcess([], 1, stdout="", stderr="Error opening data file")
        with mock.patch.object(R.subprocess, "run", return_value=failed):
            with self.assertRaises(SystemExit):
                R.ocr_words(Image.new("RGB", (50, 50)))

    def test_check_refuses_an_empty_or_missing_package(self):
        with tempfile.TemporaryDirectory() as d:
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            with self.assertRaises(SystemExit):
                R.main(["check", str(Path(d) / "nope"), "--patterns", str(pats)])
            with self.assertRaises(SystemExit):                # a package with no images
                R.main(["check", d, "--patterns", str(pats)])

    def test_wrap_ignore_skips_only_wrapped_only_matches_of_listed_images(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            (pkg / "screenshots").mkdir()
            for n in ("a", "b", "c"):
                Image.new("RGB", (4, 4)).save(pkg / f"screenshots/{n}.png")
            pats = pkg / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules = pkg / "r.json"
            rules.write_text(json.dumps({"ocr": {"wrap_ignore": ["screenshots/a.png", "screenshots/c.png"]}}))

            def run(name, hits):
                with mock.patch.object(R, "ocr_words", return_value=[]), \
                     mock.patch.object(R, "ocr_hits", return_value=hits), \
                     self.assertRaises(SystemExit) as cm:
                    R.main(["check", d, "--patterns", str(pats), "--rules", str(rules), str(pkg / f"screenshots/{name}.png")])
                return cm.exception.code

            self.assertEqual(run("a", ([], True)), 0)                 # listed, wrapped only: passes
            self.assertEqual(run("b", ([], True)), 1)                 # not listed: still fails
            self.assertEqual(run("c", ([(0, 0, 1, 1)], True)), 1)     # listed, but a direct match: still fails

    def test_only_limits_deletions_too(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            (pkg / "components/crops").mkdir(parents=True)
            Image.new("RGB", (4, 4)).save(pkg / "components/crops/file-row-default.png")
            Image.new("RGB", (4, 4)).save(pkg / "screenshots.png")
            rules = pkg / "r.json"
            rules.write_text(json.dumps({"delete_stems": ["file-row"], "ocr": {"net": False}}))
            with self.assertRaises(SystemExit) as cm:
                R.main(["apply", d, "--rules", str(rules), "--only", "screenshots/*.png"])
            self.assertTrue((pkg / "components/crops/file-row-default.png").exists())
            with self.assertRaises(SystemExit):
                R.main(["apply", d, "--rules", str(rules), "--only", "components/crops/*.png"])
            self.assertFalse((pkg / "components/crops/file-row-default.png").exists())


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class Matching(unittest.TestCase):
    def words(self, text, y=0):
        out, x = [], 0
        for t in text.split():
            out.append((t, x, y, 10 * len(t), 12, (str(y), "1", "1")))
            x += 10 * len(t) + 8
        return out

    def test_pattern_boxes_cover_only_the_matching_words(self):
        pats = [re.compile("secret plan", re.I)]
        boxes = R.find_private(self.words("a Secret Plan here"), pats, False, [])
        self.assertEqual(len(boxes), 2)
        self.assertEqual(min(b[0] for b in boxes), 18)

    def test_emails_flagged_unless_allowed(self):
        w = self.words("me@private.test")
        self.assertEqual(len(R.find_private(w, [], True, [])), 1)
        self.assertEqual(R.find_private(w, [], True, [r"@private\.test$"]), [])

    def test_region_boxes_skip_keep_words_and_glyphs(self):
        w = self.words("ok") + self.words("Private title", y=30) + self.words("..", y=60)
        boxes = R.region_boxes(w, [(0, 0, 500, 500, [re.compile("^ok$")])], [])
        self.assertEqual(len(boxes), 1)
        self.assertEqual(boxes[0][1], 30)

    def test_wrapped_title_is_found_when_two_reads_see_it(self):
        pats = [re.compile("secret plan", re.I)]
        one = self.words("a Secret", y=0) + self.words("Plan here", y=40)
        reads = [one, [(t, x + 1, y + 1, w, h, ("b",) + k) for t, x, y, w, h, k in one]]
        self.assertEqual(R.ocr_hits(pats, {"emails": False}, reads), ([], True))
        self.assertEqual(R.ocr_hits(pats, {"emails": False}, [self.words("Secret Plan")])[1], False)

    def test_patterns_file_is_read_not_embedded(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "p.json"
            f.write_text(json.dumps({"replace": [["a(b", "x"], ["real", "x"]]}))
            pats = R.load_patterns([str(f)])                # an invalid regex falls back to a literal
            self.assertTrue(pats[0].search("xa(bx") and pats[1].search("REAL"))

    def test_patterns_file_email_allow_lets_the_owner_address_through(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "p.json"
            f.write_text(json.dumps({"replace": [["x", "y"]], "email_allow": [r"^owner@mine\.test$"]}))
            allow = R.load_email_allow([str(f)])
            self.assertEqual(allow, [r"^owner@mine\.test$"])
            self.assertEqual(R.find_private(self.words("owner@mine.test"), [], True, allow), [])
            self.assertEqual(len(R.find_private(self.words("other@mine.test"), [], True, allow)), 1)
            self.assertEqual(R.load_email_allow([]), [])


if __name__ == "__main__":
    unittest.main()
