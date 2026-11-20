#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json for the Luma public site.

Sources, read from lumalabs.ai on 2026-11-18, signed out:
  raw/css-vars.json   custom properties resolved with html.light (appLight,
                      the painted marketing theme) and html.dark (appDark,
                      the class /ray and the 404 paint).

Brand roles are HSL channel triplets (--surface-*, --primary, --secondary,
--tertiary, --inactive, and the inverted set). They are stored as the
declared channels and also as the hex the probe computed. A shadcn oklch
layer (--background, --foreground, --border, --destructive, --muted) is
kept as computed hex. Tailwind v4 theme scales (type, radius, easing,
spacing, gray) come from the same harvest.

Every token carries $extensions.source. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIGHT = V["resolved"]["appLight"]
DARK = V["resolved"]["appDark"]


def val(theme, name):
    row = (LIGHT if theme == "light" else DARK).get(name) or {}
    if "value" not in row and "raw" not in row:
        raise KeyError(f"{name} missing from resolved.{theme}")
    return row.get("value", row.get("raw"))


def src(theme, name):
    return f"css-var {name} resolved on html.{theme} (lumalabs.ai, 2026-11-18)"


def leaf(value, ty, source, description=None):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


def hex_of(theme, name):
    """A colour token is always #rrggbb or rgba().

    The probe's computed-style reader joins rgb channels with commas, so a
    real colour can arrive as "#ff,ff,ff". Brand roles are authored as HSL
    channel triplets ("0 0% 100%") and CSS.supports('color') is true for that
    string, so the probe stored them as kind other. Both shapes are converted
    here. The authored triplet stays in the channels group.
    """
    row = (LIGHT if theme == "light" else DARK).get(name) or {}
    raw = (row.get("raw") or "").strip()
    value = row.get("value", raw)
    if isinstance(value, str):
        m = re.fullmatch(r"#([0-9a-fA-F]{2}),([0-9a-fA-F]{2}),([0-9a-fA-F]{2})", value.strip())
        if m:
            return "#" + "".join(m.groups()).lower()
        if re.fullmatch(r"#[0-9a-fA-F]{6}", value.strip()) or value.strip().startswith("rgba("):
            return value.strip().lower() if value.strip().startswith("#") else value.strip()
    m = re.fullmatch(r"([\d.]+) ([\d.]+)% ([\d.]+)%", raw)
    if m:
        h, s, l = float(m.group(1)), float(m.group(2)) / 100, float(m.group(3)) / 100
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m0 = l - c / 2
        sector = int(h // 60) % 6
        rgb = [
            (c, x, 0), (x, c, 0), (0, c, x),
            (0, x, c), (x, 0, c), (c, 0, x),
        ][sector]
        parts = [round((v + m0) * 255) for v in rgb]
        return "#%02x%02x%02x" % tuple(parts)
    raise KeyError(f"{name} is not a colour in resolved.{theme}: {value!r} raw={raw!r}")


def color(theme, name, description=None):
    return leaf(hex_of(theme, name), "color", src(theme, name), description)


def has(theme, name):
    return name in (LIGHT if theme == "light" else DARK)


def other(theme, name, ty, description=None):
    v = val(theme, name)
    if ty == "fontWeight" and isinstance(v, str) and v.isdigit():
        v = int(v)
    if ty == "cubicBezier" and isinstance(v, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", v)
        if not m:
            raise ValueError(f"{name}: not a cubic-bezier: {v}")
        v = [float(x) for x in m.groups()]
    if ty == "dimension" and isinstance(v, str):
        v = re.sub(r"^(-?)\.(\d)", r"\g<1>0.\2", v.strip())
    return leaf(v, ty, src(theme, name), description)


def channels(theme, name):
    """The authored HSL triplet, kept beside the computed hex."""
    row = (LIGHT if theme == "light" else DARK).get(name) or {}
    raw = row.get("raw")
    if not raw or not re.fullmatch(r"[\d.]+ [\d.]+% [\d.]+%", raw.strip()):
        return None
    return leaf(raw.strip(), "other", src(theme, name) + "; authored HSL channels, consumed as hsl(var(--name))",
                "Authored channel triplet. The painted colour is the sibling hex token.")


OBSERVED = V.get("observedFonts") or {}

# Next.js local fonts compute to a hashed family name ("__graphik_7126cf") that resolves nowhere
# outside the page. The token carries the face's real name; the computed stack stays beside it.
LOCAL_FONTS = {"graphik": "Graphik"}


def observed_family(key):
    """A computed family from raw/css-vars.json observedFonts. A missing reading fails the build."""
    computed = OBSERVED.get(key)
    if not computed:
        raise SystemExit(f"observedFonts.{key} missing from raw/css-vars.json")
    m = re.match(r"__([A-Za-z]+)_[0-9a-f]{6}\b", computed)
    if not m or m.group(1).lower() not in LOCAL_FONTS:
        raise SystemExit(f"observedFonts.{key} is not a known Next.js local font: {computed!r}")
    return LOCAL_FONTS[m.group(1).lower()], computed


BODY_FACE, BODY_COMPUTED = observed_family("bodyFamily")
H1_FACE, H1_COMPUTED = observed_family("h1Family")
graphik = leaf(
    f"{BODY_FACE}, sans-serif",
    "fontFamily",
    f"derived from the computed font-family on body, lumalabs.ai / , 2026-11-18: {BODY_COMPUTED}, the Next.js "
    f"local name for {BODY_FACE}. Not a resolvable :root custom property.",
    "UI face. The family is named as the font loader's local name says; the computed stack is in $extensions.computed.",
)
graphik["$extensions"]["computed"] = BODY_COMPUTED
if H1_FACE == BODY_FACE:
    editorial = leaf(
        "{font.family.graphik}", "fontFamily",
        f"computed font-family on the home h1, lumalabs.ai / , 2026-11-18: {H1_COMPUTED}, the same face as body.",
        "The home h1 computed to Graphik on this pass. PP Editorial is loaded on the page but was not the computed h1 family.",
    )
else:
    editorial = leaf(f"{H1_FACE}, serif", "fontFamily",
                     f"derived from the computed font-family on the home h1, lumalabs.ai / , 2026-11-18: {H1_COMPUTED}.",
                     "Display face of the home h1.")
    editorial["$extensions"]["computed"] = H1_COMPUTED

core = {
    "font": {
        "family": {
            "graphik": graphik,
            "editorial": editorial,
            "sans": other("light", "--font-sans", "fontFamily",
                          "Tailwind default sans. Body text uses the Graphik local font, not this stack."),
            "mono": other("light", "--font-mono", "fontFamily",
                          "Tailwind default mono. The marketing site does not set a branded mono face."),
        },
        "weight": {
            k: other("light", name, "fontWeight")
            for k, name in (
                ("normal", "--font-weight-normal"),
                ("medium", "--font-weight-medium"),
                ("semibold", "--font-weight-semibold"),
                ("bold", "--font-weight-bold"),
            )
            if has("light", name)
        },
        "size": {},
    },
    "radius": {},
    "spacing": {},
    "easing": {
        k: other("light", name, "cubicBezier")
        for k, name in (("in", "--ease-in"), ("out", "--ease-out"), ("in-out", "--ease-in-out"))
        if has("light", name)
    },
    "layout": {},
}
if has("light", "--navigation-bar-height"):
    core["layout"]["nav-height"] = other("light", "--navigation-bar-height", "dimension",
                                         "Declared nav height. The painted bar is measured in components.md.")
if has("light", "--spacing"):
    core["spacing"]["unit"] = other("light", "--spacing", "dimension",
                                    "Tailwind spacing base. Utilities are multiples of this.")
else:
    core.pop("spacing", None)

for step, name in (
    ("xs", "--text-xs"), ("sm", "--text-sm"), ("base", "--text-base"),
    ("lg", "--text-lg"), ("xl", "--text-xl"), ("2xl", "--text-2xl"),
    ("3xl", "--text-3xl"), ("4xl", "--text-4xl"), ("5xl", "--text-5xl"),
):
    if has("light", name):
        core["font"]["size"][step] = other("light", name, "dimension")

for step, name in (
    ("xs", "--radius-xs"), ("sm", "--radius-sm"), ("md", "--radius-md"),
    ("lg", "--radius-lg"), ("xl", "--radius-xl"), ("2xl", "--radius-2xl"),
    ("3xl", "--radius-3xl"), ("4xl", "--radius-4xl"),
):
    if has("light", name):
        core["radius"][step] = other("light", name, "dimension")

# Neutral ramp the sheets actually declare, not a full 50-950 invention.
gray = {}
for step in ("50", "100", "200", "300", "400", "500", "600", "700", "800"):
    key = f"--color-gray-{step}"
    if key in LIGHT:
        gray[step] = color("light", key)
if gray:
    core["color"] = {"gray": gray}


def semantic(theme):
    roles = {
        "surface": {
            "page": color(theme, "--surface-primary", "Page field. hsl(var(--surface-primary))."),
            "surface": color(theme, "--surface-subtle", "Raised panel. hsl(var(--surface-subtle)). Catalog surface swatch."),
            "subtle": color(theme, "--surface-subtle"),
            "elevated": color(theme, "--surface-elevated"),
            "inverted": color(theme, "--surface-inverted-primary", "Sign In and Try for free fill on the light site."),
            "inverted-subtle": color(theme, "--surface-inverted-subtle"),
            "inverted-elevated": color(theme, "--surface-inverted-elevated"),
        },
        "text": {
            "primary": color(theme, "--primary"),
            "secondary": color(theme, "--secondary"),
            "tertiary": color(theme, "--tertiary"),
            "inactive": color(theme, "--inactive"),
            "on-accent": color(theme, "--inverted-primary", "Text on the inverted button fill."),
            "muted": color(theme, "--secondary", "Secondary label colour. Catalog muted swatch."),
        },
        "shadcn": {
            "background": color(theme, "--background"),
            "foreground": color(theme, "--foreground"),
            "muted": color(theme, "--muted"),
            "muted-foreground": color(theme, "--muted-foreground"),
            "border": color(theme, "--border"),
            "input": color(theme, "--input"),
            "ring": color(theme, "--ring"),
            "destructive": color(theme, "--destructive"),
            "border": color(theme, "--border", "Hairline. Catalog border swatch."),
            "accent": color(theme, "--surface-inverted-primary", "The filled pill. Catalog accent swatch. Luma spends black and white, not a hue."),
        },
    }
    channels_group = {}
    for name in (
        "--surface-primary", "--surface-subtle", "--surface-elevated",
        "--surface-inverted-primary", "--primary", "--secondary", "--tertiary",
        "--inactive", "--inverted-primary",
    ):
        ch = channels(theme, name)
        if ch:
            channels_group[name.lstrip("-").replace("--", "")] = ch
    if channels_group:
        roles["channels"] = channels_group
    return roles


tokens = {
    "core": core,
    "light": semantic("light"),
    "dark": semantic("dark"),
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "html.light. Pricing, about, API, news and the inner marketing pages paint a white page with black text. The home hero paints a dark video under the same sheets.",
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "html.dark. /ray paints a black field with white text. The home hero also paints dark media. There is no theme switch on the marketing pages.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
