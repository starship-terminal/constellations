#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

arket.com is a Next.js + Tailwind v4 storefront; its stylesheet declares a
@theme layer on :root (raw/css-vars.json, read by tools/capture/vars.mjs):

  --color-beige/--black/--white/--grey-dark/--grey-mid/--grey-light/
    --grey-light-extra        the base palette: the warm page beige, ink and
                              a four-step grey ramp
  --color-blue/--red/--green/--alert-*/--peach/--overlay-*/--barbour-green/
    --ingrid-border/--laila-* links, status, overlay and campaign colours
  --spacing-0..--spacing-680  the rem spacing scale (0..680px resolved)
  --text-12..--text-60        the type scale (12..60px)
  --leading-*, --tracking-tighter/--tracking-wide
                              line heights and letter spacing
  --radius-1/-4/-6/-8/-12/-DEFAULT/-full/-none
                              the radius scale (2px DEFAULT, 99990px full)
  --ease-in/-out/-in-out, --default-transition-*
                              motion tokens (150ms default)
  --container-*, --font-regular/--font-small-caps, --font-weight-*
                              layout maxima, the arketSansMono /
                              arketSCSansMono families and weights
  --animate-*, --drop-shadow-input
                              keyframe presets and the input drop shadow

The site paints one light theme (the .dark probe changes nothing), so the
dark set is not emitted. A leaf is {"var": "--name"} (resolved by
build_tokens.py) or {"value": ..., "source": "..."} for a measured value.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def val(name):
    if name not in R:
        raise KeyError(name + " not in resolved vars")
    return R[name]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. arket.com is a "
    "Next.js + Tailwind v4 storefront declaring its whole design language in "
    "the @theme layer: the --color-* palette (beige, ink, grey ramp, alert "
    "and campaign hues), the --spacing-*/--text-*/--leading-*/--radius-*/"
    "--tracking-*/--container-* scales, the --ease-*/--default-transition-* "
    "motion tokens and the arketSansMono/arketSCSansMono families. The light "
    "set holds the site's roles; measured values that no variable declares "
    "(button and drawer sizes) come from raw/components-computed.json. "
    "\"var\" leaves resolve through the live document; \"value\" leaves are "
    "measured."),
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


# --------------------------------------------------------------- core ramps

KIND = {"color": "color", "dimension": "dimension", "fontFamily": "fontFamily",
        "duration": "duration", "easing": "cubicBezier", "number": "number",
        "shadow": "other"}

for name in sorted(n for n in R if n.startswith("--")):
    if name.startswith(("--tw-", "--toastify-")):
        continue
    kind = RL[name].get("kind")
    ty = KIND.get(kind, "other")
    if name.startswith("--color-"):
        emit(SPEC["core"], name, var(name, "color"))
    elif name.startswith("--spacing-"):
        emit(SPEC["core"], name, var(name, "dimension"))
    elif name.startswith("--text-"):
        emit(SPEC["core"], name, var(name, "dimension"))
    elif name.startswith("--leading-"):
        emit(SPEC["core"], name, var(name, "dimension"))
    elif name.startswith("--radius-"):
        emit(SPEC["core"], name, var(name, "dimension"))
    elif name.startswith("--tracking-"):
        emit(SPEC["core"], name, var(name, "other"))
    elif name.startswith("--container-"):
        emit(SPEC["core"], name, var(name, "dimension"))
    elif name.startswith("--ease-"):
        emit(SPEC["core"], name, var(name, "cubicBezier"))
    elif name == "--default-transition-duration":
        emit(SPEC["core"], name, var(name, "duration"))
    elif name == "--default-transition-timing-function":
        emit(SPEC["core"], name, var(name, "cubicBezier"))
    elif name.startswith("--animate-"):
        emit(SPEC["core"], name, var(name, "other"))
    elif name.startswith("--font-weight-"):
        emit(SPEC["core"], name, var(name, "fontWeight"))
    elif name == "--font-regular":
        SPEC["core"].setdefault("font", {}).setdefault("family", {})["ui"] = var(
            name, "fontFamily", description="arketSansMono: the one family the storefront paints, with an Arial-metric fallback.")
    elif name == "--font-small-caps":
        SPEC["core"].setdefault("font", {}).setdefault("family", {})["small-caps"] = var(
            name, "fontFamily", description="arketSCSansMono: the small-caps mono used on chips and counts like the \"+2\" colour marker.")
    else:
        emit(SPEC["core"], name, var(name, ty))

# ------------------------------------------------------------- light roles

def _norm(v):
    """rgb()/rgba() -> #hex, or rgba(r, g, b, a) when translucent."""
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", (v or "").strip())
    if not m:
        return (v or "").strip().lower()
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
    return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"


def _rd(reads, prop):
    """The computed value every (component, state) named here reads; refuse a missing or stale
    component and readings that disagree, instead of typing the value in."""
    vals = set()
    for comp, state in reads:
        c = C[comp]
        if c.get("missing") or c.get("recaptureMissed"):
            raise KeyError(comp)
        vals.add(_norm(c["states"][state]["style"][prop]))
    if len(vals) != 1:
        raise ValueError(f"{reads} {prop}: readings differ: {sorted(vals)}")
    return vals.pop()


LIGHT = [
    ("page", var("--color-white", description="The page field: pure white.")),
    ("surface", var("--color-beige", description="The warm ARKET beige (#faf8f3): notice and promo bands, editorial washes.")),
    ("surface-2", var("--color-grey-light", description="The light grey panel tone (#f5f5f5).")),
    ("field", var("--color-grey-light-extra", description="The input fill (#f9f9f9), e.g. the header search field.")),
    ("text", var("--color-black", description="The ink: pure black text and black button fills.")),
    ("muted", var("--color-grey-dark", description="Secondary ink (#767676): field borders, placeholders-as-border, helper text.")),
    ("accent", var("--color-blue", description="The link/action blue (#0851bd), used sparingly.")),
    ("border", var("--color-grey-mid", description="The hairline (#eaeae8): nav drawers, dividers, footer rules.")),
    ("border-strong", var("--color-ingrid-border", description="The darker hairline (#b4b4b4) used on stronger dividers.")),
    ("ink", var("--color-black", description="Primary button fill (consent CTAs, filter hover, continue).")),
    ("on-ink", var("--color-white", description="Text on the black buttons.")),
    ("danger", var("--color-red", description="Sale/error red (#d80404).")),
    ("success", var("--color-green", description="Confirmation green (#389d47), e.g. the location notice check.")),
    ("info", var("--color-blue", description="Informational blue.")),
    ("focus-ring", {"value": _rd([(k, "focus-visible") for k, c in C.items()
                                  if "style" in (c.get("states", {}).get("focus-visible") or {})
                                  and c["states"]["focus-visible"].get("via") != "focus failed"
                                  and not c.get("missing") and not c.get("recaptureMissed")], "outlineColor"), "type": "color",
                    "source": "computed outlineColor on keyboard focus (raw/components-computed.json); arket.com declares no :focus-visible style of its own, so this is the browser's default 1px auto ring, not a product token",
                    "description": "The browser-default 1px #005fcc auto outline every measured control shows on keyboard focus."}),
    ("overlay", var("--color-overlay-beige", description="The warm dimmer behind drawers and dialogs (rgba(164,155,112,0.2)).")),
    ("sale", var("--color-alert-red", description="Alert red (#c12d0d) alongside --color-red.")),
]
for key, leaf in LIGHT:
    SPEC["light"][key] = leaf

# ------------------------------------------------------------------ type + shape

def st(comp, state):
    c = C[comp]
    # A component that was not found on the last run carries missing (no
    # states) or recaptureMissed (earlier states kept under their own
    # provenance): neither is a current reading, so refuse it as a source.
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def tstyle(key, comp, state, desc):
    s = st(comp, state)
    fam = s["fontFamily"].split(",")[0].strip('"')
    small = "SCSansMono" in fam or "SC" in fam
    return {
        "fontFamily": "{font.family.small-caps}" if small else "{font.family.ui}",
        "fontSize": s["fontSize"],
        "lineHeight": s["lineHeight"],
        "fontWeight": int(s["fontWeight"]),
        # computed "normal" is no tracking; DTCG wants a px or rem dimension, so 0px, not 0em
        "letterSpacing": "0px" if s.get("letterSpacing") in (None, "normal") else s["letterSpacing"],
    }, f"computed type of {comp} {state} (raw/components-computed.json); {desc}"


typo = SPEC["core"].setdefault("typography", {})
for key, comp, state, desc in [
    ("display", "plp-title", "default", "the 28px category/hero heading"),
    ("title", "tile-label", "default", "the 22px campaign tile label"),
    ("body", "nav-item", "default", "the 16px UI line (nav, prices, buttons)"),
    ("button", "consent-accept", "default", "the 20px large-CTA label"),
    ("small", "more-colors", "default", "the small-caps chip text (\"+2\")"),
]:
    try:
        v, src = tstyle(key, comp, state, desc)
        typo[key] = {"$value": v, "$type": "typography", "$extensions": {"source": src}}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "filter-button", "default", "height", "Outlined controls (Filter/Sort/View) are 32px."),
    ("control.buttonLarge", "consent-accept", "default", "height", "The large consent CTA is 56px."),
    ("control.field", "search-field", "default", "height", "The header search field is 40px."),
    ("control.gateField", "gate-field", "default", "height", "The account gate field is 60px."),
    ("control.iconButton", "card-img-prev", "default", "height", "The card carousel arrows are 36px."),
    ("nav.height", "nav-item", "default", "height", "Nav items are 30px."),
    ("shell.header", "header", "default", "height", "The sticky header block at 1440."),
    ("drawer.width", "cart-drawer", "default", "width", "Drawers (cart, filter, location) are 538px at 1440."),
    ("consent.width", "consent-card", "default", "width", "The consent card is ~344px."),
    ("footer.linkHeight", "footer-link", "default", "height", "Footer link rows."),
    ("menu.linkHeight", "m-nav-link", "default", "height", "The 52px mobile menu rows."),
]:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
