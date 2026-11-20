#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

drinkdouze.com is a Shopify storefront (the Impact-family theme plus a
douze-custom.css layer) in French, painting light only. Its token layer
arrives two ways:

- The theme's settings arrive as an inline :root block of RGB triplets
  (--text-color: 48, 24, 22 …) plus plain roles in the same block
  (--block-border-radius, --button-height …). vars.mjs normalises the
  triplets to hex in the resolved pass. Per-section <style> scopes re-bind
  the same roles (a photo hero paints sable text, a footer paints
  sable-on-photo); those stay in the rule harvest — the resolved pass is
  the :root values.
- douze-custom.css declares the brand layer as ordinary hex/string vars:
  --color-dusk, --color-sable, the --color-flavor-* accents, the
  --font-boogy/--font-robin families and the --text-xxs … --text-9xl
  utility ramp.

Both become {"var": ...} leaves resolved on the single light pass. What the
sheets never declare — the header's painted backdrop, the swatch selected
ring, the Klaviyo-widget chrome — is a measured leaf from
raw/components-computed.json:

  ink          #301816 dusk brown: body ink, heading ink, button fill and
               the sable page's border tone #321a18
  field        #f6f2e9 sable: the boxed-section field; #ffffff root white
               inside the boxed sections' cards and fields
  flavour      #f26554 orange-piment, #f4a765 abricot-zaatar, #f3eea7
               poire-anis — per-product accents re-bound per product card
  type         Boogy 300 display (52-128px, 8vw hero) over Robin Regular
               500 body; the --text-* utility ramp 10-128px
  shape        boxed sections and media 45px, reduced blocks 16px; buttons
               and colour swatches square 0px, pack-size swatches 999px pills
  states       buttons paint a small hover/pressed shadow (rgba(0,0,0,.15)
               0 4px 8px); fields draw an inset 1px dusk ring on focus; the
               pack-size swatch checks with the flavour-accent fill + dusk
               label

A leaf is {"var": "--name"} (resolved on the light pass) or
{"value": ..., "source": "..."} for a measured value. The site paints one
theme: light.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. drinkdouze.com's "
    "Shopify theme declares its colour roles as RGB triplets in an inline "
    ":root block (resolved to hex by vars.mjs) and douze-custom.css declares "
    "the brand layer (--color-dusk/sable/flavor-*, --font-*, the --text-* "
    "ramp) as ordinary vars. Declared variables become var leaves; painted "
    "values the sheets never declare are measured leaves from "
    "raw/components-computed.json."),
    "core": {}, "light": {}, "component": {}}


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


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp [inset], ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    for m in re.finditer(
            r"(inset\s+)?(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?", spec):
        ins1, col, x, y, bl, sp, ins2 = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue
        layer = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                 "blur": f"{bl}px", "spread": f"{sp or 0}px"}
        if ins1 or ins2:  # the fields' focus ring paints inward; keep the keyword
            layer["inset"] = True
        out.append(layer)
    return out


def meas(comp, state, prop, ty, desc, xform=None):
    """A measured leaf; skipped when the component or property was not captured."""
    try:
        v = st(comp, state)[prop]
    except KeyError:
        return None
    if xform:
        v = xform(v)
    if not v or str(v).strip() in ("", "none", "rgba(0, 0, 0, 0)", "0px", "normal"):
        return None
    return {"value": v, "type": ty,
            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
            "description": desc}


def meas_text(comp, state, prop, ty, desc):
    try:
        v = ts(comp, state, prop)
    except KeyError:
        return None
    if not v or str(v).strip() in ("", "none", "normal", "rgba(0, 0, 0, 0)"):
        return None
    return {"value": v, "type": ty,
            "source": f"computed {prop} of {comp} {state} text node (raw/components-computed.json)",
            "description": desc}


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, vname, desc in [
    ("display", "--font-boogy", "Boogy: the display face — hero headlines, section headings, product titles."),
    ("display-italic", "--font-boogy-italic", "Boogy Italic: the italic accent inside display lines (flavour names, emphasis)."),
    ("body", "--font-robin-regular", "Robin Regular: the body, nav, button and form face (weight 500)."),
    ("body-semibold", "--font-robin-semibold", "Robin Semibold: the strong text weight (600) — prices, labels, button text."),
]:
    if vname in R:
        fam[key] = var(vname, "fontFamily", description=desc)

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, vname, desc in [
    ("display", "--heading-font-weight", "The Boogy display weight (300 — a light display cut)."),
    ("body", "--text-font-weight", "Robin body weight (500)."),
    ("bold", "--text-font-bold-weight", "Robin strong weight (600)."),
]:
    if vname in R:
        weight[key] = {"var": vname, "type": "fontWeight", "description": desc}

# ------------------------------------------------------------- brand hues

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, vname, desc in [
    ("dusk", "--color-dusk", "Dusk #301816: the espresso brown — ink, headings, primary fill, borders."),
    ("sable", "--color-sable", "Sable #f6f2e9: the warm sand — page field, boxed sections, text on dark/photo."),
    ("white", "--root-background", "The root white #ffffff: card and field surfaces inside boxed sections."),
    ("border", "--root-border-color", "The border tone #321a18 — dusk lifted a step."),
    ("border-darker", "--border-color-darker", "The muted border #aca3a2 on secondary chrome."),
]:
    if vname in R:
        brand[key] = var(vname, "color", description=desc)

flavor = SPEC["core"].setdefault("color", {}).setdefault("flavor", {})
for key, vname, desc in [
    ("orange-piment", "--color-flavor-orange-piment", "Orange Sanguine & Piment #f26554: the hero SKU's accent — card buttons, swatch accents."),
    ("abricot-zaatar", "--color-flavor-abricot-zaatar", "Abricot & Zaatar #f4a765."),
    ("poire-anis", "--color-flavor-poire-anis", "Poire & Anis #f3eea7."),
]:
    if vname in R:
        flavor[key] = var(vname, "color", description=desc)

status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
for key, vname, desc in [
    ("success-text", "--success-color", "Declared success ink #c7ddc2 (a sage; the theme's success pair reads pale)."),
    ("success-bg", "--success-background", "Success wash #f4f8f3."),
    ("error-text", "--error-color", "Declared error ink — the theme ships the same sage #c7ddc2 here."),
    ("error-bg", "--error-background", "Error wash #fbfdfb."),
    ("in-stock", "--product-in-stock-text-color", "In-stock green #2e9e7b."),
    ("low-stock", "--product-low-stock-text-color", "Low-stock red #df6464."),
    ("sold-out", "--product-sold-out-accent", "Sold-out grey #5b5b5b."),
]:
    if vname in R:
        status[key] = var(vname, "color", description=desc)

label = SPEC["core"].setdefault("color", {}).setdefault("product-label", {})
for key, vname, desc in [
    ("bg", "--product-custom-label-background", "Product label fill #301816."),
    ("text", "--product-custom-label-text-color", "Product label ink #ffffff."),
    ("alt-bg", "--product-custom-label-2-background", "Alt label fill #c7ddc2 sage."),
    ("alt-text", "--product-custom-label-2-text-color", "Alt label ink #000000."),
]:
    if vname in R:
        label[key] = var(vname, "color", description=desc)

# ------------------------------------------------------------ type ramp

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, vname in [
    ("xxs", "--text-xxs"), ("xs", "--text-xs"), ("sm", "--text-sm"),
    ("base", "--text-base"), ("lg", "--text-lg"), ("xl", "--text-xl"),
    ("2xl", "--text-2xl"), ("3xl", "--text-3xl"), ("4xl", "--text-4xl"),
    ("5xl", "--text-5xl"), ("6xl", "--text-6xl"), ("7xl", "--text-7xl"),
    ("8xl", "--text-8xl"), ("9xl", "--text-9xl"),
]:
    if vname in R:
        size[key] = var(vname, "dimension",
                        description=f"The douze-custom utility ramp step {key} (Tailwind-named, Robin/Boogy agnostic).")

head = SPEC["core"].setdefault("font", {}).setdefault("heading-size", {})
for key, vname, desc in [
    ("h1", "--heading-h1-font-size", "Boogy h1 72px at desktop."),
    ("h2", "--heading-h2-font-size", "Boogy h2 52px."),
    ("h3", "--heading-h3-font-size", "Boogy h3 38px."),
    ("h4", "--heading-h4-font-size", "Boogy h4 35px."),
    ("h5", "--heading-h5-font-size", "Boogy h5 12px (the small caps-like step)."),
    ("h6", "--heading-h6-font-size", "Boogy h6 18px."),
    ("large", "--heading-large-font-size", "The display 'large' step — 8vw, resolved 115.2px at 1440."),
    ("small", "--heading-small-font-size", "Heading small 12px."),
    ("xsmall", "--heading-xsmall-font-size", "Heading x-small 12px."),
    ("xxsmall", "--heading-xxsmall-font-size", "Heading xx-small 11px."),
]:
    if vname in R:
        head[key] = var(vname, "dimension", description=desc)

base = SPEC["core"].setdefault("font", {})
if "--base-font-size" in R:
    base["base-size"] = var("--base-font-size", "dimension",
                            description="The theme's base font size 16px.")

# ------------------------------------------------------------------ shape

radius = SPEC["core"].setdefault("radius", {})
for key, vname, desc in [
    ("section", "--section-border-radius", "The boxed-section rounding 45px."),
    ("block", "--block-border-radius", "Block/media rounding 45px."),
    ("block-reduced", "--block-border-radius-reduced", "Reduced block rounding 16px (drawers, small cards)."),
    ("button", "--button-border-radius", "Buttons are square: 0px."),
    ("swatch", "--color-swatch-border-radius", "Colour swatches are square: 0px."),
]:
    if vname in R:
        radius[key] = var(vname, "dimension", description=desc)

# ---------------------------------------------------------------- layout

layout = SPEC["core"].setdefault("layout", {})
for key, vname, desc in [
    ("container-max", "--container-max-width", "Max content width 1600px."),
    ("gutter", "--container-gutter", "Container gutter — 73px at desktop, 24px small."),
    ("grid-gap", "--grid-gap", "The 24px grid gap."),
    ("boxed-margin", "--boxed-sections-margin", "The 25px air around each boxed section."),
    ("breather", "--vertical-breather", "Section vertical padding 64px."),
    ("breather-tight", "--vertical-breather-tight", "Tight section padding 48px."),
    ("product-block-spacing", "--product-list-block-spacing", "Product-list block spacing 48px."),
    ("button-height", "--button-height", "Button height 52px (48px in places)."),
    ("button-small-height", "--button-small-height", "Small button height 44px."),
    ("field-height", "--form-input-field-height", "Form field height 52px."),
    ("field-gap", "--form-input-gap", "Form row gap 16px."),
]:
    if vname in R:
        layout[key] = var(vname, "dimension", description=desc)
# The column count is a count, not a length — as a "dimension" it exports
# "20px", which repeat() cannot read.
if "--grid-column-count" in R:
    layout["grid-columns"] = var("--grid-column-count", "number",
                                 description="The 20-column grid (10 at small widths).")

# -------------------------------------------------------------- light roles

light = SPEC["light"]
for name, desc in [
    ("--text-color", "Body ink — dusk #301816 on sable."),
    ("--heading-color", "Heading ink — the same dusk."),
    ("--background", "The :root page background (white under the boxed sections)."),
    ("--boxed-sections-background", "The boxed-section field — sable #f6f2e9."),
    ("--secondary-background", "The secondary surface — sable again."),
    ("--border-color", "Borders #321a18."),
    ("--primary-button-background", "Primary button fill — dusk."),
    ("--primary-button-text-color", "Text on the primary fill — white."),
    ("--secondary-button-background", "Secondary button fill — dusk too."),
    ("--secondary-button-text-color", "Text on the secondary fill — white."),
    ("--loading-bar-background", "The top loading bar — dusk."),
    ("--play-button-background", "Video play-button disc — white."),
    ("--play-button-arrow", "The play arrow — dusk."),
    ("--product-star-rating", "Star-rating fill — dusk."),
    ("--product-on-sale-accent", "Sale accent — dusk."),
    ("--payment-terms-background-color", "Payment-terms strip — white."),
]:
    if name in R:
        emit(light, name, var(name, "color",
             description=desc + " Declared in the inline :root block."))

# The photo-scoped inverse: a hero or footer section re-binds --text-color to
# sable so type paints light over media. Not a user theme — kept as a small
# inverse group, measured where painted.
inv = light.setdefault("inverse", {})
for key, comp, state, prop, desc in [
    ("text", "hero-title", "default", "color", "Sable text painted over the photo hero (the section re-binds --text-color)."),
    ("surface", "hero-title", "default", "paint", "The painted hero backdrop the inverse text sits on."),
]:
    try:
        v = norm_color(painted(comp, state) if prop == "paint" else st(comp, state)[prop])
        if v and v != "transparent":
            inv[key] = {"value": v, "type": "color",
                        "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------- component tokens

comp = SPEC["component"]

# -- buttons --------------------------------------------------------------
for key, c, state, desc in [
    ("primary", "add-to-cart", "default", "The buy-box submit 'Ajouter au panier' — the primary action."),
    ("hero", "hero-cta", "default", "The hero SHOP button."),
    ("flavor", "quick-add", "default", "The product-card button — its fill re-binds to the flavour accent (#f26554 on Orange Sanguine)."),
]:
    if not have(c, state):
        continue
    s = st(c, state)
    grp = comp.setdefault("button", {}).setdefault(key, {})
    grp["background"] = meas(c, state, "backgroundColor", "color", f"{desc} Fill, normalised.") or grp.get("background")
    grp["text"] = meas_text(c, state, "color", "color", f"{desc} Label ink.") or grp.get("text")
    grp["height"] = meas(c, state, "height", "dimension", f"{desc} Painted height.") or grp.get("height")
    grp["radius"] = meas(c, state, "borderTopLeftRadius", "dimension", f"{desc} Corner radius.") or grp.get("radius")
    grp["font-size"] = meas_text(c, state, "fontSize", "dimension", f"{desc} Label size.") or grp.get("font-size")
    grp["font-weight"] = meas_text(c, state, "fontWeight", "fontWeight", f"{desc} Label weight.") or grp.get("font-weight")
    # The capture records the keyboard state as "focus-visible" (a real
    # Shift+Tab, Tab focus); a listed state that is absent stops the build
    # instead of silently dropping its tokens.
    for stt, leaf in [("hover", "hover"), ("focus-visible", "focus")]:
        if not have(c, stt):
            raise SystemExit(f"{c}: state {stt!r} missing from raw/components-computed.json")
        if (C[c]["states"][stt].get("via") or "") == "focus failed":
            continue  # a failed keyboard focus is not a focus reading
        ss = st(c, stt)
        grp[leaf] = {}
        # Outline readings only export when an outline really paints —
        # computed outlineColor/Width keep their non-none defaults under
        # outlineStyle:none, so gating on the colour alone invents rings.
        props = [("backgroundColor", "color", "fill"), ("color", "color", "ink"),
                 ("borderTopColor", "color", "border"), ("borderTopWidth", "dimension", "border width")]
        ostyle = ss.get("outlineStyle") or "none"
        if ostyle != "none":
            ring = ("outline (style auto: the browser's own focus ring)"
                    if ostyle == "auto" else "outline")
            props += [("outlineColor", "color", ring), ("outlineWidth", "dimension", "outline width")]
        props += [("boxShadow", "shadow", "shadow")]
        for prop, ty, d in props:
            # The focus group carries the ring, plus any fill, ink or border that
            # changes from the default reading; an unchanged one is not a focus token.
            if leaf == "focus" and not prop.startswith(("outline", "boxShadow")) and ss.get(prop) == s.get(prop):
                continue
            m = meas(c, stt, prop, ty, f"{desc} {d}, {stt}.",
                     shadow_layers if ty == "shadow" else None)
            if m:
                grp[leaf][prop.replace("Color", "").replace("Width", "-width").lower() or prop] = m
        if not grp[leaf]:
            del grp[leaf]

# -- nav / header ---------------------------------------------------------
for key, c, desc in [
    ("bar", "announcement-bar", "The top announcement strip."),
    ("header", "header", "The sticky transparent header over the hero."),
    ("link", "nav-link", "A header nav link."),
    ("icon-button", "icon-button", "The newsletter envelope toggle."),
    ("cart-count", "cart-count", "The cart count bubble."),
]:
    if not have(c, "default"):
        continue
    grp = comp.setdefault("nav", {}).setdefault(key, {})
    for prop, ty, d in [("backgroundColor", "color", "fill"), ("color", "color", "ink"),
                        ("height", "dimension", "height"), ("borderTopLeftRadius", "dimension", "radius"),
                        ("borderBottomColor", "color", "bottom border"), ("fontSize", "dimension", "size"),
                        ("fontWeight", "fontWeight", "weight"), ("letterSpacing", "dimension", "tracking")]:
        m = meas(c, "default", prop, ty, f"{desc} Painted {d}.")
        if m:
            grp[prop.replace("Color", "").replace("Width", "-width").lower() or prop] = m

# -- fields ---------------------------------------------------------------
for key, c, desc in [
    ("text", "email-field", "The login email field."),
    ("search", "search-field", "The search input."),
    ("newsletter", "newsletter-field", "The footer Klaviyo email field."),
]:
    if not have(c, "default"):
        continue
    grp = comp.setdefault("field", {}).setdefault(key, {})
    for prop, ty, d in [("backgroundColor", "color", "fill"), ("color", "color", "ink"),
                        ("height", "dimension", "height"), ("borderTopLeftRadius", "dimension", "radius"),
                        ("borderTopColor", "color", "border"), ("borderTopWidth", "dimension", "border width"),
                        ("fontSize", "dimension", "size"), ("paddingLeft", "dimension", "left padding")]:
        m = meas(c, "default", prop, ty, f"{desc} Painted {d}.")
        if m:
            grp[prop.replace("Color", "").replace("Width", "-width").lower() or prop] = m
    if have(c, "focused"):
        grp["focus"] = {}
        props = [("borderTopColor", "color", "border")]
        if (st(c, "focused").get("outlineStyle") or "none") != "none":
            props += [("outlineColor", "color", "outline"),
                      ("outlineWidth", "dimension", "outline width"), ("outlineOffset", "dimension", "outline offset")]
        props += [("boxShadow", "shadow", "ring")]
        for prop, ty, d in props:
            m = meas(c, "focused", prop, ty, f"{desc} Focus {d}.", shadow_layers if ty == "shadow" else None)
            if m:
                grp["focus"][prop.replace("Color", "").replace("Width", "-width").replace("Offset", "-offset").lower() or prop] = m
        if not grp["focus"]:
            del grp["focus"]

# -- swatch / radio -------------------------------------------------------
if have("variant-swatch-2", "default") or have("variant-swatch", "default"):
    c = "variant-swatch-2" if have("variant-swatch-2", "default") else "variant-swatch"
    grp = comp.setdefault("swatch", {})
    grp["background"] = meas(c, "default", "backgroundColor", "color", "Unchecked pack-size swatch fill.")
    grp["text"] = meas_text(c, "default", "color", "color", "Swatch label ink.")
    grp["border"] = meas(c, "default", "borderTopColor", "color", "Swatch border.")
    grp["border-width"] = meas(c, "default", "borderTopWidth", "dimension", "Swatch border width.")
    grp["radius"] = meas(c, "default", "borderTopLeftRadius", "dimension", "Swatch radius.")
    grp["height"] = meas(c, "default", "height", "dimension", "Swatch height.")
    grp = {k: v for k, v in grp.items() if v}
    comp["swatch"] = grp
if have("variant-swatch", "default"):
    sel = comp.setdefault("swatch", {}).setdefault("selected", {})
    sel["background"] = meas("variant-swatch", "default", "backgroundColor", "color", "Checked swatch fill — the flavour accent (#f26554 on Orange Sanguine).")
    sel["text"] = meas_text("variant-swatch", "default", "color", "color", "Checked swatch label ink — dusk.")
    sel["border"] = meas("variant-swatch", "default", "borderTopColor", "color", "Checked swatch border.")
    comp["swatch"]["selected"] = {k: v for k, v in sel.items() if v}

# -- cards / sections -------------------------------------------------------
for key, c, desc in [
    ("product-card", "product-card", "A product-item card in the shop grid."),
    ("login-card", "login-card", "The centred login card."),
    ("empty-state", "cart-empty", "The empty-cart block."),
    ("section", "marquee", "The moving claim banner between boxed sections."),
]:
    if not have(c, "default"):
        continue
    grp = comp.setdefault("card" if "card" in key or key == "empty-state" else "section", {}).setdefault(key.replace("product-", "").replace("-state", ""), {})
    for prop, ty, d in [("backgroundColor", "color", "fill"), ("color", "color", "ink"),
                        ("borderTopLeftRadius", "dimension", "radius"), ("borderTopColor", "color", "border"),
                        ("height", "dimension", "height"), ("fontSize", "dimension", "size")]:
        m = meas(c, "default", prop, ty, f"{desc} Painted {d}.")
        if m:
            grp[prop.replace("Color", "").replace("Width", "-width").lower() or prop] = m

# -- type (measured) --------------------------------------------------------
type_ = comp.setdefault("type", {})
for key, c, state, desc in [
    ("display", "hero-title", "default", "The Boogy hero headline."),
    ("h2", "section-h2", "default", "A boxed-section heading."),
    ("product-title", "pdp-title", "default", "The 60px Boogy product title."),
    ("body", "story-lede", "default", "Robin body text."),
    ("nav", "nav-link", "default", "A header nav link."),
    ("button", "add-to-cart", "default", "Button label type."),
]:
    if not have(c, state):
        continue
    grp = type_.setdefault(key, {})
    for prop, ty, d in [("fontFamily", "fontFamily", "family"), ("fontSize", "dimension", "size"),
                        ("fontWeight", "fontWeight", "weight"), ("lineHeight", "dimension", "leading"),
                        ("letterSpacing", "dimension", "tracking"), ("textTransform", "other", "transform"),
                        ("color", "color", "ink")]:
        m = meas_text(c, state, prop, ty, f"{desc} {d}.")
        if m:
            grp[d.replace(" ", "-")] = m

def prune(node):
    """Drop leaves a missing measurement left as None, and emptied groups."""
    if not isinstance(node, dict):
        return node
    out = {}
    for k, v in node.items():
        if v is None:
            continue
        if isinstance(v, dict):
            v = prune(v)
            if not v:
                continue
        out[k] = v
    return out


SPEC = {k: (prune(v) if isinstance(v, dict) else v) for k, v in SPEC.items()}

RAW.mkdir(exist_ok=True)
(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
n = json.dumps(SPEC).count('"var"') + json.dumps(SPEC).count('"value"')
print(f"component-tokens.json: {n} leaves")
