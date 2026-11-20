"""Tests for tools/refero/fetch.py and mirror_media.py, plus the
emitted-vs-consumed contract between the refero JSON the tools write and what
the app (web/) reads. Run with `make test`."""
import json
import os
import re
import sqlite3
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "refero"))
import catalog  # noqa: E402
import check as refero_check  # noqa: E402
import fetch  # noqa: E402
import mirror_media  # noqa: E402
import refero_media  # noqa: E402


# ---------------------------------------------------------------- fetch.py


def push(chunk):
    """One self.__next_f.push line as it appears in a Refero page."""
    return f"self.__next_f.push([1,{json.dumps(chunk)}])"


RESULT = {"meta": {"siteName": "Acme", "url": "https://acme.example",
                   "extractedAt": "2026-01-01"},
          "designSystem": {"theme": "light", "northStar": "Move fast"},
          "screenshot": {"url": "https://images.refero.design/styles/acme.jpg"}}

OWN_SHOT = "https://images.refero.design/styles/acme.jpg"
OTHER_SHOT = "https://images.refero.design/styles/peer.jpg"
CDN = "https://images.refero.design/"


def media_record(shot, video=None, poster=None, detail=None, detail_poster=None):
    """One style's record as escaped JSON inside the raw page text."""
    parts = [r'\"screenshotUrl\":\"' + shot + r'\"']
    for name, val in (("previewVideoUrl", video),
                      ("previewVideoPosterUrl", poster),
                      ("previewVideoDetailUrl", detail),
                      ("previewVideoDetailPosterUrl", detail_poster)):
        parts.append(r'\"' + name + r'\":' + (r'\"' + val + r'\"' if val else "null"))
    return ",".join(parts)


def media_page(record):
    """A page holding a result blob whose screenshot anchors `record`, the
    record itself, then a related style's record with different values."""
    result = {"meta": {"siteName": "Acme"}, "designSystem": {},
              "screenshot": {"url": OWN_SHOT}}
    page = push('"result":' + json.dumps(result))
    page += r'{\"screenshot\":{\"url\":\"' + OWN_SHOT + r'\"}}'
    page += "record:{" + record + "}"
    page += "related:{" + media_record(
        OTHER_SHOT, video=CDN + "v/peer.mp4", poster=CDN + "i/peer.jpg") + "}"
    return page


class SlugifyTest(unittest.TestCase):
    def test_names_slug_to_dashes(self):
        self.assertEqual(fetch.slugify("Acme Inc."), "acme-inc")
        self.assertEqual(fetch.slugify("  B2B SaaS!  "), "b2b-saas")
        self.assertEqual(fetch.slugify("a--b"), "a-b")

    def test_empty_names_fall_back(self):
        self.assertEqual(fetch.slugify(""), "unnamed")
        self.assertEqual(fetch.slugify("!!!"), "unnamed")


class UniqueSlugTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE styles (uuid TEXT, slug TEXT)")
        self.db.execute("INSERT INTO styles VALUES ('u1', 'acme')")
        self.db.execute("INSERT INTO styles VALUES ('u2', 'acme-2')")

    def tearDown(self):
        self.db.close()

    def test_taken_names_pick_the_next_number(self):
        self.assertEqual(fetch.unique_slug(self.db, "Acme"), "acme-3")
        self.assertEqual(fetch.unique_slug(self.db, "Fresh"), "fresh")

    def test_a_refetch_keeps_its_own_slug(self):
        self.assertEqual(fetch.unique_slug(self.db, "Acme", uuid="u1"), "acme")


class FlightBlobTest(unittest.TestCase):
    def test_push_chunks_join_and_unescape(self):
        page = push('{"a":"he said \\"hi\\""}') + push(',"b":[1]}')
        self.assertEqual(fetch.flight_blob(page),
                         '{"a":"he said \\"hi\\""},"b":[1]}')

    def test_other_push_shapes_are_ignored(self):
        self.assertEqual(fetch.flight_blob('self.__next_f.push([0,"x"])'
                                           + push("real")), "real")


class ExtractResultTest(unittest.TestCase):
    def test_finds_the_result_object(self):
        page = push('"other":{"result":{"no":"keys"}}') + \
            push('"result":' + json.dumps(RESULT))
        self.assertEqual(fetch.extract_result(fetch.flight_blob(page)), RESULT)

    def test_braces_and_escapes_inside_strings_do_not_break_the_scan(self):
        result = {**RESULT,
                  "meta": {**RESULT["meta"], "siteName": 'a "b" } { \\'}}
        page = push('"result":' + json.dumps(result))
        self.assertEqual(fetch.extract_result(fetch.flight_blob(page)), result)

    def test_an_undecodable_result_key_falls_through_to_the_next(self):
        page = push('"result":{"truncated') + \
            push('"result":' + json.dumps(RESULT))
        self.assertEqual(fetch.extract_result(fetch.flight_blob(page)), RESULT)

    def test_no_result_returns_none(self):
        self.assertIsNone(fetch.extract_result(fetch.flight_blob(push('"x":1'))))
        self.assertIsNone(fetch.extract_result(""))


class ParsePageTest(unittest.TestCase):
    def test_result_and_design_md(self):
        page = push('"result":' + json.dumps(RESULT)) + \
            '<pre class="whitespace-pre-wrap"><code># Hi &amp; bye</code></pre>'
        result, design_md = fetch.parse_page(page)
        self.assertEqual(result, RESULT)
        self.assertEqual(design_md, "# Hi & bye")

    def test_a_page_without_a_result_raises(self):
        with self.assertRaises(ValueError):
            fetch.parse_page("<html></html>")

    def test_style_name_prefers_meta_then_title(self):
        page = "<title>T | Refero Styles</title>"
        self.assertEqual(fetch.style_name(RESULT, page), "Acme")
        self.assertEqual(fetch.style_name({"meta": {}}, page), "T")
        self.assertIsNone(fetch.style_name({"meta": {}}, "<html/>"))


class ResolveComponentHtmlTest(unittest.TestCase):
    def test_refs_resolve_to_their_text_rows(self):
        # The row length counts UTF-8 bytes; ⌘ (3 bytes) exercises the slice.
        html = '<style>.a{content:"⌘"}</style><div>hi</div>'
        row = "1e:T" + format(len(html.encode()), "x") + "," + html
        result = {"designSystem": {"components": [
            {"name": "a", "html": "$1e"}, {"name": "b"}]}}
        blob = '"result":' + json.dumps(result) + "}" + row + "tail"
        self.assertEqual(fetch.resolve_component_html(result, blob), 0)
        self.assertEqual(
            result["designSystem"]["components"][0]["html"], html)

    def test_unresolved_refs_and_undefined_become_none(self):
        result = {"designSystem": {"components": [
            {"html": "$zz"}, {"html": "$undefined"}]}}
        misses = fetch.resolve_component_html(result, "blob without rows")
        self.assertEqual(misses, 1)
        self.assertIsNone(result["designSystem"]["components"][0]["html"])
        self.assertIsNone(result["designSystem"]["components"][1]["html"])

    def test_parse_page_resolves_component_refs(self):
        html = "<div>ok</div>"
        row = "1e:T" + format(len(html.encode()), "x") + "," + html
        result = {**RESULT,
                  "designSystem": {"components": [{"html": "$1e"}]}}
        page = push('"result":' + json.dumps(result) + "}" + row)
        got, _ = fetch.parse_page(page)
        self.assertEqual(
            got["designSystem"]["components"][0]["html"], html)


class ExtractMediaTest(unittest.TestCase):
    def test_media_comes_from_the_style_s_own_record(self):
        page = media_page(media_record(
            OWN_SHOT, video=CDN + "v/acme.mp4", poster=CDN + "i/acme.jpg",
            detail=CDN + "v/acme-d.mp4", detail_poster=CDN + "i/acme-d.jpg"))
        self.assertEqual(fetch.extract_media(page), {
            "video_url": CDN + "v/acme.mp4",
            "video_poster_url": CDN + "i/acme.jpg",
            "video_detail_url": CDN + "v/acme-d.mp4",
            "video_detail_poster_url": CDN + "i/acme-d.jpg"})

    def test_the_fixed_key_set_and_nulls_when_absent(self):
        page = media_page(media_record(OWN_SHOT))
        media = fetch.extract_media(page)
        self.assertEqual(set(media), set(fetch.MEDIA_URL_FIELDS))
        self.assertTrue(all(v is None for v in media.values()))

    def test_first_occurrence_wins_when_the_anchor_is_missing(self):
        # No result screenshot blob: the first record's fields win.
        page = "record:{" + media_record(OTHER_SHOT, video=CDN + "v/a.mp4") + "}"
        self.assertEqual(fetch.extract_media(page)["video_url"],
                         CDN + "v/a.mp4")

    def test_non_cdn_and_absent_fields_yield_none(self):
        page = media_page(media_record(
            OWN_SHOT, video="https://other.cdn.example/v.mp4"))
        self.assertIsNone(fetch.extract_media(page)["video_url"])


def styles_db():
    """An in-memory db holding the styles columns write_meta reads."""
    db = sqlite3.connect(":memory:")
    db.execute("""CREATE TABLE styles (uuid, slug, name, tagline, theme,
        product_type, design_style, tags, page_url, source_url, extracted_at,
        fetched_at, screenshot_url, components_json)""")
    db.execute("INSERT INTO styles VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               ("u1", "acme", "Acme", "tag", "light", "devtools", "technical",
                '["neon"]', "https://p/acme", "https://acme.example",
                "t0", "t1", "https://img/s.jpg", None))
    return db


MEDIA = {k: None for k in fetch.MEDIA_URL_FIELDS}
MEDIA["video_url"] = "https://img/v.mp4"

# What fetch writes to meta.json: the base keys, the label keys, the media
# URL keys and the component flag. tools/refero/check.py compares META_FIELDS
# of it against the db.
META_KEYS = {"uuid", "slug", "name", "tagline", "theme", "product_type",
             "design_style", "tags", "page_url", "source_url", "extracted_at",
             "fetched_at", "screenshot_url", "has_components"} | set(MEDIA)


class StyleMetaTest(unittest.TestCase):
    def test_the_meta_key_set_is_fixed(self):
        meta = fetch.style_meta("u1", "acme", "Acme", RESULT, MEDIA,
                                {"product_type": "devtools",
                                 "design_style": "technical", "tags": ["neon"]},
                                "t1")
        self.assertEqual(set(meta), META_KEYS)
        self.assertEqual(meta["tagline"], "Move fast")
        self.assertEqual(meta["theme"], "light")
        self.assertEqual(meta["source_url"], "https://acme.example")
        self.assertEqual(meta["extracted_at"], "2026-01-01")
        self.assertEqual(meta["video_url"], "https://img/v.mp4")


class WriteMetaTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.refero = Path(self.tmp.name) / "refero"
        self.refero.mkdir()
        self.patch = mock.patch.object(fetch, "REFERO", self.refero)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def meta(self, slug="acme"):
        return json.loads((self.refero / slug / "meta.json").read_text())

    def write_meta(self, slug, media):
        db = styles_db()
        try:
            fetch.write_meta(db, slug, media)
        finally:
            db.close()

    def test_media_keys_merge_into_an_existing_meta(self):
        folder = self.refero / "acme"
        folder.mkdir()
        (folder / "meta.json").write_text(json.dumps(
            {"uuid": "u1", "slug": "acme", "name": "Acme", "custom": 1}))
        self.write_meta("acme", MEDIA)
        meta = self.meta()
        self.assertEqual(list(meta)[:3], ["uuid", "slug", "name"])
        self.assertEqual(meta["custom"], 1)
        self.assertEqual(meta["video_url"], "https://img/v.mp4")
        self.assertEqual(meta["has_components"], False)
        self.assertEqual(set(meta),
                         {"uuid", "slug", "name", "custom", "has_components"}
                         | set(MEDIA))

    def test_a_missing_meta_is_rebuilt_from_the_styles_row(self):
        self.write_meta("acme", MEDIA)
        meta = self.meta()
        self.assertEqual(set(meta), META_KEYS)
        self.assertEqual(meta["uuid"], "u1")
        self.assertEqual(meta["tags"], ["neon"])

    def test_a_corrupt_meta_moves_aside_and_rebuilds(self):
        folder = self.refero / "acme"
        folder.mkdir()
        (folder / "meta.json").write_text('{"uuid": "u1", "trun')
        self.write_meta("acme", MEDIA)
        self.assertEqual(self.meta()["uuid"], "u1")
        self.assertEqual(set(self.meta()), META_KEYS)
        self.assertEqual((folder / "meta.json.bad").read_text(),
                         '{"uuid": "u1", "trun')

    def test_a_non_object_meta_is_also_torn(self):
        folder = self.refero / "acme"
        folder.mkdir()
        (folder / "meta.json").write_text("[]")
        self.write_meta("acme", MEDIA)
        self.assertTrue((folder / "meta.json.bad").is_file())
        self.assertEqual(set(self.meta()), META_KEYS)

    def test_atomic_write_leaves_no_tmp(self):
        self.write_meta("acme", MEDIA)
        self.assertEqual(list((self.refero / "acme").glob("*.tmp")), [])


# ------------------------------------------------------------- mirror_media


class Resp:
    """A urlopen response with just enough surface for download()."""
    def __init__(self, data=b"bytes", content_type="image/jpeg"):
        self._data = data
        self.headers = {"Content-Type": content_type}

    def read(self):
        return self._data

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class FaviconUrlTest(unittest.TestCase):
    def test_the_url_param_is_the_quoted_https_host(self):
        self.assertEqual(
            refero_media.favicon_url("https://www.acme.example/x"),
            refero_media.FAVICON_API + "https%3A%2F%2Fwww.acme.example")
        self.assertEqual(
            refero_media.favicon_url("acme.example"),
            refero_media.FAVICON_API + "https%3A%2F%2Facme.example")

    def test_no_host_means_no_url(self):
        self.assertIsNone(refero_media.favicon_url(None))
        self.assertIsNone(refero_media.favicon_url(""))
        self.assertIsNone(refero_media.favicon_url("http://"))


ROW = ("acme", "https://img/s.jpg", "https://img/p.jpg", "https://img/v.mp4",
       "https://img/d.mp4", "https://img/dp.jpg", "https://acme.example")


class StyleUrlsTest(unittest.TestCase):
    def test_every_kind_resolves_from_the_row(self):
        urls = mirror_media.style_urls(ROW)
        self.assertEqual(set(urls), set(refero_media.KINDS))
        self.assertEqual(urls["shots"], "https://img/s.jpg")
        self.assertEqual(urls["detail-posters"], "https://img/dp.jpg")
        self.assertEqual(urls["favicons"],
                         refero_media.favicon_url("https://acme.example"))


class DownloadTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dest = Path(self.tmp.name) / "shots" / "acme.jpg"
        self.dest.parent.mkdir(parents=True)
        self.sleep = mock.patch.object(mirror_media.time, "sleep")
        self.sleep.start()

    def tearDown(self):
        self.sleep.stop()
        self.tmp.cleanup()

    def fetch_it(self, side):
        return mock.patch.object(mirror_media.OPENER, "open",
                                 side_effect=side)

    def test_a_good_response_writes_via_partial(self):
        with self.fetch_it([Resp(b"img")]) as u:
            mirror_media.download("shots", "https://x", self.dest)
        self.assertEqual(self.dest.read_bytes(), b"img")
        self.assertEqual(u.call_count, 1)
        self.assertFalse(self.dest.with_name("acme.jpg.partial").exists())

    def test_an_html_response_is_rejected_and_keeps_no_file(self):
        with self.fetch_it([Resp(b"<html>", "text/html")]), \
                self.assertRaises(ValueError):
            mirror_media.download("shots", "https://x", self.dest)
        self.assertFalse(self.dest.exists())
        self.assertFalse(self.dest.with_name("acme.jpg.partial").exists())

    def test_a_generic_content_type_is_accepted(self):
        with self.fetch_it([Resp(b"img", "application/octet-stream")]):
            mirror_media.download("shots", "https://x", self.dest)
        self.assertTrue(self.dest.exists())

    def test_kind_prefixes_are_enforced(self):
        with self.fetch_it([Resp(b"img", "image/png")]), \
                self.assertRaises(ValueError):
            mirror_media.download("videos", "https://x", self.dest)
        with self.fetch_it([Resp(b"v", "video/mp4")]):
            mirror_media.download("videos", "https://x", self.dest)

    def test_failures_retry_then_raise(self):
        err = urllib.error.URLError("down")
        with self.fetch_it([err, err, Resp(b"img")]) as u:
            mirror_media.download("shots", "https://x", self.dest)
        self.assertEqual(u.call_count, 3)
        with self.fetch_it([err] * 4), self.assertRaises(urllib.error.URLError):
            mirror_media.download("shots", "https://x", self.dest)

    def test_a_failed_rename_cleans_the_partial(self):
        with self.fetch_it([Resp(b"img")]), \
                mock.patch.object(mirror_media.os, "replace",
                                  side_effect=OSError("disk")), \
                self.assertRaises(OSError):
            mirror_media.download("shots", "https://x", self.dest)
        self.assertFalse(self.dest.with_name("acme.jpg.partial").exists())


class MissingFilesTest(unittest.TestCase):
    def test_expected_files_that_are_absent_or_empty_are_listed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shots").mkdir()
            (root / "shots" / "acme.jpg").write_bytes(b"x")
            (root / "posters").mkdir()
            (root / "posters" / "acme.jpg").write_bytes(b"")  # empty = missing
            missing = mirror_media.missing_files([ROW], root, set(refero_media.KINDS))
        self.assertEqual(set(missing),
                         {("posters", "acme"), ("videos", "acme"),
                          ("detail", "acme"), ("detail-posters", "acme"),
                          ("favicons", "acme")})

    def test_a_row_without_urls_expects_nothing(self):
        row = ("beta",) + (None,) * 5 + (None,)
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(mirror_media.missing_files(
                [row], Path(tmp), set(refero_media.KINDS)), [])

    def test_only_filters_the_kinds(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = mirror_media.missing_files([ROW], Path(tmp), {"shots"})
        self.assertEqual(missing, [("shots", "acme")])


# ------------------------------------------- emitted <-> consumed contract

# The emitted object shapes (catalog.py) and what of them the app reads. The
# consumed side is the TypeScript interfaces in web/lib/refero.ts plus the
# literal field accesses in the components and lib sources under web/.
INDEX_KEYS = {"version", "cdn", "mediaBase", "styles"}
CARD_KEYS = {"slug", "name", "tagline", "theme", "industry", "type", "style",
             "tags", "src", "card", "cardRemote", "video", "videoRemote"}
ENTITY_KEYS = {"slug", "name", "tagline", "theme", "industry", "type", "style",
               "source_url", "page_url", "media", "docs", "ds", "similar",
               "mediaBase"}
MEDIA_KEYS = set(catalog.REFERO_MEDIA)
MEDIA_PAIR_KEYS = {"local", "remote"}
DOCS_KEYS = {"design_md", "variables_css", "theme_css", "tokens_json"}
DS_KEYS = set(catalog.REFERO_DS_KEYS)
SIMILAR_KEYS = {"slug", "name", "why"}

WEB = TOOLS.parent / "web"
REFERO_TS = (WEB / "lib" / "refero.ts").read_text()
WEB_SRC = "\n".join(p.read_text() for p in
                    sorted((WEB / "components").rglob("*.tsx"))
                    + sorted((WEB / "lib").rglob("*.ts")))
APP_SRC = "\n".join(p.read_text() for p in sorted((WEB / "app").rglob("*.tsx")))


def ts_fields(name: str) -> set:
    """The field names one `export interface` declares: interfaces are written
    line-per-field, so a line-start identifier is a field and a nested inline
    type's keys are not."""
    m = re.search(rf"export interface {name} \{{(.*?)^\}}", REFERO_TS, re.S | re.M)
    return set(re.findall(r"(?m)^\s*(\w+)\s*:", m.group(1)))

CONTRACT_META = {"slug": "alpha", "name": "Alpha", "tagline": "tag",
                 "theme": "light", "product_type": "devtools",
                 "design_style": "technical", "tags": ["neon"], "uuid": "u1",
                 "source_url": "https://www.alpha.example.com/x",
                 "page_url": "https://p/alpha", "extracted_at": "t0",
                 "fetched_at": "t1", "screenshot_url": "https://img/s.jpg",
                 "video_url": "https://img/v.mp4",
                 "video_poster_url": "https://img/p.jpg",
                 "video_detail_url": "https://img/d.mp4",
                 "video_detail_poster_url": "https://img/dp.jpg"}
CONTRACT_DS = {"meta": {"thumbnailUrl": "https://img/t.jpg"}, "industry": "media",
               "description": "desc", "theme": "dark", "northStar": "n",
               "colors": [{"hex": "#fff"}], "typography": [], "typeScale": [],
               "spacing": {}, "elevation": [], "elevationPhilosophy": "p",
               "dos": [], "donts": [], "components": {}, "imagery": {},
               "layout": {}, "customSections": [], "surfaces": [],
               "similar": [{"business": "Beta", "why": "same"}]}
CONTRACT_BETA = {"slug": "beta", "name": "Beta"}
CONTRACT_BETA_DS = {"description": "d2"}


MEDIA_BASE = "https://media.example.test"
DEFAULT_MEDIA_BASE = "https://pub-b22e019453104cc8b3c214b1009a6c42.r2.dev"  # the public R2 bucket


class MediaBaseTest(unittest.TestCase):
    """refero_media.media_base(): the environment wins, else the default bucket."""

    def test_the_environment_wins_and_an_empty_value_means_the_site_itself(self):
        with mock.patch.object(refero_media, "load_env", return_value=[]):
            for value in (MEDIA_BASE, ""):
                with mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_MEDIA_BASE": value}):
                    self.assertEqual(refero_media.media_base(), value)

    def test_unset_falls_back_to_the_default_bucket(self):
        env = {k: v for k, v in os.environ.items() if k != "DESIGN_SYSTEMS_MEDIA_BASE"}
        with mock.patch.object(refero_media, "load_env", return_value=[]), \
                mock.patch.dict(os.environ, env, clear=True):
            self.assertEqual(refero_media.media_base(), DEFAULT_MEDIA_BASE)

    def test_load_env_reads_only_the_named_keys_and_never_overrides(self):
        with tempfile.TemporaryDirectory() as d:
            env_file = Path(d) / ".env"
            env_file.write_text("DESIGN_SYSTEMS_MEDIA_BASE=https://from-file.test\n"
                                "export OTHER_KEY='x'\nSITE_PASSWORD=never\n")
            clean = {k: v for k, v in os.environ.items()
                     if k not in ("DESIGN_SYSTEMS_MEDIA_BASE", "OTHER_KEY", "SITE_PASSWORD")}
            with mock.patch.dict(os.environ, clean, clear=True):
                self.assertEqual(refero_media.load_env(("DESIGN_SYSTEMS_MEDIA_BASE", "OTHER_KEY"),
                                                       env_file), ["DESIGN_SYSTEMS_MEDIA_BASE", "OTHER_KEY"])
                self.assertEqual(os.environ["OTHER_KEY"], "x")
                self.assertNotIn("SITE_PASSWORD", os.environ)
                os.environ["DESIGN_SYSTEMS_MEDIA_BASE"] = "https://already.test"
                refero_media.load_env(("DESIGN_SYSTEMS_MEDIA_BASE",), env_file)
                self.assertEqual(os.environ["DESIGN_SYSTEMS_MEDIA_BASE"], "https://already.test")


class ReferoEmitContractTest(unittest.TestCase):
    """build_refero's output pinned against fixed key sets and what the app
    actually reads (the web/ TypeScript interfaces and field accesses)."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.site = root / "web" / "data"
        for slug, meta, ds in (("alpha", CONTRACT_META, CONTRACT_DS),
                               ("beta", CONTRACT_BETA, CONTRACT_BETA_DS)):
            folder = root / "refero" / slug
            folder.mkdir(parents=True)
            (folder / "meta.json").write_text(json.dumps(meta))
            (folder / "design-system.json").write_text(json.dumps(ds))
            (folder / "DESIGN.md").write_text("# D\n")
        # build_refero reads the media base through its own copy of refero_media (catalog.py
        # loads it by location, so it is not the `refero_media` imported here), whose media_base()
        # copies DESIGN_SYSTEMS_MEDIA_BASE from the repo's .env into os.environ. Pin the
        # value and skip the .env, so the output does not depend on the machine and
        # nothing leaks into the rest of the test run.
        cls.env_before = os.environ.get("DESIGN_SYSTEMS_MEDIA_BASE")
        with mock.patch.object(catalog, "ROOT", root), \
                mock.patch.object(catalog, "DATA", cls.site), \
                mock.patch.object(catalog.refero_media, "load_env", return_value=[]) as cls.load_env, \
                mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_MEDIA_BASE": MEDIA_BASE}):
            out = catalog.build_refero()
        cls.index = json.loads(out.read_text())
        cls.entity = json.loads(
            (cls.site / "refero" / "style" / "alpha.json").read_text())
        cls.beta = json.loads(
            (cls.site / "refero" / "style" / "beta.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_the_media_base_comes_from_the_environment(self):
        self.assertEqual(self.index["mediaBase"], MEDIA_BASE)
        self.load_env.assert_called_with(("DESIGN_SYSTEMS_MEDIA_BASE",))
        self.assertEqual(os.environ.get("DESIGN_SYSTEMS_MEDIA_BASE"), self.env_before)  # restored, or still absent

    def test_emitted_key_sets_are_fixed(self):
        self.assertEqual(set(self.index), INDEX_KEYS)
        card = self.index["styles"][0]
        self.assertEqual(set(card), CARD_KEYS)
        self.assertEqual(set(self.entity), ENTITY_KEYS)
        self.assertEqual(set(self.entity["media"]), MEDIA_KEYS)
        for pair in self.entity["media"].values():
            if pair is not None:
                self.assertEqual(set(pair), MEDIA_PAIR_KEYS)
        self.assertEqual(set(self.entity["docs"]), DOCS_KEYS)
        self.assertEqual(set(self.entity["similar"][0]), SIMILAR_KEYS)
        # ds holds exactly the keys the page renders when the source has them.
        self.assertEqual(set(self.entity["ds"]), DS_KEYS)
        self.assertEqual(set(self.beta["ds"]), {"description"})

    def test_the_page_reads_exactly_the_emitted_keys(self):
        # The app's TypeScript interfaces (web/lib/refero.ts) declare the
        # consumed side: a key emitted but not declared is dead payload
        # (issue #61), and a key declared but not emitted renders undefined.
        self.assertEqual(ts_fields("ReferoIndex"), INDEX_KEYS)
        self.assertEqual(ts_fields("ReferoCard"), CARD_KEYS)
        self.assertEqual(ts_fields("ReferoEntity"), ENTITY_KEYS)
        self.assertEqual(ts_fields("ReferoMedia"), MEDIA_PAIR_KEYS)
        similar = re.search(r"similar: \{(.*?)\}", REFERO_TS, re.S).group(1)
        self.assertEqual(set(re.findall(r"(\w+)\s*:", similar)), SIMILAR_KEYS)

    def test_the_page_reads_the_emitted_doc_and_ds_keys(self):
        # DOC_TABS (web/app/refero/[slug]/page.tsx) looks each entry's key up in
        # e.docs: a key the page asks for but the builder never emits hides the
        # document, and one emitted but never read is dead payload.
        tabs = re.search(r"const DOC_TABS[^=]*= \[(.*?)\];", APP_SRC, re.S).group(1)
        self.assertEqual(set(re.findall(r'\["(\w+)"', tabs)), DOCS_KEYS)
        # interface Ds (components/ReferoDetail.tsx) names every ds field the
        # page renders; the builder ships exactly REFERO_DS_KEYS.
        m = re.search(r"interface Ds \{(.*?)^\}", WEB_SRC, re.S | re.M)
        ds_fields = set(re.findall(r"(?m)^\s*(\w+)\??:", m.group(1)))
        self.assertEqual(ds_fields, DS_KEYS)

    def test_every_media_key_the_page_reads_is_emitted(self):
        # ReferoDetail indexes e.media by its MEDIA_TABS kind and reads
        # e.media.<key> literals for the poster fallbacks; every one must be
        # an emitted media key.
        tabs = re.search(r"const MEDIA_TABS = \[(.*?)\] as const", WEB_SRC, re.S).group(1)
        tab_keys = set(re.findall(r'\["(\w+)"', tabs))
        reads = set(re.findall(r"e\.media\.(\w+)", WEB_SRC))
        self.assertEqual((tab_keys | reads) - MEDIA_KEYS, set())

    def test_media_locals_are_the_shared_path_contract(self):
        for key, (kind, _field) in catalog.REFERO_MEDIA.items():
            with self.subTest(kind=kind):
                pair = self.entity["media"][key]
                self.assertEqual(pair["local"],
                                 refero_media.local_path(kind, "alpha"))
                dest = refero_media.media_dest("/media", kind, "alpha")
                # /refero-media/<kind>/<slug><ext> == <root>/<kind>/<slug><ext>
                self.assertEqual(
                    str(dest), "/media/" + pair["local"].split("/refero-media/")[1])
        # Every mirror kind is emitted, and vice versa.
        self.assertEqual({k for k, _ in catalog.REFERO_MEDIA.values()},
                         set(refero_media.KINDS))

    def test_the_page_derives_card_media_under_the_same_kinds(self):
        # Index cards carry no media block; localMedia() builds the same
        # /refero-media/<kind>/ paths from literals, and the media route's own
        # MEDIA_KINDS is the other registry — both stay inside the mirror's.
        calls = re.findall(r"localMedia\([^)]*\)", WEB_SRC)
        literals = {w for call in calls for w in re.findall(r'"(\w+)"', call)}
        # "p"/"s" are the card-flag values inside the calls; the rest are
        # file extensions.
        literals -= {"p", "s", "jpg", "jpeg", "png", "webp", "mp4"}
        route_kinds = set(re.findall(
            r"(\w+):", re.search(r"const MEDIA_KINDS[^=]*= \{(.*?)\}", WEB_SRC, re.S).group(1)))
        self.assertEqual((literals | route_kinds) - set(refero_media.KINDS), set())

    def test_the_emitted_favicon_is_the_mirrored_file_with_no_remote(self):
        # A remote favicon-service URL would let the service see which styles are browsed.
        self.assertEqual(self.entity["media"]["favicon"],
                         {"local": refero_media.local_path("favicons", self.entity["slug"]), "remote": None})
        self.assertNotIn("gstatic", json.dumps(self.entity) + json.dumps(self.index))


class MetaCatalogContractTest(unittest.TestCase):
    """meta.json keys vs what catalog.py reads and check.py compares; the
    committed refero/catalog.json rows pinned to CATALOG_FIELDS."""

    def test_every_catalog_meta_read_is_a_key_fetch_emits(self):
        src = (TOOLS / "catalog.py").read_text()
        refero_src = src[re.search(r"^# -+ refero$", src, re.M).start():
                         re.search(r"^def build\(", src, re.M).start()]
        reads = set(re.findall(r"\bmeta\.get\(\"(\w+)\"", refero_src)) | \
            set(re.findall(r"\bmeta\[\"(\w+)\"\]", refero_src))
        self.assertEqual(reads - META_KEYS, set())

    def test_every_compared_meta_field_is_emitted(self):
        self.assertEqual(set(refero_check.META_FIELDS) - META_KEYS, set())

    def test_catalog_rows_carry_exactly_the_catalog_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            refero = Path(tmp) / "refero"
            with mock.patch.object(fetch, "REFERO", refero), \
                    mock.patch.object(fetch, "WORK", refero / ".work"), \
                    mock.patch.object(fetch, "DB", refero / "refero.db"):
                db = fetch.init_db()
                db.execute(
                    """INSERT INTO styles (uuid, slug, name, tagline, page_url,
                       source_url, theme, extracted_at, fetched_at,
                       product_type, design_style, tags)
                       VALUES ('u1','acme','Acme','tag','https://p/a',
                               'https://s.example','light','t0','t1',
                               'devtools','technical','["neon"]')""")
                db.commit()
                db.close()
                fetch.cmd_catalog()
                cat = json.loads((refero / "catalog.json").read_text())
        self.assertEqual(set(cat),
                         {"version", "about", "source", "sitemap", "count",
                          "styles"})
        self.assertEqual(cat["count"], 1)
        self.assertEqual(set(cat["styles"][0]),
                         set(refero_check.CATALOG_FIELDS)
                         | set(refero_check.CATALOG_DERIVED_FIELDS))


if __name__ == "__main__":
    unittest.main()
