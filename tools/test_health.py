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
                         {"id": "C1", "title": "Component coverage"}, {"id": "V1", "title": "Principles"}]}
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
    def test_counts_leave_out_criteria_a_capture_cannot_meet(self):
        with Package():
            text = health.package_section(CRITERIA, audit({"slug": "x", "name": "X", "grades": grades(
                F1="meets", F2="partly", C1="missing", V1="na")}), SYSTEM)
        self.assertIn("**1 of 3 met, 1 partly, 1 missing**; V1 do not apply", text)

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
        self.assertIn("no `DESIGN.md`", text)
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

    def test_catalog_table_ranks_by_the_scorecard(self):
        snap = audit({"slug": "a", "name": "A", "grades": grades(F1="partly", F2="partly", C1="meets", V1="na")},
                     {"slug": "b", "name": "B", "grades": grades(F1="meets", F2="meets", C1="meets", V1="na")})
        systems = [{"slug": "a"}, {"slug": "b"}, {"slug": "c"}]
        with Package():
            table = health.catalog_table(snap, systems)
        rows = [line for line in table.splitlines() if line.startswith("| [")]
        self.assertEqual([r.split("]")[0][3:] for r in rows], ["b", "a", "c"])
        self.assertIn("not graded yet", rows[2])


if __name__ == "__main__":
    unittest.main()
