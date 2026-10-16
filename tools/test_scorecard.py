"""Tests for tools/scorecard.py. Run with `make test`."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scorecard as bp  # noqa: E402

CRITERIA = {"layers": {"F": "Foundations"}, "criteria": [
    {"id": "F1", "layer": "Foundations", "title": "Ramps", "doneWhen": "x"},
    {"id": "F2", "layer": "Foundations", "title": "Roles", "doneWhen": "y"}]}
SYSTEM = {"slug": "a", "name": "A", "short": "A", "category": "c", "goodFor": "g", "url": "https://a.example",
          "captured": "2026-10-01", "themes": ["light"],
          "grades": {"F1": {"grade": "meets", "evidence": "e"}, "F2": {"grade": "partly", "evidence": "f"}}}


def audit(*systems, date="2026-10-16"):
    return {"date": date, "rubric": "1", "method": "m", "systems": list(systems)}


class CheckTest(unittest.TestCase):
    def test_clean_data_passes(self):
        self.assertEqual(bp.check(CRITERIA, [audit(SYSTEM)]), [])

    def test_real_data_passes(self):
        self.assertEqual(bp.check(*bp.load()), [])

    def test_grade_for_unknown_criterion_fails(self):
        extra = copy.deepcopy(SYSTEM)
        extra["grades"]["F17"] = {"grade": "meets", "evidence": "leftover"}
        problems = bp.check(CRITERIA, [audit(extra)])
        self.assertEqual(len(problems), 1)
        self.assertIn("F17", problems[0])

    def test_duplicate_slug_fails(self):
        problems = bp.check(CRITERIA, [audit(SYSTEM, copy.deepcopy(SYSTEM))])
        self.assertEqual(len(problems), 1)
        self.assertIn("'a' appears 2 times", problems[0])

    def test_missing_criterion_and_bad_grade_fail(self):
        broken = copy.deepcopy(SYSTEM)
        del broken["grades"]["F2"]
        broken["grades"]["F1"]["grade"] = "great"
        problems = bp.check(CRITERIA, [audit(broken)])
        self.assertEqual(len(problems), 2)


class PageTest(unittest.TestCase):
    def test_every_cell_has_text_besides_colour(self):
        html = bp.heatmap(CRITERIA, [SYSTEM], audit(SYSTEM))
        self.assertIn('<span class="sc-sr">F1 Ramps: Meets</span>', html)
        self.assertIn('<caption id="sc-caption">', html)
        self.assertIn('scope="row"', html)

    def test_changelog_lists_grade_changes(self):
        later = copy.deepcopy(SYSTEM)
        later["grades"]["F2"]["grade"] = "meets"
        md = bp.changelog_page(CRITERIA, [audit(SYSTEM, date="2026-10-01"), audit(later)])
        self.assertIn("F2 Roles partly → meets", md)
        self.assertLess(md.index("2026-10-16"), md.index("2026-10-01"))

    def test_every_page_is_kept_out_of_search(self):
        for md in (bp.index_page(CRITERIA, audit(SYSTEM)), bp.system_page(CRITERIA, audit(SYSTEM), SYSTEM, 1),
                   bp.criteria_page(CRITERIA, audit(SYSTEM)), bp.changelog_page(CRITERIA, [audit(SYSTEM)])):
            self.assertTrue(md.startswith("---\nsearch:\n  exclude: true\n"))


if __name__ == "__main__":
    unittest.main()
