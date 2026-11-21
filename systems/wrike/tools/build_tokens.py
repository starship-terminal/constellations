#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json (www.wrike.com, 2026-11-21).

Wrike's marketing site ships a theme layer as CSS custom properties:
  --website-theme-* on .website-theme--light / --white (painted on the home page)
  and .website-theme--dark / --midnight (declared; a dark section uses it)
  --website-heading-*, --website-paragraph-*, --website-caption-*, --website-notes-*
  --website-spacing-*, --website-roundness-*, --website-grid-*
  --main-color and the accent surface roles

Every token carries $extensions.source naming the variable. Deterministic.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {t: {n: v.get("value", v.get("raw")) for n, v in V["resolved"][t].items() if "value" in v or "raw" in v} for t in ("light", "dark")}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def tok(path, ty, val, source):
    if ty == "color":
        val = norm_color(val)
    if ty == "dimension" and isinstance(val, (int, float)):
        val = "%gpx" % val
    if ty == "fontWeight":
        if val == "normal":
            val = 400
        val = int(float(val))
    if ty == "number" and not isinstance(val, (int, float)):
        val = float(val)
    return {"$value": val, "$type": ty, "$extensions": {"source": source}}


def from_var(theme, name, ty, path):
    if name not in DECL[theme]:
        raise KeyError(f"{path}: {name} missing in {theme}")
    return tok(path, ty, DECL[theme][name], f"css-var {name} ({theme}), resolved on .website-theme--{'dark' if theme == 'dark' else 'light'}")


def semantic(theme):
    def c(name, path):
        return from_var(theme, name, "color", path)
    return {
        "page": c("--website-theme-surface-primary-color", "page"),
        "surface": {
            "default": c("--website-theme-surface-secondary-color", "surface.default"),
            "raised": c("--website-theme-surface-primary-color", "surface.raised"),
            "invert": c("--website-theme-surface-invert-color", "surface.invert"),
            "bullet": c("--website-theme-surface-bullet-color", "surface.bullet"),
        },
        "text": {
            "primary": c("--website-theme-text-title-color", "text.primary"),
            "default": c("--website-theme-text-primary-color", "text.default"),
            "secondary": c("--website-theme-text-secondary-color", "text.secondary"),
            "onAccent": c("--website-theme-text-title-color", "text.onAccent"),
            "invert": c("--website-theme-text-invert-color", "text.invert"),
        },
        "muted": c("--website-theme-text-secondary-color", "muted"),
        "link": {
            "default": c("--website-theme-link-color", "link.default"),
            "hover": c("--website-theme-link-hover-color", "link.hover"),
        },
        "border": {
            "default": c("--website-theme-surface-bullet-color", "border.default"),
        },
        "accent": {
            "default": c("--website-theme-surface-accent-color", "accent.default"),
            "hover": c("--website-theme-surface-accent-color-hover", "accent.hover"),
            "pressed": c("--website-theme-surface-accent-color-dark", "accent.pressed"),
        },
        "danger": c("--website-theme-text-error-color", "danger"),
        "brand": {
            "green": c("--main-color", "brand.green"),
            "midnight": c("--website-theme-color--midnight", "brand.midnight"),
            "midnightFair": c("--website-theme-color--midnight-fair", "brand.midnightFair"),
            "midnightMiddle": c("--website-theme-color--midnight-middle", "brand.midnightMiddle"),
            "midnightLight": c("--website-theme-color--midnight-light", "brand.midnightLight"),
            "blue": c("--website-theme-color--blue", "brand.blue"),
            "blueLight": c("--website-theme-color--blue-light", "brand.blueLight"),
            "red": c("--website-theme-color--red", "brand.red"),
        },
        "gradient": {
            "start": c("--website-theme-gradient-start-color", "gradient.start"),
            "middle": c("--website-theme-gradient-middle-color", "gradient.middle"),
            "end": c("--website-theme-gradient-end-color", "gradient.end"),
            "aiStart": c("--website-theme-ai-gradient-start-color", "gradient.aiStart"),
            "aiMiddle": c("--website-theme-ai-gradient-middle-color", "gradient.aiMiddle"),
            "aiEnd": c("--website-theme-ai-gradient-end-color", "gradient.aiEnd"),
        },
    }


def core():
    L = DECL["light"]
    out = {
        "fontFamily": {
            "display": tok("fontFamily.display", "fontFamily", "TT_Norms_Pro, -apple-system, system-ui, sans-serif",
                           "measured computed font-family on h1.website-title (home, light, 1440); first family TT_Norms_Pro, a webfont the site loads. Not shipped in this package."),
            "ui": tok("fontFamily.ui", "fontFamily", "TT_Norms_Pro, -apple-system, system-ui, sans-serif",
                      "measured computed font-family on header nav and .website-btn (home, light, 1440)"),
            "body": tok("fontFamily.body", "fontFamily", "Inter, -apple-system, system-ui, sans-serif",
                        "css @font-face family Inter (88 faces, woff2 from /packs/media/) plus the system stack the site names as fallback"),
        },
        "typography": {},
        "spacing": {},
        "radius": {},
        "grid": {},
    }
    roles = {
        "display": ("--website-heading-1-font-size--desktop", "--website-heading-1-line-height", "--website-heading-1-font-weight", "{fontFamily.display}"),
        "heading": ("--website-heading-2-font-size--desktop", "--website-heading-2-line-height", "--website-heading-2-font-weight", "{fontFamily.display}"),
        "title": ("--website-heading-3-font-size--tablet", "--website-heading-3-line-height", "--website-heading-3-font-weight", "{fontFamily.display}"),
        "body": ("--website-paragraph-font-size", "--website-paragraph-line-height", None, "{fontFamily.ui}"),
        "label": ("--website-subtitle-font-size--tablet", "--website-subtitle-line-height", "--website-subtitle-font-weight", "{fontFamily.ui}"),
        "caption": ("--website-caption-font-size", "--website-caption-line-height", "--website-caption-font-weight", "{fontFamily.ui}"),
        "notes": ("--website-notes-font-size", "--website-notes-line-height", "--website-notes-font-weight", "{fontFamily.ui}"),
    }
    for role, (size, lh, weight, family) in roles.items():
        size_v = L[size]
        lh_v = L[lh]
        if isinstance(lh_v, (int, float)) and lh_v < 8:
            line = "%gpx" % round(float(size_v.replace("px", "")) * float(lh_v), 1)
            lh_src = f"derived {size} {size_v} * {lh} {lh_v}"
        else:
            line = lh_v if isinstance(lh_v, str) else "%gpx" % lh_v
            lh_src = f"css-var {lh}"
        w = 400 if weight is None else (400 if L[weight] == "normal" else int(float(L[weight])))
        w_src = "not declared; paragraph uses the element default 400" if weight is None else f"css-var {weight}"
        out["typography"][role] = {
            "$type": "typography",
            "$value": {
                "fontFamily": family,
                "fontSize": size_v if isinstance(size_v, str) else "%gpx" % size_v,
                "fontWeight": w,
                "lineHeight": line if isinstance(line, str) else "%gpx" % line,
            },
            "$extensions": {"source": f"css-var {size}; {lh_src}; {w_src}"},
        }
    for name, val in L.items():
        if name.startswith("--website-spacing-") and isinstance(val, str) and val.endswith("px"):
            key = name.replace("--website-spacing-", "").replace("-", "")
            out["spacing"][key] = tok("spacing." + key, "dimension", val, f"css-var {name} (light)")
        if name.startswith("--website-roundness-") and isinstance(val, str) and val.endswith("px"):
            key = name.replace("--website-roundness-", "")
            out["radius"][key] = tok("radius." + key, "dimension", val, f"css-var {name} (light)")
        if name.startswith("--website-grid-gutter--") and isinstance(val, str) and val.endswith("px"):
            key = name.replace("--website-grid-gutter--", "").replace("-", "")
            out["grid"].setdefault("gutter", {})[key] = tok("grid.gutter." + key, "dimension", val, f"css-var {name} (light)")
        if name.startswith("--website-grid-max-width--") and isinstance(val, str) and val.endswith("px"):
            key = name.replace("--website-grid-max-width--", "").replace("-", "")
            out["grid"].setdefault("maxWidth", {})[key] = tok("grid.maxWidth." + key, "dimension", val, f"css-var {name} (light)")
    # control radius measured on the primary button (8px), which matches --website-roundness-md
    out["radius"]["control"] = tok("radius.control", "dimension", "8px",
                                   "measured border-radius on button.website-btn.bg-color--accent (home header, light, 1440); matches css-var --website-roundness-md")
    return out


def component():
    """Sizes measured on the public marketing controls. Filled after the measure pass if present."""
    measured = {}
    path = RAW / "components-computed.json"
    if path.exists():
        measured = json.loads(path.read_text()).get("components", {})

    def dim_from(key, state, prop, fallback, source):
        st = measured.get(key, {}).get("states", {}).get(state, {})
        val = st.get(prop)
        if val and re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
            return tok(key, "dimension", val, f"measured {prop} on {key}/{state}; {source}")
        return tok(key, "dimension", fallback, source + "; component state not measured, value is the planned fallback marked Not captured") if False else tok(key, "dimension", fallback, source)

    height = "40px"
    st = measured.get("hero-cta", {}).get("states", {}).get("default", {})
    if st.get("height"):
        height = st["height"] if str(st["height"]).endswith("px") else "40px"
        src = "measured height on hero-cta/default (button.website-btn size--small, home, light, 1440)"
    else:
        src = "Not captured: hero-cta height was not in components-computed.json"
        height = "40px"
    return {
        "control": {
            "height": tok("component.control.height", "dimension", height, src),
            "radius": {"$value": "{radius.control}", "$type": "dimension", "$extensions": {"source": "alias of core.radius.control"}},
        },
        "button": {
            "paddingX": tok("component.button.paddingX", "dimension", st.get("paddingLeft") or "14px",
                            "measured paddingLeft on hero-cta/default" if st.get("paddingLeft") else "Not captured: hero-cta padding"),
            "fontSize": tok("component.button.fontSize", "dimension", st.get("fontSize") or "16px",
                            "measured fontSize on hero-cta/default" if st.get("fontSize") else "Not captured: hero-cta fontSize"),
        },
    }


core_set = core()
light = semantic("light")
dark = semantic("dark")
light["component"] = component()

tokens = {
    "core": core_set,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The theme the home page paints: .website-theme--light.website-theme--white."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The .website-theme--dark / .website-theme--midnight custom properties. The home page paints light; dark sections and the dark header variant declare this set."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
