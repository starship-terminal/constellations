#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dona.ai is a Gatsby 4 + styled-components marketing site: raw/css-vars.json
(read by tools/capture/vars.mjs) shows there is no design-token layer — the
only custom properties are component-scoped helpers (--button-color: #19191B
on the Button classes, --icon-color/--icon-size on icons, --blur-opacity on
the newsletter submit) — so every design token here is a **measured computed
value** from raw/components-computed.json:

  neutrals    ink #19191b, muted #616870, placeholder #bfc3c8, white field,
              the #eceff2/#e9ecef button greys, #f4f4f5/#eff2f5 tile fills
              -> core.color.neutral / core.color.fill
  brand       the #008ffd blue on the Try for free CTA, the feature and
              newsletter swooshes, and the #7289da Discord fill
              -> core.color.brand
  fonts       Inter 400/500/600/700 (the @font-face faces raw/css-vars.json
              lists, served inline as woff2 and from /static/inter-*.woff2)
              -> core.font.family / weight
  ramp        measured display/h2/h3/lede/body/small sizes, plus the 40px
              newsletter field and the mobile ramp -> core.font.*
  shape       32px button pills, 20px media cards, 40px cookie banner, 14px
              chips, 50% round close, 75% ellipse swooshes -> core.radius
  shadows     the #0c1442 low-alpha lift shadows, the button inset bevel, the
              card ring + the join-button blue glow -> core.shadow
  states      #005fcc focus ring, hover greys, the modal scrim
              -> core.measured, light.action.*

A leaf is {"var": "--name"} (resolved by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value; dona.ai's only var
declarations are component-scoped so nothing resolves on :root and every
leaf is measured. The site paints one light theme; the `dark` set is left
empty so build_tokens.py emits core and light only.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. dona.ai declares "
    "no :root design vars (only component-scoped --button-color/--icon-*/"
    "--blur-opacity helpers), so the tree is built from measured computed "
    "styles on the running pages (raw/components-computed.json), cross-checked "
    "against the declared var values. Semantic roles land in the light set "
    "(the only theme the public surface paints)."),
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


TYPED = "Reconstruction: entered by hand at capture time from a probe never written to raw/; no reading in raw/ holds it"


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
    m = re.fullmatch(r"rgba?\((\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?)(?:,\s*([\d.]+))?\)", v)
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


def shadow_layers(sh):
    """CSS boxShadow string -> DTCG shadow layers (inset last in the string)."""
    layers = []
    for m in re.finditer(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)(\s+inset)?", sh):
        col, x, y, bl, sp, ins = m.groups()
        d = {"color": norm_color(col), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp}
        if ins:
            d["inset"] = True
        layers.append(d)
    return layers


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("sans", "hero-h1", "default", "The one family the surface paints: Inter, falling back to sans-serif. Inter 400/500/600/700 ship as inline woff2 plus /static/inter-*.woff2 subset files (raw/css-vars.json fonts)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json); the @font-face declarations are in raw/css-vars.json fonts",
                    "description": desc}

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-h1", "default", "color", "The near-black ink #19191b on every heading, button label and body line — also the declared --button-color on the Button classes (raw/css-vars.json app)."),
    ("muted", "section-para", "default", "color", "The secondary body grey #616870 under the section heads."),
    ("placeholder", None, "default", None, "The #bfc3c8 of the email field's placeholder text."),
    ("paper", "cookie-banner", "default", "backgroundColor", "The white the page field and the cookie banner paint."),
]:
    if comp is None:  # placeholder lives on the input's ::placeholder, not its style
        try:
            v = norm_color(C["email-input"]["states"][state]["placeholder"]["color"])
            neutral[key] = {"value": v, "type": "color",
                            "source": "computed placeholder color of email-input default (raw/components-computed.json)",
                            "description": desc}
        except KeyError:
            pass
    elif have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}

fill = SPEC["core"].setdefault("color", {}).setdefault("fill", {})
for key, comp, state, desc in [
    ("control", "cookie-accept", "default", "The #eceff2 resting grey of the pill buttons (Accept, Login, Watch video)."),
    ("control-hover", "cookie-accept", "hover", "The #e9ecef hover step on the grey pills."),
    ("ghost-hover", "nav-about", "hover", "The #f2f4f8 wash the borderless About button picks up on hover."),
    ("tile", "feature-tile", "default", "The #f4f4f5 feature-tile field."),
    ("media", "hero-video", "default", "The #eff2f5 field the hero media tile paints."),
    ("chip", "social-link", "default", "The #e0e3e7 social-chip fill."),
    ("chip-hover", "social-link", "hover", "The #dde0e4 chip hover step."),
    ("chip-pressed", "social-link", "pressed", "The #dadde1 chip pressed step."),
    ("close", "modal-close", "default", "The #b0b5ba round modal-close fill."),
    ("close-hover", "modal-close", "hover", "The #a8adb3 hover step on the close button."),
    ("chip-twitter-pressed", "footer-twitter", "pressed", "The #e6e9ed deepest chip step, on the footer's Twitter chip."),
]:
    if have(comp, state, "backgroundColor"):
        v = norm_color(st(comp, state)["backgroundColor"])
        if v and v != "transparent":
            fill[key] = {"value": v, "type": "color",
                         "source": f"computed backgroundColor of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("blue", "try-cta", "default", "backgroundColor", "The Dona blue #008ffd: the Try for free CTA fill, the swoosh ellipses behind feature tiles and the newsletter field, and the follow-social button."),
    ("blue-hover", "try-cta", "hover", "backgroundColor", "The #0087fd hover step on the blue CTA."),
    ("ink", "join-btn", "default", "backgroundColor", "The #19191b near-black fill of the Join button — same ink as the text."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state)[prop])
        if v and v != "transparent":
            brand[key] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
# The social row's Discord fill and the join-button glow live on painted
# layers inside the newsletter form, not on the measured node's own style.
for n in (C["newsletter"]["states"]["default"].get("paint") or []):
    if n.get("bg") == "rgb(114, 137, 218)":
        brand["discord"] = {"value": "#7289da", "type": "color",
                            "source": "painted fill of the Discord social button inside newsletter default (raw/components-computed.json)",
                            "description": "The #7289da Discord-brand fill of the community button in the social row."}
    if n.get("shadow", "").startswith("rgb(111, 171, 255)"):
        brand["glow"] = {"value": "#6fabff", "type": "color",
                         "source": "painted boxShadow of the submit wrapper's ::before inside newsletter default (raw/components-computed.json)",
                         "description": "The #6fabff blue glow behind the Join our newsletter button."}

# The hero media card's third shadow layer is a 1px #e6e9ed inset ring — the
# only hairline "border" on a surface whose controls are all borderless.
if have("hero-video", "default", "boxShadow"):
    m = re.search(r"rgb\(230, 233, 237\) 0px 0px 0px 1px inset", st("hero-video", "default")["boxShadow"])
    if m:
        fill["ring"] = {"value": "#e6e9ed", "type": "color",
                        "source": "computed boxShadow inset layer of hero-video default (raw/components-computed.json)",
                        "description": "The #e6e9ed 1px inset hairline the media card draws instead of a border."}

measured_extra = {
    "scrim": ("rgba(191, 195, 200, 0.8)", "computed backgroundColor of video-modal default (raw/components-computed.json)",
              "The translucent light-grey scrim rgba(191,195,200,.8) the video modal lays over the page."),
}
extra = SPEC["core"].setdefault("color", {}).setdefault("overlay", {})
if have("video-modal", "default", "backgroundColor"):
    extra["scrim"] = {"value": norm_color(st("video-modal", "default")["backgroundColor"]),
                      "type": "color",
                      "source": measured_extra["scrim"][1],
                      "description": measured_extra["scrim"][2]}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Headline, button-label and body ink."})
if "muted" in neutral:
    emit(light, "--text-secondary", {"value": "{color.neutral.muted}", "type": "color",
                                     "source": ALIAS, "description": "Section body copy."})
if "placeholder" in neutral:
    emit(light, "--text-placeholder", {"value": "{color.neutral.placeholder}", "type": "color",
                                       "source": ALIAS, "description": "The email field's placeholder."})
# Like every other measured leaf here, a reading the capture could not take is left out.
if have("try-cta", "default", "color"):
    emit(light, "--text-inverse", {"value": norm_color(st("try-cta", "default")["color"]), "type": "color",
                                   "source": "computed color of try-cta default (raw/components-computed.json)",
                                   "description": "White labels on the blue and ink buttons."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The white page and banner field."})
if "tile" in fill:
    emit(light, "--surface-card", {"value": "{color.fill.tile}", "type": "color",
                                   "source": ALIAS, "description": "The #f4f4f5 feature-tile field."})
if "media" in fill:
    emit(light, "--surface-media", {"value": "{color.fill.media}", "type": "color",
                                    "source": ALIAS, "description": "The #eff2f5 hero-media field."})
if "ink" in brand:
    emit(light, "--surface-inverse", {"value": "{color.brand.ink}", "type": "color",
                                      "source": ALIAS, "description": "The ink fill the Join button paints."})
if "blue" in brand:
    emit(light, "--action-primary", {"value": "{color.brand.blue}", "type": "color",
                                     "source": ALIAS, "description": "The #008ffd primary CTA and swoosh blue."})
if "blue-hover" in brand:
    emit(light, "--action-primary-hover", {"value": "{color.brand.blue-hover}", "type": "color",
                                           "source": ALIAS, "description": "The #0087fd hover step on the primary CTA."})
if "control" in fill:
    emit(light, "--action-secondary", {"value": "{color.fill.control}", "type": "color",
                                       "source": ALIAS, "description": "The #eceff2 resting fill of the grey pill buttons."})
if "control-hover" in fill:
    emit(light, "--action-secondary-hover", {"value": "{color.fill.control-hover}", "type": "color",
                                             "source": ALIAS, "description": "The #e9ecef hover step on the grey pills."})
if "ghost-hover" in fill:
    emit(light, "--action-ghost-hover", {"value": "{color.fill.ghost-hover}", "type": "color",
                                         "source": ALIAS, "description": "The #f2f4f8 wash a borderless nav button picks up on hover."})
if "scrim" in extra:
    emit(light, "--overlay-scrim", {"value": "{color.overlay.scrim}", "type": "color",
                                    "source": ALIAS, "description": "The modal's translucent page scrim."})
if "ring" in fill:
    emit(light, "--border-hairline", {"value": "{color.fill.ring}", "type": "color",
                                      "source": ALIAS, "description": "The 1px inset ring on media cards — the only hairline on the surface."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, prop, bag, ty, desc in [
    ("display", "hero-h1", "default", "fontSize", type_scale, "dimension", "The 84px display size on the home/about/legal h1s."),
    ("display", "hero-h1", "default", "lineHeight", leading, "dimension", "Display line height (92.4px, a 1.1 ratio)."),
    ("display", "hero-h1", "default", "fontWeight", weight, "fontWeight", "Display weight — Inter Bold."),
    ("display-mobile", "m-hero", "default", "fontSize", type_scale, "dimension", "The 40px display size the mobile h1 drops to."),
    ("display-mobile", "m-hero", "default", "lineHeight", leading, "dimension", "Mobile display line height."),
    ("h2", "section-h2", "default", "fontSize", type_scale, "dimension", "The 32px section head."),
    ("h2", "section-h2", "default", "lineHeight", leading, "dimension", "Section-head line height."),
    ("h2", "section-h2", "default", "fontWeight", weight, "fontWeight", "Section-head weight — Inter SemiBold."),
    ("h3", "section-h3", "default", "fontSize", type_scale, "dimension", "The 26px feature head."),
    ("h3", "section-h3", "default", "lineHeight", leading, "dimension", "Feature-head line height."),
    ("h4", "legal-h4", "default", "fontSize", type_scale, "dimension", "The 18px legal subhead."),
    ("h4", "legal-h4", "default", "lineHeight", leading, "dimension", "Legal-subhead line height."),
    ("lede", "hero-lede", "default", "fontSize", type_scale, "dimension", "The 24px hero/mission lede."),
    ("lede", "hero-lede", "default", "lineHeight", leading, "dimension", "Lede line height."),
    ("lede", "hero-lede", "default", "fontWeight", weight, "fontWeight", "Hero-lede weight — Inter Medium (mission text uses SemiBold)."),
    ("field-display", "email-input", "default", "fontSize", type_scale, "dimension", "The 40px newsletter email field — display-sized input text."),
    ("field-display", "email-input", "default", "lineHeight", leading, "dimension", "Field line height."),
    ("field-mobile", "m-email-input", "default", "fontSize", type_scale, "dimension", "The 28px mobile field size."),
    ("body-lg", "section-para", "default", "fontSize", type_scale, "dimension", "The 18px section body copy."),
    ("body-lg", "section-para", "default", "lineHeight", leading, "dimension", "Body-large line height (a 1.45 ratio)."),
    ("body", "legal-text", "default", "fontSize", type_scale, "dimension", "The 16px base body size."),
    ("body", "legal-text", "default", "lineHeight", leading, "dimension", "Base line height (a 1.45 ratio)."),
    ("body", "legal-text", "default", "fontWeight", weight, "fontWeight", "Body weight — Inter Regular."),
    ("small", "footer-link", "default", "fontSize", type_scale, "dimension", "The 14px footer/legal small size."),
    ("small", "footer-link", "default", "lineHeight", leading, "dimension", "Small line height."),
    ("button", "try-cta", "default", "fontSize", type_scale, "dimension", "The 16px big-button label."),
    ("button", "try-cta", "default", "lineHeight", leading, "dimension", "Button-label line height."),
    ("button", "try-cta", "default", "fontWeight", weight, "fontWeight", "Button-label weight — Inter Medium."),
    ("button-sm", "cookie-accept", "default", "fontSize", type_scale, "dimension", "The 14px small-button label (nav, cookie Accept)."),
    ("button-sm", "cookie-accept", "default", "lineHeight", leading, "dimension", "Small-button line height."),
]:
    v = ts(comp, state, prop)
    if v:
        if ty == "fontWeight":
            v = int(v)
        own = st(comp, state).get(prop)
        node = (C[comp]["states"][state].get("textStyle") or {}).get("node")
        bag[key] = {"type": ty, "value": v,
                    "source": f"computed {prop} of {comp} {state}" + (f" first text node ({node})" if str(v) != str(own) else "") + " (raw/components-computed.json)",
                    "description": desc}

# ---------------------------------------------------------- radius, extras

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "try-cta", "default", "borderTopLeftRadius", "The 32px pill on every Button — nav, CTAs, Join, Accept."),
    ("card", "feature-tile", "default", "borderTopLeftRadius", "The 20px feature/media card radius."),
    ("banner", "cookie-banner", "default", "borderTopLeftRadius", "The 40px cookie-banner radius."),
    ("chip", "social-link", "default", "borderTopLeftRadius", "The 14px social-chip radius."),
    ("avatar", "team-avatar", "default", "borderTopLeftRadius", "The 12px team-avatar radius."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
# Percentage radii are not DTCG dimensions (one px or rem length), so they are listed under
# core.$extensions.notTokenised with their readings instead of being typed as dimensions.
SPEC["core"]["_notTokenised"] = []
try:
    SPEC["core"]["_notTokenised"].append(
        {"name": "radius.swoosh", "value": C["newsletter"]["states"]["default"]["::before"]["borderRadius"],
         "source": "computed borderRadius of the newsletter form's ::before swoosh (raw/components-computed.json)",
         "why": "a percentage of the box: the 75% radius that turns the blue ::before layers into elliptical swooshes behind feature tiles and the newsletter field"})
except KeyError:
    pass
if have("modal-close", "default", "borderTopLeftRadius"):
    SPEC["core"]["_notTokenised"].append(
        {"name": "radius.round", "value": st("modal-close", "default")["borderTopLeftRadius"],
         "source": "computed borderTopLeftRadius of modal-close default (raw/components-computed.json)",
         "why": "a percentage of the box: the 50% circle on the modal close button"})

shadow = SPEC["core"].setdefault("shadow", {})
for key, comp, state, desc in [
    ("button", "cookie-accept", "default", "The resting lift on the grey pill buttons: a hairline drop plus an inset top-light bevel."),
    ("action", "try-cta", "default", "The deeper lift on the coloured CTAs: drop + 40px ambient + inset bevel."),
    ("join", "join-btn", "default", "The Join button's shadow — the action lift plus a 999px inset overlay used for hover dimming (rgba(0,0,0,0) at rest)."),
    ("card", "hero-video", "default", "The hero-media card shadow: drop + 80px ambient + a #e6e9ed inset hairline ring."),
    ("banner", "cookie-banner", "default", "The floating cookie-banner shadow (three ascending layers)."),
    ("banner-mobile", "m-cookie-banner", "default", "The mobile banner variant's upward shadow (the 8/16/40 layers run negative, the shape of a top-anchored bar) — read from the marked consent node, which sat offscreen on the 390 pass; its real placement is unverified."),
    ("chip", "social-link", "default", "The social chip's bevel — same shape as the button lift but keyed on black, not #0c1442."),
]:
    try:
        sh = st(comp, state)["boxShadow"]
        if sh and sh != "none" and not sh.startswith("rgba(0, 0, 0, 0)"):
            layers = shadow_layers(sh)
            if layers:
                shadow[key] = {"value": layers, "type": "shadow",
                               "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)"
                               + ("; the marked node sat offscreen on the 390 pass and its crop caught body text, so this is not confirmed as the banner; recapture needed" if comp == "m-cookie-banner" else ""),
                               "description": desc}
    except KeyError:
        pass
# The join button's blue glow is a painted ::before, not the node's own shadow.
for n in (C["newsletter"]["states"]["default"].get("paint") or []):
    if n.get("shadow", "").startswith("rgb(111, 171, 255)"):
        layers = shadow_layers(n["shadow"])
        if layers:
            shadow["glow"] = {"value": layers, "type": "shadow",
                              "source": "painted boxShadow of the submit wrapper's ::before inside newsletter default (raw/components-computed.json)",
                              "description": "The #6fabff 140px bloom behind the Join our newsletter button."}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "cookie-learn", "focus-visible", "outlineColor", "color", "The 1px #005fcc keyboard-focus ring — the browser's own ring, the site sets no custom :focus-visible style."),
    ("underline", "cookie-learn", "default", None, "color", "The 1px ink ::before bar the Learn more link paints as its underline."),
]:
    if prop is None:
        try:
            v = norm_color(C[comp]["states"][state]["::before"]["backgroundColor"])
            meas[key] = {"value": v, "type": ty,
                         "source": f"computed ::before backgroundColor of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
        except KeyError:
            pass
    elif have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
# Unstyled anchors keep the UA stylesheet link colours — honest record, not a
# Dona design value.
if have("social-link", "default", "color"):
    meas["ua-link"] = {"value": norm_color(st("social-link", "default")["color"]), "type": "color",
                       "source": "computed color of social-link default (raw/components-computed.json)",
                       "description": "#0000ee — the browser-default link colour on the unstyled social/logo anchors, not a Dona token."}
if have("social-link", "pressed", "color"):
    meas["ua-link-active"] = {"value": norm_color(st("social-link", "pressed")["color"]), "type": "color",
                              "source": "computed color of social-link pressed (raw/components-computed.json)",
                              "description": "#ff0000 — the UA :active link colour the same anchors pick up when pressed."}

dur = SPEC["core"].setdefault("duration", {})
ease = SPEC["core"].setdefault("easing", {})
for key, comp, state, bag, desc in [
    ("hover", "cookie-accept", "default", dur, "The 150ms hover duration on the pill buttons"),
    ("submit", "join-btn", "default", None, "The Join button's staged transition: background-color .25s, box-shadow .15s, padding .3s."),
    ("modal", "video-modal", "default", dur, "The 300ms opacity fade on the video modal"),
]:
    try:
        s = st(comp, state)
        if bag is None:
            # multi-value transition recorded as one duration token per property
            props_ = s["transitionProperty"].split(", ")
            durs_ = s["transitionDuration"].split(", ")
            for p_, d_ in zip(props_, durs_):
                k = re.sub(r"[^a-z0-9]+", "-", p_.lower()).strip("-")
                dur[f"submit-{k}"] = {"value": d_, "type": "duration",
                                     "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                                     "description": f"The Join button's {p_} duration."}
            continue
        d = s["transitionDuration"]
        if d and d != "0s":
            first = d.split(",")[0].strip()
            bag[key] = {"value": first, "type": "duration",
                        "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                                     "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
# The scroll-in reveal the sheets declare: 1s cubic-bezier(0.17, 0.17, 0, 1).
try:
    sheets_meta = json.loads((RAW / "components-computed.json").read_text())["_meta"]["sheets"]
    seen = set()
    for page, rules in sheets_meta.items():
        for r in rules:
            t = r.get("transition") or ""
            if "cubic-bezier(0.17, 0.17, 0, 1)" in t and "reveal" not in seen:
                seen.add("reveal")
                dur["reveal"] = {"value": "1s", "type": "duration",
                                 "source": f"declared transition in the readable sheets on {page} (raw/components-computed.json _meta.sheets)",
                                 "description": "The 1s scroll-in reveal the Fade wrapper carries."}
                ease["reveal"] = {"value": "cubic-bezier(0.17, 0.17, 0, 1)", "type": "cubicBezier",
                                  "source": f"declared transition in the readable sheets on {page} (raw/components-computed.json _meta.sheets)",
                                  "description": "The custom out-quint-like reveal easing."}
except KeyError:
    pass
# One easing per transitioned property; split between whole functions, never inside cubic-bezier().
_tf = set(re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st("cookie-accept", "default")["transitionTimingFunction"])) if have("cookie-accept", "default", "transitionTimingFunction") else set()
if len(_tf) > 1:
    raise ValueError(f"cookie-accept transitions use several easings: {_tf}")
if _tf:
    ease["standard"] = {"value": _tf.pop(), "type": "cubicBezier",
                        "source": "computed transitionTimingFunction of cookie-accept default (raw/components-computed.json)",
                        "description": "The plain ease every 150ms hover transition uses."}

# ------------------------------------------------------------- spacing/layout

layout = SPEC["core"].setdefault("layout", {})
# The container, gutter and grid gap came from capture probes whose readings were never written
# to raw/; they are kept, labelled as entered by hand. The content measure is a reading.
for key, val, why, desc in [
    ("container", "1140px", "the maxWidth of Container__Wrapper", "The 1140px content container."),
    ("gutter", "20px", "the paddingLeft/Right of Container__Wrapper", "The 20px side gutter inside the container."),
    ("grid-gap", "32px", "the columnGap/rowGap of the pages__Grid feature grid", "The 32px gap in the two-column feature grid."),
]:
    layout[key] = {"value": val, "type": "dimension", "source": f"{TYPED} ({why})", "description": desc}
_bars = [c for c in ("header", "newsletter") if have(c, "default", "width")]
if len({st(c, "default")["width"] for c in _bars}) > 1:
    raise ValueError("header and newsletter no longer paint one measure")
if _bars:
    layout["content"] = {"value": st(_bars[0], "default")["width"], "type": "dimension",
                         "source": "computed width of " + " and ".join(f"{c} default" for c in _bars) + " (raw/components-computed.json)",
                         "description": "The 1100px measure the bars actually paint."}

sp = SPEC["core"].setdefault("spacing", {})
for key, comp, state, prop, desc in [
    ("button-x", "try-cta", "default", "paddingLeft", "The 26px inline padding on the 52px buttons."),
    ("button-y", "try-cta", "default", "paddingTop", "The 14px block padding on the 52px buttons."),
    ("button-sm-x", "cookie-accept", "default", "paddingLeft", "The 20px inline padding on the 36px buttons."),
    ("button-sm-y", "cookie-accept", "default", "paddingTop", "The 6px block padding on the 36px buttons."),
    ("header-top", "header", "default", "paddingTop", "The 32px the header bar drops from the top."),
    ("banner", "cookie-banner", "default", "paddingTop", "The 18px inside the cookie banner (12px on mobile)."),
    ("footer-y", "footer", "default", "paddingTop", "The 64px above and below the footer row."),
]:
    if have(comp, state, prop):
        sp[key] = {"value": st(comp, state)[prop], "type": "dimension",
                   "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                   "description": desc}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "try-cta", "default", "height", "The 52px big-button height."),
    ("button-sm.height", "cookie-accept", "default", "height", "The 36px nav/cookie-button height."),
    ("header.height", "header", "default", "height", "The 68px header bar."),
    ("field.height", "email-input", "default", "height", "The 60px email field line."),
    ("close.size", "modal-close", "default", "width", "The 56px round close button."),
    ("chip.size", "social-link", "default", "width", "The 40px social chip."),
    ("avatar.size", "team-avatar", "default", "width", "The 125px team avatar."),
    ("tile.size", "feature-tile", "default", "width", "The 534px feature tile (two per row with the 32px gap)."),
    ("banner.height", "cookie-banner", "default", "height", "The 76px desktop cookie banner."),
    ("logo.width", "logo", "default", "width", "The 95x28 logo mark."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# Declared icon sizing vars (component-scoped, so they never resolve on
# :root) — recorded as measured values with their declaring selectors.
icon = comp.setdefault("icon", {})
for key, val, sel, desc in [
    ("size-sm", "14px", ".dAKTtu svg", "The 14px icon inside button labels."),
    ("size-md", "16px", ".cMsCXE", "The 16px standard icon."),
    ("size-lg", "30px", ".biKXiR", "The 30px feature icon."),
    ("size-xl", "40px", ".hCwPPL svg", "The 40px cookie/social icon."),
]:
    icon[key] = {"type": "dimension", "value": val,
                 "source": f"declared --icon-size on {sel} in the readable sheets (raw/css-vars.json app)",
                 "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
