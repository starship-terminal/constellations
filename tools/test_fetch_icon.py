"""Tests for tools/fetch_icon.py. Run with `make test`. No network: fetch is patched."""
import http.client
import importlib.util
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
        for sizes in ("", "any", "192", "x192", "bigxbig"):
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


if __name__ == "__main__":
    unittest.main()
