#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Values are the custom properties resolved on :root of https://www.make.com/
on 2026-11-21 (Playwright getComputedStyle). Make's marketing site ships one
light theme. A dark band on the FAQ and 404 is a section colour, not a second
theme, so there is no dark set.

Every token carries $extensions.source. A clamp() spacing or type size is
kept as the desktop end of the clamp (the max), labelled Derived, because
DTCG dimension wants one length. The authored clamp stays in raw/css-vars.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
R = RAW["resolved"]

SRC = "css-var resolved on :root, https://www.make.com/, 2026-11-21 (raw/css-vars.json)"


def color(name):
    v = R[name].strip()
    if v.startswith("#") and len(v) in (4, 7):
        if len(v) == 4:
            v = "#" + "".join(c * 2 for c in v[1:])
        return v.lower()
    if v == "white":
        return "#ffffff"
    if v == "transparent":
        return "transparent"
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    raise ValueError(f"{name} is not a flat colour: {v!r}")


def rem_px(value):
    """One rem length to px at 16px root. Derived."""
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", value.strip())
    if not m:
        raise ValueError(value)
    px = float(m.group(1)) * 16
    return ("%g" % round(px, 3)) + "px"


def clamp_max_px(value):
    """Desktop end of a Make clamp(min, fluid, max). The max is N * 1rem."""
    m = re.search(r",\s*(-?\d*\.?\d+)\s*\*\s*1rem\)\s*$", value.strip())
    if not m:
        raise ValueError("no clamp max: " + value[:80])
    px = float(m.group(1)) * 16
    return ("%g" % round(px, 3)) + "px"


def token(value, typ, source, extra=None):
    ext = {"source": source}
    if extra:
        ext.update(extra)
    return {"$type": typ, "$value": value, "$extensions": ext}


def swatch(group, step):
    key = f"--_default---swatch--{group}-{step}"
    if key not in R and group == "brand" and step == "500":
        key = "--_default---swatch--brand-500-main"
    return token(color(key), "color", f"{SRC}; {key}")


def ramp(group, steps):
    return {step: swatch(group, step) for step in steps}


STEPS = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

core = {
    "color": {
        "brand": ramp("brand", STEPS),
        "accent": ramp("accent", STEPS),
        "neutral": ramp("neutral", STEPS),
        "gray": ramp("gray", STEPS),
        "green": ramp("green", STEPS),
        "red": ramp("red", STEPS),
        "yellow": ramp("yellow", STEPS),
        "blue": {
            "300": swatch("blue", "300"),
            "600": swatch("blue", "600"),
        },
    },
    "font": {
        "family": {
            "sans": token(
                "Satoshi, Arial, sans-serif",
                "fontFamily",
                SRC + "; --_typography---font--primary-family",
            ),
            "fallback": token(
                'Arial, "Helvetica Neue", Helvetica, sans-serif',
                "fontFamily",
                SRC + "; --_typography---font--secondary-font",
            ),
            "mono": token(
                '"Geist Mono Latin 300", Arial, sans-serif',
                "fontFamily",
                SRC + "; --_typography---font--tertiary-font",
            ),
        },
        "weight": {
            "regular": token("400", "fontWeight", SRC + "; --_typography---font--primary-regular"),
            "medium": token("500", "fontWeight", SRC + "; --_typography---font--primary-medium"),
            "semibold": token("600", "fontWeight", SRC + "; --_typography---font--primary-semibold"),
            "bold": token("800", "fontWeight", SRC + "; --_typography---font--primary-bold"),
        },
    },
    "typography": {},
    "space": {},
    "radius": {
        "small": token(rem_px(R["--_default---radius--small"]), "dimension", SRC + "; --_default---radius--small (0.5rem)", {"derived": "rem to px at 16px root"}),
        "medium": token(rem_px(R["--_default---radius--medium"]), "dimension", SRC + "; --_default---radius--medium (0.75rem)", {"derived": "rem to px at 16px root"}),
        "main": token(rem_px(R["--_default---radius--main"]), "dimension", SRC + "; --_default---radius--main (1rem)", {"derived": "rem to px at 16px root"}),
        "round": token("9999px", "dimension", SRC + "; --_default---radius--round is 100vw (pill). 9999px is the practical pill length", {"derived": "100vw recorded as a pill"}),
    },
    "size": {
        "buttonSmall": token(rem_px("2rem"), "dimension", SRC + "; --_default---swatch--button-size--small"),
        "buttonMedium": token(rem_px("3rem"), "dimension", SRC + "; --_default---swatch--button-size--medium"),
        "buttonLarge": token(rem_px("5rem"), "dimension", SRC + "; --_default---swatch--button-size--large"),
        "gutter": token(rem_px(R["--_default---site--gutter"]), "dimension", SRC + "; --_default---site--gutter"),
    },
    "motion": {
        "cardHoverDuration": token("0.3s", "duration", SRC + "; --card-hover-duration"),
        "cardHoverEase": token("ease", "cubicBezier", SRC + "; --card-hover-ease is the keyword ease, not a cubic-bezier()"),
        "themeEase": token("cubic-bezier(0.4, 0, 0.2, 1)", "cubicBezier", SRC + "; --theme-ease"),
    },
    "shadow": {
        "cardHover": token(
            "0px 20px 40px -12px rgba(52, 34, 55, 0.18)",
            "shadow",
            SRC + "; --card-hover-shadow",
        ),
    },
}

TYPE_ROLES = [
    ("display", "--_typography---font-size--display", "500", "1.2"),
    ("h1", "--_typography---font-size--h1", "500", "1.2"),
    ("h2", "--_typography---font-size--h2", "500", "1.2"),
    ("h3", "--_typography---font-size--h3", "500", "1.25"),
    ("h4", "--_typography---font-size--h4", "500", "1.3"),
    ("h5", "--_typography---font-size--h5", "500", "1.35"),
    ("h6", "--_typography---font-size--h6", "500", "1.4"),
    ("text-xlarge", "--_typography---font-size--text-xlarge", "400", "1.5"),
    ("text-large", "--_typography---font-size--text-large", "400", "1.5"),
    ("body", "--_typography---font-size--text-main", "400", "1.5"),
    ("text-small", "--_typography---font-size--text-small", "400", "1.5"),
    ("caption", "--_typography---font-size--text-xsmall", "400", "1.5"),
]
for role, key, weight, lh in TYPE_ROLES:
    size = clamp_max_px(R[key])
    core["typography"][role] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.sans}",
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": lh,
        },
        "$extensions": {
            "source": f"{SRC}; {key} desktop clamp end. lineHeight {lh} is --_text-style---line-height (1.5) for body and a Derived heading ratio from the live h1 (60px/72px = 1.2) where the role is display or h1; other heading ratios are Derived from the same scale, not a per-role token",
        },
    }

SPACE_KEYS = [
    "4", "6", "8", "12", "16", "20", "24", "28", "32", "36", "40", "48", "64", "80", "96", "112", "160", "224",
]
for step in SPACE_KEYS:
    key = f"--_spacing---space--{step}"
    core["space"][step] = token(
        clamp_max_px(R[key]),
        "dimension",
        f"{SRC}; {key} desktop clamp end",
        {"derived": "desktop end of fluid clamp"},
    )
core["space"]["none"] = token("0px", "dimension", SRC + "; --_spacing---space--none (0rem)", {"derived": "0rem to 0px"})

# Semantic light roles. Page, text and accent come from computed body/h1/button
# on the homepage, which match these swatches. Secondary text and link are theme vars.
light = {
    "page": token("{color.neutral.50}", "color", SRC + "; body background computed rgb(255,255,255) on home; nearest published swatch is neutral (white). Page is recorded as white via neutral alias after check", ),
    "surface": token("#ffffff", "color", "computed backgroundColor on body, https://www.make.com/, 2026-11-21"),
    "raised": token("#ffffff", "color", "computed background of the Product mega menu panel, visible in screenshots/home-light-product-menu.png; not a separate custom property"),
    "text": token("{color.neutral.900}", "color", "computed color on body and h1 is rgb(52, 34, 55), which is --_default---swatch--neutral-900 / --_default---swatch--brand-text"),
    "muted": token("{color.neutral.600}", "color", SRC + "; --_theme---text-secondary rgb(105, 88, 108) matches neutral-600"),
    "placeholder": token("{color.neutral.500}", "color", SRC + "; --_theme---text-placeholder"),
    "onAccent": token("#ffffff", "color", "computed color on the Try it free button, https://www.make.com/, 2026-11-21"),
    "link": token("#803bbf", "color", SRC + "; --_theme---text-link--text rgb(128, 59, 191), brand-700"),
    "accent": token("#8f4bd2", "color", "computed backgroundColor on Try it free, rgb(143, 75, 210), brand-600"),
    "accentHover": token("#803bbf", "color", "computed backgroundColor on Try it free while hovered, rgb(128, 59, 191), brand-700"),
    "border": token("{color.neutral.300}", "color", SRC + "; --_default---swatch--neutral-300. Field borders on the login wall match this family; exact field border is Not captured as its own token"),
    "borderBrand": token("#a66ee2", "color", SRC + "; --_theme---border-brand"),
    "success": token("{color.green.500}", "color", SRC + "; green ramp. The home 'No credit card required' check uses a green fill; the exact check colour was not isolated from the icon"),
    "danger": token("{color.red.500}", "color", SRC + "; red ramp. No live error state was submitted, so this is the published ramp, not a field error"),
    "warning": token("{color.yellow.500}", "color", SRC + "; yellow ramp. No warning component was on the public pages"),
    "info": token("{color.blue.300}", "color", SRC + "; --_default---swatch--blue-300. No info component was on the public pages"),
    "scrim": token("rgba(52, 34, 55, 0.45)", "color", "Not captured as a custom property. The Product menu dims the page; this value is Sampled-adjacent and marked Not captured in the coverage table rather than used as measured"),
    "focus": token("{color.neutral.900}", "color", "Not captured. First Tab landed on the code-island host with outline none. Focus ring is Not captured"),
}

# page should be the measured white, not an alias that we then contradict
light["page"] = token("#ffffff", "color", "computed backgroundColor on body, https://www.make.com/, 2026-11-21, rgb(255, 255, 255)")
# drop the speculative scrim and focus from semantic set; they are Not captured
del light["scrim"]
del light["focus"]

doc = {
    "$description": "Make (make.com) public marketing site, captured 2026-11-21. One light theme. Values from resolved CSS custom properties and computed styles.",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

# Checks
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)

errors = []
for path, node in walk(doc):
    if "source" not in node.get("$extensions", {}):
        errors.append("no source " + path)
    if node["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", str(node["$value"])):
        errors.append("bad dimension " + path + " " + str(node["$value"]))
    if node["$type"] == "color" and node["$value"].startswith("{") is False:
        if not (node["$value"].startswith("#") or node["$value"].startswith("rgb") or node["$value"] == "transparent"):
            errors.append("bad color " + path + " " + node["$value"])
if errors:
    raise SystemExit("\n".join(errors))

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print(f"wrote {out} ({sum(1 for _ in walk(doc))} tokens)")
