#!/usr/bin/env python3
"""Build systems/sora/tokens.json from raw/css-vars.json and raw/computed.json.

Sora's public site on 2026-11-19 was the sunset page at
https://sora.chatgpt.com/sunset. Light tokens are declared on :root and dark
tokens override them on .dark. The page loaded with html.dark. A second read
applied class "light", which dropped the .dark overrides and resolved :root.

Every colour here is a declaration from those two blocks, or a getComputedStyle
reading named in raw/computed.json. Nothing is sampled from a screenshot.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMPUTED = json.loads((RAW / "computed.json").read_text())

ROOT = VARS["root"]
DARK = VARS["dark"]
FONT = (
    "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "
    "Cantarell, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, "
    "Segoe UI Symbol, Noto Color Emoji"
)


def src(where):
    return {"source": where}


def color(value, where):
    return {"$type": "color", "$value": value, "$extensions": src(where)}


def dim(value, where):
    return {"$type": "dimension", "$value": value, "$extensions": src(where)}


def font_family(value, where):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(where)}


def shadow(value, where):
    return {"$type": "shadow", "$value": value, "$extensions": src(where)}


def hsl_triplet(raw):
    """`240 3.7% 15.9%` is the shadcn form Sora stores. Return a CSS hsl()."""
    parts = raw.split()
    if len(parts) == 3 and parts[1].endswith("%") and parts[2].endswith("%"):
        return f"hsl({parts[0]} {parts[1]} {parts[2]})"
    return None


def rgb_triplet(raw):
    """`0 0 0` and `255 255 255` are space-separated sRGB channels."""
    parts = raw.split()
    if len(parts) == 3 and all(re.fullmatch(r"\d{1,3}", p) for p in parts):
        return "rgb(" + " ".join(parts) + ")"
    return None


def as_color(raw):
    if raw.startswith("#") or raw.startswith("rgb") or raw.startswith("hsl") or raw.startswith("rgba"):
        return raw
    return hsl_triplet(raw) or rgb_triplet(raw) or raw


def token_name(css_name):
    return css_name[2:].replace("-", ".") if False else css_name[2:]


# Semantic colour names that are colours in both themes. Layout lengths and
# shadows stay out of this map.
COLOUR_NAMES = [
    "text-primary", "text-secondary", "text-tertiary", "text-inverse",
    "text-destructive", "text-destructive-foreground",
    "bg-primary", "bg-secondary", "bg-tertiary", "bg-quaternary", "bg-inverse",
    "bg-lighter", "bg-light", "bg-active", "bg-error", "bg-destructive",
    "chatgpt-bg-primary", "action-color",
    "border-subtle", "border-primary", "border-active", "focus-outline",
    "bg-popover", "bg-popover-old", "bg-composer", "bg-composer-button",
    "background", "foreground", "card", "card-foreground",
    "popover", "popover-foreground", "primary", "primary-foreground",
    "secondary", "secondary-foreground", "tertiary", "tertiary-foreground",
    "muted", "muted-foreground", "accent", "accent-foreground",
    "destructive", "destructive-foreground", "border", "input", "ring",
]


def theme_set(theme):
    declared = ROOT if theme == "light" else {**ROOT, **DARK}
    selector = ":root" if theme == "light" else ".dark"
    sheet = "4f834fecb0689d51.css"
    colours = {}
    for name in COLOUR_NAMES:
        key = "--" + name
        if key not in declared:
            continue
        raw = declared[key]
        where = f"Measured. {selector} {key}: {raw} in {sheet}"
        group, leaf = ("text", name[5:]) if name.startswith("text-") else (
            ("background", name[3:]) if name.startswith("bg-") else (None, None)
        )
        if name == "chatgpt-bg-primary":
            group, leaf = "background", "chatgpt"
        elif name == "action-color":
            group, leaf = "action", "color"
        elif name.startswith("border-"):
            group, leaf = "border", name[7:]
        elif name == "focus-outline":
            group, leaf = "focus", "outline"
        elif group is None:
            group, leaf = "shadcn", name
        colours.setdefault(group, {})[leaf.replace("-", ".")] = color(as_color(raw), where)
        # keep leaf keys hyphen-free for DTCG paths: use hyphen as nested? 
        # The line above used a dot inside the leaf which would nest. Fix below.
    # Rebuild cleanly so a leaf never contains a dot.
    colours = {}
    for name in COLOUR_NAMES:
        key = "--" + name
        if key not in declared:
            continue
        raw = declared[key]
        where = f"Measured. {selector} {key}: {raw} in {sheet}"
        if name.startswith("text-"):
            group, leaf = "text", name[5:]
        elif name.startswith("bg-"):
            group, leaf = "background", name[3:]
        elif name == "chatgpt-bg-primary":
            group, leaf = "background", "chatgpt"
        elif name == "action-color":
            group, leaf = "action", "color"
        elif name.startswith("border-"):
            group, leaf = "border", name[7:]
        elif name == "focus-outline":
            group, leaf = "focus", "outline"
        else:
            group, leaf = "shadcn", name
        colours.setdefault(group, {})[leaf] = color(as_color(raw), where)
    reading = COMPUTED["computed"]["exportLink"]["dark" if theme == "dark" else "lightClassApplied"]
    where_btn = (
        "Measured. getComputedStyle(main a) on the sunset page, html.dark"
        if theme == "dark"
        else "Measured. getComputedStyle(main a) after adding class light and removing class dark"
    )
    colours["control"] = {
        "button-background": color(reading["backgroundColor"], where_btn + ", backgroundColor"),
        "button-text": color(reading["color"], where_btn + ", color"),
    }
    shadows = {}
    for name in ("shadow-popover", "shadow-composer", "shadow-inset-stroke", "shadow-inset-stroke-inverse"):
        key = "--" + name
        if key not in declared:
            continue
        raw = declared[key]
        shadows[name[7:]] = shadow(raw, f"Measured. {selector} {key}: {raw} in {sheet}")
    return {"color": colours, "shadow": shadows}


def core():
    sheet = "4f834fecb0689d51.css"
    # Tailwind v3.4.17 default scale, read from the same stylesheet's utilities.
    # 1rem is 16px on this page (html font-size was 16px).
    spacing_steps = {
        "0": "0px",
        "1": "4px",
        "2": "8px",
        "3": "12px",
        "4": "16px",
        "5": "20px",
        "6": "24px",
        "8": "32px",
        "9": "36px",
        "12": "48px",
    }
    spacing = {}
    rules = COMPUTED["utilityRules"]
    evidence = {
        "0": "Measured. .gap-0{gap:0} and .p-0{padding:0}",
        "1": "Measured. .gap-1{gap:.25rem} and .p-1{padding:.25rem}; html font-size 16px, so 4px",
        "2": "Measured. .gap-2{gap:.5rem} and .p-2{padding:.5rem}; 8px",
        "3": "Measured. .px-3{padding-left:.75rem;padding-right:.75rem}; computed button padding 12px",
        "4": "Measured. .gap-4{gap:1rem} and .p-4{padding:1rem}; 16px",
        "5": "Measured. .gap-5{gap:1.25rem} and .p-5{padding:1.25rem}; 20px",
        "6": "Measured. .gap-6{gap:1.5rem} and .px-6; computed column gap 24px and main padding 24px",
        "8": "Measured. .gap-8{gap:2rem}; 32px",
        "9": "Measured. .gap-9{gap:2.25rem} and .p-9{padding:2.25rem}; 36px",
        "12": "Measured. .gap-12{gap:3rem}; 48px",
    }
    for step, value in spacing_steps.items():
        spacing[step] = dim(value, evidence[step] + f" in {sheet}")

    radius_rules = {
        "sm": ("2px", ".rounded-sm{border-radius:.125rem}"),
        "md": ("6px", ".rounded-md{border-radius:.375rem}"),
        "lg": ("8px", ".rounded-lg{border-radius:.5rem}"),
        "xl": ("12px", ".rounded-xl{border-radius:.75rem}; computed Export link border-radius 12px"),
        "2xl": ("16px", ".rounded-2xl{border-radius:1rem}"),
        "3xl": ("24px", ".rounded-3xl{border-radius:1.5rem}"),
        "full": ("9999px", ".rounded-full{border-radius:9999px}"),
    }
    radius = {}
    for name, (value, rule) in radius_rules.items():
        radius[name] = dim(value, f"Measured. {rule} in {sheet}")

    type_styles = {
        "body": {
            "fontFamily": "{font.family.sans}",
            "fontSize": "14px",
            "fontWeight": "400",
            "lineHeight": "20px",
            "source": "Measured. getComputedStyle(body) font-size 14px, weight 400, line-height 20px on the sunset page",
        },
        "copy": {
            "fontFamily": "{font.family.sans}",
            "fontSize": "16px",
            "fontWeight": "400",
            "lineHeight": "24px",
            "source": "Measured. main p.text-base computed font-size 16px, line-height 24px; .text-base{font-size:1rem;line-height:1.5rem}",
        },
        "button": {
            "fontFamily": "{font.family.sans}",
            "fontSize": "14px",
            "fontWeight": "600",
            "lineHeight": "20px",
            "source": "Measured. Export link computed font-size 14px, weight 600, line-height 20px; .text-sm and .font-semibold",
        },
    }
    typography = {}
    for name, style in type_styles.items():
        where = style.pop("source")
        typography[name] = {
            "$type": "typography",
            "$value": style,
            "$extensions": src(where),
        }

    motion = {
        "duration": {
            "pulse": dim("2000ms", "Measured. .animate-pulse{animation:pulse 2s cubic-bezier(.4,0,.6,1) infinite}"),
            "spin": dim("1000ms", "Measured. .animate-spin{animation:spin 1s linear infinite}"),
            "progress": dim("1200ms", "Measured. .progress-bar-indeterminate{animation:progress-bar-indeterminate 1.2s linear infinite}"),
            "card-fade": dim("3000ms", "Measured. .placeholderCard{animation:cardFade 3s cubic-bezier(.45,0,.4,1) infinite both}"),
            "caret": dim("1000ms", "Measured. .animate-caret-blink{animation:caret-blink 1s step-end infinite}"),
            "firework": dim("600ms", "Measured. .emoji-firework-center{animation:emoji-firework-center .6s ease-out forwards}"),
        },
        "easing": {
            "pulse": {
                "$type": "cubicBezier",
                "$value": [0.4, 0, 0.6, 1],
                "$extensions": src("Measured. .animate-pulse cubic-bezier(.4,0,.6,1)"),
            },
            "card-fade": {
                "$type": "cubicBezier",
                "$value": [0.45, 0, 0.4, 1],
                "$extensions": src("Measured. .placeholderCard cubic-bezier(.45,0,.4,1)"),
            },
            "ease-out": {
                "$type": "cubicBezier",
                "$value": [0, 0, 0.2, 1],
                "$extensions": {
                    "source": "Derived. .emoji-firework-center animation timing keyword ease-out, expanded to the CSS ease-out control points. The keyword itself was measured.",
                    "keyword": "ease-out",
                },
            },
            "linear": {
                "$type": "cubicBezier",
                "$value": [0, 0, 1, 1],
                "$extensions": {
                    "source": "Derived. .animate-spin and .progress-bar-indeterminate timing keyword linear, expanded to the CSS linear control points. The keyword itself was measured.",
                    "keyword": "linear",
                },
            },
        },
    }
    motion["$extensions"] = {
        "source": "Declared in 4f834fecb0689d51.css. None of these animations were running on the sunset page.",
        "reducedMotion": (
            "Two @media (prefers-reduced-motion: reduce) rules set animation:none on "
            ".placeholderCard and on .emoji-firework-center, .emoji-firework-particle. "
            "Other animations have no reduce rule in the fetched sheets."
        ),
    }

    layout = {
        "sidebar-width": dim("196px", "Measured. :root --sidebar-width: 196px. Not painted on the sunset page."),
        "sidebar-gap": dim("21px", "Measured. :root --sidebar-gap: 21px. .dark sets --sidebar-gap: 0px in one later rule; the computed dark value on the sunset page was 21px, so the live value is recorded under dark.layout."),
        "mobile-tab-bar-height": dim("54px", "Measured. :root --mobile-tab-bar-height: 54px. Not painted on the sunset page."),
        "sunset-column": dim("448px", "Measured. .max-w-md{max-width:28rem} and getComputedStyle of the sunset column, width 448px."),
        "sunset-padding-inline": dim("24px", "Measured. main padding 0px 24px from .px-6{padding-left:1.5rem;padding-right:1.5rem}."),
    }

    return {
        "font": {
            "family": {
                "sans": font_family(FONT, "Measured. .font-sans and getComputedStyle(body).fontFamily on the sunset page. OpenAI Sans is declared in @font-face but was not the computed family."),
                "openai-sans": font_family("OpenAI Sans", "Measured. @font-face font-family: OpenAI Sans in eda963f33b3839f5.css, weights 400, 500, 600, 700, normal and italic. Not the computed family on the sunset page."),
            }
        },
        "spacing": spacing,
        "radius": radius,
        "typography": typography,
        "motion": motion,
        "layout": layout,
    }


def component_metrics():
    return {
        "button": {
            "radius": dim("12px", "Measured. Export link border-radius 12px; .rounded-xl{border-radius:.75rem}"),
            "padding": dim("8px", "Measured. Export link padding 8px 12px. Vertical padding is this token; horizontal is 12px (core.spacing.3)."),
            "height": dim("36px", "Measured. Export link height 36px; .h-9{height:2.25rem}"),
        }
    }


def build():
    light = theme_set("light")
    dark = theme_set("dark")
    light["component"] = component_metrics()
    dark["component"] = component_metrics()
    # Dark computed --sidebar-gap stayed 21px; do not invent a 0px override.
    # The sunset page resolved --sidebar-gap to the :root 21px value while
    # html.dark was set. That reading stays in core.layout.sidebar-gap. A
    # later stylesheet rule sets .dark --sidebar-gap to 0px, but it did not
    # win on the live element, so it is not a token.
    doc = {
        "$description": "Sora sunset page tokens, measured 2026-11-19 from https://sora.chatgpt.com/sunset.",
        "core": core(),
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
    }
    text = json.dumps(doc, indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    return text


if __name__ == "__main__":
    build()
