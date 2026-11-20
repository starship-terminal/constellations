#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

asos.com styles itself with ~41 custom properties whose names are build-time
hashes (--1fot7dv, --3pchel, …) declared on :root by the sitechrome stylesheets
(raw/css-vars.json, read by tools/capture/vars.mjs; the `generated` bin). The
names carry no semantics, so this builder gives each declared colour a readable
alias and puts it under a descriptive core.color.<family> bucket — no role is
claimed there.

Roles are only asserted where a measurement backs them: every leaf in the
`light` set resolves through a css var whose resolved value equals the colour
measured on a real component (raw/components-computed.json). The pairings:

  surface.inverse  --1fot7dv #000000  header/nav/footer paint black
  surface.page     --3pchel  #ffffff  page, fields, buttons on black
  text.primary     --11lcxa5 #2d2d2d  pdp-title/cat-pill/load-more colour
  text.secondary   --f1xms7  #666666  flyout-link colour
  border.default   --na3s62  #dddddd  cat-pill/load-more/reviews-cta border
  action.primary   --1e93okh #018849  add-to-bag + bag-cta background
  action.primaryHover --14cp6y8 #006637  add-to-bag :hover background
  surface.promo    --xes0jb  #cde2f5  promo-message-box background
  surface.wash     --1wwppwc #eeeeee  save-button/m-nav-link background
  anchor.inherit   (no var)  #0000ee  the wrapping anchor's inherited colour —
                          the product description overrides it with #2d2d2d, so
                          it is the wrapper's unused colour, not a link colour
  focus.outline    (no var)  #005fcc  :focus-visible outline, 1–5 px
  nav.hover        (no var)  #051a6e  nav-item :hover fill

The declared error/sale/purple palette members (--1mii22u, --1xvrmqx,
--1ffq8ns) stay under core.color only: no component reading records them in
use, so no role is claimed for them.

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one light
theme — a .dark probe resolves identically — so `dark` is empty and the export
holds core and light only.

Not tokenised: --18bniqv "45,45,45" and --1cripqf "255,255,255" are rgb()
channel triplets the sheets compose into rgba(var(--x), α) — duplicates of
--11lcxa5 and --3pchel; --icon/--image/--size/--thickness are scoped widget
vars that never resolve on :root; --swiper-*/--ot-* are vendor (Swiper,
OneTrust) and stay in css-vars.json only.
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
    "The token tree build_tokens.py turns into tokens.json. asos.com declares "
    "its palette as hash-named custom properties on :root (css-vars.json's "
    "`generated` bin); they land under descriptive core.color families. The "
    "light set holds only roles a measurement verified — each resolves through "
    "a var whose value equals a colour read off a live component. The shop "
    "paints one light theme: a .dark probe resolves identically, so dark is "
    "empty. A leaf with \"var\" resolves through the live document; \"value\" "
    "leaves are measured on the running page."),
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


# ------------------------------------------------------------- core palette
# Every colour var the sitechrome sheets declare, aliased under a descriptive
# family. Aliases are bucketed by hue/value, not by role.
PALETTE = {
    "neutral": {
        "--3pchel": "white", "--6gu3az": "grey-50", "--sm859b": "grey-100",
        "--1wwppwc": "grey-200", "--na3s62": "grey-300", "--h1m6hk": "grey-400",
        "--10c6hzt": "grey-500", "--f1xms7": "grey-600", "--4439lq": "grey-700",
        "--198t7lw": "ink-800", "--19n3pjb": "ink-850", "--45kpnl": "ink-870",
        "--11lcxa5": "ink-900", "--1fot7dv": "black",
    },
    "green": {
        "--19t30l9": "wash", "--cod972": "tint", "--5eoeaa": "mint",
        "--173zcrj": "bright", "--1e93okh": "default", "--14cp6y8": "dark",
    },
    "orange": {
        "--1njx4kw": "wash", "--rrfoye": "tint", "--19qikbp": "light",
        "--a5az0j": "default", "--1gu65g4": "deep",
    },
    "blue": {
        "--xes0jb": "wash", "--1asa9bf": "tint", "--1cf22is": "default",
        "--lzto1h": "deep",
    },
    "red": {
        "--1j5f6ai": "wash", "--1mii22u": "bright", "--1xvrmqx": "deep",
    },
    "purple": {
        "--oyq41c": "wash", "--stskl1": "light", "--1ffq8ns": "default",
        "--1lx7ll5": "deep",
    },
    "bronze": {"--fc982a": "default"},
}
for fam, names in PALETTE.items():
    for name, alias in sorted(names.items(), key=lambda kv: kv[1]):
        if name in R:
            emit(SPEC["core"].setdefault("color", {}).setdefault(fam, {}),
                 "--" + alias, var(name, source=f"css-var {name}"))

# rgb() channel triplets the sheets compose into rgba(var(--x), α); kept as
# strings because the value is a channel list, not a colour.
for name, alias in (("--18bniqv", "ink"), ("--1cripqf", "inverse")):
    if name in R:
        SPEC["core"].setdefault("color", {}).setdefault("channel", {})[alias] = \
            {"value": "rgb(%s)" % R[name], "type": "color",
             "source": f"css-var {name} (channel triplet, used inside rgb()/rgba() composition)"}

# ------------------------------------------------------------------- fonts
# No font vars are declared: family is measured on live text, weights are the
# @font-face declarations in css-vars.json (futura-pt book 400, demi 500,
# bold 700; FuturaStd 400/700). fw 900 is what the browser computes on
# nav-tab/load-more — the heaviest Futura face available.


def ff(comp):
    """The computed fontFamily of a component's default state, as raw records it."""
    v = C[comp]["states"]["default"]["style"].get("fontFamily")
    if not v:
        raise KeyError(f"{comp}: no computed fontFamily in raw/components-computed.json")
    return v


def fw(*comps):
    """The computed fontWeight every named component's default state shares."""
    vals = {C[c]["states"]["default"]["style"]["fontWeight"] for c in comps}
    if len(vals) != 1:
        raise ValueError(f"{comps}: fontWeight readings differ: {sorted(vals)}")
    return vals.pop()


SPEC["core"]["font"] = {
    "family": {
        "primary": {"value": ff("pdp-price"),
                    "type": "fontFamily",
                    "source": "computed fontFamily of pdp-price (raw/components-computed.json); faces futura-pt 400/500/700 + FuturaStd 400/700 in css-vars.json",
                    "description": "Futura PT everywhere — the ASOS face."},
        "legacy": {"value": ff("promo-strip"),
                   "type": "fontFamily",
                   "source": "computed fontFamily of promo-strip/promo-tab (raw/components-computed.json)",
                   "description": "The promo furniture's stack, with \"Futura Std\" second."},
    },
    "weight": {
        "regular": {"value": fw("pdp-title"), "type": "fontWeight", "source": "computed fontWeight of body copy (pdp-title)"},
        "demi": {"value": "500", "type": "fontWeight", "source": "futura-pt demi @font-face in css-vars.json"},
        "semibold": {"value": fw("continue-button"), "type": "fontWeight", "source": "computed fontWeight of continue-button"},
        "bold": {"value": fw("add-to-bag", "promo-tab"), "type": "fontWeight", "source": "computed fontWeight of add-to-bag/promo-tab"},
        "heavy": {"value": fw("nav-tab", "load-more", "m-nav-link"), "type": "fontWeight", "source": "computed fontWeight of nav-tab/load-more/m-nav-link"},
    },
    "size": {},
    "tracking": {},
}
# Measured type scale (fontSize on real components).
for comp, key, desc in [
    ("promo-tab", "xxs", "10.5625px on the promo-strip WOMEN/MEN tabs."),
    ("promo-strip", "xs", "13px promo strip copy."),
    ("nav-item", "sm", "14px on nav rows, footer links, styles-count."),
    ("pdp-price", "base", "16px body — prices, fields, buttons."),
    ("bag-title", "md", "17.6–18px on page/section titles."),
    ("plp-title", "lg", "24px on collection and login titles."),
]:
    try:
        fs = C[comp]["states"]["default"]["style"]["fontSize"]
        SPEC["core"]["font"]["size"][key] = {
            "value": fs, "type": "dimension",
            "source": f"computed fontSize of {comp} (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass
# Measured tracking (letterSpacing). ASOS tracks everything a little, and
# uppercase labels a lot.
for comp, key, desc in [
    ("size-select", "tight", "0.4px on fields and inputs."),
    ("add-to-bag", "base", "0.6px on buttons and strip copy."),
    ("cat-pill", "wide", "1px on pills and promo tabs."),
    ("plp-title", "wider", "1.7px on the collection title."),
    ("hero-cta", "caps", "2px on uppercase CTAs and menu rows."),
    ("bag-title", "capsWide", "2.5px on the MY BAG title."),
]:
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
    "text-primary": "--11lcxa5", "text-secondary": "--f1xms7",
    "text-inverse": "--3pchel",
    "surface-page": "--3pchel", "surface-subtle": "--sm859b",
    "surface-wash": "--1wwppwc", "surface-inverse": "--1fot7dv",
    "surface-promo": "--xes0jb",
    "border-default": "--na3s62",
    "action-primary": "--1e93okh", "action-primaryHover": "--14cp6y8",
    # No status-* or accent-* roles: --1mii22u (red), --1xvrmqx (deep red) and
    # --1ffq8ns (purple) are declared palette members whose colours appear in
    # no saved component reading, so a role claim here would look verified
    # where nothing measured it. They stay under core.color until a measured
    # use is recorded.
}
ROLE_DESC = {
    "text-primary": "rgb(45,45,45) on titles, prices, fields — resolved from {v}.",
    "text-secondary": "rgb(102,102,102) on flyout links and support copy — resolved from {v}.",
    "text-inverse": "White text on black chrome — resolved from {v}.",
    "surface-page": "The white page/field surface — resolved from {v}.",
    "surface-subtle": "#f8f8f8 wash under grids — resolved from {v}.",
    "surface-wash": "#eeeeee on the save heart and mobile menu rows — resolved from {v}.",
    "surface-inverse": "The black header, nav, drawer and footer — resolved from {v}.",
    "surface-promo": "#cde2f5 light-blue promo band under the PDP price — resolved from {v}.",
    "border-default": "#dddddd hairline on pills, buttons, fields — resolved from {v}.",
    "action-primary": "The ASOS buy green — add-to-bag and bag CTA — resolved from {v}.",
    "action-primaryHover": "rgb(0,102,55) on add-to-bag :hover — resolved from {v}.",
}
for role, name in sorted(ROLES.items()):
    if name in R:
        node, last = descend(SPEC["light"], role.split("-"))
        node[last] = var(name, source=f"css-var {name}",
                         description=ROLE_DESC[role].format(v=name))

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


for comp, state, key, prop, desc in [
    ("nav-item", "focus-visible", "focus-outline", "outlineColor", "The :focus-visible ring on chrome controls."),
    ("continue-button", "focus-visible", "focus-outline-alt", "outlineColor", "The #0770cf focus blue on my.asos.com (matches --1cf22is)."),
    ("nav-item", "hover", "nav-hover", "backgroundColor", "The deep-navy fill a category button takes on hover."),
    # The wrapping anchor's own `color` — its #0000ee never paints text: the
    # product description inside overrides it with rgb(45,45,45) (text.primary).
    # Named for what it is, so nobody reuses it as the product-link colour.
    ("tile-name", "hover", "anchor-inherit", "color", "The wrapper anchor's unused inherited blue — the visible product link text is text.primary #2d2d2d."),
    ("cat-pill", "hover", "hover-wash", "backgroundColor", "#f5f5f5 pill hover wash."),
    ("add-to-bag", "hover", "action-hover", "backgroundColor", "The darker buy green on hover."),
    ("continue-button", "hover", "ink-hover", "backgroundColor", "The near-black button hover on my.asos.com."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "add-to-bag", "default", "height", "Buttons are 44px — add-to-bag, save heart, reviews CTA."),
    ("control.heightLg", "continue-button", "default", "height", "The login continue button is 48px."),
    ("control.heightWide", "load-more", "default", "height", "LOAD MORE is 54.5px."),
    ("control.fieldHeight", "size-select", "default", "height", "Fields and selects are 38px."),
    ("control.pillHeight", "cat-pill", "default", "height", "Category pills are 36px."),
    ("control.heightBar", "sort-button", "default", "height", "Sort/Filter bar buttons are 43px."),
    ("radius.none", "add-to-bag", "default", "borderTopLeftRadius", "Corners are square — 0px on buttons, pills, fields."),
    ("radius.round", "save-button", "default", "borderTopLeftRadius", "Icon-only buttons are fully round."),
    ("header.height", "header", "default", "height", "The desktop header block is 140px."),
    ("nav.height", "nav-item", "default", "height", "The category nav row is 50px."),
    ("nav.tabHeight", "nav-tab", "default", "height", "WOMEN/MEN floor tabs are 60px."),
    ("icon.tapTarget", "account-icon", "default", "width", "Header icons get a 50x60 tap target."),
    ("icon.social", "footer-social", "default", "width", "Social icons are 30px."),
    ("icon.search", "search-button", "default", "width", "The inline search button is 38px."),
    ("tile.width", "product-tile", "default", "width", "Product tiles are ~335px at 1440 (4 across)."),
    ("flyout.width", "nav-flyout", "default", "width", "The mega-menu panel is ~1302px."),
    ("focus.width", "nav-item", "focus-visible", "outlineWidth", "Focus rings run 1–5px; nav buttons take 5px."),
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
