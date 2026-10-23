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

    def test_a_grade_without_evidence_fails(self):
        broken = copy.deepcopy(SYSTEM)
        del broken["grades"]["F1"]["evidence"]
        problems = bp.check(CRITERIA, [audit(broken)])
        self.assertEqual(len(problems), 1)
        self.assertIn("F1", problems[0])
        self.assertIn('"evidence"', problems[0])

    def test_a_grade_entry_of_the_wrong_shape_fails(self):
        for bad in ("meets", {"evidence": "e"}):
            broken = copy.deepcopy(SYSTEM)
            broken["grades"]["F2"] = bad
            problems = bp.check(CRITERIA, [audit(broken)])
            self.assertEqual(len(problems), 1, bad)
            self.assertIn("F2", problems[0])

    def test_malformed_grades_do_not_crash_check(self):
        broken = copy.deepcopy(SYSTEM)
        broken["grades"] = ["meets"]
        problems = bp.check(CRITERIA, [audit(broken)])
        self.assertEqual(len(problems), 1)
        self.assertIn("grades must be an object", problems[0])


PLATFORM_CRITERIA = {"layers": {"F": "Foundations"}, "criteria": [
    {"id": "F1", "layer": "Foundations", "title": "Ramps", "doneWhen": "Web ramps.",
     "platforms": {"mobile": "Mobile ramps.", "desktop": "Desktop ramps."}},
    {"id": "F2", "layer": "Foundations", "title": "Roles", "doneWhen": "Web roles.",
     "platforms": {"mobile": "Native roles.", "desktop": "Native roles."}},
    {"id": "F3", "layer": "Foundations", "title": "Hover", "doneWhen": "Hover too.",
     "platforms": {"mobile": "No hover."}},
    {"id": "F4", "layer": "Foundations", "title": "Plain", "doneWhen": "Same everywhere."}]}


def graded(platform=None, slug="a"):
    s = copy.deepcopy(SYSTEM) | {"slug": slug, "grades": {c["id"]: {"grade": "meets", "evidence": "e"}
                                                           for c in PLATFORM_CRITERIA["criteria"]}}
    if platform:
        s["platform"] = platform
    return s


class PlatformWordingTest(unittest.TestCase):
    def test_a_platform_uses_its_own_wording_else_the_web_wording(self):
        f1, f3, f4 = (PLATFORM_CRITERIA["criteria"][i] for i in (0, 2, 3))
        self.assertEqual(bp.done_when(f1, "mobile"), "Mobile ramps.")
        self.assertEqual(bp.done_when(f1, "web"), "Web ramps.")
        self.assertEqual(bp.done_when(f3, "desktop"), "Hover too.")
        self.assertEqual(bp.done_when(f4, "mobile"), "Same everywhere.")

    def test_platforms_sharing_a_wording_are_grouped(self):
        f2, f3, f4 = PLATFORM_CRITERIA["criteria"][1:]
        self.assertEqual(bp.wordings(f2), [(["web"], "Web roles."), (["mobile", "desktop"], "Native roles.")])
        self.assertEqual(bp.wordings(f3), [(["web", "desktop"], "Hover too."), (["mobile"], "No hover.")])
        self.assertEqual(bp.wordings(f4), [(["web", "mobile", "desktop"], "Same everywhere.")])

    def test_a_snapshot_entry_without_a_platform_is_web(self):
        self.assertEqual(bp.platform_of(SYSTEM), "web")

    def test_check_refuses_a_web_or_unknown_platform_wording_and_an_unknown_platform(self):
        criteria = copy.deepcopy(PLATFORM_CRITERIA)
        criteria["criteria"][3]["platforms"] = {"web": "copy", "watch": "tiny"}
        problems = bp.check(criteria, [audit(graded("tv"))])
        self.assertEqual(len(problems), 2)
        self.assertIn("F4: platforms has web, watch", problems[0])
        self.assertIn("unknown platform 'tv'", problems[1])
        self.assertEqual(bp.check(PLATFORM_CRITERIA, [audit(graded("mobile"))]), [])

    def test_the_system_page_shows_the_wording_for_its_platform(self):
        mobile = graded("mobile")
        md = bp.system_page(PLATFORM_CRITERIA, audit(mobile), mobile, 1)
        self.assertIn("Graded against the mobile wording", md)
        for text in ("Mobile ramps.", "Native roles.", "No hover.", "Same everywhere."):
            self.assertIn(f'<span class="sc-done">{text}</span>', md)
        for text in ("Web ramps.", "Web roles.", "Hover too."):
            self.assertNotIn(text, md)
        self.assertNotIn("Re-review due", md)
        stale = mobile | {"reviewedPlatform": "web"}
        self.assertIn("set against the web wording, before this package was graded as mobile",
                      bp.system_page(PLATFORM_CRITERIA, audit(stale), stale, 1))
        web = bp.system_page(PLATFORM_CRITERIA, audit(SYSTEM | graded()), graded(), 1)
        self.assertIn('<span class="sc-done">Web ramps.</span>', web)
        self.assertIn(" · web · ", web)

    def test_the_criteria_page_shows_every_platform_wording(self):
        md = bp.criteria_page(PLATFORM_CRITERIA, audit(graded()))
        self.assertIn("*Web:* Web ramps.<br>*Mobile:* Mobile ramps.<br>*Desktop:* Desktop ramps.", md)
        self.assertIn("*Web:* Web roles.<br>*Mobile and desktop:* Native roles.", md)
        self.assertIn("*Web and desktop:* Hover too.<br>*Mobile:* No hover.", md)
        self.assertIn("| Plain | Same everywhere. |", md)

    def test_the_changelog_renders_a_rubric_2_snapshot_beside_a_rubric_3_one(self):
        old = audit(SYSTEM | graded(), date="2026-10-16")
        old["rubric"] = "2"
        new = audit(graded("mobile"), date="2026-10-17")
        new["rubric"] = "3"
        new["systems"][0]["grades"]["F3"]["grade"] = "partly"
        md = bp.changelog_page(PLATFORM_CRITERIA, [old, new])
        self.assertIn("- Rubric changed from version 2 to 3", md)
        self.assertIn("F3 Hover meets → partly", md)
        self.assertNotIn("platform web", md)  # the old entry predates the field, so no change is claimed
        newer = copy.deepcopy(new) | {"date": "2026-10-18"}
        newer["systems"][0]["platform"] = "desktop"
        self.assertIn("**A**: platform mobile → desktop.", bp.changelog_page(PLATFORM_CRITERIA, [old, new, newer]))

    def test_the_real_changelog_renders_every_snapshot(self):
        criteria, audits = bp.load()
        md = bp.changelog_page(criteria, audits)
        self.assertEqual(md.count("\n## "), len(audits))


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

    def test_only_the_index_page_hides_the_rail(self):
        self.assertTrue(bp.index_page(CRITERIA, audit(SYSTEM)).startswith("---\nhide:\n  - navigation\n---\n"))
        for md in (bp.system_page(CRITERIA, audit(SYSTEM), SYSTEM, 1),
                   bp.criteria_page(CRITERIA, audit(SYSTEM)), bp.changelog_page(CRITERIA, [audit(SYSTEM)])):
            self.assertFalse(md.startswith("---"))


if __name__ == "__main__":
    unittest.main()
