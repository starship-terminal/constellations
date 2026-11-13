#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Two public surfaces paint signed out, both dark only:

  marketing   endlesstools.io — a Next.js + Tailwind v4 one-pager. Its bundle
              declares a real @theme layer (the --color-*, --text-*, --radius-*,
              --ease-*, --blur-* custom properties harvested into
              raw/css-vars.json by tools/capture/vars.mjs and resolved in the
              "dark" probe pass) but paints most accents as arbitrary values —
              the pink CTA #ff13b1, the blue education chip #2c5cff and the
              card fills #121212/#1d1d1d are literal utilities, never declared.
              Those become **measured** leaves from raw/components-computed.json.
  app shell   app.endlesstools.io — the /login card and /legal/* documents on
              Tailwind v3, same grey ramp (--color-black #0a0a0a, grey-1 #373737,
              grey-2 #2a2a2a, grey-3 #555, grey-4 #959595, secondary #1e1e1e,
              white #efefef ink). body.bg-back paints rgb(10 10 10).

  ink         #fff on marketing (body text-white), #efefef on the app shell;
              muted #959595 (--color-grey-4), dimmed white/30 labels
  field       #000 marketing page, #0a0a0a app page; #121212 plan cards
              (hover #1d1d1d), #1e1e1e input fills, white/5 login card veil,
              #080808 testimonial inset
  accent      pink #ff13b1 (hover #ff4bc4) hero CTA and #ff3dae save pill;
              blue #2c5cff (hover #5a65ff) education CTAs
  type        the declared --text-* ramp (title-primary 42/46 500 -0.03em down
              to body-secondary 12/14); the app shell measures its own ramp
              (23/25 card title, 14/15 fields, 12/13 small)
  shape       pill radii (Chrome computes rounded-full as 33554432px),
              33px plan cards, 20px login card, 16px thumbnails,
              12px --radius-fill insets, 10px --radius-base controls
  states      1px auto #005fcc UA focus rings on the marketing links;
              on the app shell 2px transparent outlines at 2px offset plus a
              border swap to grey-1 — the Tailwind focus preset

A leaf is {"var": "--name"} (resolved by build_tokens.py in the dark pass) or
{"value": ..., "source": "..."} for a measured value. The surfaces paint one
dark theme; the `light` set stays empty so build_tokens.py emits core and dark.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RD = V["resolved"]["dark"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. The two public "
    "surfaces of endlesstools.io (Tailwind v4 marketing one-pager) and "
    "app.endlesstools.io (Tailwind v3 /login and /legal/* shell) both paint a "
    "single dark theme over the same grey ramp. Declared @theme variables "
    "become var leaves resolved in the dark pass; the arbitrary-value accents "
    "and card fills are measured leaves from raw/components-computed.json. "
    "Semantic roles land in the dark set."),
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


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


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


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
fam["sans"] = {"value": 'Inter, "Inter Fallback"', "type": "fontFamily",
               "source": "computed fontFamily of every measured component (raw/components-computed.json); the Inter @font-face faces are in raw/css-vars.json fonts",
               "description": "Inter variable (100-900, woff2, swap) with next/font's Arial-metric 'Inter Fallback'; the only family any measured text paints."}
fam["system"] = var("--font-sans", "fontFamily",
                  description="The plain ui-sans-serif system stack Tailwind v4 declares; painted as the login legal line's font.")
if "--font-mono" in R:
    fam["mono"] = var("--font-mono", "fontFamily",
                      description="The ui-monospace system stack (declared; no measured text paints it on the public surfaces).")
fam["skeleton"] = {"value": '"Flow Rounded", "Flow Rounded Fallback"', "type": "fontFamily",
                   "source": "@font-face 'Flow Rounded' declared as --font-skeleton in the app bundle (raw/css-vars.json fonts)",
                   "description": "Flow Rounded: the geometric placeholder face the app bundles for skeleton/loading text; no measured component paints it."}

# ------------------------------------------------------------ declared ramp
# The marketing @theme text scale, resolved in the dark pass.

size = SPEC["core"]["font"].setdefault("size", {})
lead = SPEC["core"]["font"].setdefault("lineHeight", {})
wght = SPEC["core"]["font"].setdefault("weight", {})
trck = SPEC["core"]["font"].setdefault("tracking", {})

for key, vname, desc in [
    ("title-primary", "--text-title-primary", "42px: hero, section and newsletter titles."),
    ("title-secondary", "--text-title-secondary", "24px: asset/section sub-heads; the mobile hero size."),
    ("subtitle", "--text-subtitle", "18px subtitle step (declared; no measured component paints it on the public pages)."),
    ("body-primary", "--text-body-primary", "14px: lede, footer and consent text."),
    ("body-secondary", "--text-body-secondary", "12px: pill buttons, chips and small labels."),
]:
    if vname in R:
        size[key] = var(vname, "dimension", description=desc)
for key, vname in [
    ("title-primary", "--text-title-primary--line-height"),
    ("title-secondary", "--text-title-secondary--line-height"),
    ("subtitle", "--text-subtitle--line-height"),
    ("body-primary", "--text-body-primary--line-height"),
    ("body-secondary", "--text-body-secondary--line-height"),
]:
    if vname in R:
        lead[key] = var(vname, "dimension")
for key, vname, desc in [
    ("medium", "--font-weight-medium", "500: every title, button and label — no lighter or bolder weight paints."),
    ("title-primary", "--text-title-primary--font-weight", "500 on the 42px titles."),
    ("title-secondary", "--text-title-secondary--font-weight", "500 on the 24px heads."),
]:
    if vname in R:
        wght[key] = var(vname, "fontWeight", description=desc)
for key, vname, desc in [
    ("title", "--text-title-primary--letter-spacing", "-0.03em: the tight tracking on both title steps."),
    ("tight", "--tracking-tight", "-0.025em Tailwind tracking-tight (billing toggle, login labels)."),
]:
    if vname in R:
        trck[key] = var(vname, "other" if RD[vname].get("kind") == "other" else "dimension", description=desc)

# Measured type steps the ramp does not declare (app shell + specials).
for key, comp, state, prop, desc in [
    ("price", "plan-price", "default", "fontSize", "42px price figure on the plan cards."),
    ("login-title", "login-title", "default", "fontSize", "23px login card title."),
    ("legal-title", "legal-title", "default", "fontSize", "42px legal document title."),
    ("toggle", "billing-yearly", "default", "fontSize", "16px billing toggle label."),
    ("body", "footer-link", "default", "fontSize", "14px footer/body text."),
    ("login-body", "login-field", "default", "fontSize", "14px login field text (its own 15px leading)."),
    ("login-small", "login-forgot", "default", "fontSize", "12px login helper text (13px leading)."),
    ("chip", "plan-chip", "default", "fontSize", "14px plan chip label at 35px leading."),
]:
    if have(comp, state, prop):
        size[key] = {"value": st(comp, state)[prop], "type": "dimension",
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
for key, comp, state, desc in [
    ("price", "plan-price", "default", "42px flat leading on the price figure."),
    ("login-title", "login-title", "default", "25px on the login card title."),
    ("legal-title", "legal-title", "default", "40px on the legal title."),
    ("toggle", "billing-yearly", "default", "24px on the billing toggle."),
    ("body", "footer-link", "default", "18px on footer text."),
    ("login-body", "login-field", "default", "15px on login field text."),
    ("login-small", "login-forgot", "default", "13px on login helper text."),
    ("chip", "plan-chip", "default", "35px on the plan chips (full line-height pill)."),
    ("save-pill", "save-pill", "default", "25px on the save pill."),
]:
    if have(comp, state, "lineHeight"):
        lead[key] = {"value": st(comp, state)["lineHeight"], "type": "dimension",
                     "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
for key, comp, state, prop, desc in [
    ("regular", "hero-lede", "default", "fontWeight", "400 body copy weight."),
    ("legal", "legal-title", "default", "fontWeight", "400 on the legal document title."),
    ("login-label", "login-field", "default", "fontWeight", "500 on login fields and buttons."),
]:
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        wght[key] = {"value": int(v), "type": "fontWeight",
                     "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
for key, comp, state, desc in [
    ("price", "plan-price", "default", "-0.03em on the price figure."),
    ("login-label", "login-field", "default", "-0.025em on the login labels."),
]:
    if have(comp, state, "letterSpacing"):
        trck[key] = {"value": st(comp, state)["letterSpacing"], "type": "other",
                     "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

# ------------------------------------------------------------- core colour

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, vname, desc in [
    ("black", "--color-black", "#0a0a0a: the app-shell page field (body.bg-back) and the ink on white controls."),
    ("white", "--color-white", "#fff: marketing ink and the white controls."),
    ("secondary", "--color-secondary", "#1e1e1e: input fills and translucent nav pills."),
    ("grey-1", "--color-grey-1", "#373737: hover fills and focused field borders."),
    ("grey-2", "--color-grey-2", "#2a2a2a: field borders, sign-in pill, switch hover."),
    ("grey-3", "--color-grey-3", "#555: secondary greys."),
    ("grey-4", "--color-grey-4", "#959595: muted text — ledes, footer, placeholders, helpers."),
]:
    if vname in R:
        neutral[key] = var(vname, "color", description=desc)

# Painted neutrals that are arbitrary utilities, never declared.
for key, val, src, desc in [
    ("page", "#000000", "the body.bg-[#000] literal on the marketing page + computed fills of header/nav gradient", "#000 marketing page field (Tailwind black, not the --color-black #0a0a0a)."),
    ("card", "#121212", "computed backgroundColor of plan-card default (raw/components-computed.json)", "#121212 plan/testimonial card fill."),
    ("card-hover", "#1d1d1d", "computed backgroundColor of plan-card hover; declared literal in hover:bg-[#1D1D1D]", "#1d1d1d card hover fill."),
    ("inset", "#080808", "computed backgroundColor of social-card default (raw/components-computed.json)", "#080808 testimonial card fill."),
    ("ring", "#222222", "computed boxShadow ring of plan-card default; declared literal in .ring-[#222222]", "#222 card hairline ring."),
    ("thumb-border", "#343434", "computed borderTopColor of asset-thumb default (raw/components-computed.json)", "#343434 asset thumbnail border."),
    ("ink", "#efefef", "computed color of login-field default and textStyle of login-card (raw/components-computed.json)", "#efefef app-shell text white (bg-white utility, not --color-white #fff)."),
    ("hover-white", "#c4c4c4", "computed backgroundColor of plan-cta hover; declared literal in hover:bg-[#C4C4C4]", "#c4c4c4 white-button hover fill."),
]:
    neutral[key] = {"value": val, "type": "color", "source": src, "description": desc}

alpha = neutral.setdefault("alpha", {})
for key, val, src, desc in [
    ("veil-5", "rgba(239, 239, 239, 0.05)", "computed backgroundColor of login-card default (raw/components-computed.json)", "5% app-ink veil: the login card fill."),
    ("ink-75", "rgba(239, 239, 239, 0.75)", "computed color of legal-signin hover / legal-link (raw/components-computed.json)", "75% app ink on hover/legal links."),
    ("ink-90", "rgba(239, 239, 239, 0.9)", "computed backgroundColor of send-code hover (raw/components-computed.json)", "90% app ink: app-button hover fill."),
    ("white-30", "oklab(0.999994 0.0000455678 0.0000200868 / 0.3)", "computed color of billing-monthly default (raw/components-computed.json); Tailwind white/30 color-mix", "30% white: unselected toggle label."),
    ("white-75", "oklab(0.999994 0.0000455678 0.0000200868 / 0.75)", "declared color-mix in hover:text-white/75 (raw/css-vars.json tailwind)", "75% white on text hover."),
    ("white-85", "oklab(0.999994 0.0000455678 0.0000200868 / 0.85)", "computed backgroundColor of news-submit hover (raw/components-computed.json); Tailwind white/85", "85% white: marketing button hover."),
    ("black-50", "oklab(0.144787 0.00000661612 0.00000289828 / 0.5)", "computed backgroundColor of carousel-prev default (raw/components-computed.json); Tailwind black/50", "50% black: carousel arrow rest fill."),
    ("black-80", "oklab(0.144787 0.00000661612 0.00000289828 / 0.8)", "computed backgroundColor of carousel-prev hover; declared hover:bg-black/80", "80% black: carousel arrow hover fill."),
    ("placeholder-50", "oklab(0.999994 0.0000455678 0.0000200868 / 0.5)", "computed placeholder color of news-field (raw/components-computed.json)", "50% white: newsletter field placeholder."),
]:
    alpha[key] = {"value": val, "type": "color", "source": src, "description": desc}

accent = SPEC["core"].setdefault("color", {}).setdefault("accent", {})
for key, val, src, desc in [
    ("pink", "#ff13b1", "computed backgroundColor of hero-cta default (raw/components-computed.json)", "#ff13b1 magenta: the hero Start-creating fill."),
    ("pink-hover", "#ff4bc4", "computed backgroundColor of hero-cta hover; declared literal in hover:bg-[#FF4BC4]", "#ff4bc4 pink hover/pressed."),
    ("pill", "#ff3dae", "computed backgroundColor of save-pill default and billing-yearly paint (raw/components-computed.json)", "#ff3dae pink: the 'Save 20%' pill."),
    ("blue", "#2c5cff", "computed backgroundColor of plan-chip-edu and edu-cta default (raw/components-computed.json)", "#2c5cff blue: education chip and CTA."),
    ("blue-hover", "#5a65ff", "computed backgroundColor of edu-cta hover; declared literal in hover:bg-[#5A65FF]", "#5a65ff blue hover/pressed."),
    ("focus", "#005fcc", "computed outlineColor of footer-link/plan-cta focus-visible (raw/components-computed.json): the UA -webkit-focus-ring-color", "#005fcc: the browser's own keyboard focus ring on marketing links."),
]:
    accent[key] = {"value": val, "type": "color", "source": src, "description": desc}

grad = SPEC["core"].setdefault("gradient", {})
for key, val, src, desc in [
    ("nav", "linear-gradient(rgb(0, 0, 0) 14.73%, rgba(0, 10, 10, 0) 100%)", "computed backgroundImage of header default (raw/components-computed.json); declared .nav-gradient", "The black veil the sticky header fades from."),
    ("overlay", "linear-gradient(rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 85.27%)", "declared .ui-overlay-gradient in the readable sheets (raw/css-vars.json tailwind)", "The bottom fade over media tiles."),
]:
    grad[key] = {"value": val, "type": "other", "source": src, "description": desc}

# ------------------------------------------------------------------- shape

radius = SPEC["core"].setdefault("radius", {})
for key, vname, desc in [
    ("base", "--radius-base", "10px: app-shell fields and buttons."),
    ("fill", "--radius-fill", "12px: inner tiles and card fills."),
]:
    if vname in R:
        radius[key] = var(vname, "dimension", description=desc)
for key, val, src, desc in [
    ("thumb", "16px", "computed borderTopLeftRadius of asset-thumb default (raw/components-computed.json)", "16px asset thumbnails."),
    ("login", "20px", "computed borderTopLeftRadius of login-card default (raw/components-computed.json)", "20px login card."),
    ("card", "33px", "computed borderTopLeftRadius of plan-card default (raw/components-computed.json)", "33px plan/testimonial cards."),
    ("pill", "9999px", "computed radius of every rounded-full control (raw/components-computed.json): Chrome resolves Tailwind rounded-full (calc(infinity * 1px)) to 33554432px", "Fully rounded: buttons, chips, pills, checkboxes."),
]:
    radius[key] = {"value": val, "type": "dimension", "source": src, "description": desc}

# ----------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
if "--spacing" in R:
    sp["unit"] = var("--spacing", "dimension",
                     description="Tailwind v4's 4px spacing unit.")
for key, comp, state, prop, desc in [
    ("control-x", "nav-cta", "default", "paddingLeft", "20px inline padding on pill buttons and the newsletter field."),
    ("chip-x", "plan-chip", "default", "paddingLeft", "15px chip padding."),
    ("pill-x", "save-pill", "default", "paddingLeft", "10px save-pill padding."),
    ("field-x", "login-field", "default", "paddingLeft", "15px app-field padding."),
    ("switch-x", "login-switch", "default", "paddingLeft", "25px secondary-button padding."),
    ("signin-x", "legal-signin", "default", "paddingLeft", "30px legal sign-in padding."),
    ("card", "plan-card", "default", "paddingTop", "15px plan-card padding."),
    ("login-card", "login-card", "default", "paddingTop", "50px login-card padding."),
    ("footer-y", "footer", "default", "paddingTop", "150px above and below the footer."),
]:
    if have(comp, state, prop):
        sp[key] = {"value": st(comp, state)[prop], "type": "dimension",
                   "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                   "description": desc}

# ------------------------------------------------------------------ motion

mot = SPEC["core"].setdefault("motion", {})
if "--default-transition-duration" in R:
    mot.setdefault("duration", {})["default"] = var("--default-transition-duration", "duration",
        description="150ms: the default transition duration on buttons and pills.")
for key, val, src, desc in [
    ("fast", "0.2s", "declared .duration-200 in the readable sheets (raw/css-vars.json tailwind)", "200ms duration used on toggles."),
    ("slow", "0.3s", "declared .duration-300 in the readable sheets (raw/css-vars.json tailwind)", "300ms duration used on cards."),
]:
    mot.setdefault("duration", {})[key] = {"value": val, "type": "duration", "source": src, "description": desc}
if "--ease-in-out" in R:
    mot.setdefault("easing", {})["in-out"] = var("--ease-in-out", "cubicBezier",
        description="cubic-bezier(.4,0,.2,1): the default transition timing.")
mot.setdefault("press", {})["scale"] = {"value": "scale(0.95)", "type": "other",
    "source": "declared .active:scale-95 in the readable sheets (raw/css-vars.json tailwind)",
    "description": "Buttons scale to 95% while pressed."}
# The keyframe animations recorded by measure.mjs's sheet walk
# (raw/components-computed.json _meta.sheets): the marketing page's own two,
# the app shell's Tailwind three.
for key, val, src, desc in [
    ("gradient-flow", "move-gradient 1.5s ease-in-out infinite alternate",
     "recorded .animate-gradient-flow rule (raw/components-computed.json _meta.sheets.home)",
     "The gradient drift on the hero title's marks."),
    ("orbit", "et-orbit var(--orbit-duration, 28s) linear infinite",
     "recorded .animate-orbit rule (raw/components-computed.json _meta.sheets.home)",
     "The hero's orbiting asset marks."),
    ("skeleton", "SkeletonLoading 1s linear infinite alternate",
     "recorded .ui-skeleton__field/.ui-skeleton__unit rule (raw/components-computed.json _meta.sheets.login)",
     "The app shell's skeleton shimmer (the Flow Rounded placeholder face)."),
    ("pulse", "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite",
     "recorded .animate-pulse rule (raw/components-computed.json _meta.sheets.login)",
     "Tailwind's pulse on the app shell."),
    ("spin", "spin 1s linear infinite",
     "recorded .animate-spin rule (raw/components-computed.json _meta.sheets.login)",
     "Tailwind's spin on the app shell."),
]:
    mot.setdefault("animation", {})[key] = {"value": val, "type": "other",
        "source": src, "description": desc}

# ---------------------------------------------------------------- gradients
# (kept in core.color.gradient above)

# ------------------------------------------------------------------- dark set

D = SPEC["dark"]

surf = D.setdefault("surface", {})
surf["page"] = {"value": "{color.neutral.page}", "type": "color",
                "source": "role alias over the core palette",
                "description": "#000 marketing page field."}
surf["app"] = {"value": "{color.neutral.black}", "type": "color",
               "source": "role alias over the core palette",
               "description": "#0a0a0a app-shell page field (body.bg-back)."}
surf["header-veil"] = {"value": "{gradient.nav}", "type": "other",
                       "source": "role alias over the core palette",
                       "description": "The black fade behind the sticky header."}
surf["card"] = {"value": "{color.neutral.card}", "type": "color", "source": "role alias",
                "description": "#121212 card fill."}
surf["card-hover"] = {"value": "{color.neutral.card-hover}", "type": "color", "source": "role alias",
                      "description": "#1d1d1d card hover fill."}
surf["inset"] = {"value": "{color.neutral.inset}", "type": "color", "source": "role alias",
                 "description": "#080808 testimonial card fill."}
surf["field"] = {"value": "{color.neutral.secondary}", "type": "color", "source": "role alias",
                 "description": "#1e1e1e field fill."}
surf["raised"] = {"value": "{color.neutral.grey-2}", "type": "color", "source": "role alias",
                  "description": "#2a2a2a raised fill (sign-in pill, switch hover)."}
surf["hover"] = {"value": "{color.neutral.grey-1}", "type": "color", "source": "role alias",
                 "description": "#373737 hover/focused fill."}
surf["veil"] = {"value": "{color.neutral.alpha.veil-5}", "type": "color", "source": "role alias",
                "description": "5% ink veil (login card)."}
surf["overlay"] = {"value": "{color.neutral.alpha.black-50}", "type": "color", "source": "role alias",
                   "description": "50% black overlay (carousel arrow)."}
surf["overlay-hover"] = {"value": "{color.neutral.alpha.black-80}", "type": "color", "source": "role alias",
                         "description": "80% black overlay hover."}

text = D.setdefault("text", {})
text["primary"] = {"value": "{color.neutral.white}", "type": "color", "source": "role alias",
                   "description": "#fff marketing text (body text-white)."}
text["app"] = {"value": "{color.neutral.ink}", "type": "color", "source": "role alias",
               "description": "#efefef app-shell text."}
text["muted"] = {"value": "{color.neutral.grey-4}", "type": "color", "source": "role alias",
                 "description": "#959595 muted text (ledes, footer, helpers)."}
text["dim"] = {"value": "{color.neutral.alpha.white-30}", "type": "color", "source": "role alias",
               "description": "30% white: unselected labels."}
text["app-dim"] = {"value": "{color.neutral.alpha.ink-75}", "type": "color", "source": "role alias",
                   "description": "75% app ink: legal links, sign-in hover."}
text["on-light"] = {"value": "{color.neutral.black}", "type": "color", "source": "role alias",
                    "description": "#0a0a0a on white controls."}
text["on-accent"] = {"value": "{color.neutral.white}", "type": "color", "source": "role alias",
                     "description": "#fff on the pink/blue accents."}
text["placeholder"] = {"value": "{color.neutral.alpha.placeholder-50}", "type": "color", "source": "role alias",
                       "description": "50% white placeholder on marketing fields."}
text["placeholder-app"] = {"value": "{color.neutral.grey-4}", "type": "color", "source": "role alias",
                           "description": "#959595 placeholder on app fields."}

bdr = D.setdefault("border", {})
bdr["card"] = {"value": "{color.neutral.ring}", "type": "color", "source": "role alias",
               "description": "#222 card hairline (1px ring)."}
bdr["field"] = {"value": "{color.neutral.grey-2}", "type": "color", "source": "role alias",
                "description": "#2a2a2a field border."}
bdr["field-focus"] = {"value": "{color.neutral.grey-1}", "type": "color", "source": "role alias",
                      "description": "#373737 focused field border/ring."}
bdr["thumb"] = {"value": "{color.neutral.thumb-border}", "type": "color", "source": "role alias",
                "description": "#343434 asset thumbnail border."}
bdr["muted"] = {"value": "{color.neutral.grey-4}", "type": "color", "source": "role alias",
                "description": "#959595 consent box border (border-current on muted text)."}

act = D.setdefault("action", {})
act["bg"] = {"value": "{color.neutral.white}", "type": "color", "source": "role alias",
             "description": "#fff primary controls (nav CTA, plan CTA, newsletter submit)."}
act["fg"] = {"value": "{color.neutral.black}", "type": "color", "source": "role alias",
             "description": "#0a0a0a on the white controls."}
act["bg-hover"] = {"value": "{color.neutral.hover-white}", "type": "color", "source": "role alias",
                   "description": "#c4c4c4 white-control hover."}
act["bg-hover-soft"] = {"value": "{color.neutral.alpha.white-85}", "type": "color", "source": "role alias",
                        "description": "85% white hover (newsletter submit)."}
act["app-bg"] = {"value": "{color.neutral.ink}", "type": "color", "source": "role alias",
                 "description": "#efefef app-shell buttons (bg-white utility)."}
act["app-bg-hover"] = {"value": "{color.neutral.alpha.ink-90}", "type": "color", "source": "role alias",
                       "description": "90% app-ink button hover."}
act["nav-bg-hover"] = {"value": "{color.neutral.grey-1}", "type": "color", "source": "role alias",
                       "description": "#373737 nav-action hover fill: the header's white pill flips dark."}
act["nav-fg-hover"] = {"value": "{color.neutral.white}", "type": "color", "source": "role alias",
                       "description": "#fff nav-action hover text."}

acc = D.setdefault("accent", {})
for k, desc in [
    ("pink", "#ff13b1 primary accent CTA."),
    ("pink-hover", "#ff4bc4 accent hover/pressed."),
    ("pill", "#ff3dae save/discount pill."),
    ("blue", "#2c5cff education accent."),
    ("blue-hover", "#5a65ff education hover/pressed."),
]:
    acc[k] = {"value": "{color.accent." + k + "}", "type": "color", "source": "role alias",
              "description": desc}
D.setdefault("focus", {})["ua"] = {"value": "{color.accent.focus}", "type": "color", "source": "role alias",
    "description": "#005fcc: the UA keyboard focus ring on marketing links (1px auto outline, 1px offset)."}

# --------------------------------------------------------- typography set
# Composite styles (DTCG typography leaves) over the ramp; the app shell's
# measured steps sit beside the declared marketing ramp. DESIGN.md reads
# core.typography, so the composites live in core.

typ = SPEC["core"].setdefault("typography", {})
def style(font, fz, lh, fw, ls, src, desc):
    return {"$value": {"fontFamily": font, "fontSize": fz, "lineHeight": lh,
                       "fontWeight": fw, "letterSpacing": ls},
            "$type": "typography",
            "$extensions": {"source": src},
            "$description": desc}

FAM = "{font.family.sans}"
if "--text-title-primary" in R:
    typ["title-primary"] = style(FAM, "{font.size.title-primary}", "{font.lineHeight.title-primary}",
                                 "{font.weight.title-primary}", "{font.tracking.title}",
                                 "declared --text-title-primary composite (raw/css-vars.json)",
                                 "Hero, section and newsletter titles: 42/46, 500, -0.03em.")
if "--text-title-secondary" in R:
    typ["title-secondary"] = style(FAM, "{font.size.title-secondary}", "{font.lineHeight.title-secondary}",
                                   "{font.weight.title-secondary}", "{font.tracking.title}",
                                   "declared --text-title-secondary composite (raw/css-vars.json)",
                                   "Sub-heads and the mobile hero: 24/26, 500, -0.03em.")
if "--text-subtitle" in R:
    typ["subtitle"] = style(FAM, "{font.size.subtitle}", "{font.lineHeight.subtitle}",
                            "{font.weight.medium}", "normal",
                            "declared --text-subtitle composite (raw/css-vars.json)",
                            "18/20 subtitle step.")
if "--text-body-primary" in R:
    typ["body"] = style(FAM, "{font.size.body-primary}", "{font.lineHeight.body-primary}",
                        "{font.weight.regular}", "normal",
                        "declared --text-body-primary composite (raw/css-vars.json)",
                        "14/18 lede, footer and consent text.")
if "--text-body-secondary" in R:
    typ["label"] = style(FAM, "{font.size.body-secondary}", "{font.lineHeight.body-secondary}",
                         "{font.weight.medium}", "normal",
                         "declared --text-body-secondary composite (raw/css-vars.json)",
                         "12/14 pill buttons and small labels.")
for key, fz, lh, fw, ls, src, desc in [
    ("price", "{font.size.price}", "{font.lineHeight.price}", "{font.weight.title-primary}", "{font.tracking.price}",
     "computed text style of plan-price default", "42/42 price figure."),
    ("login-title", "{font.size.login-title}", "{font.lineHeight.login-title}", "{font.weight.medium}", "normal",
     "computed text style of login-title default", "23/25 app card title."),
    ("legal-title", "{font.size.legal-title}", "{font.lineHeight.legal-title}", "{font.weight.legal}", "normal",
     "computed text style of legal-title default", "42/40 legal document title."),
    ("toggle", "{font.size.toggle}", "{font.lineHeight.toggle}", "{font.weight.medium}", "{font.tracking.tight}",
     "computed text style of billing-yearly default", "16/24 billing toggle."),
    ("login-label", "{font.size.login-body}", "{font.lineHeight.login-body}", "{font.weight.login-label}", "{font.tracking.login-label}",
     "computed text style of login-field default", "14/15 app labels and fields."),
    ("login-small", "{font.size.login-small}", "{font.lineHeight.login-small}", "{font.weight.login-label}", "normal",
     "computed text style of login-forgot default", "12/13 app helper text."),
    ("chip", "{font.size.chip}", "{font.lineHeight.chip}", "{font.weight.medium}", "normal",
     "computed text style of plan-chip default", "14/35 plan chip label."),
]:
    typ[key] = style(FAM, fz, lh, fw, ls, src + " (raw/components-computed.json)", desc)

# ---------------------------------------------------------------- component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "nav-cta", "default", "height", "35px nav pill buttons."),
    ("button-lg.height", "hero-cta", "default", "height", "36px marketing CTAs."),
    ("button-mobile.height", "m-cta", "default", "height", "38px mobile CTA."),
    ("button-app.height", "send-code", "default", "height", "35px app buttons."),
    ("field.height", "login-field", "default", "height", "35px app fields."),
    ("field-news.height", "news-field", "default", "height", "35px newsletter field."),
    ("chip.height", "plan-chip", "default", "height", "35px plan chips."),
    ("pill.height", "save-pill", "default", "height", "25px save pill."),
    ("signin.height", "legal-signin", "default", "height", "40px legal sign-in pill."),
    ("carousel.size", "carousel-prev", "default", "width", "40px round carousel arrows."),
    ("consent.size", "news-consent", "default", "width", "18px consent checkbox."),
    ("thumb.size", "asset-thumb", "default", "width", "144px asset thumbnails."),
    ("logo.height", "logo", "default", "height", "40px logo block."),
    ("header.height", "header", "default", "height", "80px sticky header."),
    ("card-plan.width", "plan-card", "default", "width", "357px plan card column."),
    ("card-login.width", "login-card", "default", "width", "450px login card."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# Component colour/geometry tokens (DESIGN.md reads bg/text/radius/padding/height).
def comp_leaf(group, key, ty, val, src, desc):
    comp.setdefault(group, {})[key] = {"type": ty, "value": val, "source": src, "description": desc}

# The white marketing pills split on hover: the plan/team card CTAs grey to
# #c4c4c4 keeping dark text, the newsletter submit softens to white/85, and the
# header's Start-for-free pill inverts to #373737 with white text. One generic
# `button` group would publish the plan behaviour for the other two.
if have("plan-cta", "hover"):
    comp_leaf("button", "bg", "color", "{action.bg}", "role alias", "White plan/team card pill (plan-cta, team-cta).")
    comp_leaf("button", "text", "color", "{action.fg}", "role alias", "Dark ink on the white pills.")
    comp_leaf("button", "bg-hover", "color", "{action.bg-hover}", "role alias", "#c4c4c4 hover on the white card pills.")
    comp_leaf("button", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded.")
    comp_leaf("button", "padding", "dimension", "{spacing.control-x}", "role alias", "20px inline padding.")
if have("nav-cta", "hover"):
    comp_leaf("button-nav", "bg", "color", "{action.bg}", "role alias", "The header's white Start-for-free pill.")
    comp_leaf("button-nav", "text", "color", "{action.fg}", "role alias", "Dark ink at rest.")
    comp_leaf("button-nav", "bg-hover", "color", "{action.nav-bg-hover}", "role alias", "#373737 hover: the nav pill inverts dark, unlike the card pills.")
    comp_leaf("button-nav", "text-hover", "color", "{action.nav-fg-hover}", "role alias", "#fff hover text on the nav pill.")
    comp_leaf("button-nav", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded.")
    comp_leaf("button-nav", "padding", "dimension", "{spacing.control-x}", "role alias", "20px inline padding.")
if have("news-submit", "hover"):
    comp_leaf("button-news", "bg", "color", "{action.bg}", "role alias", "White newsletter submit pill.")
    comp_leaf("button-news", "text", "color", "{action.fg}", "role alias", "Dark ink on the submit.")
    comp_leaf("button-news", "bg-hover", "color", "{action.bg-hover-soft}", "role alias", "85% white hover on the submit.")
    comp_leaf("button-news", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded.")
    comp_leaf("button-news", "padding", "dimension", "{spacing.control-x}", "role alias", "20px inline padding.")
if have("hero-cta", "default"):
    comp_leaf("button-accent", "bg", "color", "{accent.pink}", "role alias", "Pink hero CTA.")
    comp_leaf("button-accent", "bg-hover", "color", "{accent.pink-hover}", "role alias", "#ff4bc4 hover.")
    comp_leaf("button-accent", "text", "color", "{text.on-accent}", "role alias", "White on pink.")
    comp_leaf("button-accent", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded.")
if have("edu-cta", "default"):
    comp_leaf("button-edu", "bg", "color", "{accent.blue}", "role alias", "Blue education CTA.")
    comp_leaf("button-edu", "bg-hover", "color", "{accent.blue-hover}", "role alias", "#5a65ff hover.")
    comp_leaf("button-edu", "text", "color", "{text.on-accent}", "role alias", "White on blue.")
    comp_leaf("button-edu", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded.")
if have("send-code", "default"):
    comp_leaf("button-app", "bg", "color", "{action.app-bg}", "role alias", "#efefef app button.")
    comp_leaf("button-app", "bg-hover", "color", "{action.app-bg-hover}", "role alias", "90% ink hover.")
    comp_leaf("button-app", "text", "color", "#000000", "computed color of send-code default (raw/components-computed.json)", "Black text on the app button.")
    comp_leaf("button-app", "radius", "dimension", "{radius.base}", "role alias", "10px app radius.")
if have("login-field", "default"):
    comp_leaf("field", "bg", "color", "{surface.field}", "role alias", "#1e1e1e app field.")
    comp_leaf("field", "text", "color", "{text.app}", "role alias", "#efefef field text.")
    comp_leaf("field", "border", "color", "{border.field}", "role alias", "#2a2a2a field border.")
    comp_leaf("field", "border-focus", "color", "{border.field-focus}", "role alias", "#373737 focused border.")
    comp_leaf("field", "radius", "dimension", "{radius.base}", "role alias", "10px app radius.")
    comp_leaf("field", "padding", "dimension", "{spacing.field-x}", "role alias", "15px inline padding.")
if have("news-field", "default"):
    comp_leaf("field-pill", "bg", "color", "{surface.field}", "role alias", "#1e1e1e newsletter field.")
    comp_leaf("field-pill", "text", "color", "{text.primary}", "role alias", "#fff field text.")
    comp_leaf("field-pill", "radius", "dimension", "{radius.pill}", "role alias", "Fully rounded pill field.")
    comp_leaf("field-pill", "padding", "dimension", "{spacing.control-x}", "role alias", "20px inline padding.")
if have("plan-card", "default"):
    comp_leaf("card", "bg", "color", "{surface.card}", "role alias", "#121212 plan card.")
    comp_leaf("card", "bg-hover", "color", "{surface.card-hover}", "role alias", "#1d1d1d card hover.")
    comp_leaf("card", "border", "color", "{border.card}", "role alias", "#222 hairline ring.")
    comp_leaf("card", "radius", "dimension", "{radius.card}", "role alias", "33px card radius.")
    comp_leaf("card", "padding", "dimension", "{spacing.card}", "role alias", "15px card padding.")
if have("social-card", "default"):
    comp_leaf("card-social", "bg", "color", "{surface.inset}", "role alias", "#080808 testimonial card.")
    comp_leaf("card-social", "border", "color", "{color.neutral.grey-1}", "role alias", "#373737 inset ring (a box-shadow ring, not a border).")
    comp_leaf("card-social", "radius", "dimension", "{radius.fill}", "role alias", "12px fill radius on the testimonial card.")
if have("login-card", "default"):
    comp_leaf("card-app", "bg", "color", "{surface.veil}", "role alias", "5% ink veil login card.")
    comp_leaf("card-app", "radius", "dimension", "{radius.login}", "role alias", "20px login card radius.")
    comp_leaf("card-app", "padding", "dimension", "{spacing.login-card}", "role alias", "50px login card padding.")

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
