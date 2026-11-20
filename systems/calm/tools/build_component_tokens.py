#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

calm.com is a Next.js marketing app (styled-components) that compiles its
theme into literals: raw/css-vars.json (tools/capture/vars.mjs) holds almost
no usable custom-property token layer, so nearly every leaf is a **measured
computed value** from raw/components-computed.json:

  light       deep-navy ink and lede text on white/light fields, the white
              pill actions with navy labels, the calm-blue -> violet brand
              gradient ends on the logo tile and the Sign-up-today pill
  accents     the measured gradient ends plus the upsell bar's gradient
  dark        the /app/* preview shell: scene-gradient canvas, deeper rail,
              white labels, white selected tab, dark unselected tab, card
              tiles, the gradient upsell/signup bars
  fonts       Figtree across both surfaces
  ramp        measured hero/section/lede/nav/meta steps plus the shell's
              rail/tab/card text sizes
  shape       fully-rounded pills (nav CTA, tabs, signup pill), tile radii,
              the auth-card radius
  states      the measured focus ring, the shell's hover transitions

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints two
surfaces: the light marketing pages and the dark app preview shell, so both
the light and dark sets are populated.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. calm.com "
    "compiles its styled-components theme into literals, so the product's "
    "own pages declare no --* token layer to alias; the only declared "
    "layers the captured surfaces carry are third-party: Zendesk Garden's "
    "--zd-* set on the /faq/web help center (emitted under core.zd) and "
    "WordPress presets on health.calm.com (raw only). Both the light "
    "marketing set and the dark app-shell set are built from measured "
    "computed styles (raw/components-computed.json)."),
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


def gradient_stops(comp, state):
    """Extract the colour stops of a painted linear-gradient."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return []
    hay = [c.get("style", {}).get("backgroundImage", "")]
    hay += [n.get("bgImage", "") for n in c.get("paint", [])]
    hay += [n.get("bgImage", "") for n in c.get("ancestors", [])]
    cols = []
    for h in hay:
        found = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", h)
        if "gradient" in h and found:
            return [norm_color(f) for f in found]
    return cols


def place_stops(stops):
    """CSS stop placement: an unpositioned first stop is 0 and last is 1; unpositioned stops between two
    positioned ones are spread evenly between them (not pushed to the end)."""
    pos = [p for _, p in stops]
    if pos[0] is None:
        pos[0] = 0.0
    if pos[-1] is None:
        pos[-1] = 1.0
    i = 0
    while i < len(pos):
        if pos[i] is None:
            j = i
            while pos[j] is None:
                j += 1
            lo, hi, n = pos[i - 1], pos[j], j - i + 1
            for k in range(i, j):
                pos[k] = round(lo + (hi - lo) * (k - i + 1) / n, 4)
            i = j
        i += 1
    return [(col, p) for (col, _), p in zip(stops, pos)]


def gradient_full(comp, state):
    """Extract the (colour, position) stops of a painted linear-gradient."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return []
    hay = [c.get("style", {}).get("backgroundImage", "")]
    hay += [n.get("bgImage", "") for n in c.get("paint", [])]
    hay += [n.get("bgImage", "") for n in c.get("ancestors", [])]
    for h in hay:
        if "gradient" not in h:
            continue
        stops = [(norm_color(col), float(pct[:-1]) / 100 if pct else None)
                 for col, pct in re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s*(\d+(?:\.\d+)?%)?", h)]
        if stops:
            return place_stops(stops)
    return []


def gradient_angle(comp, state):
    """The measured linear-gradient angle, e.g. "113.79deg", or None."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    hay = [c.get("style", {}).get("backgroundImage", "")]
    hay += [n.get("bgImage", "") for n in c.get("paint", [])]
    hay += [n.get("bgImage", "") for n in c.get("ancestors", [])]
    for h in hay:
        m = re.search(r"linear-gradient\(\s*(-?[\d.]+)(deg|turn|rad|grad)", h)
        if m:
            return m.group(1) + "deg" if m.group(2) == "deg" else m.group(0).split("(")[1].split(",")[0].strip()
    return None


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


def put(bag, key, comp, state, prop, ty, desc, transform=None):
    """Emit a measured leaf when the reading exists."""
    try:
        if prop == "paint":
            v = painted(comp, state)
        elif prop == "textStyle-color":
            v = C[comp]["states"][state].get("textStyle", {}).get("color")
        elif prop.startswith("text-"):
            v = ts(comp, state, prop[5:])
        else:
            v = st(comp, state).get(prop, "")
        v = (v or "").strip()
        if not v or v == "transparent" or v == "none":
            return
        if transform:
            v = transform(v)
            if not v:
                return
        if ty == "color":
            v = norm_color(v)
        bag[key] = {"value": v, "type": ty,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("body", "hero-sub", "default", "The Figtree stack on marketing body text."),
    ("display", "hero-title", "default", "The Figtree display stack on the hero headline."),
    ("app", "rail-item", "default", "The Figtree stack inside the dark app shell."),
    ("health", "h-hero", "default", "The stack the WordPress B2B surface serves."),
]:
    v = ts(comp, state, "fontFamily")
    if v:
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# --------------------------------------------------------- light colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "section-h2", "default", "color", "The deep-navy ink on marketing headings."),
    ("muted", "hero-sub", "default", "color", "The muted black of the hero sub-copy and secondary text."),
    ("paper", "nav-cta", "default", "paint", "The white of the header pill and the auth cards."),
    ("on-paper", "nav-cta", "default", "color", "The navy label inside the white pills."),
    ("field", "cookie-banner", "default", "paint", "The field the consent bottom sheet paints."),
    ("link", "learn-more", "default", "color", "The near-black text of the section cards and inline links."),
    ("hairline", "login-social-btn", "default", "borderTopColor", "The hairline on the outline social buttons."),
    ("footer-panel", "footer", "default", "paint", "The deep-navy footer panel at the bottom of the light page."),
    ("on-footer", "footer-link", "default", "color", "The white links on the navy footer panel."),
]:
    put(neutral, key, comp, state, prop, "color", desc)
# the header's navy scrim over the hero photograph
scrimstops = gradient_full("header", "default")
if len(scrimstops) >= 2:
    neutral["scrim"] = {"value": [{"color": col, "position": pos} for col, pos in scrimstops],
                        "type": "gradient",
                        "angle": gradient_angle("header", "default"),
                        "source": "computed backgroundImage of header default (raw/components-computed.json)",
                        "description": "The navy scrim the header paints over the hero photograph so the white nav stays legible."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# the brand gradient ends: the hero CTA and the Sign-up-today pill paint
# linear-gradient(#2477aa -> #6461e0)
stops = gradient_stops("signup-button", "default") or gradient_stops("logo", "default") or gradient_stops("upsell", "default")
if len(stops) >= 2:
    brand["blue"] = {"value": stops[0], "type": "color",
                     "source": "first stop of the painted linear-gradient on the Sign-up-today pill / logo tile (raw/components-computed.json)",
                     "description": "The calm-blue gradient start."}
    brand["violet"] = {"value": stops[-1], "type": "color",
                       "source": "last stop of the painted linear-gradient on the Sign-up-today pill / logo tile (raw/components-computed.json)",
                       "description": "The violet gradient end."}
for key, comp, state, prop, desc in [
    ("cta-ink", "signup-button", "default", "color", "The white text on the gradient pill."),
    ("hero-ink", "hero-title", "default", "color", "The navy the hero headline paints over the photograph."),
]:
    put(brand, key, comp, state, prop, "color", desc)
# the mobile menu's lighter ramp
menustops = gradient_full("m-menu-open", "default")
if len(menustops) >= 2:
    brand["menu"] = {"value": [{"color": col, "position": pos} for col, pos in menustops],
                     "type": "gradient",
                     "angle": gradient_angle("m-menu-open", "default"),
                     "source": "computed backgroundImage of m-menu-open default (raw/components-computed.json)",
                     "description": "The lighter calm-blue to violet ramp the mobile menu paints."}

# ------------------------------------------------------- dark shell colours

appc = SPEC["core"].setdefault("color", {}).setdefault("app", {})
# the shell canvas is a painted scene gradient, not a solid: emit the ramp as
# a gradient token plus its deep stop as the solid surface-page swatch
scenestops = gradient_full("scene", "default")
scene_src = "computed backgroundImage of scene default (raw/components-computed.json)"
if len(scenestops) < 2:
    # Fallback evidence: the /app/* re-measure stayed PerimeterX-blocked after
    # a standalone probe already read the live SceneGradient. raw/scene-probe.json
    # persists that reading with its own provenance.
    probe = RAW / "scene-probe.json"
    if probe.exists():
        bgi = json.loads(probe.read_text()).get("measurements", {}).get("backgroundImage", "")
        hits = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s*(\d+(?:\.\d+)?%)?", bgi)
        scenestops = [(norm_color(col), float(pct[:-1]) / 100 if pct else None) for col, pct in hits]
        if scenestops and all(p is None for _, p in scenestops):
            scenestops[0] = (scenestops[0][0], 0.0)
            scenestops[-1] = (scenestops[-1][0], 1.0)
        scene_src = "computed backgroundImage of the live SceneGradient div, persisted from the standalone probe (raw/scene-probe.json)"
if len(scenestops) >= 2:
    appc["scene"] = {"value": [{"color": col, "position": pos} for col, pos in scenestops],
                     "type": "gradient",
                     "angle": gradient_angle("scene", "default"),
                     "source": scene_src,
                     "description": "The scene gradient the /app/* preview shell paints behind everything."}
    appc["canvas"] = {"value": scenestops[-1][0], "type": "color",
                      "source": "deep stop of the painted scene gradient (" + scene_src.split("(")[-1].rstrip(")") + ")",
                      "description": "The deep end of the scene gradient the rail and content sit over."}
for key, comp, state, prop, desc in [
    ("rail", "rail", "default", "backgroundColor", "The left rail fill (black at 30% over the scene gradient)."),
    ("text", "rail-item", "default", "textStyle-color", "The near-white shell text."),
    ("card-scrim", "content-card", "default", "paint", "The artwork tile's overlay scrim."),
    ("pill", "tab", "default", "backgroundColor", "The unselected category pill field."),
    ("pill-text", "tab", "default", "color", "The unselected tab's label."),
    ("active", "tab-active", "default", "backgroundColor", "The selected white category pill."),
    ("active-ink", "tab-active", "default", "color", "The dark label on the selected pill."),
    ("raised", "d-login", "default", "backgroundColor", "The raised dark Login pill on the shell top bar."),
    ("upsell", "upsell", "default", "paint", "The upsell bar's painted field."),
]:
    put(appc, key, comp, state, prop, "color", desc)
# the bottom signup bar paints a light gradient, not a solid
barstops = gradient_full("signup-bar", "default")
if len(barstops) >= 2:
    appc["bar"] = {"value": [{"color": col, "position": pos} for col, pos in barstops],
                   "type": "gradient",
                   "source": "computed backgroundImage of signup-bar default (raw/components-computed.json)",
                   "angle": gradient_angle("signup-bar", "default"),
                   "description": "The light-blue gradient the bottom signup bar paints."}
appstops = gradient_stops("upsell", "default")
if len(appstops) >= 2:
    # the painted ramp inside the upsell banner is the little TimeIconWrapper
    # decoration (cyan -> violet), not the banner field itself
    appc["icon-ramp"] = {"value": [{"color": col, "position": pos}
                                   for col, pos in gradient_full("upsell", "default")],
                         "type": "gradient",
                         "angle": gradient_angle("upsell", "default"),
                         "source": "computed backgroundImage of the TimeIconWrapper inside upsell default (raw/components-computed.json)",
                         "description": "The cyan-to-violet gradient the clock icon inside the upsell banner paints."}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
ROLE_LIGHT = [
    ("--text-primary", "ink", "Body and heading ink."),
    ("--text-secondary", "muted", "Secondary text: the muted hero sub-copy."),
    ("--surface-page", "paper", "The white marketing field behind the auth cards and page sections."),
    ("--surface-field", "field", "The consent-sheet field."),
    ("--action-primary", "paper", "The white pill actions carry the navy label."),
    ("--text-on-action", "on-paper", "The navy label inside the white pills."),
    ("--link", "link", "Inline and section-card links."),
    ("--border-field", "hairline", "The outline-button hairline."),
    ("--surface-footer", "footer-panel", "The navy footer panel closing the light page."),
    ("--text-on-footer", "on-footer", "The white links on the navy footer panel."),
]
for name, key, desc in ROLE_LIGHT:
    if key in neutral:
        emit(light, name, {"value": "{color.neutral." + key + "}", "type": "color",
                           "source": ALIAS, "description": desc})
if "blue" in brand:
    emit(light, "--action-accent", {"value": "{color.brand.blue}", "type": "color",
                                    "source": ALIAS, "description": "The brand gradient start used on accent pills."})
if "hero-ink" in brand:
    emit(light, "--text-hero", {"value": "{color.brand.hero-ink}", "type": "color",
                                "source": ALIAS, "description": "The headline colour over hero photography."})

dark = SPEC["dark"]
ROLE_DARK = [
    ("--text-primary", "text", "Shell text."),
    ("--surface-page", "canvas", "The app-preview canvas."),
    ("--surface-rail", "rail", "The left rail fill."),
    ("--surface-pill", "pill", "The unselected category pill."),
    ("--text-pill", "pill-text", "The unselected tab label."),
    ("--surface-active", "active", "The selected white pill."),
    ("--text-on-active", "active-ink", "The dark label on the selected pill."),
    ("--surface-raised", "raised", "The raised dark Login pill."),
]
for name, key, desc in ROLE_DARK:
    if key in appc:
        emit(dark, name, {"value": "{color.app." + key + "}", "type": "color",
                          "source": ALIAS, "description": desc})
if "text" in appc:
    emit(dark, "--action-primary", {"value": "{color.app.text}", "type": "color",
                                    "source": ALIAS, "description": "The white Try-Calm-for-Free pill on the dark top bar."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, prop, desc in [
    ("display", "hero-title", "default", "fontSize", "The marketing display size (Calm your mind.)."),
    ("display-mobile", "m-hero", "default", "fontSize", "The display size at 390px."),
    ("h2", "section-h2", "default", "fontSize", "The marketing section-heading size."),
    ("lede", "hero-sub", "default", "fontSize", "The hero lede size."),
    ("body", "header", "default", "fontSize", "The page base size."),
    ("nav", "nav-link", "default", "fontSize", "Nav link / button label size."),
    ("meta", "footer-link", "default", "fontSize", "Footer-link text."),
    ("app-section", "med-title", "default", "fontSize", "The dark shell's section title."),
    ("app-nav", "rail-item", "default", "fontSize", "The rail item label."),
    ("app-tab", "tab", "default", "fontSize", "The category pill text."),
    ("app-meta", "see-all", "default", "fontSize", "The See-All / card-meta size."),
    ("health-display", "h-hero", "default", "fontSize", "The B2B hero size."),
]:
    v = ts(comp, state, prop)
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "Display leading."),
    ("h2", "section-h2", "default", "Heading leading."),
    ("nav", "nav-link", "default", "Nav link leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v and re.search(r"(px|rem)$", v):
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The display weight."),
    ("nav", "nav-link", "default", "Nav link weight."),
    ("cta", "nav-cta", "default", "The pill label weight."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weight[key] = {"type": "fontWeight", "value": v,
                       "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "nav-cta", "default", "borderTopLeftRadius", "The fully-rounded nav/hero pills."),
    ("tab", "tab", "default", "borderTopLeftRadius", "The category-pill radius."),
    ("tile", "content-card", "default", "PAINT_RADIUS:ImageWrapper", "The content-tile artwork radius."),
    ("rail-item", "rail-item", "default", "borderTopLeftRadius", "The rail-item radius."),
    ("card", "login-dialog", "default", "borderTopLeftRadius", "The auth-card radius."),
    ("badge", "card-badge", "default", "borderTopLeftRadius", "The New-badge radius."),
    ("menu", "m-menu-button", "default", "borderTopLeftRadius", "The menu-button radius."),
]:
    if prop.startswith("PAINT_RADIUS:"):
        want = prop.split(":", 1)[1].lower()
        node = next((n for n in (C.get(comp, {}).get("states", {}).get(state, {}).get("paint") or [])
                     if want in str(n.get("node", "")).lower() and n.get("radius")), None)
        if node:
            radius[key] = {"value": node["radius"], "type": "dimension",
                           "source": f"measured borderRadius of the {want} layer painted inside {comp} {state} (raw/components-computed.json)",
                           "description": desc}
        continue
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

easing = {}
for key, vname, desc in [
    ("standard", "--ease-standard", "A declared easing variable, if the sheets carry one."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)
for key, comp, state, desc in [
    ("measured", "tab", "default", "The category pills' measured easing."),
]:
    try:
        s = st(comp, state)
        fn = s["transitionTimingFunction"].split(",")[0].strip()
        if fn and fn != "ease":
            easing[key] = {"value": fn, "type": "cubicBezier",
                           "source": f"computed transitionTimingFunction of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except (KeyError, TypeError):
        pass
if easing:
    SPEC["core"]["easing"] = easing

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# the focus ring: a painted outline or a shadow, whatever the page draws
for comp, state in (("nav-cta", "focus-visible"), ("nav-link", "focus-visible")):
    try:
        s = st(comp, state)
        if s.get("outlineStyle") != "none" and float(s.get("outlineWidth", "0px").replace("px", "") or 0) > 0:
            meas["focus-ring"] = {"value": {"width": s["outlineWidth"], "style": s["outlineStyle"],
                                            "color": norm_color(s["outlineColor"]), "offset": s["outlineOffset"]},
                                  "type": "other",
                                  "source": f"computed outline of {comp} {state} (raw/components-computed.json)",
                                  "description": "The keyboard-focus ring."}
            break
        if s.get("boxShadow") and s["boxShadow"] != "none":
            m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)", s["boxShadow"])
            if m:
                meas["focus-ring"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp} for a, x, y, bl, sp in m],
                                      "type": "shadow",
                                      "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                                      "description": "The keyboard-focus ring drawn as a shadow."}
                break
    except KeyError:
        continue
# no backdrop token: the login card's own fill is the only measured paint in
# its subtree, and the dimmed overlay layer was never captured as a node.
for key, comp, state, prop, ty, desc in [
    ("card-border", "content-card", "default", "borderTopColor", "color", "The content-tile border, when painted."),
    ("control-transition", "tab", "default", "transitionDuration", "duration", "The category pill's transition."),
    ("nav-transition", "nav-link", "default", "transitionDuration", "duration", "The nav link's transition."),
    ("cta-transition", "nav-cta", "default", "transitionDuration", "duration", "The CTA pill's transition."),
]:
    try:
        if prop == "paint":
            v = painted(comp, state)
        else:
            v = st(comp, state).get(prop, "")
        v = (v or "").strip()
        if not v or v == "none":
            continue
        if prop == "borderTopColor":
            s0 = st(comp, state)
            if s0.get("borderTopStyle") in ("none", "hidden") or s0.get("borderTopWidth") in ("0px", "0"):
                continue
        if ty == "duration":
            v = v.split(",")[0].strip()
            if v == "0s":
                continue
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
    except KeyError:
        pass

# the painted elevations: the health card's lift, the auth card over the
# scrim, and the content tile's shadow on its ImageWrapper layer
shadows = {}
for key, cname, state, paint_node, desc in [
    ("card", "h-card", "default", None, "The B2B card's lift."),
    ("dialog", "login-dialog", "default", None, "The auth card's elevation over the scrim."),
    ("tile", "content-card", "default", "ImageWrapper", "The content tile's lift, painted on its artwork layer."),
]:
    try:
        if paint_node:
            want = paint_node.lower()
            node = next((n for n in (C[cname]["states"][state].get("paint") or [])
                         if want in str(n.get("node", "")).lower() and n.get("shadow")), None)
            shadow_str = node["shadow"] if node else ""
            src = f"measured boxShadow of the {paint_node} layer painted inside {cname} {state} (raw/components-computed.json)"
        else:
            shadow_str = st(cname, state).get("boxShadow", "")
            src = f"computed boxShadow of {cname} {state} (raw/components-computed.json)"
        m = re.findall(
            r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)",
            shadow_str)
        if m:
            shadows[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y,
                                       "blur": bl, "spread": sp} for a, x, y, bl, sp in m],
                            "type": "shadow",
                            "source": src,
                            "description": desc}
    except KeyError:
        pass
if shadows:
    SPEC["core"]["shadow"] = shadows

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "nav-cta", "default", "height", "The header pill height."),
    ("hero-cta.height", "hero-cta", "default", "height", "The hero action height."),
    ("tab.height", "tab", "default", "height", "A category pill's height."),
    ("card.radius", "login-dialog", "default", "borderTopLeftRadius", "The auth-card corner radius."),
    ("tile.radius", "content-card", "default", "PAINT_RADIUS:ImageWrapper", "A content tile's artwork corner radius."),
    ("rail.width", "rail", "default", "width", "The app rail's width."),
    ("rail-item.height", "rail-item", "default", "height", "A rail item's height."),
    ("header.height", "header", "default", "height", "The marketing header height."),
    ("header.height-mobile", "m-header", "default", "height", "The marketing header at 390px."),
    ("banner.height", "cookie-banner", "default", "height", "The consent bottom-sheet height."),
    ("signup-bar.height", "signup-bar", "default", "height", "The bottom signup bar's height."),
]:
    if prop.startswith("PAINT_RADIUS:"):
        want = prop.split(":", 1)[1].lower()
        pn = next((n for n in (C.get(cname, {}).get("states", {}).get(state, {}).get("paint") or [])
                   if want in str(n.get("node", "")).lower() and n.get("radius")), None)
        if not pn:
            continue
        val, src = pn["radius"], f"measured borderRadius of the {want} layer painted inside {cname} {state} (raw/components-computed.json)"
    elif have(cname, state, prop):
        val = st(cname, state)[prop]
        src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
    else:
        continue
    node = comp
    parts = key.split(".")
    for p_ in parts[:-1]:
        node = node.setdefault(p_, {})
    node[parts[-1]] = {"type": "dimension", "value": val,
                       "source": src,
                       "description": desc}

# -------------------------------------------------- help center declared layer

# /faq/web is a Zendesk Guide help center: it serves Garden's --zd-* declared
# layer (the 103-colour palette, font families, sizes, weights and line
# heights in raw/css-vars.json resolved). It is the only declared token layer
# on any captured surface — calm.com's own pages compile theirs to literals —
# so it is emitted under core.zd exactly as declared, var by var.
ZD_KIND = {"color": "color", "dimension": "dimension", "number": "number",
           "fontFamily": "fontFamily"}
for rname, rv in sorted(RL.items()):
    if not rname.startswith("--zd-"):
        continue
    kind = rv.get("kind") or "other"
    ty = ZD_KIND.get(kind, "other")
    if rname.startswith("--zd-font-weight"):
        ty = "fontWeight"
    emit(SPEC["core"], rname, var(rname, ty,
        description="The Zendesk Garden token the /faq/web help center declares."))

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
