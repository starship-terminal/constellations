"""Tests for app/scripts/build-media-taxonomy.py's term IDs."""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import subprocess
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "build_media_taxonomy", ROOT / "app/scripts/build-media-taxonomy.py"
)
taxonomy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(taxonomy)


class TermIdTest(unittest.TestCase):
    # Expected values are what taxonomyTermId in app/src/contracts/taxonomy.ts
    # returns for the same input.
    def test_readable_labels_slug_like_the_app(self):
        self.assertEqual(taxonomy.term_id("web-categories", "Food & Drink"), "web-categories:food-drink")
        self.assertEqual(taxonomy.term_id("g", "  Café — Bar  "), "g:café-bar")

    def test_label_without_letters_or_digits_falls_back_to_code_points(self):
        self.assertEqual(taxonomy.term_id("g", "&"), "g:u-26")
        self.assertEqual(taxonomy.term_id("g", "★ ☆"), "g:u-2605-20-2606")
        self.assertEqual(taxonomy.term_id("g", ""), "g:u-")


class AsciiLocaleTest(unittest.TestCase):
    def test_the_seed_builds_under_an_ascii_locale_with_utf8_mode_off(self):
        # catalog.json and the tokens files hold non-ASCII text; every read must say UTF-8.
        code = ("import importlib.util, sys; s = importlib.util.spec_from_file_location('t', sys.argv[1]); "
                "m = importlib.util.module_from_spec(s); s.loader.exec_module(m); "
                "print(len(m.build()['packages']))")
        env = {**os.environ, "LC_ALL": "C", "LANG": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0"}
        run = subprocess.run([sys.executable, "-c", code, str(ROOT / "app/scripts/build-media-taxonomy.py")],
                             capture_output=True, text=True, env=env, encoding="utf-8")
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertGreater(int(run.stdout.strip()), 0)


class FontEvidenceTest(unittest.TestCase):
    def test_only_the_primary_family_of_a_stack_is_assigned(self):
        # An invented package whose font token lists two families the
        # vocabulary knows: only the first is rendered-font evidence.
        system = {
            "slug": "invented",
            "platform": "web",
            "tokens": "systems/invented/tokens.json",
            "preview": {"fonts": ["font.body"]},
        }
        tokens = {"font": {"body": {"$value": "Inter, Arial, sans-serif"}}}
        media = [{"path": "systems/invented/screenshots/home.png"}]
        catalog = taxonomy.catalog
        with mock.patch.object(catalog, "load_catalog", return_value={"systems": [system]}), \
                mock.patch.object(catalog, "resolver_for", return_value=catalog.Resolver(tokens)), \
                mock.patch.object(catalog, "list_images", side_effect=lambda s, folder, ext: media if folder == "screenshots" else []):
            result = taxonomy.build()
        fonts = [t["termId"] for a in result["assignments"] for t in a["terms"] if t["termId"].startswith("web-fonts:")]
        self.assertEqual(fonts, ["web-fonts:inter"])


class SeedLagTest(unittest.TestCase):
    """On a pull request the seed may leave out packages the merge adds, and is
    otherwise re-derived from the merge's catalog and files, never trusted from
    the branch."""

    def system(self, slug):
        return {"slug": slug, "name": slug.title(), "platform": "web",
                "tokens": f"systems/{slug}/tokens.json", "preview": {}}

    def setUp(self):
        self.shots = {
            "old": ["systems/old/screenshots/home.png"],
            "newer": ["systems/newer/screenshots/pricing.png"],   # landed on main after the branch started
            "added": ["systems/added/screenshots/login.png"],     # this pull request's
        }
        self.old, self.newer, self.added = self.system("old"), self.system("newer"), self.system("added")
        self.base = [self.old, self.newer]
        self.branch = [self.old, self.added]
        self.head = [self.old, self.newer, self.added]

    def images(self, system, folder, exts):
        return [{"path": p} for p in self.shots.get(system["slug"], [])] if folder == "screenshots" else []

    def seed(self, systems):
        catalog = taxonomy.catalog
        with mock.patch.object(catalog, "load_catalog", return_value={"systems": systems}), \
                mock.patch.object(catalog, "fonts", return_value=[]), \
                mock.patch.object(catalog, "list_images", side_effect=self.images):
            return taxonomy.build()

    def matches(self, committed, head=None, base=None, branch=None, env=None, fail=False):
        env = {"GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"} if env is None else env
        catalog = taxonomy.catalog
        refs = {"origin/main": base or self.base, "refs/pr-head": branch or self.branch}

        def run(args, **kwargs):
            if fail:
                raise catalog.subprocess.CalledProcessError(128, args)
            ref, _, path = args[-1].partition(":")
            assert args[:2] == ["git", "show"] and path == "catalog.json", args
            return mock.Mock(stdout=json.dumps({"systems": refs[ref]}), returncode=0)

        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch.object(catalog.subprocess, "run", run), \
                mock.patch.object(catalog, "load_catalog", return_value={"systems": head or self.head}), \
                mock.patch.object(catalog, "fonts", return_value=[]), \
                mock.patch.object(catalog, "list_images", side_effect=self.images):
            return taxonomy.matches_base(taxonomy.build(), committed)

    def test_a_seed_that_lags_main_or_this_pull_request_is_accepted(self):
        for subset in ([self.old], [self.old, self.added], [self.old, self.newer]):
            self.assertTrue(self.matches(self.seed(subset)), [s["slug"] for s in subset])

    def test_a_hand_edited_seed_is_rejected_even_when_the_branch_carries_it(self):
        edited = self.seed(self.branch)
        edited["assignments"] = edited["assignments"][:-1]
        self.assertFalse(self.matches(edited))

    def test_an_existing_package_with_new_images_and_no_rebuild_is_rejected(self):
        committed = self.seed([self.old])
        self.shots["old"] = self.shots["old"] + ["systems/old/screenshots/settings.png"]
        self.assertFalse(self.matches(committed))

    def test_leaving_out_a_package_the_branch_and_main_share_is_rejected(self):
        self.assertFalse(self.matches(self.seed([self.added])))

    def test_a_removed_package_still_named_is_rejected(self):
        head, branch = [self.newer, self.added], [self.added]
        self.assertFalse(self.matches(self.seed(self.base), head=head, branch=branch))
        self.assertTrue(self.matches(self.seed([self.added]), head=head, branch=branch))

    def test_no_pull_request_or_an_unreadable_ref_keeps_the_exact_rule(self):
        prior = self.seed([self.old])
        self.assertFalse(self.matches(prior, env={}))
        self.assertFalse(self.matches(prior, fail=True))


if __name__ == "__main__":
    unittest.main()
