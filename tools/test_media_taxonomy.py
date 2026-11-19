"""Tests for app/scripts/build-media-taxonomy.py's term IDs."""
from __future__ import annotations

import importlib.util
import json
import os
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


class BaseTreeFilesTest(unittest.TestCase):
    def test_non_ascii_capture_name_stays_unquoted(self):
        raw = b"systems/cafe/screenshots/caf\xc3\xa9-dark.png\0systems/cafe/screenshots/plain.png\0"
        with mock.patch.dict(os.environ, {"GITHUB_BASE_REF": "main"}), \
                mock.patch.object(taxonomy.subprocess, "run", return_value=mock.Mock(stdout=raw)):
            files = taxonomy._base_tree_files()
        self.assertEqual(files, {
            "systems/cafe/screenshots/café-dark.png",
            "systems/cafe/screenshots/plain.png",
        })


class SeedLagTest(unittest.TestCase):
    """matches_base accepts a seed that predates packages already on main."""

    def system(self, slug):
        return {"slug": slug, "name": slug.title(), "platform": "web",
                "tokens": f"systems/{slug}/tokens.json", "preview": {}}

    def images(self, system, folder, exts):
        shots = {
            "old": ["systems/old/screenshots/home.png"],
            "newer": ["systems/newer/screenshots/pricing.png"],
            "added": ["systems/added/screenshots/login.png"],
        }
        if folder != "screenshots":
            return []
        return [{"path": path} for path in shots.get(system["slug"], [])]

    def setUp(self):
        self.old = self.system("old")
        self.newer = self.system("newer")
        self.added = self.system("added")
        self.base = {"systems": [self.old, self.newer]}
        self.head = {"systems": [self.old, self.newer, self.added]}
        self.files = {
            "systems/old/screenshots/home.png",
            "systems/newer/screenshots/pricing.png",
        }

    def prior_seed(self, systems):
        catalog = taxonomy.catalog
        with mock.patch.object(catalog, "load_catalog", return_value={"systems": systems}), \
                mock.patch.object(catalog, "fonts", return_value=[]), \
                mock.patch.object(catalog, "list_images", side_effect=self.images):
            return taxonomy.build()

    def matches(self, head, committed, files=None, base_ref="main",
                branch_seed=None, branch_catalog=None, head_sha="refs/pr-head",
                script_changed=False, script_matches_branch=True):
        catalog = taxonomy.catalog
        shown = json.dumps(self.base)
        listed = b"\0".join(path.encode() for path in (files if files is not None else self.files)) + b"\0"

        def fake_run(args, **kwargs):
            if args[:2] == ["git", "show"] and args[2].endswith(":catalog.json"):
                payload = branch_catalog if args[2].startswith(head_sha) and branch_catalog else shown
                return mock.Mock(stdout=payload, returncode=0)
            if args[:2] == ["git", "show"] and args[2].endswith(":app/src/data/media-taxonomy.json"):
                if branch_seed is None:
                    raise subprocess.CalledProcessError(1, args)
                return mock.Mock(stdout=json.dumps(branch_seed), returncode=0)
            if args[:2] == ["git", "show"]:
                return mock.Mock(stdout=shown, returncode=0)
            if args[:2] == ["git", "ls-tree"]:
                return mock.Mock(stdout=listed, returncode=0)
            if args[:2] == ["git", "diff"]:
                changed = "app/scripts/build-media-taxonomy.py\n" if script_changed else ""
                return mock.Mock(stdout=changed, returncode=0)
            if args[:2] == ["git", "rev-parse"]:
                blob = "branch\n" if args[2].startswith(head_sha) else (
                    "branch\n" if script_matches_branch else "merge\n")
                return mock.Mock(stdout=blob, returncode=0)
            raise AssertionError(args)

        env = {"GITHUB_BASE_REF": base_ref, "GITHUB_HEAD_SHA": head_sha} if base_ref else {}
        with mock.patch.dict(os.environ, env, clear=False), \
                mock.patch.object(taxonomy.subprocess, "run", fake_run), \
                mock.patch.object(catalog, "load_catalog", return_value=head), \
                mock.patch.object(catalog, "fonts", return_value=[]), \
                mock.patch.object(catalog, "list_images", side_effect=self.images):
            if not base_ref:
                os.environ.pop("GITHUB_BASE_REF", None)
            return taxonomy.matches_base({"packages": head["systems"]}, committed)

    def test_an_older_seed_is_accepted(self):
        self.assertTrue(self.matches(self.head, self.prior_seed([self.old])))

    def test_a_seed_matching_the_branch_head_is_accepted_when_main_moved(self):
        seed = self.prior_seed([self.old])
        branch = {"systems": [self.old, self.added]}
        self.assertTrue(self.matches(
            self.head, seed, branch_seed=seed, branch_catalog=json.dumps(branch)))

    def test_a_script_that_matches_the_branch_is_accepted(self):
        # The branch seed differs, so the shortcut does not return early.
        # The merge copy of the script matches the branch, so a base-only
        # script change is not a capture edit.
        self.assertTrue(self.matches(
            self.head, self.prior_seed([self.old]),
            branch_seed={"packages": []}, script_changed=True,
            script_matches_branch=True))

    def test_a_script_that_differs_from_the_branch_is_rejected(self):
        self.assertFalse(self.matches(
            self.head, self.prior_seed([self.old]),
            branch_seed={"packages": []}, script_changed=True,
            script_matches_branch=False))

    def test_a_seed_that_differs_from_the_branch_head_is_rejected(self):
        seed = self.prior_seed([self.old])
        seed["coverage"] = "hand edited"
        branch = {"systems": [self.old, self.added]}
        self.assertFalse(self.matches(
            self.head, seed, branch_seed=self.prior_seed([self.old]),
            branch_catalog=json.dumps(branch)))

    def test_changed_generated_content_is_rejected(self):
        seed = self.prior_seed([self.old])
        seed["coverage"] = "hand edited"
        self.assertFalse(self.matches(self.head, seed))

    def test_an_edited_existing_row_is_rejected(self):
        head = json.loads(json.dumps(self.head))
        head["systems"][0]["name"] = "Old edited"
        self.assertFalse(self.matches(head, self.prior_seed([self.old])))

    def test_a_removed_named_image_is_rejected(self):
        seed = self.prior_seed([self.old, self.added])
        files = set(self.files)
        self.assertFalse(self.matches(self.head, seed, files=files))

    def test_without_a_pull_request_base_the_exemption_does_not_apply(self):
        self.assertFalse(self.matches(self.head, self.prior_seed([self.old]), base_ref=None))


if __name__ == "__main__":
    unittest.main()
