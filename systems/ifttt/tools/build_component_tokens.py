#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

IFTTT's signed-out surfaces (ifttt.ai + ifttt.com) are Sass-compiled Rails
markup: the token layer is nearly absent — a handful of custom properties
(--card-color, --hero-unit, --primary-text on the home/plans heroes; the
explore hero's --cycle-lag/--cycle-count/--cycle-keyframes cycler math) —
and everything else is literal hex/rgb() on class names. vars.mjs harvests
every literal into css-vars.json's `palette`; the few real variables are
emitted under light.misc resolved in the single theme.

The measured component readings (raw/components-computed.json, written by
tools/capture/public/measure.mjs) supply everything else:

  light.color.*        semantic roles read off the painted page: the white
                       ground, the near-black ink, the black action pill,
                       the outlined secondary, the hairline borders, the
                       section tints — each leaf carries the measurement
                       it was read from
  core.palette.*       literal colours the sheets declare, not already a
                       semantic role (named after the class fragment that
                       uses them, or p<hex>)
  core.typography.*    measured type composites (Museo Sans Rounded scale)
  core.font.family.*   the proprietary faces by name (never shipped)
  core.component.*     measured geometry: header height, button and input
                       heights, card and control radii
  light.component.*    component roles painted by the page: the dark
                       surfaces (explore/service/connect heroes, the
                       recommended plan card header), the on-dark ink and
                       actions, the modal, the billing switch, the tabs

IFTTT paints one theme — there is no theme control — so there is a `light`
set alone. Dark grounds are painted sections and land under
light.component.dark as the measured values they are.

Each leaf: {"type": ..., "var": "--name"} resolved by build_tokens.py, or a
measured {"type", "value", "source"}. Every leaf carries $extensions.source.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["light"]
TREE = {"core": {}, "light": {}, "component": {}}


def emit_at(root, path, leaf):
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = leaf


def cam(name):
    """--foo-bar-baz -> fooBarBaz (a token key, not a CSS name)."""
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


KIND_TY = {"color": "color", "dimension": "dimension", "duration": "duration",
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily"}

emitted = set()


def VAR(name, ty, path, desc=None):
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    emit_at("light", path, leaf)
    emitted.add(name)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


# ------------------------------------------------------- the real vars
# The handful of custom properties IFTTT actually declares (the home and
# plans heroes' --card-color/--hero-unit/--primary-text, the explore
# cycler's --cycle-*) land under light.misc resolved in the one theme.
declared = set()
for rule in V.get("app", []):
    declared.update(rule.get("properties", {}))
for n in sorted(declared):
    if n in emitted or n not in R:
        continue
    kind = R[n].get("kind", "other")
    VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}")


def norm_lit(c):
    """A palette literal -> '#rrggbb' or 'rgba(r, g, b, a)'."""
    c = re.sub(r"\s*,\s*", ", ", c.strip().lower())
    m = re.fullmatch(r"#([0-9a-f]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(x * 2 for x in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)\s*(?:[,/]\s*([\d.]+%?))?\)", c)
    if m:
        r, g, b, a = m.groups()
        r, g, b = int(float(r)), int(float(g)), int(float(b))
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    return None


# ----------------------------------------------------- semantic roles
# Measured off the painted components: the leaf's "source" is the element
# and state it was read from, never the stylesheet guess.
C_PATH = RAW / "components-computed.json"
# Required: without it every measured token would drop silently.
C = json.loads(C_PATH.read_text())["components"]


def style_of(comp, state, prop):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    return (st.get("style") or {}).get(prop)


def semantic(comp, prop, path, label, state="default", root="light"):
    """A painted role read off a real element."""
    v = style_of(comp, state, prop)
    if v is None or v == "rgba(0, 0, 0, 0)":
        return
    lit(norm_lit(v) or v, "color",
        f"measured {comp} {state} on {C[comp].get('page')} ({label})",
        root, path, desc=label)


# page ground + ink
semantic("prose-p", "color", "color.text.body", "body ink")
semantic("plan-feature", "color", "color.text.muted", "secondary ink (the plan feature lines)")
semantic("hero-headline", "color", "color.text.display", "headline ink")
semantic("nav-link", "color", "component.dark.navInk", "nav-link ink on the dark heroes")
semantic("applet-meta", "color", "color.text.onColorSubtle", "secondary ink on brand-coloured heroes")
semantic("footer-link", "color", "color.text.footer", "footer link ink")

def page_bg(key, url_key=None):
    pass  # body bg is read from layout.json below


# body ground from the layout readings
L_PATH = RAW / "layout.json"
if L_PATH.exists():
    L = json.loads(L_PATH.read_text())
    home = L.get("home@1440") or {}
    bg = (home.get("body") or {}).get("bg") or home.get("bodyBg")
    if bg:
        lit(norm_lit(bg) or bg, "color",
            "document body computed background on ifttt.ai/ (raw/layout.json home@1440)",
            "light", "color.bg.page", desc="the page ground")
    explore = L.get("explore@1440") or {}
    ebg = (explore.get("body") or {}).get("bg") or explore.get("bodyBg")
    if ebg and norm_lit(ebg):
        lit(norm_lit(ebg), "color",
            "document body computed background on /explore (raw/layout.json explore@1440) — the dark painted explore ground",
            "light", "component.dark.ground", desc="the dark painted ground behind /explore")

# action fills
semantic("hero-submit", "backgroundColor", "color.action.fill", "primary action fill")
semantic("hero-submit", "color", "color.action.onFill", "ink on the primary fill")
semantic("hero-submit", "backgroundColor", "color.action.hoverFill", "primary fill on hover", state="hover")
# color.action.navFill was read from plan-cta-filled, whose saved element is
# the header signup, not the plan card. nav-signup already records the
# dark-hero header pill. The light-header fill is not re-sourced from the
# mis-keyed reading.
semantic("plan-cta", "borderTopColor", "color.action.outline", "outlined pill border")
semantic("plan-cta", "color", "color.action.outlineInk", "outlined pill ink")
semantic("nav-login", "borderTopColor", "component.dark.outline", "outlined pill border on the dark heroes")
semantic("nav-login", "color", "component.dark.outlineInk", "outlined pill ink on the dark heroes")
semantic("nav-signup", "backgroundColor", "component.dark.navFill", "header 'Get started' fill on the dark heroes")
semantic("nav-signup", "color", "component.dark.navFillInk", "header 'Get started' ink on the dark heroes")
semantic("secondary-cta", "borderTopColor", "color.action.secondaryOutline", "secondary CTA border")
semantic("secondary-cta", "color", "color.action.secondaryInk", "secondary CTA ink")
semantic("plan-cta", "borderTopColor", "component.planCard.ctaBorder", "plan card CTA border")
# plan-cta-filled's saved reading is the header signup, not the Pro card CTA.
# The token is omitted until a scoped recapture measures the card button.

# links + badges
semantic("prose-link", "color", "color.text.link", "link ink in prose")
# save-badge's saved reading is the whole billing row (transparent, 193x56),
# and its paint layers are the switch, not a measured badge style. No badge
# fill or ink is invented from that row.

# dark-painted surfaces and their on-colour ink
semantic("explore-hero", "backgroundColor", "component.dark.heroBg", "explore dark hero ground")
semantic("explore-service-chip", "color", "component.dark.chipInk", "service chip ink on the dark hero")
semantic("explore-service-chip", "backgroundColor", "component.dark.chipBg", "service chip fill on the dark hero")
semantic("service-hero", "backgroundColor", "component.dark.serviceHeroBg", "service/applet/connect hero ground")
semantic("get-started-today", "backgroundColor", "component.dark.actionFill", "action fill on the dark heroes")
semantic("get-started-today", "color", "component.dark.actionInk", "action ink on the dark heroes")
semantic("author-link", "color", "component.dark.linkInk", "link ink on the applet hero")

# fields
semantic("nav-search", "backgroundColor", "component.input.searchBg", "header search field fill")
semantic("nav-search", "borderTopColor", "component.input.searchBorder", "header search field border")
semantic("hero-prompt", "backgroundColor", "component.promptCard.fieldBg", "prompt field fill")
semantic("share-url-field", "backgroundColor", "component.input.shareFieldBg", "share URL field fill")

# cards
semantic("applet-card", "backgroundColor", "component.card.appletBg", "applet card ground")
semantic("service-card", "backgroundColor", "component.card.serviceBg", "service card ground")
semantic("plan-card-recommended", "backgroundColor", "component.planCard.recommendedBg", "recommended plan card ground")

# the billing switch
semantic("billing-toggle", "backgroundColor", "component.switch.trackOn", "billing switch track (on)")
semantic("billing-toggle", "backgroundColor", "component.switch.trackOff", "billing switch track (off)", state="toggled")
semantic("featured-tab", "backgroundColor", "component.tab.fill", "featured tab fill")
# featured-tab-active's saved default is the Smart home tab left selected.
# The selected state of featured-tab is that same reading, stored under the
# state it belongs to.
semantic("featured-tab", "backgroundColor", "component.tab.activeFill", "featured tab fill, active", state="selected")
semantic("featured-tab", "color", "component.tab.activeInk", "featured tab ink, active", state="selected")

# ----------------------------------------------------- literal palette
# IFTTT's Sass-compiled classes hard-code their colours; literals already
# captured as a semantic role or a resolved var are skipped, the rest
# become core.palette primitives named after the class fragment that
# uses them.
covered = set()
for rec in R.values():
    v = rec.get("value") or rec.get("raw")
    if rec.get("kind") == "color" and isinstance(v, str):
        covered.add(v.lower())
for tree in (TREE["light"],):
    def walk(o):
        if isinstance(o, dict):
            if "value" in o and isinstance(o["value"], str):
                covered.add(o["value"].lower())
            else:
                for x in o.values():
                    walk(x)
    walk(tree)

PAL_NAMES = [  # class fragment -> token name
    ("white", "white"), ("black", "black"), ("grey", "grey"),
    ("save", "saveGreen"), ("green", "green"), ("red", "red"),
    ("blue", "blue"), ("pink", "pink"), ("orange", "orange"), ("yellow", "yellow"),
    ("placeholder", "grey"),
]
def pal_name(literal, uses):
    # Match whole class-name fragments only — "red" must not inherit "reddit"
    # or "required", "grey" not "greyish" (IFTTT's utility classes are noisy).
    frags = set()
    for u in uses:
        for tok in re.split(r"[^a-z]+", u["selector"].lower()):
            frags.add(tok)
    for frag, name in PAL_NAMES:
        if frag in frags:
            return name
    hexv = (norm_lit(literal) or "").lstrip("#")
    return "p" + re.sub(r"[^0-9a-f]", "", hexv)[:6]

palette_items = sorted(V.get("palette", {}).items(), key=lambda kv: -kv[1]["count"])
seen_names = set()
for literal, d in palette_items:
    v = norm_lit(literal)
    if v is None:
        continue
    if v.lower() in covered or literal == "#0000":
        continue
    if d["count"] < 3:
        continue
    name = pal_name(literal, d["uses"])
    while name in seen_names:
        name += "2"
    seen_names.add(name)
    uses = "; ".join(u["selector"][:110] for u in d["uses"][:3])
    lit(v, "color",
        f"literal in the site's stylesheets (raw/css-vars.json palette, {d['count']} declarations; e.g. {uses})",
        "core", f"palette.{name}")

# ------------------------------------------------- measured geometry
def geom(comp, state, field, path, label):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    rect = st.get("rect") or {}
    style = st.get("style") or {}
    v = rect.get(field) if field in rect else style.get(field)
    if v is None:
        return
    try:
        px = float(re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:px)?", str(v)).group(1))
    except Exception:
        return
    lit(f"{px:g}px", "dimension",
        f"measured {comp} {state} on {C[comp].get('page')} ({label})",
        "component", path)


geom("site-header", "default", "h", "header.height", "the unified header")
geom("nav-signup", "default", "h", "button.small.height", "header 'Get started' pill")
geom("nav-login", "default", "h", "button.small.height", "header 'Log in' pill")
geom("hero-submit", "default", "h", "button.hero.height", "'Start building'")
geom("secondary-cta", "default", "h", "button.secondary.height", "'Join today' secondary")
geom("plan-cta", "default", "h", "button.planCta.height", "plan card CTA")
geom("connect-toggle", "default", "h", "connectToggle.height", "the Applet Connect toggle")
geom("connect-toggle", "default", "w", "connectToggle.width", "the Applet Connect toggle")
geom("nav-search", "default", "h", "input.search.height", "header search field")
geom("gallery-search", "default", "h", "input.gallerySearch.height", "'Search automations' field")
geom("hero-prompt", "default", "h", "promptField.height", "hero prompt textarea")
geom("share-url-field", "default", "h", "input.shareField.height", "share URL field")
geom("featured-tab", "default", "h", "tab.height", "featured category tab")
geom("billing-toggle", "default", "h", "switch.height", "billing switch track")
geom("billing-toggle", "default", "w", "switch.width", "billing switch track")
geom("explore-service-chip", "default", "h", "serviceChip.height", "explore hero service chip")
geom("service-icon", "default", "w", "serviceIcon.size", "service icon tile")
geom("m-header", "default", "h", "mobileHeader.height", "mobile header")
geom("m-menu-button", "default", "h", "menuButton.height", "mobile hamburger")
geom("back-button", "default", "h", "backButton.height", "detail 'Back' pill")


def style_tok(comp, state, prop, path, ty, label):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    v = (st.get("style") or {}).get(prop)
    if v is None:
        return
    lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})",
        "component", path)


def radius_tok(comp, state, path, label):
    """The capture records the four corner properties, never the shorthand;
    emit the shared radius when all four agree. A fully rounded corner
    reads as the clamp — emitted at the pill bound."""
    st = C.get(comp, {}).get("states", {}).get(state, {})
    s = st.get("style") or {}
    corners = [s.get(f"border{p}Radius") for p in
               ("TopLeft", "TopRight", "BottomRight", "BottomLeft")]
    if not all(corners) or len(set(corners)) != 1:
        return
    v = corners[0]
    desc = None
    try:
        if float(re.fullmatch(r"(-?\d+(?:\.\d+)?(?:e\+?\d+)?)px", v).group(1)) >= 9999:
            v, desc = "9999px", "all four corners measure the full-radius clamp — a pill"
    except Exception:
        pass
    lit(v, "dimension",
        f"measured {comp} {state} on {C[comp].get('page')} ({label})",
        "component", path, desc=desc)


radius_tok("nav-signup", "default", "button.small.radius", "header pill corner")
radius_tok("nav-login", "default", "button.small.outlinedRadius", "outlined pill corner")
radius_tok("hero-submit", "default", "button.hero.radius", "'Start building' corner")
radius_tok("secondary-cta", "default", "button.secondary.radius", "secondary CTA corner")
radius_tok("plan-cta", "default", "button.planCta.radius", "plan CTA corner")
radius_tok("connect-toggle", "default", "connectToggle.radius", "Connect toggle corner")
radius_tok("nav-search", "default", "input.search.radius", "search field corner")
radius_tok("hero-prompt", "default", "promptField.radius", "prompt textarea corner")
# explore-prompt-card's saved reading is the dark hero (section, 1440x579,
# radius 0). The card's corner is not in that reading, so it is not emitted.
radius_tok("share-url-field", "default", "input.shareField.radius", "share URL field corner")
radius_tok("featured-tab", "default", "tab.radius", "featured tab corner")
radius_tok("billing-toggle", "default", "switch.radius", "billing switch corner")
radius_tok("applet-card", "default", "card.applet.radius", "applet card corner")
radius_tok("service-card", "default", "card.service.radius", "service card corner")
radius_tok("service-chip", "default", "serviceIcon.radius", "service icon tile corner")
radius_tok("explore-service-chip", "default", "serviceChip.radius", "explore chip corner")
radius_tok("plan-card", "default", "card.plan.radius", "plan card corner")
radius_tok("plan-card-recommended", "default", "card.planRecommended.radius", "recommended plan card corner")
radius_tok("example-prompt-card", "default", "card.example.radius", "example prompt card corner")
radius_tok("story-card", "default", "card.story.radius", "story card corner")
radius_tok("share-button", "default", "button.share.radius", "Share pill corner")
radius_tok("back-button", "default", "button.back.radius", "Back pill corner")

# shadows, where a component paints one
for comp, st, path, label in [
    ("applet-card", "default", "card.applet.shadow", "applet card shadow"),
    ("service-card", "default", "card.service.shadow", "service card shadow"),
    ("plan-card-recommended", "default", "card.planRecommended.shadow", "recommended card shadow"),
    # explore-prompt-card's saved element is the hero, whose shadow is none.
    # The card's shadow is not in the reading.
    ("site-header", "default", "header.shadow", "header shadow"),
]:
    v = style_of(comp, st, "boxShadow")
    if v and v != "none":
        style_tok(comp, st, "boxShadow", path, "other", label)

# ------------------------------------------------- measured type scale
# The recording holds two type reads: `style` is the component element's
# own computed style, `textStyle` the first real text node inside it.
def typ(comp, path, name, state="default"):
    st = C.get(comp, {}).get("states", {}).get(state, {})
    s = st.get("textStyle") or st.get("style") or {}
    if not s.get("fontSize"):
        return
    style = {
        "fontFamily": s["fontFamily"],
        "fontSize": s["fontSize"],
        "fontWeight": int(float(s["fontWeight"])),
        "lineHeight": s["lineHeight"],
    }
    if s.get("letterSpacing") and s["letterSpacing"] != "normal":
        style["letterSpacing"] = s["letterSpacing"]
    leaf = {"$value": style, "$type": "typography",
            "$description": name,
            "$extensions": {"source": f"measured {comp} on {C[comp].get('page')} ({state} state)"}}
    emit_at("core", path, leaf)


typ("hero-headline", "typography.hero", "the home hero display — Museo Sans Rounded 900")
typ("explore-hero", "typography.exploreHero", "the explore 'Automate X with Y' display")
typ("marketing-h1", "typography.pageTitle", "a marketing page headline")
typ("section-heading", "typography.sectionTitle", "a home section heading")
typ("prose-p", "typography.body", "body prose — Museo Sans Rounded")
typ("prose-link", "typography.bodyLink", "a body-text link")
typ("nav-link", "typography.navLink", "a nav link")
typ("nav-signup", "typography.button", "the header button label")
typ("hero-submit", "typography.buttonHero", "the hero action label")
typ("plan-price", "typography.price", "the plan price figure")
typ("applet-meta", "typography.appletMeta", "the applet byline")
typ("featured-tab", "typography.tab", "a featured category tab")
typ("footer-link", "typography.footerLink", "a footer link")
typ("explore-service-chip", "typography.serviceChip", "a service chip label")

# --------------------------------------------------------- font faces
# Museo Sans Rounded is proprietary and never shipped: name + role from
# the @font-face harvest and the measured stacks.
_st = C["site-header"]["states"]["default"]
_brand = (_st.get("textStyle") or {}).get("fontFamily") or _st["style"]["fontFamily"]
if "Museo Sans Rounded" not in _brand:
    raise ValueError(f"site-header: computed fontFamily {_brand!r} does not name Museo Sans Rounded")
lit(_brand, "fontFamily",
    "computed fontFamily of site-header default (raw/components-computed.json), verbatim; 'Museo Sans Rounded' weights 300/500/700/900 + italics are declared by @font-face in the site's sheets, served from web-assets.ifttt.com — the name is evidence, the font file is not shipped",
    "core", "font.family.brand", desc="the brand face — every weight the site ships")
lit('ui-sans-serif, system-ui, sans-serif', "fontFamily",
    "Reconstruction — entered by hand at capture time: a hand-written fallback stack for consumers without the licensed face; nothing on the site declares it",
    "core", "font.family.fallback", desc="fallback for consumers without the licensed face")

(RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
