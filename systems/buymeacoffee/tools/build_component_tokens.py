#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

buymeacoffee.com paints two public frontends signed out — the Nuxt marketing
pages (home/faq/reviews/blog/brand/about, Circular faces on a #faf8f0 cream
field) and the Vite-built creator page and login card (/cara.app, /login —
Tailwind utilities on white, themed per creator by inline --theme-color* vars).
Neither declares a design-token layer: the harvested sheets carry only three
layout vars on :root (--header-height, --auth-header-height, --footer-height),
the --vc-* carousel vars and Tailwind internals, so the tokens are **measured
computed styles** from raw/components-computed.json plus the inline
--theme-color* declarations read off the live DOM:

  light       #222 ink on the #faf8f0 marketing field and white creator/login
              fields; #f0f0f0 input fills; rgba(34,34,34,.05) hover pills;
              #e5e5e5/#e5e7eb hairlines; #717171 secondary text
  brand       the #ffdd00 yellow button paint (::before layers, hover #ffc800)
  theme       the per-creator accent set declared inline on the page root —
              #ff813f support buttons/tab/fields, #ff6b1c hover, the 5/8/10/25%
              tints — sampled from /cara.app
  fonts       Circular Bold (display/nav/buttons), Circular Regular (body),
              Circular Medium (nav/labels), Circular Book (fields), Borel
              Regular (FAQ title script); the Vite app's own widgets sit on the
              ui-sans-serif stack
  ramp        measured 96/64/48/24/22/20/18/17/16/15px steps
  shape       9999px pills everywhere buttons live, a 40px ::before pill on the
              marketing bmc-btns, 12px fields and dropdowns, 24px cards, 16px
              creator tiles, 10px menu rows, 8px tabs, 6px checkboxes
  states      the Vite app's #2563eb 4px ring (Tailwind ring-blue-600) over a
              2px white offset, the marketing links' Chromium auto outline,
              the 0.075-0.25s field/tab transitions, the 0.3s mobile-menu slide

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py — only the
three :root layout vars qualify) or {"value": ..., "source": "..."} for a
measured value. Every surface paints light-only, so only the light set is
populated.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def current(comp):
    """The component's entry, refused when the last run did not read it: missing
    (no states) or recaptureMissed (earlier states kept under their own
    provenance) is not a current reading, so it cannot source a role."""
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(f"{comp}: not a current reading (missing or recaptureMissed)")
    return c
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
# The inline --theme-color* set a creator page paints (read off live elements).
INLINE = {}
for row in V.get("inline", []):
    for n, v in (row.get("properties") or {}).items():
        INLINE.setdefault(n, {"value": v, "on": row.get("on", ""), "page": row.get("page", "")})


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def val(v, ty, src, desc):
    return {"value": v, "type": ty, "source": src, "description": desc}


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. buymeacoffee.com "
    "declares no design-token layer beyond three :root layout vars "
    "(raw/css-vars.json), so the light set is built from measured computed "
    "styles (raw/components-computed.json) plus the inline --theme-color* "
    "accent set a creator page declares on its root element."),
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


def paint_radius(comp, state):
    try:
        return next((n.get("radius") for n in C[comp]["states"][state].get("paint", [])
                     if n.get("radius") and n["radius"] not in ("0px", "0")), None)
    except KeyError:
        return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("bold", "hero-title", "default", "Circular Bold — display type, headings, buttons and bold menu rows."),
    ("regular", "hero-sub", "default", "Circular Regular — body and tagline copy."),
    ("medium", "nav-link", "default", "Circular Medium — nav links, labels, tabs and field text."),
    ("book", "c-name", "default", "Circular Book — the Vite app's field and menu text."),
    ("borel", "f-h1", "default", "Borel Regular — the script display accent (FAQ title, Wall-of-love heart)."),
]:
    v = ts(comp, state, "fontFamily") or (have(comp, state, "fontFamily") and st(comp, state)["fontFamily"])
    if v:
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
if have("c-header", "default", "fontFamily"):
    fam["app"] = {"value": st("c-header", "default")["fontFamily"], "type": "fontFamily",
                  "source": "computed fontFamily of c-header default — the element's own stack, not its text's (raw/components-computed.json)",
                  "description": "The Vite creator/login app's base stack (ui-sans-serif first); widgets that set no face fall through to it."}
for face in ("Circular Black",):
    if any(face in (f.get("font-family") or "") for f in V.get("fonts", [])):
        key = face.split()[-1].lower()
        fam[key] = {"value": f'"{face}"', "type": "fontFamily",
                    "source": "declared @font-face in the harvested buymeacoffee.com sheets (raw/css-vars.json fonts); not painted on a captured component",
                    "description": f"{face} — declared face; heaviest weight of the marketing family."}

# ---------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-title", "default", "color", "The #222 ink on headings, body text and button labels."),
    ("ink-v2", "c-name", "default", "color", "The #151515 ink the Vite app paints in its fields."),
    ("grey", "section-eyebrow", "default", "color", "The #717171 grey on section eyebrows and secondary copy."),
    ("cream", "page-field", "default", "backgroundColor", "The #faf8f0 cream field the marketing pages paint on."),
    ("field", "l-email", "default", "backgroundColor", "The #f0f0f0 input fill on the login card and support widget."),
    ("divider", "l-social", "default", "borderTopColor", "The #e5e5e5 hairline on the social buttons and divider."),
]:
    try:
        v = ts(comp, state, prop) if prop in ("color", "fontSize") else st(comp, state).get(prop)
        v = norm_color(v)
        if v and v != "transparent" and not v.startswith("rgba(0, 0, 0, 0)"):
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass
for key, comp, state, desc in [
    ("hover-fill", "nav-link", "hover", "The 5%-black pill a marketing nav link paints on hover (::before)."),
    ("search-fill", "nav-search", "default", "The 3%-black field the Search-creators pill paints."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and not v.startswith("#"):
        neutral[key] = {"value": v, "type": "color",
                        "source": f"painted layer under {comp} {state} (raw/components-computed.json)",
                        "description": desc}
_paper = {norm_color(current(c)["states"]["default"]["style"].get("backgroundColor", "")) for c in ("c-widget", "c-header", "r-tweet")}
if len(_paper) != 1:
    raise ValueError(f"paper: readings differ: {sorted(_paper)}")
neutral["paper"] = {"value": _paper.pop(), "type": "color",
                    "source": "computed backgroundColor of c-widget / c-header / r-tweet on /cara.app (raw/components-computed.json)",
                    "description": "The white creator-page field, cards and dropdowns."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, desc in [
    ("yellow", "nav-cta", "default", "The #ffdd00 yellow pill paint (::before) on every marketing bmc-btn and the login CTA."),
    ("yellow-hover", "l-cta", "hover", "The #ffc800 the yellow paint deepens to on hover."),
]:
    v = norm_color(painted(comp, state) or "")
    if v:
        brand[key] = {"value": v, "type": "color",
                      "source": f"painted layer under {comp} {state} (raw/components-computed.json)",
                      "description": desc}

# The per-creator accent set, declared inline as --theme-color* on the page
# root and repainted into the widget, tabs, pills and buttons.
theme = SPEC["core"].setdefault("color", {}).setdefault("theme", {})
for key, vname, comp, state, prop, desc in [
    ("accent", "--theme-color", "c-support", "default", "paint", "The per-creator accent (#ff813f on /cara.app) on the Support button, quantity pills, active tab and field focus."),
    ("accent-hover", "--theme-color-hover-color", "c-support", "hover", "paint", "The accent's hover step (#ff6b1c on /cara.app)."),
    ("accent-25", "--theme-color-25", "c-qty-off", "default", "borderTopColor", "The 25%-accent tint on unchecked pill borders."),
    ("on-accent", "--theme-text-color", "c-qty-on", "default", "color", "The text colour generated against the accent (white here)."),
]:
    if vname in INLINE:
        v = norm_color(INLINE[vname]["value"])
        theme[key] = {"value": v, "type": "color",
                      "source": f"inline {vname} declared on {INLINE[vname]['on']} at {INLINE[vname]['page']} (raw/css-vars.json inline){'; cross-checked against ' + prop + ' of ' + comp + ' ' + state if have(comp, state, prop) else ''}",
                      "description": desc}
for key, vname, desc in [
    ("accent-05", "--theme-color-05", "The 5%-accent tint (hover fills)."),
    ("accent-08", "--theme-color-08", "The 8%-accent tint (hover fills)."),
    ("accent-10", "--theme-color-1", "The 10%-accent tint (selected fills)."),
]:
    if vname in INLINE:
        theme[key] = {"value": norm_color(INLINE[vname]["value"]), "type": "color",
                      "source": f"inline {vname} declared on {INLINE[vname]['on']} at {INLINE[vname]['page']} (raw/css-vars.json inline)",
                      "description": desc}

focus = SPEC["core"].setdefault("color", {}).setdefault("focus", {})
try:
    sh = next((n.get("shadow") for n in C["c-qty-on"]["states"]["focus-visible"].get("paint", []) if n.get("shadow") and "rgb(37" in n["shadow"]), None)
    m = sh and re.search(r"rgb\(37,\s*99,\s*235\)", sh)
    if m:
        focus["ring"] = {"value": "#2563eb", "type": "color",
                         "source": "painted boxShadow under c-qty-on focus-visible (raw/components-computed.json)",
                         "description": "The Tailwind blue-600 focus ring the Vite app draws (4px ring over a 2px white offset)."}
except KeyError:
    pass
try:
    outl = next((n.get("outline") for n in C["nav-link"]["states"]["focus-visible"].get("paint", []) if n.get("outline")), None)
    m = outl and re.search(r"rgb\(0,\s*95,\s*204\)", outl)
    if m:
        focus["browser"] = {"value": "#005fcc", "type": "color",
                            "source": "painted outline under nav-link focus-visible (raw/components-computed.json)",
                            "description": "Chromium's 1px auto outline the marketing links keep (no custom ring declared)."}
except KeyError:
    pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "{color.neutral.ink}", "Body, heading and button-label ink."),
    ("--text-secondary", "{color.neutral.grey}", "Eyebrow and secondary copy."),
    ("--surface-page", "{color.neutral.cream}", "The marketing page field."),
    ("--surface-card", "{color.neutral.paper}", "Cards, the creator field, dropdowns and panels."),
    ("--surface-field", "{color.neutral.field}", "Input fills."),
    ("--action-primary", "{color.brand.yellow}", "The yellow pill paint on marketing and login CTAs."),
    ("--action-accent", "{color.theme.accent}", "The per-creator accent on the creator page."),
    ("--text-on-action", "{color.neutral.ink}", "Text on the yellow pills."),
    ("--text-on-accent", "{color.theme.on-accent}", "Text on the accent paint."),
    ("--border-field", "{color.neutral.divider}", "Hairlines on social buttons and dividers."),
    ("--focus-ring", "{color.focus.ring}", "The #2563eb ring the Vite app draws on focus."),
]:
    emit(light, name, {"value": target, "type": "color", "source": ALIAS, "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The 96px marketing display (Fund your creative work)."),
    ("h2", "section-h2", "default", "The 64px section headings."),
    ("faq-title", "f-h1", "default", "The 48px Borel page title (FAQ, Wall of love)."),
    ("display-mobile", "m-hero", "default", "The display size at 390px."),
    ("lede", "section-lede", "default", "The 24px section lede / widget title."),
    ("tagline", "hero-sub", "default", "The 22px hero tagline."),
    ("question", "f-q", "default", "The 20px FAQ question / mobile menu item."),
    ("body", "f-a", "default", "The 18px FAQ answer body."),
    ("button", "l-cta", "default", "The 17px Vite-app button / field size."),
    ("base", "header", "default", "The 16px base size (nav, body, menu rows)."),
    ("tab", "c-tab", "default", "The 15px profile-tab size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "Tight display leading (~0.99x)."),
    ("h2", "section-h2", "default", "Section-heading leading (1.25x)."),
    ("lede", "section-lede", "default", "Lede leading."),
    ("tagline", "hero-sub", "default", "Tagline leading (1.5x)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The -2.4px display tracking."),
    ("h2", "section-h2", "default", "The -2px heading tracking."),
    ("eyebrow", "section-eyebrow", "default", "The +2px eyebrow tracking (uppercase)."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        tracking[key] = {"type": "dimension", "value": v,
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "c-qty-on", "default", "borderTopLeftRadius", "The 9999px pill on quantity buttons, the Support/Join buttons and the Vite CTA."),
    ("bmc-pill", "nav-cta", "default", "paint-radius", "The 40px pill the marketing bmc-btn paints as its ::before layer."),
    ("field", "l-email", "default", "borderTopLeftRadius", "The 12px field radius (inputs, textarea, custom-amount box)."),
    ("panel", "nav-dropdown", "default", "borderTopLeftRadius", "The 12px dropdown/panel radius."),
    ("card", "r-tweet", "default", "borderTopLeftRadius", "The 24px card radius (tweet cards, the support widget)."),
    ("tile", "creator-card", "default", "borderTopLeftRadius", "The 16px hero creator-tile radius."),
    ("item", "menu-link", "default", "borderTopLeftRadius", "The 10px menu-row radius."),
    ("tab", "c-tab", "default", "borderTopLeftRadius", "The 8px tab/search field radius."),
    ("check", "c-monthly", "default", "paint-radius", "The 6px checkbox radius."),
]:
    if prop == "paint-radius":
        pr = paint_radius(comp, state)
        if pr:
            radius[key] = {"value": pr, "type": "dimension",
                           "source": f"painted layer radius under {comp} {state} (raw/components-computed.json)",
                           "description": desc}
        continue
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ---------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
SH_RE = re.compile(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)")


def layers(v):
    return [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp}
            for a, x, y, bl, sp in SH_RE.findall(v or "")
            if not a.startswith("rgba(0, 0, 0, 0)")]


for key, comp, state, desc in [
    ("menu", "nav-dropdown", "default", "The three-layer dropdown shadow (2px hairline + 40px bloom + 5px contact)."),
    ("card", "r-tweet", "default", "The 4px card shadow on tweet cards."),
    ("header", "c-header", "default", "The 1px line the sticky creator header casts."),
]:
    try:
        ls = layers(st(comp, state).get("boxShadow"))
        if ls:
            shadow[key] = {"value": ls, "type": "shadow",
                           "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass
try:
    ls = layers(next((n.get("shadow") for n in C["c-qty-on"]["states"]["focus-visible"].get("paint", []) if n.get("shadow")), ""))
    if ls:
        shadow["focus-ring"] = {"value": ls, "type": "shadow",
                                "source": "painted boxShadow under c-qty-on focus-visible (raw/components-computed.json)",
                                "description": "The focus treatment every Vite-app control draws: a 2px white offset under a 4px #2563eb ring."}
except KeyError:
    pass

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, desc in [
    ("tab-transition", "c-tab", "default", "The 0.2s transition on the profile tabs."),
    ("field-transition", "l-email", "default", "The 0.075s fill/border change on the login fields."),
    ("widget-field-transition", "c-name", "default", "The 0.25s transition on the widget fields."),
    ("menu-transition", "m-menu-open", "default", "The 0.3s slide of the mobile menu panel."),
    ("card-transition", "creator-card", "default", "The 0.2s float on the hero creator tiles."),
    ("tweet-transition", "r-tweet", "default", "The 0.1s lift on the tweet cards."),
    ("reveal-transition", "section-h2", "default", "The 0.8s scroll-reveal on marketing sections."),
]:
    try:
        s = st(comp, state)
        first = (s.get("transitionDuration") or "").split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s.get('transitionProperty', 'all')[:60]})"}
    except (KeyError, TypeError):
        pass
# the tweet card lifts ~3% on hover
try:
    d0 = C["r-tweet"]["states"]["default"]["rect"]["w"]
    dh = C["r-tweet"]["states"]["hover"]["rect"]["w"]
    if d0 and dh and dh > d0:
        meas["card-hover-scale"] = {"value": round(dh / d0, 4), "type": "number",
                                    "source": "hover rect / default rect of r-tweet (raw/components-computed.json)",
                                    "description": "The ~1.03 scale a tweet card takes on hover."}
except KeyError:
    pass
# the login CTA's yellow deepens on hover; the creator accent darkens on hover
for key, comp, desc in [
    ("bmc-pill-hover-scale", "nav-cta", "The bmc-btn ::before grows slightly on hover (~1.02x/1.04x)."),
]:
    try:
        d0 = C[comp]["states"]["default"]["rect"]["w"]
        dh = C[comp]["states"]["hover"]["rect"]["w"]
        if d0 and dh and dh != d0:
            meas[key] = {"value": round(dh / d0, 4), "type": "number",
                         "source": f"hover rect / default rect of {comp} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "nav-cta", "default", "height", "The marketing button/pill height."),
    ("hero-cta.height", "hero-cta", "default", "height", "The hero Start-my-page pill height."),
    ("button.height", "l-cta", "default", "height", "The Vite-app primary button height."),
    ("field.height", "l-email", "default", "height", "The login/widget field height."),
    ("qty.height", "c-qty-on", "default", "height", "The quantity pill's square size."),
    ("tab.height", "c-tab", "default", "height", "A profile tab's height."),
    ("slide.size", "r-slide", "default", "height", "The square carousel button size."),
    ("header.height", "header", "default", "height", "The marketing header height."),
    ("header.height-mobile", "m-header", "default", "height", "The marketing header at 390px."),
    ("creator-header.height", "c-header", "default", "height", "The sticky creator-page header height."),
    ("widget.width", "c-widget", "default", "width", "The support widget's width on the creator page."),
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
