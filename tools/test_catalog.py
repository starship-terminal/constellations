"""Tests for tools/catalog.py. Run with `make test`."""
import contextlib
import copy
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog  # noqa: E402


class NonAsciiTest(unittest.TestCase):
    def test_git_ignored_recognises_a_non_ascii_name(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            (root / ".gitignore").write_text("dumps/\n")
            (root / "dumps").mkdir()
            ignored, kept = root / "dumps" / "café-dark.png", root / "café-light.png"
            ignored.write_text("x")
            kept.write_text("x")
            with mock.patch.object(catalog, "ROOT", root):
                self.assertEqual(catalog.git_ignored([ignored, kept]), {ignored})

    def test_pull_request_catalogs_read_non_ascii_rows_under_an_ascii_locale(self):
        # The taxonomy and coverage --check fallbacks read the base and head catalogs
        # through `git show`; under LC_ALL=C with UTF-8 mode off that must still decode.
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git = lambda *a: subprocess.run(["git", *a], cwd=root, check=True, capture_output=True)
            git("init", "-q")
            (root / "catalog.json").write_text(json.dumps({"systems": [{"slug": "cafe", "name": "Café — Bar"}]},
                                                          ensure_ascii=False), encoding="utf-8")
            git("add", "catalog.json")
            git("-c", "user.name=t", "-c", "user.email=t@example.test", "commit", "-qm", "c")
            git("update-ref", "refs/remotes/origin/main", "HEAD")
            git("update-ref", "refs/pr-head", "HEAD")
            code = ("import sys, json; sys.path.insert(0, sys.argv[1]); import catalog; from pathlib import Path; "
                    "base, head = catalog.pull_request_catalogs(Path(sys.argv[2])); "
                    "print(json.dumps(base['cafe']['name']))")
            env = {**os.environ, "LC_ALL": "C", "LANG": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0",
                   "GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"}
            run = subprocess.run([sys.executable, "-c", code, str(Path(catalog.__file__).parent), str(root)],
                                 capture_output=True, text=True, encoding="utf-8", env=env)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(json.loads(run.stdout), "Café — Bar")

    def test_atomic_write_writes_utf8_whatever_the_locale(self):
        opened = []
        real = catalog.os.fdopen

        def fdopen(fd, mode="r", *args, **kwargs):
            opened.append(kwargs.get("encoding"))
            return real(fd, mode, *args, **kwargs)

        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(catalog.os, "fdopen", fdopen):
            path = Path(tmp) / "out.json"
            catalog.atomic_write(path, "café\n")
            self.assertEqual(path.read_bytes(), "café\n".encode("utf-8"))
        self.assertEqual(opened, ["utf-8"])


class UntestedHelpersTest(unittest.TestCase):
    """latest_scores, list_images' preview.exclude, the thumbnail cache, and repo_file's
    guard outside a git checkout."""

    def test_latest_scores_counts_grades_and_keeps_failing_contrast(self):
        criteria = {"criteria": [{"id": "F15"}, {"id": "C1"}, {"id": "V1"}]}
        audits = [{"date": "2026-01-01", "systems": [{"slug": "x", "grades": {}}]},
                  {"date": "2026-01-02", "systems": [
                      {"slug": "x", "grades": {"F15": {"grade": "partly", "evidence": "Script: 3.9:1 muted"},
                                               "C1": {"grade": "meets", "evidence": "e"},
                                               "V1": {"grade": "na", "evidence": "e"}}},
                      {"slug": "y", "grades": {"F15": {"grade": "meets", "evidence": "Script: ok"}}}]}]
        import scorecard
        with mock.patch.object(scorecard, "load", return_value=(criteria, audits)), \
                mock.patch.object(scorecard, "check", return_value=[]):
            out = catalog.latest_scores()
        self.assertEqual(out["x"]["meets"], 1)
        self.assertEqual(out["x"]["partly"], 1)
        self.assertEqual((out["x"]["applicable"], out["x"]["date"]), (2, "2026-01-02"))
        self.assertEqual(out["x"]["contrast"], "3.9:1 muted")
        self.assertIsNone(out["y"]["contrast"])

    def test_latest_scores_exits_on_malformed_audit_data(self):
        import scorecard
        with mock.patch.object(scorecard, "load", return_value=({"criteria": []}, [{"date": "d", "systems": []}])), \
                mock.patch.object(scorecard, "check", return_value=["d: a systems entry is not an object"]), \
                self.assertRaises(SystemExit) as e:
            catalog.latest_scores()
        self.assertIn("scorecard data problems", str(e.exception))

    def test_list_images_skips_excluded_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("screenshots/home.png", "screenshots/drafts/old.png", "screenshots/draftsman.png"):
                (root / "systems/x" / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / "systems/x" / rel).write_bytes(b"")
            system = {"slug": "x", "preview": {"exclude": ["drafts/"]}}
            with mock.patch.object(catalog, "ROOT", root):
                paths = [i["path"] for i in catalog.list_images(system, "screenshots", {".png"})]
        self.assertEqual(paths, ["systems/x/screenshots/draftsman.png", "systems/x/screenshots/home.png"])

    def test_a_truncated_cached_thumbnail_is_not_kept(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "s.png", Path(tmp) / "t.jpg"
            src.write_bytes(b"png")
            dst.write_bytes(b"\xff\xd8 half a jpeg")
            self.assertFalse(catalog._thumb_ok(dst))
            made = []
            with mock.patch.object(catalog, "_thumb_backend", return_value="sips"), \
                    mock.patch.object(catalog.subprocess, "run",
                                      side_effect=lambda *a, **k: made.append(a) or mock.Mock(returncode=0)):
                catalog._make_thumb(src, dst)
            self.assertEqual(len(made), 1)  # regenerated despite the newer mtime

    def test_a_complete_newer_thumbnail_short_circuits(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "s.png", Path(tmp) / "t.jpg"
            src.write_bytes(b"png")
            dst.write_bytes(b"\xff\xd8 jpeg \xff\xd9")
            self.assertTrue(catalog._thumb_ok(dst))
            with mock.patch.object(catalog, "_thumb_backend", side_effect=AssertionError("regenerated")):
                self.assertTrue(catalog._make_thumb(src, dst))

    def test_outside_a_git_checkout_only_fonts_are_refused(self):
        # Pinned as it is: a copied tree without .git serves files git would ignore.
        # Whether that should fail closed is an open decision, not this test's.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            (root / "systems/x/fonts").mkdir(parents=True)
            (root / "systems/x/dumps").mkdir(parents=True)
            with mock.patch.object(catalog, "ROOT", root):
                self.assertTrue(catalog._ignored_or_private(root / "systems/x/fonts/a.woff2"))
                self.assertFalse(catalog._ignored_or_private(root / "systems/x/dumps/page.html"))


class ResolverTest(unittest.TestCase):
    def setUp(self):
        self.res = catalog.Resolver({
            "core": {"palette": {"white": {"$value": "#ffffff"}},
                     "fontFamily": {"ui": {"$value": ["Inter", "sans-serif"]}}},
            "light": {"neutral": {"0": {"$value": "{palette.white}"}},
                      "bg": {"page": {"$value": "{neutral.0}"}},
                      "loop": {"$value": "{loop}"}},
            "app": {"canvas": {"$type": "color", "$value": {"colorSpace": "srgb",
                                                             "components": [0, 0.5, 1], "alpha": 1}}},
            "studio": {"text": {"value": "rgba(0, 0, 0, 1)", "type": "color"}},
        })

    def test_alias_resolves_in_own_set_then_core(self):
        self.assertEqual(self.res.lookup("light.bg.page"), "#ffffff")

    def test_dtcg_colour_object_becomes_hex(self):
        self.assertEqual(self.res.lookup("app.canvas"), "#0080ff")

    def test_tokens_studio_value_key(self):
        self.assertEqual(self.res.lookup("studio.text"), "rgba(0, 0, 0, 1)")

    def test_font_list_joins(self):
        self.assertEqual(self.res.lookup("core.fontFamily.ui"), "Inter, sans-serif")

    def test_missing_and_cyclic_return_none(self):
        self.assertIsNone(self.res.lookup("light.nope"))
        self.assertIsNone(self.res.lookup("light.loop"))


class PaletteCheckTest(unittest.TestCase):
    ROLES = {r: f"light.{r}" for r in catalog.SWATCH_ROLES}

    def test_complete_palette_passes(self):
        self.assertEqual(catalog.palette_problems("x", {"swatches": {"light": self.ROLES}}, ["light"]), [])

    def test_missing_swatches_fail(self):
        self.assertTrue(catalog.palette_problems("x", {}, ["light"]))
        self.assertTrue(catalog.palette_problems("x", {"swatches": {}}, ["light"]))

    def test_missing_role_fails(self):
        roles = dict(self.ROLES)
        del roles["accent"]
        problems = catalog.palette_problems("x", {"swatches": {"light": roles}}, ["light"])
        self.assertEqual(len(problems), 1)
        self.assertIn("accent", problems[0])

    def test_theme_must_be_declared(self):
        problems = catalog.palette_problems("x", {"swatches": {"dark": self.ROLES}}, ["light"])
        self.assertIn("not in themes", problems[0])


class CaptureCheckTest(unittest.TestCase):
    GOOD = {"harness": "Claude Code", "model": "Claude Opus 5.5",
            "route": "iphone-mirroring", "durationMin": None,
            "version": "1.2.3", "pr": "https://example.invalid/pr/1"}

    def test_complete_block_passes(self):
        self.assertEqual(catalog.capture_problems("x", self.GOOD), [])

    def test_optional_version_and_pr_may_be_absent(self):
        capture = {k: v for k, v in self.GOOD.items() if k in
                   ("harness", "model", "route", "durationMin")}
        self.assertEqual(catalog.capture_problems("x", capture), [])

    def test_missing_block_is_not_reported_here(self):
        self.assertEqual(catalog.capture_problems("x", None), [])
        self.assertIn("capture", catalog.REQUIRED_FIELDS)

    def test_non_object_and_empty_block_fail(self):
        self.assertTrue(catalog.capture_problems("x", "Claude Code"))
        self.assertTrue(catalog.capture_problems("x", {}))

    def test_unknown_route_fails(self):
        capture = dict(self.GOOD, route="screenshot-everything")
        problems = catalog.capture_problems("x", capture)
        self.assertIn("route", problems[0])

    def test_every_route_in_use_passes(self):
        for route in catalog.CAPTURE_ROUTES:
            self.assertEqual(catalog.capture_problems("x", dict(self.GOOD, route=route)),
                             [], route)

    def test_text_and_bool_duration_fail_null_and_number_pass(self):
        self.assertTrue(catalog.capture_problems("x", dict(self.GOOD, durationMin="one hour")))
        self.assertTrue(catalog.capture_problems("x", dict(self.GOOD, durationMin=True)))
        self.assertEqual(catalog.capture_problems("x", dict(self.GOOD, durationMin=25)), [])
        self.assertEqual(catalog.capture_problems("x", dict(self.GOOD, durationMin=None)), [])


class ThumbTest(unittest.TestCase):
    def setUp(self):
        # attach_thumbs prunes its directory: never run it against the real one.
        self._tmp = tempfile.TemporaryDirectory()
        self.enterContext(self._tmp)
        self.enterContext(mock.patch.object(catalog, "DATA", Path(self._tmp.name)))

    def test_shared_path_is_thumbnailed_once(self):
        calls = []
        original = catalog._make_thumb
        catalog._make_thumb = lambda src, dst: calls.append(src) or False
        try:
            items = [{"path": "systems/a/s.png"}, {"path": "systems/a/s.png"}, {"path": "systems/a/t.png"}]
            catalog.attach_thumbs(items)
        finally:
            catalog._make_thumb = original
        self.assertEqual(len(calls), 2)
        self.assertEqual([i["thumb"] for i in items], ["systems/a/s.png", "systems/a/s.png", "systems/a/t.png"])

    def test_fallback_to_full_size_warns_once(self):
        original = catalog._make_thumb
        catalog._make_thumb = lambda src, dst: False
        try:
            items = [{"path": "systems/a/s.png"}, {"path": "systems/a/t.png"}]
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                catalog.attach_thumbs(items)
        finally:
            catalog._make_thumb = original
        self.assertEqual(err.getvalue().count("warning:"), 1)
        self.assertIn("2 of 2 gallery thumbnails fell back to the full-size screenshot",
                      err.getvalue())
        self.assertEqual([i["thumb"] for i in items], ["systems/a/s.png", "systems/a/t.png"])

    def _warn_on_thumb_failure(self, backend):
        original_make, original_backend = catalog._make_thumb, catalog._thumb_backend
        catalog._make_thumb = lambda src, dst: False
        catalog._thumb_backend = lambda: backend
        try:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                catalog.attach_thumbs([{"path": "systems/a/s.png"}])
        finally:
            catalog._make_thumb, catalog._thumb_backend = original_make, original_backend
        return err.getvalue()

    def test_fallback_warning_names_missing_deps(self):
        err = self._warn_on_thumb_failure(None)
        self.assertIn("no `sips` on PATH and Pillow is not importable", err)
        self.assertIn("requirements-capture.txt", err)

    def test_fallback_warning_names_failed_backend(self):
        err = self._warn_on_thumb_failure("sips")
        self.assertIn("`sips` could not convert them", err)

    def test_thumb_backend_prefers_sips_else_pillow_else_none(self):
        sentinel = object()
        saved_pil = sys.modules.get("PIL", sentinel)
        original_which = shutil.which
        try:
            shutil.which = lambda name: "/usr/bin/sips"
            catalog._thumb_backend.cache_clear()
            self.assertEqual(catalog._thumb_backend(), "sips")

            shutil.which = lambda name: None
            sys.modules["PIL"] = None  # forces ImportError on `from PIL import ...`
            catalog._thumb_backend.cache_clear()
            self.assertIsNone(catalog._thumb_backend())
        finally:
            shutil.which = original_which
            if saved_pil is sentinel:
                sys.modules.pop("PIL", None)
            else:
                sys.modules["PIL"] = saved_pil
            catalog._thumb_backend.cache_clear()
        try:
            import PIL  # noqa: F401
        except ImportError:
            self.skipTest("Pillow not installed")
        shutil.which = lambda name: None
        catalog._thumb_backend.cache_clear()
        try:
            self.assertEqual(catalog._thumb_backend(), "pillow")
        finally:
            shutil.which = original_which
            catalog._thumb_backend.cache_clear()


class ExportTest(unittest.TestCase):
    TOKENS = {
        "core": {"gray": {"0": {"$value": "#ffffff"}, "9": {"$value": "#111111"}},
                 "space": {"2": {"$value": "8px"}},
                 "type": {"body": {"$value": {"fontSize": "14px"}}}},
        "light": {"text": {"primary": {"$value": "{gray.9}"}}},
        "dark": {"text": {"primary": {"$value": "{gray.0}"}}},
        "app": {"canvas": {"$value": "#000000"}},
    }

    def test_sets_split_into_base_and_themes(self):
        out = catalog.export_tokens(self.TOKENS, ["light", "dark"])
        self.assertEqual(out["base"]["--gray-0"], "#ffffff")
        self.assertEqual(out["base"]["--space-2"], "8px")
        self.assertEqual(out["base"]["--app-canvas"], "#000000")
        self.assertEqual(out["themes"]["light"], {"--text-primary": "#111111"})
        self.assertEqual(out["themes"]["dark"], {"--text-primary": "#ffffff"})
        self.assertEqual(out["skipped"], ["core.type.body"])

    def test_css_puts_first_theme_on_root_and_overrides_the_rest(self):
        css = catalog.export_css(catalog.export_tokens(self.TOKENS, ["light", "dark"]))
        root, dark = css.split('[data-theme="dark"]')
        self.assertIn("--text-primary: #111111;", root)
        self.assertIn("--text-primary: #ffffff;", dark)
        self.assertNotIn("--gray-0", dark)

    def test_core_token_aliasing_theme_colours_is_emitted_per_theme(self):
        tokens = {
            "core": {"shadow": {
                "lip": {"$value": {"offsetX": "0", "offsetY": "4px", "blur": "0", "color": "{border.default}"}},
                "flat": {"$value": {"offsetX": "0", "offsetY": "1px", "blur": "0", "color": "{gray.0}"}}},
                "gray": {"0": {"$value": "#ffffff"}}},
            "light": {"border": {"default": {"$value": "#e5e5e5"}}},
            "dark": {"border": {"default": {"$value": "#37464f"}}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--shadow-lip"], "0 4px 0 #e5e5e5")
        self.assertEqual(out["themes"]["dark"]["--shadow-lip"], "0 4px 0 #37464f")
        self.assertNotIn("--shadow-lip", out["base"])
        self.assertEqual(out["base"]["--shadow-flat"], "0 1px 0 #ffffff")
        self.assertEqual(out["skipped"], [])
        root, dark = catalog.export_css(out).split('[data-theme="dark"]')
        self.assertIn("--shadow-lip: 0 4px 0 #e5e5e5;", root)
        self.assertIn("--shadow-lip: 0 4px 0 #37464f;", dark)

    def test_shared_token_missing_from_a_theme_is_skipped_not_leaked(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}, "gone": {"$value": "{nowhere}"}},
            "light": {"focus": {"$value": "#3399ff"}},
            "dark": {"text": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertNotIn("--ring", out["themes"]["light"])
        self.assertNotIn("--ring", out["themes"]["dark"])
        self.assertEqual(out["unresolved"], ["core.ring", "core.gone"])
        self.assertEqual(out["skipped"], [])
        self.assertNotIn("--ring:", catalog.export_css(out))

    def test_broken_reference_is_unresolved_not_composite(self):
        tokens = {
            "core": {"gray": {"0": {"$value": "#ffffff"}},
                     "type": {"body": {"$value": {"fontFamily": "Inter", "fontSize": "14px"}}}},
            "light": {"text": {"$value": "{gray.missing}"},
                      "shadow": {"$value": {"offsetX": "0", "offsetY": "1px", "blur": "2px", "color": "{gray.nope}"}},
                      "ok": {"$value": "{gray.0}"}},
        }
        out = catalog.export_tokens(tokens, ["light"])
        self.assertEqual(out["unresolved"], ["light.text", "light.shadow"])
        self.assertEqual(out["skipped"], ["core.type.body"])
        self.assertEqual(out["themes"]["light"], {"--ok": "#ffffff"})
        css = catalog.export_css(out)
        self.assertIn("2 tokens not exported because a reference points at nothing: light.text, light.shadow", css)
        self.assertIn("1 composite tokens", css)
        self.assertNotIn("None", css)

    def test_unresolved_path_cannot_close_the_css_comment(self):
        out = catalog.export_tokens({"light": {"x*/y": {"$value": "{nowhere}"}}}, ["light"])
        css = catalog.export_css(out)
        self.assertEqual(out["unresolved"], ["light.x*/y"])
        self.assertEqual(css.count("*/"), css.count("/*"))

    def test_theme_own_token_wins_over_shared_core_token(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}},
            "light": {"focus": {"$value": "#000000"}, "ring": {"$value": "#ff0000"}},
            "dark": {"focus": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--ring"], "#ff0000")
        self.assertEqual(out["themes"]["dark"]["--ring"], "#ffffff")

    def test_theme_own_broken_token_is_not_replaced_by_the_shared_one(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}},
            "light": {"focus": {"$value": "#000000"}, "ring": {"$value": "{nowhere}"}},
            "dark": {"focus": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertNotIn("--ring", out["themes"]["light"])
        self.assertEqual(out["themes"]["dark"]["--ring"], "#ffffff")
        self.assertEqual(out["unresolved"], ["light.ring"])
        self.assertEqual(out["skipped"], [])

    def test_theme_token_with_the_same_css_name_wins_whatever_the_set_order(self):
        tokens = {
            "light": {"focus": {"$value": "#000000"}, "foo-bar": {"$value": "#ff0000"}},
            "dark": {"focus": {"$value": "#ffffff"}},
            "core": {"foo": {"bar": {"$value": "{focus}"}}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--foo-bar"], "#ff0000")
        self.assertEqual(out["themes"]["dark"]["--foo-bar"], "#ffffff")

    def test_shadows_that_reference_theme_colours_follow_the_theme(self):
        # A Duolingo-style button lip: a core shadow whose colour is a theme role.
        lip = lambda color: {"$type": "shadow", "$value": {"offsetX": "0px", "offsetY": "2px", "blur": "0px",
                                                            "spread": "0px", "color": color, "type": "dropShadow"}}
        tokens = {"core": {"shadow": {"lip": {"outline": lip("{border.default}"), "primary": lip("{accent.lip}")}}},
                  "light": {"border": {"default": {"$type": "color", "$value": "#e5e5e5"}},
                            "accent": {"lip": {"$type": "color", "$value": "#58a700"}}},
                  "dark": {"border": {"default": {"$type": "color", "$value": "#37464f"}},
                           "accent": {"lip": {"$type": "color", "$value": "#79b933"}}},
                  "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
                              {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}]}
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual([p for p in out["skipped"] if p.startswith("core.shadow.lip.")], [])
        light, dark = out["themes"]["light"], out["themes"]["dark"]
        names = sorted(n for n in light if n.startswith("--shadow-lip-"))
        self.assertEqual(names, ["--shadow-lip-outline", "--shadow-lip-primary"])
        self.assertEqual(sorted(n for n in dark if n.startswith("--shadow-lip-")), names)
        self.assertFalse(any(n.startswith("--shadow-lip-") for n in out["base"]))
        self.assertEqual(light["--shadow-lip-outline"], "0px 2px 0px 0px #e5e5e5")
        self.assertEqual(dark["--shadow-lip-outline"], "0px 2px 0px 0px #37464f")

    def test_every_package_exports(self):
        for s in catalog.load_catalog()["systems"]:
            out = catalog.export_tokens(json.loads((catalog.ROOT / s["tokens"]).read_text()), s["themes"])
            self.assertTrue(out["base"] or any(out["themes"].values()), s["slug"])


class CssValueTest(unittest.TestCase):
    def test_shadow_layers_with_alias_colour(self):
        res = catalog.Resolver({
            "core": {"blue": {"$value": "#2a78d6"}},
            "light": {"focus": {"$value": [
                {"color": "#ffffff", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "inset": True},
                {"color": "{blue}", "offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "0px"}]}},
        })
        self.assertEqual(catalog.css_value(res.final("light.focus")),
                         "inset 0px 0px 0px 1px #ffffff, 0px 2px 4px 0px #2a78d6")

    def test_cubic_bezier(self):
        self.assertEqual(catalog.css_value([0.2, 0, 0, 1]), "cubic-bezier(0.2, 0, 0, 1)")

    def test_font_stack_quotes_names_that_need_it(self):
        self.assertEqual(catalog.css_value(["Inter Variable", "SF Pro 2", "sans-serif"]),
                         'Inter Variable, "SF Pro 2", sans-serif')

    def test_dimension_object(self):
        self.assertEqual(catalog.css_value({"value": 4, "unit": "px"}), "4px")

    def test_typography_and_booleans_have_no_css_form(self):
        self.assertIsNone(catalog.css_value({"fontSize": "14px", "fontWeight": 400}))
        self.assertIsNone(catalog.css_value(True))

    def test_no_package_exports_python_reprs_or_bare_number_lists(self):
        bad = re.compile(r"\{'|: -?[0-9.]+, -?[0-9.]+, |\b(True|False|None)\b")
        for s in catalog.load_catalog()["systems"]:
            out = catalog.export_tokens(json.loads((catalog.ROOT / s["tokens"]).read_text()), s["themes"])
            lines = [line for line in catalog.export_css(out).splitlines() if bad.search(line)]
            self.assertEqual(lines, [], s["slug"])


class BuildExportsTest(unittest.TestCase):
    def test_writes_what_the_cli_prints_and_prunes_stale(self):
        import tempfile
        tokens = {"core": {"grey": {"$value": "#ffffff"}},
                  "light": {"text": {"primary": {"$value": "{grey}"}}},
                  "dark": {"text": {"primary": {"$value": "{grey}"}}}}
        with tempfile.TemporaryDirectory() as d:
            root, site = Path(d) / "root", Path(d) / "site"
            (root / "systems/x").mkdir(parents=True)
            (root / "systems/x/tokens.json").write_text(json.dumps(tokens))
            (site / "export").mkdir(parents=True)
            (site / "export/ghost.css").write_text("stale")
            (site / "export/ghost.json").write_text("stale")
            original_root, original_site = catalog.ROOT, catalog.DATA
            catalog.ROOT, catalog.DATA = root, site
            try:
                catalog.build_exports([{"slug": "x", "tokens": "systems/x/tokens.json",
                                        "themes": ["light", "dark"]}])
            finally:
                catalog.ROOT, catalog.DATA = original_root, original_site
            exported = catalog.export_tokens(tokens, ["light", "dark"])
            self.assertEqual((site / "export/x.css").read_text(),
                             catalog.export_css(exported) + "\n")
            self.assertEqual((site / "export/x.json").read_text(),
                             json.dumps(exported, indent=2) + "\n")
            self.assertFalse((site / "export/ghost.css").exists())
            self.assertFalse((site / "export/ghost.json").exists())


class ContrastTest(unittest.TestCase):
    TOKENS = {
        "core": {"white": {"$value": "#ffffff"}, "black": {"$value": "#000000"}},
        "light": {
            "page": {"$value": "{white}"},
            "text": {"$value": "{black}"},
            "faint": {"$value": "#cccccc"},
            "ink-50": {"$value": "rgba(0, 0, 0, 0.5)"},
            "glass": {"$value": "rgba(255, 255, 255, 0.5)"},
        },
    }

    def status(self, pairs, over=None):
        return [r["status"] for r in catalog.contrast(self.TOKENS, "light", pairs, over)]

    def test_black_on_white_is_21(self):
        self.assertEqual(catalog.contrast(self.TOKENS, "light", ["text:page"])[0]["ratio"], 21.0)

    def test_fail_and_large_text_threshold(self):
        self.assertEqual(self.status(["faint:page", "faint:page@3"]), ["fail", "fail"])
        self.assertEqual(self.status(["ink-50:page@3"]), ["pass"])

    def test_just_under_threshold_fails_and_does_not_display_as_threshold(self):
        tokens = {"light": {"page": {"$value": "#ffffff"}, "grey": {"$value": "rgb(118.7, 118.7, 118.7)"}}}
        row = catalog.contrast(tokens, "light", ["grey:page"])[0]
        self.assertEqual(row["status"], "fail")
        self.assertLess(row["ratio"], 4.5)

    def test_translucent_background_needs_a_backdrop(self):
        self.assertEqual(self.status(["text:glass"]), ["unchecked"])
        self.assertEqual(self.status(["text:glass"], over="page"), ["pass"])

    def test_missing_token(self):
        self.assertEqual(self.status(["nope:page"]), ["missing"])

    def test_parse_colour_forms(self):
        self.assertEqual(catalog.parse_colour("#fff"), (255, 255, 255, 1.0))
        self.assertEqual(catalog.parse_colour("rgba(0, 0, 0, 0.5)"), (0.0, 0.0, 0.0, 0.5))
        self.assertIsNone(catalog.parse_colour("red"))


class ScanTest(unittest.TestCase):
    def test_finds_redacted_text_and_signed_urls_without_printing_them(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "README.md").write_text("fine\nSigned in as Jane Doe\n")
            (Path(d) / "raw.json").write_text('{"u": "https://cdn/x.png?X-Amz-Signature=abc"}')
            (Path(d) / "shot.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR Jane Doe")
            hits = catalog.scan(Path(d), {"replace": [["jane\\s+doe", "i", "A User"]]})
        self.assertEqual(len(hits), 2)
        self.assertTrue(hits[0].endswith("README.md:2: redaction pattern 1"))
        self.assertTrue(hits[1].endswith("raw.json:1: signed URL"))
        self.assertFalse(any("Jane" in h for h in hits))

    def test_reads_every_text_file_whatever_its_extension(self):
        import tempfile
        names = ["view.tsx", "app.ts", "row.jsx", "run.sh", "Main.swift", "layout.xml", "Info.plist",
                 "pyproject.toml", "Makefile", "notes", "dump.har", "page.HTM"]
        with tempfile.TemporaryDirectory() as d:
            for n in names:
                (Path(d) / n).write_text("x\nJane Doe\n")
            (Path(d) / "font.woff2").write_bytes(b"wOF2\x00\x01Jane Doe")     # binary: skipped
            (Path(d) / ".git").mkdir()
            (Path(d) / ".git" / "COMMIT_EDITMSG").write_text("Jane Doe")      # git's own files: skipped
            hits = catalog.scan(Path(d), {"replace": [["jane\\s+doe", "i", "A User"]]})
        self.assertEqual(sorted(Path(h.split(":")[0]).name for h in hits), sorted(names))
        self.assertTrue(all(h.endswith(":2: redaction pattern 1") for h in hits))


class RedactionLoaderTest(unittest.TestCase):
    def test_one_loader_for_scan_and_redact_images(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.json", Path(d) / "b.json"
            a.write_text(json.dumps({"replace": [["Jane\\s+Doe", "g", "x"], ["a(b", "i", "x"]], "email_allow": ["^me@x\\.test$"]}))
            b.write_text(json.dumps({"replace": [["secret", "gi"]]}))           # a two-item row
            red = catalog.read_redaction([a, b])
            self.assertEqual(len(red["replace"]), 3)
            self.assertEqual(red["email_allow"], ["^me@x\\.test$"])
            pats = catalog.redaction_patterns(red)
            self.assertTrue(pats[0].search("Jane Doe") and not pats[0].search("JANE DOE"))   # flags honoured
            self.assertTrue(pats[1].search("xA(Bx"))                                           # invalid: literal
            self.assertTrue(pats[2].search("SECRET"))
            self.assertTrue(catalog.redaction_patterns(red, ignorecase=True)[0].search("JANE DOE"))
            (Path(d) / "pkg").mkdir()
            (Path(d) / "pkg" / "n.md").write_text("a(b and Secret\n")
            hits = catalog.scan(Path(d) / "pkg", red)                # a bad regex no longer crashes scan
            self.assertEqual(sorted(h.rsplit(" ", 1)[1] for h in hits), ["2", "3"])


class BadRedactionFileTest(unittest.TestCase):
    """A bad --redact file is a one-line usage error (exit 2), never a traceback or exit 1."""

    def run_scan(self, redact):
        import subprocess
        import sys
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "pkg").mkdir()
            (Path(d) / "pkg" / "n.md").write_text("hello\n")
            return subprocess.run([sys.executable, str(Path(catalog.__file__)), "scan", str(Path(d) / "pkg"),
                                   "--redact", str(redact(d))], capture_output=True, text=True)

    def assert_one_line_error(self, r, *words):
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertEqual(r.stdout, "")
        self.assertEqual(len(r.stderr.strip().splitlines()), 1, r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        for w in words:
            self.assertIn(w, r.stderr)

    def test_missing_file(self):
        r = self.run_scan(lambda d: Path(d) / "does-not-exist.json")
        self.assert_one_line_error(r, "does-not-exist.json", "not found")

    def test_not_json(self):
        def bad(d):
            f = Path(d) / "bad.txt"
            f.write_text("notjson\n")
            return f
        self.assert_one_line_error(self.run_scan(bad), "bad.txt", "not valid JSON")

    def test_wrong_shape(self):
        for body, word in [("[1, 2]", "JSON object"), ('{"replace": "x"}', "replace"),
                           ('{"replace": [["a"], 5]}', "replace"), ('{"email_allow": [1]}', "email_allow")]:
            def bad(d, body=body):
                f = Path(d) / "shape.json"
                f.write_text(body)
                return f
            self.assert_one_line_error(self.run_scan(bad), "shape.json", "wrong shape", word)

    def test_a_directory_is_an_error_too(self):
        self.assert_one_line_error(self.run_scan(lambda d: d), "cannot be read")

    def test_valid_file_still_scans(self):
        def good(d):
            f = Path(d) / "ok.json"
            f.write_text(json.dumps({"replace": [["hello", "i", "x"]]}))
            return f
        r = self.run_scan(good)
        self.assertEqual(r.returncode, 1)                       # a hit is still exit 1
        self.assertIn("redaction pattern 1", r.stdout)


class ScanFailsLoudlyTest(unittest.TestCase):
    def test_missing_or_empty_folder_is_an_error_not_clean(self):
        import tempfile
        with self.assertRaises(SystemExit):
            catalog.scan(Path("/no/such/folder"), {"replace": []})
        with tempfile.TemporaryDirectory() as d, self.assertRaises(SystemExit):
            catalog.scan(Path(d), {"replace": []})


class FindTest(unittest.TestCase):
    def test_tag_hit_outranks_description_hit(self):
        hits = catalog.find(["ios"])
        tagged = [h["slug"] for h in hits if "ios" in h.get("tags", [])]
        self.assertTrue(tagged)
        self.assertEqual([h["slug"] for h in hits[:len(tagged)]], tagged)

    def test_no_words_lists_everything(self):
        self.assertEqual(len(catalog.find([])), len(catalog.load_catalog()["systems"]))


class DesignMdValueTest(unittest.TestCase):
    def test_dimensions_become_px_rem_or_em(self):
        self.assertEqual(catalog.md_dimension(16), "16px")
        self.assertEqual(catalog.md_dimension("0"), "0px")
        self.assertEqual(catalog.md_dimension(".125rem"), "0.125rem")
        self.assertEqual(catalog.md_dimension({"value": 4, "unit": "px"}), "4px")
        self.assertEqual(catalog.md_dimension("-0.25rem"), "-0.25rem")
        self.assertIsNone(catalog.md_dimension("50%"))
        self.assertIsNone(catalog.md_dimension("auto"))
        self.assertIsNone(catalog.md_dimension("12pt"))
        self.assertEqual(catalog.md_dimension("-2%", percent_as_em=True), "-0.02em")

    def test_line_height_percent_is_a_multiplier(self):
        self.assertEqual(catalog.md_line_height("140%"), 1.4)
        self.assertEqual(catalog.md_line_height(1.25), 1.25)
        self.assertEqual(catalog.md_line_height("1.5"), 1.5)
        self.assertEqual(catalog.md_line_height("24px"), "24px")
        self.assertIsNone(catalog.md_line_height("normal"))

    def test_font_weight_and_family(self):
        self.assertEqual(catalog.md_font_weight("450"), 450)
        self.assertEqual(catalog.md_font_weight("Semi-Bold"), 600)
        self.assertIsNone(catalog.md_font_weight("heavier"))
        self.assertEqual(catalog.first_family(["Inter Variable", "sans-serif"]), "Inter Variable")
        self.assertEqual(catalog.first_family("'Gauth Home', Georgia, serif"), "Gauth Home")

    def test_colours_the_linter_accepts(self):
        self.assertEqual(catalog.md_colour("#0000001a"), "#0000001a")
        self.assertEqual(catalog.md_colour("rgba(0, 0, 0, 0.5)"), "rgba(0, 0, 0, 0.5)")
        self.assertEqual(catalog.md_colour("transparent"), "transparent")
        self.assertIsNone(catalog.md_colour("currentColor"))
        self.assertIsNone(catalog.md_colour("linear-gradient(#fff, #000)"))

    def test_yaml_quotes_keys_that_would_not_stay_strings(self):
        lines = catalog.to_yaml({"spacing": {"2": "8px", "on": "1px", "sm": "4px"},
                                 "omitted": [{"section": "rounded", "reason": "none"}]})
        self.assertIn('  "2": "8px"', lines)
        self.assertIn('  "on": "1px"', lines)
        self.assertIn('  sm: "4px"', lines)
        self.assertIn('  - section: "rounded"', lines)
        self.assertIn('    reason: "none"', lines)


class DesignMdMappingTest(unittest.TestCase):
    TOKENS = {
        "core": {
            "palette": {"green": {"$value": "#29cc57"}, "white": {"$value": "#ffffff"}},
            "fontFamily": {"ui": {"$value": ["CoFo Brilliant", "sans-serif"]}},
            "typography": {"heading": {"large": {"$type": "typography", "$value": {
                "fontFamily": "{fontFamily.ui}", "fontSize": "28px", "fontWeight": "bold",
                "lineHeight": "140%", "letterSpacing": "0px", "textCase": "uppercase"}}}},
            "radius": {"md": {"$value": "8px"}, "circle": {"$value": "50%"}},
            "spacing": {"0.5": {"$value": ".125rem"}, "4": {"$value": "1rem"}},
        },
        "light": {
            "bg": {"page": {"$value": "{palette.white}"}, "card": {"$value": "#f8f8f8"}},
            "text": {"primary": {"$value": "#000000"}, "muted": {"$value": "#00000099"}},
            "border": {"default": {"$value": "#0000001a"}},
            "accent": {"$value": "{palette.green}"},
            "gradient": {"hero": {"$value": "linear-gradient(#fff, #000)"}},
            "shadow": {"card": {"$type": "shadow", "$value": {
                "color": "#0000001a", "offsetX": "0px", "offsetY": "4px", "blur": "8px", "spread": "0px"}}},
            "component": {"button": {"primary-bg": {"$value": "{accent}"},
                                     "primary-text": {"$value": "#ffffff"},
                                     "primary-hover": {"$value": "#15b441"},
                                     "primary-radius": {"$value": "12px"}}},
        },
        "dark": {"bg": {"page": {"$value": "#000000"}}},
    }
    SYSTEM = {"slug": "x", "name": "X", "goodFor": "Testing", "themes": ["light", "dark"],
              "tokens": "systems/x/tokens.json",
              "preview": {"swatches": {"light": {
                  "page": "light.bg.page", "surface": "light.bg.card", "text": "light.text.primary",
                  "muted": "light.text.muted", "accent": "light.accent", "border": "light.border.default"}}}}

    def setUp(self):
        self.out = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(self.TOKENS))
        self.front = self.out["front"]

    def test_roles_come_from_the_swatches_with_aliases_resolved(self):
        colors = self.front["colors"]
        self.assertEqual(colors["primary"], "#29cc57")
        self.assertEqual(colors["neutral"], "#ffffff")
        self.assertEqual(colors["on-surface-variant"], "#00000099")
        self.assertEqual(self.out["roleFrom"]["primary"], "light.accent")

    def test_every_light_colour_is_named_by_its_path_and_dark_is_left_out(self):
        colors = self.front["colors"]
        self.assertEqual(colors["bg-page"], "#ffffff")
        self.assertEqual(colors["component-button-primary-bg"], "#29cc57")
        self.assertNotIn("#000000", [v for k, v in colors.items() if k.startswith("bg-")])
        self.assertIn("light.gradient.hero", self.out["skipped"])

    def test_typography_from_core_converted(self):
        self.assertEqual(self.front["typography"]["heading-large"], {
            "fontFamily": "CoFo Brilliant", "fontSize": "28px", "fontWeight": 700,
            "lineHeight": 1.4, "letterSpacing": "0px"})

    def test_scales_drop_what_has_no_px_rem_or_em_form(self):
        self.assertEqual(self.front["rounded"], {"md": "8px"})
        self.assertIn("core.radius.circle", self.out["skipped"])
        self.assertEqual(self.front["spacing"], {"0-5": "0.125rem", "4": "1rem"})
        self.assertNotIn("omitted", self.front)

    def test_components_keep_only_properties_design_md_defines(self):
        self.assertEqual(self.front["components"], {"button-primary": {
            "backgroundColor": "{colors.component-button-primary-bg}",
            "textColor": "{colors.component-button-primary-text}",
            "rounded": "12px"}})

    def test_shadows_go_to_the_body(self):
        self.assertEqual(self.out["shadows"], [("light.shadow.card", "0px 4px 8px 0px #0000001a")])

    def test_shared_core_shadow_resolves_against_the_theme(self):
        tokens = json.loads(json.dumps(self.TOKENS))
        tokens["core"]["shadow"] = {"lip": {"$type": "shadow", "$value": {
            "color": "{border.default}", "offsetX": "0px", "offsetY": "2px", "blur": "0px", "spread": "0px"}}}
        shadows = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(tokens))["shadows"]
        self.assertIn(("core.shadow.lip", "0px 2px 0px 0px #0000001a"), shadows)

    def test_missing_group_is_listed_as_omitted(self):
        tokens = json.loads(json.dumps(self.TOKENS))
        del tokens["core"]["radius"]
        front = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(tokens))["front"]
        self.assertEqual([o["section"] for o in front["omitted"]], ["rounded"])
        self.assertNotIn("rounded", front)

    def test_override_reads_split_typography_and_keeps_token_names(self):
        tokens = {"light": {
            "color": {"color-bg": {"value": "#f1f1f1"}, "color-text": {"value": "#303030"}},
            "space": {"space-100": {"value": "0.25rem"}},
            "text": {"text-body-md-font-family": {"value": "'Inter', sans-serif"},
                     "text-body-md-font-size": {"value": "0.8125rem"},
                     "text-body-md-font-weight": {"value": "450"},
                     "text-body-md-font-line-height": {"value": "1.25rem"}}}}
        roles = {r: "light.color.color-bg" for r in catalog.SWATCH_ROLES}
        system = {**self.SYSTEM, "themes": ["light"], "preview": {"swatches": {"light": roles}},
                  "designMd": {"colors": "light.color.", "typography": "light.text.text-",
                               "spacing": "light.space."}}
        front = catalog.design_md_tokens(system, catalog.Resolver(tokens))["front"]
        self.assertEqual(front["colors"]["color-text"], "#303030")
        self.assertEqual(front["spacing"], {"space-100": "0.25rem"})
        self.assertEqual(front["typography"], {"text-body-md": {
            "fontFamily": "Inter", "fontSize": "0.8125rem", "fontWeight": 450, "lineHeight": "1.25rem"}})


class DesignMdThemeTest(unittest.TestCase):
    """design_md_theme(): the theme DESIGN.md exports."""

    def system(self, themes, swatches, **extra):
        return {"themes": themes, "preview": {"swatches": {t: {} for t in swatches}}, **extra}

    def test_light_is_preferred_without_a_default(self):
        self.assertEqual(catalog.design_md_theme(self.system(["dark", "light"], ["dark", "light"])), "light")

    def test_default_theme_wins_over_the_light_preference(self):
        self.assertEqual(catalog.design_md_theme(
            self.system(["dark", "light"], ["dark", "light"], defaultTheme="dark")), "dark")

    def test_default_theme_without_a_swatch_set_falls_back_to_one(self):
        self.assertEqual(catalog.design_md_theme(
            self.system(["dark", "light"], ["light"], defaultTheme="dark")), "light")


class DesignMdDocumentTest(unittest.TestCase):
    SECTIONS = ["Overview", "Colors", "Typography", "Layout", "Elevation & Depth", "Shapes",
                "Components", "Do's and Don'ts"]

    def test_readme_parts_demote_headings_and_drop_intro_tables(self):
        intro, parts = catalog.readme_parts(
            "# T\n\nIntro.\n\n| a | b |\n|---|---|\n\n## Fonts\n\n### Sans\n\n```bash\n# comment\n```\n")
        self.assertEqual(intro, "Intro.")
        self.assertEqual(parts, [("Fonts", "#### Sans\n\n```bash\n# comment\n```")])

    def test_readme_do_and_dont_list_goes_under_dos_and_donts(self):
        _, parts = catalog.readme_parts("# T\n\n## Do and don't\n\n1. **Do one thing.**\n")
        self.assertEqual(catalog._readme_for("Do's and Don'ts", parts),
                         "### Do and don't (from README.md)\n\n1. **Do one thing.**")

    def test_every_package_has_the_spec_sections_in_order_and_points_at_its_tokens(self):
        for s in catalog.load_catalog()["systems"]:
            with self.subTest(s["slug"]):
                text = catalog.design_md(s)
                front, body = text.split("\n---\n", 1)
                self.assertTrue(front.startswith("---\n# Generated by tools/catalog.py"))
                self.assertIn('version: "alpha"', front)
                self.assertIn("primary:", front)
                headings = re.findall(r"^## (.+)$", body, re.M)
                self.assertEqual(headings, self.SECTIONS)
                tokens_rel = Path(s["tokens"]).relative_to(f"systems/{s['slug']}").as_posix()
                self.assertIn(f"[{tokens_rel}]({tokens_rel}) is the source of truth", body)
                self.assertNotIn("—", text.split("## Overview")[0])

    def test_stale_or_missing_file_is_a_problem(self):
        import tempfile
        system = catalog.load_catalog()["systems"][0]
        original = catalog.design_md_path
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "DESIGN.md"
            catalog.design_md_path = lambda s: target
            try:
                self.assertIn("missing", catalog.design_md_problems(system)[0])
                target.write_text("hand edited\n")
                self.assertIn("out of date", catalog.design_md_problems(system)[0])
                target.write_text(catalog.design_md(system))
                self.assertEqual(catalog.design_md_problems(system), [])
            finally:
                catalog.design_md_path = original

    def test_missing_readme_is_reported_not_raised(self):
        system = {**catalog.load_catalog()["systems"][0], "slug": "no-such-package"}
        problems = catalog.design_md_problems(system)
        self.assertEqual(len(problems), 1)
        self.assertIn("cannot generate DESIGN.md without systems/no-such-package/README.md", problems[0])

    def test_incomplete_palette_or_themes_is_reported_not_raised(self):
        base = catalog.load_catalog()["systems"][0]
        roles = dict(next(iter(base["preview"]["swatches"].values())))
        del roles["accent"]
        broken = [
            {**base, "preview": {**base["preview"], "swatches": {base["themes"][0]: roles}}},
            {**base, "preview": {**base["preview"], "swatches": {}}},
            {**base, "themes": []},
        ]
        for system in broken:
            problems = catalog.design_md_problems(system)
            self.assertEqual(len(problems), 1)
            self.assertIn("cannot generate DESIGN.md until themes and preview.swatches are complete", problems[0])

    def test_generation_error_is_reported_not_raised(self):
        from unittest import mock
        system = catalog.load_catalog()["systems"][0]
        with mock.patch.object(catalog, "design_md", side_effect=KeyError("page")):
            problems = catalog.design_md_problems(system)
        self.assertEqual(problems, [f"{system['slug']}: DESIGN.md generation failed: KeyError: 'page'"])

    def test_malformed_override_is_reported_not_raised(self):
        base = catalog.load_catalog()["systems"][0]
        for bad in ({"spacing": None}, {"spacing": [7]}, {"spacing": []}, {"spacing": ""}):
            problems = catalog.design_md_problems({**base, "designMd": bad})
            self.assertEqual(problems, [f"{base['slug']}: designMd.spacing must be a prefix string "
                                        "or a non-empty list of them"], bad)
        self.assertIn("must be an object", catalog.design_md_problems({**base, "designMd": ["x"]})[0])

    def test_bad_override_prefix_is_a_problem(self):
        system = {**catalog.load_catalog()["systems"][0], "designMd": {"spacing": "core.nope."}}
        self.assertIn("matches no token", catalog.design_md_problems(system)[0])


class DesignMdLintTest(unittest.TestCase):
    """lint_design_md's pass/fail rules, with the linter replaced by canned output."""

    def lint(self, stdout, stderr=""):
        from unittest import mock
        done = mock.Mock(stdout=stdout, stderr=stderr)
        path = catalog.ROOT / "systems" / "duolingo" / "DESIGN.md"
        with mock.patch.object(catalog.shutil, "which", return_value="/usr/bin/npx"), \
                mock.patch.object(catalog.subprocess, "run", return_value=done) as run:
            problems, counts = catalog.lint_design_md([path])
        self.assertIn(catalog.DESIGN_MD_LINTER, run.call_args.args[0])
        return problems, counts["systems/duolingo/DESIGN.md"] if counts else None

    @staticmethod
    def report(*findings):
        return json.dumps({"findings": [dict(zip(("severity", "rule", "message"), f)) for f in findings]})

    def test_clean_and_info_only(self):
        self.assertEqual(self.lint(self.report(("info", "token-summary", "3 colors"))), ([], {}))

    def test_allowed_warnings_are_counted_not_failed(self):
        problems, tally = self.lint(self.report(("warning", "orphaned-tokens", "a"), ("warning", "orphaned-tokens", "b"),
                                                ("warning", "contrast-ratio", "c")))
        self.assertEqual(problems, [])
        self.assertEqual(tally, {"orphaned-tokens warning": 2, "contrast-ratio warning": 1})

    def test_other_warnings_and_errors_fail(self):
        problems, _ = self.lint(self.report(("warning", "section-order", "out of order"),
                                            ("error", "broken-ref", "no such token")))
        self.assertEqual(len(problems), 2)
        self.assertIn("section-order", problems[0])
        self.assertIn("broken-ref", problems[1])

    def test_error_without_a_rule_fails_even_in_an_allowed_rule_list(self):
        problems, tally = self.lint(json.dumps({"findings": [{"severity": "error", "message": "bad colour"}]}))
        self.assertEqual(tally, {"parse error": 1})
        self.assertIn("error parse", problems[0])

    def test_unreadable_output_fails(self):
        problems, tally = self.lint("npm ERR! network", stderr="npm ERR! 404")
        self.assertIsNone(tally)
        self.assertIn("linter failed: npm ERR! 404", problems[0])

    def test_no_npx_is_a_clear_exit(self):
        from unittest import mock
        with mock.patch.object(catalog.shutil, "which", return_value=None), self.assertRaises(SystemExit):
            catalog.lint_design_md([])


class LayoutTest(unittest.TestCase):
    """layout_problems against a package folder built in a temporary repository."""

    def problems(self, entries, readme_rows, gaps=None):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "systems" / "x"
            folder.mkdir(parents=True)
            for entry in entries:
                if entry.endswith("/"):
                    (folder / entry).mkdir()
                else:
                    (folder / entry).write_text("")
            rows = "\n".join(f"| [{r}]({r}) | what it is |" for r in readme_rows)
            (folder / "README.md").write_text(f"# X\n\n| File | What |\n|---|---|\n{rows}\n\n## Fonts\n")
            system = {"slug": "x"} | ({"layoutGaps": gaps} if gaps is not None else {})
            with mock.patch.object(catalog, "ROOT", Path(tmp)):
                return catalog.layout_problems(system)

    FULL = [p for p in catalog.STANDARD_PARTS if p != "README.md"]

    def test_a_full_listed_package_is_clean(self):
        self.assertEqual(self.problems(self.FULL, self.FULL), [])

    def test_an_undeclared_missing_part_fails(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertEqual(self.problems(parts, parts), ["x: no icons/; add it, or declare it under layoutGaps with the reason"])

    def test_a_declared_gap_passes_and_a_stale_one_fails(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertEqual(self.problems(parts, parts, {"icons/": "rights"}), [])
        self.assertIn("layoutGaps declares raw/", self.problems(self.FULL, self.FULL, {"raw/": "gone"})[0])

    def test_a_gap_needs_a_reason(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertIn("reason", self.problems(parts, parts, {"icons/": ""})[0])

    def test_a_file_where_a_folder_belongs_counts_as_missing(self):
        parts = [p for p in self.FULL if p != "raw/"] + ["raw"]
        self.assertIn("x: no raw/; add it", self.problems(parts, parts)[0])

    def test_what_git_ignores_is_not_part_of_the_package(self):
        import subprocess
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("systems/*/fonts/\nsystems/*/raw/\n")
            folder = root / "systems" / "x"
            folder.mkdir(parents=True)
            for entry in self.FULL + ["fonts/"]:
                (folder / entry).mkdir() if entry.endswith("/") else (folder / entry).write_text("")
            rows = "\n".join(f"| [{r}]({r}) | what it is |" for r in self.FULL)
            (folder / "README.md").write_text(f"# X\n\n| File | What |\n|---|---|\n{rows}\n")
            with mock.patch.object(catalog, "ROOT", root):
                missing, unlisted = catalog.layout_gaps("x")
        self.assertEqual(unlisted, [])
        self.assertEqual(missing, ["raw/"])

    def test_an_extra_entry_needs_a_row(self):
        self.assertEqual(self.problems(self.FULL + ["graph.md"], self.FULL),
                         ["x: graph.md has no row in the README's file table"])
        self.assertEqual(self.problems(self.FULL + ["graph.md"], self.FULL + ["graph.md"]), [])


class SectionDataTest(unittest.TestCase):
    """The gallery's per-section data matches DESIGN.md and the catalog."""

    def system(self, slug):
        return next(s for s in catalog.load_catalog()["systems"] if s["slug"] == slug)

    def test_scales_match_design_md(self):
        for s in catalog.load_catalog()["systems"]:
            with self.subTest(slug=s["slug"]):
                data, md = catalog.section_data(s), catalog.design_md_tokens(s)
                front = md["front"]
                self.assertEqual(data["tokenTheme"], md["theme"])
                self.assertEqual([t["name"] for t in data["typeStyles"]], list(front.get("typography", {})))
                self.assertEqual({r["name"]: r["value"] for r in data["radii"]}, front.get("rounded", {}))
                self.assertEqual({r["name"]: r["value"] for r in data["spacing"]}, front.get("spacing", {}))
                self.assertEqual([(x["token"], x["css"]) for x in data["shadows"]], md["shadows"])
                self.assertEqual(data["layoutGaps"], s.get("layoutGaps", {}))

    def test_type_style_fields(self):
        style = catalog.section_data(self.system("claude"))["typeStyles"][0]
        self.assertEqual(set(style), {"name", "family", "size", "weight", "lineHeight", "letterSpacing"})
        self.assertTrue(style["size"].endswith("px"))

    def test_icons_are_capped_sorted_images_with_a_total(self):
        icons = catalog.section_data(self.system("polaris"))["icons"]
        self.assertGreater(icons["total"], catalog.ICON_LIMIT)
        self.assertEqual(len(icons["items"]), catalog.ICON_LIMIT)
        self.assertEqual(icons["items"], sorted(icons["items"]))
        self.assertTrue(all(p.startswith("systems/polaris/icons/") and p.endswith(".svg") for p in icons["items"]))

    def test_missing_parts_carry_their_reason(self):
        hevy = catalog.section_data(self.system("hevy"))
        self.assertEqual(hevy["icons"], {"total": 0, "items": []})
        self.assertIn("icons/", hevy["layoutGaps"])
        self.assertEqual(hevy["shadows"], [])

    def test_omitted_scale_gives_the_generator_reason(self):
        s = copy.deepcopy(self.system("hevy"))
        s["designMd"] = {"spacing": "core.nothing-here."}
        data = catalog.section_data(s)
        self.assertEqual(data["spacing"], [])
        self.assertIn("spacing", data["omitted"]["spacing"])


class ReferoBuildTest(unittest.TestCase):
    """build_refero emits refero/index.json plus one refero/style/<slug>.json per
    style, from a refero/ tree built in a temporary repository."""

    MEDIA_BASE = "https://media.example.test"

    def setUp(self):
        # media_base() reads DESIGN_SYSTEMS_MEDIA_BASE, loading it from the repo's .env
        # into os.environ for the rest of the process. Pin it, and keep the .env out.
        patches = [mock.patch.dict(catalog.os.environ, {"DESIGN_SYSTEMS_MEDIA_BASE": self.MEDIA_BASE}),
                   mock.patch.object(catalog.refero_media, "load_env", lambda *a, **k: None)]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def test_the_index_and_styles_carry_the_configured_media_base(self):
        index, styles = self.build([("alpha", self.ALPHA, {})])
        self.assertEqual(index["mediaBase"], self.MEDIA_BASE)
        self.assertEqual(styles["alpha"]["mediaBase"], self.MEDIA_BASE)

    def make(self, root, slug, meta, ds, docs=True):
        folder = root / "refero" / slug
        folder.mkdir(parents=True)
        (folder / "meta.json").write_text(json.dumps(meta))
        if ds is not None:
            (folder / "design-system.json").write_text(json.dumps(ds))
        if docs:
            (folder / "DESIGN.md").write_text("# Designed\n")
            (folder / "variables.css").write_text(":root {}")
            (folder / "theme.css").write_text("body {}")
            (folder / "tokens.json").write_text("{}")
        return folder

    def build(self, styles):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "web" / "data"
            for slug, meta, ds in styles:
                self.make(root, slug, meta, ds)
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "DATA", site):
                out = catalog.build_refero()
            return json.loads(out.read_text()), {
                p.stem: json.loads(p.read_text()) for p in site.glob("refero/style/*.json")}

    ALPHA = {"slug": "alpha", "name": "Alpha", "tagline": "tag", "theme": "light",
             "product_type": "devtools", "design_style": "technical", "tags": ["neon"],
             "source_url": "https://www.alpha.example.com/x", "page_url": "https://p/alpha",
             "extracted_at": "t0", "screenshot_url": "https://img/shot.jpg",
             "video_url": "https://img/v.mp4", "video_poster_url": "https://img/p.jpg",
             "video_detail_url": "https://img/d.mp4",
             "video_detail_poster_url": "https://img/dp.jpg"}
    ALPHA_DS = {"meta": {"thumbnailUrl": "https://img/t.jpg"}, "industry": "media",
                "description": "d", "colors": [], "components": {"x": 1},
                "northStar": "north", "customSections": [],
                "similar": [{"business": "Beta", "why": "same"}, {"business": "Nobody", "why": "none"}]}
    BETA = {"slug": "beta", "name": "beta", "source_url": "https://beta.io"}
    BETA_DS = {"industry": "other"}

    def test_index_rows_and_name_sort(self):
        index, _ = self.build([("beta", self.BETA, self.BETA_DS), ("alpha", self.ALPHA, self.ALPHA_DS)])
        self.assertEqual(index["version"], 2)
        self.assertEqual(index["cdn"], catalog.REFERO_CDN)
        self.assertEqual(len(index["styles"]), 2)
        alpha, beta = index["styles"]
        self.assertEqual([s["slug"] for s in index["styles"]], ["alpha", "beta"])
        self.assertEqual(alpha["src"], "alpha.example.com")
        self.assertEqual(alpha["card"], "p")
        self.assertEqual(alpha["cardRemote"], "https://img/p.jpg")
        self.assertTrue(alpha["video"])
        self.assertEqual(alpha["videoRemote"], "https://img/v.mp4")
        self.assertNotIn("videoSrc", alpha)
        self.assertEqual(beta["industry"], "other")
        self.assertEqual(alpha["type"], "devtools")
        self.assertEqual(alpha["style"], "technical")
        self.assertEqual(alpha["tags"], ["neon"])
        self.assertIsNone(beta["type"])
        self.assertEqual(beta["tags"], [])
        self.assertIsNone(beta["card"])
        self.assertIsNone(beta["cardRemote"])
        self.assertFalse(beta["video"])

    def test_card_remote_falls_back_to_thumbnail_then_shot(self):
        meta = {**self.BETA, "screenshot_url": "https://img/s.jpg"}
        index, _ = self.build([("beta", meta, {"meta": {"thumbnailUrl": "https://img/t.jpg"}})])
        self.assertEqual(index["styles"][0]["card"], "s")
        self.assertEqual(index["styles"][0]["cardRemote"], "https://img/t.jpg")

    def test_cdn_urls_emit_suffixes(self):
        cdn = catalog.REFERO_CDN
        meta = {**self.BETA, "screenshot_url": f"{cdn}image/s.jpg",
                "video_url": f"{cdn}video/v.mp4", "video_poster_url": f"{cdn}image/p.jpg"}
        index, _ = self.build([("beta", meta, self.BETA_DS)])
        row = index["styles"][0]
        self.assertEqual(row["card"], "p")
        self.assertEqual(row["cardRemote"], "image/p.jpg")
        self.assertEqual(row["videoRemote"], "video/v.mp4")

    def test_entry_file_media_docs_ds_and_similar(self):
        _, files = self.build([("beta", self.BETA, self.BETA_DS), ("alpha", self.ALPHA, self.ALPHA_DS)])
        alpha = files["alpha"]
        self.assertEqual(alpha["theme"], "light")
        self.assertEqual(alpha["industry"], "media")
        self.assertEqual(alpha["type"], "devtools")
        self.assertEqual(alpha["style"], "technical")
        self.assertEqual(alpha["source_url"], "https://www.alpha.example.com/x")
        self.assertEqual(alpha["media"]["shot"],
                         {"local": "/refero-media/shots/alpha.jpg", "remote": "https://img/shot.jpg"})
        self.assertEqual(alpha["media"]["video"]["remote"], "https://img/v.mp4")
        self.assertEqual(alpha["media"]["detail"]["remote"], "https://img/d.mp4")
        self.assertEqual(alpha["media"]["detail_poster"],
                         {"local": "/refero-media/detail-posters/alpha.jpg",
                          "remote": "https://img/dp.jpg"})
        # No favicon-service remote: only the file the host-side mirror fetched.
        self.assertEqual(alpha["media"]["favicon"], {"local": "/refero-media/favicons/alpha.png", "remote": None})
        self.assertEqual(alpha["docs"]["design_md"], "# Designed\n")
        self.assertEqual(alpha["docs"]["tokens_json"], "{}")
        # `ds` carries only what the page renders; the rest of the upstream
        # design-system (and keys lifted to the top level) is stripped.
        for k in ("meta", "components", "northStar", "customSections", "industry", "similar"):
            self.assertNotIn(k, alpha["ds"], k)
        self.assertEqual(alpha["ds"]["description"], "d")
        for k in ("tags", "extracted_at"):
            self.assertNotIn(k, alpha, k)
        self.assertEqual(alpha["similar"], [{"slug": "beta", "name": "Beta", "why": "same"},
                                            {"slug": None, "name": "Nobody", "why": "none"}])
        self.assertIsNone(files["beta"]["media"]["shot"])

    def test_a_duplicated_name_leaves_similar_unlinked(self):
        # Two styles named "Beta": alpha's "Beta" similar entry cannot pick
        # one, so it falls back to an unlinked card (slug: null).
        dup_a = {**self.BETA, "name": "Beta"}
        dup_b = {**self.BETA, "slug": "beta-2", "name": "Beta"}
        solo = {**self.BETA, "slug": "gamma", "name": "Gamma"}
        alpha_ds = {**self.ALPHA_DS,
                    "similar": [{"business": "Beta", "why": "same"},
                                {"business": "Gamma", "why": "unique"}]}
        _, files = self.build([("beta", dup_a, self.BETA_DS),
                               ("beta-2", dup_b, self.BETA_DS),
                               ("gamma", solo, self.BETA_DS),
                               ("alpha", self.ALPHA, alpha_ds)])
        self.assertEqual(files["alpha"]["similar"],
                         [{"slug": None, "name": "Beta", "why": "same"},
                          {"slug": "gamma", "name": "Gamma", "why": "unique"}])

    def test_a_folder_without_both_files_is_skipped(self):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "web" / "data"
            self.make(root, "alpha", self.ALPHA, self.ALPHA_DS)
            broken = root / "refero" / "broken"
            broken.mkdir(parents=True)
            (broken / "meta.json").write_text("{}")
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "DATA", site):
                out = catalog.build_refero()
            index = json.loads(out.read_text())
        self.assertEqual(len(index["styles"]), 1)
        self.assertEqual([s["slug"] for s in index["styles"]], ["alpha"])

    def test_a_style_named_index_gets_an_entity_file(self):
        # refero/index is a real style; under refero/style/ it cannot collide
        # with the index.
        index, files = self.build([("index", {**self.BETA, "slug": "index", "name": "index"}, self.BETA_DS)])
        self.assertEqual(len(index["styles"]), 1)
        self.assertEqual(index["styles"][0]["slug"], "index")
        self.assertEqual(files["index"]["slug"], "index")

    def test_a_removed_style_loses_its_entity_but_kept_styles_survive_a_crash(self):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "web" / "data"
            self.make(root, "alpha", self.ALPHA, self.ALPHA_DS)
            self.make(root, "beta", self.BETA, self.BETA_DS)
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "DATA", site):
                catalog.build_refero()
                self.assertTrue((site / "refero/style/beta.json").is_file())
                # An interrupted rerun leaves retained styles' files in place:
                # entities are written first and only absent slugs are pruned.
                (root / "refero" / "beta" / "meta.json").unlink()
                index = json.loads(catalog.build_refero().read_text())
            self.assertEqual(len(index["styles"]), 1)
            self.assertFalse((site / "refero/style/beta.json").exists())
            self.assertTrue((site / "refero/style/alpha.json").exists())

    def test_a_refero_folder_emptied_of_styles_writes_an_empty_index(self):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "web" / "data"
            self.make(root, "alpha", self.ALPHA, self.ALPHA_DS)
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "DATA", site):
                catalog.build_refero()
                import shutil
                shutil.rmtree(root / "refero" / "alpha")
                index = json.loads(catalog.build_refero().read_text())
            self.assertEqual(len(index["styles"]), 0)
            self.assertEqual(index["styles"], [])
            self.assertEqual(list((site / "refero/style").glob("*.json")), [])


class RepositoryTest(unittest.TestCase):
    def test_platform_is_required_and_must_be_known(self):
        import copy
        from unittest import mock
        data = copy.deepcopy(catalog.load_catalog())
        first, second = data["systems"][0], data["systems"][1]
        first["platform"] = "tv"
        del second["platform"]
        with mock.patch.object(catalog, "load_catalog", return_value=data):
            problems = catalog.check()
        self.assertEqual(problems, [f"{first['slug']}: platform 'tv' is not one of web, mobile, desktop",
                                    f"{second['slug']}: missing field platform"])

    def _icon_problems(self, mutate):
        import copy
        from unittest import mock
        data = copy.deepcopy(catalog.load_catalog())
        entry = next(s for s in data["systems"] if s.get("preview", {}).get("icon"))
        mutate(entry)
        with mock.patch.object(catalog, "load_catalog", return_value=data):
            return entry["slug"], [p for p in catalog.check() if "preview.icon" in p]

    def test_a_declared_icon_gap_needs_no_preview_icon(self):
        # A product with no icon declares icon.png under layoutGaps; check() must not then
        # also demand preview.icon (the two rules contradicted each other for tome).
        def gap(entry):
            del entry["preview"]["icon"]
            entry["layoutGaps"] = dict(entry.get("layoutGaps", {}), **{"icon.png": "no icon published"})
        slug, problems = self._icon_problems(gap)
        self.assertEqual(problems, [])

    def test_no_icon_and_no_declared_gap_is_a_problem(self):
        def bare(entry):
            del entry["preview"]["icon"]
            entry.get("layoutGaps", {}).pop("icon.png", None)
        slug, problems = self._icon_problems(bare)
        self.assertIn(f"{slug}: preview.icon None does not exist; run `python3 tools/fetch_icon.py {slug}`",
                      problems)

    def test_every_platform_in_the_catalog_is_known(self):
        platforms = {s["slug"]: s["platform"] for s in catalog.load_catalog()["systems"]}
        self.assertTrue(set(platforms.values()) <= set(catalog.PLATFORMS))
        self.assertEqual(platforms["hevy"], "mobile")

    def test_image_tags_come_from_path_words(self):
        self.assertEqual(catalog._tags_for(Path("screenshots/dark/d01-home.png")), ["dark"])
        self.assertEqual(catalog._tags_for(Path("screenshots/mobile-login-light-default.png")),
                         ["light", "mobile"])



class AtomicWriteTest(unittest.TestCase):
    def test_output_is_group_and_world_readable(self):
        # mkstemp creates the temp file 0600; without the fchmod the renamed
        # file stays owner-only and a web server running as another uid
        # answers 403 for every generated page (the live failure this guards).
        import stat
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "data.json"
            catalog.atomic_write(path, "{}")
            mode = stat.S_IMODE(path.stat().st_mode)
            self.assertEqual(mode & 0o044, 0o044, oct(mode))


class RepoFileTest(unittest.TestCase):
    def test_allowed_paths_map_into_the_checkout(self):
        self.assertEqual(catalog.repo_file("/catalog.json"), (catalog.ROOT / "catalog.json").resolve())
        self.assertEqual(catalog.repo_file("/systems/claude/README.md?x=1"),
                         (catalog.ROOT / "systems/claude/README.md").resolve())

    def test_parent_segments_cannot_leave_the_allowed_folders(self):
        for path in ("/tools/../../../../etc/passwd", "/tools/%2e%2e/%2e%2e/etc/passwd",
                     "/systems/../AGENTS.md", "/systems/..%2f..%2fetc/passwd"):
            target = catalog.repo_file(path)
            self.assertTrue(target is None or catalog.ROOT.resolve() in target.parents, path)
            self.assertNotEqual(target, (catalog.ROOT / "AGENTS.md").resolve(), path)

    def test_other_paths_are_left_to_the_built_site(self):
        self.assertIsNone(catalog.repo_file("/gallery/index.html"))
        self.assertIsNone(catalog.repo_file("/"))

    def test_ignored_files_fonts_and_example_clones_are_refused(self):
        for path in ("/systems/claude/tools/capture/dumps/home.html", "/systems/claude/tools/capture/out/x.json",
                     "/systems/claude/fonts/Product.woff2", "/systems/claude/raw/x.partial.json",
                     "/example/README.md", "/tools/kit/../../systems/claude/fonts/a.ttf"):
            self.assertIsNone(catalog.repo_file(path), path)
        self.assertIsNotNone(catalog.repo_file("/systems/claude/tokens.json"))
        self.assertIsNotNone(catalog.repo_file("/tools/kit/README.md"))

    def test_a_git_failure_refuses_rather_than_serves(self):
        import subprocess
        from unittest import mock
        failed = subprocess.CompletedProcess([], 128, b"", b"fatal")
        with mock.patch.object(catalog.subprocess, "run", return_value=failed):
            self.assertIsNone(catalog.repo_file("/systems/claude/tokens.json"))


class InnerShadowTest(unittest.TestCase):
    def test_tokens_studio_inner_shadow_exports_as_inset(self):
        layer = {"offsetX": "0px", "offsetY": "-6px", "blur": "0px", "spread": "0px", "color": "#00000026"}
        self.assertEqual(catalog.css_value(dict(layer, type="innerShadow")), "inset 0px -6px 0px 0px #00000026")
        self.assertEqual(catalog.css_value(dict(layer, inset=True)), "inset 0px -6px 0px 0px #00000026")
        self.assertEqual(catalog.css_value(dict(layer, type="dropShadow")), "0px -6px 0px 0px #00000026")
        self.assertEqual(catalog.css_value([dict(layer, type="innerShadow"), layer]),
                         "inset 0px -6px 0px 0px #00000026, 0px -6px 0px 0px #00000026")


class SmallBugsTest(unittest.TestCase):
    def test_resolver_sees_an_edited_tokens_file(self):
        # A scratch ROOT, so the test never writes a file into the checkout.
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as d, mock.patch.object(catalog, "ROOT", Path(d)):
            path = Path(d) / "edited-tokens.json"
            path.write_text('{"core": {"c": {"$value": "#000000"}}}')
            try:
                self.assertEqual(catalog.resolver_for(path.name).lookup("core.c"), "#000000")
                path.write_text('{"core": {"c": {"$value": "#ffffff"}}}')
                os.utime(path, ns=(1, 10**18))                  # a different mtime, whatever the clock says
                self.assertEqual(catalog.resolver_for(path.name).lookup("core.c"), "#ffffff")
            finally:
                catalog.resolver_for.cache_clear()

    def test_check_reports_a_missing_or_broken_tokens_file_instead_of_crashing(self):
        import copy
        from unittest import mock
        cat = copy.deepcopy(catalog.load_catalog())
        cat["systems"][0]["tokens"] = "systems/no-such/tokens.json"
        with mock.patch.object(catalog, "load_catalog", return_value=cat):
            problems = catalog.check()
        slug = cat["systems"][0]["slug"]
        self.assertIn(f"{slug}: tokens systems/no-such/tokens.json does not exist", problems)
        cat["systems"][0]["tokens"] = "README.md"                   # not JSON
        with mock.patch.object(catalog, "load_catalog", return_value=cat):
            problems = catalog.check()
        self.assertTrue(any(p.startswith(f"{slug}: tokens README.md cannot be read") for p in problems), problems)

    def test_build_refero_refuses_a_path_like_slug_before_writing(self):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            data = Path(d) / "web" / "data"
            styles = [(Path(d) / "ok", {"slug": "fine", "name": "Fine"}, {}),
                      (Path(d) / "bad", {"slug": "../../escaped", "name": "Bad"}, {})]
            with mock.patch.object(catalog, "DATA", data), \
                 mock.patch.object(catalog, "load_refero", return_value=styles), \
                 mock.patch.object(catalog, "refero_entry", return_value={}), \
                 mock.patch.object(catalog, "refero_card", return_value={"name": "x"}), \
                 self.assertRaises(SystemExit) as cm:
                catalog.build_refero()
            self.assertIn("../../escaped", str(cm.exception.code))
            self.assertFalse((data / "refero" / "style" / "fine.json").exists())
            self.assertEqual([p for p in Path(d).rglob("*.json")], [])

    def test_check_still_reports_preview_problems_with_a_broken_tokens_file(self):
        import copy
        from unittest import mock
        cat = copy.deepcopy(catalog.load_catalog())
        s = cat["systems"][0]
        s["tokens"], s["preview"]["cover"] = "README.md", "systems/no-such/cover.png"
        with mock.patch.object(catalog, "load_catalog", return_value=cat):
            problems = catalog.check()
        self.assertIn(f"{s['slug']}: preview.cover systems/no-such/cover.png does not exist", problems)

    def test_refero_slug_pattern_refuses_paths(self):
        for ok in ("linear", "a-b-2"):
            self.assertTrue(catalog.REFERO_SLUG.fullmatch(ok))
        for bad in ("../x", "a/b", "A", "a_b", "", "-a", "a.json"):
            self.assertIsNone(catalog.REFERO_SLUG.fullmatch(bad), bad)


class EnvTest(unittest.TestCase):
    def test_dotenv_loads_only_the_listed_keys(self):
        import os
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(os.environ, {}, clear=False):
            env = Path(d) / ".env"
            env.write_text("UNLISTED_SECRET=hunter2\nexport DS_CHAT_MODEL='m'\n# ANTHROPIC_API_KEY=x\n"
                           "ANTHROPIC_API_KEY=\"sk-test\"\nSOMETHING_ELSE=1\n")
            for k in ("UNLISTED_SECRET", "DS_CHAT_MODEL", "ANTHROPIC_API_KEY", "SOMETHING_ELSE"):
                os.environ.pop(k, None)
            done = catalog.refero_media.load_env(env_file=env)
            self.assertEqual(sorted(done), ["ANTHROPIC_API_KEY", "DS_CHAT_MODEL"])
            self.assertEqual(os.environ["ANTHROPIC_API_KEY"], "sk-test")
            self.assertNotIn("UNLISTED_SECRET", os.environ)
            self.assertNotIn("SOMETHING_ELSE", os.environ)
            os.environ.pop("DS_CHAT_MODEL")
            self.assertEqual(catalog.refero_media.load_env(("DS_CHAT_MODEL",), env_file=env), ["DS_CHAT_MODEL"])
            self.assertEqual(catalog.refero_media.load_env(("DS_CHAT_MODEL",), env_file=env), [])   # set wins

    def test_importing_refero_media_does_not_read_dotenv(self):
        import importlib.util
        from unittest import mock
        spec = importlib.util.spec_from_file_location(
            "refero_media_fresh", Path(catalog.__file__).resolve().parent / "refero" / "refero_media.py")
        mod = importlib.util.module_from_spec(spec)
        with mock.patch("pathlib.Path.is_file", return_value=True), \
                mock.patch("pathlib.Path.read_text", side_effect=AssertionError("read .env on import")):
            spec.loader.exec_module(mod)

    def test_subprocesses_get_a_minimal_env(self):
        import os
        import subprocess
        from unittest import mock
        with mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-test", "R2_SECRET_ACCESS_KEY": "s", "PATH": "/bin"}):
            env = catalog.tool_env(X="1")
            self.assertEqual(env["PATH"], "/bin")
            self.assertEqual(env["X"], "1")
            self.assertNotIn("ANTHROPIC_API_KEY", env)
            self.assertNotIn("R2_SECRET_ACCESS_KEY", env)
            seen = []
            done = subprocess.CompletedProcess([], 0, '{"findings": []}', "")
            with mock.patch.object(catalog.shutil, "which", return_value="/bin/npx"), \
                 mock.patch.object(catalog.subprocess, "run", side_effect=lambda *a, **k: seen.append(k.get("env")) or done):
                catalog.lint_design_md([catalog.ROOT / "systems" / "claude" / "DESIGN.md"])
            self.assertTrue(seen and all(e is not None and "ANTHROPIC_API_KEY" not in e for e in seen))
            seen.clear()
            with mock.patch.object(catalog, "_thumb_backend", return_value="sips"), \
                 mock.patch.object(catalog.subprocess, "run", side_effect=lambda *a, **k: seen.append(k.get("env")) or done):
                import tempfile
                with tempfile.TemporaryDirectory() as d:
                    src = Path(d) / "a.png"
                    src.write_bytes(b"x")
                    catalog._make_thumb(src, Path(d) / "a.jpg")
            self.assertEqual(len(seen), 1)
            self.assertIsNotNone(seen[0])
            self.assertNotIn("R2_SECRET_ACCESS_KEY", seen[0])
            self.assertNotIn("ANTHROPIC_API_KEY", seen[0])

    def test_tesseract_gets_a_minimal_env_with_one_thread(self):
        import os
        import subprocess
        from unittest import mock
        try:
            from PIL import Image
            import redact_images
        except ImportError:
            self.skipTest("Pillow and numpy are not installed")
        seen = []
        done = subprocess.CompletedProcess([], 0, "level\tpage_num\n", "")
        with mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-test", "R2_SECRET_ACCESS_KEY": "s"}), \
             mock.patch.object(redact_images.subprocess, "run", side_effect=lambda *a, **k: seen.append(k.get("env")) or done):
            redact_images._tesseract_words(Image.new("RGB", (4, 4)))
        self.assertEqual(seen[0]["OMP_THREAD_LIMIT"], "1")
        self.assertNotIn("ANTHROPIC_API_KEY", seen[0])
        self.assertNotIn("R2_SECRET_ACCESS_KEY", seen[0])


class ManifestTest(unittest.TestCase):
    SYSTEMS = [{"slug": "alpha", "url": "https://www.alpha.example"}, {"slug": "beta", "url": "https://app.beta.example"}]

    def manifest(self, *apps, totals=None):
        apps = list(apps)
        batches = max((a.get("batch", 1) for a in apps), default=0)
        return {"totals": totals or {"apps": len(apps), "batches": batches}, "apps": apps}

    def app(self, domain, status, package=None, batch=1):
        return {"domain": domain, "status": status, "package": package, "batch": batch}

    def test_a_consistent_manifest_is_clean(self):
        m = self.manifest(self.app("alpha.example", "captured", "systems/alpha"),
                          self.app("gamma.example", "pending", batch=2))
        self.assertEqual(catalog.manifest_problems(m, self.SYSTEMS), [])

    def test_a_bare_slug_is_not_a_package_path(self):
        m = self.manifest(self.app("alpha.example", "captured", "alpha"))
        self.assertEqual(len(catalog.manifest_problems(m, self.SYSTEMS)), 1)

    def test_each_kind_of_drift_is_named(self):
        m = self.manifest(self.app("alpha.example", "captured"),                     # no package
                          self.app("beta.example", "pending"),                       # beta is captured
                          self.app("gamma.example", "uncapturable", "systems/gamma"),  # package without capture
                          totals={"apps": 9, "batches": 4})
        problems = catalog.manifest_problems(m, self.SYSTEMS)
        self.assertEqual(len(problems), 5, problems)
        self.assertIn("alpha.example: captured, but its package None is not a systems/<slug> in catalog.json", problems[0])
        self.assertIn("beta.example: status 'pending', but catalog.json already has systems/beta", problems[1])
        self.assertIn("gamma.example: status 'uncapturable' with package 'systems/gamma'", problems[2])
        self.assertIn("totals.apps is 9, the file lists 3", problems[3])
        self.assertIn("totals.batches is 4, the highest batch is 1", problems[4])


if __name__ == "__main__":
    unittest.main()
