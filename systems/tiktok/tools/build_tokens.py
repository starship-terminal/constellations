#!/usr/bin/env python3
"""Build systems/tiktok/tokens.json from raw/tux-vars.json and raw/computed.json.

Every colour, length, and duration is a computed custom property or a
computed style read on https://www.tiktok.com/ on 2026-11-19. Nothing here
invents a light theme or a painted hover colour.
"""
from __future__ import annotations

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"

EVIDENCE = "Measured"
CAPTURE = "https://www.tiktok.com/ 2026-11-19, signed out, T3 preview_evaluate"
CAPTURE_LIGHT = "https://www.tiktok.com/explore 2026-11-21, signed out, headless Playwright, innerWidth 1440"


def src(note: str, capture: str = CAPTURE, evidence: str = EVIDENCE) -> dict:
    return {"$extensions": {"source": {"evidence": evidence, "capture": capture, "note": note}}}


def color_token(value: str, note: str, capture: str = CAPTURE) -> dict:
    # Written as hex (#rrggbbaa when translucent); the note keeps the computed text.
    value = value if value.startswith("{") else as_color(value)
    return {"$type": "color", "$value": value, **src(note, capture)}


def dim(value: str, note: str) -> dict:
    return {"$type": "dimension", "$value": value, **src(note)}


def font_w(value: int, note: str) -> dict:
    return {"$type": "fontWeight", "$value": value, **src(note)}


def duration(value: str, note: str) -> dict:
    return {"$type": "duration", "$value": value, **src(note)}


def cubic(value: list, note: str) -> dict:
    return {"$type": "cubicBezier", "$value": value, **src(note)}


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
    rgb = "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    return rgb if a >= 1 else rgb + "%02x" % round(a * 255)


def hsla_norm(value: str) -> str | None:
    m = re.fullmatch(
        r"hsla?\(\s*([\d.]+)\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*(?:,\s*([\d.]+)\s*)?\)",
        value.strip(),
    )
    if not m:
        return None
    h, s, l = float(m.group(1)), float(m.group(2)) / 100, float(m.group(3)) / 100
    a = float(m.group(4)) if m.group(4) is not None else 1
    r, g, b = _hsl_to_rgb(h, s, l)
    rgb = "#%02x%02x%02x" % (r, g, b)
    return rgb if a >= 1 else rgb + "%02x" % round(a * 255)


def _hsl_to_rgb(h: float, s: float, l: float) -> tuple[int, int, int]:
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    if hp < 1:
        r, g, b = c, x, 0
    elif hp < 2:
        r, g, b = x, c, 0
    elif hp < 3:
        r, g, b = 0, c, x
    elif hp < 4:
        r, g, b = 0, x, c
    elif hp < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    m = l - c / 2
    return tuple(round((v + m) * 255) for v in (r, g, b))


def as_color(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", value):
        return value.lower()
    out = rgb_to_hex(value) or rgba_norm(value) or hsla_norm(value)
    if out is None:  # a renamed var or a keyword must not pass through as a colour (16-20)
        raise ValueError(f"not a colour reading: {value!r}")
    return out


def parse_shadow(value: str) -> list:
    # "0 2px 10px rgba(0,0,0,.07)" — offsetX is unitless 0, alpha may omit a leading zero.
    m = re.fullmatch(
        r"(-?[\d.]+)(?:px)?\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+rgba\((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\.?\d+)\)",
        value.strip(),
    )
    if not m:
        raise SystemExit(f"unparsed shadow: {value!r}")
    a = float(m.group(7))
    color = "#%02x%02x%02x%02x" % (int(m.group(4)), int(m.group(5)), int(m.group(6)), round(a * 255))
    return [{
        "color": color,
        "offsetX": f"{m.group(1)}px",
        "offsetY": f"{m.group(2)}px",
        "blur": f"{m.group(3)}px",
        "spread": "0px",
    }]


def build() -> dict:
    tux = json.loads((RAW / "tux-vars.json").read_text())["vars"]
    computed = json.loads((RAW / "computed.json").read_text())

    def t(name: str) -> str:
        return as_color(tux[name]) if name.startswith("--") and not name.startswith("--tux-font") and not name.startswith("--tux-v2-radius") and not name.startswith("--tux-v2-shadow") and not name.startswith("--tux-v2-typography") and not name.startswith("--tux-v2-pressed") and name != "--side-nav-width" else tux[name]

    def c(name: str) -> str:
        return as_color(tux[name])

    page = as_color(computed["body"]["backgroundColor"])
    # 2026-11-19 body was black. The 2026-11-21 Playwright pass loaded a light page.
    assert page == "#000000", page
    text = as_color(computed["body"]["color"])
    assert text == "#ffffffe6", text  # rgba(255, 255, 255, 0.9)
    action = as_color(computed["loginButtonDesktop"]["backgroundColor"])
    assert action == "#fe2c55"
    nav_selected = as_color(computed["navButtonSelected"]["color"])
    assert nav_selected == "#ff3b5c"

    family_text = "TikTokFont, Arial, Tahoma, PingFangSC, sans-serif"
    family_display = "TikTokDisplayFont, Arial, Tahoma, PingFangSC, sans-serif"

    core = {
        "color": {
            "page": color_token(page, "computed background-color on body"),
            "text": color_token(text, "computed color on body"),
            "text-strong": color_token("#ffffff", "computed color on the login button and the Sign up link's neighbour white"),
            "text-nav": color_token("#f6f6f6", "computed color on the Explore nav button, --ui-text-1"),
            "text-muted": color_token("rgba(255, 255, 255, 0.5)", "computed color on the sidebar h3 and the copyright line"),
            "razzmatazz": color_token(c("--brand-tiktok-razzmatazz"), "--brand-tiktok-razzmatazz and --ui-shape-primary"),
            "splash": color_token(c("--brand-tiktok-splash"), "--brand-tiktok-splash"),
            "primary": color_token(c("--tux-colorPrimary"), "--tux-colorPrimary, also the selected nav color"),
            "link": color_token(c("--tux-colorLink"), "--tux-colorLink"),
            "cyan": color_token(c("--tux-colorSecondary"), "--tux-colorSecondary"),
            "positive": color_token(c("--tux-colorPositive"), "--tux-colorPositive"),
            "negative": color_token(c("--tux-colorNegative"), "--tux-colorNegative, also the focus-visible outline"),
            "ink": color_token(c("--tux-colorConstTextPrimary"), "--tux-colorConstTextPrimary"),
            "sheet": color_token("#1e1e1e", "computed background-color on the login content container"),
            "channel": color_token("rgba(255, 255, 255, 0.13)", "computed background-color on [data-e2e=channel-item] and the Search pill"),
            "mask": color_token("rgba(0, 0, 0, 0.68)", "computed background-color on the login modal mask, --tux-colorSDSecondary"),
            "close": color_token("rgba(255, 255, 255, 0.04)", "computed background-color on [aria-label=Close]"),
            "divider": color_token("rgba(255, 255, 255, 0.12)", "computed border-top-color on the login footer divider"),
            "input": color_token(c("--tux-colorBGInput"), "--tux-colorBGInput, also the hidden search form"),
            "yellow": color_token(c("--tux-colorAssistColorYellow"), "--tux-colorAssistColorYellow"),
        },
        "font": {
            "family": {
                "tiktok": font_family(family_text, "computed font-family on body"),
                "display": font_family(family_display, "computed font-family on the login h2, --tux-fontFamilyHeading"),
            },
            "weight": {
                "regular": font_w(400, "computed font-weight on body, --tux-fontWeightRegular"),
                "medium": font_w(500, "computed font-weight on the login button, --tux-fontWeightSemibold"),
                "semibold": font_w(600, "computed font-weight on the channel label and the copyright line"),
                "bold": font_w(700, "computed font-weight on the login h2, --tux-fontWeightBold"),
            },
        },
        "typography": {
            "display": typography(
                {"fontFamily": "{font.family.display}", "fontSize": "33px", "fontWeight": "{font.weight.bold}", "lineHeight": "49.5px"},
                "computed style on the login h2",
            ),
            "nav": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "16px", "fontWeight": "{font.weight.medium}", "lineHeight": "21px", "letterSpacing": "0.15px"},
                "computed style on the sidebar nav button",
            ),
            "button": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "16px", "fontWeight": "{font.weight.medium}", "lineHeight": "21px", "letterSpacing": "0.15px"},
                "computed style on the desktop Log in button",
            ),
            "channel": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "16px", "fontWeight": "{font.weight.semibold}", "lineHeight": "20px"},
                "computed style on the login channel label",
            ),
            "body": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "14px", "fontWeight": "{font.weight.regular}", "lineHeight": "21px"},
                "computed style on body",
            ),
            "footer-heading": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "15px", "fontWeight": "{font.weight.bold}", "lineHeight": "21px"},
                "computed font-size and font-weight on the sidebar h3",
            ),
            "signup-prompt": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "15px", "fontWeight": "{font.weight.regular}", "lineHeight": "21px"},
                "computed font-size on the Don't have an account line",
            ),
            "copyright": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "12px", "fontWeight": "{font.weight.semibold}", "lineHeight": "21px"},
                "computed style on the copyright line",
            ),
            "signup-link": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "11px", "fontWeight": "{font.weight.semibold}", "lineHeight": "18px"},
                "computed style on the Sign up link",
            ),
            "legal-link": typography(
                {"fontFamily": "{font.family.tiktok}", "fontSize": "10px", "fontWeight": "{font.weight.regular}", "lineHeight": "13px"},
                "computed style on Terms of Service",
            ),
        },
        "radius": {
            "button": dim("6px", "computed border-radius on the nav button and the desktop Log in button"),
            "channel": dim("24px", "computed border-radius on [data-e2e=channel-item]"),
            "sheet": dim("24px", "computed border-radius on the login content container"),
            "search": dim("999px", "computed border-radius on the Search pill"),
            "capsule": dim(tux["--tux-v2-radius-content-capsule"], "--tux-v2-radius-content-capsule"),
            # 50% of the 32 x 32 Close button (raw/computed.json close): one px length, 16px.
            "close": {"$type": "dimension", "$value": "16px", "$extensions": {"source": {
                "evidence": "Derived", "capture": CAPTURE,
                "note": "computed border-radius 50% on [aria-label=Close], a 32 x 32 box: 16px, a circle"}}},
            "tiny": dim(tux["--tux-v2-radius-content-tiny"], "--tux-v2-radius-content-tiny"),
            "small": dim(tux["--tux-v2-radius-content-small"], "--tux-v2-radius-content-small"),
            "medium": dim(tux["--tux-v2-radius-content-medium"], "--tux-v2-radius-content-medium"),
            "large": dim(tux["--tux-v2-radius-content-large"], "--tux-v2-radius-content-large"),
            "xlarge": dim(tux["--tux-v2-radius-content-xlarge"], "--tux-v2-radius-content-xlarge"),
            "level2-large": dim(tux["--tux-v2-radius-container-level2-large"], "--tux-v2-radius-container-level2-large"),
        },
        "spacing": {
            "1": dim("1px", "computed padding-top on the desktop Log in button"),
            "8": dim("8px", "computed padding on Follow, and the top of the login option container"),
            "10": dim("10px", "computed padding-left on the channel row"),
            "14": dim("14px", "computed padding-right on the channel row"),
            "16": dim("16px", "computed padding-left and padding-right on the desktop Log in button; nav x"),
            "20": dim("20px", "computed x of the desktop Log in button"),
            "24": dim("24px", "computed margin-bottom on the desktop Log in button; logo x"),
            "32": dim("32px", "computed width and height of the close control"),
            "40": dim("40px", "computed height of the nav button and the Log in button"),
            "48": dim("48px", "computed height of a login channel row"),
            "64": dim("64px", "computed padding-bottom on the login dialog"),
        },
        "borderWidth": {
            "focus": dim("2px", "declared outline-width on button:focus-visible"),
            "divider": dim("0.5px", "computed border-top-width on the login footer divider"),
        },
        "motion": {
            "duration": {
                "logo": duration("250ms", "computed transition color 0.25s ease on the logo link"),
                "modal": duration("500ms", "declared transition on DivModalContainer"),
                "nav-label": duration("400ms", "declared opacity transition on the nav label at min-width 1025px"),
                "popover": duration("300ms", "declared opacity transition on TUXPopover"),
                "utilities": duration("120ms", "declared sideNavUtilitiesEnter animation duration"),
            },
            "easing": {
                "ease": cubic([0.25, 0.1, 0.25, 1], "keyword ease on the logo transition, expanded to the CSS control points"),
                "modal": cubic([0.075, 0.82, 0.165, 1], "declared cubic-bezier on DivModalContainer"),
                "popover": cubic([0.65, 0, 0.35, 1], "declared cubic-bezier on TUXPopover"),
            },
        },
        "shadow": {
            "subtle": shadow_token(parse_shadow(tux["--tux-v2-shadow-subtle"]), "--tux-v2-shadow-subtle, declared, not painted on the measured controls"),
            "attached": shadow_token(parse_shadow(tux["--tux-v2-shadow-attached"]), "--tux-v2-shadow-attached, declared"),
            "floating": shadow_token(parse_shadow(tux["--tux-v2-shadow-floating"]), "--tux-v2-shadow-floating, declared"),
            "contrast": shadow_token(parse_shadow(tux["--tux-v2-shadow-contrast"]), "--tux-v2-shadow-contrast, declared"),
            "blocking": shadow_token(parse_shadow(tux["--tux-v2-shadow-blocking"]), "--tux-v2-shadow-blocking, declared"),
            "notice": shadow_token(parse_shadow(tux["--tux-v2-shadow-global-notice"]), "--tux-v2-shadow-global-notice, declared"),
        },
    }
    # Mark the ease expansion as Derived. The duration is measured; the control points are the CSS keyword expansion.
    core["motion"]["easing"]["ease"]["$extensions"]["source"]["evidence"] = "Derived"

    dark = {
        "background": {
            "page": color_token("{color.page}", "body background"),
            "surface": color_token("{color.sheet}", "login sheet"),
            "action": color_token("{color.razzmatazz}", "desktop Log in button"),
            "channel": color_token("{color.channel}", "login channel and Search pill"),
            "mask": color_token("{color.mask}", "login mask"),
            "input": color_token("{color.input}", "--tux-colorBGInput"),
        },
        "text": {
            "primary": color_token("{color.text}", "body color"),
            "strong": color_token("{color.text-strong}", "button label"),
            "nav": color_token("{color.text-nav}", "nav label"),
            "secondary": color_token("{color.text-muted}", "sidebar heading"),
            "on-action": color_token("{color.text-strong}", "Log in label"),
            "link": color_token("{color.primary}", "Sign up and selected nav"),
        },
        "border": {
            "stroke": color_token("{color.divider}", "login footer divider"),
            "focus": color_token("{color.negative}", "focus-visible outline"),
        },
        "component": {
            "button": {
                "bg": color_token("{color.razzmatazz}", "desktop Log in"),
                "text": color_token("{color.text-strong}", "desktop Log in label"),
                "radius": dim("{radius.button}", "desktop Log in"),
                "height": dim("40px", "desktop Log in and nav button"),
                "padding": dim("16px", "desktop Log in horizontal padding"),
            },
            "nav": {
                "text": color_token("{color.text-nav}", "unselected nav"),
                "radius": dim("{radius.button}", "nav button"),
                "height": dim("40px", "nav button"),
            },
            "channel": {
                "bg": color_token("{color.channel}", "channel row"),
                "text": color_token("{color.text}", "channel label"),
                "radius": dim("{radius.channel}", "channel row"),
                "height": dim("48px", "channel row"),
            },
            "sheet": {
                "bg": color_token("{color.sheet}", "login sheet"),
                "radius": dim("{radius.sheet}", "login sheet"),
            },
            "search": {
                "bg": color_token("{color.channel}", "Search pill"),
                "radius": dim("{radius.search}", "Search pill"),
                "height": dim("40px", "Search pill"),
            },
        },
    }

    light = light_set()
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
        "core": core,
        "dark": dark,
        "light": light,
        "$themes": [
            {
                "id": "dark",
                "name": "dark",
                "selectedTokenSets": {"core": "source", "dark": "enabled"},
            },
            {
                "id": "light",
                "name": "light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
            },
        ],
    }
    check(doc)
    return doc


def L(value: str, note: str, evidence: str = EVIDENCE) -> dict:
    value = value if value.startswith("{") else as_color(value)
    return {"$type": "color", "$value": value, **src(note, CAPTURE_LIGHT, evidence)}


def light_set() -> dict:
    """Light roles read on the signed-out Explore page, 2026-11-21.

    The 2026-11-19 dark set stays. This set does not invent a dark sheet.
    Hover and pressed are the filled Log in button only.
    """
    return {
        "background": {
            "page": L("#ffffff", "computed background-color on body, data-tux-color-scheme light"),
            "surface": L("#ffffff", "login dialog painted white on the light Explore page"),
            "raised": L("rgba(0, 0, 0, 0.05)", "computed background-color on a login channel row"),
            "action": L("#fe2c55", "computed background-color on the desktop Log in button"),
            "action-hover": L("#ea284e", "computed background-color on Log in while the pointer was over it"),
            "action-pressed": L("#e0274b", "computed background-color on Log in while the pointer was down"),
        },
        "text": {
            "primary": L("#161823", "computed color on body, --tux-colorTextPrimary"),
            "on-accent": L("#ffffff", "computed color on the desktop Log in label"),
            "link": L("#fe2c55", "computed color on Sign up and on the selected Explore nav"),
        },
    }


def main() -> None:
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")


# ---------------------------------------------------------------- check (finding 16-6)

def _token_paths(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield f"{path}{key}", value
        else:
            yield from _token_paths(value, f"{path}{key}.")


def _aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [a for v in value.values() for a in _aliases(v)]
    if isinstance(value, list):
        return [a for v in value for a in _aliases(v)]
    return []


def _follow(flat, s, ref, seen):
    """Follow an alias chain: each name resolves in the set it is read from, then core, then the
    root (the Resolver's order). Returns a problem string for a dead alias or a repeated token,
    else None."""
    # Own set, then core, then the root, where a set-qualified name such as core.color.white.solid
    # names a token in that set. The next hop resolves from the set the target was found in.
    candidates = [(s, ref), ("core", ref)]
    if "." in ref:
        candidates.append(tuple(ref.split(".", 1)))
    found = next(((fs, fp) for fs, fp in candidates if fp in flat.get(fs, {})), None)
    if found is None:
        return f"alias {{{ref}}} resolves nowhere"
    if found in seen:
        return f"alias loop through {{{ref}}}"
    target_set, target_path = found
    for nxt in _aliases(flat[target_set][target_path]["$value"]):
        err = _follow(flat, target_set, nxt, seen | {found})
        if err:
            return err
    return None


def check(doc):
    """Refuse a token with no source, a colour that is neither #rrggbb(aa) nor one whole alias, an
    alias that resolves in neither its own set nor core (the order tools/catalog.py's Resolver
    uses), and an alias chain that comes back to a token it already passed. Raises SystemExit."""
    sets = [s for s, v in doc.items() if not s.startswith("$") and isinstance(v, dict)]
    flat = {s: dict(_token_paths(doc[s])) for s in sets}
    core = flat.get("core", {})
    problems = []
    for s in sets:
        for path, token in flat[s].items():
            where = f"{s}.{path}"
            if not token.get("$extensions", {}).get("source"):
                problems.append(f"{where}: no source")
            value = token["$value"]
            for ref in _aliases(value):
                err = _follow(flat, s, ref, {(s, path)})
                if err:
                    problems.append(f"{where}: {err}")
            if token.get("$type") == "color":
                whole_alias = isinstance(value, str) and re.fullmatch(r"\{[^{}]+\}", value)
                if not whole_alias and not (isinstance(value, str) and re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", value)):
                    problems.append(f"{where}: colour {value!r} is not #rrggbb(aa) or one whole alias")
    if problems:
        raise SystemExit("token check failed:\n" + "\n".join(problems))


if __name__ == "__main__":
    main()
