"""Tests for tools/grade.py. Run with `make test`."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grade  # noqa: E402
import scorecard  # noqa: E402

ROLES = {"page": "light.bg", "surface": "light.card", "text": "light.ink", "muted": "light.soft",
         "accent": "light.ink", "border": "light.ink"}


def system_with(tokens: dict, readme: str = "# X\n", swatches=None) -> tuple[dict, tempfile.TemporaryDirectory]:
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    (root / "tokens.json").write_text(json.dumps(tokens))
    (root / "README.md").write_text(readme)
    system = {"slug": "x", "tokens": "tokens.json", "entry": "README.md",
              "preview": {"swatches": swatches or {"light": ROLES}}}
    return system, tmp


def colours(**values):
    return {"light": {k: {"$value": v, "$extensions": {"source": "m"}} for k, v in values.items()}}


class ContrastTest(unittest.TestCase):
    def run_grade(self, **values):
        system, tmp = system_with(colours(**values))
        with tmp, mock.patch.object(grade, "ROOT", Path(tmp.name)):
            return grade.grade_contrast(system)

    def test_all_pairs_pass(self):
        g, why = self.run_grade(bg="#ffffff", card="#fafafa", ink="#111111", soft="#555555")
        self.assertEqual(g, "meets")
        self.assertIn("all 4 pairs", why)

    def test_secondary_failing_is_partly_and_names_the_worst_pair(self):
        g, why = self.run_grade(bg="#ffffff", card="#f7f7f7", ink="#111111", soft="#777777")
        self.assertEqual(g, "partly")
        self.assertIn("secondary fails 2 pairs", why)
        self.assertIn("light.soft", why)

    def test_primary_failing_is_missing(self):
        g, _ = self.run_grade(bg="#ffffff", card="#ffffff", ink="#bbbbbb", soft="#555555")
        self.assertEqual(g, "missing")

    def test_theme_without_a_palette_borrows_the_paths_or_is_reported(self):
        tokens = {**colours(bg="#ffffff", card="#fafafa", ink="#111111", soft="#555555"),
                  "mobile": {k: {"$value": v} for k, v in
                             dict(bg="#ffffff", card="#ffffff", ink="#111111", soft="#999999").items()}}
        system, tmp = system_with(tokens)
        system["themes"] = ["light", "mobile", "contrast"]
        with tmp, mock.patch.object(grade, "ROOT", Path(tmp.name)):
            g, why = grade.grade_contrast(system)
        self.assertEqual(g, "partly")
        self.assertIn("mobile muted (mobile.soft)", why)
        self.assertIn("contrast not checked (no palette)", why)

    def test_translucent_surface_is_blended_over_the_page(self):
        g, why = self.run_grade(bg="#000000", card="rgba(255,255,255,0.05)", ink="#ffffff", soft="#cccccc")
        self.assertEqual(g, "meets", why)


class ProvenanceTest(unittest.TestCase):
    def run_grade(self, tokens):
        system, tmp = system_with(tokens)
        with tmp, mock.patch.object(grade, "ROOT", Path(tmp.name)):
            return grade.grade_provenance(system)

    def test_every_label_style_counts(self):
        tokens = {"a": {"$value": "1", "$extensions": {"source": "m"}}, "b": {"$value": "2", "$description": "d"},
                  "c": {"value": "3", "description": "d"}}
        self.assertEqual(self.run_grade(tokens), ("meets", "Script: 3 of 3 tokens name their source"))

    def test_mostly_labelled_is_partly_and_few_is_missing(self):
        labelled = {f"t{i}": {"$value": "1", "$description": "d"} for i in range(9)}
        self.assertEqual(self.run_grade({**labelled, "x": {"$value": "1"}})[0], "partly")
        self.assertEqual(self.run_grade({"x": {"$value": "1"}, "y": {"$value": "2"}})[0], "missing")


class DoAndDontTest(unittest.TestCase):
    def run_grade(self, readme):
        system, tmp = system_with({}, readme)
        with tmp, mock.patch.object(grade, "ROOT", Path(tmp.name)):
            return grade.grade_do_and_dont(system)

    def test_three_linked_rules_meet(self):
        rules = "\n".join(f"{i}. **Do {i}.** See [shot](screenshots/a-{i}.png)." for i in range(1, 4))
        self.assertEqual(self.run_grade(f"# X\n\n## Do and don't\n\n{rules}\n\n## Next\n\n- [x](b.png)\n")[0], "meets")

    def test_rule_without_an_image_is_partly(self):
        readme = "## Do and don't\n\n- Do a. [s](a.png)\n- Do b. [s](b.png)\n- Don't c.\n"
        self.assertEqual(self.run_grade(readme), ("partly", "Script: 3 rules, 2 linking an image (needs 3+, all linked)"))

    def test_link_on_a_wrapped_line_counts(self):
        readme = ("## Do and don't\n\n1. **Do a.** Long rule that wraps,\n   see [s](a.png).\n"
                  "2. **Do b.**\n   [s](b.png)\n3. Do c. [s](c.png)\n\nA closing paragraph [x](d.png).\n")
        self.assertEqual(self.run_grade(readme), ("meets", "Script: 3 rules, each linking a screenshot or crop"))

    def test_introduction_and_heading_suffix_are_skipped(self):
        rules = "\n".join(f"- Do {i}. [s](s{i}.png)" for i in range(3))
        readme = f"## Do and don't (observed)\n\nFollow these rules:\n\n{rules}\n"
        self.assertEqual(self.run_grade(readme)[0], "meets")

    def test_no_section_is_missing(self):
        self.assertEqual(self.run_grade("# X\n\nSome text.\n")[0], "missing")

    def test_section_ends_at_the_next_heading_of_its_level(self):
        readme = "## Do and don't\n\n- Do a. [s](a.png)\n\n## Other\n\n- not a rule\n- nor this\n"
        self.assertIn("1 rules", self.run_grade(readme)[1])


class SnapshotTest(unittest.TestCase):
    CRITERIA = {"version": "2", "layers": {"F": "Foundations"}, "criteria": [
        {"id": "F15", "layer": "Foundations", "title": "Contrast", "doneWhen": "x"},
        {"id": "V1", "layer": "Foundations", "title": "Principles", "doneWhen": "y", "optional": "where published"},
        {"id": "C1", "layer": "Foundations", "title": "Coverage", "doneWhen": "z"}]}
    BASE = {"date": "2026-10-16", "rubric": "1", "method": "Review.", "_seq": 1, "systems": [
        {"slug": "x", "grades": {"F15": {"grade": "meets", "evidence": "old"},
                                 "V1": {"grade": "missing", "evidence": "none"},
                                 "C1": {"grade": "partly", "evidence": "11/19"}}}]}

    def test_scripted_grades_replace_optional_rules_apply_and_reviews_carry_over(self):
        fresh = {"F15": {"grade": "partly", "evidence": "Script: new"}}
        with mock.patch.object(grade, "scripted", return_value=fresh):
            out = grade.snapshot(self.CRITERIA, self.BASE, [{"slug": "x"}], "2026-10-17")
        g = out["systems"][0]["grades"]
        self.assertEqual(g["F15"], fresh["F15"])
        self.assertEqual(g["V1"]["grade"], "na")
        self.assertEqual(g["C1"], {"grade": "partly", "evidence": "11/19"})
        self.assertEqual((out["date"], out["base"], out["rubric"]), ("2026-10-17", "2026-10-16", "2"))
        self.assertNotIn("_seq", out)
        self.assertTrue(out["method"].endswith("Review."))

    def test_regrading_a_scripted_snapshot_still_credits_the_review(self):
        with mock.patch.object(grade, "scripted", return_value={}):
            first = grade.snapshot(self.CRITERIA, self.BASE, [{"slug": "x"}], "2026-10-17")
            second = grade.snapshot(self.CRITERIA, first, [{"slug": "x"}], "2026-10-18")
        self.assertEqual(second["base"], "2026-10-16")
        self.assertEqual(second["method"].count("Review."), 1)


class RefreshAndReviewTest(unittest.TestCase):
    CRITERIA = SnapshotTest.CRITERIA
    BASE = {"date": "2026-10-16", "method": "Review.", "systems": [
        {"slug": "x", "name": "Old", "goodFor": "old", "url": "u", "captured": "2026-09-01", "themes": ["dark"],
         "category": "Learning", "grades": {"F15": {"grade": "meets", "evidence": "e"},
                                            "V1": {"grade": "na", "evidence": "n"},
                                            "C1": {"grade": "partly", "evidence": "11/19"}}}]}
    SOURCE = {"slug": "x", "name": "New", "goodFor": "new", "url": "u", "captured": "2026-10-17",
              "themes": ["dark", "light"], "category": "productivity"}

    def make(self, reviews=None):
        with mock.patch.object(grade, "scripted", return_value={"F15": {"grade": "meets", "evidence": "s"}}):
            return grade.snapshot(self.CRITERIA, self.BASE, [self.SOURCE], "2026-10-17",
                                  {"productivity": "Productivity"}, reviews)

    def test_package_details_come_from_the_catalog(self):
        s = self.make()["systems"][0]
        self.assertEqual((s["name"], s["themes"], s["captured"], s["category"]),
                         ("New", ["dark", "light"], "2026-10-17", "Productivity"))

    def test_a_review_replaces_reviewed_grades_and_records_its_date(self):
        s = self.make({"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})["systems"][0]
        self.assertEqual(s["grades"]["C1"]["grade"], "meets")
        self.assertEqual(s["reviewed"], "2026-10-17")

    def test_a_review_can_replace_the_method_and_later_snapshots_keep_it(self):
        with mock.patch.object(grade, "scripted", return_value={}):
            out = grade.snapshot(self.CRITERIA, self.BASE, [self.SOURCE], "2026-10-17", {},
                                 {"x": {"C1": {"grade": "meets", "evidence": "17/19"}}}, "Second review.")
            later = grade.snapshot(self.CRITERIA, out, [self.SOURCE], "2026-10-18")
        self.assertEqual(out["reviewMethod"], "Second review.")
        self.assertTrue(out["method"].endswith("Second review.") and "Review." not in out["method"])
        self.assertEqual(later["reviewMethod"], "Second review.")

    def test_a_method_without_a_review_is_refused(self):
        with mock.patch.object(grade, "scripted", return_value={}), self.assertRaises(SystemExit):
            grade.snapshot(self.CRITERIA, self.BASE, [self.SOURCE], "2026-10-17", {}, None, "Text.")

    def test_a_review_cannot_set_scripted_or_unknown_criteria(self):
        for cid in ("F15", "Z9"):
            with self.assertRaises(SystemExit):
                self.make({"x": {cid: {"grade": "meets", "evidence": "x"}, "C1": {"grade": "meets", "evidence": "x"}}})

    def test_an_optional_grade_counts_when_published_and_never_reads_missing(self):
        kept = self.make({"x": {"C1": {"grade": "meets", "evidence": "x"},
                                "V1": {"grade": "partly", "evidence": "principles page"}}})
        self.assertEqual(kept["systems"][0]["grades"]["V1"], {"grade": "partly", "evidence": "principles page"})
        dropped = self.make({"x": {"C1": {"grade": "meets", "evidence": "x"},
                                   "V1": {"grade": "missing", "evidence": "none"}}})
        self.assertEqual(dropped["systems"][0]["grades"]["V1"]["grade"], "na")
        # A later snapshot with no review keeps the published grade.
        with mock.patch.object(grade, "scripted", return_value={}):
            later = grade.snapshot(self.CRITERIA, kept, [self.SOURCE], "2026-10-18")
        self.assertEqual(later["systems"][0]["grades"]["V1"]["grade"], "partly")

    def test_the_review_sheet_lists_optional_criteria_apart(self):
        lines = grade.review_sheet(self.CRITERIA, {"slug": "x", "platform": "web"})
        opt = next(i for i, l in enumerate(lines) if l.startswith("Optional:"))
        self.assertTrue(lines[opt + 1].startswith("V1"))
        self.assertFalse(any(l.startswith("V1") for l in lines[:opt]))

    def test_a_first_review_adds_a_package_and_an_unknown_slug_is_refused(self):
        new = {**self.SOURCE, "slug": "y", "name": "Y"}
        with mock.patch.object(grade, "scripted", return_value={"F15": {"grade": "meets", "evidence": "s"}}):
            out = grade.snapshot(self.CRITERIA, self.BASE, [self.SOURCE, new], "2026-10-17",
                                 {"productivity": "Productivity"}, {"y": {"C1": {"grade": "partly", "evidence": "9/19"}}})
            with self.assertRaises(SystemExit) as e:
                grade.snapshot(self.CRITERIA, self.BASE, [self.SOURCE], "2026-10-17", {},
                               {"z": {"C1": {"grade": "meets", "evidence": "x"}}})
        y = next(s for s in out["systems"] if s["slug"] == "y")
        self.assertEqual((y["name"], y["category"], y["reviewed"]), ("Y", "Productivity", "2026-10-17"))
        self.assertEqual(set(y["grades"]), {"F15", "C1", "V1"})
        self.assertEqual(y["grades"]["V1"]["grade"], "na")
        self.assertIn("not in catalog.json", str(e.exception))

    def test_a_review_entry_needs_grade_and_evidence(self):
        for bad in ({"grade": "meets"}, {"evidence": "e"}, {"grade": "great", "evidence": "e"},
                    {"grade": ["meets"], "evidence": "e"}, "meets"):
            with self.assertRaises(SystemExit) as e:
                self.make({"x": {"C1": bad}})
            self.assertIn("C1", str(e.exception), bad)

    def test_an_incomplete_review_is_refused(self):
        criteria = {**self.CRITERIA, "criteria": self.CRITERIA["criteria"] + [
            {"id": "C2", "layer": "Foundations", "title": "States", "doneWhen": "w"}]}
        with mock.patch.object(grade, "scripted", return_value={}), self.assertRaises(SystemExit) as e:
            grade.snapshot(criteria, self.BASE, [self.SOURCE], "2026-10-17", {},
                           {"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})
        self.assertIn("C2", str(e.exception))

    def test_stale_catches_new_measurements_and_categories_within_a_grade(self):
        fresh = self.make({"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})
        moved = {"F15": {"grade": "meets", "evidence": "a different ratio"}}
        with mock.patch.object(grade, "scripted", return_value=moved):
            problems, _ = grade.stale(self.CRITERIA, fresh, [self.SOURCE], {"productivity": "Productivity"})
        self.assertTrue(any("F15" in p for p in problems))
        with mock.patch.object(grade, "scripted", return_value={"F15": {"grade": "meets", "evidence": "s"}}):
            problems, _ = grade.stale(self.CRITERIA, fresh, [self.SOURCE], {"productivity": "Tools"})
        self.assertTrue(any("category" in p for p in problems))

    def test_stale_reports_changed_details_and_old_reviews(self):
        with mock.patch.object(grade, "scripted", return_value={"F15": {"grade": "partly", "evidence": "s"}}):
            problems, warnings = grade.stale(self.CRITERIA, self.BASE, [self.SOURCE], {})
        self.assertTrue(any("F15" in p for p in problems))
        self.assertTrue(any("themes" in p for p in problems))
        self.assertTrue(any("captured 2026-10-17" in w for w in warnings))
        fresh = self.make({"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})
        with mock.patch.object(grade, "scripted", return_value={"F15": {"grade": "meets", "evidence": "s"}}):
            problems, warnings = grade.stale(self.CRITERIA, fresh, [self.SOURCE], {"productivity": "Productivity"})
        self.assertEqual((problems, warnings), ([], []))


class SiblingSnapshotTest(unittest.TestCase):
    """Two capture branches each write a snapshot from the same base; neither review may
    be lost once both merge, whichever snapshot sorts newest."""
    CRITERIA = SnapshotTest.CRITERIA
    BASE = {"date": "2026-10-16", "method": "Review.", "_seq": 1, "systems": [
        {"slug": "x", "grades": {"C1": {"grade": "partly", "evidence": "11/19"}}}]}
    CATALOG = [{"slug": "x"}, {"slug": "y"}]

    def write(self, base, date, reviews):
        with mock.patch.object(grade, "scripted", return_value={}):
            out = grade.snapshot(self.CRITERIA, base, self.CATALOG, date, {}, reviews, "Method.")
        return out | {"_seq": 1}

    def siblings(self):
        a = self.write(self.BASE, "2026-10-17", {"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})
        b = self.write(self.BASE, "2026-10-18", {"y": {"C1": {"grade": "partly", "evidence": "9/19"}}})
        return a, b

    def test_the_newest_sibling_alone_drops_the_other_review_and_check_fails(self):
        a, b = self.siblings()
        problems, warnings = grade.lost_reviews(self.CRITERIA, [self.BASE, a, b], {"x", "y"}, known={})
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("x: the review dated 2026-10-17 in scorecard/audits/2026-10-17.json", problems[0])
        self.assertEqual(warnings, [])

    def test_carry_forward_keeps_both_reviews_in_either_order(self):
        a, b = self.siblings()
        for order in ([self.BASE, a, b], [self.BASE, b | {"date": "2026-10-17"}, a | {"date": "2026-10-18"}]):
            base, restored = grade.carry_forward(self.CRITERIA, order, {"x", "y"})
            by = {s["slug"]: s for s in base["systems"]}
            self.assertEqual(by["x"]["grades"]["C1"]["grade"], "meets")
            self.assertEqual(by["x"]["reviewed"], "2026-10-17")
            self.assertEqual(by["y"]["grades"]["C1"]["grade"], "partly")
            self.assertEqual(len(restored), 1)
            with mock.patch.object(grade, "scripted", return_value={}):
                later = grade.snapshot(self.CRITERIA, base, self.CATALOG, "2026-10-19") | {"_seq": 1}
            self.assertEqual(grade.lost_reviews(self.CRITERIA, order + [later], {"x", "y"}, known={}), ([], []))

    def test_the_newer_review_wins_over_a_sibling_carrying_the_old_one(self):
        a = self.write(self.BASE, "2026-10-17", {"x": {"C1": {"grade": "meets", "evidence": "17/19"}}})
        # b was branched before a's review and re-reviewed only y, so it carries x's base grade.
        b = self.write(self.BASE, "2026-10-18", {"y": {"C1": {"grade": "partly", "evidence": "9/19"}}})
        base, _ = grade.carry_forward(self.CRITERIA, [self.BASE, a, b], {"x", "y"})
        x = next(s for s in base["systems"] if s["slug"] == "x")
        self.assertEqual(x["grades"]["C1"], {"grade": "meets", "evidence": "17/19"})
        # A later re-review that lowers the grade wins in turn.
        c = self.write(base, "2026-10-19", {"x": {"C1": {"grade": "missing", "evidence": "0/19"}}})
        base, restored = grade.carry_forward(self.CRITERIA, [self.BASE, a, b, c], {"x", "y"})
        self.assertEqual(next(s for s in base["systems"] if s["slug"] == "x")["grades"]["C1"]["grade"], "missing")
        self.assertEqual(restored, [])

    def test_a_package_gone_from_the_catalog_is_not_brought_back(self):
        a, b = self.siblings()
        base, restored = grade.carry_forward(self.CRITERIA, [self.BASE, a, b], {"y"})
        self.assertEqual([s["slug"] for s in base["systems"]], [s["slug"] for s in b["systems"]])
        self.assertEqual(restored, [])

    def test_a_known_loss_warns_only_for_that_review(self):
        a, b = self.siblings()
        audits = [self.BASE, a, b]
        problems, warnings = grade.lost_reviews(self.CRITERIA, audits, {"x", "y"}, known={"x": "2026-10-17"})
        self.assertEqual((problems, len(warnings)), ([], 1))
        problems, _ = grade.lost_reviews(self.CRITERIA, audits, {"x", "y"}, known={"x": "2026-10-01"})
        self.assertEqual(len(problems), 1)


class PlatformTest(unittest.TestCase):
    """A package is graded against its platform's wording, and grades set against another
    wording are flagged until a review sets them again."""
    CRITERIA = {"version": "3", "layers": {"F": "Foundations"}, "criteria": [
        {"id": "F5", "layer": "Foundations", "title": "Accent states", "doneWhen": "Default, hover and pressed.",
         "platforms": {"mobile": "Default and pressed."}},
        {"id": "F15", "layer": "Foundations", "title": "Contrast", "doneWhen": "x", "platforms": {"mobile": "m"}},
        {"id": "V1", "layer": "Foundations", "title": "Principles", "doneWhen": "y", "optional": "where published",
         "platforms": {"mobile": "m"}},
        {"id": "C1", "layer": "Foundations", "title": "Coverage", "doneWhen": "z"}]}
    # Rubric 2: no platform recorded, so the reviewed grades were set against the web wording.
    BASE = {"date": "2026-10-16", "rubric": "2", "method": "Review.", "systems": [
        {"slug": slug, "name": slug, "goodFor": "g", "url": "u", "captured": "2026-10-01", "themes": ["light"],
         "grades": {"F5": {"grade": "partly", "evidence": "no hover"}, "F15": {"grade": "meets", "evidence": "s"},
                    "V1": {"grade": "na", "evidence": "n"}, "C1": {"grade": "meets", "evidence": "19/19"}}}
        for slug in ("app", "web")]}
    SOURCES = [{"slug": "app", "name": "app", "goodFor": "g", "url": "u", "captured": "2026-10-01",
                "themes": ["light"], "platform": "mobile"},
               {"slug": "web", "name": "web", "goodFor": "g", "url": "u", "captured": "2026-10-01",
                "themes": ["light"], "platform": "web"}]
    FRESH = {"F15": {"grade": "meets", "evidence": "s"}}

    def snap(self, base=None, reviews=None, date="2026-10-17"):
        with mock.patch.object(grade, "scripted", return_value=self.FRESH):
            return grade.snapshot(self.CRITERIA, base or self.BASE, self.SOURCES, date, {}, reviews,
                                  "Re-reviewed." if reviews else None)

    def stale(self, audit, sources=None):
        with mock.patch.object(grade, "scripted", return_value=self.FRESH):
            return grade.stale(self.CRITERIA, audit, sources or self.SOURCES, {})

    def test_the_snapshot_records_the_platform_and_the_wording_reviews_were_set_against(self):
        out = self.snap()
        by = {s["slug"]: s for s in out["systems"]}
        self.assertEqual(out["rubric"], "3")
        self.assertEqual((by["app"]["platform"], by["app"]["reviewedPlatform"]), ("mobile", "web"))
        self.assertEqual((by["web"]["platform"], by["web"]["reviewedPlatform"]), ("web", "web"))
        self.assertEqual(by["app"]["grades"]["F5"], {"grade": "partly", "evidence": "no hover"})

    def test_a_package_reviewed_against_another_platform_is_warned_and_web_carries_over(self):
        problems, warnings = self.stale(self.snap())
        self.assertEqual(problems, [])
        self.assertEqual(len(warnings), 1)
        # Only reviewed criteria count: F15 is scripted and V1 optional.
        self.assertIn("app: reviewed grades for F5 were set against the web wording; re-review it against "
                      "the mobile wording (`python3 tools/grade.py --criteria app`)", warnings[0])

    def test_a_review_clears_the_warning_and_later_snapshots_keep_it_clear(self):
        reviewed = self.snap(reviews={"app": {"F5": {"grade": "meets", "evidence": "pressed"},
                                              "C1": {"grade": "meets", "evidence": "18/19"}}})
        app = next(s for s in reviewed["systems"] if s["slug"] == "app")
        self.assertEqual((app["reviewedPlatform"], app["reviewed"]), ("mobile", "2026-10-17"))
        self.assertEqual(self.stale(reviewed), ([], []))
        self.assertEqual(self.stale(self.snap(base=reviewed, date="2026-10-18")), ([], []))

    def test_a_platform_change_in_the_catalog_is_stale_until_regraded_then_warned(self):
        out = self.snap()
        moved = [dict(self.SOURCES[0]), dict(self.SOURCES[1], platform="mobile")]
        problems, _ = self.stale(out, moved)
        self.assertIn("web: scorecard platform 'web' differs from catalog.json", problems)
        with mock.patch.object(grade, "scripted", return_value=self.FRESH):
            regraded = grade.snapshot(self.CRITERIA, out, moved, "2026-10-18")
        problems, warnings = self.stale(regraded, moved)
        self.assertEqual(problems, [])
        self.assertTrue(any(w.startswith("web: reviewed grades for F5") for w in warnings))

    def test_a_snapshot_from_an_older_rubric_is_stale(self):
        problems, _ = self.stale(self.BASE | {"systems": []})
        self.assertIn("scorecard rubric '2' differs from scorecard/criteria.json version '3'", problems)

    def test_the_review_sheet_gives_each_reviewed_criterion_in_the_platform_wording(self):
        sheet = grade.review_sheet(self.CRITERIA, self.SOURCES[0])
        self.assertIn("app is a mobile package", sheet[0])
        self.assertIn("F15 is set automatically", sheet[0])
        self.assertEqual(sheet[1:3], ["F5   Accent states (mobile wording): Default and pressed.",
                                      "C1   Coverage: z"])
        self.assertTrue(sheet[3].startswith("Optional:"))
        self.assertEqual(sheet[4], "V1   Principles (mobile wording): m")
        self.assertIn("F5   Accent states: Default, hover and pressed.", grade.review_sheet(self.CRITERIA, self.SOURCES[1]))


class OrderTest(unittest.TestCase):
    def test_same_day_snapshots_load_in_run_order(self):
        with tempfile.TemporaryDirectory() as d:
            audits = Path(d) / "audits"
            audits.mkdir()
            (Path(d) / "criteria.json").write_text(json.dumps({"layers": {}, "criteria": []}))
            for name, method in (("2026-10-16.json", "first"), ("2026-10-16-2.json", "second"),
                                 ("2026-10-15.json", "zeroth")):
                (audits / name).write_text(json.dumps({"date": name[:10], "method": method, "systems": []}))
            with mock.patch.object(scorecard, "DATA", Path(d)):
                _, loaded = scorecard.load()
            self.assertEqual([a["method"] for a in loaded], ["zeroth", "first", "second"])


class RealLibraryTest(unittest.TestCase):
    def test_every_package_gets_all_scripted_grades(self):
        for s in grade.catalog.load_catalog()["systems"]:
            got = grade.scripted(s)
            self.assertEqual(sorted(got), sorted(grade.SCRIPTED), s["slug"])
            for g in got.values():
                self.assertIn(g["grade"], scorecard.GRADES)


class NextPathTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.folder = Path(self.tmp.name) / "audits"
        self.folder.mkdir()
        patcher = mock.patch.object(scorecard, "DATA", Path(self.tmp.name))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.tmp.cleanup)

    def touch(self, *names):
        for n in names:
            (self.folder / n).write_text("{}")

    def test_first_of_the_day_has_no_number(self):
        self.assertEqual(grade.next_path("2026-11-06").name, "2026-11-06.json")

    def test_follows_the_highest_number_even_across_a_gap(self):
        self.touch("2026-11-06.json", "2026-11-06-2.json", "2026-11-06-18.json")
        self.assertEqual(grade.next_path("2026-11-06").name, "2026-11-06-19.json")

    def test_other_dates_do_not_count(self):
        self.touch("2026-11-05-9.json", "2026-11-060.json")
        self.assertEqual(grade.next_path("2026-11-06").name, "2026-11-06.json")

class LoadReviewsTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)

    def exits(self, spec):
        with self.assertRaises(SystemExit) as raised:
            grade.load_reviews([spec], {"x"})
        return str(raised.exception)

    def test_a_good_spec_loads(self):
        (self.dir / "r.json").write_text('{"F1": {"grade": "done", "evidence": "e"}}')
        self.assertEqual(grade.load_reviews([f"x={self.dir / 'r.json'}"], {"x"}),
                         {"x": {"F1": {"grade": "done", "evidence": "e"}}})

    def test_a_bare_slug_says_what_is_expected(self):
        self.assertIn("expected SLUG=FILE", self.exits("x"))
        self.assertIn("expected SLUG=FILE", self.exits("x="))

    def test_unknown_slug_missing_file_bad_json_and_non_object(self):
        self.assertIn("not in catalog.json", self.exits(f"nope={self.dir}"))
        self.assertIn("cannot read", self.exits(f"x={self.dir / 'absent.json'}"))
        self.assertIn("cannot read", self.exits(f"x={self.dir}"))
        (self.dir / "bad.json").write_text("{")
        self.assertIn("not valid JSON", self.exits(f"x={self.dir / 'bad.json'}"))
        (self.dir / "list.json").write_text("[]")
        self.assertIn("JSON object", self.exits(f"x={self.dir / 'list.json'}"))


if __name__ == "__main__":
    unittest.main()
