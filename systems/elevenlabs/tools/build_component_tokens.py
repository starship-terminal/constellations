#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

elevenlabs.io's public signed-out surface is a Next.js + Tailwind 4 app: its
CSS arrives as linked bundles from eleven-public-cdn.elevenlabs.io
(cross-origin to the CSSOM, so vars.mjs reads every body off the network) and
declares a real custom-property layer — the --f-* type ramp, the --spacing-*/
--section-*/--rounded-* layout vars, --eggshell and --page-background-color,
the --font-inter/--font-waldenburg*/--font-geist-mono stacks and the shadcn
HSL triplets — resolved light in raw/css-vars.json. Those become {"var": ...}
leaves resolved by build_tokens.py. Everything else is **measured computed
values** from raw/components-computed.json:

  neutrals    the near-black ink on text and the black pill buttons, the
              #FDFCFC eggshell page field, white card surfaces, muted grey
              secondary text and the #e5e5e5 hairline borders
  brand       the ink action fill (the black Sign up / plan pills) with its
              hover/pressed steps, and the blue accent utility
              (rgb(43 127 255)) the gradients and links paint
  states      ink-wash hovers on ghost controls; focus rings measured off
              focus-visible states
  font        Waldenburg/WaldenburgFH on display and nav, Inter on UI and
              body text, Geist Mono for code
  shape       fully-rounded pills (buttons, tabs, plan CTAs), the
              --rounded-card radius on cards, field radii

A leaf is {"var": ...} (resolved per theme) or {"value": ..., "source": ...}
for a measured value. Only the signed-out public surface was read; every
surface painted light — there is no dark theme or dark island on the public
site, so the export holds core + light only.
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
    "The token tree build_tokens.py turns into tokens.json. elevenlabs.io's "
    "public surface is a Next.js + Tailwind 4 app whose custom-property "
    "layer (raw/css-vars.json — the --f-* type ramp, --spacing-*/"
    "--section-*/--rounded-* layout vars, --eggshell page field, the font "
    "stacks and the shadcn triplets) is var-referenced where it declares a "
    "value, and measured computed values (raw/components-computed.json) "
    "cover the ink/eggshell/white neutrals, the black-pill action ramp, the "
    "state layers, the focus rings, the Waldenburg/Inter/Geist-Mono "
    "families and the pill/card radii. Every public surface painted light "
    "— no dark theme, no dark island — so the export holds core + light "
    "only."),
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


def paint(comp, state, key):
    """A painted child layer's reading — the wash, ring or fill often lives
    on an inner chip, not the measured root (the paint list measure.mjs
    recorded per state)."""
    try:
        for L in C[comp]["states"][state].get("paint") or []:
            if L.get(key):
                return L[key]
    except KeyError:
        pass
    return None


def find_var(value, contains=None):
    """First resolved light var whose value matches."""
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            return n
    return None


def find_var_pat(pat):
    """First resolved light var whose name matches a regex."""
    for n in sorted(R):
        if re.fullmatch(pat, n):
            return n
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default",
     "The Waldenburg display family on the hero headline and headings."),
    ("sans", "nav-trigger", "default",
     "The UI sans the nav, buttons and body text paint (Inter/Waldenburg as the page serves it)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json); the @font-face blocks are served from eleven-public-cdn.elevenlabs.io (raw/css-vars.json fonts)",
                    "description": desc}
# --font-geist-mono lives on the body-class scope (.__variable_*), not :root,
# so it is not in the resolved map: emit the declared stack verbatim.
mono_rule = next((r["properties"]["--font-geist-mono"] for r in V.get("theme", [])
                  if "--font-geist-mono" in r.get("properties", {})), None)
if mono_rule:
    fam["mono"] = {"value": mono_rule.strip(), "type": "fontFamily",
                   "source": "declared --font-geist-mono on .__variable_7e8bea (raw/css-vars.json theme rules)",
                   "description": "The monospace stack (Geist Mono) for code."}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "hero-sub", "default", "The regular body/lede weight."),
    ("medium", "nav-trigger", "default", "The medium weight on nav items and controls."),
    ("semibold", "plan-cta", "default", "The semibold weight on button labels."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        try:
            weights[key] = {"value": int(float(v)), "type": "fontWeight",
                            "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
        except (TypeError, ValueError):
            pass

# ------------------------------------------------------- declared colours

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# The ink action ramp measured off the real pills (the black Sign up / plan
# CTAs), var-referenced where a custom property resolves to the same value.
for key, comp, state, prop, desc in [
    ("ink", "signup-cta", "default", "backgroundColor",
     "The near-black action fill: the Sign up pill, every plan CTA, the playground Play button."),
    ("ink-hover", "signup-cta", "hover", "backgroundColor",
     "The hover step the black pills take."),
    ("ink-pressed", "signup-cta", "pressed", "backgroundColor",
     "The pressed step."),
]:
    try:
        measured = norm_color(st(comp, state)[prop])
        vn = find_var(measured)
        leaf_ = {"type": "color",
                 "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)" + (f"; css-var {vn}" if vn else ""),
                 "description": desc}
        if vn:
            leaf_["var"] = vn
        else:
            leaf_["value"] = measured
        brand[key] = leaf_
    except KeyError:
        pass

# The blue accent the gradients, links and the orb/voice UI paint, declared
# in the Tailwind palette classes or the shadcn layer.
for key, want, contains, desc in [
    ("accent", "#2b7fff", None, "The blue accent (Tailwind blue-500) the gradients, links and interactive UI paint."),
]:
    vn = find_var(want)
    if vn:
        brand[key] = var(vn, "color",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)
    else:
        # look for the value in the harvested palette classes, on any colour property
        hit = next(((k, p) for k, v in sorted((V.get("palette") or {}).items()) for p, pv in v.items()
                    if p != "file" and norm_color(str(pv)) == want), None)
        if hit is None:
            raise SystemExit(f"{key}: {want} is neither a declared var nor in the palette classes")
        brand[key] = {"value": want, "type": "color",
                      "source": f"declared {hit[1]} {want} on the Tailwind utility class .{hit[0]} (raw/css-vars.json palette); the blue of the gradients and links",
                      "description": desc}

def hsl3(v):
    """A shadcn 'H S% L%' channel triplet -> #rrggbb."""
    m = re.fullmatch(r"([\d.]+)\s+([\d.]+)%\s+([\d.]+)%", (v or "").strip())
    if not m:
        return None
    h, s, l = float(m.group(1)) / 360, float(m.group(2)) / 100, float(m.group(3)) / 100
    def f(t):
        k = (t + h * 12) % 12
        a = s * min(l, 1 - l)
        return l - a * max(-1, min(k - 3, 9 - k, 1))
    return "#%02x%02x%02x" % tuple(round(f(x) * 255) for x in (0, 8, 4))


# declared shadcn values — HSL channel triplets, converted here and labelled
for key, pat, desc in [
    ("destructive", r"--shadcn-destructive", "The declared destructive red (hsl 0 84.2% 60.2%)."),
    ("ring", r"--shadcn-ring", "The declared focus-ring colour (hsl 0 0% 3.9% — near-black)."),
]:
    vn = find_var_pat(pat)
    hv = hsl3(R.get(vn, "")) if vn else None
    if hv:
        brand[key] = {"value": hv, "type": "color",
                      "source": f"css-var {vn} resolved light (raw/css-vars.json): an 'H S% L%' channel triplet converted here",
                      "description": desc}

# measured neutrals
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "nav-link", "default", "color",
     "The near-black ink on nav text, headings and button labels."),
    ("muted", "menu-link", "default", "color",
     "The warm grey on flyout links, the product pill, the billing select and secondary text."),
    # signup-submit has no painted ancestor in the reading (the old "ancestor-white"
    # branch fell back to a typed #ffffff); the auth card paints the white itself.
    ("white", "signin-card", "default", "backgroundColor",
     "The #ffffff surface: cards, the flyout panel, the auth card."),
    ("wash-hover", "nav-link", "hover", "paint-bg",
     "The 5% warm-ink wash a nav item's inner chip takes on hover."),
    ("wash-pressed", "oauth-google", "pressed", "paint-bg",
     "The deeper wash a ghost/OAuth button takes on pressed (nav items keep the hover wash)."),
]:
    try:
        if prop == "paint-bg":
            v = norm_color(paint(comp, state, "bg") or "")
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v:
            src = (f"painted {prop.split('-')[1]} of {comp} {state}'s inner layer "
                   f"(raw/components-computed.json paint)" if prop == "paint-bg"
                   else f"computed {prop} of {comp} {state} (raw/components-computed.json)")
            neutral[key] = {"value": v, "type": "color",
                            "source": src,
                            "description": desc}
    except KeyError:
        pass

# declared neutrals from the custom-property layer
for key, pat, desc in [
    ("eggshell", r"--eggshell", "The #FDFCFC eggshell page field."),
    ("page-bg", r"--page-background-color", "The page background role, bound to --eggshell."),
]:
    vn = find_var_pat(pat)
    if vn:
        neutral[key] = var(vn, "color",
                           source=f"css-var {vn} resolved light (raw/css-vars.json)",
                           description=desc)
# --shadcn-border is an 'H S% L%' triplet (hsl 0 0% 89.8% = #e5e5e5): convert it.
for key, pat, desc in [
    ("border", r"--shadcn-border", "The declared hairline border grey (hsl 0 0% 89.8%)."),
]:
    vn = find_var_pat(pat)
    hv = hsl3(R.get(vn, "")) if vn else None
    if hv:
        neutral[key] = {"value": hv, "type": "color",
                        "source": f"css-var {vn} resolved light (raw/css-vars.json): an 'H S% L%' channel triplet converted here",
                        "description": desc}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink on light."),
    ("--text-muted", "color.neutral.muted", "Secondary text on light."),
    ("--surface-page", "color.neutral.eggshell", "The #FDFCFC eggshell page field."),
    ("--surface-card", "color.neutral.white", "Cards, the flyout panel, the auth card."),
    ("--action-primary", "color.brand.ink", "The near-black action fill."),
    ("--action-primary-hover", "color.brand.ink-hover", "The hover step."),
    ("--action-primary-pressed", "color.brand.ink-pressed", "The pressed step."),
    ("--text-on-action", "#ffffff", "White labels on the ink fill."),
    ("--accent", "color.brand.accent", "The blue accent on gradients, links and interactive UI."),
    ("--border", "color.neutral.border", "The hairline border grey."),
    ("--state-hover", "color.neutral.wash-hover", "The hover wash on ghost controls."),
    ("--state-pressed", "color.neutral.wash-pressed", "The pressed wash."),
]:
    if target.startswith("{"):
        continue
    root_bag = target.split(".")[1] if "." in target else None
    root_key = target.split(".")[-1]
    bag = {"neutral": neutral, "brand": brand}.get(root_bag)
    if bag and root_key in bag:
        emit(light, name, {"value": "{" + target + "}", "type": "color",
                           "source": ALIAS, "description": desc})
    elif root_bag is None:
        emit(light, name, {"value": target, "type": "color",
                           "source": "computed color of the ink action labels (raw/components-computed.json)",
                           "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "The hero display size."),
    ("display", "pricing-h1", "default", "The page-title display (pricing)."),
    ("display-tts", "tts-display", "default", "The product-page display (text-to-speech)."),
    ("display-mobile", "m-hero", "default", "The display size at 390 wide."),
    ("h2", "section-h2", "default", "The section heading."),
    ("page-title", "api-h1", "default", "The API page title."),
    ("lede", "hero-sub", "default", "The hero lede."),
    ("body", "tts-textarea", "default", "The playground textarea/body size."),
    ("menu-item", "m-nav-item", "default", "The mobile-menu rows."),
    ("control", "plan-cta", "default", "The control/button text."),
    ("meta", "plan-badge", "default", "The small meta/badge text."),
    ("price", "plan-price", "default", "The plan price figure."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "Hero display leading."),
    ("display", "pricing-h1", "default", "Page-title leading."),
    ("h2", "section-h2", "default", "Heading leading."),
    ("lede", "hero-sub", "default", "Lede leading."),
    ("body", "tts-textarea", "default", "Body leading."),
    ("control", "plan-cta", "default", "Control leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, layout

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "signup-cta", "default", "borderTopLeftRadius", "The pill radius on buttons and CTAs (likely 9999px)."),
    ("button-ghost", "contact-sales", "default", "borderTopLeftRadius", "The ghost-button radius."),
    ("field", "email-field", "default", "borderTopLeftRadius", "The auth-field radius."),
    ("tab", "tool-tab", "default", "borderTopLeftRadius", "The showcase-tab radius."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
for key, pat, desc in [
    ("card", r"--rounded-card", "The declared card radius."),
    ("card-sm", r"--rounded-card-sm", "The declared small-card radius."),
]:
    vn = find_var_pat(pat)
    if vn:
        radius[key] = var(vn, "dimension",
                          source=f"css-var {vn} resolved light (raw/css-vars.json)",
                          description=desc)

space = SPEC["core"].setdefault("space", {})
for key, pat, desc in [
    ("inset", r"--spacing-inset", "The declared inset padding (1.25rem)."),
    ("gutter", r"--spacing-gutter", "The declared content gutter."),
    ("section-md", r"--section-py-md", "The declared medium section vertical padding (5rem at desktop)."),
]:
    vn = find_var_pat(pat)
    if vn:
        space[key] = var(vn, "dimension",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring-light", "signup-cta", "focus-visible", "outlineColor", "color", "The keyboard focus ring on light surfaces."),
    ("focus-ring-nav", "nav-trigger", "focus-visible", "paint-outline", "color", "The keyboard ring on nav controls — drawn on the inner chip, not the root (whose 2px outline stays transparent)."),
    ("card-shadow", "tts-card", "default", "boxShadow", "shadow", "The elevation the playground card paints."),
]:
    try:
        if prop == "boxShadow":
            s = st(comp, state)[prop]
            layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
            layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
            if layers:
                meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                             "type": "shadow",
                             "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if prop == "paint-outline":
            # the ring lives on the inner chip; the root keeps a transparent
            # 2px frame, so take the first layer whose outline isn't alpha-0
            raw = ""
            try:
                for L in C[comp]["states"][state].get("paint") or []:
                    o = L.get("outline") or ""
                    if o and "rgba(0, 0, 0, 0)" not in o:
                        raw = o
                        break
            except KeyError:
                pass
            m = re.search(r"rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8}", raw)
            v = norm_color(m.group(0)) if m else None
            if v:
                meas[key] = {"value": v, "type": ty,
                             "source": f"painted outline of {comp} {state}'s inner layer (raw/components-computed.json paint): {raw}",
                             "description": desc}
        elif have(comp, state, prop):
            v = norm_color(st(comp, state)[prop])
            if v and v != "none":
                meas[key] = {"value": v, "type": ty,
                             "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
    except KeyError:
        pass
for key, comp, state, desc in [
    ("control-transition", "plan-cta", "default", "The control transition (background-color etc.)."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        first = d.split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
# pressed buttons may scale
try:
    d0 = C["plan-cta"]["states"]["default"]["rect"]["w"]
    dp = C["plan-cta"]["states"]["pressed"]["rect"]["w"]
    if d0 and dp and dp < d0:
        meas["pressed-scale"] = {"value": round(dp / d0, 4), "type": "number",
                                 "source": "pressed rect / default rect of plan-cta (raw/components-computed.json)",
                                 "description": "The scale a pressed button takes."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "plan-cta", "default", "height", "The standard button height (plan CTAs)."),
    ("button-nav.height", "signup-cta", "default", "height", "The header action height."),
    ("field.height", "email-field", "default", "height", "The auth-field height."),
    ("field-playground.height", "tts-textarea", "default", "height", "The playground textarea height."),
    ("navcontrol.height", "nav-trigger", "default", "height", "The header control height."),
    ("menurow.height", "m-nav-item", "default", "height", "The mobile-menu row."),
    ("header.height", "nav", "default", "height", "The desktop nav height."),
    ("header.height-mobile", "m-header", "default", "height", "The mobile header height."),
    ("flyout.height", "nav-dropdown", "default", "height", "The Products flyout panel height."),
    ("plancard.height", "plan-card", "default", "height", "The plan card height."),
    ("authcard.height", "signin-card", "default", "height", "The sign-in card height."),
    ("playgroundcard.height", "tts-card", "default", "height", "The playground card height."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# Readings the selector took from another element (the README's What to distrust
# lists them, each needing a recapture): every leaf that cites one says so.
WRONG = {
    "menu-link": "its default and pressed states caught a same-href link far down the page, not the flyout's",
}


def note_wrong(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, what in WRONG.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and f"{k}: read from the wrong element" not in src:
                    node["source"] = src = src + f"; {k}: read from the wrong element ({what}); recapture needed"
        for v in node.values():
            note_wrong(v)


note_wrong(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
