#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/css-vars.json.

kinhive.com declares its palette, type, radius and motion on :root,:host, and
a second palette under html[data-app-theme=system] inside
prefers-color-scheme: dark. tools/capture/vars.mjs resolves both. This builder
reads those resolved values. It does not invent a component tree.

Deterministic: same inputs, byte-identical output. Edit the raw file, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# docs/EVIDENCE.md: a value typed into the builder with no reading in raw/ is a Reconstruction.
HAND = "Reconstruction: entered by hand at capture time; no reading in raw/ holds it."
DECL = {t: V["resolved"][t] for t in ("light", "dark")}

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")
EASE = {
    "ease": [0.25, 0.1, 0.25, 1],
    "ease-in": [0.42, 0, 1, 1],
    "ease-out": [0, 0, 0.58, 1],
    "ease-in-out": [0.42, 0, 0.58, 1],
    "linear": [0, 0, 1, 1],
}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a.rstrip("%")) in (1, 100):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        af = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "rgba(%s, %s, %s, %g)" % (r, g, b, af)
    raise ValueError("not a colour: " + v)


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def leaf(path, ty, val, src, description=None):
    if ty == "color":
        val = norm_color(val)
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", val.strip())
        val = [float("%g" % float(x)) for x in m.groups()] if m else EASE.get(val.strip(), val)
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:
            val = round(float(m.group(1)) / float(m.group(2)), 4)
        elif re.fullmatch(r"-?\d+(\.\d+)?", val):
            val = float(val) if "." in val else int(val)
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"([\d.]+)(m?s)", val.strip())
        if m:
            val = ("%g" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))) + "ms"
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
        val = val.strip() + "px"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if description:
        t["$description"] = description
    return t


def from_var(path, name, theme, ty, description=None):
    rec = DECL[theme].get(name)
    if not rec or "value" not in rec:
        raise KeyError(f"{path}: {name} has no resolved value in {theme}")
    return leaf(path, ty, rec["value"], f"css-var {name} ({theme}); declared custom property in kinhive.com's css bundle", description)


def alias(path, target, ty, src):
    t = {"$value": "{" + target + "}", "$type": ty, "$extensions": {"source": src}}
    return t


# Colour roles that flip between the light :root declaration and the dark
# media query. Names that stay the same are core ramps, aliased into both themes.
FLIP = {
    "ink", "body", "muted", "line", "canvas", "raised", "cream", "white",
    "cobalt", "cobalt-soft", "chartreuse-soft", "tomato-soft", "forest",
    "forest-soft", "lavender", "butter", "link", "destructive", "kh-yellow",
}
# forest-soft is declared only in the dark palette.
CORE_COLORS = [
    "black", "red-700", "chartreuse", "tomato", "maroon", "chocolate",
    "apricot", "tangerine", "cobalt-deep", "kh-green", "kh-orange", "alert",
]


def color_name(raw):
    return raw[len("--color-"):].replace("-", ".") if False else raw[len("--color-"):]


def semantic(theme):
    out = {"color": {}}
    for raw in sorted(k for k in DECL[theme] if k.startswith("--color-")):
        name = raw[len("--color-"):]
        if name in FLIP or (theme == "dark" and name == "forest-soft"):
            out["color"][name] = from_var(f"{theme}.color.{name}", raw, theme, "color")
        else:
            # A colour that does not flip resolves the same in both themes. It is
            # written as its value: a bare {color.name} on color.name resolves to
            # itself, and {core.color.name} names a set, which DTCG and Tokens
            # Studio readers report as dangling. Semantic roles below keep
            # {color.name} so they read this theme's own value when it flips.
            out["color"][name] = from_var(f"{theme}.color.{name}", raw, theme, "color",
                                          "Resolves the same in both themes, like core.color." + name + ".")
    # Roles a screen uses, named after the product's own tokens.
    out["background"] = {
        "page": alias(f"{theme}.background.page", f"color.white", "color", "the page field is --color-white"),
        "canvas": alias(f"{theme}.background.canvas", f"color.canvas", "color", "section wash is --color-canvas"),
        "raised": alias(f"{theme}.background.raised", f"color.raised", "color", "raised chips sit on --color-raised"),
        "cream": alias(f"{theme}.background.cream", f"color.cream", "color", "cream bands use --color-cream"),
        "ink": alias(f"{theme}.background.ink", f"color.ink", "color", "primary actions fill with --color-ink"),
        "butter": alias(f"{theme}.background.butter", f"color.butter", "color", "the promo strip and icon-button face use --color-butter"),
    }
    out["text"] = {
        "ink": alias(f"{theme}.text.ink", "color.ink", "color", "primary text is --color-ink"),
        "body": alias(f"{theme}.text.body", "color.body", "color", "secondary text is --color-body"),
        "muted": alias(f"{theme}.text.muted", "color.muted", "color", "placeholders and meta use --color-muted"),
        "on-ink": alias(f"{theme}.text.on-ink", "color.white", "color", "text on an ink fill is --color-white"),
        "link": alias(f"{theme}.text.link", "color.link", "color", "links use --color-link"),
    }
    out["border"] = {
        "line": alias(f"{theme}.border.line", "color.line", "color", "hairlines and field borders are --color-line"),
        "focus": alias(f"{theme}.border.focus", "color.ink", "color", "focused fields set border-color to --color-ink (focus:border-ink)"),
    }
    out["action"] = {
        "fill": alias(f"{theme}.action.fill", "color.ink", "color", "Join free, Subscribe and Continue fill with --color-ink"),
        "fill-hover": leaf(f"{theme}.action.fill-hover", "color", "#2a2a2c", f"{HAND} Typed from the hover:bg-[#2a2a2c] utility on the ink CTA (kinhive.com header Join free, 2026-11-18); hover was not measured."),
        "ink": alias(f"{theme}.action.ink", "color.white", "color", "label on the ink CTA is --color-white"),
        "cobalt": alias(f"{theme}.action.cobalt", "color.cobalt", "color", "the cobalt accent is --color-cobalt"),
    }
    out["status"] = {
        "destructive": alias(f"{theme}.status.destructive", "color.destructive", "color", "declared --color-destructive"),
        "alert": alias(f"{theme}.status.alert", "color.alert", "color", "declared --color-alert"),
        "forest": alias(f"{theme}.status.forest", "color.forest", "color", "declared --color-forest"),
    }
    return out


def core():
    light = DECL["light"]
    c = {"color": {}, "font": {"family": {}, "weight": {}, "size": {}, "leading": {}}, "radius": {}, "spacing": {}, "motion": {}}
    for raw, rec in sorted(light.items()):
        if not raw.startswith("--color-") or "value" not in rec:
            continue
        name = raw[len("--color-"):]
        # Core keeps the light declaration. Dark-only names are omitted here.
        if name == "forest-soft":
            continue
        c["color"][name] = leaf(f"core.color.{name}", "color", rec["value"], f"css-var {raw} (light); declared on :root,:host in kinhive.com's css bundle")
    # Families: the declared stacks, which resolve through next/font variables.
    # The two stacks are the declared --font-sans and --font-heading with their
    # next/font variables substituted; raw/ holds the declarations, not a computed read.
    for name in ("--font-figtree", "--font-affairs"):
        if not any(name in (r.get("properties") or {}) for b in ("theme", "app", "tailwind") for r in V.get(b) or []):
            raise KeyError(f"{name} is not declared in raw/css-vars.json")
    c["font"]["family"]["sans"] = leaf(
        "core.font.family.sans", "fontFamily",
        "Figtree, \"Figtree Fallback\", ui-sans-serif, system-ui, sans-serif",
        "Derived: the declared --font-sans (var(--font-figtree), ui-sans-serif, system-ui, sans-serif) with the declared --font-figtree (\"Figtree\", \"Figtree Fallback\") substituted (raw/css-vars.json)",
    )
    c["font"]["family"]["heading"] = leaf(
        "core.font.family.heading", "fontFamily",
        "affairs, \"affairs Fallback\", Georgia, serif",
        "Derived: the declared --font-heading (var(--font-affairs), Georgia, serif) with the declared --font-affairs (\"affairs\", \"affairs Fallback\", Georgia, serif) substituted (raw/css-vars.json)",
    )
    c["font"]["family"]["mono"] = from_var("core.font.family.mono", "--font-mono", "light", "fontFamily")
    for raw, key in (("--font-weight-normal", "normal"), ("--font-weight-medium", "medium"), ("--font-weight-semibold", "semibold"), ("--font-weight-bold", "bold")):
        c["font"]["weight"][key] = from_var(f"core.font.weight.{key}", raw, "light", "fontWeight")
    for raw, key in (("--text-xs", "xs"), ("--text-sm", "sm"), ("--text-xl", "xl")):
        c["font"]["size"][key] = from_var(f"core.font.size.{key}", raw, "light", "dimension")
    for raw, key in (("--text-xs--line-height", "xs"), ("--text-sm--line-height", "sm"), ("--leading-tight", "tight"), ("--leading-snug", "snug"), ("--leading-relaxed", "relaxed")):
        rec = light[raw]
        ty = "number"
        c["font"]["leading"][key] = from_var(f"core.font.leading.{key}", raw, "light", ty)
    for raw, key in (("--radius-sm", "sm"), ("--radius-md", "md"), ("--radius-lg", "lg"), ("--radius-xl", "xl"), ("--radius-2xl", "2xl")):
        c["radius"][key] = from_var(f"core.radius.{key}", raw, "light", "dimension")
    c["spacing"]["unit"] = from_var("core.spacing.unit", "--spacing", "light", "dimension", "Tailwind spacing unit. Utilities multiply it (px-3 is 0.75rem).")
    c["spacing"]["container-xs"] = from_var("core.spacing.container-xs", "--container-xs", "light", "dimension")
    c["spacing"]["container-xl"] = from_var("core.spacing.container-xl", "--container-xl", "light", "dimension")
    c["motion"]["duration"] = from_var("core.motion.duration", "--default-transition-duration", "light", "duration")
    c["motion"]["easing"] = from_var("core.motion.easing", "--default-transition-timing-function", "light", "cubicBezier")
    # Control geometry typed in from the 2026-11-18 homepage probe. The probe's
    # readings were never committed, so no file in raw/ holds them.
    c["component"] = {
        "nav-height": leaf("core.component.nav-height", "dimension", "65px", f"{HAND} Typed from the height of header.sticky on kinhive.com / at 1440, 2026-11-18."),
        "nav-link-size": leaf("core.component.nav-link-size", "dimension", "14px", f"{HAND} Typed from the font-size of the header nav links (text-[14px]), 2026-11-18."),
        "cta-height": leaf("core.component.cta-height", "dimension", "32px", f"{HAND} Typed from the height of the header Join free link (h-8), 2026-11-18."),
        "cta-radius": leaf("core.component.cta-radius", "dimension", "8px", f"{HAND} Typed from the border-radius of the header Join free link (rounded-lg), 2026-11-18."),
        "field-height": leaf("core.component.field-height", "dimension", "44px", f"{HAND} Typed from the height of #hero-email (h-11), 2026-11-18."),
        "hero-size": leaf("core.component.hero-size", "dimension", "44px", f"{HAND} Typed from the font-size of the home h1 at 1440 (sm:text-[44px] on the affairs heading), 2026-11-18."),
        "page-width": leaf("core.component.page-width", "dimension", "1440px", "desktop capture viewport, 2026-11-18"),
        "phone-width": leaf("core.component.phone-width", "dimension", "390px", "phone capture viewport, 2026-11-18"),
    }
    return c


core_set = core()
light = semantic("light")
dark = semantic("dark")

# Drop alias targets that the semantic builder pointed at a missing core name.
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core_set)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def prune(theme_name, tree):
    """A semantic colour that aliases a missing core name becomes a direct read."""
    names = NAMES | {n for n, _ in tokens_of(tree)}
    for n, t in list(tokens_of(tree)):
        for a in aliases(t["$value"]):
            ref = a[5:] if a.startswith("core.") else a
            if ref not in names and ref.startswith("color."):
                raw = "--color-" + ref.split(".", 1)[1]
                if raw in DECL[theme_name] and "value" in DECL[theme_name][raw]:
                    t["$value"] = norm_color(DECL[theme_name][raw]["value"])
                    t["$extensions"]["source"] = f"css-var {raw} ({theme_name}); alias target core.{ref} is dark-only or absent"
                else:
                    raise KeyError(f"{theme_name}.{n}: alias {{{a}}} points at nothing")


prune("light", light)
prune("dark", dark)

for n, t in list(tokens_of(core_set)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"core.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core_set,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The painted public theme. kinhive.com does not set data-app-theme on the live document, so :root colours paint."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The declared dark palette under @media (prefers-color-scheme: dark) on html[data-app-theme=system]. Resolved by emulating that media query. The public site has no theme toggle."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
