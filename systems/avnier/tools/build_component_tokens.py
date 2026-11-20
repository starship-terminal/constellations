#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

avnier.com is a Shopify storefront on a Dawn-family theme: its palette is the
theme-editor scheme variables --color-base-* declared on :root (raw/css-vars.json's
`app` bin), composed into rgb(var(--x), α) channel triplets, plus --font-*
type settings, --page-width, and --duration-* motion vars. Unlike ASOS the
names are semantic, so each declared colour keeps its own name under a
descriptive core.color.<family> bucket — no role is claimed there.

Roles are only asserted where a measurement backs them: every leaf in the
`light` set resolves through a css var whose resolved value equals the colour
measured on a real component (raw/components-computed.json). The pairings:

  text.primary       --color-base-text            #000  nav/card/field text
  text.inverse       --color-base-solid-button-labels #fff  text on black buttons/header
  text.muted         (no var)  #7a7a7a  plp-title "100 PRODUITS" grey
  surface.page       --color-base-background-1    #fff  page, fields
  surface.subtle     --color-base-background-2    #f3f3f3  alternate scheme
  action.primary     --color-base-accent-1        #000  add-to-cart/login/skip background
  action.primaryText --color-base-solid-button-labels #fff  label on the black buttons
  border.default     (no var)  rgba(0,0,0,.55)    field ring (box-shadow 0 0 0 1px)
  badge.promo        --PredictiveSearchHover      #faf6b5  predictive-search hit highlight

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The theme declares one
light scheme plus .color-inverse/.color-accent-* section schemes that invert
the same two colours; no dark mode exists, so `dark` is empty and the export
holds core and light only.

Not tokenised: --ll-* (Loloyal loyalty app), --swiper-* (vendor sliders),
--payment-terms-*, the empty --navigation-offset-height/--percent helpers.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
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


def val(name):
    if name not in R:
        raise KeyError(name + " not in resolved vars")
    return R[name]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. avnier.com declares "
    "its palette as Shopify scheme custom properties on :root (css-vars.json's "
    "`app` bin); they land under descriptive core.color families. The light "
    "set holds only roles a measurement verified — each resolves through a "
    "var whose value equals a colour read off a live component. The shop "
    "paints one light theme (a .dark probe resolves identically; "
    ".color-inverse sections invert the same two colours), so dark is empty. "
    "A leaf with \"var\" resolves through the live document; \"value\" leaves "
    "are measured on the running page."),
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


def rgb_triplet(name):
    """'0, 0, 0' -> '#000000'."""
    m = re.fullmatch(r"\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*", str(R.get(name, "")))
    if not m:
        return None
    return "#%02x%02x%02x" % tuple(int(g) for g in m.groups())


# ------------------------------------------------------------- core palette
# The declared scheme colours, under descriptive families. Values are rgb()
# channel triplets on :root; record the composed colour.
PALETTE = {
    "neutral": {
        "--color-base-text": "ink",
        "--color-base-background-1": "paper",
        "--color-base-background-2": "wash",
        "--color-base-solid-button-labels": "onInk",
        "--color-base-outline-button-labels": "onPaper",
        "--color-base-accent-1": "accent1",
        "--color-base-accent-2": "accent2",
        "--color-foreground": "foreground",
        "--color-background": "background",
        "--color-button": "button",
        "--color-button-text": "buttonText",
        "--color-link": "link",
        "--color-badge-background": "badgeBg",
        "--color-badge-border": "badgeBorder",
        "--color-card-hover": "cardHover",
    },
    "accent": {
        "--PredictiveSearchHover": "searchHighlight",
    },
}
for fam, names in PALETTE.items():
    for name, alias in sorted(names.items(), key=lambda kv: kv[1]):
        if name not in R:
            continue
        v = rgb_triplet(name) or R[name]
        SPEC["core"].setdefault("color", {}).setdefault(fam, {})[alias] = \
            {"value": v, "type": "color",
             "source": f"css-var {name} ({R[name]})"}

# ------------------------------------------------------------------- fonts
# --font-heading-family is the licensed 'avnier-font' display face (weights
# 500 seen); --font-body-family is Space Mono for everything else.
SPEC["core"]["font"] = {
    "family": {
        "primary": {"value": "'Space Mono', monospace", "type": "fontFamily",
                    "source": "--font-body-family on :root; computed on header/card/field/button text",
                    "description": "Space Mono everywhere — the Avnier workhorse."},
        "display": {"value": "avnier-font", "type": "fontFamily",
                    "source": "--font-heading-family on :root; computed on pdp-title and page titles",
                    "description": "The licensed display face for titles (weight 500, 3% tracking)."},
    },
    "weight": {},
    "size": {},
    "tracking": {},
}
# Read from the components the sources name; they must agree.
for k, comps, src in (("regular", ("m-nav-link", "nav-item", "header"), "computed fontWeight of nav/body text"),
                      ("medium", ("pdp-title",), "computed fontWeight of avnier-font titles")):
    vals = {current(c)["states"]["default"]["style"]["fontWeight"] for c in comps}
    if len(vals) != 1:
        raise ValueError(f"{k}: fontWeight readings differ: {sorted(vals)}")
    SPEC["core"]["font"]["weight"][k] = {"value": vals.pop(), "type": "fontWeight",
                                         "source": f"{src} ({' / '.join(comps)}, raw/components-computed.json)"}
for comp, key, desc in [
    ("card-price", "xxs", "12px uppercase card prices."),
    ("header", "xs", "13px body/nav copy."),
    ("search-toggle", "sm", "14px icons and pills."),
    ("add-to-cart", "base", "15px uppercase button labels."),
    ("pdp-price", "md", "The 15px visible price span (avnier-font); the wrapper reads 18px."),
    ("email-input", "lg", "16px field text."),
    ("cart-title", "display", "188-220px avnier-font page titles."),
]:
    try:
        st0 = C[comp]["states"]["default"]
        fs = (st0.get("textStyle") or {}).get("fontSize") or st0["style"]["fontSize"]
        SPEC["core"]["font"]["size"][key] = {
            "value": fs, "type": "dimension",
            "source": f"computed fontSize of {comp} (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass
for comp, key, desc in [
    ("add-to-cart", "wide", "1px on buttons and pills."),
    ("pdp-price", "wider", "1.3px on the price."),
]:
# (display titles track at 3% — recorded in measurements; a percentage is not a
# DTCG dimension, so it stays out of the token tree.)
    try:
        ls = C[comp]["states"]["default"]["style"]["letterSpacing"]
        SPEC["core"]["font"]["tracking"][key] = {
            "value": ls, "type": "dimension",
            "source": f"computed letterSpacing of {comp} (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------- roles
# Only what a measurement verified (see module docstring for the pairings).
ROLES = {
    "text-primary": "--color-base-text",
    "text-inverse": "--color-base-solid-button-labels",
    "surface-page": "--color-base-background-1",
    "surface-subtle": "--color-base-background-2",
    "surface-inverse": "--color-base-accent-1",
    "action-primary": "--color-base-accent-1",
    "action-primaryText": "--color-base-solid-button-labels",
    "badge-promo": "--PredictiveSearchHover",
}
ROLE_DESC = {
    "text-primary": "rgb(0,0,0) ink on nav, cards, fields and titles — resolved from {v}.",
    "text-inverse": "White text on the black header icons and buttons — resolved from {v}.",
    "surface-page": "The white page and field surface — resolved from {v}.",
    "surface-subtle": "#f3f3f3 alternate scheme wash — resolved from {v}.",
    "surface-inverse": "The black buttons and dark sections — resolved from {v}.",
    "action-primary": "The black buy/action fill (add-to-cart, login, skip link) — resolved from {v}.",
    "action-primaryText": "White labels on black actions — resolved from {v}.",
    "badge-promo": "#faf6b5 predictive-search hit highlight — resolved from {v}.",
}
for role, name in sorted(ROLES.items()):
    if name in R:
        node, last = descend(SPEC["light"], role.split("-"))
        # The declared scheme colours are rgb() channel triplets ("0, 0, 0");
        # emit the composed colour with the var named as its source, or the
        # raw declaration when it is already a colour (#faf6b5).
        node[last] = {"value": rgb_triplet(name) or R[name], "type": "color",
                      "source": f"css-var {name} resolved ({R[name]})",
                      "description": ROLE_DESC[role].format(v=name)}

# ------------------------------------------- measured-only colours (no var)
meas = SPEC["core"].setdefault("measured", {})


def st(comp, state):
    return C[comp]["states"][state]["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


# The pressed-state action colour: a #f4ff7a ::after wipes the black button on
# :active (also painted on the home action's underline).
try:
    v = norm_color(C["add-to-cart"]["states"]["pressed"]["::after"]["backgroundColor"])
    meas["action-pressed"] = {"value": v, "type": "color",
        "source": "computed ::after backgroundColor of add-to-cart pressed (raw/components-computed.json)",
        "description": "The #f4ff7a action yellow painted by the ::after wipe on :active."}
except KeyError:
    pass
for comp, state, key, prop, desc in [
    ("plp-title", "default", "text-muted", "color", "The #7a7a7a count/secondary grey."),
    ("sort-select", "default", "text-faded", "color", "The rgba(0,0,0,.75) dimmed select label."),
    ("email-input", "default", "border-field", "boxShadow", "The rgba(0,0,0,.55) 1px field ring (painted as a shadow; the colour is read out of the shadow value)."),
    ("add-to-cart", "default", "action-text", "color", "The near-white #f6f6f6 label on black buttons."),
]:
    try:
        raw_v = st(comp, state).get(prop, "")
        m_col = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", raw_v)  # a shadow like 'rgba(...) 0 0 0 1px' yields its colour
        v = norm_color(m_col.group(0) if m_col else raw_v)
        if v and v != "transparent" and v != "none":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ layout/motion
lay = SPEC["core"].setdefault("layout", {})
for name, key, desc in [
    ("--page-width", "page-width", "The 160rem max content width."),
    ("--page-width-margin", "page-margin", "The 2rem page gutter."),
]:
    if name in R:
        v = R[name].strip()
        if v and v != "''":
            lay[key] = {"value": v, "type": "dimension",
                        "source": f"css-var {name}", "description": desc}
mot = SPEC["core"].setdefault("motion", {})
for name, key in [("--duration-short", "short"), ("--duration-default", "default"), ("--duration-long", "long")]:
    if name in R:
        mot[key] = {"value": R[name].strip(), "type": "duration",
                    "source": f"css-var {name}",
                    "description": f"The declared {key} duration."}

# ------------------------------------------------------------------ component
comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "add-to-cart", "default", "height", "Buttons are 48px — add-to-cart, login, skip link."),
    ("control.fieldHeight", "email-input", "default", "height", "Login fields are 45px."),
    ("control.fieldWidth", "email-input", "default", "width", "Login fields run 448px."),
    ("control.iconTarget", "search-toggle", "default", "width", "Header icon targets are 40px."),
    ("control.pillWidth", "variant-radio", "default", "width", "A size chip is ~73px."),
    ("header.height", "header", "default", "height", "The desktop header is 60px."),
    ("header.heightMobile", "m-header", "default", "height", "The mobile header is ~51px."),
    ("tile.width", "product-card", "default", "width", "Product cards are 450px at 1440 (3 across)."),
    ("radius.none", "add-to-cart", "default", "borderTopLeftRadius", "Corners are square — 0px everywhere."),
    ("focus.width", "nav-item", "focus-visible", "outlineWidth", "Focus rings, where painted."),
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
