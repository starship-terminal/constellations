#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

creativemarket.com's public signed-out surface is a Rails storefront with a
Vue island layer, themed `data-theme="legacy"`. Its Sass sheets are served
from the cross-origin d3ui957tjb5bqd.cloudfront.net CDN, so vars.mjs
harvests the custom properties out of the network responses
(raw/css-vars.json): the `--default-*` globals on :root and
html[data-theme="legacy"] plus ~130 component-scoped vars — the
`.ui-button--*` skins (`--_color` #088178 teal / #4e42a1 accent, with
`--_color-hover` and `--_color-soft`), the `.ui-select` states, the dialog
and `--user-dropdown-*`/`--overflow-dropdown-*` menus, and the
Overlayscrollbar metrics.

Those become {"var": ...} leaves resolved by build_tokens.py. Measured
computed values (raw/components-computed.json) pin what the vars do not:

  type       Averta at 600 for every heading (72px membership hero,
             48px page h1, 36px sign-in, 24px product h1), 400 at 13-16px UI
  buttons    #088178 teal fill + white text, 8px radii (buy-now is the
             white/teal inverse), the #4e42a1 Save 25% accent, 44-52px tall
  surfaces   white page, #fafdff fields, #fee4c3 chips, #dff8f6 washes
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. creativemarket.com's public surface is a Rails/Vue storefront under data-theme=\"legacy\" whose declared --default-*/ui-button var layer (raw/css-vars.json, resolved under the one painted theme) is var-referenced wherever it names a value, and measured computed values (raw/components-computed.json) cover the rest: the Averta ramp (72/48/36/24px 600 headings, 13-16px UI), the #088178 teal button fills and #4e42a1 accents on white text, the 8px control and 16px card radii, the 20-32px pills, the white page and #fafdff fields."),
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

# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
fam["averta"] = var("--default-font-family", "fontFamily",
    source="css-var --default-font-family resolved (raw/css-vars.json); every measured component computes fontFamily Averta (raw/components-computed.json)",
    description="Averta (self-hosted webfont, raw/css-vars.json fonts) — every heading and all UI text.")
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "nav-link", "Measured 400 — body and nav text."),
    ("semibold", "join-link", "Measured 600 — buttons, links, headings, the wordmark."),
    ("bold", "plan-card", "Measured 700 — the membership plan card's price figure."),
]:
    if have(comp, "default", "fontWeight"):
        weights[key] = {"value": st(comp, "default")["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} default (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared palettes

def scoped(sel_hint, props):
    """Pull a component-scoped declared var value out of the app bin."""
    for e in V.get("app", []):
        if sel_hint in e.get("selector", ""):
            for p in props:
                if p in e.get("properties", {}):
                    return e["properties"][p], f"css-var {p} declared on {e['selector']} in {e['file'].split('/')[-1]} (raw/css-vars.json)"
    return None, None

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, sel, prop, desc in [
    ("teal", ".ui-button--primary", "--_color", "The #088178 signature teal — the primary action fill (Add to cart, Log In)."),
    ("teal-hover", ".ui-button--primary", "--_color-hover", "The declared #003a37 teal hover (link-hover colour too)."),
    ("teal-soft", ".ui-button--primary", "--_color-soft", "The #dff8f6 teal wash (enterprise CTA, earnings chip, site banner)."),
    ("accent", ".ui-button--accent", "--_color", "The #4e42a1 purple — the accent action (Save 25%, membership hero)."),
    ("accent-hover", ".ui-button--accent", "--_color-hover", "The declared #281f6b purple hover."),
    ("accent-soft", ".ui-button--accent", "--_color-soft", "The #edeeff purple wash."),
]:
    v, src = scoped(sel, [prop])
    if v:
        brand[key] = {"value": norm_color(v), "type": "color", "source": src, "description": desc}
for e in V.get("theme", []):
    for p, v in e.get("properties", {}).items():
        if p == "--default-color" and v == "#d53a9d" and "sale" not in brand:
            brand["sale"] = {"value": "#d53a9d", "type": "color",
                "source": f"css-var --default-color declared on {e['selector']} in {e['file'].split('/')[-1]} (raw/css-vars.json)",
                "description": "The #d53a9d sale pink painted on SALE nav items."}

# --------------------------------------------------------- semantic light

sem = SPEC["light"].setdefault("color", {})
for key, leaf, group, desc in [
    ("primary", brand.get("teal"), "action", "The #088178 primary action fill."),
    ("primary-hover", brand.get("teal-hover"), "action", "The #003a37 action hover."),
    ("primary-soft", brand.get("teal-soft"), "action", "The #dff8f6 action wash."),
    ("accent", brand.get("accent"), "action", "The #4e42a1 accent fill."),
    ("accent-hover", brand.get("accent-hover"), "action", "The #281f6b accent hover."),
    ("accent-soft", brand.get("accent-soft"), "action", "The #edeeff accent wash."),
]:
    if leaf:
        sem.setdefault(group, {})[key] = dict(leaf, description=desc)
for key, n, group, desc in [
    ("paper", "--header-bg-color", "background", "The #ffffff page/header fill."),
    ("field", "--default-input-bg-color", "background", "The #fafdff input fill."),
    ("field-active", "--default-input-active-bg-color", "background", "The field fill while editing (legacy: same #fafdff)."),
    ("site-banner", "--site-banner-bg-color", "background", "The declared banner fill — #f9d1e7 on :root, #dff8f6 under data-theme=legacy."),
    ("earnings", "--user-dropdown-earnings-bg-color", "background", "The #dff8f6 earnings chip in the user dropdown."),
    ("ink", "--default-color", "text", "The #303538 default ink."),
    ("muted", "--default-input-placeholder-color", "text", "The #899298 placeholder/muted ink."),
    ("link-hover", "--default-link-hover-color", "text", "The #003a37 link hover (teal-hover)."),
    ("hairline", "--user-dropdown-divider-color", "border", "The #e2e9ee dropdown divider hairline."),
    ("input", "--default-input-border-color", "border", "The input border — #fafdff on :root, #899298 under data-theme=legacy."),
    ("input-active", "--default-input-active-border-color", "border", "The active input border (#303538 :root / #899298 legacy)."),
    ("focus", "--accessible-outline-color", "border", "The #e06868 accessible outline."),
]:
    if n in R:
        sem.setdefault(group, {})[key] = var(n, "color",
            source=f"css-var {n} resolved (raw/css-vars.json)", description=desc)
# measured neutrals the declarations do not cover
try:
    sem.setdefault("text", {})["on-primary"] = {"value": norm_color(st("add-cart", "default")["color"]), "type": "color",
        "source": "computed color of add-cart default (raw/components-computed.json)",
        "description": "White text on the teal/purple fills."}
    sem.setdefault("text", {})["secondary"] = {"value": "#4b5258", "type": "color",
        "source": "literal Sass colour observed across the harvested sheets (raw/css-vars.json sheets)",
        "description": "The #4b5258 secondary ink painted on bylines and meta text."}
    sem.setdefault("text", {})["tertiary"] = {"value": "#6e777d", "type": "color",
        "source": "literal Sass colour observed across the harvested sheets (raw/css-vars.json sheets)",
        "description": "The #6e777d tertiary ink on small print."}
    sem.setdefault("text", {})["danger"] = {"value": "#a02828", "type": "color",
        "source": "literal Sass colour observed across the harvested sheets (raw/css-vars.json sheets)",
        "description": "The #a02828 danger ink."}
    sem.setdefault("text", {})["error"] = {"value": "#e06868", "type": "color",
        "source": "literal Sass colour observed across the harvested sheets (raw/css-vars.json sheets)",
        "description": "The #e06868 error red (same value as --accessible-outline-color)."}
    sem.setdefault("background", {})["chip"] = {"value": norm_color(st("search-chip", "default")["backgroundColor"]), "type": "color",
        "source": "computed backgroundColor of search-chip default (raw/components-computed.json)",
        "description": "The #fee4c3 suggested-search chip fill."}
except KeyError:
    pass
brand["gold"] = {"value": "#fcc875", "type": "color",
    "source": "literal Sass colour observed across the harvested sheets (raw/css-vars.json sheets)",
    "description": "The #fcc875 gold painted on rating stars and the Save 25% corner badge."}

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, desc in [
    ("display", "membership-h1", "The membership hero's measured 72px Averta 600."),
    ("h1", "category-h1", "The 48px page heading (category/search)."),
    ("signin", "signin-h1", "The 36px sign-in heading."),
    ("h2", "product-h1", "The 24px product/section heading."),
    ("m-heading", "m-heading", "The mobile 20px section heading."),
    ("body", "site-header", "The 16px UI/body size."),
    ("input", "nav-search", "The 15px field text."),
    ("button", "join-link", "The 14px button/link size."),
    ("nav", "nav-link", "The 13px nav link size."),
]:
    v = ts(comp, "default", "fontSize") if comp in C else None
    if v:
        ty[key] = {"value": v, "type": "fontSize",
                   "source": f"computed fontSize of {comp} default (raw/components-computed.json)",
                   "description": desc}

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
for key, comp, prop, desc in [
    ("control", "add-cart", "borderTopLeftRadius", "The 8px button radius (declared --btn-border-radius)."),
    ("card", "plan-card", "borderTopLeftRadius", "The 16px card radius (plan card, shop card, user dropdown)."),
    ("chip", "search-chip", "borderTopLeftRadius", "The 20px suggested-search pill."),
    ("round", "filter-btn", "borderTopLeftRadius", "The 32px filter pill."),
    ("follow", "follow-btn", "borderTopLeftRadius", "The 24px shop FOLLOW pill."),
    ("button", "login-btn", "borderTopLeftRadius", "The 3px legacy sign-in button radius."),
]:
    if have(comp, "default", prop):
        v = st(comp, "default")[prop]
        fv = str(int(float(v[:-2]))) + "px" if v.endswith("px") else v
        radii[key] = {"value": fv, "type": "dimension",
                      "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                      "description": desc}
if "--default-input-border-radius" in R:
    radii["field"] = var("--default-input-border-radius", "dimension",
                         source="css-var --default-input-border-radius resolved (raw/css-vars.json); 3px on :root, 12px under data-theme=legacy",
                         description="The declared field radius.")
if "--user-dropdown-border-radius" in R:
    radii["dropdown"] = var("--user-dropdown-border-radius", "dimension",
                            source="css-var --user-dropdown-border-radius resolved (raw/css-vars.json)",
                            description="The declared 4px dropdown/menu radius.")
bw = SPEC["core"].setdefault("border", {})
if "--default-input-border-width" in R:
    bw.setdefault("field", {})["width"] = var("--default-input-border-width", "dimension",
        source="css-var --default-input-border-width resolved (raw/css-vars.json); 1px on :root, 2px under data-theme=legacy",
        description="The declared field border width.")

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
if "--user-dropdown-box-shadow" in R:
    sh["dropdown"] = {"value": R["--user-dropdown-box-shadow"], "type": "other",
                      "source": "css-var --user-dropdown-box-shadow resolved (raw/css-vars.json)",
                      "description": "The declared dropdown/menu elevation: 0 4px 8px 10% ink."}

# ---------------------------------------------------------------- spacing

sp = SPEC["core"].setdefault("spacing", {})
if "--container-content-width" in R:
    sp["container"] = var("--container-content-width", "dimension",
        source="css-var --container-content-width resolved (raw/css-vars.json)",
        description="The 1450px max content width.")
for key, comp, prop, desc in [
    ("header-h", "site-header", "height", "The 73px site header height."),
    ("m-header-h", "m-header", "height", "The 119px mobile header."),
]:
    if have(comp, "default"):
        v = st(comp, "default").get(prop)
        if v and v not in ("0px", "auto"):
            sp[key] = {"value": v, "type": "dimension",
                       "source": f"computed {prop} of {comp} default (raw/components-computed.json)",
                       "description": desc}
if "--btn-height" in R:
    sp["btn-h"] = var("--btn-height", "dimension",
        source="css-var --btn-height resolved (raw/css-vars.json)",
        description="The declared 50px button height.")

# ----------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
if "--default-input-transition" in R:
    mo["field"] = var("--default-input-transition", "other",
                      source="css-var --default-input-transition resolved (raw/css-vars.json)",
                      description="The field's declared 0.4s cubic-bezier(0.25, 1, 0.5, 1) transition.")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "site-header", "default", "height", "dimension", "The 73px site header."),
    ("search-width", "nav-search", "default", "width", "dimension", "The 585px header search field."),
    ("search-height", "nav-search", "default", "height", "dimension", "The 44px header search height."),
    ("save25-height", "save25-button", "default", "height", "dimension", "The 32px purple Save 25% button."),
    ("product-card-width", "product-card", "default", "width", "dimension", "The 337px home product card."),
    ("add-to-cart-height", "add-to-cart-btn", "default", "height", "dimension", "The 44px card Add To Cart button."),
    ("category-card-width", "category-card", "default", "width", "dimension", "The 320px category result card."),
    ("filter-btn-height", "filter-btn", "default", "height", "dimension", "The 44px filter pill."),
    ("buy-box-width", "license-row", "default", "width", "dimension", "The 450px buy-box column."),
    ("license-row-height", "license-row", "default", "height", "dimension", "The 24px license option row."),
    ("add-cart-height", "add-cart", "default", "height", "dimension", "The 45px teal Add to cart."),
    ("buy-now-height", "buy-now", "default", "height", "dimension", "The 40px outlined Buy now."),
    ("enterprise-cta-height", "enterprise-cta", "default", "height", "dimension", "The 52px enterprise CTA."),
    ("follow-btn-width", "follow-btn", "default", "width", "dimension", "The 232px shop FOLLOW pill."),
    ("chip-height", "search-chip", "default", "height", "dimension", "The 44px suggested-search chip."),
    ("accordion-row-height", "accordion-row", "default", "height", "dimension", "The 88px details/summary row."),
    ("specs-width", "specs", "default", "width", "dimension", "The 450px Product Specs block."),
    ("plan-card-width", "plan-card", "default", "width", "dimension", "The 274px membership plan card."),
    ("signin-field-height", "username-field", "default", "height", "dimension", "The 43px sign-in fields."),
    ("login-btn-height", "login-btn", "default", "height", "dimension", "The 51px Log In / SSO buttons."),
    ("footer-height", "footer", "default", "height", "dimension", "The ~488px footer."),
    ("m-header-height", "m-header", "default", "height", "dimension", "The 119px mobile header."),
    ("m-menu-button", "m-menu-button", "default", "width", "dimension", "The 45px hamburger trigger."),
    ("m-drawer-width", "m-menu-open", "default", "width", "dimension", "The 295px mobile menu drawer."),
    ("m-search-height", "m-search", "default", "height", "dimension", "The 46px mobile search."),
    ("nav-link-size", "nav-link", "default", "fontSize", "fontSize", "Nav link 13px."),
    ("sale-color", "save25-button", "default", "backgroundColor", "color", "The #4e42a1 Save 25% fill."),
]:
    if have(cname, state):
        v = st(cname, state).get(prop)
        if v and v not in ("0px", "auto"):
            comp[name] = {"value": norm_color(v) if ty_ == "color" else v, "type": ty_,
                          "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                          "description": desc}
# measured state moves
for cname, label in [("add-cart", "add-cart"), ("buy-now", "buy-now"), ("save25-button", "save25")]:
    try:
        comp.setdefault("button", {})[f"{label}-states"] = {
            "type": "other",
            "value": {s: {"backgroundColor": norm_color(st(cname, s)["backgroundColor"]),
                          "color": norm_color(st(cname, s)["color"])}
                      for s in ("default", "hover", "pressed") if s in C[cname]["states"]},
            "source": f"computed styles of {cname} default/hover/pressed (raw/components-computed.json)",
            "description": f"The {label} button's measured state track."}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
