"""Tests for tools/refero/classify.py: the label vocabulary helpers, the
Anthropic Messages API call (urllib.request.urlopen mocked, no network, no
key spent), the batch loop and the db and meta.json writes it drives. Every
write lands in a temporary refero/. Run with `make test`."""
import io
import json
import sqlite3
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import classify  # noqa: E402
import fetch  # noqa: E402


class Resp:
    """A urlopen response whose body is an API message holding `text`."""

    def __init__(self, text=None, body=None):
        self.body = body if body is not None else json.dumps(
            {"content": [{"type": "text", "text": text}]}).encode()

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def answer(*items):
    return Resp(json.dumps(list(items)))


def label(slug, product="devtools", style="technical", tags=()):
    return {"slug": slug, "product_type": product, "design_style": style,
            "tags": list(tags)}


def style(slug, name=None):
    return {"slug": slug, "name": name or slug.title(), "host": f"{slug}.example",
            "industry": "other", "tagline": "a tagline"}


class NormTest(unittest.TestCase):
    def test_labels_are_lowercased_and_dashed(self):
        self.assertEqual(classify.norm(" Design_Tool ", classify.PRODUCT_TYPES), "design-tool")
        self.assertEqual(classify.norm("food drink", classify.PRODUCT_TYPES), "food-drink")

    def test_unknown_or_non_string_labels_are_dropped(self):
        self.assertIsNone(classify.norm("spaceship", classify.PRODUCT_TYPES))
        self.assertIsNone(classify.norm(None, classify.PRODUCT_TYPES))
        self.assertIsNone(classify.norm(3, classify.PRODUCT_TYPES))

    def test_the_two_vocabularies_do_not_overlap(self):
        self.assertFalse(set(classify.PRODUCT_TYPES) & set(classify.DESIGN_STYLES))
        self.assertEqual(classify.VOCAB, set(classify.PRODUCT_TYPES) | set(classify.DESIGN_STYLES))

    def test_the_system_prompt_lists_every_label(self):
        for key in list(classify.PRODUCT_TYPES) + list(classify.DESIGN_STYLES):
            self.assertIn(f"- {key}:", classify.SYSTEM)


class HostOfTest(unittest.TestCase):
    def test_the_host_loses_scheme_www_and_path(self):
        self.assertEqual(classify.host_of("https://www.acme.example/pricing?x=1"), "acme.example")
        self.assertEqual(classify.host_of("acme.example"), "acme.example")
        self.assertEqual(classify.host_of("http://sub.acme.example"), "sub.acme.example")

    def test_empty_values_have_no_host(self):
        self.assertIsNone(classify.host_of(""))
        self.assertIsNone(classify.host_of(None))
        self.assertIsNone(classify.host_of(42))


class CallApiTest(unittest.TestCase):
    def setUp(self):
        for patcher in (mock.patch.object(classify.time, "sleep"),
                        mock.patch.dict(classify.os.environ, {"ANTHROPIC_API_KEY": "sk-test"})):
            patcher.start()
            self.addCleanup(patcher.stop)

    def call(self, responses, batch=None, tries=3):
        batch = batch or [style("acme"), style("beta")]
        with mock.patch.object(classify.urllib.request, "urlopen",
                               side_effect=responses) as opened:
            result = classify.call_api(batch, "test-model", tries=tries)
        return result, opened

    def test_valid_labels_come_back_per_slug(self):
        (out, missing, last), opened = self.call(
            [answer(label("acme", tags=["saas"]), label("beta", "ai", "neon"))])
        self.assertEqual(out["acme"], {"product_type": "devtools", "design_style": "technical",
                                       "tags": ["saas"]})
        self.assertEqual(out["beta"]["design_style"], "neon")
        self.assertEqual((missing, last), ([], None))
        self.assertEqual(opened.call_count, 1)

    def test_the_request_is_a_keyed_json_post_for_the_batch(self):
        _, opened = self.call([answer(label("acme"), label("beta"))])
        req = opened.call_args.args[0]
        self.assertEqual(req.full_url, classify.API)
        self.assertEqual(req.get_method(), "POST")
        self.assertEqual(req.get_header("X-api-key"), "sk-test")
        self.assertEqual(req.get_header("Anthropic-version"), "2023-06-01")
        body = json.loads(req.data)
        self.assertEqual(body["model"], "test-model")
        self.assertEqual(body["temperature"], 0)
        self.assertEqual(body["system"], classify.SYSTEM)
        sent = json.loads(body["messages"][0]["content"])
        self.assertEqual([s["slug"] for s in sent], ["acme", "beta"])
        self.assertEqual(set(sent[0]), {"slug", "name", "host", "industry", "tagline"})

    def test_a_fenced_answer_with_chatter_still_parses(self):
        text = "Here you go:\n```json\n" + json.dumps([label("acme")]) + "\n```\nDone."
        (out, missing, _), _ = self.call([Resp(text)], batch=[style("acme")])
        self.assertEqual(list(out), ["acme"])
        self.assertEqual(missing, [])

    def test_labels_are_normalised_deduplicated_and_capped(self):
        raw = label("acme", "Devtools", "Technical", tags=["Saas", "devtools", "technical", "saas", "minimal",
                                       "paper", "neon", "swiss", "bogus"])
        (out, _, _), _ = self.call([answer(raw)], batch=[style("acme")])
        # primaries and repeats and unknown words are dropped; four tags at most
        self.assertEqual(out["acme"]["tags"], ["saas", "minimal", "paper", "neon"])
        self.assertEqual(out["acme"]["product_type"], "devtools")

    def test_a_null_tags_field_means_no_tags(self):
        raw = label("acme")
        raw["tags"] = None
        (out, _, _), _ = self.call([answer(raw)], batch=[style("acme")])
        self.assertEqual(out["acme"]["tags"], [])

    def test_invalid_entries_are_skipped_and_reported_missing(self):
        items = [label("acme", product="spaceship"), label("ghost"), "junk",
                 label("beta")]
        (out, missing, last), _ = self.call([Resp(json.dumps(items))], tries=1)
        self.assertEqual(list(out), ["beta"])
        self.assertEqual(missing, ["acme"])
        self.assertIn("missing/invalid slugs: ['acme']", last)

    def test_a_retry_only_re_asks_for_the_slugs_still_missing(self):
        (out, missing, last), opened = self.call(
            [answer(label("acme")), answer(label("beta"))])
        self.assertEqual(sorted(out), ["acme", "beta"])
        self.assertEqual((missing, last), ([], "missing/invalid slugs: ['beta']"))
        second = json.loads(json.loads(opened.call_args_list[1].args[0].data)
                            ["messages"][0]["content"])
        self.assertEqual([s["slug"] for s in second], ["beta"])

    def test_http_errors_and_garbage_are_retried_then_reported(self):
        responses = [urllib.error.URLError("rate limited"), Resp("not json at all"),
                     answer(label("acme"))]
        (out, missing, _), opened = self.call(responses, batch=[style("acme")])
        self.assertEqual(list(out), ["acme"])
        self.assertEqual(missing, [])
        self.assertEqual(opened.call_count, 3)

    def test_running_out_of_tries_returns_the_last_error(self):
        err = urllib.error.URLError("rate limited")
        (out, missing, last), opened = self.call([err, err], batch=[style("acme")], tries=2)
        self.assertEqual(out, {})
        self.assertEqual(missing, ["acme"])
        self.assertIn("rate limited", last)
        self.assertEqual(opened.call_count, 2)

    def test_a_response_without_content_blocks_counts_as_a_failure(self):
        (out, missing, last), _ = self.call([Resp(body=b"{}")], batch=[style("acme")], tries=1)
        self.assertEqual((out, missing), ({}, ["acme"]))
        self.assertIsNotNone(last)


class ReferoTmp(unittest.TestCase):
    """A temporary refero/ holding a db and meta.json files."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name) / "refero"
        self.refero.mkdir()
        for mod, attrs in ((classify, {"REFERO": self.refero, "DB": self.refero / "refero.db"}),
                           (fetch, {"REFERO": self.refero, "WORK": self.refero / ".work",
                                    "DB": self.refero / "refero.db"})):
            for name, value in attrs.items():
                patcher = mock.patch.object(mod, name, value)
                patcher.start()
                self.addCleanup(patcher.stop)

    def seed(self, *slugs, labelled=()):
        """styles rows for `slugs`; those in `labelled` already have labels."""
        db = fetch.init_db()
        for slug in slugs:
            db.execute(
                "INSERT INTO styles (uuid, slug, name, tagline, page_url, source_url, "
                "fetched_at, design_system_json, product_type, design_style) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                (f"u-{slug}", slug, slug.title(), "tag", "p", f"https://www.{slug}.example/x",
                 "t0", json.dumps({"industry": "saas"}),
                 "ai" if slug in labelled else None, "neon" if slug in labelled else None))
            folder = self.refero / slug
            folder.mkdir()
            (folder / "meta.json").write_text(json.dumps({"slug": slug, "theme": "light"}))
        db.commit()
        db.close()

    def rows(self):
        db = sqlite3.connect(self.refero / "refero.db")
        try:
            return {r[0]: r[1:] for r in db.execute(
                "SELECT slug, product_type, design_style, tags FROM styles ORDER BY slug")}
        finally:
            db.close()


class InitDbTest(ReferoTmp):
    def test_label_columns_are_added_to_an_older_db(self):
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("CREATE TABLE styles (slug TEXT)")
        db.commit()
        db.close()
        db = classify.init_db()
        cols = {r[1] for r in db.execute("PRAGMA table_info(styles)")}
        db.close()
        self.assertTrue({"product_type", "design_style", "tags"} <= cols)


class ApplyAndMetaTest(ReferoTmp):
    def test_apply_writes_the_row_and_the_meta_file(self):
        self.seed("acme")
        db = classify.init_db()
        classify.apply(db, {"acme": {"product_type": "ai", "design_style": "neon",
                                     "tags": ["saas"]}})
        db.close()
        self.assertEqual(self.rows()["acme"], ("ai", "neon", '["saas"]'))
        meta = json.loads((self.refero / "acme" / "meta.json").read_text())
        self.assertEqual((meta["product_type"], meta["tags"]), ("ai", ["saas"]))

    def test_a_style_with_no_folder_is_labelled_in_the_db_only(self):
        self.seed("acme")
        (self.refero / "acme" / "meta.json").unlink()
        classify.write_meta("acme", {"product_type": "ai", "design_style": "neon", "tags": []})
        self.assertFalse((self.refero / "acme" / "meta.json").exists())

    def test_a_corrupt_meta_file_is_left_alone(self):
        self.seed("acme")
        path = self.refero / "acme" / "meta.json"
        path.write_text("{torn")
        classify.write_meta("acme", {"product_type": "ai", "design_style": "neon", "tags": []})
        self.assertEqual(path.read_text(), "{torn")

    def test_labels_go_after_theme_or_at_the_end_without_one(self):
        self.seed("acme")
        path = self.refero / "acme" / "meta.json"
        path.write_text(json.dumps({"slug": "acme"}))
        labels = {"product_type": "ai", "design_style": "neon", "tags": []}
        classify.write_meta("acme", labels)
        self.assertEqual(list(json.loads(path.read_text())),
                         ["slug", "product_type", "design_style", "tags"])

    def test_a_relabel_replaces_the_old_label_keys(self):
        self.seed("acme")
        path = self.refero / "acme" / "meta.json"
        classify.write_meta("acme", {"product_type": "ai", "design_style": "neon", "tags": ["a"]})
        classify.write_meta("acme", {"product_type": "saas", "design_style": "paper", "tags": []})
        meta = json.loads(path.read_text())
        self.assertEqual(list(meta), ["slug", "theme", "product_type", "design_style", "tags"])
        self.assertEqual(meta["product_type"], "saas")


class StatsTest(ReferoTmp):
    def test_the_distribution_counts_every_label_with_none_last(self):
        self.seed("a", "b", "c", labelled=("a", "b"))
        db = classify.init_db()
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            classify.stats(db)
        db.close()
        text = out.getvalue()
        self.assertIn("product_type:", text)
        self.assertRegex(text, r"ai\s+2")
        self.assertRegex(text, r"\(none\)\s+1")
        self.assertRegex(text, r"neon\s+2")


class LabelRunTest(ReferoTmp):
    def args(self, **kw):
        return SimpleNamespace(**{"workers": 1, "batch": 2, "limit": 0, "force": False,
                                  "model": "m", **kw})

    def run_label(self, fake, **kw):
        db = classify.init_db()
        try:
            with mock.patch.object(classify, "call_api", side_effect=fake) as api, \
                 mock.patch("sys.stdout", new_callable=io.StringIO) as out, \
                 mock.patch("sys.stderr", new_callable=io.StringIO) as err:
                classify.label(db, self.args(**kw))
        finally:
            db.close()
        return api, out.getvalue(), err.getvalue()

    @staticmethod
    def labels_all(batch, model, tries=3):
        return {s["slug"]: {"product_type": "devtools", "design_style": "minimal",
                            "tags": []} for s in batch}, [], None

    def test_unlabelled_styles_are_batched_and_written(self):
        self.seed("a", "b", "c")
        api, out, _ = self.run_label(self.labels_all)
        self.assertEqual([len(c.args[0]) for c in api.call_args_list], [2, 1])
        self.assertIn("to classify: 3 styles in 2 batches", out)
        self.assertIn("labeled 3/3; 0 left unlabeled", out)
        self.assertEqual({v[0] for v in self.rows().values()}, {"devtools"})

    def test_the_prompt_carries_host_and_industry_from_the_row(self):
        self.seed("a")
        api, _, _ = self.run_label(self.labels_all)
        sent = api.call_args.args[0][0]
        self.assertEqual((sent["host"], sent["industry"]), ("a.example", "saas"))

    def test_labelled_styles_are_skipped_unless_forced(self):
        self.seed("a", "b", labelled=("a",))
        api, out, _ = self.run_label(self.labels_all)
        self.assertEqual([s["slug"] for s in api.call_args.args[0]], ["b"])
        api, out, _ = self.run_label(self.labels_all, force=True)
        self.assertIn("to classify: 2 styles", out)

    def test_nothing_to_label_makes_no_api_call(self):
        self.seed("a", labelled=("a",))
        api, out, _ = self.run_label(self.labels_all)
        api.assert_not_called()
        self.assertIn("to classify: 0 styles in 0 batches", out)

    def test_limit_caps_the_styles(self):
        self.seed("a", "b", "c")
        api, out, _ = self.run_label(self.labels_all, limit=1)
        self.assertIn("to classify: 1 styles in 1 batches", out)

    def test_a_bad_industry_json_does_not_stop_the_run(self):
        self.seed("a")
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("UPDATE styles SET design_system_json='{torn'")
        db.commit()
        db.close()
        api, _, _ = self.run_label(self.labels_all)
        self.assertIsNone(api.call_args.args[0][0]["industry"])

    def test_dropped_slugs_get_a_second_pass_in_small_chunks(self):
        self.seed("a", "b", "c")
        calls = []

        def fake(batch, model, tries=3):
            calls.append([s["slug"] for s in batch])
            if len(calls) == 1:  # the bulk pass drops "b"
                keep = [s for s in batch if s["slug"] != "b"]
                return ({s["slug"]: {"product_type": "ai", "design_style": "neon", "tags": []}
                         for s in keep}, ["b"], "dropped")
            return self.labels_all(batch, model)

        _, out, err = self.run_label(fake, batch=3)
        self.assertEqual(calls, [["a", "b", "c"], ["b"]])
        self.assertIn("partial batch of 3: dropped", err)
        self.assertIn("labeled 3/3; 0 left unlabeled", out)
        self.assertEqual(self.rows()["b"][0], "devtools")

    def test_slugs_still_missing_after_the_retry_are_reported_not_written(self):
        self.seed("a", "b")

        def fake(batch, model, tries=3):
            return {}, [s["slug"] for s in batch], "nope"

        _, out, err = self.run_label(fake)
        self.assertIn("retry of 2 still missing 2: nope", err)
        self.assertIn("labeled 0/2; 2 left unlabeled", out)
        self.assertEqual({v[0] for v in self.rows().values()}, {None})

    def test_an_exception_in_a_batch_marks_it_failed_and_the_run_goes_on(self):
        self.seed("a", "b", "c")
        state = {"n": 0}

        def fake(batch, model, tries=3):
            state["n"] += 1
            if state["n"] == 1:
                raise RuntimeError("worker died")
            return self.labels_all(batch, model)

        _, out, err = self.run_label(fake)
        self.assertIn("partial batch of 2: worker died", err)
        self.assertIn("labeled 3/3; 0 left unlabeled", out)


class MainTest(ReferoTmp):
    def run_main(self, *argv, env=None):
        env = {"ANTHROPIC_API_KEY": "sk-test"} if env is None else env
        with mock.patch.object(sys, "argv", ["classify.py", *argv]), \
             mock.patch.dict(classify.os.environ, env, clear=False), \
             mock.patch.object(classify.refero_media, "load_env", return_value=[]), \
             mock.patch.object(classify, "label") as label_run, \
             mock.patch.object(fetch, "cmd_catalog") as catalog, \
             mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            classify.main()
        return label_run, catalog, out.getvalue()

    def test_stats_prints_the_distribution_and_does_nothing_else(self):
        self.seed("a", labelled=("a",))
        label_run, catalog, out = self.run_main("--stats")
        self.assertIn("product_type:", out)
        label_run.assert_not_called()
        catalog.assert_not_called()

    def test_a_run_labels_then_refreshes_the_catalog(self):
        self.seed("a")
        label_run, catalog, _ = self.run_main("--batch", "7", "--force")
        args = label_run.call_args.args[1]
        self.assertEqual((args.batch, args.force, args.model), (7, True, classify.MODEL))
        catalog.assert_called_once()

    def test_a_missing_key_exits_before_any_work(self):
        self.seed("a")
        with mock.patch.dict(classify.os.environ, {}, clear=True), \
             mock.patch.object(sys, "argv", ["classify.py"]), \
             mock.patch.object(classify.refero_media, "load_env", return_value=[]), \
             mock.patch.object(classify, "label") as label_run, \
             self.assertRaises(SystemExit) as exit_:
            classify.main()
        self.assertIn("ANTHROPIC_API_KEY", str(exit_.exception))
        label_run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
