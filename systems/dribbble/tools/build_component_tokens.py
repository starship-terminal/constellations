#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dribbble.com is a Rails app in three CSS eras, and the signed-out page paints a
single light surface. The token layer it actually declares is Shoelace's: the
--sl-* custom properties harvested into raw/css-vars.json (tools/capture/vars.mjs),
with the --sl-color-primary-* ramp re-bound to the Dribbble pink (#ea4c89) and
the neutral/gray/danger ramps, radii, spacing, shadows, transitions and focus
ring alongside. Those become {"var": ...} leaves resolved in the light pass.

Most of the signed-out surface is styled by the older mini-master bundle —
Mona Sans, hardcoded hex and px — so the values the visitor actually sees are
**measured** leaves from raw/components-computed.json:

  ink          #0d0c22 near-black text/headings; #060318 button ink;
               #6e6d7a muted text on the directory and feeds
  pink         #ea4c89 primary: the search Go circle, the hero accent word,
               checklist ticks and the PRO badges; #f082ac the hover tint
  surfaces     #ffffff page and cards; #f8f8fc the promo strip and directory
               chips; #fbfbfc the designer-card work-strip field
  type         Mona Sans at 52px/600 on the hero down to 12px tags; Source
               Serif 4 and IBM Plex Mono are served faces on newer surfaces
  shape        8px card and chip radii, 12px on the big search field, 20px
               pill buttons, a 40px circle on the pink search Go, 50% avatars
  states       focus rings from --sl-focus-ring-* (Shoelace); hovers are
               measured state deltas

A leaf is {"var": "--name"} (resolved in the light pass by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
theme: the dark set holds the ink surfaces the light page paints (the dark
Log-in / Get-in-touch pills and the dark certified chip) — not a user toggle.
The only declared dark scope (body.dark re-binding the third-party Algolia
autocomplete vars) stays in raw/css-vars.json as evidence, not a theme.
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
    "The token tree build_tokens.py turns into tokens.json. dribbble.com's "
    "declared token layer is the Shoelace --sl-* set (its "
    "--sl-color-primary-* ramp re-bound to the Dribbble pink) harvested into "
    "raw/css-vars.json; the Rails-era mini-master styles that paint most of "
    "the signed-out surface hold their values inline, so they are measured "
    "leaves from raw/components-computed.json. Declared variables become var "
    "leaves; painted colours, geometry and the Mona Sans stack are measured "
    "leaves. The dark set names the ink surfaces painted inside the light "
    "page (dark pills, the certified chip), not a user theme."),
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


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp, ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    for m in re.finditer(
            r"(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?", spec or ""):
        col, x, y, bl, sp = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue
        out.append({"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                    "blur": f"{bl}px", "spread": f"{sp or 0}px"})
    return out


# ------------------------------------------------------------------- fonts
# Mona Sans is the painted product stack (served via the Fontshare API CSS);
# Source Serif 4 and IBM Plex Mono are the served faces on the newer surfaces.
# The Shoelace layer declares its own fallback stacks. Every family named by a
# served @font-face is recorded under core.font.face as provenance.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-title", "default", "fontFamily"):
    fam["sans"] = {"value": st("hero-title", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of hero-title default (raw/components-computed.json)",
                   "description": "Mona Sans: headings, body, nav, buttons — the product stack."}
elif have("header", "default", "fontFamily"):
    fam["sans"] = {"value": st("header", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of header default (raw/components-computed.json)",
                   "description": "Mona Sans: the product stack."}
for key, vname, desc in [
    ("shoelace-sans", "--sl-font-sans", "The Shoelace sans fallback stack (declared)."),
    ("shoelace-serif", "--sl-font-serif", "The Shoelace serif stack (declared)."),
    ("shoelace-mono", "--sl-font-mono", "The Shoelace mono stack (declared)."),
]:
    if vname in R:
        fam[key] = var(vname, "fontFamily", description=desc)

faces = SPEC["core"].setdefault("font", {}).setdefault("face", {})
for f in V.get("fonts", []):
    name = (f.get("font-family") or "").strip("'\"")
    if not name:
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    w = f.get("font-weight", "")
    sty = f.get("font-style", "")
    faces[slug] = {"value": name, "type": "fontFamily",
                   "source": f"@font-face declared in {f.get('file')} (raw/css-vars.json)",
                   "description": f"Served face {name}"
                                  + (f" {w}" if w else "")
                                  + (f" {sty}" if sty and sty != "normal" else "")
                                  + " (provenance: the font file, not a stack)."}

# ------------------------------------------------------- declared neutrals
# Shoelace ramps: --sl-color-primary-* is re-bound to the Dribbble pinks;
# neutral/gray are the greys; the hue ramps feed status roles.

core_col = SPEC["core"].setdefault("color", {})
primary = core_col.setdefault("pink", {})
for n in ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]:
    vname = f"--sl-color-primary-{n}"
    if vname in R:
        primary[n] = var(vname, "color",
                         description=f"Declared --sl-color-primary-{n} — the Shoelace primary ramp re-bound to the Dribbble pink ({R.get(vname)}).")

neutral = core_col.setdefault("neutral", {})
for n in ["0", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950", "1000"]:
    vname = f"--sl-color-neutral-{n}"
    if vname in R:
        neutral[n] = var(vname, "color", description=f"Declared --sl-color-neutral-{n}.")

gray = core_col.setdefault("gray", {})
for n in ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]:
    vname = f"--sl-color-gray-{n}"
    if vname in R:
        gray[n] = var(vname, "color", description=f"Declared --sl-color-gray-{n}.")

hue = core_col.setdefault("hue", {})
for gname in ["red", "orange", "amber", "yellow", "lime", "green", "emerald",
              "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
              "fuchsia", "pink", "rose"]:
    for n in ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]:
        vname = f"--sl-color-{gname}-{n}"
        if vname in R:
            hue.setdefault(gname, {})[n] = var(vname, "color",
                                             description=f"Declared --sl-color-{gname}-{n}.")

# Shoelace's declared status ramps (danger/success/warning — no info ramp
# exists on the site). They are raw hues, not semantic fill/text/border roles:
# the signed-out page never paints them.
status = core_col.setdefault("status", {})
for sname in ["danger", "success", "warning"]:
    for n in ["50", "100", "200", "300", "400", "500", "600", "700"]:
        vname = f"--sl-color-{sname}-{n}"
        if vname in R:
            status.setdefault(sname, {})[n] = var(vname, "color",
                                                  description=f"Declared --sl-color-{sname}-{n} — a ramp step, never painted signed out.")

# ---------------------------------------------------------- measured colours
# The mini-master values the page actually paints — never declared as vars.

meas_col = core_col.setdefault("measured", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-title", "default", "color", "The %v near-black product ink (headings, body)."),
    ("ink-deep", "login-btn", "default", "bg", "The %v deep ink the dark pills fill."),
    ("ink-on-dark", "login-btn", "default", "color", "White text on the dark pills."),
    ("muted", "designer-meta", "default", "color", "The %v muted meta tone."),
    ("muted-2", "profile-stat", "default", "color", "The %v lighter muted stat tone."),
    ("pink", "search-go", "default", "bg", "The %v Dribbble pink: search Go, accents, PRO badges."),
    ("pink-hover", "search-go", "hover", "bg", "The hover tint on the pink action."),
    ("promo-surface", "promo-banner", "default", "bg", "The %v promo-strip fill."),
    ("chip-surface", "skill-chip", "default", "bg", "The light skill-chip fill."),
    ("chip-dark", "skill-chip-dark", "default", "bg", "The dark certified-chip fill (Webflow Expert)."),
    ("chip-dark-text", "skill-chip-dark", "default", "color", "Text on the dark certified chip."),
    ("field-bg", "email-field", "default", "bg", "The auth field fill."),
    ("field-border", "email-field", "default", "borderTopColor", "The auth field border tone."),
    ("card-border", "shot-card", "default", "borderTopColor", "The shot-card hairline, if painted — the wrapper's border width is 0, so this emits nothing."),
    ("pill-border", "login-btn", "default", "borderTopColor", "The dark pill's painted 1px border (same ink as its fill)."),
    ("pink-text", "hero-accent", "default", "text:color", "The pink the rotating hero word paints."),
    ("link", "menu-link", "default", "color", "The header dropdown link ink."),
    ("footer-bg", "footer", "default", "bg", "The footer field, if painted."),
    ("footer-text", "footer-link", "default", "color", "The footer link tone."),
]:
    try:
        # "text:<prop>" reads the first text node's computed style (ts), not
        # the wrapper's — a rotating-word container inherits the page ink
        # while the word inside paints the pink.
        if prop == "bg":
            raw_v = painted(comp, state)
            src = f"computed bg of {comp} {state} (raw/components-computed.json)"
        elif prop.startswith("text:"):
            raw_v = ts(comp, state, prop[5:])
            src = f"computed {prop[5:]} of the text node inside {comp} {state} (raw/components-computed.json)"
        else:
            raw_v = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        # A border colour is only evidence when a border is painted: a 0-width
        # or 'none' border's colour is an unpainted declaration, not a reading.
        if prop.startswith("border") and prop.endswith("Color"):
            side = prop[len("border"):-len("Color")]
            s = st(comp, state)
            w = s.get(f"border{side}Width", "0px")
            if s.get(f"border{side}Style") == "none" or not float((w or "0px").replace("px", "") or 0):
                continue
        v = norm_color(raw_v)
        if v and v not in ("transparent", "rgba(0, 0, 0, 0)"):
            meas_col[key] = {"value": v, "type": "color", "source": src, "description": desc}
    except (KeyError, TypeError, ValueError):
        pass

# ------------------------------------------------------------ light roles

# The page/surface/border reads, so the roles below resolve. A missed probe leaves the
# role out (no typed white fallback).
for key, comp, state, prop, desc in [
    ("page", "promo-banner", "default", "page-bg", "The white page field."),
    ("surface", "designer-card", "default", "paint", "Card white."),
    ("border", "email-field", "default", "borderTopColor", "The field hairline %v."),
]:
    try:
        if prop == "page-bg":
            v = norm_color(next((n.get("bg") for n in reversed(C[comp]["states"][state].get("ancestors", [])) if n.get("bg")), None))
        elif prop == "paint":
            v = norm_color(painted(comp, state))
        else:
            # Only a painted border (width > 0, style not none) yields a colour.
            if prop.startswith("border") and prop.endswith("Color"):
                side = prop[len("border"):-len("Color")]
                s = st(comp, state)
                w = s.get(f"border{side}Width", "0px")
                if s.get(f"border{side}Style") == "none" or not float((w or "0px").replace("px", "") or 0):
                    continue
            v = norm_color(st(comp, state)[prop])
        if v and v not in ("transparent", "rgba(0, 0, 0, 0)"):
            meas_col[key] = {"value": v, "type": "color",
                             "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
    except (KeyError, TypeError):
        pass
ALIAS = "role alias over the palette"
MEASURED = "measured role off the live page (raw/components-computed.json)"

light = SPEC["light"]
roles = light.setdefault("color", {})
for key, ref, src, desc in [
    ("page", "{color.measured.page}", MEASURED, "The white page field."),
    ("surface", "{color.measured.surface}", MEASURED, "Card and panel white."),
    ("surface-alt", "{color.measured.promo-surface}", MEASURED, "The promo/chip %v tint."),
    ("text", "{color.measured.ink}", MEASURED, "The %v product ink."),
    ("muted", "{color.measured.muted}", MEASURED, "The %v muted text."),
    ("accent", "{color.measured.pink}", MEASURED, "The %v Dribbble pink."),
    ("accent-hover", "{color.measured.pink-hover}", MEASURED, "The pink hover tint."),
    ("on-accent", "{color.measured.ink-on-dark}", MEASURED, "White on pink and on the dark pills."),
    ("border", "{color.measured.border}", MEASURED, "The %v field/card hairline."),
    ("link", "{color.measured.link}", MEASURED, "The link ink (same near-black, underlined on hover)."),
]:
    if ref[1:-1].split(".")[-1] in meas_col:  # alias only a reading that exists
        roles[key] = {"value": ref, "type": "color", "source": src, "description": desc}

# -------------------------------------------------------------- dark set
# Not a user theme: the ink surfaces the light page paints (the dark Log-in,
# Start-Your-Project-Brief and Get-in-touch pills, the dark certified chip).

dark = SPEC["dark"]
droles = dark.setdefault("color", {})
for key, comp, state, prop, ref, desc in [
    ("surface", "login-btn", "default", "bg", "{color.measured.ink-deep}", "The dark pill fill (%v)."),
    ("text", "login-btn", "default", "color", "{color.measured.ink-on-dark}", "Text on the ink pills."),
    ("surface-chip", "skill-chip-dark", "default", "bg", "{color.measured.chip-dark}", "The dark certified-chip fill."),
]:
    try:
        v = norm_color(painted(comp, state) if prop == "bg" else st(comp, state)[prop])
        if v and ref[1:-1].split(".")[-1] in meas_col:
            droles[key] = {"value": ref, "type": "color", "source": ALIAS, "description": desc}
    except (KeyError, TypeError):
        pass

# ------------------------------------------------------------- type scale

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in ["2x-small", "x-small", "small", "medium", "large", "x-large",
          "2x-large", "3x-large", "4x-large"]:
    vname = f"--sl-font-size-{n}"
    if vname in R:
        size[n] = var(vname, "dimension", description=f"Declared --sl-font-size-{n}.")
# measured steps the Shoelace scale does not map to
for key, comp, state, desc in [
    ("hero", "hero-title", "default", "The 52px Mona Sans hero."),
    ("h1-page", "search-h1", "default", "The page h1 (search/directory title)."),
    ("body", "designer-meta", "default", "The 14px card meta text."),
    ("meta", "stat-count", "default", "The 12-13px count/tag size."),
    ("mobile-hero", "m-hero", "default", "The hero size at 390px."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        size[key] = {"value": v, "type": "dimension",
                     "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for n in ["denser", "dense", "normal", "loose", "looser"]:
    vname = f"--sl-line-height-{n}"
    if vname in R:
        leading[n] = var(vname, "number", description=f"Declared --sl-line-height-{n}.")
v = ts("hero-title", "default", "lineHeight")
if v:
    leading["hero"] = {"value": v, "type": "dimension",
                       "source": "computed lineHeight of hero-title default (raw/components-computed.json)",
                       "description": "The hero leading (62.4px on 52px)."}

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for n in ["denser", "dense", "normal", "loose", "looser"]:
    vname = f"--sl-letter-spacing-{n}"
    if vname in R:
        # Shoelace declares letter-spacing in em — a font-size multiplier, not
        # a fixed length — so it lands as a number token, not a dimension.
        # R prefers the resolved pixel value, which freezes the scale to the
        # probe's font size; read the raw declaration instead.
        decl = str(RL[vname].get("raw", R[vname])).strip()
        m = re.fullmatch(r"(-?\d*\.?\d+)em", decl)
        if m:
            tracking[n] = {"value": float(m.group(1)), "type": "number",
                           "source": f"css-var {vname} (light); declared value {decl} is em",
                           "description": f"Declared {vname} as an em multiplier on font size."}
        elif decl == "normal":
            tracking[n] = {"value": 0, "type": "number",
                           "source": f"css-var {vname} (light); declared 'normal' — the font's own spacing",
                           "description": f"Declared {vname} ('normal'): zero extra tracking."}
        else:
            tracking[n] = var(vname, "dimension", description=f"Declared --sl-letter-spacing-{n}.")

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for n in ["thin", "extra-light", "light", "normal", "medium", "semibold",
          "bold", "extra-bold", "black"]:
    vname = f"--sl-font-weight-{n}"
    if vname in R:
        weight[n] = var(vname, "fontWeight", description=f"Declared --sl-font-weight-{n}.")
for key, comp, state, desc in [
    ("hero", "hero-title", "default", "The 600 hero weight."),
    ("button", "login-btn", "default", "The button label weight."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        try:
            weight[key] = {"value": int(float(v)), "type": "fontWeight",
                           "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
        except ValueError:
            pass

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for n, desc in [
    ("small", "Declared --sl-border-radius-small (2px)."),
    ("medium", "Declared --sl-border-radius-medium (4px)."),
    ("large", "Declared --sl-border-radius-large (8px)."),
    ("x-large", "Declared --sl-border-radius-x-large (16px)."),
]:
    vname = f"--sl-border-radius-{n}"
    if vname in R:
        radius[n] = var(vname, "dimension", description=desc)
for n in ["circle", "pill"]:
    vname = f"--sl-border-radius-{n}"
    if vname in R:
        if str(R[vname]).strip().endswith("%"):
            # A percentage radius is a shape rule, not a length: kept as the
            # declared value under a non-standard type.
            radius[n] = {"value": str(R[vname]).strip(), "type": "other",
                         "source": f"css-var {vname} (light)",
                         "description": f"Declared {vname} ({R[vname]}): a percentage radius — half the element's own size, not a fixed length."}
        else:
            radius[n] = var(vname, "dimension", description=f"Declared --sl-border-radius-{n}.")
for key, comp, state, desc in [
    ("card", "shot-card", "default", "The 8px shot-card radius."),
    ("field", "email-field", "default", "The input radius."),
    ("search", "home-search", "default", "The big search field radius (12px)."),
    ("button-pill", "login-btn", "default", "The pill radius on header/dark buttons: a 10000000px cap, so the ends are fully round."),
    ("chip", "tag-chip", "default", "The tag-chip radius."),
    ("search-go", "search-go", "default", "The pink Go circle (50%)."),
]:
    if have(comp, state, "borderTopLeftRadius"):
        rv = st(comp, state)["borderTopLeftRadius"]
        src = f"computed borderTopLeftRadius of {comp} {state} (raw/components-computed.json)"
        if str(rv).strip() == "0px":
            # A wrapper can paint square while a layer inside it carries the
            # visible corner radius (the shot card's thumbnail overlay): read
            # the first non-percentage layer radius as the card's shape.
            hit = next((p for p in (C[comp]["states"][state].get("paint") or [])
                        if p.get("radius") and not str(p["radius"]).endswith("%")), None)
            if hit:
                rv = str(hit["radius"]).split()[0]
                src = f"computed borderRadius of {hit['node']} inside {comp} {state} (raw/components-computed.json)"
        if str(rv).strip().endswith("%"):
            radius[key] = {"value": str(rv).strip(), "type": "other",
                           "source": src,
                           "description": desc + " A percentage radius — relative to the element's own size."}
        else:
            radius[key] = {"value": rv, "type": "dimension",
                           "source": src,
                           "description": desc}

# No --sl-easing-* variables exist on the site; motion easings are measured
# per component (the cubic-bezier curves in raw/measurements.md).

duration = SPEC["core"].setdefault("duration", {})
for n in ["x-slow", "slow", "medium", "fast", "x-fast"]:
    vname = f"--sl-transition-{n}"
    if vname in R:
        duration[n] = var(vname, "duration", description=f"Declared --sl-transition-{n}.")

# ------------------------------------------------------------- space, layout

spacing = SPEC["core"].setdefault("spacing", {})
for n in ["3x-small", "2x-small", "x-small", "small", "medium", "large",
          "x-large", "2x-large", "3x-large", "4x-large"]:
    vname = f"--sl-spacing-{n}"
    if vname in R:
        spacing[n] = var(vname, "dimension", description=f"Declared --sl-spacing-{n}.")

# No --sl-border-width-* scale exists on the site; only the input and panel
# border widths are declared.
border_w = SPEC["core"].setdefault("border", {}).setdefault("width", {})
for key, vname in [("input", "--sl-input-border-width"), ("panel", "--sl-panel-border-width")]:
    if vname in R:
        border_w[key] = var(vname, "dimension", description=f"Declared {vname}.")

zidx = SPEC["core"].setdefault("zIndex", {})
for n in ["drawer", "dialog", "dropdown", "toast", "tooltip"]:
    vname = f"--sl-z-index-{n}"
    if vname in R:
        zidx[n] = var(vname, "number", description=f"Declared --sl-z-index-{n}.")
# dribbble's own --zi-* stacking scale, declared at :root; the calc()
# composites (--zi-shot-overlay = header + 1, and above) resolve to calc
# strings the browser evaluates — their declared expressions are in
# raw/css-vars.json; only literal numbers become tokens.
for key, vname, desc in [
    ("header", "--zi-header", "Declared --zi-header (9996): the site nav layer."),
    ("dropdown", "--zi-dropdown", "Declared --zi-dropdown (1000)."),
    ("filter", "--zi-filter", "Declared --zi-filter (1000)."),
    ("jobs-bg-effect", "--zi-jobs-bg-effect", "Declared --zi-jobs-bg-effect (10)."),
    ("playbook-head", "--zi-playbook-head", "Declared --zi-playbook-head (2)."),
]:
    if vname in R and isinstance(R[vname], (int, float)):
        zidx[key] = var(vname, "number", description=desc)

# --------------------------------------------------- dribbble declared layer
# The btn2/site-nav/input :root bindings — dribbble's own component variables,
# a second declared layer beside Shoelace's.

drb = SPEC["core"].setdefault("dribbble", {})
for key, vname, ty, desc in [
    ("button.height", "--btn-height", "dimension", "Declared --btn-height (40px): the standard button height."),
    ("button.font-size", "--btn-font-size", "dimension", "Declared --btn-font-size (13px)."),
    ("button.padding", "--btn-padding", "dimension", "Declared --btn-padding (20px horizontal)."),
    ("button.icon-size", "--btn-icon-size", "dimension", "Declared --btn-icon-size (16px)."),
    ("button.bg", "--btn-bg-color", "color", "Declared --btn-bg-color (#0d0c22): the dark pill fill."),
    ("button.bg-hover", "--btn-bg-color-hover", "color", "Declared --btn-bg-color-hover (#3d3d4e)."),
    ("button.border", "--btn-border-color", "color", "Declared --btn-border-color (the fill colour)."),
    ("button.border-hover", "--btn-border-color-hover", "color", "Declared --btn-border-color-hover."),
    ("button.text", "--btn-text-color", "color", "Declared --btn-text-color (white)."),
    ("button.text-hover", "--btn-text-color-hover", "color", "Declared --btn-text-color-hover (white)."),
    ("nav.height", "--site-nav-height", "dimension", "Declared --site-nav-height (92px with the announcement strip; 58px bare)."),
    ("nav.gutter", "--site-nav-gutter", "dimension", "Declared --site-nav-gutter (40px)."),
    ("nav.search-height", "--site-nav-search-height", "dimension", "Declared --site-nav-search-height (56px)."),
    ("nav.link-hover", "--site-nav-link-hover-color", "color", "Declared --site-nav-link-hover-color (#7b7194)."),
    ("header.total-height", "--total-header-height", "dimension", "Declared --total-header-height (nav + flash + announcement = 92px)."),
    ("banner.gutter", "--banner-gutter", "dimension", "Declared --banner-gutter (72px at desktop)."),
    ("input.padding-left", "--input-padding-left", "dimension", "Declared --input-padding-left (12px)."),
    ("input.padding-right", "--input-padding-right", "dimension", "Declared --input-padding-right (12px)."),
    ("clearable-input.size", "--clearable-input-size", "dimension", "Declared --clearable-input-size (16px)."),
    ("clearable-input.padding", "--clearable-input-padding", "dimension", "Declared --clearable-input-padding (8px)."),
    ("attachment.max-height", "--attachment-max-height", "dimension", "Declared --attachment-max-height (252px)."),
    ("attachment.min-height", "--attachment-min-height", "dimension", "Declared --attachment-min-height (100px)."),
]:
    if vname in R:
        node = drb
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = var(vname, ty, description=desc)


def declared_on(sel_part, vname):
    """The literal value a rule scoped to a selector declares — evidence when a
    variable never resolves on <body> because it is component-scoped."""
    for r in V.get("theme", []) + V.get("app", []):
        if sel_part in r["selector"] and vname in r["properties"]:
            return r["properties"][vname].strip("'\"")
    return None


# Layout values declared on page scopes (never on :root, so unresolved above):
# the 1650px home/designers container and the 72px container gutter.
layout = SPEC["core"].setdefault("layout", {})
for key, sel, vname, desc in [
    ("container-max-home", ".home-header", "--container-max-width", "Declared --container-max-width on .home-header (1650px)."),
    ("container-max-designers", "body#designers", "--container-max-width", "Declared --container-max-width on the designers directory body (1622px)."),
    ("container-gutter", ".container2--large-fill", "--container-gutter", "Declared --container-gutter at ≥1200px (72px)."),
]:
    v = declared_on(sel, vname)
    if v:
        layout[key] = {"value": v, "type": "dimension",
                       "source": f"declared {vname} on {sel} (raw/css-vars.json)",
                       "description": desc}


# ----------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
for n in ["x-small", "small", "medium", "large", "x-large"]:
    vname = f"--sl-shadow-{n}"
    if vname in R:
        layers = shadow_layers(R[vname])
        if layers:
            shadow[n] = {"value": layers, "type": "shadow",
                         "source": f"css-var {vname} (light)",
                         "description": f"Declared --sl-shadow-{n}."}
for key, comp, state, desc in [
    ("card", "designer-card", "default", "The designer-card elevation."),
    ("dropdown", "nav-dropdown", "default", "The header dropdown elevation."),
]:
    try:
        layers = shadow_layers(st(comp, state)["boxShadow"])
        if layers:
            shadow[key] = {"value": layers, "type": "shadow",
                           "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ---------------------------------------------------------------- focus ring

focus = SPEC["core"].setdefault("focusRing", {})
for n, ty, desc in [
    ("color", "color", "Declared --sl-focus-ring-color."),
    ("width", "dimension", "Declared --sl-focus-ring-width."),
    ("offset", "dimension", "Declared --sl-focus-ring-offset."),
]:
    vname = f"--sl-focus-ring-{n}"
    if vname in R:
        focus[n] = var(vname, ty, description=desc)
if "--sl-focus-ring-style" in R:
    focus["style"] = {"value": R["--sl-focus-ring-style"], "type": "fontFamily",
                      "source": "css-var --sl-focus-ring-style (light)",
                      "description": "Declared --sl-focus-ring-style (the 'solid' keyword; typed fontFamily only to carry a plain string)."}
# measured focus outline on a real control
for comp in ("login-btn", "search-go", "tag-chip", "nav-trigger"):
    try:
        s = st(comp, "focus-visible")
        if s.get("outlineStyle") == "solid" and s.get("outlineWidth") and s["outlineWidth"] != "0px":
            focus.setdefault("measured", {})["color"] = {
                "value": norm_color(s["outlineColor"]), "type": "color",
                "source": f"computed outline of {comp} focus-visible (raw/components-computed.json)",
                "description": f"The {s['outlineWidth']} solid {norm_color(s['outlineColor'])} keyboard-focus outline."}
            focus["measured"]["width"] = {"value": s["outlineWidth"], "type": "dimension",
                "source": f"computed outlineWidth of {comp} focus-visible (raw/components-computed.json)",
                "description": "The focus outline width."}
            break
    except KeyError:
        continue

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The desktop header height."),
    ("header.height-mobile", "m-header", "default", "height", "The mobile header height."),
    ("logo.width", "logo", "default", "width", "The script wordmark width."),
    ("button.height", "login-btn", "default", "height", "The dark pill button height."),
    ("button.radius", "login-btn", "default", "borderTopLeftRadius", "The pill radius."),
    ("nav-link.height", "nav-link", "default", "height", "Nav item height."),
    ("dropdown.width", "nav-dropdown", "default", "width", "The Explore dropdown panel width."),
    ("hero-title.width", "hero-title", "default", "width", "The hero heading measure."),
    ("hero-cta.height", "hero-cta", "default", "height", "The Start-Your-Project-Brief pill height."),
    ("search.height", "home-search", "default", "height", "The big search field height."),
    ("search.radius", "home-search", "default", "borderTopLeftRadius", "The big search field radius."),
    ("search-go.size", "search-go", "default", "height", "The 40px pink Go circle."),
    ("chip.height", "tag-chip", "default", "height", "The tag-chip height."),
    ("shot-card.width", "shot-card", "default", "width", "The shot-card width in the feed."),
    ("wall-cta.height", "wall-cta", "default", "height", "The Sign-up-to-continue pill height."),
    ("designer-card.width", "designer-card", "default", "width", "The directory designer-card width."),
    ("designer-cta.height", "designer-cta", "default", "height", "The Get-in-touch pill height."),
    ("skill-chip.height", "skill-chip", "default", "height", "The skill-chip height."),
    ("auth-card.width", "login-card", "default", "width", "The login card width."),
    ("field.height", "email-field", "default", "height", "Auth input height."),
    ("field.radius", "email-field", "default", "borderTopLeftRadius", "Auth input radius."),
    ("continue.height", "continue-btn", "default", "height", "The Continue button height."),
    ("footer.height", "footer", "default", "height", "The footer block height."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# transitions worth naming
meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, desc in [
    ("dropdown-transition", "nav-dropdown", "default", "The Explore dropdown open transition."),
    ("card-transition", "shot-card", "default", "The shot-card hover transition."),
]:
    try:
        s = st(comp, state)
        d = (s.get("transitionDuration") or "").split(",")[0].strip()
        if d and d != "0s":
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s.get('transitionProperty')})"}
    except (KeyError, TypeError):
        pass

# A description that names its own value says "%v" and is filled from the leaf (through
# its alias), so a recapture cannot leave the prose naming an old colour.
def fill_values(node):
    if isinstance(node, dict):
        d = node.get("description")
        if isinstance(d, str) and "%v" in d:
            v = node["value"]
            m = re.fullmatch(r"\{color\.measured\.([\w-]+)\}", str(v))
            node["description"] = d.replace("%v", str(meas_col[m.group(1)]["value"] if m else v))
        for x in node.values():
            fill_values(x)


fill_values(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
