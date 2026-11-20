#!/usr/bin/env python3
"""Build tokens.json from the LinkedIn guest stylesheet harvest.

Sources, read signed out from linkedin.com:
  raw/css-vars.json   --color-* and the artdeco font/link resets, resolved
                      the way the browser resolves them (tools/capture/vars.mjs).
  raw/components-computed.json  every font size, weight, radius, spacing step
                      and control size, read from a named component; the
                      build stops when a reading is missing. The four steps
                      no element measured (fontSize.lg, radius.md,
                      radius.full, spacing.1) carry the Reconstruction label.

The guest site paints one light theme. The dark set stays empty. Every
token carries $extensions.source. A name that did not resolve is omitted,
never filled in.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {n: d.get("value", d.get("raw")) for n, d in V.get("resolved", {}).get("light", {}).items()}


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
            return "#%02x%02x%02x" % (r, g, b) if a >= 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a[:-1]) / 100 if a.endswith("%") else float(a or 1) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


def color(path, name, description=None):
    if name not in DECL:
        raise KeyError(f"{path}: {name} did not resolve in raw/css-vars.json")
    val = norm_color(DECL[name])
    t = {
        "$value": val,
        "$type": "color",
        "$extensions": {"source": f"css-var {name} (light); guest stylesheet on linkedin.com"},
    }
    if description:
        t["$description"] = description
    return t


def dim(path, value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError(f"{path}: dimension {value!r}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_family(name, fallback_source):
    raw = DECL.get(name, "")
    # The artdeco reset quotes a long system stack. Keep the first family.
    first = raw.split(",")[0].strip().strip("'\"") if raw else ""
    if not first:
        first = "-apple-system"
        src = fallback_source
    else:
        src = f"css-var {name} (light)"
    return {"$value": first, "$type": "fontFamily", "$extensions": {"source": src, "stack": raw or fallback_source}}


ROLES = {
    "brand": "--color-brand",
    "brand-hover": "--color-action-active",
    "text": "--color-text",
    "text-secondary": "--color-text-low-emphasis",
    "text-on-brand": "--color-button-label-primary",
    "link": "--color-link",
    "link-hover": "--color-link-hover",
    "link-visited": "--artdeco-reset-link-color-purple7",
    "border": "--color-border",
    "border-faint": "--color-border-faint",
    "divider": "--color-divider-solid",
    "icon": "--color-icon",
    "background-container": "--color-background-container",
    "background-canvas": "--color-background-canvas",
    "action": "--color-action",
    "positive": "--color-container-positive",
    "caution": "--color-container-caution",
    "negative": "--color-container-negative",
    "neutral": "--color-container-neutral",
    "help": "--color-container-help",
    "input-border": "--color-input-container-border",
    "input-border-error": "--color-input-container-border-error",
    "button-primary": "--color-button-container-primary",
    "button-primary-hover": "--color-button-container-primary-hover",
    "button-primary-active": "--color-button-container-primary-active",
    "button-primary-label": "--color-button-label-primary",
    "button-primary-disabled": "--color-button-container-primary-disabled",
    "button-secondary-emphasis-border": "--color-button-container-secondary-emphasis-border",
    "button-secondary-emphasis-hover": "--color-button-container-secondary-emphasis-hover",
}

light_color = {}
for key, var in ROLES.items():
    if var not in DECL:
        continue
    light_color[key] = color(f"light.color.{key}", var)

# Semantic roles the catalog swatches and the style guide read.
background = {
    "page": color("light.background.page", "--color-background-container"),
    "canvas": color("light.background.canvas", "--color-background-canvas"),
    "surface": color("light.background.surface", "--color-background-container"),
}
text = {
    "primary": color("light.text.primary", "--color-text"),
    "secondary": color("light.text.secondary", "--color-text-low-emphasis"),
    "link": color("light.text.link", "--color-link"),
    "on-accent": color("light.text.on-accent", "--color-button-label-primary"),
}
border = {
    "default": color("light.border.default", "--color-border-faint"),
    "strong": color("light.border.strong", "--color-border"),
}
action = {
    "accent": color("light.action.accent", "--color-brand"),
    "accent-hover": color("light.action.accent-hover", "--color-button-container-primary-hover"),
}

# Geometry read from raw/components-computed.json. Every dimension below names
# the component and property it was read from; a missing reading stops the build.
COMPS = json.loads((RAW / "components-computed.json").read_text())["components"]
HAND = "Reconstruction: entered by hand at capture time; no raw reading holds this value"


def page_of(key):
    """The page a component was read on, without its search query."""
    return COMPS[key]["url"].split("?")[0]


def viewport_of(key):
    """The capture width a component was read at: the Mobile group ran at 390 x 844."""
    return "390x844" if COMPS[key].get("group", "").startswith("Mobile") else "1440x900"


def reading(key, prop, state="default"):
    st = (COMPS.get(key) or {}).get("states", {}).get(state) or {}
    value = (st.get("style") or {}).get(prop)
    if st.get("error") or value in (None, ""):
        raise SystemExit(f"no reading of {prop} on {key}/{state}")
    return value, f"measured {prop} on {key}/{state} ({page_of(key)}), {viewport_of(key)}, 2026-11-18"


def mdim(path, key, prop, note=""):
    value, source = reading(key, prop)
    return dim(path, value, source + (note and "; " + note))


def mweight(key):
    value, source = reading(key, "fontWeight")
    return {"$value": int(value), "$type": "fontWeight", "$extensions": {"source": source}}


def mratio(key):
    """line-height as a multiple of font-size, worked out from one measured element."""
    lh, _ = reading(key, "lineHeight")
    fs, _ = reading(key, "fontSize")
    ratio = round(float(lh[:-2]) / float(fs[:-2]), 3)
    return {"$value": ratio, "$type": "number", "$extensions": {"source": f"Derived: computed lineHeight {lh} / fontSize {fs} on {key}/default ({page_of(key)})"}}


def icon_width(key):
    icon = COMPS[key]["states"]["default"].get("icon") or {}
    if not isinstance(icon.get("w"), (int, float)):
        raise SystemExit(f"no icon reading on {key}")
    return dim("core.size.icon-nav", f"{icon['w']:g}px", f"measured icon box on {key}/default ({page_of(key)}): {icon['w']:g} x {icon['h']:g} painted")


core = {
    "font": {
        "family": {
            "sans": font_family(
                "--artdeco-reset-typography-font-family-sans",
                "computed font-family on body: -apple-system, system-ui, BlinkMacSystemFont, Segoe UI, Roboto",
            ),
        },
    },
    "fontSize": {
        "xs": mdim("core.fontSize.xs", "footer-link", "fontSize"),
        "sm": mdim("core.fontSize.sm", "filter-chip", "fontSize"),
        "md": mdim("core.fontSize.md", "apply-cta", "fontSize"),
        "lg": dim("core.fontSize.lg", "20px", HAND + "; the .text-lg step below the papabear breakpoint, which no capture measured"),
        "xl": mdim("core.fontSize.xl", "company-h1", "fontSize", "text-lg papabear:text-xl at 1440"),
        "display-sm": mdim("core.fontSize.display-sm", "profile-h1", "fontSize"),
        "display-md": mdim("core.fontSize.display-md", "section-heading", "fontSize"),
        "display-lg": mdim("core.fontSize.display-lg", "hero-h1", "fontSize"),
        "display-xl": mdim("core.fontSize.display-xl", "legal-h1", "fontSize", "banner__headline t-64"),
    },
    "fontWeight": {
        "regular": mweight("hero-h1"),
        "bold": mweight("company-h1"),
    },
    "lineHeight": {
        "regular": mratio("hero-h1"),
        "open": mratio("company-h1"),
    },
    "radius": {
        "sm": mdim("core.radius.sm", "signin-email", "borderTopLeftRadius"),
        "md": dim("core.radius.md", "8px", HAND + "; .rounded-md, which no measured element paints"),
        "pill": mdim("core.radius.pill", "nav-join", "borderTopLeftRadius"),
        "full": dim("core.radius.full", "9999px", HAND + "; .rounded-full, which no measured element paints"),
    },
    "spacing": {
        "1": dim("core.spacing.1", "4px", HAND + "; the 4px unit of the guest utility scale"),
        "2": mdim("core.spacing.2", "hero-email", "paddingTop"),
        "3": mdim("core.spacing.3", "apply-cta", "paddingTop", ".btn-md vertical padding"),
        "4": mdim("core.spacing.4", "filter-chip", "paddingLeft"),
        "6": mdim("core.spacing.6", "apply-cta", "paddingLeft", ".btn-md horizontal padding"),
    },
    "size": {
        "control-md": mdim("core.size.control-md", "nav-join", "height"),
        "nav": mdim("core.size.nav", "header-nav", "height"),
        "icon-nav": icon_width("nav-link"),
    },
}

light = {
    "color": light_color,
    "background": background,
    "text": text,
    "border": border,
    "action": action,
    "component": {
        "button-primary-background": color("light.component.button-primary-background", "--color-button-container-primary"),
        "button-primary-text": color("light.component.button-primary-text", "--color-button-label-primary"),
        "button-primary-radius": mdim("light.component.button-primary-radius", "nav-join", "borderTopLeftRadius"),
        "button-primary-height": mdim("light.component.button-primary-height", "nav-join", "height"),
    },
}

tokens = {
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only painted guest theme: a white canvas, rgba(0,0,0,0.9) text, #0a66c2 brand pills, a system-ui sans stack. There is no guest dark theme.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
print("resolved names used", sum(1 for v in ROLES.values() if v in DECL), "of", len(ROLES))
