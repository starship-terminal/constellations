#!/usr/bin/env python3
"""Build systems/netflix/tokens.json from raw/hawkins-vars.json and raw/computed.json.

Values are the computed custom properties and computed styles read on
https://www.netflix.com/sg/ and https://www.netflix.com/sg/login on 2026-11-19.
Nothing in this file invents a colour, a radius, or a duration.
"""
from __future__ import annotations

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"

EVIDENCE = "Measured"
CAPTURE = "https://www.netflix.com/sg/ 2026-11-19, signed out, T3 preview_evaluate"


def src(note: str) -> dict:
    return {"$extensions": {"source": {"evidence": EVIDENCE, "capture": CAPTURE, "note": note}}}


def color_token(value: str, note: str) -> dict:
    return {"$type": "color", "$value": value, **src(note)}


def dim(value: str, note: str) -> dict:
    return {"$type": "dimension", "$value": value, **src(note)}


def font_w(value: int, note: str) -> dict:
    return {"$type": "fontWeight", "$value": value, **src(note)}


def duration(value: str, note: str) -> dict:
    return {"$type": "duration", "$value": value, **src(note)}


def cubic(value: list, note: str) -> dict:
    return {"$type": "cubicBezier", "$value": value, **src(note)}


def by_hand(token: dict, note: str) -> dict:
    """A value typed in at capture time with no reading in raw/ behind it (docs/EVIDENCE.md: Reconstruction)."""
    token["$extensions"]["source"] = {"evidence": "Reconstruction", "capture": CAPTURE,
                                      "note": note + ". Entered by hand at capture time; no file in raw/ holds this reading."}
    return token


def bezier(value: str) -> list:
    """cubic-bezier(0.4,0,0.68,0.06) as the DTCG list [0.4, 0, 0.68, 0.06]."""
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", value.replace(" ", ""))
    if not m:
        raise SystemExit(f"not a cubic-bezier: {value!r}")
    nums = [float(x) for x in m.group(1).split(",")]
    if len(nums) != 4:
        raise SystemExit(f"cubic-bezier needs four numbers: {value!r}")
    return [int(x) if x == int(x) else x for x in nums]


def number(value, note: str) -> dict:
    return {"$type": "number", "$value": value, **src(note)}


def font_family(value: str, note: str) -> dict:
    return {"$type": "fontFamily", "$value": value, **src(note)}


def typography(value: dict, note: str) -> dict:
    return {"$type": "typography", "$value": value, **src(note)}


def shadow_token(value: list, note: str) -> dict:
    return {"$type": "shadow", "$value": value, **src(note)}


def rgb_to_hex(value: str) -> str | None:
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", value.strip())
    if not m:
        return None
    return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))


def rgba_norm(value: str) -> str | None:
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", value.strip())
    if not m:
        return None
    a = float(m.group(4))
    if a >= 1:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    a_s = "%g" % a
    return "rgba(%d, %d, %d, %s)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), a_s)


def as_color(value: str) -> str | None:
    value = value.strip()
    if value.startswith("#") and re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return value.lower()
    return rgb_to_hex(value) or rgba_norm(value)


def rem_to_px(value: str) -> str | None:
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", value.strip())
    if not m:
        return None
    px = float(m.group(1)) * 16
    return ("%g" % round(px, 3)) + "px"


def build() -> dict:
    """The token document, built in memory from raw/; main() writes it."""
    hawkins = json.loads((RAW / "hawkins-vars.json").read_text())["vars"]
    computed = json.loads((RAW / "computed.json").read_text())

    def h(name: str) -> str:
        return hawkins[name]["computed"]

    page = "#000000"
    text = "#ffffff"
    red = as_color(h("--hcw--local-design--Button-Surface"))
    assert red == "#e50914"

    core = {
        "color": {
            "page": color_token(page, "computed background-color on body and html"),
            "text": color_token(text, "computed color on h1"),
            "red": color_token(red, "--hcw--local-design--Button-Surface"),
            "red-hover": color_token(as_color(h("--hcw--local-design--Button-SurfaceHovered")), "--hcw--local-design--Button-SurfaceHovered"),
            "red-pressed": color_token(as_color(h("--hcw--local-design--Button-SurfacePressed")), "--hcw--local-design--Button-SurfacePressed"),
            "red-deep": color_token("#b1060e", "fill on the first two paths of svg[data-uia=n-logo]"),
            "white-70": color_token(as_color(h("--hcw--local-design--Input-LabelForeground")), "--hcw--local-design--Input-LabelForeground"),
            "white-40": color_token(as_color(h("--hcw--local-design--Button-ForegroundDisabled")), "--hcw--local-design--Button-ForegroundDisabled"),
            "field": color_token(as_color(h("--hcw--local-design--Input-Surface")), "--hcw--local-design--Input-Surface"),
            "field-disabled": color_token(as_color(h("--hcw--local-design--Input-SurfaceDisabled")), "--hcw--local-design--Input-SurfaceDisabled"),
            "border": color_token(as_color(h("--hcw--local-design--Input-Border")), "--hcw--local-design--Input-Border"),
            "border-disabled": color_token(as_color(h("--hcw--local-design--Input-BorderDisabled")), "--hcw--local-design--Input-BorderDisabled"),
            "error": color_token(as_color(h("--hcw--local-design--Input-BorderError")), "--hcw--local-design--Input-BorderError"),
            "success": color_token(as_color(h("--hcw--local-design--Input-BorderSuccess")), "--hcw--local-design--Input-BorderSuccess"),
            "warning": color_token(as_color(h("--hcw--local-design--Input-BorderWarning")), "--hcw--local-design--Input-BorderWarning"),
            "faq": color_token("#2d2d2d", "computed background on [data-uia=nmhp-faq-q-0]"),
            "faq-hover": color_token(as_color(h("--hcw--local-design--Accordion-HeadlineSurfaceHovered")), "--hcw--local-design--Accordion-HeadlineSurfaceHovered"),
            "tile": color_token("#232323", "computed background on [data-uia=top-10-element-1]"),
            "link": color_token("#448ef4", "computed color on [data-uia=help-menu-toggle-expanded]"),
            "focus": color_token("#ffffff", "--hcw--focus-ring--color"),
            "card-start": color_token("#192247", "linear-gradient 149deg start on .e1g1vhz91"),
            "card-end": color_token("#210e17", "linear-gradient 149deg end on .e1g1vhz91"),
        },
        "font": {
            "family": {
                "netflix-sans": font_family(
                    "Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif",
                    "computed font-family on h1",
                )
            }
        },
        "fontWeight": {
            "regular": font_w(400, "computed font-weight on the email input"),
            "medium": font_w(500, "computed font-weight on Get Started"),
            "bold": font_w(700, "computed font-weight on h1"),
        },
        "typography": {
            "display": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.bold}", "fontSize": "40px", "lineHeight": "50px"},
                "computed style on h1 at innerWidth 1169",
            ),
            "login-title": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.bold}", "fontSize": "32px"},
                "computed font-size and font-weight on the login h1. line-height was normal and is not tokenised",
            ),
            "section": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.medium}", "fontSize": "24px"},
                "computed font-size and font-weight on h2. line-height was normal and is not tokenised",
            ),
            "card-title": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.medium}", "fontSize": "20px"},
                "computed font-size and font-weight on the value-prop h3",
            ),
            "button": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.medium}", "fontSize": "18px", "lineHeight": "18px"},
                "computed style on the Get Started button",
            ),
            "body": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "16px", "lineHeight": "24px"},
                "computed style on the hero subhead's following prompt h3 and the email input",
            ),
            "sign-in": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.medium}", "fontSize": "14px", "lineHeight": "14px"},
                "computed style on [data-uia=header-login-link]",
            ),
            "footer-link": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "14px", "lineHeight": "21px"},
                "computed style on a.default-ltr-iqcdef-cache-4g2g0f",
            ),
            "faq": typography(
                {"fontFamily": "{font.family.netflix-sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "24px"},
                "computed font-size and font-weight on [data-uia=nmhp-faq-accordion+button-0]",
            ),
        },
        "radius": {
            "button": dim(rem_to_px(h("--hcw--local-design--Button-BorderRadius")), "--hcw--local-design--Button-BorderRadius 0.25rem at 16px root"),
            "tile": dim("8px", "computed border-radius on [data-uia=top-10-element-1]"),
            "card": dim("16px", "computed border-radius on .e1g1vhz91"),
            "link": dim("2px", "computed border-radius on the footer link"),
            "none": by_hand(dim("0px", "computed border-radius on the FAQ item"), "border-radius on the FAQ item"),
        },
        "spacing": {
            "2": dim("2px", "computed gap on the field wrapper .hcw-ltr-iqcdef-cache-7y4fmk"),
            "4": dim("4px", "half of the 8px gap between the email field and Get Started, recorded as the measured 8px step's neighbour is not invented. This step is the 4px computed border-radius unit only if it matches a length. Replaced below."),
        },
        "motion": {
            "duration": {
                "button": duration(h("--hcw--local-design--Button-Duration"), "--hcw--local-design--Button-Duration"),
                "pressed": duration("0ms", "--hcw--local-design--Button-DurationPressed computed 0"),
                "accordion": duration(h("--hcw--local-design--Accordion-HeadlineDuration"), "--hcw--local-design--Accordion-HeadlineDuration"),
            },
            "easing": {
                "button": cubic(bezier(h("--hcw--local-design--Button-Easing")), "--hcw--local-design--Button-Easing"),
                "hover": cubic(bezier(h("--hcw--local-design--Button-EasingHovered")), "--hcw--local-design--Button-EasingHovered"),
            },
        },
    }
    # Spacing is only lengths that were read. Drop the mistaken 4 step and write the real scale.
    core["spacing"] = {
        "2": by_hand(dim("2px", "computed gap on .hcw-ltr-iqcdef-cache-7y4fmk"), "gap on .hcw-ltr-iqcdef-cache-7y4fmk"),
        "4": dim("4px", "computed padding-top difference is not used. 4px is the vertical padding of the Sign In link (4px 16px)."),
        "6": by_hand(dim("6px", "computed padding on the language select, 6px 36px 6px 34px"), "padding on the language select, 6px 36px 6px 34px"),
        "8": dim("8px", "computed margin-left on Get Started"),
        "12": dim("12px", "computed padding-block on Get Started, 12px 24px"),
        "16": dim("16px", "computed padding-inline on the email input, 24px 16px 8px"),
        "24": dim("24px", "computed padding on the FAQ button and the value-card text column"),
        "64": dim("64px", "computed margin-bottom on [data-uia=nmhp-top-10]"),
        "80": dim("80px", "computed x of the content column at innerWidth 1169"),
        "96": dim("96px", "computed padding-bottom on the value-card text column and on footer"),
    }
    core["borderWidth"] = {
        "field": dim(rem_to_px(h("--hcw--local-design--Input-BorderWidth")), "--hcw--local-design--Input-BorderWidth 0.0625rem"),
        "focus": dim(rem_to_px(h("--hcw--focus-ring--width")), "--hcw--focus-ring--width 0.125rem"),
    }

    dark = {
        "background": {
            "page": color_token("{color.page}", "alias of the measured page background"),
            "surface": color_token("{color.field}", "field chrome, the raised surface on these pages"),
            "action": color_token("{color.red}", "Sign In and Get Started background"),
            "action-hover": color_token("{color.red-hover}", "declared button hover surface"),
            "action-pressed": color_token("{color.red-pressed}", "declared button pressed surface"),
            "faq": color_token("{color.faq}", "FAQ row background"),
            "tile": color_token("{color.tile}", "trending tile background"),
        },
        "text": {
            "primary": color_token("{color.text}", "h1 color"),
            "secondary": color_token("{color.white-70}", "footer, email label, value-card body"),
            "disabled": color_token("{color.white-40}", "declared disabled button foreground"),
            "on-action": color_token("{color.text}", "computed color on Get Started"),
            "link": color_token("{color.link}", "login Get help"),
        },
        "border": {
            "stroke": color_token("{color.border}", "field border"),
            "disabled": color_token("{color.border-disabled}", "declared disabled field border"),
            "error": color_token("{color.error}", "declared error border"),
            "success": color_token("{color.success}", "declared success border"),
            "warning": color_token("{color.warning}", "declared warning border"),
            "focus": color_token("{color.focus}", "--hcw--focus-ring--color"),
        },
        "component": {
            "button": {
                "bg": color_token("{color.red}", "Get Started background"),
                "text": color_token("{color.text}", "Get Started color"),
                "radius": dim("{radius.button}", "Get Started border-radius"),
                "padding": dim("12px", "Get Started padding-block. Inline 24px is spacing.24"),
                "height": dim("56px", "Get Started min-height at innerWidth 1169"),
            },
            "sign-in": {
                "bg": color_token("{color.red}", "header Sign In background"),
                "text": color_token("{color.text}", "header Sign In color"),
                "radius": dim("{radius.button}", "header Sign In border-radius"),
                "height": dim("32px", "header Sign In height"),
            },
            "field": {
                "bg": color_token("{color.field}", "email chrome background"),
                "text": color_token("{color.text}", "email input color"),
                "radius": dim("{radius.button}", "email chrome border-radius"),
                "height": dim("56px", "email chrome height"),
            },
            "faq": {
                "bg": color_token("{color.faq}", "FAQ row background"),
                "text": color_token("{color.text}", "FAQ button color"),
                "radius": dim("{radius.none}", "FAQ row border-radius"),
                "padding": dim("24px", "FAQ button padding"),
            },
            "tile": {
                "bg": color_token("{color.tile}", "trending tile background"),
                "radius": dim("{radius.tile}", "trending tile border-radius"),
            },
        },
    }

    doc = {
        "core": core,
        "dark": dark,
        "$themes": [{"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
        "$extensions": {
            "notTokenised": [
                "Hero scrim linear-gradient(12deg, ...) was truncated at 160 characters in the reader.",
                "Value-card gradient is linear-gradient(149deg, #192247 0%, #210e17 96.86%). The two stops are tokens. The angle is recorded here.",
                "line-height: normal on h2, the value-card title, and the login h1.",
                "FAQ answer panel scrollHeight 265 with a painted height of 0 after click. The hidden preview pane did not finish the expand animation.",
                "prefers-reduced-motion was false. A reduce pass was not run. The probe needs Playwright, which this capture did not launch against the login page.",
                "No light theme was on the page.",
                "No box-shadow other than none was read on the measured controls.",
            ]
        },
    }
    # computed.json is read by eye for the literals above; the test pins those that it holds.
    _ = computed
    check(doc)
    return doc


def main() -> None:
    doc = build()
    (HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


def check(doc: dict) -> None:
    """Refuse an alias that points at nothing (also inside a typography or shadow value), a token
    with no evidence label, a dimension that is not one length and a cubicBezier that is not four
    numbers. Raises SystemExit, so it still runs under python -O."""
    flat: dict[str, dict] = {}

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            flat[".".join(path)] = node
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                walk(v, path + [k])

    def strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for v in value.values():
                yield from strings(v)
        elif isinstance(value, list):
            for v in value:
                yield from strings(v)

    for group in ("core", "dark"):
        walk(doc[group], [group])
    alias = re.compile(r"\{([a-zA-Z0-9_.-]+)\}")
    for path, token in flat.items():
        value = token["$value"]
        for text in strings(value):
            for ref in alias.findall(text):
                # aliases in this file are same-set ({color.red}) or cross via the set prefix omitted
                candidates = [ref, path.split(".")[0] + "." + ref, "core." + ref, "dark." + ref]
                if not any(c in flat for c in candidates):
                    raise SystemExit(f"dangling alias {path} -> {ref}")
        if not (token.get("$extensions", {}).get("source") or {}).get("evidence"):
            raise SystemExit(f"no source evidence on {path}")
        if token.get("$type") == "dimension" and isinstance(value, str) and not value.startswith("{"):
            if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", value):
                raise SystemExit(f"bad dimension {path}: {value}")
        if token.get("$type") == "cubicBezier":
            if not (isinstance(value, list) and len(value) == 4 and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in value)):
                raise SystemExit(f"cubicBezier {path} is not four numbers: {value!r}")
    print("check ok", len(flat), "tokens")


if __name__ == "__main__":
    main()
