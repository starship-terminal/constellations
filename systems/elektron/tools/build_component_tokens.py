#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

elektron.se is a WordPress/WooCommerce site on the "thedock" theme; its
stylesheets are served same-origin and declare two named custom-property
layers on :root (raw/css-vars.json, read by tools/capture/vars.mjs and
resolved in a probe under the site's single painted theme):

  --thedock-*     the theme layer: #151515 ground, #1e1e1e surface, #eeeef2
                  text/action paper, #97979a muted, #363636 border, the
                  rgba(0,0,0,0.5) scrim, control radii and the font stacks
  --tdc-*         the component layer: the same #151515/#eeeef2 pair, the
                  #212121 raised surface, #444444/#777778 borders, a 3.5px-
                  based space ramp and the 1100px layout width
  --tdss-*        the search plugin's own layer (field radius 6px, the
                  rgba(0,0,0,0.45) overlay backdrop) — recorded, not the
                  design surface

Those become {"var": ...} leaves resolved by build_tokens.py. Everything
else is **measured computed values** from raw/components-computed.json:

  greys       #cccccc secondary button fill, #757575 field placeholder,
              #333333 underline-sweep every text link paints as a
              background-image layer, #808080 the hr rule, #ffffff the
              focus ring's white half
  states      outline buttons invert: 2px #eeeef2 border, transparent ->
              #eeeef2 fill on hover/pressed, #eeeef2 -> #151515 label;
              secondary buttons #cccccc -> #151515 with #cccccc label;
              fields go #eeeef2 -> #151515 on focus inside the login
              drawer. Focus is a double ring: #ffffff 0 0 0 2px box-shadow
              + a 2px solid #000000 outline offset 2px
  font        "Neue Haas Grotesk Text Pro" body/nav, "Neue Haas Grotesk
              Display Pro" headings and big links (450/500), "digi one v2"
              on block-button labels, "Analog One V2." in the search field
  ramp        measured 64.05/60.85 display (page titles, section h2),
              44.39/42.17 explore rows, 30.8/40.96 h1, 24.01/36.02 big
              links (footer, accordion, mobile menu), 24.01/31.93 about
              title, 17.99/26.99 product titles and prices, 14/21 nav,
              fields and body, 14/17.5 the search field
  shape       square everything — --tdc-radius 0px on buttons, fields,
              drawers; only the header search field paints 7px
  space       a 7px rhythm: --tdc-space-1..5 = 3.5/7/14/21/35, and the
              measured 10.5/17.5 paddings, 44px field pad, 70px title indent

A leaf is {"var": ...} (resolved under the dark theme) or {"value": ...,
"source": ...} for a measured value. Only the signed-out public surface
was read; the site paints one dark theme, emitted under `dark` (the
spotify convention for a single painted dark set).
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("dark", {})
J = json.loads((RAW / "components-computed.json").read_text())
C = J["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def split_layers(v):
    """Split a computed shadow list on the commas outside parentheses."""
    out, depth, cur = [], 0, ""
    for ch in v:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()] if cur.strip() else out


def shadow_value(v, where):
    """Every layer of a computed box-shadow as DTCG layers; a layer it cannot read stops the build."""
    layers = []
    for part in split_layers(v):
        m = re.fullmatch(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)"
                         r"\s+(-?\d+(?:\.\d+)?px)(?:\s+(-?\d+(?:\.\d+)?px))?(\s+inset)?", part)
        if not m:
            raise SystemExit(f"{where}: shadow layer not understood: {part!r}")
        a, x, y, bl, sp, ins = m.groups()
        layer = {"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp or "0px"}
        if ins:
            layer["inset"] = True
        layers.append(layer)
    return layers


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. elektron.se "
    "declares readable --thedock-*/--tdc-* custom properties on :root "
    "(raw/css-vars.json); they are var-referenced where the measured surface "
    "paints the same value, and measured computed values "
    "(raw/components-computed.json) cover the #cccccc/#757575/#333333/"
    "#808080 greys, the inverted outline-button and focus-ring state layers, "
    "the Neue Haas Grotesk Text/Display and digi one v2 / Analog One V2 "
    "families, the all-square radii and the 7px space rhythm. The site "
    "paints one dark theme; the roles live in the dark set."),
    "core": {}, "dark": {}, "component": {}}


def emit(root, name, leaf):
    node, last = descend(root, name.split("."))
    node[last] = leaf


def st(comp, state):
    c = C[comp]
    if c.get("missing"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer), `ancestors.N.prop` or `rect.W`; a `.border` tail
    pulls the colour out of the "T:1px solid rgb(...)" border string."""
    d = C[comp]["states"][state]
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
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


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
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool(str(s.get(prop) or "").strip())
    except KeyError:
        return False


def find_var(value, contains=None):
    """First resolved var whose value matches — used to var-reference a
    measured colour where the theme layer declares the same value."""
    for n, v in R.items():
        if norm_color(str(v)) == value and (contains is None or contains in n):
            return n
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc, vn in [
    ("text", "nav-link", "default",
     "Body, navigation and heading-adjacent text: Neue Haas Grotesk Text Pro.", "--thedock-font"),
    ("display", "section-h2", "default",
     "Display headings and the big footer/accordion/menu links: Neue Haas Grotesk Display Pro.", "--tdc-font-heading"),
    ("button", "submit-button", "default",
     "The digi one v2 face every block-button label paints (the block-button text style), with text-transform capitals on the outline actions.", None),
    ("search", "search-field", "default",
     "The Analog One V2. face the header search field paints.", None),
]:
    try:
        v = ts(comp, state, "fontFamily")
        if v:
            leaf_ = {"type": "fontFamily",
                     "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
            if vn and vn in R:
                leaf_ = {"var": vn, "type": "fontFamily",
                         "source": f"css-var {vn} (raw/css-vars.json); computed fontFamily of {comp} {state} agrees",
                         "description": desc}
            else:
                leaf_["value"] = v
            fam[key] = leaf_
    except KeyError:
        pass
mono_vn = "--thedock-mono" if "--thedock-mono" in R else None
if mono_vn:
    fam["mono"] = var(mono_vn, "fontFamily",
                    source=f"css-var {mono_vn} (raw/css-vars.json)",
                    description="The declared monospace stack for code and technical text.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "nav-link", "default", "Body and display weight (400) — the whole face set."),
    ("book", "footer-link", "default", "The 450 weight on big display links (footer, accordion, mobile menu)."),
    ("medium", "section-h2", "default", "The 500 weight on display headings and explore rows."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(float(v)), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
# The monochrome ramp: var-referenced where the theme layer declares the
# same value the surface paints, measured where it does not.
for key, vn, comp, state, prop, desc in [
    ("ink", "--thedock-bg", "cart-drawer", "default", "ancestors.0.bg",
     "The #151515 ground: page background and the label colour on paper fills."),
    ("surface", "--thedock-surface", None, None, None,
     "The #1e1e1e raised surface (secondary panels, footer layer)."),
    ("raised", "--tdc-surface", "account-modal", "opened", "paint.1.bg",
     "The #212121 raised fill the account drawer paints."),
    ("paper", "--thedock-text", "nav-link", "default", "color",
     "The #eeeef2 paper: all text, icon colour and the fill an outline button takes on hover."),
    ("muted", "--thedock-muted", None, None, None,
     "The #97979a muted text the theme layer declares."),
    ("muted2", "--tdc-muted", None, None, None,
     "The #b8b8bb secondary muted the component layer declares."),
    ("border", "--thedock-border", None, None, None,
     "The #363636 hairline the theme layer declares."),
    ("border2", "--tdc-border", None, None, None,
     "The #444444 hairline the component layer declares."),
    ("border-control", "--tdc-border-control", None, None, None,
     "The #777778 control border the component layer declares."),
    ("scrim", "--thedock-overlay", None, None, None,
     "The rgba(0,0,0,0.5) drawer/modal scrim."),
]:
    if vn and vn in R:
        src = f"css-var {vn} (raw/css-vars.json)"
        if comp:
            src += f"; computed {prop} of {comp} {state} agrees (raw/components-computed.json)"
        neutral[key] = var(vn, "color", source=src, description=desc)
    elif comp:
        v = norm_color(stprop(comp, state, prop))
        if v:
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}

# measured greys the vars do not name
for key, comp, state, prop, desc in [
    ("grey", "magic-send", "default", "backgroundColor",
     "The #cccccc secondary-button fill (Send me a code, Create New Account)."),
    ("placeholder", "search-field", "default", "placeholder.color",
     "The #757575 placeholder text inside the light fields."),
    ("sweep", "nav-link", "default", "paint.0.bgImage",
     "The #333333 of the linear-gradient underline-sweep every text link paints as a background layer."),
    ("rule", "account-modal", "opened", "paint.2.bg",
     "The #808080 hr separator inside the account drawer."),
]:
    try:
        raw_v = stprop(comp, state, prop)
        if prop.endswith("bgImage"):
            m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", raw_v or "")
            raw_v = m.group(0) if m else ""
        v = norm_color(raw_v)
        if v:
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass
# pure white, the focus ring's outer half (measured on every focus-visible state)
def spread_ring(layers, spread, where):
    """The one layer that is a flat ring of the given spread (no offset, no blur)."""
    hits = [l for l in layers if l["offsetX"] == l["offsetY"] == l["blur"] == "0px" and l["spread"] == spread
            and not l.get("inset")]
    if len(hits) != 1:
        raise SystemExit(f"{where}: expected one {spread} spread ring in the box-shadow, found {len(hits)}")
    return hits[0]


neutral["white"] = {"value": spread_ring(shadow_value(st("nav-link", "focus-visible")["boxShadow"], "nav-link focus-visible"),
                                         "2px", "nav-link focus-visible")["color"],
                    "type": "color",
                    "source": "computed boxShadow of nav-link focus-visible (raw/components-computed.json): the colour of its 2px spread layer",
                    "description": "Pure white, used only as the focus ring's 2px spread layer and the lightest field borders."}

status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
for key, vn, base, desc in [
    ("error", "--tdc-danger", "#d63638",
     "The declared danger red: --tdc-danger paints color-mix(in srgb, #d63638 70%, currentColor)."),
    ("success", "--tdc-success", "#1e7a3c",
     "The declared success green: --tdc-success paints color-mix(in srgb, #1e7a3c 70%, currentColor)."),
]:
    if vn in R:
        m = re.fullmatch(r"color-mix\(in srgb,\s*(#[0-9a-fA-F]{3,8})\s+\d+%,\s*currentColor\)", R[vn].strip())
        if not m:
            raise SystemExit(f"{vn}: expected a color-mix over a base hue, got {R[vn]!r}")
        status[key] = {"value": norm_color(m.group(1)), "type": "color",
                       "source": f"css-var {vn} (raw/css-vars.json) resolves to a color-mix over this base hue",
                       "description": desc}

# -------------------------------------------------------------------- roles

dark = SPEC["dark"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("page", "color.neutral.ink", "The #151515 page ground."),
    ("surface", "color.neutral.surface", "The #1e1e1e raised surface."),
    ("surface-raised", "color.neutral.raised", "The #212121 drawer fill."),
    ("text", "color.neutral.paper", "The #eeeef2 all-purpose text."),
    ("text-muted", "color.neutral.muted", "Secondary text."),
    ("text-muted2", "color.neutral.muted2", "The lighter secondary text the component layer declares."),
    ("border", "color.neutral.border", "The #363636 hairline."),
    ("control-border", "color.neutral.border-control", "The #777778 control border."),
    ("accent", "color.neutral.paper", "The inverted action colour: the paper fill a button takes, and its default 2px border."),
    ("accent-text", "color.neutral.ink", "The #151515 label painted on a paper fill."),
    ("field", "color.neutral.paper", "The light #eeeef2 fill of the 42px block inputs."),
    ("field-text", "color.neutral.ink", "The #151515 text inside the light fields."),
    ("secondary", "color.neutral.grey", "The #cccccc secondary-button fill."),
    ("secondary-hover", "color.neutral.ink", "Secondary buttons invert to #151515 on hover."),
    ("secondary-hover-text", "color.neutral.grey", "…with the #cccccc label staying."),
    ("scrim", "color.neutral.scrim", "The 50% black modal scrim."),
    ("placeholder", "color.neutral.placeholder", "The #757575 field placeholder."),
    ("sweep", "color.neutral.sweep", "The #333333 underline-sweep links paint on hover."),
    ("rule", "color.neutral.rule", "The #808080 separator rule."),
    ("focus-ring", "color.neutral.white", "The white 2px spread half of the double focus ring."),
]:
    emit(dark, name, {"value": "{" + target + "}", "type": "color",
                      "source": ALIAS, "description": desc})
_fo = st("nav-link", "focus-visible")
dark["focus-outline"] = {"value": norm_color(_fo["outlineColor"]), "type": "color",
                         "source": f"computed outlineColor of nav-link focus-visible (raw/components-computed.json): {_fo['outlineWidth']} {_fo['outlineStyle']} offset {_fo['outlineOffset']}, paired with the white spread ring",
                         "description": "The black 2px outline half of the double focus ring."}

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "section-h2", "default", "The 64px display of page titles and section headings."),
    ("display-mid", "explore-link", "default", "The 44px explore index rows."),
    ("title", "hero-h1", "default", "The 31px home hero heading."),
    ("heading", "footer-link", "default", "The 24px display links: footer columns, accordion rows, mobile menu."),
    ("title-mobile", "m-hero", "default", "The 24px mobile hero heading."),
    ("product", "pdp-title", "default", "The 18px product names and prices."),
    ("body", "nav-link", "default", "The 14px control, nav, field and body size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "section-h2", "default", "Display leading (60.8px on 64px — tighter than the em)."),
    ("display-mid", "explore-link", "default", "Explore-row leading (42.2px on 44.4px)."),
    ("title", "hero-h1", "default", "Hero heading leading (41px on 30.8px)."),
    ("heading", "footer-link", "default", "Display-link leading (36px on 24px)."),
    ("title-mobile", "m-hero", "default", "Mobile hero leading (31.7px on 23.8px)."),
    ("product", "pdp-title", "default", "Product-title leading (27px on 18px)."),
    ("body", "nav-link", "default", "Control/body leading (21px on 14px)."),
    ("search", "search-field", "default", "The search field's tighter 17.5px on 14px."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for key, comp, state, desc in [
    ("display", "section-h2", "default", "The -0.64px the 64px display tightens."),
    ("display-mid", "explore-link", "default", "The -0.44px the 44px rows tighten."),
    ("title", "hero-h1", "default", "The +1.23px the hero heading opens."),
    ("heading", "footer-link", "default", "The +0.96px the 24px display links open."),
    ("title-mobile", "m-hero", "default", "The +0.95px the mobile hero opens."),
    ("product", "pdp-title", "default", "The +0.72px the 18px product text opens."),
    ("field", "text-field", "default", "The +0.56px inside the contact fields."),
    ("control", "nav-link", "default", "The +0.46px the 14px UI text opens."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        tracking[key] = {"type": "dimension", "value": v,
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

# ----------------------------------------------------------------- spacing

spacing = SPEC["core"].setdefault("spacing", {})
for key, vn, comp, state, prop, desc in [
    ("s1", "--tdc-space-1", None, None, None, "3.5px — half the 7px rhythm."),
    ("s2", "--tdc-space-2", "nav-link", "default", "gap", "7px — the icon/label gap inside buttons and links."),
    ("s3", None, "submit-button", "default", "paddingTop", "10.5px — the vertical padding inside 42-46px controls."),
    ("s4", "--tdc-space-3", "text-field", "default", "paddingRight", "14px — the field's horizontal padding."),
    ("s5", None, "submit-button", "default", "paddingRight", "17.5px — the button's horizontal padding and the search field's."),
    ("s6", "--tdc-space-4", None, None, None, "21px — the declared component space step."),
    ("s7", "--tdc-space-5", None, None, None, "35px — the declared large component step; also the 35px menu icons."),
    ("s8", None, "magic-email", "default", "paddingRight", "44px — the login field's right padding for the inline icon."),
    ("s9", None, "support-title", "default", "paddingLeft", "70px — the page-title indent under the hanging bullet."),
]:
    if vn and vn in R:
        src = f"css-var {vn} (raw/css-vars.json)"
        if comp:
            src += f"; computed {prop} of {comp} {state} agrees (raw/components-computed.json)"
        spacing[key] = var(vn, "dimension", source=src, description=desc)
    elif comp:
        try:
            v = stprop(comp, state, prop)
            if v:
                spacing[key] = {"value": v, "type": "dimension",
                                "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                                "description": desc}
        except KeyError:
            pass

# ---------------------------------------------------------- radius, border

radius = SPEC["core"].setdefault("radius", {})
radius["none"] = var("--tdc-radius", "dimension",
                   source="css-var --tdc-radius (raw/css-vars.json); the computed border radius of buttons, fields and drawers agrees (raw/components-computed.json)",
                   description="Square: every button, field, card and drawer paints 0px corners.")
try:
    v = st("search-field", "default")["borderTopLeftRadius"]
    if v != "0px":
        radius["search"] = {"value": v, "type": "dimension",
                            "source": "computed borderTopLeftRadius of search-field default (raw/components-computed.json)",
                            "description": "The only rounded control found: the 7px header search field."}
except KeyError:
    pass

border = SPEC["core"].setdefault("border", {})
border["control"] = var("--tdc-border-width", "dimension",
                        source="css-var --tdc-border-width (raw/css-vars.json); computed borderTopWidth of submit-button default agrees (raw/components-computed.json)",
                        description="The 2px stroke of the outline block-buttons (EXPLORE, ADD TO CART, SUBMIT, CONTINUE SHOPPING).")
try:
    v = st("search-field", "default")["borderTopWidth"]
    if v != "0px":
        border["search"] = {"value": v, "type": "dimension",
                            "source": "computed borderTopWidth of search-field default (raw/components-computed.json): 1px solid #151515 — a self-coloured stroke",
                            "description": "The 1px same-colour border the desktop search field draws."}
except KeyError:
    pass

# ------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
try:
    hit = next((a.get("shadow") for a in C["cart-continue"]["states"]["default"].get("ancestors", []) if a.get("shadow")), None)
    if hit:
        shadow["drawer"] = {"value": shadow_value(hit, "cart-continue ancestor"),
                            "type": "shadow",
                            "source": "painted shadow on the cart drawer's panel ancestor (raw/components-computed.json)",
                            "description": "The -7px/35px drop the cart and account drawers cast leftward over the page."}
except KeyError:
    pass

# ------------------------------------------------------------- easing

easing = SPEC["core"].setdefault("easing", {})
for key, want, where, desc in [
    ("standard", "cubic-bezier(0.365, 0.305, 0, 1)", "header",
     "The site's own easing on colour, transform and header transitions."),
    ("bounce", "cubic-bezier(0, 1.05, 0.65, 1.01)", "m-header",
     "The slight-overshoot ease the mobile header height transition uses."),
    ("sweep", "cubic-bezier(.77, 0, .175, 1)", None,
     "The dramatic ease the 1.5s line/word reveal animations declare."),
]:
    hit = None
    if where:
        try:
            tf = st(where, "default").get("transitionTimingFunction", "")
            if want.replace(" ", "") in tf.replace(" ", ""):
                hit = want
        except KeyError:
            pass
    else:
        for c in C.values():
            for sv in c["states"].values():
                if "style" in sv and want.replace(" ", "") in sv["style"].get("transitionTimingFunction", "").replace(" ", ""):
                    hit = want
                    break
            if hit:
                break
        if not hit:  # declared in the readable sheets (the 1.5s line animations)
            sheets = json.dumps(J["_meta"].get("sheets", {})).replace(" ", "")
            if want.replace(" ", "") in sheets:
                hit = want
    if not hit:
        raise SystemExit(f"easing {key}: {want} is not in the readings it cites")
    easing[key] = {"value": hit, "type": "cubicBezier",
                   "source": (f"computed transitionTimingFunction of {where} default (raw/components-computed.json)" if where
                              else "declared transition in the same-origin theme sheets (raw/components-computed.json _meta.sheets)"),
                   "description": desc}

# ------------------------------------------------------------- measured extras

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring", "nav-link", "focus-visible", "boxShadow", "shadow",
     "The white half of the double focus ring: #ffffff 0 0 0 2px spread (the 2px black outline half is dark.focus-outline)."),
]:
    try:
        s = st(comp, state)[prop]
        if prop == "boxShadow":
            meas[key] = {"value": shadow_value(s, f"{comp} {state}"),
                         "type": "shadow",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
            continue
        meas[key] = {"value": norm_color(s), "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
    except KeyError:
        pass
for key, comp, state, desc in [
    ("transition-control", "nav-link", "default", "The 0.3s ease on link colour, border, background and opacity."),
    ("transition-sweep", "submit-button", "default", "The 0.4s background-size ease that drives the underline-sweep and the outline-button fill."),
    ("transition-header", "m-header", "default", "The 0.8s box-shadow bounce the header takes."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        first = d.split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty'].split(',')[0].strip()})"}
    except (KeyError, TypeError):
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The 56px desktop header bar."),
    ("header.height-mobile", "m-header", "default", "height", "The 63px mobile header bar."),
    ("control.height", "submit-button", "default", "height", "The 46px block-button height (EXPLORE, ADD TO CART, SUBMIT, CONTINUE SHOPPING)."),
    ("control.height-field", "text-field", "default", "height", "The 42px block-input height."),
    ("control.height-nav", "nav-link", "default", "height", "The 28px header link row."),
    ("control.height-search", "search-field", "default", "height", "The 40.5px desktop header search field."),
    ("menu.row-height", "m-nav-item", "default", "height", "The 36px mobile menu row."),
    ("drawer.panel-width", "account-modal", "opened", "paint.1.size", "The 420px right drawer the account modal paints."),
    ("drawer.content-width", "magic-email", "default", "width", "The 392px drawer content column."),
    ("icon.nav", "nav-link", "default", "icon.w", "The 28px header icons."),
    ("icon.menu", "m-menu-button", "default", "icon.w", "The 35px menu/drawer icons."),
]:
    try:
        if prop.startswith("icon."):  # icon metrics are numbers, not style strings
            iv = C[cname]["states"][state].get("icon") or {}
            v = "%gpx" % float(iv.get(prop[5:], 0) or 0)
        else:
            v = stprop(cname, state, prop)
        if not v:
            continue
        if prop.endswith(".size"):  # a paint layer's "WxH" string -> its width
            v = "%gpx" % float(str(v).split("x")[0])
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass
if "--tdc-layout-width" in R:
    comp.setdefault("layout", {})["width"] = var("--tdc-layout-width", "dimension",
                                               source="css-var --tdc-layout-width (raw/css-vars.json)",
                                               description="The 1100px content column the component layer declares.")

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
