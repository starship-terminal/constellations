#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

endel.io and app.endel.io are Next.js builds; their bundles declare named
custom properties on :root (raw/css-vars.json, read by tools/capture/vars.mjs
through the CSSOM on the live pages and re-parsed in a probe document per
host):

  --color-black, --color-gray-1..5, --color-white   the neutral ramp the whole
                                                    product is painted in
  --color-green, --color-orange                     declared accents (never
                                                    painted on the captured
                                                    signed-out routes)
  --color-accent-green(-hover)                      app.endel.io's two extra
                                                    accent greens (same)
  --color-gradient-1                                a #181818 -> transparent
                                                    scrim, kept as a var note
  --max-width, --gutter, --gap, --max-cols, --cols-1..12
                                                    the 12-column grid the
                                                    layout is built on
                                                    (1280px page, 64px
                                                    gutters, 24px gaps)
  --title-h1..h4, --line-height-h1..h4              the display scale
  --text-1..5, --line-height-text-1..5              the text scale

The grid evidence lines up: a soundscape card is exactly --cols-3 (270px),
the footer field --cols-5 (466px), the login card --cols-6 (564px), a
soundscape row or carousel banner --cols-10 (956px) and an accordion row
--cols-12 (1152px).

A leaf is {"var": "--name"} (resolved per host by build_tokens.py) or
{"value": ..., "source": ...} for a measured value. Everything the site
paints is one dark theme, so the semantic set is emitted under `dark` and no
light set exists.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
COMP = C["components"]
R = {n: v.get("value", v.get("raw")) for s in ("site", "app") for n, v in V["resolved"][s].items()}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. endel.io and "
    "app.endel.io declare named :root vars (a neutral ramp, two declared "
    "accents the signed-out pages never paint, the 12-column grid and the "
    "apercuPro type scale); \"var\" leaves resolve through those "
    "declarations, \"value\" leaves are measured computed styles. Both hosts "
    "paint one dark theme, so the semantic set lands in `dark`."),
    "core": {}, "dark": {}, "component": {}}

# ------------------------------------------------------------- core palette

for path, var, desc in [
    ("color.neutral.black", "--color-black", "The pure black every page paints on (#000, body's own fill and the header scrim's base)."),
    ("color.neutral.800", "--color-gray-1", "#191919: card fills (accordion rows, the mini-player pill, the timer sheet) and the footer hairline."),
    ("color.neutral.700", "--color-gray-2", "#262626: the default fill of every button and pill (Try Today, Sign In, Continue, OAuth, the scenario pills)."),
    ("color.neutral.500", "--color-gray-3", "#808080: field borders, the hover/pressed fill of gray-2 buttons, the link focus ring, the volume track's empty half."),
    ("color.neutral.300", "--color-gray-4", "#bfbfbf: muted text (footer headings and legal links, the accordion answer, the mini-player's time)."),
    ("color.neutral.200", "--color-gray-5", "#e0e0e0: the lightest grey, the FREEMIUM account chip's label."),
    ("color.neutral.white", "--color-white", "#fff: text, strong borders (focused fields, the Unlock and Continue borders), the play button's fill."),
    ("color.accent.green", "--color-green", "#82d133, declared on both hosts' :root; nothing on the captured signed-out routes paints it."),
    ("color.accent.orange", "--color-orange", "#ff7a00, declared on both hosts' :root; nothing on the captured signed-out routes paints it."),
    ("color.accent.bright", "--color-accent-green", "#58ff5d, declared on app.endel.io's :root only; nothing on the captured signed-out routes paints it."),
    ("color.accent.brightHover", "--color-accent-green-hover", "#3ee843, the hover state of --color-accent-green, declared on app.endel.io's :root only."),
]:
    node, last = descend(SPEC["core"], path.split("."))
    node[last] = {"var": var, "type": "color", "description": desc}
    if var not in R:
        raise SystemExit(f"{var} not in resolved css-vars")


def st(comp, state):
    c = COMP[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """`styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth painted child
    layer) or `ancestors.N.prop`, or the special `ringShadow`: the colour of
    the `0 0 0 Npx` ring layer in the element's own boxShadow (the product's
    focus ring is a spread shadow, not an outline)."""
    d = COMP[comp]["states"][state]
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and (prop.endswith(".border") or prop.endswith(".outline")):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "var" in v:
            BY_VALUE.setdefault(norm_color(R[v["var"]]), prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"].setdefault("color", {}), "color.")


def role(path, comp, state, prop, desc):
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    node = SPEC["dark"]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


for path, comp, state, prop, desc in [
    ("page", "page-ground", "default", "backgroundColor", "The pure black every captured route paints on (body's own fill)."),
    ("text", "hero-title", "default", "color", "The display type's white; all captured text is white or a grey."),
    ("muted", "footer-legal", "default", "textStyle.color", "Secondary text: footer legal links, accordion answers, the mini-player's time (#bfbfbf on the text node)."),
    ("faint", "app-header", "default", "textStyle.color", "The lightest text grey, the FREEMIUM account chip's label (#e0e0e0)."),
    ("surface", "accordion-title", "default", "backgroundColor", "The card fill, #191919 (accordion rows, the mini-player pill, the timer sheet)."),
    ("surfaceRaised", "btn-signin", "default", "backgroundColor", "The control fill, #262626 (every button and pill at rest)."),
    ("fillHover", "btn-signin", "hover", "backgroundColor", "The hover and pressed fill of gray-2 controls, #808080."),
    ("border", "input-email-login", "default", "borderTopColor", "The resting field border, #808080."),
    ("borderStrong", "input-email-login", "focused", "borderTopColor", "The focused-field and primary-action border, pure white."),
    ("borderSubtle", "footer", "default", "paint.2.border", "The 1px hairline under the footer columns, #191919."),
    ("bar", "player-header", "default", "paint.0.bg", "The player header's inner bar, #2b2b2b, a grey between gray-2 and gray-3 that no var names."),
    ("scrim", "timer-dialog", "opened", "backgroundColor", "The modal overlay, rgba(0,0,0,0.8), behind the timer sheet."),
    ("focus", "btn-signin", "focus-visible", "ringShadow", "The keyboard focus ring's colour #666666, painted as a 6px spread shadow (the UA outline is suppressed)."),
    ("chipOutline", "banner", "default", "paint.0.outline", "The carousel banner's inset outline, rgba(255,255,255,0.15)."),
    ("onAccent", "banner", "default", "textStyle.color", "Text on a white fill inside the banner (the SPECIAL OFFER tag chip), black."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- type scale and the grid

for path, var, ty, desc in [
    ("font.size.h1", "--title-h1", "dimension", "60px display size (the Endel wordmark hero)."),
    ("font.size.h2", "--title-h2", "dimension", "44px section titles."),
    ("font.size.h3", "--title-h3", "dimension", "36px smaller headings — also the mobile display size (m-hero-title computes 36px)."),
    ("font.size.h4", "--title-h4", "dimension", "28px minor headings and the player title."),
    ("font.size.text1", "--text-1", "dimension", "22px lead text and big links/buttons (nav items, Try Now, button labels)."),
    ("font.size.text2", "--text-2", "dimension", "18px secondary links (Learn More, footer links)."),
    ("font.size.text3", "--text-3", "dimension", "16px base text and small button labels (header buttons)."),
    ("font.size.text4", "--text-4", "dimension", "14px muted labels (footer headings, mini-player meta)."),
    ("font.size.text5", "--text-5", "dimension", "10px microtext."),
    ("font.lineHeight.h1", "--line-height-h1", "dimension", "72px on the 60px display size."),
    ("font.lineHeight.h2", "--line-height-h2", "dimension", "56px on h2."),
    ("font.lineHeight.h3", "--line-height-h3", "dimension", "42px on h3."),
    ("font.lineHeight.h4", "--line-height-h4", "dimension", "36px on h4."),
    ("font.lineHeight.text1", "--line-height-text-1", "dimension", "28px on the 22px text."),
    ("font.lineHeight.text2", "--line-height-text-2", "dimension", "24px on the 18px text."),
    ("font.lineHeight.text3", "--line-height-text-3", "dimension", "24px on the 16px text."),
    ("font.lineHeight.text4", "--line-height-text-4", "dimension", "20px on the 14px text."),
    ("font.lineHeight.text5", "--line-height-text-5", "dimension", "14px on the 10px microtext."),
    ("layout.container", "--max-width", "dimension", "The 1280px page column."),
    ("layout.gutter", "--gutter", "dimension", "The 64px side gutter inside the 1280px column."),
    ("layout.gap", "--gap", "dimension", "The 24px grid gap."),
    ("layout.cols", "--max-cols", "number", "The 12-column grid."),
]:
    node, last = descend(SPEC["core"], path.split("."))
    node[last] = {"var": var, "type": ty, "description": desc}
    if var not in R:
        raise SystemExit(f"{var} not in resolved css-vars")

for i in range(1, 13):
    node, last = descend(SPEC["core"], f"layout.col.{i}".split("."))
    node[last] = {"var": f"--cols-{i}", "type": "dimension",
                  "description": f"The width of {i} column{'s' if i > 1 else ''} at the 1280px container ({R.get(f'--cols-{i}')})."}

# ------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("page-ground", "default", "fontStack", "fontFamily", "apercuPro plus the metric-matched 'apercuPro Fallback' (a local Arial face with override descriptors), the stack every captured node uses."),
    ("hero-title", "default", "titleTracking", "letterSpacing", "The 0.35px tracking on the display sizes (h1-h3 share it)."),
    ("footer-link", "default", "linkHover", "color", "Links do not repaint on hover; the colour stays white."),
    ("btn-try", "hover", "glowColour", "boxShadow", "The Try Today button keeps its white 15px glow through hover."),
    ("volume", "default", "sliderBase", "color", "The volume slider's own colour #101010 (the track paints a white/gray-3 gradient over it)."),
    ("m-menu-button", "default", "mobileMenuLabel", "fontSize", "The 12px label on the mobile Menu button."),
]:
    try:
        v = stprop(comp, state, prop)
        if key == "glowColour":
            m = re.search(r"rgba?\([^)]*\)", v or "")
            v = m.group(0) if m else ""
        if key == "fontStack":
            meas[key] = {"value": v, "type": "fontFamily",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json); the apercuPro faces are @font-face declarations in the site and app bundles (fonts in raw/css-vars.json)",
                         "description": desc}
            continue
        if not v or v == "transparent":
            continue
        ty = "color" if re.match(r"rgba?\(|#", str(v)) else "dimension"
        meas[key] = {"value": norm_color(v) if ty == "color" else v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
    except KeyError:
        pass

# font.family.sans as a first-class token (the stack measured on the hero)
SPEC["core"].setdefault("font", {})
ff = SPEC["core"]["font"]
ff.setdefault("family", {})
ff["family"]["sans"] = meas.pop("fontStack")

# shadows: measured boxShadow strings parsed into DTCG layers
def shadow_layers(comp, state):
    sh = st(comp, state).get("boxShadow", "")
    layers = []
    for layer in re.split(r",(?![^(]*\))", sh):
        m = re.fullmatch(r"\s*(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s*", layer)
        if m:
            layers.append({"color": norm_color(m.group(1)), "offsetX": m.group(2), "offsetY": m.group(3),
                           "blur": m.group(4), "spread": m.group(5)})
        elif re.search(r"inset", layer):
            pass  # inset layers are recorded as measured colour tokens instead
    return layers


for comp, state, key, desc in [
    ("btn-try", "default", "glow", "The white 0 0 15px glow on the Try Today button (kept through hover and press)."),
    ("btn-signin", "focus-visible", "focusRing", "The product's keyboard focus ring on buttons: a #666666 6px spread shadow."),
    ("press-logo", "focus-visible", "focusRingLink", "The focus ring on plain links and tiles: a #808080 4px spread shadow."),
]:
    try:
        layers = shadow_layers(comp, state)
        if layers:
            SPEC["core"].setdefault("shadow", {})[key] = {
                "value": layers, "type": "shadow",
                "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# radius scale (measured; the bundle names the two button variants
# border-radius-basic (12px) and border-radius-full (100px))
for comp, state, key, prop, desc in [
    ("btn-try", "default", "basic", "borderTopLeftRadius", "The 12px corner of buttons, fields, accordion rows and the mobile menu button (the bundle's border-radius-basic)."),
    ("play-button", "default", "full", "paint.0.radius", "The 100px pill/circle corner (play and transport buttons, scenario pills, the mini-player pill; the bundle's border-radius-full)."),
    ("btn-explore", "default", "sheet", "paint.0.radius", "The 20px top corner of the player's bottom Explore sheet (20px 20px 0 0)."),
    ("banner", "default", "card", "borderTopLeftRadius", "The 24px corner of the explore carousel banner."),
    ("timer-dialog", "opened", "dialog", "paint.2.radius", "The 32px corner of the timer sheet."),
    ("banner-dot", "default", "round", "paint.0.radius", "The 50% carousel dot."),
]:
    try:
        v = stprop(comp, state, prop)
        if v:
            SPEC["core"].setdefault("radius", {})[key] = {
                "value": v.split()[0] if " " in str(v) else v, "type": "dimension",
                "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# motion: buttons transition background-color + border-color 0.2s ease;
# the player's sheets slide in/out 0.3s on the declared cubic-beziers.
dur = SPEC["core"].setdefault("duration", {})
dur["hover"] = {"value": "0.2s", "type": "duration",
                "source": "computed transitionDuration of btn-signin default (raw/components-computed.json)",
                "description": "The 200ms background/border transition on every button and accordion row."}
dur["sheet"] = {"value": "0.3s", "type": "duration",
                "source": "declared slide-in-out/slide-out transition in the app bundle's CSSOM (raw/components-computed.json _meta.sheets)",
                "description": "The 300ms slide of the timer sheet and the mobile menu."}
ease = SPEC["core"].setdefault("easing", {})
ease["standard"] = {"value": "ease", "type": "cubicBezier",
                    "source": "computed transitionTimingFunction of btn-signin default (raw/components-computed.json)",
                    "description": "Plain ease on the hover transitions."}
ease["sheetIn"] = {"value": "cubic-bezier(0.25, 0.46, 0.45, 0.94)", "type": "cubicBezier",
                   "source": "declared .slide-in-out-enter animation in the app bundle's CSSOM (raw/components-computed.json _meta.sheets)",
                   "description": "The sheet's entrance bezier."}
ease["sheetOut"] = {"value": "cubic-bezier(0.55, 0.085, 0.68, 0.53)", "type": "cubicBezier",
                    "source": "declared .slide-in-out-exit animation in the app bundle's CSSOM (raw/components-computed.json _meta.sheets)",
                    "description": "The sheet's exit bezier."}

# The header's painted scrim: black -> 65% black -> transparent (the
# --color-gradient-1 var is the similar #181818 -> transparent fade).
SPEC["core"]["gradient"] = {
    "headerScrim": {"type": "gradient",
                    "value": [{"color": "{color.neutral.black}", "position": 0},
                              {"color": "rgba(0, 0, 0, 0.65)", "position": 0.5},
                              {"color": "rgba(0, 0, 0, 0)", "position": 1}],
                    "source": "computed backgroundImage of header default (raw/components-computed.json)",
                    "description": "The fade the fixed header paints over scrolled content."},
    "declaredScrim": {"type": "gradient",
                      "value": [{"color": "#181818", "position": 0},
                                {"color": "rgba(0, 0, 0, 0)", "position": 1}],
                      "source": "declared --color-gradient-1 on :root (raw/css-vars.json); where it mounts was not identified on the captured routes",
                      "description": "The bundle's #181818-to-transparent fade."},
}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNav", "btn-try", "default", "rect.h", "Header buttons are 44px (Try Today, Sign In)."),
    ("control.height", "btn-set-timer", "default", "rect.h", "The 56px large controls (Set Timer, Continue, OAuth, scenario pills, transport buttons)."),
    ("control.heightMobile", "m-menu-button", "default", "rect.h", "The mobile Menu button is 36px."),
    ("control.border", "btn-set-timer", "default", "style.borderTopWidth", "Every button and field carries a 2px border (often painted its own fill colour)."),
    ("field.height", "input-email-login", "default", "rect.h", "The sign-in email field is 62px."),
    ("field.width", "input-email-login", "default", "rect.w", "The login field and card are 564px wide, exactly --cols-6."),
    ("footerField.width", "footer", "default", "paint.0.size", "The footer newsletter field is 466px wide, exactly --cols-5 (466x56)."),
    ("header.height", "header", "default", "rect.h", "The fixed header is 72px."),
    ("header.heightMobile", "m-header", "default", "rect.h", "The mobile header is 56px."),
    ("footer.height", "footer", "default", "rect.h", "The footer block at 1440px."),
    ("card.size", "soundscape-card", "default", "rect.w", "A soundscape card is 270px, exactly --cols-3."),
    ("row.width", "soundscape-row", "default", "rect.w", "A soundscape row (and the carousel banner) is 956px, exactly --cols-10."),
    ("accordion.width", "accordion-title", "default", "rect.w", "An FAQ row spans the full grid, 1152px = --cols-12."),
    ("play.size", "play-button", "default", "rect.w", "The round play control is 72px."),
    ("transport.size", "player-control", "default", "rect.w", "The player's transport buttons are 56px."),
    ("icon.size", "accordion-title", "default", "icon.w", "Row and chevron icons are 24px."),
    ("icon.sizeLg", "play-button", "default", "icon.w", "The play glyph is 36px."),
    ("dot.size", "banner-dot", "default", "rect.w", "Carousel dots are 12px."),
    ("volume.width", "volume", "default", "rect.w", "The volume slider is 129px wide, 5px tall."),
    ("mobileMenu.width", "m-menu-flyout", "default", "rect.w", "A promo row in the open mobile menu, 326px."),
]:
    try:
        if prop == "rect.w":
            v = "%gpx" % COMP[cname]["states"][state]["rect"]["w"]
        elif prop == "rect.h":
            v = "%gpx" % COMP[cname]["states"][state]["rect"]["h"]
        elif prop == "icon.w":
            v = "%gpx" % COMP[cname]["states"][state]["icon"]["w"]
        elif prop == "paint.0.size":
            v = COMP[cname]["states"][state]["paint"][0]["size"].replace(".0x", "x").split("x")[0] + "px"
        else:
            v = stprop(cname, state, prop.replace("style.", ""))
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except (KeyError, IndexError):
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
