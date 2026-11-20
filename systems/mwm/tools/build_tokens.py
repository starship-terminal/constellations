#!/usr/bin/env python3
"""Build systems/mwm/tokens.json from raw/css-vars.json and raw/components.json.

The marketing site declares one dark token layer, --mwm-*, on :root. Console's
signed-out page declares a second --mwm-* layer (focus, motion, extra text
steps) and a --cx-* product layer. Create's signed-out page declares its own
--bg-*, --text-* and --accent-* layer. None of the three ships a light theme.

Every colour is the value getComputedStyle resolved on the root, or a computed
style on a named element. A dimension is one px length. Anything else (a
gradient, a transparent keyword, a hatch) is listed under $extensions.notTokenised.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())

SRC = "Measured. getComputedStyle on :root, https://mwm.ai/, 1440x900, 2026-11-19"
SRC_CONSOLE = "Measured. getComputedStyle on :root, https://console.mwm.ai/sign-in, 1440x900, 2026-11-19"
SRC_CREATE = "Measured. getComputedStyle on :root, https://create.mwm.ai/sign-in, 1440x900, 2026-11-19"


def color(c):
    c = c.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            return "rgba(%d, %d, %d, %g)" % (*rgb, round(a, 3))
        return "#%02x%02x%02x" % tuple(rgb)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", c)
    if m:
        rgb = [int(m.group(i)) for i in (1, 2, 3)]
        a = float(m.group(4)) if m.group(4) else 1
        if a >= 1:
            return "#%02x%02x%02x" % tuple(rgb)
        return "rgba(%d, %d, %d, %g)" % (*rgb, round(a, 3))
    m = re.fullmatch(r"hsla\(\s*([\d.]+)\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*,\s*([\d.]+)\s*\)", c)
    if m:
        hue, sat, lig, a = (float(m.group(i)) for i in (1, 2, 3, 4))
        return hsla_hex(hue, sat / 100, lig / 100, a)
    raise ValueError("colour not understood: " + c)


def hsla_hex(h, s, l, a):
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    rgb = [round((v + m) * 255) for v in (r, g, b)]
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %g)" % (*rgb, round(a, 3))


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise ValueError("not a px length: %r" % v)
    return ("%g" % round(float(m.group(1)), 3)) + "px"


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, token):
    node = tree
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = token


def take_color(tree, group, name, raw, source):
    if raw in ("transparent", "none", ""):
        return False
    # A value that does not parse fails the build: dropping it silently would leave the role out
    # of tokens.json with nothing to say a reading was lost.
    put(tree, [group, name], tok(color(raw), "color", source + "; " + name))
    return True


def resolved(block):
    return block["resolved"] if isinstance(block, dict) and "resolved" in block else block

home = resolved(VARS["home"])
console = resolved(VARS["console"])
create = resolved(VARS["create"])

core = {}
put(core, ["font", "family", "ui"], tok(
    "Inter, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", "fontFamily",
    SRC + "; --mwm-font-ui. Inter loaded. Modern Gothic is named by --mwm-font-display and did not load."))
put(core, ["font", "family", "display"], tok(
    "Inter, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", "fontFamily",
    SRC + "; computed font-family on h1 is Inter. --mwm-font-display names Modern Gothic first; that face did not load."))
put(core, ["font", "family", "mono"], tok(
    "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace", "fontFamily",
    SRC + "; --mwm-font-mono with the unloaded Modern Gothic Mono name dropped."))
put(core, ["font", "family", "console"], tok(
    "InterVariable, Inter, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", "fontFamily",
    SRC_CONSOLE + "; --mwm-font-ui on the console sign-in page."))
put(core, ["font", "family", "create"], tok(
    "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif", "fontFamily",
    SRC_CREATE + "; computed font-family on body."))

put(core, ["font", "weight", "regular"], tok("400", "fontWeight", SRC + "; body"))
put(core, ["font", "weight", "medium"], tok("500", "fontWeight", "Measured. .mwm-select-pill computed font-weight, https://mwm.ai/"))
put(core, ["font", "weight", "semibold"], tok("600", "fontWeight", "Measured. .mwm-product-start computed font-weight"))
put(core, ["font", "weight", "bold"], tok("700", "fontWeight", "Measured. .mwm-plan-popular computed font-weight, https://mwm.ai/pricing"))

put(core, ["font", "size", "nav"], tok("13px", "dimension", "Measured. .mwm-product-nav-item computed font-size"))
put(core, ["font", "size", "body"], tok("14px", "dimension", "Measured. body computed font-size, https://mwm.ai/"))
put(core, ["font", "size", "lede"], tok("16px", "dimension", "Measured. .mwm-hero-copy p computed font-size"))
put(core, ["font", "size", "prompt"], tok("16px", "dimension", "Measured. .mwm-prompt textarea computed font-size"))
put(core, ["font", "size", "link"], tok("18px", "dimension", "Measured. .mwm-build-link computed font-size"))
put(core, ["font", "size", "plan-title"], tok("32px", "dimension", "Measured. pricing h2 computed font-size"))
put(core, ["font", "size", "section"], tok("48px", "dimension", "Measured. home h2 computed font-size"))
put(core, ["font", "size", "display"], tok("72px", "dimension", "Measured. home h1 computed font-size"))
put(core, ["font", "size", "price"], tok("28px", "dimension", "Measured. .mwm-plan-price-amount strong computed font-size"))

put(core, ["font", "line-height", "nav"], tok("16px", "dimension", "Measured. .mwm-product-nav-item computed line-height"))
put(core, ["font", "line-height", "body"], tok("21px", "dimension", "Measured. body computed line-height"))
put(core, ["font", "line-height", "lede"], tok("24px", "dimension", "Measured. .mwm-hero-copy p computed line-height"))
put(core, ["font", "line-height", "plan-title"], tok("40px", "dimension", "Measured. pricing h2 computed line-height"))
put(core, ["font", "line-height", "section"], tok("54px", "dimension", "Measured. home h2.lifecycle-title computed line-height"))
put(core, ["font", "line-height", "display"], tok("76px", "dimension", "Measured. home h1 computed line-height"))

put(core, ["font", "letter-spacing", "nav"], tok("-0.26px", "dimension", "Measured. .mwm-product-nav-item computed letter-spacing"))
put(core, ["font", "letter-spacing", "lede"], tok("-0.32px", "dimension", "Measured. .mwm-hero-copy p computed letter-spacing"))
put(core, ["font", "letter-spacing", "section"], tok("-1.92px", "dimension", "Measured. home h2 computed letter-spacing"))
put(core, ["font", "letter-spacing", "display"], tok("-2.88px", "dimension", "Measured. home h1 computed letter-spacing"))

put(core, ["radius", "button"], tok("8px", "dimension", SRC + "; --mwm-radius-btn"))
put(core, ["radius", "card"], tok("16px", "dimension", SRC + "; --mwm-radius-card"))
put(core, ["radius", "panel"], tok("24px", "dimension", SRC + "; --mwm-radius-panel"))
put(core, ["radius", "frame"], tok("20px", "dimension", "Measured. .mwm-build-frame computed border-radius"))
put(core, ["radius", "field"], tok("6px", "dimension", "Measured. console email input computed border-radius"))
put(core, ["radius", "pill"], tok("999px", "dimension", "Measured. .mwm-plan-popular computed border-radius"))
put(core, ["radius", "sm"], tok("4px", "dimension", SRC_CONSOLE + "; --mwm-radius-sm"))
put(core, ["radius", "lg"], tok("12px", "dimension", SRC_CONSOLE + "; --mwm-radius-lg"))

put(core, ["space", "4"], tok("4px", "dimension", "Derived. 4px step used by the prompt chip gap; the site has no spacing custom properties"))
put(core, ["space", "8"], tok("8px", "dimension", "Derived. prompt chip padding uses 8px"))
put(core, ["space", "12"], tok("12px", "dimension", "Measured. .mwm-product-nav-item padding-inline"))
put(core, ["space", "14"], tok("14px", "dimension", "Measured. .mwm-product-start padding-inline"))
put(core, ["space", "16"], tok("16px", "dimension", "Measured. .mwm-product-login padding-inline end"))
put(core, ["space", "24"], tok("24px", "dimension", SRC_CONSOLE + "; --cx-gutter"))
put(core, ["space", "32"], tok("32px", "dimension", "Measured. .mwm-plan-card padding-inline"))
put(core, ["space", "40"], tok("40px", "dimension", "Measured. .mwm-plan-card padding-top"))
put(core, ["space", "72"], tok("72px", "dimension", "Measured. .mwm-product-topbar height"))

put(core, ["size", "nav-item"], tok("32px", "dimension", "Measured. .mwm-product-nav-item height"))
put(core, ["size", "plan-cta"], tok("44px", "dimension", "Measured. Get MWM AI Pro link height"))
put(core, ["size", "prompt-control"], tok("40px", "dimension", "Measured. prompt chip and icon button height"))
put(core, ["size", "signin-button"], tok("48px", "dimension", "Measured. console .signin-btn height"))
put(core, ["size", "field"], tok("43px", "dimension", "Measured. console email input height"))

put(core, ["shadow", "prompt"], tok([{
    "color": "rgba(0, 0, 0, 0.38)", "offsetX": "0px", "offsetY": "26px",
    "blur": "90px", "spread": "0px",
}], "shadow", "Measured. .mwm-prompt computed box-shadow"))

# Motion, from the console token layer (the marketing site declares durations
# as Tailwind utilities, not custom properties).
put(core, ["motion", "duration", "fast"], tok("140ms", "duration", SRC_CONSOLE + "; --mwm-duration .14s"))
put(core, ["motion", "duration", "sheet"], tok("180ms", "duration", SRC_CONSOLE + "; --mwm-motion-sheet .18s"))
put(core, ["motion", "duration", "base"], tok("150ms", "duration", SRC_CONSOLE + "; --default-transition-duration .15s"))
put(core, ["motion", "easing", "standard"], tok(
    [0.4, 0, 0.2, 1], "cubicBezier", SRC_CONSOLE + "; --mwm-ease"))
put(core, ["motion", "easing", "out"], tok(
    [0.2, 0, 0, 1], "cubicBezier", SRC_CONSOLE + "; --mwm-ease-out"))

dark = {}
not_tokenised = []

# Marketing colour roles.
ROLE = {
    "ink": "--mwm-ink",
    "ink-alt": "--mwm-ink-alt",
    "page": "--mwm-bg",
    "surface": "--mwm-surface-1",
    "surface-2": "--mwm-surface-2",
    "surface-hover": "--mwm-surface-hover",
    "panel": "--mwm-panel",
    "panel-2": "--mwm-panel-2",
    "hairline": "--mwm-hairline",
    "control": "--mwm-control",
    "control-active": "--mwm-control-active",
    "text": "--mwm-text",
    "text-muted": "--mwm-text-muted",
    "text-body": "--mwm-text-body",
    "text-tertiary": "--mwm-text-tertiary",
    "orange": "--mwm-orange",
    "orange-hot": "--mwm-orange-hot",
    "up": "--mwm-up",
    "down": "--mwm-down",
    "glow": "--mwm-glow-peak",
    "ai-grad-top": "--mwm-ai-grad-top",
    "ai-grad-bot": "--mwm-ai-grad-bot",
    "button-primary": "--mwm-btn-primary-bg",
    "button-primary-text": "--mwm-btn-primary-fg",
    "button-secondary": "--mwm-btn-secondary-bg",
    "button-secondary-text": "--mwm-btn-secondary-fg",
    "button-ghost-text": "--mwm-btn-ghost-fg",
}
for name, css_name in ROLE.items():
    take_color(dark, "color", name, home[css_name], SRC + "; " + css_name)
for name, css_name in {
    "line": "--mwm-line",
    "line-strong": "--mwm-line-strong",
    "muted": "--mwm-muted",
    "soft": "--mwm-soft",
    "orange-data-muted": "--mwm-orange-data-muted",
    "orange-data-border": "--mwm-orange-data-border",
    "orange-data-border-strong": "--mwm-orange-data-border-strong",
}.items():
    take_color(dark, "color", name, home[css_name], SRC + "; " + css_name)

# Computed colours the custom properties do not name.
computed = COMP["components"]
put(dark, ["color", "button-primary-hover"], tok(
    "#e9edf2", "color", "Measured. .mwm-product-start :hover computed background-color, rgb(233, 237, 242)"))
put(dark, ["color", "nav-hover"], tok(
    "rgba(255, 255, 255, 0.1)", "color", "Measured. .mwm-product-nav-item :hover computed background-color"))
put(dark, ["color", "topbar"], tok(
    "rgba(13, 13, 13, 0.8)", "color", "Measured. .mwm-product-topbar computed background-color"))
put(dark, ["color", "lede"], tok(
    "rgba(255, 255, 255, 0.7)", "color", "Measured. .mwm-hero-copy p computed color"))
put(dark, ["color", "focus"], tok(
    "#005fcc", "color", "Observed. Chromium's default focus ring, not an MWM colour: .mwm-product-nav-item, button-primary "
    "and button-secondary :focus-visible compute outline 'rgb(0, 95, 204) auto 1px' (raw/components.json), the "
    "browser's -webkit-focus-ring-color with outline-style auto. The marketing site styles no ring of its own; "
    "console's own ring is console.focus-ring."))
put(dark, ["color", "chip"], tok(
    "rgba(255, 255, 255, 0.05)", "color", "Measured. prompt chip computed background-color"))
put(dark, ["color", "prompt-border"], tok(
    "rgba(255, 255, 255, 0.1)", "color", "Measured. .mwm-prompt computed border-color"))
put(dark, ["color", "card-border"], tok(
    "rgba(255, 255, 255, 0.2)", "color", "Measured. .mwm-number-card computed border-color"))

# Console extras that the marketing layer does not declare.
for name, css_name in {
    "focus-ring": "--mwm-focus",
    "text-1": "--mwm-text-1",
    "text-2": "--mwm-text-2",
    "text-3": "--mwm-text-3",
    "agent": "--mwm-agent",
    "caution": "--mwm-caution",
    "live": "--mwm-live",
    "negative": "--mwm-negative",
    "line-subtle": "--mwm-line-subtle",
}.items():
    take_color(dark, "console", name, console[css_name], SRC_CONSOLE + "; " + css_name)

# Create's own page colours, the ones that actually paint the sign-in.
for name, css_name in {
    "page": "--bg-primary",
    "secondary": "--bg-secondary",
    "input": "--bg-input",
    "surface": "--bg-surface",
    "text": "--text-primary",
    "text-secondary": "--text-secondary",
    "text-muted": "--text-muted",
    "orange": "--brand-orange",
    "border": "--border-default",
}.items():
    take_color(dark, "create", name, create[css_name], SRC_CREATE + "; " + css_name)
put(dark, ["create", "provider"], tok(
    "rgba(255, 255, 255, 0.1)", "color", "Measured. create .signin-btn computed background-color"))
put(dark, ["create", "provider-hover"], tok(
    "rgba(255, 255, 255, 0.14)", "color", "Measured. create .signin-btn :hover computed background-color"))

not_tokenised.append({"name": "--mwm-btn-ghost-bg", "value": "transparent", "why": "DTCG colour tokens here are opaque or rgba strings; transparent is the absence of a fill"})
not_tokenised.append({"name": "--mwm-hatch", "value": console.get("--mwm-hatch", ""), "why": "a repeating gradient, not a single colour"})
not_tokenised.append({"name": "--mwm-font-display", "value": home["--mwm-font-display"], "why": "names Modern Gothic, which did not load; the computed face is Inter"})
not_tokenised.append({"name": "--brand-gradient-orange-pink", "value": create.get("--brand-gradient-orange-pink", ""), "why": "a gradient; the orange stop is create.orange"})

dark["$extensions"] = {"notTokenised": not_tokenised}

doc = {
    "$description": "MWM public signed-out surfaces, measured 2026-11-19. One dark theme. core holds type, radius, space and motion. dark holds the marketing --mwm-* colours, the console sign-in extras, and the create sign-in colours.",
    "core": core,
    "light": {},
    "dark": dark,
    "$themes": [{"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
}

if __name__ == "__main__":
    out = HERE / "tokens.json"
    text = json.dumps(doc, indent=1) + "\n"
    out.write_text(text)
    print("wrote", out, "bytes", len(text))
