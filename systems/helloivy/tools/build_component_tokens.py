#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

helloivy.co ships two unrelated design layers on its public surfaces:

  www.helloivy.co — a Framer marketing build. Its real theme layer is five
  hashed design tokens declared on <body> and re-pointed under
  @media (prefers-color-scheme: dark) and by the footer's "Change theme"
  toggle (html[toggle-theme], localStorage.currentToggleState):

    --token-3ea41072-e4a3-4fbd-afee-986fdaa2559f   ink
    --token-8cbad9a1-8614-4d19-b13a-92f1480b19cb   ground
    --token-38cd3004-b4ac-4a01-8a89-0d1effb0d55a   muted
    --token-fb7fb35d-7178-4772-a7d9-bc61bb13cc4d   inverse surface
    --token-c6b5aded-e7a1-4e90-a38d-5c70a03600db   inverse ink

  plus the --framer-link-* roles the rich-text presets declare. Everything
  else on that surface is per-component paint, so the component tokens are
  measured, not declared.

  app.helloivy.co — the product, a Vue SPA. Its semantic layer arrives as an
  inline `style=` theme block on the share page's section.main_section
  (workspace theming, the default palette): hashed --<hash> vars aliased by
  the semantic names --main-color/--link-color/--checkbox (#3F40F2 indigo),
  --app-color, --canvas/--sidebar/--hover/--book/--comment/--project ramp,
  --selection/--text-selection, --scrollBar*, --image-shadow, --book-icon,
  --main-font-family and the shell dimensions --sidebar-width/
  --header-height/--main-header-height. /login carries no section so the
  names stay unresolved there — the login card is measured, not themed.

  /docs is a third surface: a hosted docs platform (General Sans, its own
  chrome) sharing neither layer. Its roles are measured where captured.

Each leaf: {"type", "var"} resolved per theme by build_tokens.py, or a
measured {"type", "value", "source"}. Every leaf carries $extensions.source.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["light"]
RD = V["resolved"]["dark"]
TREE = {"core": {}, "light": {}, "dark": {}, "component": {}}


def emit_at(root, path, leaf):
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = leaf


def cam(name):
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


emitted = set()


def VAR(name, ty, path, desc=None, themes=("light", "dark")):
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    for t in themes:
        emit_at(t, path, leaf)
    emitted.add(name)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


def lit_theme(light_val, dark_val, ty, light_src, dark_src, path, desc=None):
    """A measured role that re-points per theme: each set gets its own leaf."""
    l = {"type": ty, "value": light_val, "source": light_src}
    d = {"type": ty, "value": dark_val, "source": dark_src}
    if desc:
        l["description"] = d["description"] = desc
    emit_at("light", path, l)
    emit_at("dark", path, d)


HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def reading(comp, prop, state="default"):
    """The computed value of prop on comp: the first text node's own reading (textStyle) when
    the capture recorded one, else the element's. Raises when it is missing, so a recapture that
    loses the reading fails the build instead of keeping a typed value."""
    st = C[comp]["states"][state]
    v = (st.get("textStyle") or {}).get(prop) or (st.get("style") or {}).get(prop)
    if not v:
        raise KeyError(f"{comp} {state}: no {prop} reading")
    return v


def measured_lit(comp, prop, ty, path, desc=None, state="default", what=""):
    v = reading(comp, prop, state)
    if ty == "fontWeight":
        v = int(float(v))
    lit(v, ty, f"computed {prop} of {comp} {state} on {C[comp].get('page')} (raw/components-computed.json){what}",
        "core", path, desc=desc)


def app_theme(var):
    v = V["appTheme"].get("@" + var)
    if v is None:
        raise KeyError(f"{var}: not in raw/css-vars.json appTheme")
    return v


# ------------------------------------------------------------ marketing roles
# The five Framer design tokens, re-pointed per theme — resolved in the probe
# carrying the site's own sheets under emulated prefers-color-scheme (the
# same values the footer's "Change theme" toggle paints, verified live).
MARKETING = [
    ("--token-8cbad9a1-8614-4d19-b13a-92f1480b19cb", "color.ground",
     "the page ground — the cream #faf6f0 field; dark re-points it to #16161a"),
    ("--token-3ea41072-e4a3-4fbd-afee-986fdaa2559f", "color.ink",
     "the primary ink — black on the cream ground; dark re-points it to #edecda"),
    ("--token-38cd3004-b4ac-4a01-8a89-0d1effb0d55a", "color.muted",
     "the muted ink — black in light (the site keeps one ink weight); #666662 in dark"),
    ("--token-fb7fb35d-7178-4772-a7d9-bc61bb13cc4d", "color.inverseSurface",
     "the inverse surface — white in light, black in dark; the CTA/footer pills paint it"),
    ("--token-c6b5aded-e7a1-4e90-a38d-5c70a03600db", "color.inverseInk",
     "the inverse ink — black in light, cream #faf6f0 in dark; text on the inverse surface"),
]
for name, path, desc in MARKETING:
    VAR(name, "color", path, desc=desc)

# The rich-text link roles the Framer presets declare. raw/css-vars.json holds
# --framer-link-text-color #0099ff on five preset rules and the ink tokens on two others; which
# preset paints a body link was never measured, so the sources say so.
LINK_NOTE = "declared --framer-link-text-color #0099ff on five rich-text preset rules (raw/css-vars.json); two other presets point it at the ink tokens, and which preset paints a body link was not measured"
lit("#0099ff", "color", LINK_NOTE, "light", "color.link", desc="in-body link blue (#0099ff) on the default rich-text preset")
lit("#0099ff", "color", LINK_NOTE, "dark", "color.link", desc="in-body link blue (#0099ff) on the default rich-text preset")
HOVER_NOTE = "declared --framer-link-hover-text-color #555555 on one rich-text preset rule (raw/css-vars.json); another points it at the ink token"
lit("#555555", "color", HOVER_NOTE, "light", "color.linkHover", desc="link hover grey")
lit("#555555", "color", HOVER_NOTE, "dark", "color.linkHover", desc="link hover grey")

# ------------------------------------------------------- the app's own layer
# section.main_section's inline theme on the public share — the semantic
# names resolve through hashed vars; the values below are the painted
# declarations read live (raw/css-vars.json appTheme). Light-only surface:
# the app paints no dark pass on this route.
APP = "the app product layer — section.main_section's inline workspace theme on the public share (app.helloivy.co/…/share), %s; the same values the app's CSS names alias"
# (token key, painted value, the real --var name it resolves from, desc) —
# the var names are the section's own declarations (raw/css-vars.json
# appTheme), spelled exactly as painted.
APP_THEME = [
    ("primary", "#fff", "--primary", "the primary role — white"),
    ("brand", "#3F40F2", "--main-color", "the brand indigo — --main-color, --link-color and --checkbox all paint it"),
    ("mainColor", "#3F40F2", "--main-color", "--main-color — links, primary actions, the checked accent"),
    ("linkColor", "#3F40F2", "--link-color", "--link-color"),
    ("checkbox", "#3F40F2", "--checkbox", "--checkbox — checked state fill"),
    ("ink", "#37352f", "--app-color", "--app-color — the product ink"),
    ("canvasInk", "#323235", "--canvas-color", "--canvas-color — the document canvas' ink"),
    ("canvas", "#fff", "--canvas", "--canvas — the document/page ground"),
    ("sidebar", "#F5F6F4", "--sidebar", "--sidebar — the sidebar ground"),
    ("hover", "#F3F5F7", "--hover", "--hover — hover row fill"),
    ("book", "#F5F6FA", "--book", "--book — the book/page-list ground"),
    ("hoverBook", "#F1F3F5", "--hover-book", "--hover-book"),
    ("comment", "#fdffe4", "--comment", "--comment — comment pin tint"),
    ("selection", "#F3F5F7", "--selection", "--selection — selected-row fill"),
    ("textSelection", "#e4f2ff", "--text-selection", "--text-selection — text selection tint"),
    ("project", "#ECEDF1", "--project", "--project — project chip fill"),
    ("projectHover", "#F1F1F5", "--projectHover", "--projectHover"),
    ("scrollBar", "#eee", "--scrollBarColor", "--scrollBarColor — the scrollbar track"),
    ("scrollBarThumb", "#CCCCCC", "--scrollBarThumbColor", "--scrollBarThumbColor"),
    ("scrollBarThumbHover", "#9e9d9d", "--scrollBarThumbHover", "--scrollBarThumbHover"),
    ("imageShadow", "#e7e7e7", "--image-shadow", "--image-shadow — image drop line"),
    ("bookIcon", "#323232", "--book-icon", "--book-icon — icon ink in the book list"),
]
for key, val, var, desc in APP_THEME:
    if app_theme(var) != val:
        raise ValueError(f"{var}: the table says {val}, raw appTheme paints {app_theme(var)}")
    lit(app_theme(var), "color", APP % var, "core", f"app.color.{key}", desc=desc)
lit(app_theme("--main-font-family"), "fontFamily", APP % "--main-font-family", "core", "app.font.family", desc="the product face — --main-font-family")
for key, val, var, desc in [
    ("sidebarWidth", "242px", "--sidebar-width", "--sidebar-width — the workspace rail"),
    ("headerHeight", "66px", "--header-height", "--header-height — the document header strip"),
    ("mainHeaderHeight", "65px", "--main-header-height", "--main-header-height — the app header strip"),
]:
    lit(app_theme(var), "dimension", APP % var, "core", f"app.layout.{key}", desc=desc)

# ------------------------------------------------------------- core scales
# Type faces — measured on painted elements (the Framer pages declare
# Unbounded display + Inter body; the hosted docs paint "General Sans"; the
# app paints Inter).
measured_lit("hero-heading", "fontFamily", "fontFamily", "font.family.display",
             desc="Unbounded — the marketing display face; headings only")
measured_lit("nav-link", "fontFamily", "fontFamily", "font.family.body",
             desc="Inter — the marketing UI face; nav, body copy, buttons")
measured_lit("docs-link", "fontFamily", "fontFamily", "font.family.docs",
             desc="General Sans — the docs surface's face (a different platform than the marketing site)")

for key, comp in [("regular", "hero-copy"), ("medium", "faq-question"), ("semibold", "nav-link")]:
    measured_lit(comp, "fontWeight", "fontWeight", f"font.weight.{key}")
lit(700, "fontWeight", HAND + " (no captured element paints 700; the plan-card title is 500)", "core", "font.weight.bold")

# The measured type ramp (px, at the painted size of the text node).
lit("12px", "dimension", HAND + " (the footer and docs wrappers compute 12px, but no text node paints it)", "core", "font.size.xs")
for key, comp in [
    ("sm", "login-forgot"), ("smMd", "docs-link"), ("md", "login-input-email"), ("base", "nav-link"),
    ("lg", "login-continue"), ("xl", "plan-card"), ("title2", "login-card"), ("lead", "hero-copy"),
    ("displaySm", "m-hero-heading"), ("displayMd", "feature-card"), ("displayLg", "section-heading"),
    ("displayXl", "hero-heading"),
]:
    measured_lit(comp, "fontSize", "dimension", f"font.size.{key}")

lit(reading("login-input-email", "borderTopLeftRadius"), "dimension", "computed borderTopLeftRadius of login-input-email default on app/login (raw/components-computed.json); login-continue and login-google match", "core", "radius.field", desc="the product's control corner — inputs and buttons")
lit(reading("nav-cta", "borderTopLeftRadius"), "dimension", "computed borderTopLeftRadius of nav-cta default on / (raw/components-computed.json); hero-cta matches — a pill", "core", "radius.pill", desc="the marketing pill — every marketing button")

# ------------------------------------------------- measured component tokens
if True:  # components-computed.json is required (read above)

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

    geom("nav-bar", "default", "h", "navBar.height", "the marketing top strip")
    geom("nav-cta", "default", "h", "button.cta.height", "marketing pill button")
    geom("nav-cta", "default", "w", "button.cta.width", "marketing pill button")
    geom("nav-menu-box", "default", "h", "menuBox.height", "the nav menu box")
    geom("login-card", "default", "w", "loginCard.width", "the app login card")
    geom("login-input-email", "default", "h", "input.height", "app text field")
    geom("login-continue", "default", "h", "button.appHeight", "the app's primary button")
    geom("share-header", "default", "h", "shareHeader.height", "the share page top strip")
    geom("post-card", "default", "w", "postCard.width", "a blog index card")
    geom("plan-card", "default", "w", "planCard.width", "a pricing plan column")
    geom("m-nav-bar", "default", "h", "mobileNav.height", "the phone top strip")

    def pad(comp, state, path, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        s = st.get("style") or {}
        vals = [s.get(f"padding{d}") for d in ("Top", "Right", "Bottom", "Left")]
        if not all(vals):
            return
        lit(" ".join(vals), "other",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    pad("nav-cta", "default", "button.cta.padding", "marketing pill padding")
    pad("login-input-email", "default", "input.padding", "app field padding")
    pad("login-continue", "default", "button.app.padding", "the app's primary button padding")

    # Measured marketing button paint — the pill is the ink in light, the
    # inverse ink in dark; its text is the inverse surface/ink.
    st = C.get("nav-cta", {}).get("states", {})
    lt, dk = st.get("default", {}).get("style", {}), st.get("dark", {}).get("style", {})
    if lt.get("backgroundColor"):
        lit_theme("{color.ink}", "{color.inverseInk}", "color",
                  f"measured nav-cta default backgroundColor {lt['backgroundColor']} on / (the ink role)",
                  f"measured nav-cta dark backgroundColor {dk.get('backgroundColor')} on / (the inverse ink role)",
                  "component.button.cta.bg", desc="the marketing pill fill — paints the ink role in light, the inverse ink in dark")
        # The label keeps painting the inverse *surface* value in both
        # themes: white on the black pill in light, the measured
        # rgb(0, 0, 0) black on the cream pill in dark (the captured dark
        # textStyle.color — not color.ink, which would fade on #faf6f0).
        lit_theme("{color.inverseSurface}", "{color.inverseSurface}", "color",
                  "measured nav-cta default text color rgb(255, 255, 255) on / (the inverse surface role)",
                  f"measured nav-cta dark text color {reading('nav-cta', 'color', 'dark')} on / (the inverse surface role — the label stays black)",
                  "component.button.cta.fg", desc="the marketing pill label colour")
    # No border token: the captured pill paints borderTopWidth 0px /
    # borderTopStyle none — its computed borderTopColor (the unvisited-link
    # currentColor) is not a real border, so nothing is published as one.

    # The app's measured button paint (login-continue: near-black pill, hover black).
    lc = C.get("login-continue", {}).get("states", {})
    if lc.get("default", {}).get("style", {}).get("backgroundColor"):
        lit(lc["default"]["style"]["backgroundColor"], "color",
            "measured login-continue default backgroundColor on app/login", "component", "button.app.bg",
            desc="the app's primary button fill")
    if lc.get("hover", {}).get("style", {}).get("backgroundColor"):
        lit(lc["hover"]["style"]["backgroundColor"], "color",
            "measured login-continue hover backgroundColor on app/login", "component", "button.app.bgHover")
    ie = C.get("login-input-email", {}).get("states", {})
    if ie.get("default", {}).get("style", {}).get("backgroundColor"):
        lit(ie["default"]["style"]["backgroundColor"], "color",
            "measured login-input default backgroundColor on app/login", "component", "input.bg",
            desc="the app's field fill")
    if ie.get("default", {}).get("style", {}).get("borderTopColor"):
        lit(ie["default"]["style"]["borderTopColor"], "color",
            "measured login-input default borderTopColor on app/login", "component", "input.border")
    if ie.get("focused", {}).get("style", {}).get("borderTopColor"):
        lit(ie["focused"]["style"]["borderTopColor"], "color",
            "measured login-input focused borderTopColor on app/login (the field clicked into)", "component", "input.borderFocused")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography.
    def typ(comp, path, name, state="default"):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        # The capture's textStyle block is the first real text node's own
        # type; the container's style carries the wrapper's face, which is
        # smaller/inherited whenever they differ (a card's heading vs its
        # body). Prefer the measured text.
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
                "$extensions": {"source": f"measured {comp} {state} on {C[comp].get('page')}"}}
        emit_at("core", path, leaf)

    typ("hero-heading", "typography.display", "the marketing hero — Unbounded 82/90")
    typ("section-heading", "typography.h2", "a mid-page section heading — Unbounded 62/68")
    typ("m-hero-heading", "typography.displayMobile", "the hero at 390px — Unbounded 32/38")
    typ("hero-copy", "typography.lead", "the hero supporting paragraph — Inter 27/41")
    typ("nav-link", "typography.navLink", "a marketing nav link — Inter 16/19 600")
    typ("faq-question", "typography.faqQuestion", "a pricing FAQ row — Inter-Medium 16/26")
    typ("feature-card", "typography.cardTitle", "a feature tile title — Unbounded 34/41", state="default")
    typ("theme-control", "typography.small", "the footer control label — Inter 14/21")
    typ("login-card", "typography.appTitle", "the app login heading — Inter 23/28 600")
    typ("login-continue", "typography.appButton", "the app's primary button label — Inter 17/21 500")
    typ("login-input-email", "typography.field", "an app text field — Inter 15/23")
    typ("docs-link", "typography.docsNav", "a docs nav link — General Sans 14/20 600")
    typ("share-doc", "typography.docBody", "the share document body — Inter 16/26")

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
    print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
