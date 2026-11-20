"""Tests for tools/brief.py. Run with `make test`."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brief  # noqa: E402
import catalog  # noqa: E402
import grade  # noqa: E402
import health  # noqa: E402

RULES = ("## Do and don't\n\n"
         "1. **Do keep one filled button.** The rest are outlined. See [a](screenshots/a.png).\n"
         "2. Don't tint the chrome. It stays grey, see [b](screenshots/b.png).\n"
         "3. **Don't fake states with opacity.**\n"
         "   Wrapped onto a second line with [c](screenshots/c.png).\n")
README = ("# X design reference\n\nIntro.\n\n| File | What it is |\n|---|---|\n| [tokens.json](tokens.json) | Tokens |\n\n"
          "## Health\n\n<!-- health:start. x -->\n\nOld.\n\n<!-- health:end -->\n\n## Fonts\n\nInter.\n\n" + RULES)


def colours(**values):
    return {k: {"$value": v} for k, v in values.items()}


TOKENS = {
    "core": {"font": {"sans": {"$value": "Inter, Arial, sans-serif"}},
             "typography": {"body": {"$value": {"fontFamily": "Inter", "fontSize": "14px"}}},
             "radius": {"sm": {"$value": "4px"}, "lg": {"$value": "8px"}},
             "spacing": {"1": {"$value": "4px"}},
             "focusRing": {"width": {"$value": "2px"}, "color": {"$value": "{ink}"}}},
    "light": {**colours(bg="#ffffff", card="#fafafa", ink="#111111", soft="#999999", line="#dddddd"),
              "border": {"focus": {"$value": "{ink}"}}},
    "dark": colours(bg="#000000", card="rgba(255,255,255,0.05)", ink="#ffffff", soft="#cccccc", line="#333333"),
}
ROLES = {"page": "bg", "surface": "card", "text": "ink", "muted": "soft", "accent": "ink", "border": "line"}


def palette(theme):
    return {role: f"{theme}.{name}" for role, name in ROLES.items()}


SYSTEM = {"slug": "x", "name": "X", "goodFor": "Tests", "captured": "2026-10-10", "tokens": "systems/x/tokens.json",
          "entry": "systems/x/README.md", "themes": ["light", "dark", "contrast"],
          "preview": {"swatches": {"light": palette("light"), "dark": palette("dark")}, "fonts": ["core.font.sans"]}}


class Package:
    """A temporary repository with one package, `systems/x/`."""

    def __init__(self, tokens=TOKENS, readme=README, entries=()):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.folder = self.root / "systems" / "x"
        self.folder.mkdir(parents=True)
        (self.folder / "README.md").write_text(readme)
        (self.folder / "tokens.json").write_text(json.dumps(tokens))
        for entry in entries:
            path = self.folder / entry
            path.parent.mkdir(parents=True, exist_ok=True)
            if not entry.endswith("/"):
                path.write_text("")
        self.patches = [mock.patch.object(m, "ROOT", self.root) for m in (catalog, brief, grade, health)]

    def __enter__(self):
        catalog.resolver_for.cache_clear()
        for p in self.patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self.patches:
            p.stop()
        catalog.resolver_for.cache_clear()
        self.tmp.cleanup()

    def readme(self):
        return (self.folder / "README.md").read_text()


class PrinciplesTest(unittest.TestCase):
    def test_bold_lead_else_first_sentence(self):
        self.assertEqual(brief.lead("**Do keep it flat.** Because."), "Do keep it flat.")
        self.assertEqual(brief.lead("Don't tint the chrome. It stays grey."), "Don't tint the chrome.")
        self.assertEqual(brief.lead("Keep `fill.brand` for send"), "Keep `fill.brand` for send")

    def test_rules_are_numbered_and_link_the_section(self):
        text = "\n".join(brief.principles(README))
        self.assertIn("1. Do keep one filled button.\n2. Don't tint the chrome.\n3. Don't fake states with opacity.", text)
        self.assertIn("[Do and don't](#do-and-dont)", text)

    def test_no_section_and_an_empty_section_are_said(self):
        self.assertIn("has no \"Do and don't\" section", "\n".join(brief.principles("# X\n\n## Fonts\n")))
        self.assertIn("lists no rules", "\n".join(brief.principles("# X\n\n## Do's and don'ts\n\nNothing yet.\n")))

    def test_slug_matches_github_anchors(self):
        self.assertEqual(brief.slug("Do and don't"), "do-and-dont")
        self.assertEqual(brief.slug("Do's and Don'ts"), "dos-and-donts")


class SectionTest(unittest.TestCase):
    def section(self, system=SYSTEM, **kw):
        with Package(**kw):
            return brief.section(system)

    def test_tokens_table_has_a_column_per_theme_with_values(self):
        text = self.section()
        self.assertIn("| Role | light | dark |", text)
        self.assertIn("| page | #ffffff `light.bg` | #000000 `dark.bg` |", text)
        self.assertIn("`core.font.sans` is Inter, then 2 fallbacks", text)
        self.assertIn("1 type style (`core.typography`), 2 radius steps (`core.radius`), 1 spacing step", text)

    def test_contrast_rows_match_grade_and_unchecked_themes_are_named(self):
        text = self.section()
        with Package():
            rows, _, _ = grade.contrast_rows(SYSTEM)
        light_muted = next(r for r in rows if r["theme"] == "light" and r["role"] == "muted" and r["bgRole"] == "page")
        self.assertIn(f"{light_muted['ratio']:.2f}:1 fail", text)
        self.assertIn("| dark | 21.00:1 pass |", text)
        self.assertIn(f"{sum(r['status'] == 'pass' for r in rows)} of 8 pairs pass 4.5:1", text)
        self.assertIn("Not checked, no palette: contrast.", text)

    def test_focus_tokens_shortest_first_at_most_four_resolved(self):
        text = self.section()
        self.assertIn("Focus tokens: `light.border.focus` #111111; `core.focusRing.color` #111111; "
                      "`core.focusRing.width` 2px.", text)
        many = json.loads(json.dumps(TOKENS))
        many["core"]["focus"] = {k: {"$value": "1px"} for k in ("a", "b", "c", "d", "e")}
        text = self.section(tokens=many)
        self.assertEqual(re.findall(r"`core\.focus\.(\w)`", text), ["a", "b", "c", "d"])

    def test_a_base_focus_token_comes_before_its_variants(self):
        tokens = json.loads(json.dumps(TOKENS))
        tokens["light"]["border"] = {"focus-danger": {"$value": "#ff0000"}, "x": {"focus": {"$value": "{ink}"}}}
        text = self.section(tokens=tokens)
        self.assertLess(text.index("`light.border.x.focus`"), text.index("`light.border.focus-danger`"))

    def test_a_focus_token_not_measured_carries_its_evidence_label(self):
        tokens = json.loads(json.dumps(TOKENS))
        tokens["core"]["focusRing"] = {
            "width": {"$value": "2px", "$extensions": {"source": {"evidence": "Measured"}}},
            "color": {"$value": "#123456", "$extensions": {"source": {"evidence": "Reconstruction"}}},
            "offset": {"$value": "1px", "$extensions": {"source": "Sampled from the focus crop."}},
            "inset": {"$value": "0px", "$extensions": {"evidence": "Derived", "source": "rem at 16px"}}}
        del tokens["light"]["border"]
        text = self.section(tokens=tokens)
        self.assertIn("`core.focusRing.color` #123456 (Reconstruction, not measured)", text)
        self.assertIn("`core.focusRing.width` 2px;", text)
        self.assertIn("`core.focusRing.inset` 0px;", text)
        self.assertIn("`core.focusRing.offset` 1px (Sampled, not measured)", text)

    def test_a_key_holding_a_dot_keeps_its_label(self):
        tokens = json.loads(json.dumps(TOKENS))
        tokens["light"]["border"] = {"input.error.focus": {
            "$value": "#ff0000", "$extensions": {"source": {"evidence": "Sampled"}}}}
        self.assertIn("`light.border.input.error.focus` #ff0000 (Sampled, not measured)", self.section(tokens=tokens))

    def test_token_objects_walks_like_flatten(self):
        tokens = json.loads(json.dumps(TOKENS))
        tokens["light"]["a.b"] = {"c": {"$value": "#000000"}}
        tokens["core"]["legacy"] = {"value": "1px", "type": "dimension"}
        self.assertEqual(set(brief.token_objects(tokens)), set(catalog.flatten(tokens)))

    def test_evidence_reads_each_label_place(self):
        self.assertEqual(brief.evidence({"$extensions": {"source": {"evidence": "Sampled (text)"}}}), "Sampled")
        self.assertEqual(brief.evidence({"$extensions": {"evidence": "Observed", "source": "UA ring"}}), "Observed")
        self.assertEqual(brief.evidence({"$extensions": {"source": "Reconstruction: entered by hand."}}),
                         "Reconstruction")
        self.assertEqual(brief.evidence({"$extensions": {"source": "not captured in dark"}}), "Not captured")
        self.assertIsNone(brief.evidence({"$extensions": {"source": "computed outline of the field"}}))
        self.assertIsNone(brief.evidence({"$extensions": {"source": "Measuredness"}}))
        self.assertIsNone(brief.evidence({"$value": "1px"}))
        self.assertIsNone(brief.evidence(None))

    def test_no_focus_tokens_is_said(self):
        tokens = json.loads(json.dumps(TOKENS))
        del tokens["core"]["focusRing"], tokens["light"]["border"]
        self.assertIn("no focus tokens", self.section(tokens=tokens))

    def test_pipes_in_cells_are_escaped(self):
        tokens = json.loads(json.dumps(TOKENS))
        tokens["light"]["a|b"] = {"$value": "#ffffff"}
        system = json.loads(json.dumps(SYSTEM))
        system["preview"]["swatches"]["light"]["page"] = "light.a|b"
        text = self.section(system=system, tokens=tokens)
        self.assertIn("| page | #ffffff `light.a\\|b` |", text)

    def test_components_count_crops_and_name_declared_gaps(self):
        text = self.section(entries=("components.md", "components/crops/a.png", "components/crops/sub/b.png",
                                     "components/crops/notes.txt", "components/c.svg"))
        self.assertIn("[components.md](components.md)", text)
        self.assertIn("2 element crops in [components/crops/](components/crops)", text)
        self.assertIn("1 other image in [components/](components)", text)
        system = {**SYSTEM, "layoutGaps": {"patterns.md": "not written yet."}}
        text = self.section(system=system)
        self.assertIn("no patterns.md (not written yet)", text)
        self.assertIn("no components/", text)

    def test_short_and_never_matches_the_do_heading(self):
        text = self.section()
        self.assertLess(len(text.splitlines()), 50)
        self.assertIsNone(grade.DO_HEADING.search(text))
        self.assertNotIn("\u2014", text)


class PlacementTest(unittest.TestCase):
    BRIEF = "## Brief\n\n<!-- brief:start. x -->\n\nold\n\n<!-- brief:end -->\n"

    def test_inserted_after_the_file_table_before_health_and_replaced_in_place(self):
        first = brief.with_section(README, self.BRIEF)
        self.assertLess(first.index("| [tokens.json]"), first.index("## Brief"))
        self.assertLess(first.index("<!-- brief:end -->"), first.index("## Health"))
        second = brief.with_section(first, self.BRIEF.replace("old", "new"))
        self.assertEqual(second.count("## Brief"), 1)
        self.assertEqual(second.replace("new", "old"), first)

    def test_without_health_it_goes_before_the_first_section(self):
        readme = "# X\n\n| File | What |\n|---|---|\n\n## Fonts\n\nInter.\n"
        out = brief.with_section(readme, self.BRIEF)
        self.assertLess(out.index("## Brief"), out.index("## Fonts"))
        self.assertTrue(brief.with_section("# X\n", self.BRIEF).endswith(self.BRIEF))

    def test_health_added_later_goes_after_the_brief(self):
        readme = brief.with_section("# X\n\n## Fonts\n\nInter.\n", self.BRIEF)
        out = health.with_section(readme, "## Health\n\nh\n\n<!-- health:end -->\n")
        self.assertLess(out.index("<!-- brief:end -->"), out.index("## Health"))
        self.assertLess(out.index("## Health"), out.index("## Fonts"))
        self.assertEqual(brief.with_section(out, self.BRIEF), out)

    def test_the_section_never_reaches_design_md(self):
        for _, rx in catalog.README_SECTIONS:
            self.assertIsNone(re.search(rx, "Brief", re.I))
        with Package():
            text = brief.with_section(README, brief.section(SYSTEM))
        intro, parts = catalog.readme_parts(text)
        self.assertNotIn("brief", intro.lower())
        for section, _ in catalog.README_SECTIONS:
            self.assertNotIn("Read this before designing", catalog._readme_for(section, parts))

    def test_k2_still_reads_the_real_section(self):
        with Package():
            text = brief.with_section(README, brief.section(SYSTEM))
        self.assertEqual(grade.do_and_dont(text), grade.do_and_dont(README))
        self.assertEqual(grade.do_and_dont(text)[0], "Do and don't")


class WriteTest(unittest.TestCase):
    def test_write_then_check_is_clean_and_an_edit_is_stale(self):
        with Package() as pkg:
            self.assertEqual(len(brief.write([SYSTEM])), 1)
            self.assertEqual(brief.problems([SYSTEM]), [])
            self.assertEqual(brief.write([SYSTEM]), [])
            (pkg.folder / "README.md").write_text(pkg.readme().replace("1. Do keep", "1. Do not keep", 1))
            self.assertEqual(len(brief.problems([SYSTEM])), 1)

    def test_brief_and_health_reach_a_fixed_point(self):
        criteria = {"criteria": [{"id": "F1", "title": "Colour ramps"}]}
        snap = {"date": "2026-10-17", "systems": [{"slug": "x", "name": "X", "grades": {
            "F1": {"grade": "meets", "evidence": "ok"}}}]}
        readme = README.split("## Health")[0] + "## Fonts\n\nInter.\n\n" + RULES
        with Package(readme=readme) as pkg:
            (pkg.root / "README.md").write_text("<!-- catalog:start -->\n<!-- catalog:end -->\n")
            brief.write([SYSTEM])
            health.write(criteria, snap, [SYSTEM])
            once = pkg.readme()
            self.assertEqual(brief.write([SYSTEM]), [])
            self.assertEqual(health.write(criteria, snap, [SYSTEM]), [])
            self.assertEqual(pkg.readme(), once)
        self.assertLess(once.index("## Brief"), once.index("## Health"))


if __name__ == "__main__":
    unittest.main()
