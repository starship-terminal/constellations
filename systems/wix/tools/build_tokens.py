#!/usr/bin/env python3
"""Build systems/wix/tokens.json from raw/readings.json.

Every value is a computed style from a signed-out Wix page, or a row copied
from the public Wix Design System Colors page. Nothing is filled from memory.
A value that was not read is listed under $extensions.notTokenised.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "readings.json").read_text())

MARKETING = "computed style, https://www.wix.com/, 1440x900, light, signed out, 2026-11-18"
PLANS = "computed style, https://www.wix.com/plans, 1440x900, light, signed out, 2026-11-18"
LOGIN = "computed style, https://users.wix.com/signin, signed out, not submitted, 2026-11-18"
WDS = "published row, https://www.wix-pages.com/design-system-documentation/#/page/foundations/colors, v1.352.0, 2026-11-18"
MOTION = "computed animation or transition, https://www.wix.com/, 2026-11-18"
GUIDE = "published text, https://www.wix-pages.com/design-system-documentation/#/page/guidelines/motion, 2026-11-18"


def color(value: str, source: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value: str, source: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def number(value: str, source: str) -> dict:
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def bezier_points(value: str) -> list:
    """"0.25, 0.1, 0.25, 1" as the four numbers DTCG's cubicBezier holds. A string would
    export as a bare number list, which is not a CSS easing."""
    points = [float(p) for p in value.split(",")]
    assert len(points) == 4, value
    return [int(p) if p.is_integer() else p for p in points]


def duration(value: str, source: str) -> dict:
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def cubic(value: str, source: str) -> dict:
    return {"$type": "cubicBezier", "$value": bezier_points(value), "$extensions": {"source": source}}


def rgb_hex(rgb: str) -> str:
    parts = rgb.replace("rgb(", "").replace(")", "").split(",")
    return "#%02x%02x%02x" % tuple(int(p.strip()) for p in parts)


def alias(path: str, source: str) -> dict:
    return {"$type": "color", "$value": path, "$extensions": {"source": source}}


# Foundation solids read from the public Colors table.
FOUNDATION = {
    "black": {
        "100": "#000624", "200": "#44485f", "300": "#595d70", "400": "#868aa5",
        "500": "#acafc4", "550": "#cfd1dc", "600": "#dfe5eb", "700": "#eceff3",
        "750": "#f6f7f9",
    },
    "white": {"solid": "#ffffff"},
    "blue": {
        "0": "#084ebd", "50": "#0f62e6", "100": "#116dff", "150": "#116dff",
        "200": "#5999ff", "250": "#80b1ff", "300": "#a8caff", "350": "#d1dcff",
        "400": "#d6e6fe", "500": "#e7f0ff", "600": "#f4f7ff",
    },
    "green": {
        "0": "#1d8649", "50": "#229954", "100": "#25a55a", "200": "#51b77b",
        "300": "#87cea5", "400": "#c8e8d6", "500": "#e1f4eb", "600": "#e9f6ee",
    },
    "red": {
        "0": "#b81206", "50": "#d0180b", "100": "#e62214", "200": "#ff6d63",
        "300": "#f69891", "400": "#fbd0cd", "500": "#fde3e1", "600": "#fdeceb",
    },
    "orange": {
        "0": "#df4d00", "50": "#f05300", "100": "#fe620f", "200": "#ff7d38",
        "300": "#fcbd9c", "400": "#fddbc8", "500": "#fee5d7", "600": "#feefe6",
    },
    "yellow": {
        "0": "#d59900", "50": "#e7a600", "100": "#ffb700", "200": "#ffc23d",
        "300": "#ffd16e", "400": "#ffe2a5", "500": "#fff0d1", "600": "#fff6e5",
    },
    "purple": {
        "0": "#7416a5", "50": "#8e1dd1", "100": "#9a27d5", "200": "#c161f0",
        "300": "#cf8cf1", "400": "#e3c3f4", "500": "#f1e0f9", "600": "#f7edfc",
    },
    "iris": {
        "0": "#4d3dd0", "50": "#5443e3", "100": "#5a48f5", "200": "#7b6df7",
        "300": "#a59bfa", "400": "#d6d1fc", "500": "#e7e4fe", "600": "#eeecfe",
    },
    "pink": {
        "0": "#bd22a1", "50": "#e221ac", "100": "#f639d3", "200": "#ff77e6",
        "300": "#ffa9ef", "400": "#ffc2f3", "500": "#fdd7f2", "600": "#feebfb",
    },
}


def foundation() -> dict:
    out = {}
    for family, steps in FOUNDATION.items():
        out[family] = {
            step: color(value, f"{WDS}; --wds-color-{family}-{step}" if step != "solid" else f"{WDS}; --wds-color-white")
            for step, value in steps.items()
        }
    return out


def build() -> dict:
    m = RAW["marketing"]["computed"]
    p = RAW["marketing"]["plans"]
    login = RAW["login"]
    tokens = {
        "core": {
            "color": foundation(),
            "font": {
                "display": font("wix-madefor-display-v2, sans-serif", f"{MARKETING}; h1 font-family"),
                "display-header": font("Madefor-Display, Helvetica Neue, Helvetica, Arial, sans-serif", f"{MARKETING}; header CTA font-family"),
                "text": font("wix-madefor-text-v2, sans-serif", f"{MARKETING}; body paragraph font-family"),
                "text-bold": font("madefor-text-mediumbold, sans-serif", f"{MARKETING}; Get Started label font-family"),
                "login": font("Madefor, Helvetica Neue, Helvetica, Arial, sans-serif", f"{LOGIN}; input font-family"),
                "login-display": font("Madefor Display, sans-serif", f"{LOGIN}; h1 font-family"),
            },
            "typography": {
                "display": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.display}",
                        "fontSize": "82.5px",
                        "fontWeight": "400",
                        "lineHeight": "99px",
                        "letterSpacing": "-1.65px",
                    },
                    "$extensions": {"source": f"{MARKETING}; h1 computed. line-height rounded from 99.0001px"},
                },
                "heading": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.display}",
                        "fontSize": "48px",
                        "fontWeight": "400",
                        "lineHeight": "54.72px",
                        "letterSpacing": "-0.48px",
                    },
                    "$extensions": {"source": f"{MARKETING}; section h2"},
                },
                "plans-title": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "madefor-display, sans-serif",
                        "fontSize": "60px",
                        "fontWeight": "400",
                        "lineHeight": "66px",
                    },
                    "$extensions": {"source": f"{PLANS}; h1. line-height rounded from 66.0001px"},
                },
                "body": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.text}",
                        "fontSize": "16px",
                        "fontWeight": "400",
                        "lineHeight": "20.8px",
                    },
                    "$extensions": {"source": f"{MARKETING}; hero paragraph"},
                },
                "nav": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.display-header}",
                        "fontSize": "16px",
                        "fontWeight": "400",
                        "lineHeight": "24px",
                    },
                    "$extensions": {"source": f"{MARKETING}; header nav label and Start for free"},
                },
                "login-title": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.login-display}",
                        "fontSize": "36px",
                        "fontWeight": "500",
                    },
                    "$extensions": {"source": f"{LOGIN}; h1 at 1440. phone size is 28px, recorded in notTokenised"},
                },
                "button": {
                    "$type": "typography",
                    "$value": {
                        "fontFamily": "{font.login}",
                        "fontSize": "14px",
                        "fontWeight": "530",
                        "lineHeight": "24px",
                    },
                    "$extensions": {"source": f"{LOGIN}; Continue with Email computed font-weight 530"},
                },
            },
            "radius": {
                "header-cta": dim("42px", f"{MARKETING}; Start for free border-radius"),
                "pill": dim("50px", f"{MARKETING}; Get Started border-radius"),
                "plans-cta": dim("99px", f"{PLANS}; Start for Free border-radius"),
                "domain": dim("999px", f"{MARKETING}; domain input border-radius"),
                "field": dim("6px", f"{LOGIN}; email field border-radius"),
                "login-button": dim("6px", f"{LOGIN}; Continue with Email border-radius"),
            },
            "space": {
                "header-pad-x": dim("20px", f"{MARKETING}; fixed header padding"),
                "nav-pad-x": dim("12px", f"{MARKETING}; nav item padding"),
                "cta-pad-y": dim("8px", f"{MARKETING}; Start for free padding-top"),
                "cta-pad-x": dim("30px", f"{MARKETING}; Start for free padding-left"),
                "login-button-pad-y": dim("9px", f"{LOGIN}; Continue with Email padding-top"),
                "plan-pad-top": dim("45px", f"{PLANS}; plan column padding-top"),
                "plan-pad-x": dim("26.25px", f"{PLANS}; plan column padding-left"),
                "header-height": dim("72px", f"{MARKETING}; fixed header height"),
                "cta-height": dim("40px", f"{MARKETING}; Start for free height"),
                "pill-height": dim("54px", f"{MARKETING}; Get Started height"),
                "field-height": dim("52px", f"{LOGIN}; email field height at 1440"),
                "login-button-height": dim("43px", f"{LOGIN}; Continue with Email height"),
            },
            "motion": {
                "duration": {
                    "menu": duration("300ms", f"{MOTION}; menu panel 0.3s and scrim background-color 0.3s"),
                    "fast": duration("200ms", f"{MOTION}; transition all, visibility 0.2s ease, 88 elements"),
                    "reveal": duration("1200ms", f"{MOTION}; motion-revealIn and motion-fadeIn 1.2s"),
                    "guide-fast": duration("100ms", f"{GUIDE}; Fast step, upper bound of 50 to 100ms"),
                    "guide-moderate": duration("250ms", f"{GUIDE}; Moderate step, upper bound of 150 to 250ms"),
                    "guide-slow": duration("500ms", f"{GUIDE}; Slow step, upper bound of 300 to 500ms"),
                },
                "easing": {
                    "ease": cubic("0.25, 0.1, 0.25, 1", f"{MOTION}; keyword ease on the 0.2s transition, expanded"),
                    "ease-in-out": cubic("0.42, 0, 0.58, 1", f"{MOTION}; keyword ease-in-out on wiggle-soft, expanded"),
                    "linear": cubic("0, 0, 1, 1", f"{MOTION}; keyword linear on circle4Cycle, expanded"),
                },
            },
            "layout": {
                "desktop": dim("1440px", "measured innerWidth after preview_resize 1440x900"),
                "phone": dim("390px", "measured innerWidth after preview_resize 390x844"),
                "content": dim("1152px", f"{MARKETING}; h1 bounding width at 1440"),
            },
        },
        "light": {
            "background": {
                "page": color("#ffffff", f"{MARKETING}; --wst-color-fill-background-primary rgb(255,255,255)"),
                "surface": color("#f0f0f0", f"{MARKETING}; --wst-color-fill-background-secondary rgb(240,240,240)"),
                "header": color("#ffffff", f"{MARKETING}; fixed header background"),
                "login": color("#f4f1f2", f"{LOGIN}; painted page wrapper at 1440"),
                "field": color("#ffffff", f"{LOGIN}; email field background"),
                "section-mint": color("#bdead5", f"{MARKETING}; section background rgb(189, 234, 213)"),
                "section-sage": color("#d2e4c7", f"{MARKETING}; section background rgb(210, 228, 199)"),
            },
            "text": {
                "primary": color("#000000", f"{MARKETING}; --wst-color-text-primary and h1"),
                "secondary": color("#6e6e6e", f"{MARKETING}; --wst-color-text-secondary rgb(110,110,110)"),
                "muted": color("#5e5e5e", f"{MARKETING}; menu eyebrow rgb(94, 94, 94)"),
                "on-accent": color("#ffffff", f"{MARKETING}; Start for free color"),
                "ink": color("#000624", f"{LOGIN}; h1 and input rgb(0, 6, 36), same hex as --wds-color-black-100"),
                "plans": color("#101585", f"{PLANS}; h1 rgb(16, 21, 133)"),
                "link": color("#1a6aff", f"{MARKETING}; --wst-color-action and 22 links rgb(26, 106, 255)"),
                "login-link": color("#2f5dff", f"{LOGIN}; Sign Up and Continue with SSO rgb(47, 93, 255)"),
            },
            "border": {
                "line": color("#000000", f"{MARKETING}; --wst-color-line"),
                "field": color("#868aa5", f"{LOGIN}; email field border rgb(134, 138, 165), same hex as --wds-color-black-400"),
                "social": color("#000000", f"{LOGIN}; Continue with Google border"),
                "plans": color("#101585", f"{PLANS}; Compare Plan Features border"),
                "disabled": color("#c2c2c2", f"{MARKETING}; --wst-color-disabled rgb(194,194,194)"),
            },
            "action": {
                "header": color("#166aea", f"{MARKETING}; Start for free background rgb(22, 106, 234). Token --wst-button-color-fill-primary resolved to rgb(26,106,255); the painted control is this value"),
                "token": color("#1a6aff", f"{MARKETING}; --wst-button-color-fill-primary resolved"),
                "login": color("#2f5dff", f"{LOGIN}; Continue with Email background"),
                "plans": color("#101585", f"{PLANS}; Start for Free background"),
                "ink": color("#000000", f"{MARKETING}; Get Started background"),
                "focus": color("#1b73e8", f"{LOGIN}; Continue with Email focus outline rgb(27, 115, 232)"),
            },
            "status": {
                "success": alias("{color.green.100}", f"{WDS}; --wds-color-fill-success-primary aliases --wds-color-green-100"),
                "warning": alias("{color.yellow.100}", f"{WDS}; --wds-color-fill-warning-primary aliases --wds-color-yellow-100"),
                "danger": alias("{color.red.100}", f"{WDS}; --wds-color-fill-destructive-primary aliases --wds-color-red-100"),
                "urgent": alias("{color.orange.100}", f"{WDS}; --wds-color-fill-urgent-primary aliases --wds-color-orange-100"),
                "info": alias("{color.blue.100}", f"{WDS}; --wds-color-fill-standard-primary aliases --wds-color-blue-100"),
            },
            "scrim": color("#00000080", f"{MARKETING}; open Product menu scrim, computed rgba(0, 0, 0, 0.5)"),
            "focus": {
                "ring": color("#000000", f"{MARKETING}; Product button focus box-shadow 0 0 0 1px and 0 0 0 3px"),
            },
            "component": {
                "button": {
                    "bg": alias("{action.header}", f"{MARKETING}; header CTA"),
                    "text": alias("{text.on-accent}", f"{MARKETING}; header CTA"),
                    "radius": dim("42px", f"{MARKETING}; header CTA"),
                    "height": dim("40px", f"{MARKETING}; header CTA"),
                    "padding": dim("30px", f"{MARKETING}; header CTA padding-left. vertical padding is 8px"),
                },
                "field": {
                    "bg": alias("{background.field}", f"{LOGIN}; email field"),
                    "text": alias("{text.ink}", f"{LOGIN}; email input"),
                    "radius": dim("6px", f"{LOGIN}; email field"),
                    "height": dim("52px", f"{LOGIN}; email field at 1440"),
                },
            },
        },
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
        ],
    }
    tokens["core"]["$extensions"] = {
        "notTokenised": [
            "Dark theme: prefers-color-scheme dark left wix.com light. No dark token set.",
            "Hover and pressed colours: mouseenter did not change the Start for free computed background. Not stored.",
            "Disabled control: --wst-button-color-fill-primary-disabled resolved to rgb(194,194,194). No disabled control was on the page.",
            "Checkbox, radio, switch, select, textarea, tabs, toast, avatar, badge, table: not on the signed-out pages that were opened.",
            "Login form was not submitted. No validation error, no password field, no phone field.",
            "Reduced motion: not emulated. Infinite animations (circle4Cycle 7.2s, marqueeHorizontal 54s, wiggle-soft 3s) were running with prefers-reduced-motion false.",
            "cubic-bezier control points past the first number were truncated by the reader (cubic-bezier(0.645, cubic-bezier(0.12). Not stored as easing tokens.",
            "WDS motion guide publishes ranges (50 to 100ms, 150 to 250ms, 300 to 500ms) and keyword easings, not control points. Upper bounds are stored; the ranges are not a single duration.",
            "Marketing --wst-font-style-* sizes are calc() against a 1920 design width. Computed sizes on the live elements are stored instead.",
            "Screenshots: preview_snapshot returned 'The browser is not producing screenshot frames'. No image was invented.",
            "WDS transparent steps, gradients, and the other 400 semantic aliases are in the page table and not copied one by one.",
            "Phone login h1 is 28px and the field is 50px tall. Desktop values are the tokens.",
        ]
    }
    return tokens


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


def main() -> None:
    data = build()
    check(data)
    path = ROOT / "tokens.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
