#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cal.com's public surface spans three hosts, all of which declare a real
design-token layer — the custom properties harvested into raw/css-vars.json
(tools/capture/vars.mjs), resolved per surface and theme:

  marketing   cal.com/ /pricing /feature /teams /enterprise /customers /blog
              /faq — light only, calSans, painted in the --color-hp-* layer
              (#242424 ink, #6a6e78 muted, #e5e7eb lines, #cc4510 accent)
  booker      the public booking page on i.cal.com (cal.com/peer) — Inter,
              the --cal-* semantic layer, and the only surface that paints
              dark (its supported ?theme=dark&embed=true mode)
  auth        app.cal.com/auth/login and /signup — light cards, fontSans
              body and fontHeading display, the same --cal-* neutrals
              (serialized by the browser as lab()/oklab(), converted to hex)

So: declared {"var": ...} leaves carry the --color-hp-* and --cal-* layers,
--hp-shadow-* elevation, --ease-hp-* curves and --font-weight-*; measured
{"value": ..., "source": ...} leaves carry the type ramp, radii, control
heights, the near-black paints the variables do not name, and the focus ring.

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The light set holds the
marketing roles plus a booker.* subtree; the dark set is the booker's dark
theme (the marketing pages never paint dark, so their --color-hp-* dark
declarations stay unexported as a surface that does not paint).
"""
import json, math, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SURF = V["surfaces"]
# Light-resolution lookup for spec authoring: the site owns --color-hp-*,
# the booker owns --cal-*; shared names resolve identically (0 conflicts).
R = {}
for s in ("booker", "site"):
    for n, e in SURF[s]["resolved"]["light"].items():
        R[n] = e.get("value", e.get("raw"))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. cal.com declares "
    "the --color-hp-* homepage layer and the --cal-* semantic layer in its "
    "stylesheets (raw/css-vars.json); the marketing light roles alias the hp "
    "palette, the booker light roles live under light.booker.* over the same "
    "--cal-* variables the dark set re-resolves for the booker's dark theme "
    "(raw/components-computed.json for the measured pieces)."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    node[last] = leaf


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def _gam(u):
    u = max(0.0, min(1.0, u))
    return 12.92 * u if u <= 0.0031308 else 1.055 * u ** (1 / 2.4) - 0.055


def _hx(r, g, b, a=1.0):
    r, g, b = (max(0, min(255, round(v))) for v in (r, g, b))
    if a is None or float(a) >= 0.999:
        return "#%02x%02x%02x" % (r, g, b)
    return f"rgba({r}, {g}, {b}, {'%g' % float(a)})"


def _oklab(L, a, b, alpha):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541729 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return _hx(_gam(r) * 255, _gam(g) * 255, _gam(bb) * 255, alpha)


def _lab(L, a, b, alpha):
    """CIE Lab (D50, as CSS Color 4 defines lab()) -> sRGB, Bradford-adapted to D65."""
    k, eps = 24389 / 27, 216 / 24389
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    x = fx ** 3 if fx ** 3 > eps else (116 * fx - 16) / k
    y = fy ** 3 if L > k * eps else L / k
    z = fz ** 3 if fz ** 3 > eps else (116 * fz - 16) / k
    X, Y, Z = x * 0.3457 / 0.3585, y, z * (1 - 0.3457 - 0.3585) / 0.3585  # D50 white
    M1 = [[0.9554734527042182, -0.023098536874261423, 0.0632593086610217],
          [-0.028369706963208136, 1.0099954580058226, 0.021041398966943008],
          [0.012314001688319899, -0.020507696433477912, 1.3303659366080753]]  # Bradford D50 -> D65
    X, Y, Z = (sum(M1[i][j] * v for j, v in enumerate((X, Y, Z))) for i in range(3))
    M2 = [[3.2409699419045226, -1.537383177570094, -0.4986107602930034],
          [-0.9692436362808796, 1.8759675015077202, 0.04155505740717559],
          [0.05563007969699366, -0.20397695888897652, 1.0569715142428786]]  # XYZ D65 -> linear sRGB
    r, g, bb = (sum(M2[i][j] * v for j, v in enumerate((X, Y, Z))) for i in range(3))
    return _hx(_gam(r) * 255, _gam(g) * 255, _gam(bb) * 255, alpha)


def norm_color(v):
    """Any CSS colour the computed styles emitted -> #rrggbb or rgba(r, g, b, a).

    The auth host serializes its neutrals as lab()/oklab()/color(srgb), so the
    wide-gamut notations are converted to plain sRGB here."""
    v = (v or "").strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return _hx(r, g, b, round(a, 3))
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else (float(a) if a else 1)
        return _hx(float(r), float(g), float(b), a)
    m = re.fullmatch(r"oklab\(\s*([\d.]+)%?\s+(-?[\d.e]+)\s+(-?[\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, a, b, al = m.groups()
        L = float(L) / 100 if "%" in m.group(0).split(" ")[0] else float(L)
        al = float(al[:-1]) / 100 if al and al.endswith("%") else (float(al) if al else 1)
        return _oklab(L, float(a), float(b), al)
    m = re.fullmatch(r"oklch\(\s*([\d.]+)%?\s+([\d.e]+)\s+([\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, ch, h, al = m.groups()
        al = float(al[:-1]) / 100 if al and al.endswith("%") else (float(al) if al else 1)
        L = float(L) / 100 if "%" in m.group(0).split(" ")[0] else float(L)  # oklch(50% ...) is L 0.5
        return _oklab(L, float(ch) * math.cos(math.radians(float(h))), float(ch) * math.sin(math.radians(float(h))), al)
    m = re.fullmatch(r"lab\(\s*([\d.]+)%?\s+(-?[\d.e]+)\s+(-?[\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, a, b, al = m.groups()
        al = float(al[:-1]) / 100 if al and al.endswith("%") else (float(al) if al else 1)
        return _lab(float(L), float(a), float(b), al)
    m = re.fullmatch(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, al = m.groups()
        al = float(al[:-1]) / 100 if al and al.endswith("%") else (float(al) if al else 1)
        return _hx(float(r) * 255, float(g) * 255, float(b) * 255, al)
    return v


def split_layers(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [x.strip() for x in out]


def parse_shadow(s):
    """A computed box-shadow string -> DTCG shadow layers (transparent dropped)."""
    layers = []
    for l in split_layers(s or ""):
        inset = bool(re.search(r"(?:^|\s)inset(?:\s|$)", l))
        toks = re.sub(r"(?:^|\s)inset(?:\s|$)", " ", l).strip()
        m = re.match(r"^(.*?)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)(?:\s+(-?[\d.]+px))?$", toks)
        if not m:
            continue
        color, x, y, bl, sp = m.groups()
        color = norm_color(color.strip())
        if color in ("rgba(0, 0, 0, 0)", "transparent", ""):
            continue
        d = {"color": color, "offsetX": x, "offsetY": y, "blur": bl, "spread": sp or "0px"}
        if inset:
            d["inset"] = True
        layers.append(d)
    return layers


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def painted(comp, state):
    """First painted fill on or under the component."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg"):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg"):
            return n["bg"]
    return None


def measured(comp, state, prop, ty="color", via_text=False):
    if via_text:
        v = ts(comp, state, prop)
    else:
        try:
            v = st(comp, state).get(prop)
        except KeyError:
            return None
    if not v or v == "none":
        return None
    return norm_color(v) if ty == "color" else v


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("sans", "header", "default", "The marketing stack: the CalSans variable face with its metric fallback."),
    ("display", "signup-title", "default", "The fontHeading display face on the auth pages' headings."),
    ("app", "auth-card", "default", "The fontSans body face on the app.cal.com auth cards."),
    ("booker", "bk-page", "default", "The Inter stack the public booking page paints in."),
]:
    v = ts(comp, state, "fontFamily") or (have(comp, state, "fontFamily") and st(comp, state)["fontFamily"])
    if v:
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
if "--font-mono" in R:
    fam["mono"] = var("--font-mono", "fontFamily",
                      description="The declared monospace stack.")

wt = SPEC["core"]["font"].setdefault("weight", {})
for key, vname, desc in [
    ("normal", "--font-weight-normal", "Regular body weight."),
    ("medium", "--font-weight-medium", "The 500 nav, button and label weight."),
    ("semibold", "--font-weight-semibold", "The 600 booker title weight."),
    ("bold", "--font-weight-bold", "The 700 display and section-heading weight."),
]:
    if vname in R:
        wt[key] = var(vname, "fontWeight", description=desc)

# ------------------------------------------------------- declared colours
#
# The marketing pages paint the --color-hp-* homepage layer; the booker and
# auth hosts paint the --cal-* semantic layer. Both are declared, both are
# exported — hp under color.hp.*, cal under color.cal.* (light resolution;
# the dark set re-resolves the --cal-* variables for the booker dark theme).

hp = SPEC["core"].setdefault("color", {}).setdefault("hp", {})
for key, vname, desc in [
    ("page", "--color-hp-page", "The white marketing page field."),
    ("surface", "--color-hp-surface", "Card/panel white."),
    ("surface-2", "--color-hp-surface-2", "The #f9fafb sunken section field."),
    ("raised", "--color-hp-raised", "Raised white control fill."),
    ("field", "--color-hp-field", "The #f3f4f6 input/chip field."),
    ("chip", "--color-hp-chip", "The #f3f4f6 chip fill."),
    ("well", "--color-hp-well", "The #e5e7eb inset well."),
    ("plate", "--color-hp-plate", "The #f3f4f6 plate under framed content."),
    ("plate-line", "--color-hp-plate-line", "The 6%-ink plate ring."),
    ("hairline", "--color-hp-hairline", "The 7%-ink hairline."),
    ("line", "--color-hp-line", "The #e5e7eb rule line."),
    ("line-2", "--color-hp-line-2", "The #dee1e6 heavier rule (plan-card border)."),
    ("ink", "--color-hp-ink", "The #242424 headline ink — also the dark button fill."),
    ("ink-2", "--color-hp-ink-2", "The #292929 secondary ink."),
    ("text", "--color-hp-text", "The #111111 strongest text."),
    ("body", "--color-hp-body", "The #374151 body text."),
    ("muted", "--color-hp-muted", "The #6a6e78 muted text (hero lede)."),
    ("subtle", "--color-hp-subtle", "The #5f6570 quieter text."),
    ("quiet", "--color-hp-quiet", "The #858993 quietest text."),
    ("tint", "--color-hp-tint", "The #0f234b navy tint the shadows are drawn in."),
    ("on-ink", "--color-hp-on-ink", "The white label on dark fills."),
    ("accent", "--color-hp-accent", "The #cc4510 orange accent."),
    ("accent-ink", "--color-hp-accent-ink", "The #a83a0c accent text."),
    ("slot", "--color-hp-slot", "The #dee1e6 slot chip in the hero mock."),
    ("slot-selected", "--color-hp-slot-selected", "The #242424 selected slot."),
    ("highlight", "--color-hp-highlight", "White highlight paint."),
    ("bar", "--hp-bar", "The 52%-white glass the floating header blurs over."),
    ("material", "--hp-material", "The 74% #f3f4f6 window material."),
    ("mica", "--hp-mica", "The 88% #f3f4f6 mica material."),
]:
    if vname in R:
        hp[key] = var(vname, "color", description=desc)

cal = SPEC["core"]["color"].setdefault("cal", {})
for key, vname, desc in [
    ("bg", "--cal-bg", "The booker page field (#ffffff light)."),
    ("bg-subtle", "--cal-bg-subtle", "The #eeeff2 subtle fill (focused slot)."),
    ("bg-muted", "--cal-bg-muted", "The #f6f7f9 muted fill (slot hover)."),
    ("bg-emphasis", "--cal-bg-emphasis", "The #e5e7eb emphasis fill (day cell)."),
    ("bg-inverted", "--cal-bg-inverted", "The #070a0d inverted field."),
    ("bg-primary", "--cal-bg-primary", "The #1d2735 declared primary fill."),
    ("bg-primary-emphasis", "--cal-bg-primary-emphasis", "The #3c3e44 primary hover."),
    ("bg-brand", "--cal-bg-brand", "The declared brand fill."),
    ("bg-brand-emphasis", "--cal-bg-brand-emphasis", "The declared brand hover."),
    ("bg-info", "--cal-bg-info", "The #dde7fd info wash."),
    ("bg-success", "--cal-bg-success", "The #e4fbed success wash."),
    ("bg-error", "--cal-bg-error", "The #f9e3e1 error wash."),
    ("bg-attention", "--cal-bg-attention", "The #ffedd6 attention wash."),
    ("brand", "--cal-brand", "The declared brand colour (#111827 default)."),
    ("brand-text", "--cal-brand-text", "Text on the brand fill."),
    ("brand-emphasis", "--cal-brand-emphasis", "The brand emphasis."),
    ("text", "--cal-text", "The #3c3e44 booker/app body text."),
    ("text-emphasis", "--cal-text-emphasis", "The #070a0d strong booker text."),
    ("text-muted", "--cal-text-muted", "The #9ca3b0 muted booker text."),
    ("text-subtle", "--cal-text-subtle", "The #6b7280 subtle booker text."),
    ("text-inverted", "--cal-text-inverted", "Inverted text (#ffffff light)."),
    ("text-error", "--cal-text-error", "The #811d1d error text."),
    ("text-info", "--cal-text-info", "The #243c84 info text."),
    ("text-attention", "--cal-text-attention", "The #74331b attention text."),
    ("border", "--cal-border", "The #d1d5db booker field/slot border."),
    ("border-subtle", "--cal-border-subtle", "The #e5e7eb subtle border."),
    ("border-emphasis", "--cal-border-emphasis", "The #9ca3b0 emphasis border."),
    ("border-booker", "--cal-border-booker", "The booker frame border."),
]:
    if vname in R:
        cal[key] = var(vname, "color", description=desc)

# Measured paints the declared layers do not name.
paint = SPEC["core"]["color"].setdefault("paint", {})
for key, comp, state, prop, desc in [
    ("booker-primary", "bk-confirm", "default", "backgroundColor",
     "The #292929 fill the booker's confirm button and today cell paint — the booking page's effective brand paint (the declared --cal-brand #111827 is not what this page paints)."),
    ("bar", "header", "default", "backgroundColor",
     "The 72% #f4f4f4 glass the floating header bar computes to over --hp-bar."),
    ("footer", "footer", "default", "backgroundColor",
     "The #111111 near-black footer field."),
    ("hover-veil", "menu-link", "hover", "backgroundColor",
     "The ~4%-ink wash a dropdown item takes on hover."),
    ("muted-auth", "forgot-link", "default", "color",
     "The #696969 muted text on the app.cal.com auth cards."),
    ("emphasis-auth", "sso-google", "default", "backgroundColor",
     "The #262626 dark fill of the auth pages' SSO and continue buttons."),
]:
    if prop == "paint":
        v = norm_color(painted(comp, state) or "")
    else:
        v = measured(comp, state, prop)
    if v and v != "transparent":
        paint[key] = {"value": v, "type": "color",
                      "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                      "description": desc}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, tgt, desc in [
    ("--text-primary", "{color.hp.ink}", "Headline and strong text (#242424)."),
    ("--text-body", "{color.hp.body}", "Marketing body text."),
    ("--text-muted", "{color.hp.muted}", "Muted lede text."),
    ("--text-subtle", "{color.hp.subtle}", "Quieter text (pricing sub-line)."),
    ("--text-quiet", "{color.hp.quiet}", "The quietest marketing text."),
    ("--text-on-action", "{color.hp.on-ink}", "White label on the dark buttons."),
    ("--surface-page", "{color.hp.page}", "The white marketing page field."),
    ("--surface-raised", "{color.hp.raised}", "Raised white controls/cards."),
    ("--surface-sunken", "{color.hp.surface-2}", "The #f9fafb sunken field."),
    ("--surface-field", "{color.hp.field}", "The #f3f4f6 field fill."),
    ("--surface-chip", "{color.hp.chip}", "The chip fill."),
    ("--surface-well", "{color.hp.well}", "The inset well."),
    ("--surface-bar", "{color.paint.bar}", "The floating header's 72%-white glass."),
    ("--surface-dark", "{color.paint.footer}", "The near-black footer field."),
    ("--action-primary", "{color.hp.ink}", "The #242424 dark button fill."),
    ("--action-primary-hover", "{color.paint.hover-veil}", "The 4%-ink hover wash on quiet items."),
    ("--accent", "{color.hp.accent}", "The #cc4510 orange accent."),
    ("--accent-ink", "{color.hp.accent-ink}", "Accent-coloured text."),
    ("--border", "{color.hp.line}", "The #e5e7eb rule."),
    ("--border-strong", "{color.hp.line-2}", "The #dee1e6 heavier rule."),
    ("--border-hairline", "{color.hp.hairline}", "The 7%-ink hairline."),
]:
    emit(light, name, {"value": tgt, "type": "color", "source": ALIAS, "description": desc})

# The booker's light roles: the same --cal-* variables the dark set
# re-resolves, kept under booker.* so the marketing roles stay distinct.
for name, tgt, desc in [
    ("--booker-text", "{color.cal.text}", "Booker body text (#3c3e44)."),
    ("--booker-text-emphasis", "{color.cal.text-emphasis}", "The strong booker ink (day numbers)."),
    ("--booker-text-muted", "{color.cal.text-muted}", "Muted booker text."),
    ("--booker-text-subtle", "{color.cal.text-subtle}", "Subtle booker text."),
    ("--booker-text-inverted", "{color.cal.text-inverted}", "Inverted booker text."),
    ("--booker-surface", "{color.cal.bg}", "The booking page field."),
    ("--booker-surface-subtle", "{color.cal.bg-subtle}", "Focused slot fill."),
    ("--booker-surface-muted", "{color.cal.bg-muted}", "Slot hover fill."),
    ("--booker-surface-emphasis", "{color.cal.bg-emphasis}", "The selected day-cell fill."),
    ("--booker-border", "{color.cal.border}", "Slot and field borders."),
    ("--booker-border-subtle", "{color.cal.border-subtle}", "The booker frame border."),
    ("--booker-action", "{color.paint.booker-primary}", "The #292929 confirm/today paint this booking page uses for its brand moments."),
    ("--booker-brand", "{color.cal.brand}", "The declared brand colour."),
]:
    emit(light, name, {"value": tgt, "type": "color", "source": ALIAS, "description": desc})

# The booker's dark theme — the only dark surface that paints signed out.
# var leaves resolve under the dark theme, so the same --cal-* names carry
# their dark values here.
dark = SPEC["dark"]
for name, vname, desc in [
    ("--text-primary", "--cal-text", "The #d4d4d4 booker dark body text."),
    ("--text-emphasis", "--cal-text-emphasis", "The #fafafa strong dark text."),
    ("--text-muted", "--cal-text-muted", "The #a3a3a3 muted dark text."),
    ("--text-subtle", "--cal-text-subtle", "The subtle dark text."),
    ("--text-inverted", "--cal-text-inverted", "The #000000 inverted dark text."),
    ("--surface-page", "--cal-bg", "The #0f0f0f dark canvas."),
    ("--surface-subtle", "--cal-bg-subtle", "The #262626 subtle dark fill."),
    ("--surface-muted", "--cal-bg-muted", "The #171717 muted dark fill."),
    ("--surface-emphasis", "--cal-bg-emphasis", "The #404040 emphasis dark fill."),
    ("--surface-inverted", "--cal-bg-inverted", "The #fafafa inverted dark field."),
    ("--border", "--cal-border", "The #4d4d4d dark border."),
    ("--border-subtle", "--cal-border-subtle", "The #262626 subtle dark border."),
    ("--border-emphasis", "--cal-border-emphasis", "The #737373 emphasis dark border."),
    ("--action-primary", "--cal-bg-primary", "The #f5f5f5 inverted dark button fill."),
    ("--brand", "--cal-brand", "The dark brand (#ffffff)."),
]:
    emit(dark, name, {"var": vname, "type": "color", "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, prop, desc in [
    ("display", "hero-title", "default", "fontSize", "The 80px hero display ('Where people find the time to meet')."),
    ("h1", "pricing-h1", "default", "fontSize", "The 64px page-heading size."),
    ("h2", "signup-title", "default", "fontSize", "The 56px fontHeading size on the auth cards."),
    ("display-mobile", "m-hero", "default", "fontSize", "The 42px display size at 390px."),
    ("h3", "plan-tab", "default", "fontSize", "The 22px plan-name/section size."),
    ("lede", "hero-sub", "default", "fontSize", "The 20px lede (also the booker event title)."),
    ("body", "header", "default", "fontSize", "The 16px base size."),
    ("ui", "nav-link", "default", "fontSize", "The 14px nav/button/field size."),
    ("small", "trust-row", "default", "fontSize", "The 13px smallest auth text."),
    ("tiny", "changelog", "default", "fontSize", "The 11px badge label (text node)."),
]:
    v = ts(comp, state, prop)
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"]["font"].setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The 1.08 display leading."),
    ("h1", "pricing-h1", "default", "The 1.0 page-heading leading."),
    ("h2", "signup-title", "default", "The 1.0 auth-heading leading."),
    ("lede", "hero-sub", "default", "The 1.4 lede leading."),
    ("ui", "nav-link", "default", "The 1.5 control-label leading."),
    ("body", "header", "default", "The 1.5 body leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

track = SPEC["core"]["font"].setdefault("letterSpacing", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The -0.8px display tracking (-1%)."),
    ("h1", "pricing-h1", "default", "The -0.64px heading tracking (-1%)."),
    ("h3", "plan-tab", "default", "The -0.22px section tracking (-1%)."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        track[key] = {"type": "dimension", "value": v,
                      "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                      "description": desc}

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("sm", "changelog", "default", "borderTopLeftRadius", "The 8px badge/day-cell radius."),
    ("md", "nav-link", "default", "borderTopLeftRadius", "The 10px control radius (nav items, slots, fields, SSO buttons)."),
    ("lg", "nav-cta", "default", "borderTopLeftRadius", "The 12px CTA radius (header and plan buttons)."),
    ("xl", "hero-google", "default", "borderTopLeftRadius", "The 14px hero-button/card radius."),
    ("2xl", "header", "default", "borderTopLeftRadius", "The 18px floating-bar and menu-card radius."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
if have("billing-toggle", "default", "borderTopLeftRadius"):
    radius["pill"] = {"value": "9999px", "type": "dimension",
                      "source": "computed borderTopLeftRadius of billing-toggle default: the capsule computes to an unbounded 3.36e7px, normalized here to the pill constant (raw/components-computed.json)",
                      "description": "The capsule shape (billing switch)."}

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("hp", "--ease-hp", "The homepage's long ease-out cubic-bezier(.19,1,.22,1)."),
    ("hp-fly", "--ease-hp-fly", "The fly-in curve cubic-bezier(.22,1,.36,1)."),
    ("hp-quad", "--ease-hp-quad", "The quad curve cubic-bezier(.25,.46,.45,.94)."),
    ("out", "--ease-out", "The standard Tailwind ease-out."),
    ("in-out", "--ease-in-out", "The standard ease-in-out."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)

# ------------------------------------------------------------------ shadows

shadow = SPEC["core"].setdefault("shadow", {})
for key, vname, desc in [
    ("lift", "--hp-shadow-lift", "The resting button/card ring + drop (1px 6% + 1px 4%)."),
    ("raised", "--hp-shadow-raised", "The raised control: white inset top line, ring and drop."),
    ("well", "--hp-shadow-well", "The inset well shadow."),
    ("plate", "--hp-shadow-plate", "The inset plate ring."),
    ("float", "--hp-shadow-float", "The floating-menu ring + soft drop."),
    ("print", "--hp-shadow-print", "The product-mock window shadow."),
    ("print-lift", "--hp-shadow-print-lift", "The lifted print shadow."),
    ("window", "--hp-shadow-window", "The big OS-window shadow on the hero mock."),
]:
    if vname in R:
        layers = parse_shadow(str(R[vname]))
        if layers:
            shadow[key] = {"value": layers, "type": "shadow",
                           "source": f"css-var {vname} (light)",
                           "description": desc}

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# The marketing focus ring: a 1px white gap then a 3px #9ca3af ring, drawn as
# box-shadow layers on :focus-visible (the element's own outline stays none).
try:
    s = st("nav-cta", "focus-visible")
    layers = parse_shadow(s.get("boxShadow", ""))
    if layers:
        meas["focus-ring"] = {"value": layers, "type": "shadow",
                              "source": "computed boxShadow of nav-cta focus-visible (raw/components-computed.json)",
                              "description": "The keyboard focus ring every marketing control draws: 1px white gap, then a 3px #9ca3af ring."}
except KeyError:
    pass
# The booker's focus ring: a 1px half-white gap + 2px 10%-black ring (bk-slot).
try:
    s = st("bk-slot", "focus-visible")
    layers = parse_shadow(s.get("boxShadow", ""))
    if layers:
        meas["booker-focus-ring"] = {"value": layers, "type": "shadow",
                                     "source": "computed boxShadow of bk-slot focus-visible (raw/components-computed.json)",
                                     "description": "The booker's quieter focus ring: 1px 20%-white gap, then a 2px 10%-black ring."}
except KeyError:
    pass
# The pressed slot inverts its shadow to a 1px top inset.
try:
    s = st("bk-slot", "pressed")
    layers = parse_shadow(s.get("boxShadow", ""))
    if layers:
        meas["slot-pressed-shadow"] = {"value": layers, "type": "shadow",
                                       "source": "computed boxShadow of bk-slot pressed (raw/components-computed.json)",
                                       "description": "The slot's pressed state: the drop shadow flips to a top inset."}
except KeyError:
    pass
for key, comp, state, prop, desc in [
    ("control-transition", "bk-day", "default", "transitionDuration", "The booker controls' 0.15s colour/shadow transition."),
    ("menu-transition", "menu-link", "default", "transitionDuration", "The dropdown items' 0.1s hover fade."),
    ("navitem-transition", "m-nav-item", "default", "transitionDuration", "The mobile nav items' 0.15s transition."),
]:
    try:
        s = st(comp, state)
        first = s[prop].split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except (KeyError, TypeError):
        pass
if "--default-transition-duration" in R:
    meas["default-duration"] = var("--default-transition-duration", "duration",
                                   description="The declared default 0.15s transition duration.")

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The floating header height at 1440."),
    ("header.height-mobile", "m-header", "default", "height", "The floating header at 390."),
    ("nav.button-height", "nav-cta", "default", "height", "The 36px nav control height."),
    ("hero.button-height", "hero-google", "default", "height", "The 64px hero SSO button height."),
    ("control.height", "plan-cta", "default", "height", "The 36px standard button height."),
    ("slot.height", "bk-slot", "default", "height", "The 36px booker slot height."),
    ("day.size", "bk-day", "default", "height", "The 59px booker day cell."),
    ("field.height", "bk-field", "default", "height", "The 32px booker field height."),
    ("auth.field-height", "email-field", "default", "height", "The 30px auth field height."),
    ("auth.button-height", "signup-google", "default", "height", "The 40px auth button height."),
    ("menu.card-width", "menu-link", "default", "width", "The 200px product-card column in the dropdown."),
    ("mobile.navitem-height", "m-nav-item", "default", "height", "The 48px mobile menu row."),
    ("card.radius", "plan-card", "default", "borderTopLeftRadius", "The plan-card radius."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
