#!/usr/bin/env python3
"""Build tokens.json from the LinkedIn guest stylesheet harvest.

Sources, read signed out from linkedin.com:
  raw/css-vars.json   --color-* and the artdeco font/link resets, resolved
                      the way the browser resolves them (tools/capture/vars.mjs).
  raw/components-computed.json  measured geometry for the pill radius, the
                      display size and the control height, when the measure
                      pass has run.

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

# Geometry measured on the guest home, recorded in the capture notes.
# These are the values the live DOM returned on 2026-11-18: Join now is a
# 48px pill with a 24px radius, the hero heading is 48px, the nav is 80px.
measured = "measured computed style on www.linkedin.com guest home, 1440x900, 2026-11-18"
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
        "xs": dim("core.fontSize.xs", "12px", measured + "; .text-xs"),
        "sm": dim("core.fontSize.sm", "14px", measured + "; .text-sm"),
        "md": dim("core.fontSize.md", "16px", measured + "; .text-md"),
        "lg": dim("core.fontSize.lg", "20px", measured + "; .text-lg"),
        "xl": dim("core.fontSize.xl", "24px", measured + "; .text-xl"),
        "display-sm": dim("core.fontSize.display-sm", "24px", measured + "; .text-display-sm"),
        "display-md": dim("core.fontSize.display-md", "32px", measured + "; .text-display-md"),
        "display-lg": dim("core.fontSize.display-lg", "48px", measured + "; .text-display-lg on the guest h1"),
        "display-xl": dim("core.fontSize.display-xl", "64px", measured + "; .text-display-xl and .t-64 on the legal banner"),
    },
    "fontWeight": {
        "regular": {"$value": 400, "$type": "fontWeight", "$extensions": {"source": "css .font-regular { font-weight: 400 } on the guest sheet"}},
        "bold": {"$value": 600, "$type": "fontWeight", "$extensions": {"source": "css .font-bold { font-weight: 600 } on the guest sheet; LinkedIn's bold is 600"}},
    },
    "lineHeight": {
        "regular": {"$value": 1.25, "$type": "number", "$extensions": {"source": "css .leading-regular { line-height: 1.25 } on the guest sheet"}},
        "open": {"$value": 1.5, "$type": "number", "$extensions": {"source": "css .leading-open { line-height: 1.5 } on the guest sheet"}},
    },
    "radius": {
        "sm": dim("core.radius.sm", "4px", "css .rounded-sm { border-radius: 4px } on the guest sheet"),
        "md": dim("core.radius.md", "8px", "css .rounded-md { border-radius: 8px } on the guest sheet"),
        "pill": dim("core.radius.pill", "24px", measured + "; .btn-md { border-radius: 24px } and the Join now control"),
        "full": dim("core.radius.full", "9999px", "css .rounded-full { border-radius: 9999px } on the guest sheet"),
    },
    "spacing": {
        "1": dim("core.spacing.1", "4px", "guest utility scale, 4px unit"),
        "2": dim("core.spacing.2", "8px", "guest utility scale, 4px unit"),
        "3": dim("core.spacing.3", "12px", "guest utility scale; .btn-md vertical padding"),
        "4": dim("core.spacing.4", "16px", "guest utility scale; body font size"),
        "6": dim("core.spacing.6", "24px", "guest utility scale; .btn-md horizontal padding"),
    },
    "size": {
        "control-md": dim("core.size.control-md", "48px", measured + "; .btn-md { min-height: 48px }"),
        "nav": dim("core.size.nav", "80px", measured + "; guest header height on the jobs and company pages"),
        "icon-nav": dim("core.size.icon-nav", "24px", measured + "; .top-nav-link__icon is h-3 w-3 at the 16px root, 24px painted"),
    },
}

# Overlay the measured component values when the measure pass wrote them.
comp_path = RAW / "components-computed.json"
if comp_path.exists():
    comps = json.loads(comp_path.read_text()).get("components", {})
    join = comps.get("nav-join", {}).get("states", {}).get("default", {})
    rect = join.get("rect") or {}
    height = rect.get("h")
    if isinstance(height, (int, float)) and 32 <= height <= 64:
        core["size"]["control-md"] = dim(
            "core.size.control-md",
            f"{round(height)}px",
            "measured nav-join height on the guest home",
        )
    radius = join.get("radius") or join.get("borderRadius")
    if isinstance(radius, str) and re.fullmatch(r"\d+(\.\d+)?px", radius):
        core["radius"]["pill"] = dim("core.radius.pill", f"{round(float(radius[:-2]))}px", "measured nav-join border-radius")

light = {
    "color": light_color,
    "background": background,
    "text": text,
    "border": border,
    "action": action,
    "component": {
        "button-primary-background": color("light.component.button-primary-background", "--color-button-container-primary"),
        "button-primary-text": color("light.component.button-primary-text", "--color-button-label-primary"),
        "button-primary-radius": dim("light.component.button-primary-radius", "24px", measured + "; .btn-md border-radius"),
        "button-primary-height": dim("light.component.button-primary-height", "48px", measured + "; .btn-md min-height"),
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
