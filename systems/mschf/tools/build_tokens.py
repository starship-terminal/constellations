#!/usr/bin/env python3
"""Build tokens.json from the MSCHF public-index readings.

MSCHF's marketing site (https://mschf.com) ships one dark theme and no
:root token block. The values below are the colours, type sizes and
spacing the live page computed at 1440px and 390px on 2026-11-19, plus
the rules in raw/stylesheets.txt. vw lengths are stored as the px the
browser computed at 1440 (the capture width) and the declared vw is
kept on $extensions.declared. A second theme was not painted, so there
is no dark set: the page ground is black and the ink is grey, and that
pair is the light set the catalog reads.

raw/motion.json, when present, becomes core.motion through motion.py.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion as motion_mod  # noqa: E402


def tok(value, ty, source, **ext):
    out = {"$value": value, "$type": ty, "$extensions": {"source": {"evidence": "Measured", "detail": source}}}
    if ext:
        out["$extensions"].update(ext)
    return out


SRC = "measured on https://mschf.com at 1440x900, 2026-11-19, headless Chromium; declared rule in raw/stylesheets.txt"

# Computed at 1440 from the declared vw (4.51389vw = 65px, 3.88888vw = 56px,
# 1.80556vw = 26px, 1.94444vw = 28px, 0.694444vw = 10px, 0.833333vw = 12px,
# 0.208333vw = 3px, 1.77667vw = 25.584px, 0.98vw = 14.112px).
core = {
    "color": {
        "$description": "The five colours the index paints. There is no ramp.",
        "page": tok("#000000", "color", SRC + "; body background-color rgb(0, 0, 0)"),
        "ink": tok("#84898e", "color", SRC + "; body color rgb(132, 137, 142); utility .text-[#84898E]"),
        "inkHover": tok("#ffffff", "color", SRC + "; a.link:hover and .hover:text-white:hover"),
        "gold": tok("#ffc700", "color", SRC + "; header button background and .links color rgb(255, 199, 0)"),
        "red": tok("#f00007", "color", SRC + "; .row.project-tbd and the logo path fill #F00007"),
        "rule": tok("rgba(168, 145, 65, 0.3)", "color", SRC + "; section.projects-previous and section.projects-new border-color"),
        "linkBlue": tok("#40aaff", "color", SRC + "; the GSCT row computes rgb(64, 170, 255). The same colour is declared on section.subscription, which is not in the DOM"),
        "focus": tok("#005fcc", "color", SRC + "; UA focus-visible outline rgb(0, 95, 204) on header a and header button"),
    },
    "font": {
        "family": {
            "mono": tok("MSCHFSansMono, monospace, Arial, Helvetica, sans-serif", "fontFamily",
                        SRC + "; @font-face MSCHFSansMono from /_nuxt/MSCHFSansMono.DOBS5JtI.otf, weight 400"),
        },
        "weight": {
            "regular": tok("400", "fontWeight", SRC + "; the only loaded face"),
        },
    },
    "typography": {
        "row": tok({
            "fontFamily": "{font.family.mono}",
            "fontWeight": "{font.weight.regular}",
            "fontSize": "65px",
            "lineHeight": "56px",
            "letterSpacing": "0",
        }, "typography", SRC + "; body font-size 4.51389vw computed 65px, line-height 3.88888vw computed 56px, text-transform uppercase",
           declared="4.51389vw / 3.88888vw", textTransform="uppercase"),
        "index": tok({
            "fontFamily": "{font.family.mono}",
            "fontWeight": "{font.weight.regular}",
            "fontSize": "26px",
            "lineHeight": "28px",
            "letterSpacing": "0",
        }, "typography", SRC + "; .row .left font-size 1.80556vw computed 26px, line-height 1.94444vw computed 28px",
           declared="1.80556vw / 1.94444vw"),
        "rowPhone": tok({
            "fontFamily": "{font.family.mono}",
            "fontWeight": "{font.weight.regular}",
            "fontSize": "30.16px",
            "lineHeight": "29.12px",
            "letterSpacing": "-0.905px",
        }, "typography", "measured at 390x844; body font-size 7.73333vw, line-height 7.46667vw, letter-spacing -0.232vw",
           declared="7.73333vw / 7.46667vw / -0.232vw"),
        "indexPhone": tok({
            "fontFamily": "{font.family.mono}",
            "fontWeight": "{font.weight.regular}",
            "fontSize": "15.6px",
            "lineHeight": "14.56px",
            "letterSpacing": "0",
        }, "typography", "measured at 390x844; .row .left font-size 4vw, line-height 3.73333vw",
           declared="4vw / 3.73333vw"),
    },
    "radius": {
        "none": tok("0px", "dimension", SRC + "; body, header button, rows and sections all compute border-radius 0px"),
    },
    "spacing": {
        "headerInset": tok("10px", "dimension", SRC + "; header right and top 0.694444vw, computed 10px at 1440", declared="0.694444vw"),
        "mainPad": tok("10px", "dimension", SRC + "; main padding-left 0.694444vw, computed 10px", declared="0.694444vw"),
        "sectionPadY": tok("14px", "dimension", SRC + "; section.projects-previous padding-top 0.98vw, computed 14.112px", declared="0.98vw"),
        "sectionPadX": tok("26px", "dimension", SRC + "; main section padding-right 1.77667vw, computed 25.584px", declared="1.77667vw"),
        "sectionPadLeft": tok("10px", "dimension", SRC + "; main section padding-left 0.694444vw, computed 10px", declared="0.694444vw"),
        "rule": tok("3px", "dimension", SRC + "; main section border-left-width 0.208333vw, computed 3px (2.5px subpixel, painted 3px in the 1x shot)", declared="0.208333vw"),
        "logoPadY": tok("10px", "dimension", SRC + "; header button padding-block 0.694444vw, computed 10px", declared="0.694444vw"),
        "logoPadX": tok("12px", "dimension", SRC + "; header button padding-inline 0.833333vw, computed 12px", declared="0.833333vw"),
        "logo": tok("65px", "dimension", SRC + "; header button width 4.51389vw, computed 65px square", declared="4.51389vw"),
        "row": tok("56px", "dimension", SRC + "; .row height equals the 56px line box"),
        "indexCol": tok("26px", "dimension", SRC + "; .row .left computed font-size, the column is declared 4ch", declared="4ch"),
        "titleCol": tok("65px", "dimension", SRC + "; one row line; the title column is declared 33ch", declared="33ch"),
    },
}

# The set is named `dark` so it matches the only theme the page paints.
# The catalog swatches point at `dark.*`.
dark = {
    "$description": "The only painted theme. The page is black.",
    "surface": {
        "page": tok("{color.page}", "color", SRC),
        "raised": tok("{color.page}", "color", SRC + "; rows and sections have no raised fill, background is transparent over the page"),
    },
    "text": {
        "primary": tok("{color.ink}", "color", SRC),
        "muted": tok("{color.ink}", "color", SRC + "; no second text colour was read: the unreleased question-mark rows paint the same grey ink as body text. The 30% gold rule is a border colour (border.subtle), not text"),
        "onAccent": tok("{color.red}", "color", SRC + "; logo paths on the gold button"),
    },
    "accent": tok("{color.gold}", "color", SRC + "; the header button is the only filled control"),
    "border": {
        "subtle": tok("{color.rule}", "color", SRC),
        "strong": tok("{color.red}", "color", SRC + "; .row.project-tbd and the upcoming border-image start"),
    },
    "component": {
        "button": {
            "bg": tok("{color.gold}", "color", SRC),
            "text": tok("{color.red}", "color", SRC + "; the button has no text; the mark inside it is #F00007"),
            "radius": tok("{radius.none}", "dimension", SRC),
            "padding": tok("10px", "dimension", SRC + "; padding-block; padding-inline is 12px, see core.spacing.logoPadX"),
            "height": tok("{spacing.logo}", "dimension", SRC),
            "width": tok("{spacing.logo}", "dimension", SRC),
        },
        "link": {
            "text": tok("{color.ink}", "color", SRC),
            "background": tok("rgba(0, 0, 0, 0)", "color", SRC),
        },
        "row": {
            "text": tok("{color.ink}", "color", SRC),
            "background": tok("rgba(0, 0, 0, 0)", "color", SRC),
            "height": tok("{spacing.row}", "dimension", SRC),
        },
    },
}

motion_path = RAW / "motion.json"
not_tokenised = [
    {"name": "section.subscription", "value": "#40aaff", "why": "declared and not mounted. The same blue paints on the GSCT link, which is color.linkBlue"},
    {"name": "section.projects-upcoming-and-links border-image", "value": "linear-gradient(rgb(240, 0, 7), rgb(0, 0, 0))", "why": "a gradient border, not a flat colour; the section's own computed border-left-color is the Tailwind default rgb(229, 231, 235) because border-image replaces it"},
    {"name": "input", "value": "transparent, 3.88889vw tall, 13.5417vw wide", "why": "declared; no input is in the DOM. The only textarea is a hidden g-recaptcha-response"},
    {"name": "placeholder", "value": "rgb(156, 163, 175)", "why": "Tailwind preflight on input::placeholder; no placeholder is painted"},
    {"name": ".row .left width", "value": "4ch", "why": "a ch length; spacing.indexCol stores the computed 26px index size instead"},
    {"name": ".row .right width", "value": "33ch", "why": "a ch length; the title column is not a px token"},
]
if motion_path.exists():
    raw_motion = json.loads(motion_path.read_text())
    group, extra = motion_mod.build(raw_motion)
    core["motion"] = group
    not_tokenised.extend(extra)

core["$extensions"] = {"notTokenised": not_tokenised}
dark["$extensions"] = {"notTokenised": []}

tokens = {
    "core": core,
    "dark": dark,
    "$themes": [{
        "id": "dark",
        "name": "Dark",
        "selectedTokenSets": {"core": "source", "dark": "enabled"},
        "$description": "The only theme mschf.com paints. The ground is black.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "dark"]},
}

# checks
import re


def walk(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from walk(v, prefix + k + ".")


names = dict(walk(core))
names.update(walk(dark))
for n, t in list(names.items()):
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names:
            raise SystemExit(f"alias {{{a}}} from {n} points at nothing")
    if t["$type"] == "color" and not re.search(r"\{", json.dumps(t["$value"])):
        if not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", t["$value"]):
            raise SystemExit(f"colour {n} {t['$value']!r}")
    if t["$type"] == "dimension" and not re.search(r"\{", str(t["$value"])):
        if not re.fullmatch(r"-?\d*\.?\d+(px|rem)", t["$value"]):
            raise SystemExit(f"dimension {n} {t['$value']!r}")

TEXT = json.dumps(tokens, indent=2, ensure_ascii=False) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("tokens", len(names))
