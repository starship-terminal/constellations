"""Tests for tools/catalog.py. Run with `make test`."""
import copy
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog  # noqa: E402


class ResolverTest(unittest.TestCase):
    def setUp(self):
        self.res = catalog.Resolver({
            "core": {"palette": {"white": {"$value": "#ffffff"}},
                     "fontFamily": {"ui": {"$value": ["Inter", "sans-serif"]}}},
            "light": {"neutral": {"0": {"$value": "{palette.white}"}},
                      "bg": {"page": {"$value": "{neutral.0}"}},
                      "loop": {"$value": "{loop}"}},
            "app": {"canvas": {"$type": "color", "$value": {"colorSpace": "srgb",
                                                             "components": [0, 0.5, 1], "alpha": 1}}},
            "studio": {"text": {"value": "rgba(0, 0, 0, 1)", "type": "color"}},
        })

    def test_alias_resolves_in_own_set_then_core(self):
        self.assertEqual(self.res.lookup("light.bg.page"), "#ffffff")

    def test_dtcg_colour_object_becomes_hex(self):
        self.assertEqual(self.res.lookup("app.canvas"), "#0080ff")

    def test_tokens_studio_value_key(self):
        self.assertEqual(self.res.lookup("studio.text"), "rgba(0, 0, 0, 1)")

    def test_font_list_joins(self):
        self.assertEqual(self.res.lookup("core.fontFamily.ui"), "Inter, sans-serif")

    def test_missing_and_cyclic_return_none(self):
        self.assertIsNone(self.res.lookup("light.nope"))
        self.assertIsNone(self.res.lookup("light.loop"))


class PaletteCheckTest(unittest.TestCase):
    ROLES = {r: f"light.{r}" for r in catalog.SWATCH_ROLES}

    def test_complete_palette_passes(self):
        self.assertEqual(catalog.palette_problems("x", {"swatches": {"light": self.ROLES}}, ["light"]), [])

    def test_missing_swatches_fail(self):
        self.assertTrue(catalog.palette_problems("x", {}, ["light"]))
        self.assertTrue(catalog.palette_problems("x", {"swatches": {}}, ["light"]))

    def test_missing_role_fails(self):
        roles = dict(self.ROLES)
        del roles["accent"]
        problems = catalog.palette_problems("x", {"swatches": {"light": roles}}, ["light"])
        self.assertEqual(len(problems), 1)
        self.assertIn("accent", problems[0])

    def test_theme_must_be_declared(self):
        problems = catalog.palette_problems("x", {"swatches": {"dark": self.ROLES}}, ["light"])
        self.assertIn("not in themes", problems[0])


class ThumbTest(unittest.TestCase):
    def test_shared_path_is_thumbnailed_once(self):
        calls = []
        original = catalog._make_thumb
        catalog._make_thumb = lambda src, dst: calls.append(src) or False
        try:
            items = [{"path": "systems/a/s.png"}, {"path": "systems/a/s.png"}, {"path": "systems/a/t.png"}]
            catalog.attach_thumbs(items)
        finally:
            catalog._make_thumb = original
        self.assertEqual(len(calls), 2)
        self.assertEqual([i["thumb"] for i in items], ["systems/a/s.png", "systems/a/s.png", "systems/a/t.png"])


class ExportTest(unittest.TestCase):
    TOKENS = {
        "core": {"gray": {"0": {"$value": "#ffffff"}, "9": {"$value": "#111111"}},
                 "space": {"2": {"$value": "8px"}},
                 "type": {"body": {"$value": {"fontSize": "14px"}}}},
        "light": {"text": {"primary": {"$value": "{gray.9}"}}},
        "dark": {"text": {"primary": {"$value": "{gray.0}"}}},
        "app": {"canvas": {"$value": "#000000"}},
    }

    def test_sets_split_into_base_and_themes(self):
        out = catalog.export_tokens(self.TOKENS, ["light", "dark"])
        self.assertEqual(out["base"]["--gray-0"], "#ffffff")
        self.assertEqual(out["base"]["--space-2"], "8px")
        self.assertEqual(out["base"]["--app-canvas"], "#000000")
        self.assertEqual(out["themes"]["light"], {"--text-primary": "#111111"})
        self.assertEqual(out["themes"]["dark"], {"--text-primary": "#ffffff"})
        self.assertEqual(out["skipped"], ["core.type.body"])

    def test_css_puts_first_theme_on_root_and_overrides_the_rest(self):
        css = catalog.export_css(catalog.export_tokens(self.TOKENS, ["light", "dark"]))
        root, dark = css.split('[data-theme="dark"]')
        self.assertIn("--text-primary: #111111;", root)
        self.assertIn("--text-primary: #ffffff;", dark)
        self.assertNotIn("--gray-0", dark)

    def test_core_token_aliasing_theme_colours_is_emitted_per_theme(self):
        tokens = {
            "core": {"shadow": {
                "lip": {"$value": {"offsetX": "0", "offsetY": "4px", "blur": "0", "color": "{border.default}"}},
                "flat": {"$value": {"offsetX": "0", "offsetY": "1px", "blur": "0", "color": "{gray.0}"}}},
                "gray": {"0": {"$value": "#ffffff"}}},
            "light": {"border": {"default": {"$value": "#e5e5e5"}}},
            "dark": {"border": {"default": {"$value": "#37464f"}}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--shadow-lip"], "0 4px 0 #e5e5e5")
        self.assertEqual(out["themes"]["dark"]["--shadow-lip"], "0 4px 0 #37464f")
        self.assertNotIn("--shadow-lip", out["base"])
        self.assertEqual(out["base"]["--shadow-flat"], "0 1px 0 #ffffff")
        self.assertEqual(out["skipped"], [])
        root, dark = catalog.export_css(out).split('[data-theme="dark"]')
        self.assertIn("--shadow-lip: 0 4px 0 #e5e5e5;", root)
        self.assertIn("--shadow-lip: 0 4px 0 #37464f;", dark)

    def test_shared_token_missing_from_a_theme_is_skipped_not_leaked(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}, "gone": {"$value": "{nowhere}"}},
            "light": {"focus": {"$value": "#3399ff"}},
            "dark": {"text": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertNotIn("--ring", out["themes"]["light"])
        self.assertNotIn("--ring", out["themes"]["dark"])
        self.assertEqual(out["unresolved"], ["core.ring", "core.gone"])
        self.assertEqual(out["skipped"], [])
        self.assertNotIn("--ring:", catalog.export_css(out))

    def test_broken_reference_is_unresolved_not_composite(self):
        tokens = {
            "core": {"gray": {"0": {"$value": "#ffffff"}},
                     "type": {"body": {"$value": {"fontFamily": "Inter", "fontSize": "14px"}}}},
            "light": {"text": {"$value": "{gray.missing}"},
                      "shadow": {"$value": {"offsetX": "0", "offsetY": "1px", "blur": "2px", "color": "{gray.nope}"}},
                      "ok": {"$value": "{gray.0}"}},
        }
        out = catalog.export_tokens(tokens, ["light"])
        self.assertEqual(out["unresolved"], ["light.text", "light.shadow"])
        self.assertEqual(out["skipped"], ["core.type.body"])
        self.assertEqual(out["themes"]["light"], {"--ok": "#ffffff"})
        css = catalog.export_css(out)
        self.assertIn("2 tokens not exported because a reference points at nothing: light.text, light.shadow", css)
        self.assertIn("1 composite tokens", css)
        self.assertNotIn("None", css)

    def test_unresolved_path_cannot_close_the_css_comment(self):
        out = catalog.export_tokens({"light": {"x*/y": {"$value": "{nowhere}"}}}, ["light"])
        css = catalog.export_css(out)
        self.assertEqual(out["unresolved"], ["light.x*/y"])
        self.assertEqual(css.count("*/"), css.count("/*"))

    def test_theme_own_token_wins_over_shared_core_token(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}},
            "light": {"focus": {"$value": "#000000"}, "ring": {"$value": "#ff0000"}},
            "dark": {"focus": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--ring"], "#ff0000")
        self.assertEqual(out["themes"]["dark"]["--ring"], "#ffffff")

    def test_theme_own_broken_token_is_not_replaced_by_the_shared_one(self):
        tokens = {
            "core": {"ring": {"$value": "{focus}"}},
            "light": {"focus": {"$value": "#000000"}, "ring": {"$value": "{nowhere}"}},
            "dark": {"focus": {"$value": "#ffffff"}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertNotIn("--ring", out["themes"]["light"])
        self.assertEqual(out["themes"]["dark"]["--ring"], "#ffffff")
        self.assertEqual(out["unresolved"], ["light.ring"])
        self.assertEqual(out["skipped"], [])

    def test_theme_token_with_the_same_css_name_wins_whatever_the_set_order(self):
        tokens = {
            "light": {"focus": {"$value": "#000000"}, "foo-bar": {"$value": "#ff0000"}},
            "dark": {"focus": {"$value": "#ffffff"}},
            "core": {"foo": {"bar": {"$value": "{focus}"}}},
        }
        out = catalog.export_tokens(tokens, ["light", "dark"])
        self.assertEqual(out["themes"]["light"]["--foo-bar"], "#ff0000")
        self.assertEqual(out["themes"]["dark"]["--foo-bar"], "#ffffff")

    def test_duolingo_lip_shadows_follow_the_theme(self):
        system = next(s for s in catalog.load_catalog()["systems"] if s["slug"] == "duolingo")
        out = catalog.export_tokens(json.loads((catalog.ROOT / system["tokens"]).read_text()), system["themes"])
        self.assertEqual([p for p in out["skipped"] if p.startswith("core.shadow.lip.")], [])
        light, dark = out["themes"]["light"], out["themes"]["dark"]
        names = [n for n in light if n.startswith("--shadow-lip-")]
        self.assertEqual(len(names), 9)
        self.assertEqual(sorted(n for n in dark if n.startswith("--shadow-lip-")), sorted(names))
        self.assertFalse(any(n.startswith("--shadow-lip-") for n in out["base"]))
        self.assertEqual(light["--shadow-lip-outline"], "0px 2px 0px 0px #e5e5e5")
        self.assertEqual(dark["--shadow-lip-outline"], "0px 2px 0px 0px #37464f")

    def test_every_package_exports(self):
        for s in catalog.load_catalog()["systems"]:
            out = catalog.export_tokens(json.loads((catalog.ROOT / s["tokens"]).read_text()), s["themes"])
            self.assertTrue(out["base"] or any(out["themes"].values()), s["slug"])


class CssValueTest(unittest.TestCase):
    def test_shadow_layers_with_alias_colour(self):
        res = catalog.Resolver({
            "core": {"blue": {"$value": "#2a78d6"}},
            "light": {"focus": {"$value": [
                {"color": "#ffffff", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "inset": True},
                {"color": "{blue}", "offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "0px"}]}},
        })
        self.assertEqual(catalog.css_value(res.final("light.focus")),
                         "inset 0px 0px 0px 1px #ffffff, 0px 2px 4px 0px #2a78d6")

    def test_cubic_bezier(self):
        self.assertEqual(catalog.css_value([0.2, 0, 0, 1]), "cubic-bezier(0.2, 0, 0, 1)")

    def test_font_stack_quotes_names_that_need_it(self):
        self.assertEqual(catalog.css_value(["Inter Variable", "SF Pro 2", "sans-serif"]),
                         'Inter Variable, "SF Pro 2", sans-serif')

    def test_dimension_object(self):
        self.assertEqual(catalog.css_value({"value": 4, "unit": "px"}), "4px")

    def test_typography_and_booleans_have_no_css_form(self):
        self.assertIsNone(catalog.css_value({"fontSize": "14px", "fontWeight": 400}))
        self.assertIsNone(catalog.css_value(True))

    def test_no_package_exports_python_reprs_or_bare_number_lists(self):
        bad = re.compile(r"\{'|: -?[0-9.]+, -?[0-9.]+, |\b(True|False|None)\b")
        for s in catalog.load_catalog()["systems"]:
            out = catalog.export_tokens(json.loads((catalog.ROOT / s["tokens"]).read_text()), s["themes"])
            lines = [line for line in catalog.export_css(out).splitlines() if bad.search(line)]
            self.assertEqual(lines, [], s["slug"])


class ContrastTest(unittest.TestCase):
    TOKENS = {
        "core": {"white": {"$value": "#ffffff"}, "black": {"$value": "#000000"}},
        "light": {
            "page": {"$value": "{white}"},
            "text": {"$value": "{black}"},
            "faint": {"$value": "#cccccc"},
            "ink-50": {"$value": "rgba(0, 0, 0, 0.5)"},
            "glass": {"$value": "rgba(255, 255, 255, 0.5)"},
        },
    }

    def status(self, pairs, over=None):
        return [r["status"] for r in catalog.contrast(self.TOKENS, "light", pairs, over)]

    def test_black_on_white_is_21(self):
        self.assertEqual(catalog.contrast(self.TOKENS, "light", ["text:page"])[0]["ratio"], 21.0)

    def test_fail_and_large_text_threshold(self):
        self.assertEqual(self.status(["faint:page", "faint:page@3"]), ["fail", "fail"])
        self.assertEqual(self.status(["ink-50:page@3"]), ["pass"])

    def test_just_under_threshold_fails_and_does_not_display_as_threshold(self):
        tokens = {"light": {"page": {"$value": "#ffffff"}, "grey": {"$value": "rgb(118.7, 118.7, 118.7)"}}}
        row = catalog.contrast(tokens, "light", ["grey:page"])[0]
        self.assertEqual(row["status"], "fail")
        self.assertLess(row["ratio"], 4.5)

    def test_translucent_background_needs_a_backdrop(self):
        self.assertEqual(self.status(["text:glass"]), ["unchecked"])
        self.assertEqual(self.status(["text:glass"], over="page"), ["pass"])

    def test_missing_token(self):
        self.assertEqual(self.status(["nope:page"]), ["missing"])

    def test_parse_colour_forms(self):
        self.assertEqual(catalog.parse_colour("#fff"), (255, 255, 255, 1.0))
        self.assertEqual(catalog.parse_colour("rgba(0, 0, 0, 0.5)"), (0.0, 0.0, 0.0, 0.5))
        self.assertIsNone(catalog.parse_colour("red"))


class ScanTest(unittest.TestCase):
    def test_finds_redacted_text_and_signed_urls_without_printing_them(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "README.md").write_text("fine\nSigned in as Jane Doe\n")
            (Path(d) / "raw.json").write_text('{"u": "https://cdn/x.png?X-Amz-Signature=abc"}')
            (Path(d) / "shot.png").write_bytes(b"Jane Doe")
            hits = catalog.scan(Path(d), {"replace": [["jane\\s+doe", "i", "A User"]]})
        self.assertEqual(len(hits), 2)
        self.assertTrue(hits[0].endswith("README.md:2: redaction pattern 1"))
        self.assertTrue(hits[1].endswith("raw.json:1: signed URL"))
        self.assertFalse(any("Jane" in h for h in hits))


class ScanFailsLoudlyTest(unittest.TestCase):
    def test_missing_or_empty_folder_is_an_error_not_clean(self):
        import tempfile
        with self.assertRaises(SystemExit):
            catalog.scan(Path("/no/such/folder"), {"replace": []})
        with tempfile.TemporaryDirectory() as d, self.assertRaises(SystemExit):
            catalog.scan(Path(d), {"replace": []})


class FindTest(unittest.TestCase):
    def test_tag_hit_outranks_description_hit(self):
        hits = catalog.find(["ios"])
        self.assertEqual(hits[0]["slug"], "hevy")

    def test_no_words_lists_everything(self):
        self.assertEqual(len(catalog.find([])), len(catalog.load_catalog()["systems"]))


class DesignMdValueTest(unittest.TestCase):
    def test_dimensions_become_px_rem_or_em(self):
        self.assertEqual(catalog.md_dimension(16), "16px")
        self.assertEqual(catalog.md_dimension("0"), "0px")
        self.assertEqual(catalog.md_dimension(".125rem"), "0.125rem")
        self.assertEqual(catalog.md_dimension({"value": 4, "unit": "px"}), "4px")
        self.assertEqual(catalog.md_dimension("-0.25rem"), "-0.25rem")
        self.assertIsNone(catalog.md_dimension("50%"))
        self.assertIsNone(catalog.md_dimension("auto"))
        self.assertIsNone(catalog.md_dimension("12pt"))
        self.assertEqual(catalog.md_dimension("-2%", percent_as_em=True), "-0.02em")

    def test_line_height_percent_is_a_multiplier(self):
        self.assertEqual(catalog.md_line_height("140%"), 1.4)
        self.assertEqual(catalog.md_line_height(1.25), 1.25)
        self.assertEqual(catalog.md_line_height("1.5"), 1.5)
        self.assertEqual(catalog.md_line_height("24px"), "24px")
        self.assertIsNone(catalog.md_line_height("normal"))

    def test_font_weight_and_family(self):
        self.assertEqual(catalog.md_font_weight("450"), 450)
        self.assertEqual(catalog.md_font_weight("Semi-Bold"), 600)
        self.assertIsNone(catalog.md_font_weight("heavier"))
        self.assertEqual(catalog.first_family(["Inter Variable", "sans-serif"]), "Inter Variable")
        self.assertEqual(catalog.first_family("'Gauth Home', Georgia, serif"), "Gauth Home")

    def test_colours_the_linter_accepts(self):
        self.assertEqual(catalog.md_colour("#0000001a"), "#0000001a")
        self.assertEqual(catalog.md_colour("rgba(0, 0, 0, 0.5)"), "rgba(0, 0, 0, 0.5)")
        self.assertEqual(catalog.md_colour("transparent"), "transparent")
        self.assertIsNone(catalog.md_colour("currentColor"))
        self.assertIsNone(catalog.md_colour("linear-gradient(#fff, #000)"))

    def test_yaml_quotes_keys_that_would_not_stay_strings(self):
        lines = catalog.to_yaml({"spacing": {"2": "8px", "on": "1px", "sm": "4px"},
                                 "omitted": [{"section": "rounded", "reason": "none"}]})
        self.assertIn('  "2": "8px"', lines)
        self.assertIn('  "on": "1px"', lines)
        self.assertIn('  sm: "4px"', lines)
        self.assertIn('  - section: "rounded"', lines)
        self.assertIn('    reason: "none"', lines)


class DesignMdMappingTest(unittest.TestCase):
    TOKENS = {
        "core": {
            "palette": {"green": {"$value": "#29cc57"}, "white": {"$value": "#ffffff"}},
            "fontFamily": {"ui": {"$value": ["CoFo Brilliant", "sans-serif"]}},
            "typography": {"heading": {"large": {"$type": "typography", "$value": {
                "fontFamily": "{fontFamily.ui}", "fontSize": "28px", "fontWeight": "bold",
                "lineHeight": "140%", "letterSpacing": "0px", "textCase": "uppercase"}}}},
            "radius": {"md": {"$value": "8px"}, "circle": {"$value": "50%"}},
            "spacing": {"0.5": {"$value": ".125rem"}, "4": {"$value": "1rem"}},
        },
        "light": {
            "bg": {"page": {"$value": "{palette.white}"}, "card": {"$value": "#f8f8f8"}},
            "text": {"primary": {"$value": "#000000"}, "muted": {"$value": "#00000099"}},
            "border": {"default": {"$value": "#0000001a"}},
            "accent": {"$value": "{palette.green}"},
            "gradient": {"hero": {"$value": "linear-gradient(#fff, #000)"}},
            "shadow": {"card": {"$type": "shadow", "$value": {
                "color": "#0000001a", "offsetX": "0px", "offsetY": "4px", "blur": "8px", "spread": "0px"}}},
            "component": {"button": {"primary-bg": {"$value": "{accent}"},
                                     "primary-text": {"$value": "#ffffff"},
                                     "primary-hover": {"$value": "#15b441"},
                                     "primary-radius": {"$value": "12px"}}},
        },
        "dark": {"bg": {"page": {"$value": "#000000"}}},
    }
    SYSTEM = {"slug": "x", "name": "X", "goodFor": "Testing", "themes": ["light", "dark"],
              "tokens": "systems/x/tokens.json",
              "preview": {"swatches": {"light": {
                  "page": "light.bg.page", "surface": "light.bg.card", "text": "light.text.primary",
                  "muted": "light.text.muted", "accent": "light.accent", "border": "light.border.default"}}}}

    def setUp(self):
        self.out = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(self.TOKENS))
        self.front = self.out["front"]

    def test_roles_come_from_the_swatches_with_aliases_resolved(self):
        colors = self.front["colors"]
        self.assertEqual(colors["primary"], "#29cc57")
        self.assertEqual(colors["neutral"], "#ffffff")
        self.assertEqual(colors["on-surface-variant"], "#00000099")
        self.assertEqual(self.out["roleFrom"]["primary"], "light.accent")

    def test_every_light_colour_is_named_by_its_path_and_dark_is_left_out(self):
        colors = self.front["colors"]
        self.assertEqual(colors["bg-page"], "#ffffff")
        self.assertEqual(colors["component-button-primary-bg"], "#29cc57")
        self.assertNotIn("#000000", [v for k, v in colors.items() if k.startswith("bg-")])
        self.assertIn("light.gradient.hero", self.out["skipped"])

    def test_typography_from_core_converted(self):
        self.assertEqual(self.front["typography"]["heading-large"], {
            "fontFamily": "CoFo Brilliant", "fontSize": "28px", "fontWeight": 700,
            "lineHeight": 1.4, "letterSpacing": "0px"})

    def test_scales_drop_what_has_no_px_rem_or_em_form(self):
        self.assertEqual(self.front["rounded"], {"md": "8px"})
        self.assertIn("core.radius.circle", self.out["skipped"])
        self.assertEqual(self.front["spacing"], {"0-5": "0.125rem", "4": "1rem"})
        self.assertNotIn("omitted", self.front)

    def test_components_keep_only_properties_design_md_defines(self):
        self.assertEqual(self.front["components"], {"button-primary": {
            "backgroundColor": "{colors.component-button-primary-bg}",
            "textColor": "{colors.component-button-primary-text}",
            "rounded": "12px"}})

    def test_shadows_go_to_the_body(self):
        self.assertEqual(self.out["shadows"], [("light.shadow.card", "0px 4px 8px 0px #0000001a")])

    def test_shared_core_shadow_resolves_against_the_theme(self):
        tokens = json.loads(json.dumps(self.TOKENS))
        tokens["core"]["shadow"] = {"lip": {"$type": "shadow", "$value": {
            "color": "{border.default}", "offsetX": "0px", "offsetY": "2px", "blur": "0px", "spread": "0px"}}}
        shadows = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(tokens))["shadows"]
        self.assertIn(("core.shadow.lip", "0px 2px 0px 0px #0000001a"), shadows)

    def test_missing_group_is_listed_as_omitted(self):
        tokens = json.loads(json.dumps(self.TOKENS))
        del tokens["core"]["radius"]
        front = catalog.design_md_tokens(self.SYSTEM, catalog.Resolver(tokens))["front"]
        self.assertEqual([o["section"] for o in front["omitted"]], ["rounded"])
        self.assertNotIn("rounded", front)

    def test_override_reads_split_typography_and_keeps_token_names(self):
        tokens = {"light": {
            "color": {"color-bg": {"value": "#f1f1f1"}, "color-text": {"value": "#303030"}},
            "space": {"space-100": {"value": "0.25rem"}},
            "text": {"text-body-md-font-family": {"value": "'Inter', sans-serif"},
                     "text-body-md-font-size": {"value": "0.8125rem"},
                     "text-body-md-font-weight": {"value": "450"},
                     "text-body-md-font-line-height": {"value": "1.25rem"}}}}
        roles = {r: "light.color.color-bg" for r in catalog.SWATCH_ROLES}
        system = {**self.SYSTEM, "themes": ["light"], "preview": {"swatches": {"light": roles}},
                  "designMd": {"colors": "light.color.", "typography": "light.text.text-",
                               "spacing": "light.space."}}
        front = catalog.design_md_tokens(system, catalog.Resolver(tokens))["front"]
        self.assertEqual(front["colors"]["color-text"], "#303030")
        self.assertEqual(front["spacing"], {"space-100": "0.25rem"})
        self.assertEqual(front["typography"], {"text-body-md": {
            "fontFamily": "Inter", "fontSize": "0.8125rem", "fontWeight": 450, "lineHeight": "1.25rem"}})


class DesignMdDocumentTest(unittest.TestCase):
    SECTIONS = ["Overview", "Colors", "Typography", "Layout", "Elevation & Depth", "Shapes",
                "Components", "Do's and Don'ts"]

    def test_readme_parts_demote_headings_and_drop_intro_tables(self):
        intro, parts = catalog.readme_parts(
            "# T\n\nIntro.\n\n| a | b |\n|---|---|\n\n## Fonts\n\n### Sans\n\n```bash\n# comment\n```\n")
        self.assertEqual(intro, "Intro.")
        self.assertEqual(parts, [("Fonts", "#### Sans\n\n```bash\n# comment\n```")])

    def test_readme_do_and_dont_list_goes_under_dos_and_donts(self):
        _, parts = catalog.readme_parts("# T\n\n## Do and don't\n\n1. **Do one thing.**\n")
        self.assertEqual(catalog._readme_for("Do's and Don'ts", parts),
                         "### Do and don't (from README.md)\n\n1. **Do one thing.**")

    def test_every_package_has_the_spec_sections_in_order_and_points_at_its_tokens(self):
        for s in catalog.load_catalog()["systems"]:
            with self.subTest(s["slug"]):
                text = catalog.design_md(s)
                front, body = text.split("\n---\n", 1)
                self.assertTrue(front.startswith("---\n# Generated by tools/catalog.py"))
                self.assertIn('version: "alpha"', front)
                self.assertIn("primary:", front)
                headings = re.findall(r"^## (.+)$", body, re.M)
                self.assertEqual(headings, self.SECTIONS)
                tokens_rel = Path(s["tokens"]).relative_to(f"systems/{s['slug']}").as_posix()
                self.assertIn(f"[{tokens_rel}]({tokens_rel}) is the source of truth", body)
                self.assertNotIn("—", text.split("## Overview")[0])

    def test_stale_or_missing_file_is_a_problem(self):
        import tempfile
        system = catalog.load_catalog()["systems"][0]
        original = catalog.design_md_path
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "DESIGN.md"
            catalog.design_md_path = lambda s: target
            try:
                self.assertIn("missing", catalog.design_md_problems(system)[0])
                target.write_text("hand edited\n")
                self.assertIn("out of date", catalog.design_md_problems(system)[0])
                target.write_text(catalog.design_md(system))
                self.assertEqual(catalog.design_md_problems(system), [])
            finally:
                catalog.design_md_path = original

    def test_missing_readme_is_reported_not_raised(self):
        system = {**catalog.load_catalog()["systems"][0], "slug": "no-such-package"}
        problems = catalog.design_md_problems(system)
        self.assertEqual(len(problems), 1)
        self.assertIn("cannot generate DESIGN.md without systems/no-such-package/README.md", problems[0])

    def test_incomplete_palette_or_themes_is_reported_not_raised(self):
        base = catalog.load_catalog()["systems"][0]
        roles = dict(next(iter(base["preview"]["swatches"].values())))
        del roles["accent"]
        broken = [
            {**base, "preview": {**base["preview"], "swatches": {base["themes"][0]: roles}}},
            {**base, "preview": {**base["preview"], "swatches": {}}},
            {**base, "themes": []},
        ]
        for system in broken:
            problems = catalog.design_md_problems(system)
            self.assertEqual(len(problems), 1)
            self.assertIn("cannot generate DESIGN.md until themes and preview.swatches are complete", problems[0])

    def test_generation_error_is_reported_not_raised(self):
        from unittest import mock
        system = catalog.load_catalog()["systems"][0]
        with mock.patch.object(catalog, "design_md", side_effect=KeyError("page")):
            problems = catalog.design_md_problems(system)
        self.assertEqual(problems, [f"{system['slug']}: DESIGN.md generation failed: KeyError: 'page'"])

    def test_malformed_override_is_reported_not_raised(self):
        base = catalog.load_catalog()["systems"][0]
        for bad in ({"spacing": None}, {"spacing": [7]}, {"spacing": []}, {"spacing": ""}):
            problems = catalog.design_md_problems({**base, "designMd": bad})
            self.assertEqual(problems, [f"{base['slug']}: designMd.spacing must be a prefix string "
                                        "or a non-empty list of them"], bad)
        self.assertIn("must be an object", catalog.design_md_problems({**base, "designMd": ["x"]})[0])

    def test_bad_override_prefix_is_a_problem(self):
        system = {**catalog.load_catalog()["systems"][0], "designMd": {"spacing": "core.nope."}}
        self.assertIn("matches no token", catalog.design_md_problems(system)[0])


class DesignMdLintTest(unittest.TestCase):
    """lint_design_md's pass/fail rules, with the linter replaced by canned output."""

    def lint(self, stdout, stderr=""):
        from unittest import mock
        done = mock.Mock(stdout=stdout, stderr=stderr)
        path = catalog.ROOT / "systems" / "duolingo" / "DESIGN.md"
        with mock.patch.object(catalog.shutil, "which", return_value="/usr/bin/npx"), \
                mock.patch.object(catalog.subprocess, "run", return_value=done) as run:
            problems, counts = catalog.lint_design_md([path])
        self.assertIn(catalog.DESIGN_MD_LINTER, run.call_args.args[0])
        return problems, counts["systems/duolingo/DESIGN.md"] if counts else None

    @staticmethod
    def report(*findings):
        return json.dumps({"findings": [dict(zip(("severity", "rule", "message"), f)) for f in findings]})

    def test_clean_and_info_only(self):
        self.assertEqual(self.lint(self.report(("info", "token-summary", "3 colors"))), ([], {}))

    def test_allowed_warnings_are_counted_not_failed(self):
        problems, tally = self.lint(self.report(("warning", "orphaned-tokens", "a"), ("warning", "orphaned-tokens", "b"),
                                                ("warning", "contrast-ratio", "c")))
        self.assertEqual(problems, [])
        self.assertEqual(tally, {"orphaned-tokens warning": 2, "contrast-ratio warning": 1})

    def test_other_warnings_and_errors_fail(self):
        problems, _ = self.lint(self.report(("warning", "section-order", "out of order"),
                                            ("error", "broken-ref", "no such token")))
        self.assertEqual(len(problems), 2)
        self.assertIn("section-order", problems[0])
        self.assertIn("broken-ref", problems[1])

    def test_error_without_a_rule_fails_even_in_an_allowed_rule_list(self):
        problems, tally = self.lint(json.dumps({"findings": [{"severity": "error", "message": "bad colour"}]}))
        self.assertEqual(tally, {"parse error": 1})
        self.assertIn("error parse", problems[0])

    def test_unreadable_output_fails(self):
        problems, tally = self.lint("npm ERR! network", stderr="npm ERR! 404")
        self.assertIsNone(tally)
        self.assertIn("linter failed: npm ERR! 404", problems[0])

    def test_no_npx_is_a_clear_exit(self):
        from unittest import mock
        with mock.patch.object(catalog.shutil, "which", return_value=None), self.assertRaises(SystemExit):
            catalog.lint_design_md([])


class LayoutTest(unittest.TestCase):
    """layout_problems against a package folder built in a temporary repository."""

    def problems(self, entries, readme_rows, gaps=None):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "systems" / "x"
            folder.mkdir(parents=True)
            for entry in entries:
                if entry.endswith("/"):
                    (folder / entry).mkdir()
                else:
                    (folder / entry).write_text("")
            rows = "\n".join(f"| [{r}]({r}) | what it is |" for r in readme_rows)
            (folder / "README.md").write_text(f"# X\n\n| File | What |\n|---|---|\n{rows}\n\n## Fonts\n")
            system = {"slug": "x"} | ({"layoutGaps": gaps} if gaps is not None else {})
            with mock.patch.object(catalog, "ROOT", Path(tmp)):
                return catalog.layout_problems(system)

    FULL = [p for p in catalog.STANDARD_PARTS if p != "README.md"]

    def test_a_full_listed_package_is_clean(self):
        self.assertEqual(self.problems(self.FULL, self.FULL), [])

    def test_an_undeclared_missing_part_fails(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertEqual(self.problems(parts, parts), ["x: no icons/; add it, or declare it under layoutGaps with the reason"])

    def test_a_declared_gap_passes_and_a_stale_one_fails(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertEqual(self.problems(parts, parts, {"icons/": "rights"}), [])
        self.assertIn("layoutGaps declares raw/", self.problems(self.FULL, self.FULL, {"raw/": "gone"})[0])

    def test_a_gap_needs_a_reason(self):
        parts = [p for p in self.FULL if p != "icons/"]
        self.assertIn("reason", self.problems(parts, parts, {"icons/": ""})[0])

    def test_a_file_where_a_folder_belongs_counts_as_missing(self):
        parts = [p for p in self.FULL if p != "raw/"] + ["raw"]
        self.assertIn("x: no raw/; add it", self.problems(parts, parts)[0])

    def test_what_git_ignores_is_not_part_of_the_package(self):
        import subprocess
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("systems/*/fonts/\nsystems/*/raw/\n")
            folder = root / "systems" / "x"
            folder.mkdir(parents=True)
            for entry in self.FULL + ["fonts/"]:
                (folder / entry).mkdir() if entry.endswith("/") else (folder / entry).write_text("")
            rows = "\n".join(f"| [{r}]({r}) | what it is |" for r in self.FULL)
            (folder / "README.md").write_text(f"# X\n\n| File | What |\n|---|---|\n{rows}\n")
            with mock.patch.object(catalog, "ROOT", root):
                missing, unlisted = catalog.layout_gaps("x")
        self.assertEqual(unlisted, [])
        self.assertEqual(missing, ["raw/"])

    def test_an_extra_entry_needs_a_row(self):
        self.assertEqual(self.problems(self.FULL + ["graph.md"], self.FULL),
                         ["x: graph.md has no row in the README's file table"])
        self.assertEqual(self.problems(self.FULL + ["graph.md"], self.FULL + ["graph.md"]), [])


class SectionDataTest(unittest.TestCase):
    """The gallery's per-section data matches DESIGN.md and the catalog."""

    def system(self, slug):
        return next(s for s in catalog.load_catalog()["systems"] if s["slug"] == slug)

    def test_scales_match_design_md(self):
        for s in catalog.load_catalog()["systems"]:
            with self.subTest(slug=s["slug"]):
                data, md = catalog.section_data(s), catalog.design_md_tokens(s)
                front = md["front"]
                self.assertEqual(data["tokenTheme"], md["theme"])
                self.assertEqual([t["name"] for t in data["typeStyles"]], list(front.get("typography", {})))
                self.assertEqual({r["name"]: r["value"] for r in data["radii"]}, front.get("rounded", {}))
                self.assertEqual({r["name"]: r["value"] for r in data["spacing"]}, front.get("spacing", {}))
                self.assertEqual([(x["token"], x["css"]) for x in data["shadows"]], md["shadows"])
                self.assertEqual(data["layoutGaps"], s.get("layoutGaps", {}))

    def test_type_style_fields(self):
        style = catalog.section_data(self.system("claude"))["typeStyles"][0]
        self.assertEqual(set(style), {"name", "family", "size", "weight", "lineHeight", "letterSpacing"})
        self.assertTrue(style["size"].endswith("px"))

    def test_icons_are_capped_sorted_images_with_a_total(self):
        icons = catalog.section_data(self.system("polaris"))["icons"]
        self.assertGreater(icons["total"], catalog.ICON_LIMIT)
        self.assertEqual(len(icons["items"]), catalog.ICON_LIMIT)
        self.assertEqual(icons["items"], sorted(icons["items"]))
        self.assertTrue(all(p.startswith("systems/polaris/icons/") and p.endswith(".svg") for p in icons["items"]))

    def test_missing_parts_carry_their_reason(self):
        hevy = catalog.section_data(self.system("hevy"))
        self.assertEqual(hevy["icons"], {"total": 0, "items": []})
        self.assertIn("icons/", hevy["layoutGaps"])
        self.assertEqual(hevy["shadows"], [])

    def test_omitted_scale_gives_the_generator_reason(self):
        s = copy.deepcopy(self.system("hevy"))
        s["designMd"] = {"spacing": "core.nothing-here."}
        data = catalog.section_data(s)
        self.assertEqual(data["spacing"], [])
        self.assertIn("spacing", data["omitted"]["spacing"])


class ReferoBuildTest(unittest.TestCase):
    """build_refero emits refero/index.json plus one refero/style/<slug>.json per
    style, from a refero/ tree built in a temporary repository."""

    def make(self, root, slug, meta, ds, docs=True):
        folder = root / "refero" / slug
        folder.mkdir(parents=True)
        (folder / "meta.json").write_text(json.dumps(meta))
        if ds is not None:
            (folder / "design-system.json").write_text(json.dumps(ds))
        if docs:
            (folder / "DESIGN.md").write_text("# Designed\n")
            (folder / "variables.css").write_text(":root {}")
            (folder / "theme.css").write_text("body {}")
            (folder / "tokens.json").write_text("{}")
        return folder

    def build(self, styles):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "docs" / "gallery"
            for slug, meta, ds in styles:
                self.make(root, slug, meta, ds)
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "SITE", site):
                out = catalog.build_refero()
            return json.loads(out.read_text()), {
                p.stem: json.loads(p.read_text()) for p in site.glob("refero/style/*.json")}

    ALPHA = {"slug": "alpha", "name": "Alpha", "tagline": "tag", "theme": "light",
             "product_type": "devtools", "design_style": "technical", "tags": ["neon"],
             "source_url": "https://www.alpha.example.com/x", "page_url": "https://p/alpha",
             "extracted_at": "t0", "screenshot_url": "https://img/shot.jpg",
             "video_url": "https://img/v.mp4", "video_poster_url": "https://img/p.jpg"}
    ALPHA_DS = {"meta": {"thumbnailUrl": "https://img/t.jpg"}, "industry": "media",
                "similar": [{"business": "Beta", "why": "same"}, {"business": "Nobody", "why": "none"}]}
    BETA = {"slug": "beta", "name": "beta", "source_url": "https://beta.io"}
    BETA_DS = {"industry": "other"}

    def test_index_rows_and_name_sort(self):
        index, _ = self.build([("beta", self.BETA, self.BETA_DS), ("alpha", self.ALPHA, self.ALPHA_DS)])
        self.assertEqual(index["version"], 1)
        self.assertEqual(index["count"], 2)
        alpha, beta = index["styles"]
        self.assertEqual([s["slug"] for s in index["styles"]], ["alpha", "beta"])
        self.assertEqual(alpha["src"], "alpha.example.com")
        self.assertEqual(alpha["card"], "/refero-media/posters/alpha.jpg")
        self.assertEqual(alpha["cardRemote"], "https://img/p.jpg")
        self.assertTrue(alpha["video"])
        self.assertEqual(beta["industry"], "other")
        self.assertEqual(alpha["type"], "devtools")
        self.assertEqual(alpha["style"], "technical")
        self.assertEqual(alpha["tags"], ["neon"])
        self.assertIsNone(beta["type"])
        self.assertEqual(beta["tags"], [])
        self.assertIsNone(beta["card"])
        self.assertIsNone(beta["cardRemote"])
        self.assertFalse(beta["video"])

    def test_card_remote_falls_back_to_thumbnail_then_shot(self):
        meta = {**self.BETA, "screenshot_url": "https://img/s.jpg"}
        index, _ = self.build([("beta", meta, {"meta": {"thumbnailUrl": "https://img/t.jpg"}})])
        self.assertEqual(index["styles"][0]["card"], "/refero-media/shots/beta.jpg")
        self.assertEqual(index["styles"][0]["cardRemote"], "https://img/t.jpg")

    def test_entry_file_media_docs_ds_and_similar(self):
        _, files = self.build([("beta", self.BETA, self.BETA_DS), ("alpha", self.ALPHA, self.ALPHA_DS)])
        alpha = files["alpha"]
        self.assertEqual(alpha["theme"], "light")
        self.assertEqual(alpha["industry"], "media")
        self.assertEqual(alpha["type"], "devtools")
        self.assertEqual(alpha["style"], "technical")
        self.assertEqual(alpha["source_url"], "https://www.alpha.example.com/x")
        self.assertEqual(alpha["media"]["shot"],
                         {"local": "/refero-media/shots/alpha.jpg", "remote": "https://img/shot.jpg"})
        self.assertEqual(alpha["media"]["video"]["remote"], "https://img/v.mp4")
        self.assertIsNone(alpha["media"]["detail"])
        self.assertIn("url=https://alpha.example.com", alpha["media"]["favicon"]["remote"])
        self.assertEqual(alpha["media"]["favicon"]["local"], "/refero-media/favicons/alpha.png")
        self.assertEqual(alpha["docs"]["design_md"], "# Designed\n")
        self.assertEqual(alpha["docs"]["tokens_json"], "{}")
        self.assertNotIn("meta", alpha["ds"])
        self.assertEqual(alpha["similar"], [{"slug": "beta", "name": "Beta", "why": "same"},
                                            {"slug": None, "name": "Nobody", "why": "none"}])
        self.assertIsNone(files["beta"]["media"]["shot"])

    def test_a_folder_without_both_files_is_skipped(self):
        import tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            root, site = Path(tmp), Path(tmp) / "docs" / "gallery"
            self.make(root, "alpha", self.ALPHA, self.ALPHA_DS)
            broken = root / "refero" / "broken"
            broken.mkdir(parents=True)
            (broken / "meta.json").write_text("{}")
            with mock.patch.object(catalog, "ROOT", root), mock.patch.object(catalog, "SITE", site):
                out = catalog.build_refero()
            index = json.loads(out.read_text())
        self.assertEqual(index["count"], 1)
        self.assertEqual([s["slug"] for s in index["styles"]], ["alpha"])

    def test_a_style_named_index_gets_an_entity_file(self):
        # refero/index is a real style; under refero/style/ it cannot collide
        # with the index.
        index, files = self.build([("index", {**self.BETA, "slug": "index", "name": "index"}, self.BETA_DS)])
        self.assertEqual(index["count"], 1)
        self.assertEqual(index["styles"][0]["slug"], "index")
        self.assertEqual(files["index"]["slug"], "index")


class RepositoryTest(unittest.TestCase):
    def test_catalog_checks_clean(self):
        self.assertEqual(catalog.check(), [])

    def test_platform_is_required_and_must_be_known(self):
        import copy
        from unittest import mock
        data = copy.deepcopy(catalog.load_catalog())
        first, second = data["systems"][0], data["systems"][1]
        first["platform"] = "tv"
        del second["platform"]
        with mock.patch.object(catalog, "load_catalog", return_value=data):
            problems = catalog.check()
        self.assertEqual(problems, [f"{first['slug']}: platform 'tv' is not one of web, mobile, desktop",
                                    f"{second['slug']}: missing field platform"])

    def test_every_platform_in_the_catalog_is_known(self):
        platforms = {s["slug"]: s["platform"] for s in catalog.load_catalog()["systems"]}
        self.assertTrue(set(platforms.values()) <= set(catalog.PLATFORMS))
        self.assertEqual(platforms["hevy"], "mobile")

    def test_image_tags_come_from_path_words(self):
        self.assertEqual(catalog._tags_for(Path("screenshots/dark/d01-home.png")), ["dark"])
        self.assertEqual(catalog._tags_for(Path("screenshots/mobile-login-light-default.png")),
                         ["light", "mobile"])



class RepoFileTest(unittest.TestCase):
    def test_allowed_paths_map_into_the_checkout(self):
        self.assertEqual(catalog.repo_file("/catalog.json"), (catalog.ROOT / "catalog.json").resolve())
        self.assertEqual(catalog.repo_file("/systems/claude/README.md?x=1"),
                         (catalog.ROOT / "systems/claude/README.md").resolve())

    def test_parent_segments_cannot_leave_the_allowed_folders(self):
        for path in ("/tools/../../../../etc/passwd", "/tools/%2e%2e/%2e%2e/etc/passwd",
                     "/systems/../AGENTS.md", "/systems/..%2f..%2fetc/passwd"):
            target = catalog.repo_file(path)
            self.assertTrue(target is None or catalog.ROOT.resolve() in target.parents, path)
            self.assertNotEqual(target, (catalog.ROOT / "AGENTS.md").resolve(), path)

    def test_other_paths_are_left_to_the_built_site(self):
        self.assertIsNone(catalog.repo_file("/gallery/index.html"))
        self.assertIsNone(catalog.repo_file("/"))


if __name__ == "__main__":
    unittest.main()
