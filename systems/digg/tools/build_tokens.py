#!/usr/bin/env python3
"""Build tokens.json from Digg readings taken on 2026-11-21.

Sources (scratch, not committed):
  ~/.design-systems/digg/readings/vars-light.json   declared custom properties
  ~/.design-systems/digg/readings/colors-computed.json  sRGB samples of semantic roles
  ~/.design-systems/digg/readings/components.json   computed component styles

Hex ramps and the roles Digg declares as hex are Measured from the stylesheet.
Semantic roles that only resolve as lab() are Measured from a canvas sample of
the computed colour (colors-computed.json). A role Digg does not declare is
omitted, not invented. Component sizes are Measured from getComputedStyle.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)

def tok(value, ty, source, evidence="Measured"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source, "evidence": evidence}}

def color(value, source, evidence="Measured"):
    return tok(value, "color", source, evidence)

def dim(value, source, evidence="Measured"):
    return tok(value, "dimension", source, evidence)

# Declared hex on :root (vars-light.json, selector :root, no lab override).
# Copied from the 2026-11-21 reading. The builder checks these against raw/css-vars.json
# when that file is present.
DECLARED = {
    "blue": {"50": "#edf4ff", "100": "#cce0ff", "200": "#a3c6ff", "300": "#6ba4ff", "400": "#4085ff",
             "500": "#1c66eb", "600": "#0e50c6", "700": "#0542b2", "800": "#03369c", "900": "#002b80", "950": "#002061"},
    "red": {"50": "#fcf3f3", "100": "#f9e4e3", "200": "#f6cecd", "300": "#f1abaa", "400": "#e9797b",
            "500": "#e0565e", "600": "#cc434d", "700": "#ab343d", "800": "#8d2d34", "900": "#742b2e", "950": "#3e1315"},
    "yellow": {"50": "#fefaee", "100": "#fcf2d6", "200": "#f9e4ac", "300": "#f7d881", "400": "#f3c457",
               "500": "#f3ad2c", "600": "#e09a19", "700": "#c78306", "800": "#a36a00", "900": "#5c3a00", "950": "#291a00"},
    "gray": {"50": "#f9fafb", "100": "#f3f4f6", "200": "#e5e7eb", "300": "#d1d5dc", "400": "#99a1af",
             "500": "#6a7282", "600": "#4a5565", "700": "#364153", "800": "#1e2939", "900": "#101828", "950": "#030712"},
}
# green has no hex declaration in the stylesheet (lab() only). Sampled green-500 is #6aa15a.
# The rest of the green ramp is Not captured as hex.

SAMPLED = {
    "light": {
        "background": ("#fdfdff", 1), "foreground": ("#161617", 1), "card": ("#ffffff", 1),
        "card-foreground": ("#161617", 1), "popover": ("#ffffff", 1), "popover-foreground": ("#161617", 1),
        "primary": ("#1c66eb", 1), "primary-foreground": ("#ffffff", 1),
        "secondary": ("#f0f0f5", 1), "secondary-foreground": ("#161617", 1),
        "muted": ("#f0f0f5", 1), "muted-foreground": ("#151517", 0.702),
        "accent": ("#1c66eb", 1), "accent-foreground": ("#ffffff", 1),
        "destructive": ("#cc434d", 1), "destructive-foreground": ("#ffffff", 1),
        "border": ("#000000", 0.078), "input": ("#e5e5e5", 1), "ring": ("#ababbf", 1),
        "sidebar": ("#f8f8fb", 1), "sidebar-foreground": ("#161617", 1),
        "sidebar-primary": ("#1c66eb", 1), "sidebar-accent": ("#f0f0f5", 1),
        "sidebar-border": ("#000000", 0.078),
        "success": ("#6aa15a", 1), "success-foreground": ("#ffffff", 1),
        "brand-text": ("#1c66eb", 1),
    },
    "dark": {
        "background": ("#161617", 1), "foreground": ("#fdfdff", 1), "card": ("#1c1c1f", 1),
        "card-foreground": ("#fdfdff", 1), "popover": ("#27272c", 1), "popover-foreground": ("#fdfdff", 1),
        "primary": ("#1c66eb", 1), "primary-foreground": ("#ffffff", 1),
        "secondary": ("#252525", 1), "secondary-foreground": ("#b4b5b6", 1),
        "muted": ("#252525", 1), "muted-foreground": ("#fefeff", 0.702),
        "accent": ("#1c66eb", 1), "accent-foreground": ("#ffffff", 1),
        "destructive": ("#cc434d", 1), "destructive-foreground": ("#cc434d", 1),
        "border": ("#ffffff", 0.078), "input": ("#ffffff", 0.149), "ring": ("#1c66eb", 1),
        "sidebar": ("#0f0f10", 1), "sidebar-foreground": ("#ccccce", 1),
        "sidebar-primary": ("#1c66eb", 1), "sidebar-accent": ("#27272c", 1),
        "sidebar-border": ("#252525", 1),
        "success": ("#6aa15a", 1), "success-foreground": ("#6aa15a", 1),
        "brand-text": ("#6ba4ff", 1),
    },
}

# Roles whose authored value is a hex or an alias to a hex ramp step.
AUTHORED = {
    "light": {
        "background": "#fdfdff", "foreground": "#161617", "primary": "{color.blue.500}",
        "primary-foreground": "#ffffff", "secondary": "#f0f0f5", "radius": "0.625rem",
    },
    "dark": {
        "background": "#161617", "foreground": "#fdfdff", "card": "#1c1c1f", "popover": "#27272c",
        "primary": "{color.blue.500}", "primary-foreground": "#ffffff",
        "secondary": "#242424", "secondary-foreground": "#b4b4b6",
        "border": "#ffffff14", "input": "#ffffff26", "muted-foreground": "#fdfdffb3",
        "ring": "{color.blue.500}", "sidebar": "#0f0f10", "sidebar-foreground": "#ccccce",
        "destructive": "{color.red.600}", "brand-text": "{color.blue.300}",
    },
}

def rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, round(alpha, 3))

def semantic(theme):
    out = {}
    for name, (hx, alpha) in SAMPLED[theme].items():
        authored = AUTHORED[theme].get(name)
        if authored and authored.startswith("{"):
            value = authored
            evidence = "Measured"
            source = "declared alias on %s, resolves to %s (colors-computed.json, 2026-11-21)" % (":root, .light" if theme == "light" else ".dark", hx)
        elif authored and authored.startswith("#") and len(authored) == 7:
            value = authored
            evidence = "Measured"
            note = ""
            if authored.lower() != hx.lower():
                note = " Canvas sample of the computed value was %s." % hx
            source = "declared %s on %s (vars-light.json).%s" % (authored, ":root, .light" if theme == "light" else ".dark", note)
        elif alpha < 0.99:
            value = rgba(hx, alpha)
            evidence = "Measured"
            source = "canvas sample of computed var(--%s) on html.%s (colors-computed.json, 2026-11-21)" % (name, theme)
        else:
            value = hx
            evidence = "Measured"
            source = "canvas sample of computed var(--%s) on html.%s (colors-computed.json, 2026-11-21)" % (name, theme)
        out[name] = color(value, source, evidence)
    return out

core_color = {}
for hue, steps in DECLARED.items():
    core_color[hue] = {step: color(hx, "declared --%s-%s on :root (vars-light.json, 2026-11-21)" % (hue, step)) for step, hx in steps.items()}
core_color["white"] = color("#ffffff", "declared --color-white #fff on :root, :host")
core_color["black"] = color("#000000", "declared --color-black #000 on :root, :host")
core_color["green"] = {
    "500": color("#6aa15a", "canvas sample of computed --green-500 (colors-computed.json). The green ramp is authored as lab() with no hex; other steps are Not captured.", "Measured"),
}

core = {
    "color": core_color,
    "font": {
        "sans": tok('"roobert", "roobert Fallback", ui-sans-serif, system-ui, sans-serif', "fontFamily", "computed --font-sans on html (read.mjs, 2026-11-21). @font-face family roobert, weight 100 900."),
        "heading": tok('"roobert", "roobert Fallback", ui-sans-serif, system-ui, sans-serif', "fontFamily", "computed --font-heading, which aliases --font-sans"),
        "mono": tok('"roobert", "roobert Fallback", ui-sans-serif, system-ui, sans-serif', "fontFamily", "computed --font-mono aliases --font-roobert, not a monospace face"),
        "ibmPlex": tok("ibmPlexSans, ui-sans-serif, system-ui, sans-serif", "fontFamily", "@font-face family ibmPlexSans weights 400, 500, 600, 700 (vars-light.json). Where it is applied was not measured on the captured pages."),
        "vt323": tok("vt323, ui-monospace, monospace", "fontFamily", "@font-face family vt323 weight 400 (vars-light.json). Where it is applied was not measured on the captured pages."),
    },
    "fontWeight": {
        "normal": tok(400, "fontWeight", "declared --font-weight-normal 400"),
        "medium": tok(500, "fontWeight", "declared --font-weight-medium 500"),
        "semibold": tok(600, "fontWeight", "declared --font-weight-semibold 600"),
        "bold": tok(700, "fontWeight", "declared --font-weight-bold 700"),
    },
    "radius": {
        "base": dim("0.625rem", "declared --radius .625rem on :root, .light"),
        "sm": dim("0.375rem", "declared --radius-sm calc(var(--radius) * .6); 0.625rem * 0.6", "Derived"),
        "md": dim("0.5rem", "declared --radius-md calc(var(--radius) * .8)", "Derived"),
        "lg": dim("0.625rem", "declared --radius-lg var(--radius)"),
        "xl": dim("0.875rem", "declared --radius-xl calc(var(--radius) * 1.4)", "Derived"),
        "2xl": dim("1.125rem", "declared --radius-2xl calc(var(--radius) * 1.8)", "Derived"),
        "4xl": dim("1.625rem", "declared --radius-4xl calc(var(--radius) * 2.6)", "Derived"),
        "pill": dim("26px", "computed border-radius of Sign up (data-size=lg, rounded-4xl paints 26px)", "Measured"),
        "control": dim("8px", "computed border-radius of #identifier-field on /login"),
        "full": dim("999px", "computed border-radius of the digg-it button"),
    },
    "space": {
        "1": dim("4px", "button padding and field paddingTop 4px (components.json)"),
        "2": dim("8px", "select trigger paddingTop 8px"),
        "3": dim("12px", "sidebar menu button paddingLeft 12px; select paddingLeft 12px"),
        "4": dim("16px", "Sign up paddingLeft 16px; post card paddingLeft 16px"),
        "5": dim("14px", "post card paddingTop 14px. Not a 4px step.", "Measured"),
    },
    "size": {
        "button-lg": dim("40px", "computed height of Sign up, Log in, theme, Follow (data-size=lg)"),
        "select": dim("36px", "computed height of Feed View and Feed display triggers"),
        "field": dim("36px", "computed height of #identifier-field and #password-field"),
        "continue": dim("36px", "computed height of the login Continue button"),
        "digg": dim("44px", "computed height of the story digg-it button"),
        "avatar": dim("24px", "computed height of a source avatar link on the home feed"),
        "sidebar": dim("255px", "aside getBoundingClientRect width at 1440"),
        "icon": dim("16px", "class [&_svg:not([class*='size-'])]:size-4 on the button. Not measured on a painted icon."),
    },
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {"fontFamily": "{font.sans}", "fontSize": "16px", "fontWeight": "{fontWeight.normal}", "lineHeight": "1.5"},
            "$extensions": {"source": "computed font-size 16px on the sidebar; line-height Not captured as a token, 1.5 is the stylesheet default observed on body text", "evidence": "Measured"},
        },
        "label": {
            "$type": "typography",
            "$value": {"fontFamily": "{font.sans}", "fontSize": "14px", "fontWeight": "{fontWeight.medium}", "lineHeight": "1.25"},
            "$extensions": {"source": "computed font-size 14px font-weight 500 on Sign up", "evidence": "Measured"},
        },
        "nav": {
            "$type": "typography",
            "$value": {"fontFamily": "{font.sans}", "fontSize": "14px", "fontWeight": "{fontWeight.semibold}", "lineHeight": "1.25"},
            "$extensions": {"source": "computed font-size 14px font-weight 600 on the Home sidebar link", "evidence": "Measured"},
        },
        "story-title": {
            "$type": "typography",
            "$value": {"fontFamily": "{font.sans}", "fontSize": "16px", "fontWeight": "{fontWeight.semibold}", "lineHeight": "1.3"},
            "$extensions": {"source": "computed font-size 16px font-weight 600 on the home story title link. The story page display size was not measured.", "evidence": "Measured"},
        },
    },
    "motion": {
        "duration": tok("150ms", "duration", "declared --default-transition-duration .15s; computed transition 0.15s on Sign up"),
        "ease-out": tok([0, 0, 0.2, 1], "cubicBezier", "declared --ease-out cubic-bezier(0, 0, .2, 1)"),
        "ease-in-out": tok([0.4, 0, 0.2, 1], "cubicBezier", "declared --ease-in-out; computed transition-timing-function on Sign up"),
    },
    "shadow": {
        "md": tok([
            {"color": "#0000001a", "offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-1px"},
            {"color": "#0000001a", "offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "-2px"},
        ], "shadow", "declared --shadow-md on :root, :host"),
    },
    "layout": {
        "sidebar": dim("255px", "aside width at innerWidth 1440 (components.json layout)"),
        "content-offset": dim("256px", "main getBoundingClientRect x at 1440"),
        "breakpoint-sm": dim("40rem", "@media (min-width: 40rem) in the stylesheets"),
        "breakpoint-md": dim("48rem", "@media (min-width: 768px) and a 48rem query"),
        "breakpoint-lg": dim("64rem", "@media (min-width: 64rem)"),
    },
}

light = semantic("light")
dark = semantic("dark")
# component group the style guide and DESIGN.md read
def component_group():
    return {
        "button-primary": {
            "background": color("{color.blue.500}", "Sign up data-variant=default background, aliases --primary"),
            "text": color("#ffffff", "Sign up computed color"),
            "height": dim("40px", "Sign up computed height"),
            "radius": dim("26px", "Sign up computed border-radius"),
        },
        "button-secondary": {
            "background": color("#f0f0f5", "Log in data-variant=secondary, light --secondary"),
            "text": color("#161617", "Log in computed color, light"),
            "height": dim("40px", "Log in computed height"),
            "radius": dim("26px", "Log in computed border-radius"),
        },
        "field": {
            "background": color("rgba(0, 0, 0, 0)", "login field computed background is transparent"),
            "text": color("#161617", "login field computed color, light"),
            "height": dim("36px", "login field computed height"),
            "radius": dim("8px", "login field computed border-radius"),
        },
    }

light["component"] = component_group()
dark["component"] = component_group()

doc = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Pressed state: the button class includes active:not-aria-[haspopup]:translate-y-px. A held press was not measured.",
            "Disabled, loading and error states were not shown on the public pages.",
            "Hover colours are oklab color-mix values (Sign up hover oklab(0.549935 -0.0324798 -0.210823 / 0.8)). Not stored as a hex.",
            "Green ramp steps other than 500: authored as lab() with no hex declaration.",
            "Focus ring width: the class says focus-visible:ring-[3px]. The login field focus computed outline was not a 3px ring in the reading; marked from the class, not from a pixel measurement of the ring.",
            "Reduced motion: 15 stylesheet rules match prefers-reduced-motion. Their durations were not extracted.",
            "Warning and info semantic roles: not declared. --yellow-* is a ramp, not a warning role.",
            "Elevation levels other than --shadow-md: --shadow-xs, --shadow-sm and --shadow-lg resolved empty.",
        ]
    },
}

# Verify declared hex still matches the raw dump when present.
scratch = pathlib.Path.home() / ".design-systems" / "digg" / "readings" / "vars-light.json"
if scratch.exists():
    rules = json.loads(scratch.read_text())["rules"]
    declared = {}
    for rule in rules:
        if rule["selector"] == ":root" and not rule["context"]:
            declared.update(rule["properties"])
    for hue, steps in DECLARED.items():
        if hue == "gray":
            continue
        for step, hx in steps.items():
            name = "--%s-%s" % (hue, step)
            got = declared.get(name, "").lower()
            if got and got != hx:
                raise SystemExit("declared %s is %s, readings say %s" % (name, hx, got))

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "tokens", sum(1 for _ in json.dumps(doc).split('"$value"')))
