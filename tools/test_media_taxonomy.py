"""Tests for app/scripts/build-media-taxonomy.py's term IDs."""
from __future__ import annotations

import importlib.util
import unittest
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


if __name__ == "__main__":
    unittest.main()
