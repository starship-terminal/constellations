"""Tests for tools/refero/mirror_media.py beyond download() itself: the db
guard, the per-file job, ffmpeg compression, the untrusted-row guards (slug and
URL scheme), and the command line (--check,
--only, --limit, --force, --compress-videos). The download opener and
subprocess.run are mocked; the db and the media root are temporary, so
nothing reaches the network or ~/services. Run with `make test`."""
import io
import sqlite3
import sys
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import mirror_media  # noqa: E402

COLUMNS = ("slug", "screenshot_url", "video_poster_url", "video_url",
           "video_detail_url", "video_detail_poster_url", "source_url")
FULL = ("acme", "https://cdn/s.jpg", "https://cdn/p.jpg", "https://cdn/v.mp4",
        "https://cdn/d.mp4", "https://cdn/dp.jpg", "https://acme.example")
SHOT_ONLY = ("beta", "https://cdn/b.jpg", None, None, None, None, None)
BY_URL = {"https://cdn/s.jpg": ("image/jpeg", b"shot"),
          "https://cdn/p.jpg": ("image/jpeg", b"poster"),
          "https://cdn/v.mp4": ("video/mp4", b"video-bytes"),
          "https://cdn/d.mp4": ("video/mp4", b"detail-bytes"),
          "https://cdn/dp.jpg": ("image/jpeg", b"dposter"),
          "https://cdn/b.jpg": ("image/jpeg", b"beta-shot")}


class Resp:
    def __init__(self, data=b"x", content_type="image/jpeg"):
        self.data = data
        self.headers = {"Content-Type": content_type}

    def read(self):
        return self.data

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def serve(request, timeout=None):
    """urlopen stand-in: answers from BY_URL, 404s everything else."""
    url = request.full_url
    if url.startswith(mirror_media.FAVICON_API):
        return Resp(b"icon", "image/png")
    if url not in BY_URL:
        raise urllib.error.URLError(f"404 {url}")
    content_type, data = BY_URL[url]
    return Resp(data, content_type)


class MirrorTmp(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.db_path = self.tmp / "refero.db"
        self.media = self.tmp / "media"
        for patcher in (mock.patch.object(mirror_media, "DB", self.db_path),
                        mock.patch.object(mirror_media.time, "sleep")):
            patcher.start()
            self.addCleanup(patcher.stop)

    def make_db(self, *rows):
        db = sqlite3.connect(self.db_path)
        db.execute(f"CREATE TABLE styles ({', '.join(COLUMNS)})")
        db.executemany(f"INSERT INTO styles VALUES ({','.join('?' * len(COLUMNS))})", rows)
        db.commit()
        db.close()

    def main(self, *argv, which=None):
        argv = ["mirror_media.py", "--media-root", str(self.media), "--workers", "1", *argv]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(mirror_media.shutil, "which", return_value=which), \
             mock.patch("sys.stdout", new_callable=io.StringIO) as out, \
             mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            try:
                mirror_media.main()
                code = None
            except SystemExit as ex:
                code = ex.code
        return code, out.getvalue(), err.getvalue()


class OpenDbTest(MirrorTmp):
    def test_a_missing_db_exits_with_the_fix(self):
        with self.assertRaises(SystemExit) as raised:
            mirror_media.open_db()
        self.assertIn("run tools/refero/fetch.py first", str(raised.exception))
        self.assertFalse(self.db_path.exists())  # never created as a 0-byte file

    def test_an_lfs_pointer_exits_with_the_fix(self):
        self.db_path.write_text("version https://git-lfs.github.com/spec/v1\noid sha256:0\n")
        with self.assertRaises(SystemExit) as raised:
            mirror_media.open_db()
        self.assertIn("git lfs pull", str(raised.exception))

    def test_the_db_opens_read_only(self):
        self.make_db(FULL)
        db = mirror_media.open_db()
        try:
            self.assertEqual(db.execute("SELECT slug FROM styles").fetchall(), [("acme",)])
            with self.assertRaises(sqlite3.OperationalError):
                db.execute("DELETE FROM styles")
        finally:
            db.close()


class DoJobTest(MirrorTmp):
    def test_a_download_job_reports_downloaded(self):
        dest = self.tmp / "shots" / "acme.jpg"
        dest.parent.mkdir()
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve):
            result = mirror_media.do_job(("shots", "acme", "https://cdn/s.jpg", dest, False), None)
        self.assertEqual(result, ("shots", "downloaded", False, None))
        self.assertEqual(dest.read_bytes(), b"shot")

    def test_a_failed_download_reports_the_slug_and_the_error(self):
        dest = self.tmp / "shots" / "acme.jpg"
        dest.parent.mkdir()
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve):
            kind, status, compressed, err = mirror_media.do_job(
                ("shots", "acme", "https://cdn/missing.jpg", dest, False), None)
        self.assertEqual((kind, status, compressed), ("shots", "failed", False))
        self.assertTrue(err.startswith("acme: "))
        self.assertFalse(dest.exists())

    def test_a_compress_only_job_skips_the_download(self):
        dest = self.tmp / "videos" / "acme.mp4"
        dest.parent.mkdir()
        dest.write_bytes(b"x" * 100)
        with mock.patch.object(mirror_media, "compress_video", return_value=True) as shrink, \
             mock.patch.object(mirror_media.OPENER, "open") as opened:
            result = mirror_media.do_job(("videos", "acme", None, dest, True), "/bin/ffmpeg")
        self.assertEqual(result, ("videos", "skipped", True, None))
        shrink.assert_called_once_with(dest, "/bin/ffmpeg")
        opened.assert_not_called()

    def test_images_are_never_compressed(self):
        dest = self.tmp / "shots" / "acme.jpg"
        dest.parent.mkdir()
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve), \
             mock.patch.object(mirror_media, "compress_video") as shrink:
            mirror_media.do_job(("shots", "acme", "https://cdn/s.jpg", dest, True), "/bin/ffmpeg")
        shrink.assert_not_called()

    def test_an_ffmpeg_failure_is_reported_but_keeps_the_download(self):
        dest = self.tmp / "videos" / "acme.mp4"
        dest.parent.mkdir()
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve), \
             mock.patch.object(mirror_media, "compress_video",
                               side_effect=RuntimeError("bad codec")):
            result = mirror_media.do_job(("videos", "acme", "https://cdn/v.mp4", dest, True),
                                         "/bin/ffmpeg")
        self.assertEqual(result, ("videos", "downloaded", False, "acme: compress: bad codec"))
        self.assertEqual(dest.read_bytes(), b"video-bytes")


class CompressVideoTest(MirrorTmp):
    def setUp(self):
        super().setUp()
        self.path = self.tmp / "acme.mp4"
        self.path.write_bytes(b"x" * 1000)

    def ffmpeg(self, out_size, returncode=0, stderr=b""):
        def run(cmd, **kw):
            self.cmd = cmd
            if out_size is not None:
                Path(cmd[-1]).write_bytes(b"y" * out_size)
            return SimpleNamespace(returncode=returncode, stderr=stderr)
        return mock.patch.object(mirror_media.subprocess, "run", side_effect=run)

    def leftovers(self):
        return sorted(p.name for p in self.tmp.glob("*.compress*"))

    def test_a_smaller_encode_replaces_the_original(self):
        with self.ffmpeg(400):
            self.assertTrue(mirror_media.compress_video(self.path, "/bin/ffmpeg"))
        self.assertEqual(self.path.stat().st_size, 400)
        self.assertEqual(self.cmd[:2], ["/bin/ffmpeg", "-y"])
        self.assertIn("-an", self.cmd)
        self.assertEqual(self.leftovers(), [])

    def test_a_larger_encode_is_discarded(self):
        with self.ffmpeg(2000):
            self.assertFalse(mirror_media.compress_video(self.path, "/bin/ffmpeg"))
        self.assertEqual(self.path.stat().st_size, 1000)
        self.assertEqual(self.leftovers(), [])

    def test_a_failing_ffmpeg_raises_with_its_last_stderr_line(self):
        with self.ffmpeg(None, returncode=1, stderr=b"first\nInvalid data found\n"), \
                self.assertRaises(RuntimeError) as raised:
            mirror_media.compress_video(self.path, "/bin/ffmpeg")
        self.assertEqual(str(raised.exception), "Invalid data found")
        self.assertEqual(self.path.read_bytes(), b"x" * 1000)

    def test_a_silent_failure_names_the_exit_code(self):
        with self.ffmpeg(None, returncode=7), self.assertRaises(RuntimeError) as raised:
            mirror_media.compress_video(self.path, "/bin/ffmpeg")
        self.assertIn("ffmpeg exit 7", str(raised.exception))

    def test_an_empty_output_counts_as_a_failure(self):
        with self.ffmpeg(0), self.assertRaises(RuntimeError):
            mirror_media.compress_video(self.path, "/bin/ffmpeg")
        self.assertEqual(self.leftovers(), [])


class MainCheckTest(MirrorTmp):
    def test_check_passes_when_every_expected_file_exists(self):
        self.make_db(SHOT_ONLY)
        (self.media / "shots").mkdir(parents=True)
        (self.media / "shots" / "beta.jpg").write_bytes(b"x")
        code, out, _ = self.main("--check")
        self.assertIsNone(code)
        self.assertIn("media root ok", out)

    def test_check_lists_what_is_missing_and_exits_nonzero(self):
        self.make_db(FULL, SHOT_ONLY)
        code, _, err = self.main("--check")
        self.assertIn("7 expected files missing", code)
        self.assertIn("shots: 2 missing (e.g. acme, beta)", err)
        self.assertIn("favicons: 1 missing", err)
        self.assertFalse(self.media.exists())  # --check downloads nothing

    def test_check_honours_only(self):
        self.make_db(FULL)
        code, _, err = self.main("--check", "--only", "videos")
        self.assertIn("1 expected files missing", code)
        self.assertNotIn("shots", err)

    def test_an_unknown_only_kind_is_a_usage_error(self):
        self.make_db(FULL)
        code, _, err = self.main("--only", "shots,gifs")
        self.assertEqual(code, 2)
        self.assertIn("unknown --only kinds: gifs", err)

    def test_a_db_without_the_table_exits_with_the_fix(self):
        sqlite3.connect(self.db_path).close()
        code, _, _ = self.main()
        self.assertIn("run tools/refero/fetch.py first", code)


class MainDownloadTest(MirrorTmp):
    def run_main(self, *argv, **kw):
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve) as opened:
            result = self.main(*argv, **kw)
        return result, opened

    def test_every_kind_is_mirrored_into_its_folder(self):
        self.make_db(FULL)
        (code, out, err), opened = self.run_main()
        self.assertIsNone(code)
        self.assertEqual(err, "")
        self.assertEqual(opened.call_count, 6)
        self.assertEqual((self.media / "shots" / "acme.jpg").read_bytes(), b"shot")
        self.assertEqual((self.media / "videos" / "acme.mp4").read_bytes(), b"video-bytes")
        self.assertEqual((self.media / "detail" / "acme.mp4").read_bytes(), b"detail-bytes")
        self.assertEqual((self.media / "posters" / "acme.jpg").read_bytes(), b"poster")
        self.assertEqual((self.media / "detail-posters" / "acme.jpg").read_bytes(), b"dposter")
        self.assertEqual((self.media / "favicons" / "acme.png").read_bytes(), b"icon")
        self.assertIn("6 files to fetch or compress", out)
        self.assertRegex(out, r"shots\s+1\s+0\s+0\s+0")
        self.assertEqual(sorted(p.name for p in self.media.rglob("*.partial")), [])

    def test_a_rerun_skips_files_that_exist_and_counts_missing_urls(self):
        self.make_db(FULL, SHOT_ONLY)
        self.run_main()
        (code, out, _), opened = self.run_main()
        self.assertIsNone(code)
        opened.assert_not_called()
        self.assertIn("0 files to fetch or compress", out)
        self.assertRegex(out, r"shots\s+0\s+2\s+0\s+0")
        self.assertRegex(out, r"videos\s+0\s+1\s+1\s+0")  # beta has no video url

    def test_force_downloads_again(self):
        self.make_db(SHOT_ONLY)
        self.run_main("--only", "shots")
        (self.media / "shots" / "beta.jpg").write_bytes(b"stale")
        (_, out, _), opened = self.run_main("--only", "shots", "--force")
        self.assertEqual(opened.call_count, 1)
        self.assertEqual((self.media / "shots" / "beta.jpg").read_bytes(), b"beta-shot")

    def test_an_empty_file_counts_as_absent(self):
        self.make_db(SHOT_ONLY)
        (self.media / "shots").mkdir(parents=True)
        (self.media / "shots" / "beta.jpg").write_bytes(b"")
        _, opened = self.run_main("--only", "shots")
        self.assertEqual(opened.call_count, 1)

    def test_only_and_limit_narrow_the_run(self):
        self.make_db(FULL, SHOT_ONLY)
        (_, out, _), opened = self.run_main("--only", "shots", "--limit", "1")
        self.assertEqual(opened.call_count, 1)
        self.assertTrue((self.media / "shots" / "acme.jpg").exists())
        self.assertFalse((self.media / "shots" / "beta.jpg").exists())
        self.assertNotIn("videos", out)

    def test_a_failed_download_is_reported_and_the_run_finishes(self):
        row = ("gamma", "https://cdn/gone.jpg", None, None, None, None, None)
        self.make_db(row, SHOT_ONLY)
        (code, out, err), _ = self.run_main("--only", "shots")
        self.assertIsNone(code)
        self.assertIn("FAIL gamma:", err)
        self.assertRegex(out, r"shots\s+1\s+0\s+0\s+1")
        self.assertFalse((self.media / "shots" / "gamma.jpg").exists())
        self.assertTrue((self.media / "shots" / "beta.jpg").exists())

    def test_the_default_media_root_comes_from_refero_media(self):
        self.make_db(SHOT_ONLY)
        argv = ["mirror_media.py", "--workers", "1", "--only", "shots"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(mirror_media.refero_media, "default_media_root",
                               return_value=self.media), \
             mock.patch.object(mirror_media.OPENER, "open", side_effect=serve), \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            mirror_media.main()
        self.assertTrue((self.media / "shots" / "beta.jpg").exists())


class MainCompressTest(MirrorTmp):
    def test_a_missing_ffmpeg_warns_and_mirrors_raw(self):
        self.make_db(FULL)
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve), \
             mock.patch.object(mirror_media.Path, "home", return_value=self.tmp):
            code, _, err = self.main("--only", "videos", "--compress-videos", which=None)
        self.assertIsNone(code)
        self.assertIn("warning: ffmpeg not found", err)
        self.assertEqual((self.media / "videos" / "acme.mp4").read_bytes(), b"video-bytes")

    def test_existing_videos_are_re_encoded_without_a_download(self):
        self.make_db(FULL)
        (self.media / "videos").mkdir(parents=True)
        (self.media / "videos" / "acme.mp4").write_bytes(b"x" * 100)
        with mock.patch.object(mirror_media.OPENER, "open") as opened, \
             mock.patch.object(mirror_media, "compress_video", return_value=True) as shrink:
            code, out, _ = self.main("--only", "videos", "--compress-videos",
                                     which="/bin/ffmpeg")
        self.assertIsNone(code)
        opened.assert_not_called()
        shrink.assert_called_once()
        self.assertRegex(out, r"videos\s+0\s+1\s+0\s+0\s+1")  # skipped, compressed

    def test_new_videos_are_downloaded_then_compressed(self):
        self.make_db(FULL)
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=serve), \
             mock.patch.object(mirror_media, "compress_video", return_value=False) as shrink:
            code, out, _ = self.main("--only", "videos,posters", "--compress-videos",
                                     which="/bin/ffmpeg")
        self.assertIsNone(code)
        self.assertEqual(shrink.call_count, 1)  # the poster is an image
        self.assertIn("compressed", out)


class UntrustedRowTest(MirrorTmp):
    """A styles row arrives through the committed text dump, so its slug and
    URLs are untrusted: neither may reach a local file or leave the root."""

    def test_media_dest_refuses_a_path_like_slug(self):
        for bad in ("../x", "../../etc/x", "a/b", "Acme", "", "-a", "a--b", None):
            with self.assertRaises(ValueError, msg=repr(bad)):
                mirror_media.media_dest(self.media, "shots", bad)
        self.assertEqual(mirror_media.media_dest(self.media, "shots", "acme-2"),
                         self.media / "shots" / "acme-2.jpg")

    def test_download_refuses_a_non_https_url_without_opening_it(self):
        secret = self.tmp / "secret.jpg"
        secret.write_bytes(b"local file")
        dest = self.tmp / "shots" / "acme.jpg"
        dest.parent.mkdir()
        for url in (secret.as_uri(), "http://cdn/s.jpg", "ftp://cdn/s.jpg"):
            with mock.patch.object(mirror_media.OPENER, "open") as opened, \
                    self.assertRaises(ValueError, msg=url):
                mirror_media.download("shots", url, dest)
            opened.assert_not_called()
        self.assertFalse(dest.exists())

    def test_a_redirect_away_from_https_is_refused(self):
        handler = mirror_media.HttpsOnlyRedirect()
        req = urllib.request.Request("https://cdn/s.jpg")
        for target in ("http://cdn/s.jpg", "file:///etc/hosts"):
            with self.assertRaises(mirror_media.NotHttps, msg=target):
                handler.redirect_request(req, None, 302, "Found", {}, target)
        followed = handler.redirect_request(req, None, 302, "Found", {}, "https://cdn2/s.jpg")
        self.assertEqual(followed.full_url, "https://cdn2/s.jpg")
        self.assertTrue(any(isinstance(h, mirror_media.HttpsOnlyRedirect)
                            for h in mirror_media.OPENER.handlers))

    def test_a_refused_redirect_is_not_retried_and_writes_nothing(self):
        dest = self.tmp / "shots" / "acme.jpg"
        dest.parent.mkdir()
        refused = mirror_media.NotHttps("refusing a non-https redirect to 'http://cdn/s.jpg'")
        with mock.patch.object(mirror_media.OPENER, "open", side_effect=refused) as opened, \
                self.assertRaises(mirror_media.NotHttps):
            mirror_media.download("shots", "https://cdn/s.jpg", dest)
        self.assertEqual(opened.call_count, 1)
        self.assertFalse(dest.exists())

    def test_a_file_url_in_the_db_is_never_copied_into_the_mirror(self):
        secret = self.tmp / "secret.jpg"
        secret.write_bytes(b"local file")
        self.make_db(("gamma", secret.as_uri(), None, None, None, None, None))
        code, _, err = self.main("--only", "shots")  # real opener: it must not run
        self.assertIsNone(code)
        self.assertIn("FAIL gamma: refusing a non-https url", err)
        self.assertFalse((self.media / "shots" / "gamma.jpg").exists())

    def test_a_path_like_slug_is_skipped_and_nothing_lands_outside_the_root(self):
        self.make_db(("../../escape", "https://cdn/s.jpg", None, None, None, None, None),
                     SHOT_ONLY)
        with mock.patch.object(mirror_media.OPENER, "open",
                               side_effect=serve) as opened:
            code, _, err = self.main("--only", "shots")
        self.assertIsNone(code)
        self.assertIn("FAIL '../../escape': unsafe slug, skipped", err)
        self.assertEqual(opened.call_count, 1)  # beta only
        self.assertTrue((self.media / "shots" / "beta.jpg").exists())
        self.assertEqual(sorted(p.name for p in self.tmp.rglob("escape*")), [])

    def test_check_fails_on_an_unsafe_slug(self):
        self.make_db(("a/b", "https://cdn/s.jpg", None, None, None, None, None))
        code, _, err = self.main("--check", "--only", "shots")
        self.assertIn("1 styles rows have an unsafe slug", code)
        self.assertIn("FAIL 'a/b'", err)


if __name__ == "__main__":
    unittest.main()
