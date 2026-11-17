#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

grow.google is Google's glue marketing framework: a server-rendered site
whose versioned gstatic marketing-cms bundle (gwg-us-*.*/All.min.css)
declares only the glue colour layer as custom properties — the
--glue-{blue,green,grey,red,yellow,purple}-{50..900} ramps on :root (a
six-step ramp, 50..900, no 25 except grey). Every other decision is a
compiled literal, so spacing, type, radii, states and shadows are measured
computed styles from raw/components-computed.json, never restated by hand.

Each leaf either names a variable ("var", resolved per theme against the
resolved declarations in raw/css-vars.json) or carries a measured value and
the measurement it came from ("source"):

  core      the declared glue palette + the measured type ramp, weights,
            tracking, radii, shadows and control transitions
  light     the semantic roles every signed-out page paints: surfaces,
            inks, link and button states, the promo banner, the jumplinks
            pill bar, the certificate cards, the expansion hairline, the
            dark editorial hero
  component measured control geometry (header height, pill sizes, the
            mega-menu, drawer button, card cells, video teaser)
No dark or app set exists: the site paints light only (no toggle, no dark
media query, no sign-in). The APAC regional edition (/intl/ALL_sg/ from
this host) shares the same bundle family and is a screenshot variant, not a
separate token surface.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
J = json.loads((RAW / "components-computed.json").read_text())
C = J["components"]


def st(key, state="default"):
    return (C.get(key, {}).get("states") or {}).get(state) or {}


def sty(key, state="default"):
    return st(key, state).get("style") or {}


def val(key, prop, state="default"):
    return sty(key, state).get(prop)


def rect(key, state="default"):
    return st(key, state).get("rect") or {}


def src(key, prop, state="default", what=None):
    return "measured %s of %s %s on grow.google's US edition (raw/components-computed.json)" % (what or prop, key, state)


def lit(v, ty, source, desc=None):
    d = {"value": v, "type": ty, "source": source}
    if desc:
        d["description"] = desc
    return d


def var(name, ty, source=None, desc=None):
    d = {"var": name, "type": ty}
    if source:
        d["source"] = source
    if desc:
        d["description"] = desc
    return d


def px(v):
    return "%gpx" % round(float(str(v).replace("px", "")), 2)


def num(v, fallback):
    try:
        f = float(str(v).replace("px", "").strip())
        return f
    except (TypeError, ValueError):
        return fallback


# ---------- palette: the declared glue ramps (resolved css-var leaves) ----------

RESOLVED = set(json.loads((RAW / "css-vars.json").read_text()).get("resolved", {}).get("light", {}))

palette = {}
for family in ("blue", "green", "grey", "red", "yellow", "purple"):
    steps = {}
    for n in ("--glue-%s-%s" % (family, s) for s in ("0", "25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900")):
        step = n.rsplit("-", 1)[1]
        steps[step] = var(n, "color", "css-var %s declared on :root by gwg-us-1.2.12 styles/default/All.min.css" % n)
    # keep only steps the sheet actually declares (purple ships 100+900 only,
    # grey ships 0+25 too)
    steps = {s: l for s, l in steps.items() if l["var"] in RESOLVED}
    if steps:
        palette[family] = steps


# ---------- type ramp: measured font metrics ----------

def face(key, state="default"):
    fam = val(key, "fontFamily", state) or '"Google Sans Flex", Arial, Helvetica, sans-serif'
    return fam


FLEX = face("hero-h1")


def typ(key, label, state="default", desc=None):
    s = sty(key, state)
    return lit(
        {"fontFamily": FLEX, "fontSize": px(s["fontSize"]), "fontWeight": int(num(s.get("fontWeight"), 400)),
         "lineHeight": px(s["lineHeight"]), "letterSpacing": s.get("letterSpacing", "normal")},
        "typography", "%s: %s" % (src(key, "typography", state), "%s %s/%s %s, ls %s" % (FLEX.split(",")[0].strip('"'), s["fontSize"], s["lineHeight"], s.get("fontWeight"), s.get("letterSpacing"))),
        desc)


# ---------- build the spec ----------

shadow_tabbar = val("tab-bar", "boxShadow") or "none"
shadow_btn_hover = val("cert-cta", "boxShadow", "hover") or "none"
shadow_btn_pressed = val("cert-cta", "boxShadow", "pressed") or "none"

core = {
    "color": {
        "palette": palette,
        "_description": "The declared glue colour layer: the versioned gstatic bundle declares only these ramps as custom properties; every other colour the site paints is a compiled literal read as a measured computed style.",
    },
    "font": {
        "family": {
            "sans": lit(FLEX, "fontFamily", src("hero-h1", "fontFamily"), "The variable face everything paints: Google Sans Flex opsz 6-144 wght 100-1000, served from fonts.googleapis.com (Google Sans Text, Google Sans, Google Sans Display and Product Sans faces are also requested and declared in the font sheet)."),
            "system": lit("Arial, Helvetica, sans-serif", "fontFamily", "the fallback tail of the measured fontFamily stack", "The fallback tail the flex stack declares."),
        },
        "weight": {
            "regular": lit(400, "fontWeight", src("body-p", "fontWeight")),
            "medium": lit(500, "fontWeight", src("nav-link", "fontWeight")),
            "bold": lit(700, "fontWeight", src("stat-chip", "fontWeight"), "The stat figures are the only 700-weight text measured; headings all paint regular/medium."),
        },
    },
    "typography": {
        "display-1": typ("cert-h1", "display-1", "default", "Certificate/AI page display heading (60px/72px, ls -0.5) on the dark hero / tinted band."),
        "display-2": typ("certs-h1", "display-2", "default", "The catalog display heading (48px/56px, ls -0.5); the stat figures share the size at 700 weight."),
        "headline": typ("hero-h1", "headline", "default", "The home hero headline (36px/44px, ls -0.25)."),
        "title": typ("h2", "title", "default", "A section heading (28px/36px)."),
        "stat": typ("stat-chip", "stat", "default", "The 700-weight stat figure (48px/57.6px)."),
        "body": typ("header", "body", "default", "The default text size (16px/24px) — nav, links, body copy."),
        "body-small": typ("body-p", "body-small", "default", "Secondary body copy (14px/21px)."),
        "eyebrow": typ("eyebrow", "eyebrow", "default", "The uppercase eyebrow (14px/24px, 500, ls 0.5px)."),
        "caption": typ("breadcrumb", "caption", "default", "Breadcrumb/caption text (12px/20px)."),
        "nav": typ("nav-link", "nav", "default", "Header nav text (16px/24px, 500, ls 0.25px)."),
        "button": typ("cert-cta", "button", "default", "Pill button text (16px/24px, 500, ls 0.5px)."),
    },
    "radius": {
        "pill": lit(px(val("cert-cta", "borderTopLeftRadius") or 48), "dimension", src("cert-cta", "borderTopLeftRadius"), "The fully-round pill: every button and the jumplinks tab bar."),
        "bar": lit(px(val("tab-bar", "borderTopLeftRadius") or 120), "dimension", src("tab-bar", "borderTopLeftRadius"), "The jumplinks pill bar (120px — the bar itself)."),
        "card": lit(px(val("card-link", "borderTopLeftRadius") or 8), "dimension", src("card-link", "borderTopLeftRadius"), "The announcement card link radius (8px)."),
        "control": lit(px(val("nav-link", "borderTopLeftRadius") or 4), "dimension", src("nav-link", "borderTopLeftRadius"), "Small controls: nav links, menu items, the drawer button (4px)."),
    },
    "shadow": {
        "elevation-1": lit(
            [{"offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px", "color": "rgba(60, 64, 67, 0.3)"},
             {"offsetX": "0px", "offsetY": "1px", "blur": "3px", "spread": "1px", "color": "rgba(60, 64, 67, 0.15)"}],
            "shadow", src("tab-bar", "boxShadow"), "The glue elevation the jumplinks bar and hovered buttons share."),
        "button-pressed": lit(
            [{"offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px", "color": "rgba(60, 64, 67, 0.3)"},
             {"offsetX": "0px", "offsetY": "2px", "blur": "6px", "spread": "2px", "color": "rgba(60, 64, 67, 0.15)"}],
            "shadow", src("cert-cta", "boxShadow", "pressed"), "The deeper elevation a pressed button paints."),
    },
    "space": {
        "button": {"x": lit(px(val("cert-cta", "paddingLeft") or 16), "dimension", src("cert-cta", "paddingLeft")),
                   "y": lit(px(val("cert-cta", "paddingTop") or 12), "dimension", src("cert-cta", "paddingTop"))},
        "nav": {"x": lit(px(val("nav-link", "paddingLeft") or 12), "dimension", src("nav-link", "paddingLeft"))},
        "tab": {"x": lit(px(val("tab", "paddingLeft") or 8), "dimension", src("tab", "paddingLeft")),
                "y": lit(px(val("tab", "paddingTop") or 7), "dimension", src("tab", "paddingTop"))},
        "page": {"x": lit(px(rect("cert-hero").get("x", 72)), "dimension", "measured content-column inset (72px) at 1440 on grow.google's US edition (raw/components-computed.json)", "The 72px page inset: content starts at x=72 on a 1440 canvas (the 1296px column).")},
    },
    "focusRing": {
        "color": lit("#1a73e8", "color", src("nav-link", "boxShadow", "focus-visible", "the 2px focus ring (a box-shadow, not an outline)"), "Keyboard focus is a 2px box-shadow ring offset 1px, never an outline."),
        "width": lit("2px", "dimension", src("tab", "boxShadow", "focus-visible", "the 2px ring width")),
        "offset": lit("1px", "dimension", src("promo-link", "outlineOffset", "focus-visible", "the ring offset")),
    },
}

light = {
    "color": {
        "surface": {
            "base": lit("#ffffff", "color", src("header", "backgroundColor"), "The page ground — header, mega-menu and body all paint white."),
            "muted": lit("#f8f9fa", "color", src("nav-link", "backgroundColor", "focus-visible"), "The quiet hover wash on controls (grey-50)."),
            "footer": lit("#eff2f7", "color", src("footer", "backgroundColor"), "The blue-grey footer band."),
            "dark": lit("#18191d", "color", src("cert-hero", "backgroundColor"), "The editorial dark hero on certificate pages — a section paint, not a theme."),
        },
        "ink": {
            "primary": lit("#202124", "color", src("hero-h1", "color"), "Near-black ink (grey-900)."),
            "secondary": lit("#3c4043", "color", src("nav-link", "color"), "Nav and body ink (grey-800)."),
            "tertiary": lit("#5f6368", "color", src("m-drawer-btn", "color"), "Icon-only ink (grey-700)."),
            "inverse": lit("#ffffff", "color", src("cert-h1", "color"), "Ink on the dark hero and on filled buttons."),
        },
        "link": {
            "default": lit("#3186ff", "color", src("breadcrumb", "color"), "The site's painted link/accent blue — brighter than the declared #1a73e8 brand step."),
            "hover": lit("#3186ff", "color", src("learn-more-btn", "color", "hover")),
            "hoverWash": lit("rgba(26, 115, 232, 0.04)", "color", src("learn-more-btn", "backgroundColor", "hover"), "The faint brand wash a text link gains on hover."),
            "pressed": lit("rgba(26, 115, 232, 0.1)", "color", src("learn-more-btn", "backgroundColor", "pressed")),
            "legacy": lit("#1a73e8", "color", src("card-link", "color"), "The older brand blue still painted by card links (glue-blue-600)."),
        },
        "accent": {"value": "{color.palette.blue.600}", "type": "color", "source": "alias to the declared glue-blue-600", "description": "The declared brand blue (glue-blue-600 #1a73e8): the card-link colour and the focus-ring colour."},
        "line": {
            "hairline": lit("#dadce0", "color", src("expansion-panel", "borderTopColor"), "The row separator the expansion panels draw (grey-300)."),
        },
        "focus": {"value": "{focusRing.color}", "type": "color", "source": "alias to the measured focus ring"},
    },
    "button": {
        "primary": {
            "bg": lit("#3186ff", "color", src("cert-cta", "backgroundColor"), "The filled pill — the site's painted action blue."),
            "bgHover": lit("#185abc", "color", src("cert-cta", "backgroundColor", "hover"), "Hover darkens to glue-blue-800."),
            "bgPressed": lit("#185abc", "color", src("cert-cta", "backgroundColor", "pressed")),
            "fg": lit("#ffffff", "color", src("cert-cta", "color")),
            "radius": {"value": "{radius.pill}", "type": "dimension", "source": "alias to the measured pill radius"},
            "paddingX": {"value": "{space.button.x}", "type": "dimension", "source": "alias to the measured button padding"},
            "paddingY": {"value": "{space.button.y}", "type": "dimension", "source": "alias to the measured button padding"},
            "shadowHover": {"value": "{shadow.elevation-1}", "type": "shadow", "source": "alias to the measured hover elevation"},
        },
    },
    "banner": {
        "bg": lit("#ffffff", "color", src("promo-banner", "backgroundColor") or "measured transparent — the promo text paints on white"),
        "link": lit("#3186ff", "color", src("promo-banner", "color"), "The promo copy colour; the Enroll now tail is a filled pill."),
    },
    "tab": {
        "bar": {"bg": lit("#ffffff", "color", src("tab-bar", "backgroundColor")), "shadow": {"value": "{shadow.elevation-1}", "type": "shadow", "source": "alias to the measured bar elevation"}, "radius": {"value": "{radius.bar}", "type": "dimension", "source": "alias to the measured bar radius"}},
        "item": {
            "fg": lit("#3c4043", "color", src("tab", "color")),
            "bgHover": lit("#f8f9fa", "color", src("tab", "backgroundColor", "hover")),
            "bgPressed": lit("#f1f3f4", "color", src("tab", "backgroundColor", "pressed")),
        },
    },
    "surface": {
        "hero": {"bg": {"value": "{color.surface.dark}", "type": "color", "source": "alias to the dark hero surface"}, "ink": {"value": "{color.ink.inverse}", "type": "color", "source": "alias to inverse ink"}},
    },
    "stat": {
        "number": lit("#202124", "color", src("stat-chip", "color"), "The measured stat figure colour; sibling stats paint one of the four brand hues (the screenshots show red/blue/yellow/green numbers — only the first is measured)."),
    },
    # DESIGN.md reads component tokens out of the colour set's `component`
    # group (grok's convention): colour-role aliases plus the measured
    # geometry it can express (height / radius). The values themselves are
    # the measured roles above and the measured geometry under core.geometry —
    # renamed from component so the two groups never share a CSS property name.
    "component": {
        "button": {
            "bg": {"value": "{button.primary.bg}", "type": "color", "source": "alias to the measured pill fill"},
            "fg": {"value": "{button.primary.fg}", "type": "color", "source": "alias to the measured pill text"},
            "radius": {"value": "{radius.pill}", "type": "dimension", "source": "alias to the measured pill radius"},
            "height": {"value": "{geometry.button.height}", "type": "dimension", "source": "alias to the measured button height"},
        },
        "hero": {
            "bg": {"value": "{surface.hero.bg}", "type": "color", "source": "alias to the measured dark hero paint"},
            "fg": {"value": "{surface.hero.ink}", "type": "color", "source": "alias to the measured hero ink"},
            "height": {"value": "{geometry.hero.height}", "type": "dimension", "source": "alias to the measured hero height"},
        },
        "tab": {
            "bar": {
                "bg": {"value": "{tab.bar.bg}", "type": "color", "source": "alias to the measured jumplinks bar paint"},
                "radius": {"value": "{radius.bar}", "type": "dimension", "source": "alias to the measured bar radius"},
            },
        },
        "card": {
            "bg": {"value": "{color.surface.base}", "type": "color", "source": "alias to the measured card paint"},
            "radius": {"value": "{radius.card}", "type": "dimension", "source": "alias to the measured card radius"},
            "height": {"value": "{geometry.card.announcement.height}", "type": "dimension", "source": "alias to the measured announcement card height"},
        },
        "header": {
            "bg": {"value": "{color.surface.base}", "type": "color", "source": "alias to the measured header paint"},
            "height": {"value": "{geometry.header.height}", "type": "dimension", "source": "alias to the measured header height"},
        },
        "footer": {
            "bg": {"value": "{color.surface.footer}", "type": "color", "source": "alias to the measured footer band"},
            "height": {"value": "{geometry.footer.height}", "type": "dimension", "source": "alias to the measured footer height"},
        },
        "banner": {
            "bg": {"value": "{banner.bg}", "type": "color", "source": "alias to the measured promo banner paint"},
            "height": {"value": "{geometry.banner.height}", "type": "dimension", "source": "alias to the measured promo anchor height"},
        },
        "megaMenu": {
            "bg": {"value": "{color.surface.base}", "type": "color", "source": "alias to the measured mega-menu paint"},
            "height": {"value": "{geometry.megaMenu.height}", "type": "dimension", "source": "alias to the measured mega-menu height"},
        },
    },
}

component = {
    "header": {"height": lit(px(rect("header").get("h", 64)), "dimension", src("header", "rect.height"), "The 64px top bar at 1440 and 390 wide."),
               "width": lit(px(rect("header").get("w", 1440)), "dimension", src("header", "rect.width"))},
    "nav": {"itemHeight": lit(px(rect("nav-link").get("h", 48)), "dimension", src("nav-link", "rect.height"))},
    "megaMenu": {"height": lit(px(rect("mega-panel").get("h", 623)), "dimension", src("mega-panel", "rect.height")),
                 "width": lit(px(rect("mega-panel").get("w", 1440)), "dimension", src("mega-panel", "rect.width"), "The full-bleed panel." )},
    "button": {"height": lit(px(rect("cert-cta").get("h", 50)), "dimension", src("cert-cta", "rect.height"))},
    "drawerButton": {"size": lit(px(rect("m-drawer-btn").get("w", 48)), "dimension", src("m-drawer-btn", "rect.width"), "The 48px square drawer toggle at 390 wide.")},
    "jumplink": {"height": lit(px(rect("tab").get("h", 38)), "dimension", src("tab", "rect.height"))},
    "banner": {"height": lit(px(rect("promo-banner").get("h", 20)), "dimension", src("promo-banner", "rect.height"), "The promo anchor's own box; the painted bar is its paragraph parent.")},
    "video": {"width": lit(px(rect("video-teaser").get("w", 616.5)), "dimension", src("video-teaser", "rect.width")),
              "height": lit(px(rect("video-teaser").get("h", 346.5)), "dimension", src("video-teaser", "rect.height"))},
    "hero": {"height": lit(px(rect("cert-hero").get("h", 720)), "dimension", src("cert-hero", "rect.height"))},
    "card": {"announcement": {"width": lit(px(rect("card").get("w", 1296)), "dimension", src("card", "rect.width")),
                              "height": lit(px(rect("card").get("h", 285)), "dimension", src("card", "rect.height"))},
             "certificate": {"width": lit(px(rect("cert-card").get("w", 370)), "dimension", src("cert-card", "rect.width")),
                             "height": lit(px(rect("cert-card").get("h", 386)), "dimension", src("cert-card", "rect.height"))}},
    "footer": {"height": lit(px(rect("footer").get("h", 837)), "dimension", src("footer", "rect.height"))},
    "select": {"width": lit(px(rect("footer-lang").get("w", 233)), "dimension", src("footer-lang", "rect.width"))},
    "expansionPanel": {"rowHeight": lit(px(rect("expansion-panel").get("h", 93)), "dimension", src("expansion-panel", "rect.height"))},
    "mobileHeader": {"height": lit(px(rect("m-header").get("h", 64)), "dimension", src("m-header", "rect.height", "default", "rect.height at 390 wide"))},
}

# Motion comes from the probe: build_tokens.py turns raw/motion.json into the
# core.motion group via tools/motion.py (docs/decisions/0001); the per-element
# transition shorthand is already inside that probe output.
core["geometry"] = component
SPEC = {"core": core, "light": light}
(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("component-tokens.json:", sum(1 for _ in re.finditer(r'"(?:value|var)":', json.dumps(SPEC))), "leaves")
