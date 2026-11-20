"""Tests for tools/health.py. Run with `make test`."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog  # noqa: E402
import health  # noqa: E402

CRITERIA = {"criteria": [{"id": "F1", "title": "Colour ramps"}, {"id": "F2", "title": "Background roles"},
                         {"id": "C1", "title": "Component coverage"}, {"id": "V1", "title": "Principles", "optional": "where published"}]}
README = "# X design reference\n\nIntro.\n\n| File | What it is |\n|---|---|\n| [tokens.json](tokens.json) | Tokens |\n\n## Fonts\n\nInter.\n"


def grades(**by_id):
    return {cid: {"grade": g, "evidence": f"why {cid}"} for cid, g in by_id.items()}


def audit(*systems, date="2026-10-17"):
    return {"date": date, "systems": list(systems)}


class Package:
    """A temporary repository with one package, `systems/x/`, holding the given entries."""

    def __init__(self, entries=("tokens.json",), readme=README):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        folder = self.root / "systems" / "x"
        folder.mkdir(parents=True)
        (folder / "README.md").write_text(readme)
        for entry in entries:
            if entry.endswith("/"):
                (folder / entry).mkdir()
            else:
                (folder / entry).write_text("")
        (self.root / "README.md").write_text("# lib\n\n<!-- catalog:start -->\n<!-- catalog:end -->\n")
        self.patches = [mock.patch.object(catalog, "ROOT", self.root), mock.patch.object(health, "ROOT", self.root)]

    def __enter__(self):
        for p in self.patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def readme(self):
        return (self.root / "systems" / "x" / "README.md").read_text()


SYSTEM = {"slug": "x", "captured": "2026-10-10", "goodFor": "Tests | pipes", "themes": ["light"]}


class SectionTest(unittest.TestCase):
    def test_counts_leave_out_optional_criteria_a_product_does_not_publish(self):
        with Package():
            text = health.package_section(CRITERIA, audit({"slug": "x", "name": "X", "grades": grades(
                F1="meets", F2="partly", C1="missing", V1="na")}), SYSTEM)
        self.assertIn("**1 of 3 met, 1 partly, 1 missing**; V1 are optional for a capture and not published", text)

    def test_a_product_level_not_applicable_is_told_apart_from_an_optional_one(self):
        with Package():
            text = health.package_section(CRITERIA, audit({"slug": "x", "name": "X", "grades": grades(
                F1="na", F2="meets", C1="meets", V1="na")}), SYSTEM)
        self.assertIn("; F1 do not apply; V1 are optional for a capture and not published", text)

    def test_open_criteria_list_missing_before_partly(self):
        with Package():
            text = health.package_section(CRITERIA, audit({"slug": "x", "name": "X", "grades": grades(
                F1="partly", F2="meets", C1="missing", V1="na")}), SYSTEM)
        self.assertLess(text.index("| C1 Component coverage | Missing"), text.index("| F1 Colour ramps | Partly"))
        self.assertNotIn("Background roles", text)

    def test_evidence_with_a_pipe_stays_in_its_cell(self):
        g = grades(F1="partly", F2="meets", C1="meets", V1="na")
        g["F1"]["evidence"] = "a | b\nc"
        with Package():
            text = health.package_section(CRITERIA, audit({"slug": "x", "name": "X", "grades": g}), SYSTEM)
        self.assertIn("| a \\| b c |", text)

    def test_a_capture_newer_than_the_review_is_flagged(self):
        graded = {"slug": "x", "name": "X", "reviewed": "2026-10-01", "grades": grades(F1="meets", F2="meets", C1="meets", V1="na")}
        with Package():
            text = health.package_section(CRITERIA, audit(graded), SYSTEM)
        self.assertIn("Re-review due", text)
        self.assertIn("Every gradable criterion is met.", text)

    def test_an_ungraded_package_says_how_to_grade_it(self):
        with Package():
            text = health.package_section(CRITERIA, audit(), SYSTEM)
        self.assertIn("Not graded yet", text)
        self.assertIn("--review x=", text)

    def test_layout_names_missing_parts_and_unlisted_entries(self):
        with Package(entries=("tokens.json", "extra.md", "raw/")):
            text = health.package_section(CRITERIA, audit(), SYSTEM)
        self.assertIn("no `icon.png`, `DESIGN.md`", text)
        self.assertNotIn("`raw/`,", text.split("not in the file table")[0])
        self.assertIn("not in the file table above: `extra.md`, `raw/`", text)


class FileTableTest(unittest.TestCase):
    def test_only_the_file_table_lists_entries(self):
        readme = README + "\n| Value | Source |\n|---|---|\n| a | `raw/notes.json` |\n"
        with Package(entries=("tokens.json", "raw/"), readme=readme):
            _, unlisted = catalog.layout_gaps("x")
        self.assertEqual(unlisted, ["raw/"])


class PlacementTest(unittest.TestCase):
    def test_inserted_before_the_first_section_and_replaced_in_place(self):
        first = health.with_section(README, "## Health\n\nold\n\n<!-- health:end -->\n")
        self.assertLess(first.index("## Health"), first.index("## Fonts"))
        self.assertGreater(first.index("## Health"), first.index("| [tokens.json]"))
        second = health.with_section(first, "## Health\n\nnew\n\n<!-- health:end -->\n")
        self.assertNotIn("old", second)
        self.assertEqual(second.count("## Health"), 1)
        self.assertEqual(second.replace("new", "old"), first)

    def test_the_section_never_reaches_design_md(self):
        text = health.with_section(README, "## Health\n\nColours and fonts and components\n\n<!-- health:end -->\n")
        _, parts = catalog.readme_parts(text)
        for section, _ in catalog.README_SECTIONS:
            self.assertNotIn("Colours and fonts", catalog._readme_for(section, parts))


class WriteTest(unittest.TestCase):
    def test_write_then_check_is_clean_and_an_edit_is_stale(self):
        snap = audit({"slug": "x", "name": "X", "grades": grades(F1="meets", F2="partly", C1="meets", V1="na")})
        with Package() as pkg:
            self.assertEqual(len(health.write(CRITERIA, snap, [SYSTEM])), 2)
            self.assertEqual(health.problems(CRITERIA, snap, [SYSTEM]), [])
            self.assertEqual(health.write(CRITERIA, snap, [SYSTEM]), [])
            path = pkg.root / "systems" / "x" / "README.md"
            path.write_text(pkg.readme().replace("Partly", "Meets"))
            self.assertEqual(len(health.problems(CRITERIA, snap, [SYSTEM])), 1)
            root = (pkg.root / "README.md").read_text()
        self.assertIn("| [x](systems/x/README.md) | Tests \\| pipes | 2026-10-10 | light | 2 of 3 met, 1 partly, 0 missing |", root)

    def test_an_add_only_slug_keeps_the_base_catalog_table(self):
        """The check CI runs, including on main after the pull request merges.
        A new ungraded slug whose own Health matches is accepted when the
        root table still lists only the graded package. No pull request base
        is set. Editing the graded package's Health, or hand-editing the new
        section, still fails."""
        snap = audit({"slug": "x", "name": "X", "grades": grades(F1="meets", F2="partly", C1="meets", V1="na")})
        added = {"slug": "clay", "captured": "2026-11-19", "goodFor": "CRM", "themes": ["light"], "category": "productivity",
                 "layoutGaps": {"icons/": "No standalone SVG icon set was lifted."}}
        with Package() as pkg:
            health.write(CRITERIA, snap, [SYSTEM])
            self.assertEqual(health.problems(CRITERIA, snap, [SYSTEM]), [])
            clay = pkg.root / "systems" / "clay"
            clay.mkdir()
            (clay / "README.md").write_text("# Clay\n\n## Fonts\n\nInter.\n")
            (clay / "tokens.json").write_text("")
            section = health.package_section(CRITERIA, snap, added)
            (clay / "README.md").write_text("# Clay\n\n" + section)
            # No GITHUB_BASE_REF and no base catalog: this is the main push.
            self.assertEqual(health.problems(CRITERIA, snap, [SYSTEM, added]), [])
            # A layoutGaps reason that still has its closing period is the same section.
            (clay / "README.md").write_text("# Clay\n\n" + section.replace(").", ".)."))
            self.assertEqual(health.problems(CRITERIA, snap, [SYSTEM, added]), [])
            (clay / "README.md").write_text("# Clay\n\n" + section)
            # A hand-edited Health section on the new package still fails.
            (clay / "README.md").write_text("# Clay\n\n" + section.replace("Not graded yet", "Graded by hand"))
            stale = health.problems(CRITERIA, snap, [SYSTEM, added])
            self.assertTrue(any("systems/clay/README.md" in line for line in stale))
            (clay / "README.md").write_text("# Clay\n\n" + section)
            # An edit to the package the table already lists still fails.
            (pkg.root / "systems" / "x" / "README.md").write_text(
                pkg.readme().replace("Partly", "Meets"))
            edited = health.problems(CRITERIA, snap, [SYSTEM, added])
            self.assertTrue(any("systems/x/README.md" in line for line in edited))

    def test_the_root_table_may_omit_only_ungraded_packages(self):
        """root_omits_only_ungraded: each way the root table can be wrong while a
        package's own Health is current still fails."""
        snap = audit({"slug": "x", "name": "X", "grades": grades(F1="meets", F2="partly", C1="meets", V1="na")})
        y = {"slug": "y", "captured": "2026-10-11", "goodFor": "Other", "themes": ["dark"]}
        stale = "README.md: Health is stale; run `python3 tools/health.py`"
        with Package() as pkg:
            (pkg.root / "systems" / "y").mkdir()
            (pkg.root / "systems" / "y" / "README.md").write_text(README)
            health.write(CRITERIA, snap, [SYSTEM, y])
            root = pkg.root / "README.md"
            current = root.read_text()

            def table(systems):
                return health.TABLE.sub(lambda _: health.catalog_table(snap, systems), current, count=1)

            # Leaving out ungraded y is accepted; that is the exemption.
            root.write_text(table([SYSTEM]))
            self.assertEqual(health.problems(CRITERIA, snap, [SYSTEM, y]), [])
            # Leaving out graded x is not.
            root.write_text(table([y]))
            self.assertIn(stale, health.problems(CRITERIA, snap, [SYSTEM, y]))
            # A row for a package not in the catalog is not.
            ghost = {"slug": "ghost", "captured": "2026-10-01", "goodFor": "Gone", "themes": ["light"]}
            root.write_text(table([SYSTEM, y, ghost]))
            self.assertIn(stale, health.problems(CRITERIA, snap, [SYSTEM, y]))
            # A stale row for a listed package is not.
            root.write_text(table([{**SYSTEM, "goodFor": "Old words"}]))
            self.assertIn(stale, health.problems(CRITERIA, snap, [SYSTEM, y]))

    def test_catalog_table_ranks_by_the_scorecard(self):
        snap = audit({"slug": "a", "name": "A", "grades": grades(F1="partly", F2="partly", C1="meets", V1="na")},
                     {"slug": "b", "name": "B", "grades": grades(F1="meets", F2="meets", C1="meets", V1="na")})
        systems = [{"slug": "a"}, {"slug": "b"}, {"slug": "c"}]
        with Package():
            table = health.catalog_table(snap, systems)
        rows = [line for line in table.splitlines() if "README.md)" in line]
        self.assertEqual([r.split("]")[0].split("[")[-1] for r in rows], ["b", "a", "c"])
        self.assertIn("not graded yet", rows[2])

    def test_catalog_table_shows_no_icon_for_a_declared_icon_gap(self):
        # A package with the icon.png layout gap has no preview.icon: its row must not
        # point at an icon.png that does not exist.
        systems = [{"slug": "a", "preview": {"icon": "systems/a/icon.png"}},
                   {"slug": "b", "preview": {}, "layoutGaps": {"icon.png": "no icon published"}}]
        with Package():
            table = health.catalog_table(audit(), systems)
        rows = [line for line in table.splitlines() if "README.md)" in line]
        self.assertTrue(rows[0].startswith('| <img src="systems/a/icon.png" width="20" alt="a"> |'))
        self.assertTrue(rows[1].startswith("|  | [b](systems/b/README.md)"))


if __name__ == "__main__":
    unittest.main()
