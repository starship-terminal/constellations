"""Tests for app/scripts/build-media-taxonomy.py's term IDs."""
from __future__ import annotations

import importlib.util
import io
import json
import os
import tempfile
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


class CheckTest(unittest.TestCase):
    """--check demands the exact derivation, on a pull request and on main alike."""

    FRESH = {"packages": [{"referenceId": "systems:alpha"}, {"referenceId": "systems:added"}], "assignments": []}

    def check(self, committed):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "media-taxonomy.json"
            if committed is not None:
                out.write_text(json.dumps(committed))
            pr = {"GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"}
            with mock.patch.object(taxonomy, "OUTPUT", out), \
                    mock.patch.object(taxonomy, "build", return_value=self.FRESH), \
                    mock.patch.dict(os.environ, pr), mock.patch("sys.argv", ["build", "--check"]), \
                    mock.patch("sys.stdout", new_callable=io.StringIO):
                taxonomy.main()

    def test_the_exact_seed_passes(self):
        self.check(self.FRESH)

    def test_a_seed_that_lags_main_or_names_a_removed_package_fails(self):
        for committed in ({**self.FRESH, "packages": self.FRESH["packages"][:1]},
                          {**self.FRESH, "packages": self.FRESH["packages"] + [{"referenceId": "systems:gone"}]},
                          None):
            with self.assertRaises(SystemExit) as e:
                self.check(committed)
            self.assertIn("stale", str(e.exception))


if __name__ == "__main__":
    unittest.main()
