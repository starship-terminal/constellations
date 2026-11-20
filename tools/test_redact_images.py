"""Tests for tools/redact_images.py. Run with `make test`; skipped when Pillow or numpy is missing."""
import contextlib
import io
import json
import re
import shutil
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

    def test_binary_tesseract_stderr_still_stops_the_run_cleanly(self):
        # Seen when tesseract cannot open its input: it echoes the PNG's own bytes.
        import os
        import stat
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / "tesseract"
            fake.write_text("#!/bin/sh\nprintf 'Image file \\211PNG cannot be read!\\n' >&2\nexit 1\n")
            fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
            with mock.patch.dict(os.environ, {"PATH": f"{d}{os.pathsep}{os.environ.get('PATH', '')}"}):
                with self.assertRaises(SystemExit) as caught:
                    R.ocr_words(Image.new("RGB", (50, 50)))
        self.assertIn("tesseract failed (exit 1)", str(caught.exception))
        self.assertIn("cannot be read", str(caught.exception))

    def test_tall_narrow_captures_are_enlarged_like_short_ones(self):
        from unittest import mock
        sizes = []

        def fake(im, psm=11, min_conf=0):
            sizes.append(im.size)
            return []

        with mock.patch.object(R, "_tesseract_words", side_effect=fake):
            R.ocr_words(Image.new("RGB", (390, 3000)))         # a full-page mobile capture
            R.ocr_words(Image.new("RGB", (390, 300)))
            R.ocr_words(Image.new("RGB", (1440, 400)))
        self.assertEqual(sizes[0], (390 * 3, R.TILE * 3))          # first strip, enlarged 3x
        self.assertEqual(sizes[-2], (390 * 3, 300 * 3))
        self.assertEqual(sizes[-1], (1440, 400))
        self.assertEqual([R.ocr_scale(w) for w in (390, 499, 500, 999, 1000)], [3, 3, 2, 2, 1])

    @unittest.skipIf(shutil.which("tesseract") is None, "tesseract is not on PATH")
    def test_small_text_in_a_tall_capture_is_read(self):
        from PIL import ImageDraw, ImageFont
        im = Image.new("RGB", (390, 2000), "white")                # 9px text: read only when enlarged
        ImageDraw.Draw(im).text((10, 1500), "someone@private.test", fill="black", font=ImageFont.load_default(size=9))
        words = R.ocr_words(im)
        self.assertTrue(any("@" in w[0] for w in words), words)
        self.assertEqual(len(R.find_private(words, [], True, [])), 1)

    def test_check_refuses_an_empty_or_missing_package(self):
        with tempfile.TemporaryDirectory() as d:
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            with self.assertRaises(SystemExit):
                R.main(["check", str(Path(d) / "nope"), "--patterns", str(pats)])
            with self.assertRaises(SystemExit):                # a package with no images
                R.main(["check", d, "--patterns", str(pats)])

    def test_bad_patterns_or_rules_file_is_a_one_line_exit_2(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "pkg"
            pkg.mkdir()
            bad = Path(d) / "bad.json"
            bad.write_text("notjson")
            good = Path(d) / "p.json"
            good.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules = Path(d) / "r.json"
            rules.write_text("{}")
            cases = [
                (["check", str(pkg), "--patterns", str(Path(d) / "nope.json")], "nope.json"),
                (["check", str(pkg), "--patterns", str(bad)], "bad.json"),
                (["check", str(pkg), "--patterns", str(good), "--rules", str(bad)], "bad.json"),
                (["check", str(pkg), "--patterns", str(good), "--rules", str(Path(d) / "gone.json")], "gone.json"),
                (["apply", str(pkg), "--rules", str(bad)], "bad.json"),
                (["apply", str(pkg), "--rules", str(rules), "--patterns", str(bad)], "bad.json"),
            ]
            for argv, name in cases:
                err = io.StringIO()
                with contextlib.redirect_stderr(err), self.assertRaises(SystemExit) as cm:
                    R.main(argv)
                self.assertEqual(cm.exception.code, 2, argv)
                self.assertEqual(len(err.getvalue().strip().splitlines()), 1, err.getvalue())
                self.assertIn(name, err.getvalue())

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

    def test_check_loads_the_packages_own_rules_file(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "systems" / "demo"
            (pkg / "screenshots").mkdir(parents=True)
            Image.new("RGB", (4, 4)).save(pkg / "screenshots/a.png")
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules_dir = Path(d) / "redact-rules"
            rules_dir.mkdir()
            own = rules_dir / "demo.json"
            own.write_text(json.dumps({"ocr": {"email_allow": ["@own\\.test$"]}}))
            other = Path(d) / "other.json"
            other.write_text(json.dumps({"ocr": {"email_allow": ["@other\\.test$"]}}))

            def run(*extra, pkg_dir=pkg):
                seen = []
                def fake_hits(patterns, cfg, reads):
                    seen.append(cfg["email_allow"])
                    return [], False
                with mock.patch.object(R, "RULES_DIR", rules_dir), \
                     mock.patch.object(R, "ocr_words", return_value=[]), \
                     mock.patch.object(R, "ocr_hits", side_effect=fake_hits), \
                     contextlib.redirect_stdout(io.StringIO()) as out, \
                     self.assertRaises(SystemExit) as cm:
                    R.main(["check", str(pkg_dir), "--patterns", str(pats), *extra])
                self.assertEqual(cm.exception.code, 0)
                return seen[0], out.getvalue()

            allow, out = run()                                      # no --rules: the package's own file
            self.assertEqual(allow, [re.escape("@own.test")])     # read as its plain text, escaped
            self.assertEqual(out.count("rules: tools/redact-rules/demo.json"), 1)
            allow, out = run("--rules", str(other))                 # an explicit file wins
            self.assertEqual(allow, [re.escape("@other.test")])
            self.assertIn(f"rules: {other}", out)
            self.assertNotIn("demo.json", out)
            own.unlink()                                            # no file for the package: nothing loaded
            allow, out = run()
            self.assertEqual(allow, [])
            self.assertNotIn("rules:", out)

    def test_check_reads_every_image_in_every_folder_and_fails_on_unknown_types(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            for rel in ("screenshots/a.png", "icons/b.webp", "raw/c.gif", "icon.png", "raw/deep/d.jpg"):
                (pkg / rel).parent.mkdir(parents=True, exist_ok=True)
                Image.new("RGB", (4, 4)).save(pkg / rel)
            (pkg / "raw/notes.json").write_text("{}")
            pats = pkg / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            seen = []

            def fake_words(im, boost=False):
                seen.append(im.size)
                return []

            def run():
                seen.clear()
                with mock.patch.object(R, "ocr_words", side_effect=fake_words), \
                     contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as cm:
                    R.main(["check", d, "--patterns", str(pats)])
                return cm.exception.code, out.getvalue()

            code, out = run()
            self.assertEqual(code, 0, out)
            self.assertEqual(len(seen), 5)                        # png, webp, gif, root icon, nested jpg
            self.assertIn("5 images read", out)
            readable, unreadable = R.check_images(pkg)
            self.assertEqual(sorted(f.relative_to(pkg).as_posix() for f in readable),
                             ["icon.png", "icons/b.webp", "raw/c.gif", "raw/deep/d.jpg", "screenshots/a.png"])
            Image.new("RGB", (4, 4)).save(pkg / "icons/e.bmp")    # a type check cannot read
            (pkg / "raw/dump").write_bytes((pkg / "icon.png").read_bytes())   # an image with no extension
            (pkg / "raw/layers").write_bytes(b"8BPS\x00\x01" + bytes(20))     # a renamed Photoshop file
            code, out = run()
            self.assertEqual(code, 1)
            self.assertIn("UNREADABLE icons/e.bmp", out)
            self.assertIn("UNREADABLE raw/dump", out)
            self.assertIn("UNREADABLE raw/layers", out)
            self.assertNotIn("notes.json", out)

    def test_check_skips_git_ignored_images_with_non_ascii_names(self):
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            if subprocess.run(["git", "init", "-q", d], capture_output=True).returncode:
                self.skipTest("git is not available")
            (pkg / ".gitignore").write_text("fonts/\n")
            (pkg / "fonts").mkdir()
            Image.new("RGB", (4, 4)).save(pkg / "fonts/é.png")
            Image.new("RGB", (4, 4)).save(pkg / "fonts/é.bmp")
            Image.new("RGB", (4, 4)).save(pkg / "kept é.png")
            readable, unreadable = R.check_images(pkg)
            self.assertEqual([f.name for f in readable], ["kept é.png"])
            self.assertEqual(unreadable, [])

    def test_check_reads_every_frame_of_an_animation(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            frames = [Image.new("RGB", (8, 8), c) for c in ("red", "blue", "green")]
            frames[0].save(pkg / "anim.gif", save_all=True, append_images=frames[1:])
            pats = pkg / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            calls = []
            with mock.patch.object(R, "ocr_words", side_effect=lambda im, boost=False: calls.append(1) or []), \
                 contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
                R.main(["check", d, "--patterns", str(pats)])
            self.assertEqual(len(calls), 3)

    def test_check_ignores_a_rules_file_that_switches_detectors_off(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            Image.new("RGB", (4, 4)).save(pkg / "a.png")
            pats = pkg / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules = pkg / "r.json"
            rules.write_text(json.dumps({"ocr": {"emails": False, "net": False}}))
            words = [("someone@private.test", 0, 0, 100, 12, ("1", "1", "1"))]
            with mock.patch.object(R, "ocr_words", return_value=words), \
                 contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as cm:
                R.main(["check", d, "--patterns", str(pats), "--rules", str(rules)])
            self.assertEqual(cm.exception.code, 1)
            self.assertIn("sets ocr.emails to false; check ignores that", out.getvalue())
            self.assertIn("sets ocr.net to false", out.getvalue())
            words = [("Secret", 0, 0, 60, 12, ("1", "1", "1")), ("Plan", 70, 0, 40, 12, ("1", "1", "1"))]
            pats.write_text(json.dumps({"replace": [["secret plan", "i", "x"]]}))
            rules.write_text(json.dumps({"ocr": {"net": False}}))
            with mock.patch.object(R, "ocr_words", return_value=words), \
                 contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as cm:
                R.main(["check", d, "--patterns", str(pats), "--rules", str(rules)])
            self.assertEqual(cm.exception.code, 1)                 # a pattern match, no email: still caught
            self.assertIn("HIT a.png", out.getvalue())

    def test_apply_never_deletes_outside_the_package(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "pkg"
            (pkg / "screenshots").mkdir(parents=True)
            Image.new("RGB", (4, 4)).save(pkg / "screenshots/a.png")
            keep = Path(d) / "outside.png"
            Image.new("RGB", (4, 4)).save(keep)
            rules = Path(d) / "r.json"
            rules.write_text(json.dumps({"delete": ["screenshots/a.png", "../outside.png"], "ocr": {"net": False}}))
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as cm:
                R.main(["apply", str(pkg), "--rules", str(rules)])
            self.assertIn("outside the package", str(cm.exception.code))
            self.assertTrue(keep.exists())
            self.assertTrue((pkg / "screenshots/a.png").exists())     # nothing deleted at all
            rules.write_text(json.dumps({"delete": ["../outside-link.png"], "ocr": {"net": False}}))
            (Path(d) / "outside-link.png").symlink_to(pkg / "screenshots/a.png")   # outside, pointing in
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as cm:
                R.main(["apply", str(pkg), "--rules", str(rules)])
            self.assertIn("outside the package", str(cm.exception.code))
            self.assertTrue((Path(d) / "outside-link.png").is_symlink())

    def test_apply_still_requires_rules(self):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                R.main(["apply", d])
            self.assertEqual(cm.exception.code, 2)

    def test_unknown_option_is_rejected_not_treated_as_a_file(self):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stderr(io.StringIO()):
            pkg = Path(d) / "pkg"
            pkg.mkdir()
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            with self.assertRaises(SystemExit) as cm:
                R.main(["check", str(pkg), "--patterns", str(pats), "--ruels", str(pats)])
            self.assertEqual(cm.exception.code, 2)
            with self.assertRaises(SystemExit) as cm:
                R.main(["lines", "--potterns", str(pats)])
            self.assertEqual(cm.exception.code, 2)

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

    def test_allow_entries_match_whole_parts_of_an_address(self):
        cases = [
            (r"@example\.com?\b", "x@example.com", True),
            (r"@example\.com?\b", "x@example.co", True),
            (r"@example\.com?\b", "x@example.co.evil.test", False),
            (r"@example\.com?\b", "x@example.com.evil.test", False),
            (r"@example\.com$", "x@example.com.", True),          # a sentence's full stop
            (r"@example\.com$", "x@sub.example.com", False),
            (r"\.example$", "x@acme.example", True),
            (r"\.example$", "x@acme.example.evil", False),
            (r"^owner@mine\.test$", "owner@mine.test", True),
            (r"^owner@mine\.test$", "other@mine.test", False),
            (r"^owner@", "owner@anywhere.test", True),
            (r"^owner@", "owner2@anywhere.test", False),
            (r"^ownerlong", "ownerlong@x.test", True),
            (r"^ownerlo", "ownerlong@x.test", True),              # ^: the start of the local part
            (r"^ownerlo", "x@ownerlong.test", False),
            (r"owner", "owner@x.test", True),                     # the whole local part
            (r"owner", "a.owner@x.test", False),
            (r"example", "x@example.com", False),                 # a piece of the domain
            (r"wagmi@[0-9][0-9.x]*", "wagmi@2.15.2", True),       # an npm version string
            (r"wagmi@[0-9][0-9.x]*", "wagmi.user@private.test", False),
            (r"viem@[0-9][0-9.x]*", "viem.user@private.test", False),
        ]
        for allow, addr, ok in cases:
            self.assertEqual(R.email_allowed(addr, [allow]), ok, (allow, addr))
        self.assertEqual(len(R.find_private(self.words("x@example.co.evil.test"), [], True, [r"@example\.com?\b"])), 1)

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


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class RulesText(unittest.TestCase):
    """A rules file is committed: its notes may say what a family hides, never hold the value."""

    def test_leaks_are_named_by_path_and_kind_never_by_value(self):
        rules = {"_note": "the popup shows jane.roe@acme-widgets.biz and +1 555 010 0199",
                 "families": [{"name": "call 555-010-0199", "files": ["a.png"], "rects": [[0, 0, 10, 10]]}],
                 "ocr": {"email_allow": ["^nobody@acme-widgets\\.biz$"]}}
        leaks = R.rules_text_leaks(rules)
        self.assertEqual(leaks, ["_note: an email address its email_allow does not pass",
                                 "_note: a phone-number-shaped string",
                                 "families[0].name: a phone-number-shaped string"])
        self.assertFalse(any("555" in x or "jane" in x for x in leaks))

    def test_escaped_addresses_and_crowded_numbers_are_still_found(self):
        self.assertEqual(R.rules_text_leaks({"ocr": {"keep": ["^person@private-corp\\.biz$"]}}),
                         ["ocr.keep[0]: an email address its email_allow does not pass"])
        for text in ["555-010-0199 555-010-0200", "555-010-0199 (2026-10-23)", "call (555) 010-0199 today",
                     "+44 20 7946 0958", "1 555 010 0199 and 1 555 010 0200 and 1 555 010 0201"]:
            with self.subTest(text=text):
                self.assertEqual(R.rules_text_leaks({"_note": text}), ["_note: a phone-number-shaped string"])
        for text in ["2026-10-23 2026-10-24", "rects [[800, 25385, 1115, 25520]]", "1440 x 900 at 2x",
                     "version 1.2.3", "id 1234567890"]:
            with self.subTest(text=text):
                self.assertEqual(R.rules_text_leaks({"_note": text}), [])

    def test_allowed_reserved_and_non_phone_values_pass(self):
        rules = {"_note": "placeholders name@example.com, a@b.test, support@vendor-x.biz; captured 2026-10-23; "
                          "size [2880, 1800]; version 1.2.3.4",
                 "families": [{"rects": [[800, 25385, 1115, 25520]], "size": [[2880, 1800]]}],
                 "ocr": {"email_allow": ["^support@vendor-x\\.biz$", "nobody@listed-only-here\\.biz"],
                         "keep": ["^support@vendor-x\\.biz$"]}}
        self.assertEqual(R.rules_text_leaks(rules), [])     # email_allow itself is never read as text

    def test_check_fails_on_a_rules_file_holding_a_value(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            Image.new("RGB", (4, 4)).save(pkg / "a.png")
            pats = pkg / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules = pkg / "r.json"
            rules.write_text(json.dumps({"_note": "painted out jane.roe@acme-widgets.biz"}))
            with mock.patch.object(R, "ocr_words", return_value=[]), \
                 contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as cm:
                R.main(["check", d, "--patterns", str(pats), "--rules", str(rules)])
            self.assertEqual(cm.exception.code, 1)
            self.assertIn("LEAK r.json _note: an email address", out.getvalue())
            self.assertNotIn("jane.roe", out.getvalue())
            rules.write_text(json.dumps({"_note": "painted out a demo user's email address"}))
            with mock.patch.object(R, "ocr_words", return_value=[]), \
                 contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as cm:
                R.main(["check", d, "--patterns", str(pats), "--rules", str(rules)])
            self.assertEqual(cm.exception.code, 0)

    def test_every_committed_rules_file_is_free_of_values(self):
        for f in sorted(R.RULES_DIR.glob("*.json")):
            with self.subTest(rules=f.name):
                self.assertEqual(R.rules_text_leaks(json.loads(f.read_text())), [])


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class AllowEntries(unittest.TestCase):
    """A package rules file's email_allow is exact addresses or one @domain each, never a pattern."""

    def test_patterns_and_free_mail_domains_are_refused(self):
        cases = {
            "the three bypasses review found": [r"^(assistant)@[\w.-]+$", r"^[a-z]+@gmail\.com$",
                                                r"^(?=vip)[a-z]+@gmail\.com$"],
            "alternation": [r"@example\.(com|org)$", r"^(jane|john)@vendor\.biz$", "a@x\\.biz|.*"],
            "character classes": [r"^sup[a-z]*@vendor\.biz$", r"^satoshi[0-9]@gmail\.com$", r"@\w+\.com$"],
            "quantifiers": [r"^satoshi2?@gmail\.com$", ".*", "@.+", r"^a{2}@vendor\.biz$", r"^as+istant@vendor\.biz$"],
            "groups": [r"^(?:a)@vendor\.biz$", r"^(a)@vendor\.biz$"],
            "backreferences": [r"^(a)\1@vendor\.biz$"],
            "lookarounds": [r"^[a-z]+(?<=vip)@gmail\.com$", r"^(?!x)a@vendor\.biz$"],
            "inline flags": [r"(?i)a@vendor\.biz", r"(?x) a @vendor\.biz"],
            "an unescaped dot": ["name@example.com", r"@vendor.biz$"],
            "an empty or non-text entry": ["", 7, None],
            "no domain": ["name@", "you@", r"^assistant@", "owner", r"\.example$", r"example\.com$"],
            "a free-mail domain": [r"@gmail\.com$", r"@mail\.com$", r"@yahoo\.co\.jp$", r"@agentmail\.to\b",
                                   r"@email\.com$", r"@mail\.gmail\.com", r"@GMAIL\.COM$"],
            "non-ASCII spellings": ["@gma\u0131l\\.com$", "@gma\u0130l\\.com$", "@\uff47mail\\.com$",
                                    "j\u00f6rg@vendor\\.biz", "@vend\u043er\\.biz"],
        }
        for kind, entries in cases.items():
            for entry in entries:
                with self.subTest(kind=kind, entry=entry):
                    self.assertIsNotNone(R.allow_entry_problem(entry))

    def test_exact_addresses_and_vendor_domains_pass(self):
        for entry, text in [(r"^support@vendor\.biz$", "support@vendor.biz"), (r"@vendor\.biz$", "@vendor.biz"),
                            (r"@example\.inc", "@example.inc"), (r"satoshi@gmail\.com$", "satoshi@gmail.com"),
                            (r"^ALICE@gmail\.com$", "ALICE@gmail.com"), (r"john\.doe\+1@gmail\.com\b", "john.doe+1@gmail.com"),
                            (r"^kaichen@agentm$", "kaichen@agentm"), (r"@my-shop\.biz", "@my-shop.biz")]:
            with self.subTest(entry=entry):
                self.assertEqual(R.allow_entry_text(entry), (text, None))

    def test_an_address_matches_exactly_and_a_domain_matches_the_whole_domain(self):
        allow = R.package_allow("r.json", [r"^ALICE@gmail\.com$", r"@vendor\.biz$"])
        for addr, ok in [("alice@gmail.com", True), ("Alice@Gmail.com.", True), ("alice2@gmail.com", False),
                         ("bob@gmail.com", False), ("xalice@gmail.com", False), ("a@vendor.biz", True),
                         ("A@VENDOR.BIZ", True), ("a@sub.vendor.biz", False), ("a@vendor.biz.evil.test", False),
                         ("vendor.biz@evil.test", False)]:
            with self.subTest(addr=addr):
                self.assertEqual(R.email_allowed(addr, allow), ok)

    def test_a_dotless_i_domain_would_have_passed_gmail(self):
        entry = "@gma\u0131l\\.com$"                                  # what review found
        self.assertTrue(R.email_allowed("stranger@gmail.com", [entry]))     # the matcher folds it to gmail
        self.assertIsNotNone(R.allow_entry_problem(entry))                  # so validation refuses it

    def test_the_reserved_example_tld_needs_no_entry(self):
        w = lambda a: [(a, 0, 0, 10, 10, ("1", "1", "1"))]
        self.assertEqual(R.find_private(w("learner@acme.example"), [], True, []), [])
        self.assertEqual(len(R.find_private(w("x@acme.example.evil.test"), [], True, [])), 1)

    def test_check_and_apply_refuse_a_rules_file_with_a_pattern(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "pkg"
            pkg.mkdir()
            Image.new("RGB", (4, 4)).save(pkg / "a.png")
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]], "email_allow": ["^owner@"]}))
            rules = Path(d) / "r.json"
            rules.write_text(json.dumps({"ocr": {"email_allow": [r"@vendor\.biz$", ".*"]}}))
            for argv in (["check", str(pkg), "--patterns", str(pats), "--rules", str(rules)],
                         ["apply", str(pkg), "--rules", str(rules), "--patterns", str(pats)]):
                err = io.StringIO()
                with mock.patch.object(R, "ocr_words", return_value=[]), contextlib.redirect_stderr(err), \
                     contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as cm:
                    R.main(argv)
                self.assertEqual(cm.exception.code, 2, argv)
                self.assertIn('".*" is a regex pattern', err.getvalue())
                self.assertNotIn("vendor", err.getvalue())                 # only the refused entry is named
            # the private patterns file is the owner's: its pattern entry is not refused
            rules.write_text(json.dumps({"ocr": {"email_allow": [r"@vendor\.biz$"]}}))
            with mock.patch.object(R, "ocr_words", return_value=[]), contextlib.redirect_stdout(io.StringIO()), \
                 self.assertRaises(SystemExit) as cm:
                R.main(["check", str(pkg), "--patterns", str(pats), "--rules", str(rules)])
            self.assertEqual(cm.exception.code, 0)

    def test_every_committed_rules_file_lists_exact_entries(self):
        for f in sorted(R.RULES_DIR.glob("*.json")):
            allow = json.loads(f.read_text()).get("ocr", {}).get("email_allow", [])
            for entry in allow:
                with self.subTest(rules=f.name, entry=entry):
                    self.assertIsNone(R.allow_entry_problem(entry))


@unittest.skipIf(R is None, "Pillow and numpy are not installed")
class RulesKeys(unittest.TestCase):
    """A rules file key at a level that never reads it, or an unknown key, is refused, not ignored."""

    def test_misplaced_and_unknown_keys_are_named(self):
        rules = {"_note": "a note", "wrap_ignore": ["screenshots/a.png"], "colour": "red",
                 "ocr": {"_why": "a note", "families": [], "email_allow": []},
                 "families": [{"name": "rows", "files": ["*.png"], "rect": [0, 0, 1, 1],
                               "ocr_lines": [{"rect": [0, 0, 1, 1], "keep": [], "files": []}]}]}
        self.assertEqual(R.rules_key_problems(rules), [
            "wrap_ignore belongs in ocr",
            "colour is not a rules-file key",
            "ocr.families belongs in the top level",
            "families[0].rect belongs in an ocr_lines entry",
            "families[0].ocr_lines[0].files belongs in a family",
        ])

    def test_wrong_shapes_are_named(self):
        self.assertEqual(R.rules_key_problems({"ocr": [], "families": [7]}),
                         ["ocr must be a JSON object", "families[0] must be a JSON object"])
        self.assertEqual(R.rules_key_problems({"families": {}}), ["families must be a list"])
        # a bad entry before a good one does not shift the good one's index in the message
        self.assertEqual(R.rules_key_problems({"families": [7, {"ocr_lines": [{"bogus": 1}]}]}),
                         ["families[0] must be a JSON object", "families[1].ocr_lines[0].bogus is not a rules-file key"])

    def test_documented_keys_pass(self):
        rules = {"families": [{"name": "n", "files": ["*"], "skip": [], "size": [[1, 1]], "rects": [],
                               "ocr_lines": [{"rect": [0, 0, 1, 1], "keep": ["^x$"]}]}],
                 "delete_stems": [], "delete": [], "excludeSources": [], "captureLimitations": {},
                 "ocr": {"net": True, "emails": True, "email_allow": [], "keep": [], "boost": [],
                         "delete_if_covered": 0.3, "wrap_ignore": []}}
        self.assertEqual(R.rules_key_problems(rules), [])

    def test_check_and_apply_refuse_a_misplaced_key(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "pkg"
            pkg.mkdir()
            Image.new("RGB", (4, 4)).save(pkg / "a.png")
            pats = Path(d) / "p.json"
            pats.write_text(json.dumps({"replace": [["x", "y"]]}))
            rules = Path(d) / "r.json"
            rules.write_text(json.dumps({"ocr": {"emails": True}, "wrap_ignore": ["a.png"]}))
            for argv in (["check", str(pkg), "--patterns", str(pats), "--rules", str(rules)],
                         ["apply", str(pkg), "--rules", str(rules), "--patterns", str(pats), "--dry-run"]):
                err = io.StringIO()
                with mock.patch.object(R, "ocr_words", return_value=[]), contextlib.redirect_stderr(err), \
                     contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as cm:
                    R.main(argv)
                self.assertEqual(cm.exception.code, 2, argv)
                self.assertEqual(len(err.getvalue().strip().splitlines()), 1, err.getvalue())
                self.assertIn("r.json", err.getvalue())
                self.assertIn("wrap_ignore belongs in ocr", err.getvalue())

    def test_every_committed_rules_file_puts_each_key_where_it_is_read(self):
        files = sorted(R.RULES_DIR.glob("*.json"))
        self.assertTrue(files)
        for f in files:
            with self.subTest(rules=f.name):
                self.assertEqual(R.rules_key_problems(json.loads(f.read_text())), [])


if __name__ == "__main__":
    unittest.main()
