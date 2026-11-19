"""Tests for the network and subprocess paths of tools/refero/fetch.py, with
urllib.request.urlopen and subprocess.run mocked: the page and sitemap GETs,
the fetch pass's failure handling, the media backfill, the node export pass
and the argument dispatch. Nothing touches the network or the real refero/
store; every write lands in a temporary directory. Run with `make test`."""
import contextlib
import io
import json
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
import fetch  # noqa: E402
import fetch_collections  # noqa: E402

UUID = "00000000-0000-0000-0000-00000000000a"
UUID_B = "00000000-0000-0000-0000-00000000000b"
CDN = "https://images.refero.design/"
SHOT = CDN + "styles/acme.jpg"
RESULT = {"meta": {"siteName": "Acme", "url": "https://acme.example",
                   "extractedAt": "2026-01-01"},
          "designSystem": {"theme": "light", "northStar": "Move fast"},
          "screenshot": {"url": SHOT}}
NO_MEDIA = {k: None for k in fetch.MEDIA_URL_FIELDS}


def page_for(result=RESULT, design_md="# Acme", video=None):
    """A Refero style page: the flight payload holding the result blob, the
    DESIGN.md block, and (optionally) the style's own escaped media record."""
    page = "self.__next_f.push([1,%s])" % json.dumps('"result":' + json.dumps(result))
    page += r'{\"screenshot\":{\"url\":\"' + SHOT + r'\"}}'
    if video:
        page += r'{\"screenshotUrl\":\"' + SHOT + r'\",\"previewVideoUrl\":\"' + video + r'\"}'
    page += f'<pre class="whitespace-pre-wrap"><code>{design_md}</code></pre>'
    page += "<title>Acme | Refero Styles</title>"
    return page


class Resp:
    """A urlopen response with the surface fetch.get uses."""

    def __init__(self, body, headers=None):
        self.body = body.encode() if isinstance(body, str) else body
        self.headers = headers or {}

    def read(self, n=-1):
        return self.body if n < 0 else self.body[:n]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


@contextlib.contextmanager
def urlopen(side):
    """Stand in for the opener fetch.get builds; yields the open() mock."""
    opened = mock.MagicMock(side_effect=side)
    with mock.patch.object(fetch, "opener", return_value=SimpleNamespace(open=opened)):
        yield opened


class NoSleep(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(fetch.time, "sleep")
        self.sleep = patcher.start()
        self.addCleanup(patcher.stop)


class GetTest(NoSleep):
    def test_returns_bytes_or_decoded_text(self):
        with urlopen([Resp("héllo"), Resp("héllo")]):
            self.assertEqual(fetch.get("https://x"), "héllo".encode())
            self.assertEqual(fetch.get("https://x", binary=False), "héllo")

    def test_sends_a_browser_user_agent_and_a_timeout(self):
        with urlopen([Resp("ok")]) as opened:
            fetch.get("https://x/page")
        req = opened.call_args.args[0]
        self.assertEqual(req.full_url, "https://x/page")
        self.assertIn("Mozilla", req.get_header("User-agent"))
        self.assertEqual(opened.call_args.kwargs["timeout"], 90)

    def test_failures_back_off_then_succeed(self):
        err = urllib.error.URLError("down")
        with urlopen([err, err, Resp("ok")]) as opened:
            self.assertEqual(fetch.get("https://x"), b"ok")
        self.assertEqual(opened.call_count, 3)
        self.assertEqual([c.args[0] for c in self.sleep.call_args_list], [1, 2])

    def test_the_last_failure_is_raised(self):
        err = urllib.error.URLError("down")
        with urlopen([err] * 4) as opened, self.assertRaises(urllib.error.URLError):
            fetch.get("https://x")
        self.assertEqual(opened.call_count, 4)

    def test_tries_bounds_the_attempts(self):
        with urlopen([OSError("a"), OSError("b")]) as opened, self.assertRaises(OSError):
            fetch.get("https://x", tries=2)
        self.assertEqual(opened.call_count, 2)


    def test_a_body_over_the_cap_raises_without_a_retry(self):
        with mock.patch.object(fetch, "MAX_RESPONSE", 4), \
                urlopen([Resp("12345"), Resp("ok")]) as opened, \
                self.assertRaises(fetch.TooLarge):
            fetch.get("https://x")
        self.assertEqual(opened.call_count, 1)
        with mock.patch.object(fetch, "MAX_RESPONSE", 4), urlopen([Resp("1234")]):
            self.assertEqual(fetch.get("https://x"), b"1234")  # exactly the cap is fine


    def test_a_body_short_of_its_content_length_is_retried(self):
        cut = Resp("par", {"Content-Length": "7"})
        with urlopen([cut, Resp("partial", {"Content-Length": "7"})]) as opened:
            self.assertEqual(fetch.get("https://x"), b"partial")
        self.assertEqual(opened.call_count, 2)
        with urlopen([Resp("par", {"Content-Length": "7"})] * 4), \
                self.assertRaises(fetch.http.client.IncompleteRead):
            fetch.get("https://x")

    def test_a_refused_redirect_is_not_retried(self):
        refused = fetch.RedirectRefused("refusing a redirect")
        with urlopen([refused, Resp("ok")]) as opened, self.assertRaises(fetch.RedirectRefused):
            fetch.get("https://x")
        self.assertEqual(opened.call_count, 1)


class CheckedRedirectTest(unittest.TestCase):
    def follow(self, allowed, target):
        handler = fetch.CheckedRedirect(allowed)
        req = urllib.request.Request("https://styles.refero.design/collections/a")
        return handler.redirect_request(req, None, 302, "Found", {}, target)

    def test_the_default_follows_only_https(self):
        self.assertEqual(self.follow(fetch.https_only, "https://cdn.example/a").full_url,
                         "https://cdn.example/a")
        for target in ("http://styles.refero.design/a", "ftp://x/a"):
            with self.assertRaises(fetch.RedirectRefused, msg=target):
                self.follow(fetch.https_only, target)

    def test_collections_follow_only_the_refero_host(self):
        ok = fetch_collections.on_base
        self.assertEqual(self.follow(ok, f"{fetch_collections.BASE}/collections/b").full_url,
                         f"{fetch_collections.BASE}/collections/b")
        for target in ("https://192.168.1.1/admin", "http://styles.refero.design/x",
                       "https://styles.refero.design.example/x"):
            with self.assertRaises(fetch.RedirectRefused, msg=target):
                self.follow(ok, target)

    def test_the_opener_carries_the_check(self):
        built = fetch.opener(fetch.https_only)
        self.assertTrue(any(isinstance(h, fetch.CheckedRedirect) for h in built.handlers))


class CollectionUrlsTest(unittest.TestCase):
    def test_only_https_pages_on_the_refero_host_are_kept(self):
        base = fetch_collections.BASE
        locs = [f"{base}/", f" {base}/collections/dark ", f"{base}/design-md/guide",
                "file:///etc/passwd", "http://styles.refero.design/collections/x",
                "https://192.168.1.1/admin", "https://styles.refero.design.example/x",
                "ftp://styles.refero.design/x", base]
        xml = "<urlset>" + "".join(f"<url><loc>{u}</loc></url>" for u in locs) + "</urlset>"
        with mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            urls = fetch_collections.collection_urls(xml)
        self.assertEqual(urls, [f"{base}/collections/dark", f"{base}/design-md/guide"])
        self.assertEqual(err.getvalue().count("SKIP off-site sitemap url"), 5)
        self.assertIn("'file:///etc/passwd'", err.getvalue())

    def test_pages_are_fetched_through_the_capped_get_with_the_host_check(self):
        with mock.patch.object(fetch_collections.refero_fetch, "get", return_value=b"x") as get:
            self.assertEqual(fetch_collections.get(fetch_collections.SITEMAP), b"x")
        get.assert_called_once_with(fetch_collections.SITEMAP, True, 4,
                                    allowed=fetch_collections.on_base)


class SitemapAndPageTest(NoSleep):
    def test_the_sitemap_yields_every_style_uuid(self):
        xml = (f"<urlset><url><loc>{fetch.BASE}/style/{UUID}</loc></url>"
               f"<url><loc>{fetch.BASE}/style/{UUID_B}</loc></url>"
               f"<url><loc>{fetch.BASE}/about</loc></url></urlset>")
        with urlopen([Resp(xml)]) as opened:
            self.assertEqual(fetch.fetch_sitemap_uuids(), [UUID, UUID_B])
        self.assertEqual(opened.call_args.args[0].full_url, fetch.SITEMAP)

    def test_fetch_one_parses_the_page_into_its_parts(self):
        video = CDN + "v/acme.mp4"
        with urlopen([Resp(page_for(video=video))]) as opened:
            uuid, url, result, design_md, name, media = fetch.fetch_one(UUID)
        self.assertEqual(opened.call_args.args[0].full_url, f"{fetch.BASE}/style/{UUID}")
        self.assertEqual((uuid, url), (UUID, f"{fetch.BASE}/style/{UUID}"))
        self.assertEqual(result["designSystem"]["theme"], "light")
        self.assertEqual(design_md, "# Acme")
        self.assertEqual(name, "Acme")
        self.assertEqual(media["video_url"], video)
        self.assertIsNone(media["video_poster_url"])

    def test_a_page_with_no_result_raises(self):
        with urlopen([Resp("<html></html>")]), self.assertRaises(ValueError):
            fetch.fetch_one(UUID)


class ReferoTmp(NoSleep):
    """A temporary refero/ that fetch reads and writes."""

    def setUp(self):
        super().setUp()
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name) / "refero"
        for name, value in {"REFERO": self.refero, "WORK": self.refero / ".work",
                            "DB": self.refero / "refero.db"}.items():
            patcher = mock.patch.object(fetch, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def rows(self, sql, *args):
        db = sqlite3.connect(self.refero / "refero.db")
        try:
            return db.execute(sql, args).fetchall()
        finally:
            db.close()

    def fetch_args(self, **kw):
        return SimpleNamespace(**{"force": False, "limit": 0, "workers": 1, **kw})

    def run_quiet(self, fn, *args):
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out, \
             mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            fn(*args)
        return out.getvalue(), err.getvalue()


class CmdFetchTest(ReferoTmp):
    def fetch_pages(self, pages, **kw):
        """Run cmd_fetch over a sitemap of `pages`, uuid -> body or Exception."""
        def fake_get(url, binary=True, tries=4):
            if url == fetch.SITEMAP:
                return "".join(f"/style/{u}" for u in pages).encode()
            body = pages[url.rsplit("/", 1)[1]]
            if isinstance(body, Exception):
                raise body
            return body.encode()
        with mock.patch.object(fetch, "get", side_effect=fake_get):
            return self.run_quiet(fetch.cmd_fetch, self.fetch_args(**kw))

    def test_a_fetch_stores_the_row_and_the_folder(self):
        out, _ = self.fetch_pages({UUID: page_for(video=CDN + "v/a.mp4")})
        self.assertIn("fetched 1, errors 0", out)
        row = self.rows("SELECT slug, name, theme, video_url FROM styles")[0]
        self.assertEqual(row, ("acme", "Acme", "light", CDN + "v/a.mp4"))
        self.assertEqual((self.refero / "acme" / "DESIGN.md").read_text(), "# Acme")
        self.assertTrue((self.refero / ".work" / f"{UUID}.json").exists())

    def test_a_failed_page_is_recorded_and_the_rest_still_land(self):
        out, err = self.fetch_pages({UUID: urllib.error.URLError("boom"),
                                     UUID_B: page_for()})
        self.assertIn("FAIL " + UUID, err)
        self.assertIn("fetched 1, errors 1 (1 in fetch_errors)", out)
        self.assertEqual(self.rows("SELECT uuid FROM fetch_errors"), [(UUID,)])
        self.assertEqual(self.rows("SELECT uuid FROM styles"), [(UUID_B,)])

    def test_a_later_success_clears_the_recorded_failure(self):
        self.fetch_pages({UUID: urllib.error.URLError("boom")})
        self.fetch_pages({UUID: page_for()})
        self.assertEqual(self.rows("SELECT uuid FROM fetch_errors"), [])
        self.assertEqual(self.rows("SELECT slug FROM styles"), [("acme",)])

    def test_stored_styles_are_skipped_unless_forced(self):
        self.fetch_pages({UUID: page_for()})
        out, _ = self.fetch_pages({UUID: urllib.error.URLError("not asked")})
        self.assertIn("to fetch: 0", out)
        out, _ = self.fetch_pages({UUID: page_for()}, force=True)
        self.assertIn("fetched 1, errors 0", out)

    def test_limit_caps_how_many_styles_are_fetched(self):
        out, _ = self.fetch_pages({UUID: page_for(), UUID_B: page_for()}, limit=1)
        self.assertIn("to fetch: 1", out)
        self.assertEqual(len(self.rows("SELECT uuid FROM styles")), 1)

    def test_same_named_styles_get_numbered_slugs(self):
        self.fetch_pages({UUID: page_for(), UUID_B: page_for()}, workers=1)
        slugs = sorted(r[0] for r in self.rows("SELECT slug FROM styles"))
        self.assertEqual(slugs, ["acme", "acme-2"])

    def test_resolved_component_html_is_written_beside_the_style(self):
        result = json.loads(json.dumps(RESULT))
        result["designSystem"]["components"] = [{"name": "Button", "html": "<b/>"}]
        self.fetch_pages({UUID: page_for(result)})
        comps = json.loads((self.refero / "acme" / "components.json").read_text())
        self.assertEqual(comps[0]["name"], "Button")
        meta = json.loads((self.refero / "acme" / "meta.json").read_text())
        self.assertTrue(meta["has_components"])
        # A refetch with none left removes the stale file.
        self.fetch_pages({UUID: page_for()}, force=True)
        self.assertFalse((self.refero / "acme" / "components.json").exists())

    def test_a_refetch_keeps_labels_a_classifier_already_set(self):
        self.fetch_pages({UUID: page_for()})
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("UPDATE styles SET product_type='ai', design_style='neon', "
                   "tags='[\"minimal\"]'")
        db.commit()
        db.close()
        self.fetch_pages({UUID: page_for()}, force=True)
        meta = json.loads((self.refero / "acme" / "meta.json").read_text())
        self.assertEqual((meta["product_type"], meta["design_style"], meta["tags"]),
                         ("ai", "neon", ["minimal"]))


class EnrichMediaTest(ReferoTmp):
    def setUp(self):
        super().setUp()
        db = fetch.init_db()
        db.execute(
            "INSERT INTO styles (uuid, slug, name, page_url, fetched_at, tagline) "
            "VALUES (?,?,?,?,?,?)",
            (UUID, "acme", "Acme", f"{fetch.BASE}/style/{UUID}", "t0", "tag"))
        db.commit()
        db.close()
        (self.refero / "acme").mkdir()
        (self.refero / "acme" / "meta.json").write_text(json.dumps({"slug": "acme"}))

    def test_media_lands_in_the_row_and_in_meta_json(self):
        video = CDN + "v/acme.mp4"
        with mock.patch.object(fetch, "get", return_value=page_for(video=video).encode()):
            out, _ = self.run_quiet(fetch.cmd_enrich_media, self.fetch_args())
        self.assertIn("enriched 1, errors 0", out)
        video_url, fetched = self.rows("SELECT video_url, media_fetched_at FROM styles")[0]
        self.assertEqual(video_url, video)
        self.assertIsNotNone(fetched)
        meta = json.loads((self.refero / "acme" / "meta.json").read_text())
        self.assertEqual(meta["video_url"], video)
        self.assertEqual(meta["slug"], "acme")

    def test_a_failure_is_recorded_and_the_row_stays_retryable(self):
        with mock.patch.object(fetch, "get", side_effect=OSError("offline")):
            _, err = self.run_quiet(fetch.cmd_enrich_media, self.fetch_args())
        self.assertIn("FAIL acme: offline", err)
        self.assertEqual(self.rows("SELECT uuid, error FROM fetch_errors"),
                         [(UUID, "offline")])
        self.assertIsNone(self.rows("SELECT media_fetched_at FROM styles")[0][0])

    def test_enriched_rows_are_skipped_unless_forced(self):
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("UPDATE styles SET media_fetched_at='t1'")
        db.commit()
        db.close()
        with mock.patch.object(fetch, "get") as get:
            out, _ = self.run_quiet(fetch.cmd_enrich_media, self.fetch_args())
            self.assertIn("to enrich: 0", out)
            get.assert_not_called()
            get.return_value = page_for().encode()
            out, _ = self.run_quiet(fetch.cmd_enrich_media, self.fetch_args(force=True))
        self.assertIn("enriched 1, errors 0", out)

    def test_limit_caps_the_backfill(self):
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("INSERT INTO styles (uuid, slug, name, page_url, fetched_at) "
                   "VALUES (?,?,?,?,?)", (UUID_B, "beta", "Beta", "p", "t0"))
        db.commit()
        db.close()
        with mock.patch.object(fetch, "get", return_value=page_for().encode()) as get:
            out, _ = self.run_quiet(fetch.cmd_enrich_media, self.fetch_args(limit=1))
        self.assertIn("to enrich: 1", out)
        self.assertEqual(get.call_count, 1)


class CmdExportTest(ReferoTmp):
    def setUp(self):
        super().setUp()
        db = fetch.init_db()
        db.execute(
            "INSERT INTO styles (uuid, slug, name, page_url, fetched_at, result_json) "
            "VALUES (?,?,?,?,?,?)",
            (UUID, "acme", "Acme", "p", "t0", json.dumps(RESULT)))
        db.commit()
        db.close()

    def node(self, records, returncode=0):
        """A subprocess.run stand-in for the node pass: it writes the jobs'
        artifact lines next to the jobs file, as export.js does."""
        def run(cmd, **kw):
            jobs_file = cmd[2]
            self.cmd = cmd
            self.jobs = json.loads(Path(jobs_file).read_text())
            Path(jobs_file + ".artifacts.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in records))
            return SimpleNamespace(returncode=returncode)
        return mock.patch.object(fetch.subprocess, "run", side_effect=run)

    ARTIFACTS = {"variables.css": "v", "theme.css": "t", "tokens.json": "{}",
                 "design-system.json": '{"a":1}', "prompt.txt": "p"}

    def test_artifacts_from_node_are_stored_on_the_row(self):
        with self.node([{"uuid": UUID, "artifacts": self.ARTIFACTS}]):
            out, _ = self.run_quiet(fetch.cmd_export)
        self.assertIn("exporting 1 styles", out)
        self.assertEqual(self.cmd[0], "node")
        self.assertEqual(self.jobs[0]["slug"], "acme")
        self.assertEqual(self.jobs[0]["outDir"], str(self.refero / "acme"))
        row = self.rows("SELECT variables_css, theme_css, tokens_json, "
                        "design_system_json, prompt_txt FROM styles")[0]
        self.assertEqual(row, ("v", "t", "{}", '{"a":1}', "p"))

    def test_a_torn_work_file_is_restored_from_the_db(self):
        work = self.refero / ".work"
        work.mkdir(exist_ok=True)
        (work / f"{UUID}.json").write_text('{"torn":')
        with self.node([{"uuid": UUID, "artifacts": self.ARTIFACTS}]):
            self.run_quiet(fetch.cmd_export)
        self.assertEqual(json.loads((work / f"{UUID}.json").read_text())["designSystem"]
                         ["theme"], "light")

    def test_a_per_style_error_is_reported_and_skipped(self):
        with self.node([{"uuid": UUID, "error": "bad tokens"}]):
            _, err = self.run_quiet(fetch.cmd_export)
        self.assertIn(f"export FAIL {UUID}: bad tokens", err)
        self.assertIsNone(self.rows("SELECT variables_css FROM styles")[0][0])

    def test_a_failing_node_exits_with_its_code(self):
        with self.node([], returncode=3), self.assertRaises(SystemExit) as exit_:
            self.run_quiet(fetch.cmd_export)
        self.assertEqual(exit_.exception.code, 3)


class MainDispatchTest(unittest.TestCase):
    def run_main(self, *argv):
        names = ("cmd_fetch", "cmd_export", "cmd_catalog", "cmd_enrich_media")
        calls = []
        patches = [mock.patch.object(fetch, n, side_effect=lambda *a, n=n: calls.append(n))
                   for n in names]
        # The text dump refresh runs last however main ends; record it rather
        # than dump the repo's real refero.db from a unit test.
        patches.append(mock.patch.object(
            fetch.refero_dump, "refresh",
            side_effect=lambda path: calls.append(("refresh", path))))
        for p in patches:
            p.start()
        try:
            with mock.patch.object(sys, "argv", ["fetch.py", *argv]):
                fetch.main()
        finally:
            for p in patches:
                p.stop()
        self.assertEqual(calls[-1], ("refresh", fetch.DB))
        return calls[:-1]

    def test_the_default_run_fetches_exports_then_catalogs(self):
        self.assertEqual(self.run_main(), ["cmd_fetch", "cmd_export", "cmd_catalog"])

    def test_catalog_only(self):
        self.assertEqual(self.run_main("--catalog-only"), ["cmd_catalog"])

    def test_export_only_also_refreshes_the_catalog(self):
        self.assertEqual(self.run_main("--export-only"), ["cmd_export", "cmd_catalog"])

    def test_enrich_media_also_refreshes_the_catalog(self):
        self.assertEqual(self.run_main("--enrich-media"),
                         ["cmd_enrich_media", "cmd_catalog"])

    def test_enrich_media_cannot_combine_with_the_other_passes(self):
        with mock.patch("sys.stderr"), self.assertRaises(SystemExit):
            self.run_main("--enrich-media", "--catalog-only")


if __name__ == "__main__":
    unittest.main()
