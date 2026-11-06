"""Tests for tools/fetch_icon.py. Run with `make test`. No network: fetch is patched."""
import contextlib
import http.client
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("fetch_icon", HERE / "fetch_icon.py")
fetch_icon = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fetch_icon)


class DeclaredSizeTest(unittest.TestCase):
    def test_reads_the_width_of_each_size(self):
        self.assertEqual(fetch_icon.declared_size("192x192"), 192)
        self.assertEqual(fetch_icon.declared_size("16x16 32X32"), 32)

    def test_any_or_junk_is_zero(self):
        for sizes in ("", "any", "192", "x192", "bigxbig", "\u00b2x\u00b2"):
            self.assertEqual(fetch_icon.declared_size(sizes), 0, sizes)


class CandidatesTest(unittest.TestCase):
    PAGE = (b'<html><head><link rel="icon" href="/small.png" sizes="16x16">'
            b'<link rel="icon" href="/big.png" sizes="192x192">'
            b'<link rel="icon" href="/mid.png" sizes="48x48"></head></html>')

    def test_largest_declared_raster_comes_first(self):
        page = (self.PAGE, "text/html", "https://example.test/")
        with mock.patch.object(fetch_icon, "fetch", return_value=page), \
             mock.patch.object(fetch_icon.refero_media, "favicon_url", return_value=None):
            urls = fetch_icon.candidates("https://example.test/")
        self.assertEqual(urls, ["https://example.test/apple-touch-icon.png",
                                "https://example.test/big.png",
                                "https://example.test/mid.png",
                                "https://example.test/small.png"])


    def test_a_malformed_href_is_skipped(self):
        page = (b'<link rel="icon" href="http://[bad/icon.png" sizes="512x512">' + self.PAGE,
                "text/html", "https://example.test/")
        with mock.patch.object(fetch_icon, "fetch", return_value=page), \
             mock.patch.object(fetch_icon.refero_media, "favicon_url", return_value=None):
            urls = fetch_icon.candidates("https://example.test/")
        self.assertEqual(urls[1], "https://example.test/big.png")


class FetchTest(unittest.TestCase):
    def test_non_http_scheme_is_never_opened(self):
        with mock.patch.object(fetch_icon.urllib.request, "urlopen") as urlopen:
            self.assertIsNone(fetch_icon.fetch("file:///etc/passwd"))
        urlopen.assert_not_called()

    def test_malformed_url_returns_none(self):
        # urlparse raises ValueError on an unclosed IPv6 bracket; urlopen raises
        # http.client.InvalidURL on a control character. Neither may escape.
        self.assertIsNone(fetch_icon.fetch("http://[bad/icon.png"))
        with mock.patch.object(fetch_icon.urllib.request, "urlopen",
                               side_effect=http.client.InvalidURL("x")):
            self.assertIsNone(fetch_icon.fetch("https://example.test/a\nb.png"))


def _png(size=(300, 200)):
    """PNG bytes of a solid image, or None without Pillow."""
    try:
        from PIL import Image
    except ImportError:
        return None
    buf = io.BytesIO()
    Image.new("RGB", size, "red").save(buf, "PNG")
    return buf.getvalue()


class ConvertTest(unittest.TestCase):
    def setUp(self):
        self.png = _png()
        if self.png is None:
            self.skipTest("needs Pillow")
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)

    def test_pillow_shrinks_to_at_most_128(self):
        from PIL import Image
        src, dst = self.tmp / "icon.png", self.tmp / "out.png"
        src.write_bytes(self.png)
        with mock.patch.object(fetch_icon.shutil, "which", return_value=None):
            self.assertTrue(fetch_icon.convert(src, dst))
        with Image.open(dst) as im:
            self.assertEqual(im.size, (128, 85))

    def test_unreadable_bytes_fail_without_raising(self):
        src, dst = self.tmp / "icon.png", self.tmp / "out.png"
        src.write_bytes(b"<svg/> not a raster")
        with mock.patch.object(fetch_icon.shutil, "which", return_value=None):
            self.assertFalse(fetch_icon.convert(src, dst))

    @unittest.skipIf(shutil.which("sips") is None, "sips is macOS only")
    def test_sips_path(self):
        src, dst = self.tmp / "icon.png", self.tmp / "out.png"
        src.write_bytes(self.png)
        with mock.patch.dict(sys.modules, {"PIL": None}):    # no Pillow fallback: sips alone must work
            self.assertTrue(fetch_icon.convert(src, dst))
        self.assertGreater(dst.stat().st_size, 0)


class FetchIconTest(unittest.TestCase):
    """fetch_icon() and main() against a throwaway ROOT; fetch is patched."""

    def setUp(self):
        self.png = _png()
        if self.png is None:
            self.skipTest("needs Pillow")
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)
        for slug in ("acme", "beta"):
            (self.root / "systems" / slug).mkdir(parents=True)
        (self.root / "catalog.json").write_text(json.dumps({"systems": [
            {"slug": "acme", "url": "https://acme.test/"}, {"slug": "beta", "url": "https://beta.test/"}]}))
        for patch in (mock.patch.object(fetch_icon, "ROOT", self.root),
                      mock.patch.object(fetch_icon.shutil, "which", return_value=None),
                      mock.patch.object(fetch_icon.refero_media, "favicon_url", return_value=None)):
            patch.start()
            self.addCleanup(patch.stop)
        self.served = {}
        self.opened = []
        fetch = mock.patch.object(fetch_icon, "fetch", side_effect=self.fetch)
        fetch.start()
        self.addCleanup(fetch.stop)

    def fetch(self, url, timeout=20):
        self.opened.append(url)
        return self.served.get(url)

    def test_skips_non_images_and_svg_then_writes_the_first_raster(self):
        self.served = {
            "https://acme.test/": (b'<link rel="apple-touch-icon" href="/touch">'
                                   b'<link rel="icon" href="/a.png">', "text/html", "https://acme.test/"),
            "https://acme.test/touch": (b"<html>", "text/html", ""),
            "https://acme.test/apple-touch-icon.png": (b"<svg/>", "image/svg+xml", ""),
            "https://acme.test/a.png": (self.png, "image/png", ""),
        }
        with contextlib.redirect_stdout(io.StringIO()) as out:
            dst = fetch_icon.fetch_icon("acme", None, None)
        self.assertEqual(dst, self.root / "systems" / "acme" / "icon.png")
        self.assertTrue(dst.is_file())
        self.assertIn("https://acme.test/a.png -> systems/acme/icon.png", out.getvalue())

    def test_url_and_host_override_the_catalog(self):
        self.served = {"https://cdn.test/i.png": (self.png, "image/png", "")}
        with contextlib.redirect_stdout(io.StringIO()):
            fetch_icon.fetch_icon("acme", None, "https://cdn.test/i.png")
        self.assertEqual(self.opened, ["https://cdn.test/i.png"])
        self.opened.clear()
        with self.assertRaises(SystemExit):
            fetch_icon.fetch_icon("acme", "https://other.test", None)
        self.assertEqual(self.opened[0], "https://other.test")

    def test_unknown_slug_and_no_source(self):
        with self.assertRaises(SystemExit) as caught:
            fetch_icon.fetch_icon("nope", None, None)
        self.assertIn("no catalog entry", str(caught.exception))
        with self.assertRaises(SystemExit) as caught:
            fetch_icon.fetch_icon("acme", None, None)
        self.assertIn("no icon source worked", str(caught.exception))

    def main(self, *argv):
        err = io.StringIO()
        with mock.patch.object(sys, "argv", ["fetch_icon.py", *argv]), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            try:
                fetch_icon.main()
                code = 0
            except SystemExit as e:
                code = e.code
        return code, err.getvalue()

    def test_main_argument_errors(self):
        self.assertEqual(self.main()[0], 2)
        self.assertEqual(self.main("acme", "beta", "--url", "https://x.test/i.png")[0], 2)

    def test_all_carries_on_past_a_product_with_no_icon(self):
        # acme has nothing reachable; beta must still be fetched.
        self.served = {"https://beta.test/apple-touch-icon.png": (self.png, "image/png", "")}
        code, err = self.main("--all")
        self.assertTrue((self.root / "systems" / "beta" / "icon.png").is_file())
        self.assertEqual(code, "no icon for 1 of 2: acme")
        self.assertIn("acme: no icon source worked", err)
        code, _ = self.main("beta")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
