#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

exactly.ai is a Framer-published marketing site that paints one light theme on
every signed-out surface. Its declared design layer is small and flat
(raw/css-vars.json): 27 --token-<uuid> colour names on <body> — the Framer
"colour styles" the site's components read — and nothing else of intent (the
rest of the custom properties are per-component --framer-* internals and
embedded-widget vars). Everything below either names one of those variables
("var") or carries a computed value measured on the real DOM
(raw/components-computed.json) with the measurement it came from ("source").

Measured shape of the system, signed out at 1440 x 900 (mobile 390 x 844):

  palette   #fb411f accent (the Start-for-free pill on interior pages, the
            "For free" chip), #1e1e1e ink (text, the dark CTA fill), #000
            (footer canvas), #fff and #f7f7f7 surfaces, alpha greys
            #40404006-99 and #7c7c7c06-1a washes, #ffffff0a-99 whites
  on-image  the photo-hero surfaces invert the header: white nav text, a
            white Start-for-free pill and a rgba(255,255,255,.1) glass
            Book-a-demo pill over the picture
  type      Inter wght 300 display 47px/60 -1.88px (27px/36 on mobile),
            Inter Variable 32/44 article h2, 22/32 leads and article prose,
            21/32 card titles (Inter on the plan cards, Inter Variable on
            showcase) and footer text, 14/20 UI, 16/32 the modal search
            field; 600 only for caption links
  shape     1000px pills (nav links, CTAs), 100px plan CTAs, 40px cards,
            square text
  motion    0.2s colour transitions on links

The site gives no dark theme: one prefers-color-scheme media rule repaints
nothing, so the export holds a single light set.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def var(name, ty="color", **kw):
    if name not in R:
        raise KeyError(f"{name} is not a resolved variable in raw/css-vars.json")
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def val(value, ty, source, **kw):
    d = {"value": value, "type": ty, "source": f"measured {source}"}
    d.update(kw)
    return d


def st(key, state="default"):
    return C[key]["states"][state]["style"]


def tts(key, state="default"):
    return C[key]["states"][state].get("textStyle") or {}


def fg(key, state="default"):
    """The painted text colour: the descendant text node when one exists,
    else the element's own colour."""
    return (tts(key, state).get("color") or st(key, state)["color"])


def bg(key, state="default"):
    return st(key, state)["backgroundColor"]


def fs(key, state="default"):
    t = tts(key, state)
    return (t.get("fontSize") or st(key, state)["fontSize"]), (t.get("lineHeight") or st(key, state)["lineHeight"])


def ff(key, state="default"):
    return tts(key, state).get("fontFamily") or st(key, state)["fontFamily"]


def fw(key, state="default"):
    return int(tts(key, state).get("fontWeight") or st(key, state)["fontWeight"])


def ls(key, state="default"):
    return tts(key, state).get("letterSpacing") or st(key, state)["letterSpacing"]


def rect(key, dim, state="default"):
    """A measured box edge as a px dimension (the rect is recorded in CSS px, 2 decimals)."""
    return ("%g" % round(C[key]["states"][state]["rect"][dim], 2)) + "px"


M = "computed style of {k} {s} (raw/components-computed.json)"


def mm(key, prop, state="default"):
    return M.format(k=key, s=state) + " · " + prop


# ---- the declared palette: every --token-* the site ships, by role ----
# (name, token path, what the site uses it for, as far as measurement shows)
PALETTE = [
    ("--token-6bd2bf74-c0db-460d-af58-5af6b5254b54", "ink", "#1e1e1e — primary ink: body and heading text on light, the dark CTA fill on plan cards"),
    ("--token-7e2e2b25-d7c2-4e1b-8c85-c488cce631cd", "ink-alt", "#1e1e1e — a second ink declaration (Framer colour styles are duplicated per use)"),
    ("--token-b0f4d26e-7fc3-444b-98ee-f5c162ef3422", "black", "#000 — the footer canvas and true-black text"),
    ("--token-ba35b1b8-095f-4e2a-a672-6cac2a527073", "black-alt", "#000 — a second black declaration"),
    ("--token-fca3ff45-f85b-4188-8a5a-4165f4a664e8", "black-70", "rgba(0,0,0,.7) — translucent black"),
    ("--token-c81b98ef-023d-46a5-bb93-d03732a947eb", "black-20", "rgba(0,0,0,.2) — a pale black wash"),
    ("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", "paper", "#fff — page canvas and the light pill fill"),
    ("--token-279276a7-1140-4de3-9fda-da103e5da9f4", "paper-2", "#fff — second white (the support-bubble fill reads it)"),
    ("--token-86c05ec3-f643-416d-b481-7d691d035bf0", "paper-3", "#fff — third white"),
    ("--token-d1e1eac9-5c52-46a9-8c88-c4c7aa28ccec", "paper-4", "#fff — fourth white"),
    ("--token-04831ba3-78f3-4aa2-ae8b-5e5356257505", "paper-5", "#fff — fifth white"),
    ("--token-bd46276e-f33e-4c99-835d-b15019849f13", "mist", "#f7f7f7 — card fill: showcase card inner, the plan cards' ancestor surface"),
    ("--token-97a5b36a-40e1-41a1-b620-975afa509dc7", "mist-85", "rgba(235,235,235,.85) — a milky surface"),
    ("--token-60e752ab-0c0a-4597-9846-dec051a62533", "accent", "#fb411f — the brand orange: Start-for-free pill on interior pages, the For-free chip"),
    ("--token-1c76e087-ac93-4255-838e-bfbcd3918e85", "accent-alt", "#fb411f — a second accent declaration"),
    ("--token-63655132-06e3-46c9-b5e5-e10ca2cfd708", "grey-08", "rgba(64,64,64,.08) — a hairline grey wash"),
    ("--token-95c74eec-178d-4c0f-b3bb-cd5ff24bf37d", "grey-16", "rgba(64,64,64,.16) — a light grey wash"),
    ("--token-a4dfd562-a99a-4d54-8ac2-2686e42dcc9f", "grey-36", "rgba(64,64,64,.36) — a mid grey"),
    ("--token-fc8120db-7707-4e3b-a78e-7fe0b0fa7602", "grey-48", "rgba(64,64,64,.48) — placeholder and muted text"),
    ("--token-6c14e0fb-f377-48f9-8e72-c2739403571a", "grey-60", "rgba(64,64,64,.6) — secondary text (the plan price)"),
    ("--token-81ce0e37-29f5-44cd-96c7-39e2529798a0", "warm-06", "rgba(124,124,124,.06) — the faintest neutral wash"),
    ("--token-65e1419e-26fc-4200-9266-4d550957818c", "warm-08", "rgba(124,124,124,.08) — chip and field fill: the Search… trigger, collection cards, the Read-study pill"),
    ("--token-50d79254-7011-4ac9-b365-d3a67e6d6bdf", "warm-10", "rgba(124,124,124,.10) — a slightly deeper neutral wash"),
    ("--token-faf5189b-ad03-49a0-aa02-6413224fcc45", "white-10", "rgba(255,255,255,.1) — the glass Book-a-demo pill over the hero photo"),
    ("--token-43760daa-8737-46ce-9555-3aba75b59bb4", "white-20", "rgba(255,255,255,.2) — the industry-card image border"),
    ("--token-e48c39d2-dcde-49d6-a9ce-92b2b7d12341", "white-40", "rgba(255,255,255,.4) — a soft white"),
    ("--token-3a806071-b041-43a8-b489-4903bdd7258c", "white-60", "rgba(255,255,255,.6) — muted on-image text: hero sub, footer text"),
]
palette = {}
for name, path, desc in PALETTE:
    palette[path] = var(name, description=desc)

SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. exactly.ai's declared design layer is "
        "the 27 --token-* colour names its Framer stylesheets put on <body> (raw/css-vars.json); "
        "everything else is measured computed style (raw/components-computed.json). One light theme: "
        "the site paints light on every signed-out surface, and its single prefers-color-scheme media "
        "rule repaints nothing. Leaves either name a variable ('var', resolved in light) or carry a "
        "measured value with its source ('value' + 'source')."
    ),
    "core": {
        "color": {"palette": palette},
        "font": {
            "family": {
                "display": val(ff("hero-h1"), "fontFamily", mm("hero-h1", "fontFamily"), description="Inter with its 'Inter Placeholder' fallback — the wght-300 display face (hero, section and page headlines)."),
                "ui": val(ff("nav-cta"), "fontFamily", mm("nav-cta", "fontFamily"), description="Inter Variable with placeholder fallback — UI text: nav, CTAs, card titles, footer."),
                "body": val(ff("article-body"), "fontFamily", mm("article-body", "fontFamily"), description="Inter Variable — article and long-form text."),
                "card": val(ff("plan-name"), "fontFamily", mm("plan-name", "fontFamily"), description="Inter with its 'Inter Placeholder' fallback — the plan-card title face (showcase card titles paint Inter Variable)."),
            },
            "size": {
                "display": val(fs("hero-h1")[0], "dimension", mm("hero-h1", "fontSize"), description="Display size: every h1 and the 47px section headings.", responsive={"mobile": fs("m-hero-h1")[0]}),
                "display-sm": val(fs("m-hero-h1")[0], "dimension", mm("m-hero-h1", "fontSize"), description="The display at 390 wide."),
                "heading-2": val(fs("article-h2")[0], "dimension", mm("article-h2", "fontSize"), description="Article section headings."),
                "lead": val(fs("article-body")[0], "dimension", mm("article-body", "fontSize"), description="Lead and article body size; also the FAQ question/answer text."),
                "card": val(fs("plan-name")[0], "dimension", mm("plan-name", "fontSize"), description="Card titles (h4/h5) and footer text."),
                "drawer": val(fs("m-drawer-link")[0], "dimension", mm("m-drawer-link", "fontSize"), description="Mobile drawer links."),
                "field": val(fs("help-search-input")[0], "dimension", mm("help-search-input", "fontSize"), description="The modal search field."),
                "ui": val(fs("nav-cta")[0], "dimension", mm("nav-cta", "fontSize"), description="UI text: nav links, CTA labels, plan features, chips."),
            },
            "weight": {
                "light": val(fw("hero-h1"), "fontWeight", mm("hero-h1", "fontWeight"), description="Display headlines."),
                "regular": val(fw("article-body"), "fontWeight", mm("article-body", "fontWeight"), description="Everything else."),
                "semibold": val(fw("read-more"), "fontWeight", mm("read-more", "fontWeight"), description="Caption links only (Read more, industry-card titles)."),
            },
            "lineHeight": {
                "display": val(fs("hero-h1")[1], "dimension", mm("hero-h1", "lineHeight")),
                "display-sm": val(fs("m-hero-h1")[1], "dimension", mm("m-hero-h1", "lineHeight")),
                "heading-2": val(fs("article-h2")[1], "dimension", mm("article-h2", "lineHeight")),
                "lead": val(fs("article-body")[1], "dimension", mm("article-body", "lineHeight")),
                "card": val(fs("plan-name")[1], "dimension", mm("plan-name", "lineHeight")),
                "drawer": val(fs("m-drawer-link")[1], "dimension", mm("m-drawer-link", "lineHeight")),
                "field": val(fs("help-search-input")[1], "dimension", mm("help-search-input", "lineHeight")),
                "ui": val(fs("nav-cta")[1], "dimension", mm("nav-cta", "lineHeight")),
            },
            "letterSpacing": {
                "display": val(ls("hero-h1"), "dimension", mm("hero-h1", "letterSpacing"), description="-4% of the display size."),
                "display-sm": val(ls("m-hero-h1"), "dimension", mm("m-hero-h1", "letterSpacing")),
                "heading-2": val(ls("article-h2"), "dimension", mm("article-h2", "letterSpacing")),
                "lead": val(ls("article-body"), "dimension", mm("article-body", "letterSpacing")),
                "card": val(ls("plan-name"), "dimension", mm("plan-name", "letterSpacing")),
                "card-alt": val(ls("showcase-card-title"), "dimension", mm("showcase-card-title", "letterSpacing")),
                "semibold-ui": val(ls("read-more"), "dimension", mm("read-more", "letterSpacing")),
                "none": {"value": "0px" if ls("nav-cta") == "normal" else ls("nav-cta"), "type": "dimension",
                         "source": "derived: " + mm("nav-cta", "letterSpacing") + " is 'normal', which tracks at 0px",
                         "description": "UI text tracks normally."},
            },
        },
        "typography": {
            "display": {"$type": "typography", "$value": {"fontFamily": "{font.family.display}", "fontSize": "{font.size.display}", "fontWeight": "{font.weight.light}", "lineHeight": "{font.lineHeight.display}", "letterSpacing": "{font.letterSpacing.display}"}, "$extensions": {"source": "composed from the hero-h1 measurements"}},
            "heading-2": {"$type": "typography", "$value": {"fontFamily": "{font.family.ui}", "fontSize": "{font.size.heading-2}", "fontWeight": "{font.weight.regular}", "lineHeight": "{font.lineHeight.heading-2}", "letterSpacing": "{font.letterSpacing.heading-2}"}, "$extensions": {"source": "composed from the article-h2 measurements"}},
            "lead": {"$type": "typography", "$value": {"fontFamily": "{font.family.body}", "fontSize": "{font.size.lead}", "fontWeight": "{font.weight.regular}", "lineHeight": "{font.lineHeight.lead}", "letterSpacing": "{font.letterSpacing.lead}"}, "$extensions": {"source": "composed from the article-body measurements"}},
            "card": {"$type": "typography", "$value": {"fontFamily": "{font.family.card}", "fontSize": "{font.size.card}", "fontWeight": "{font.weight.regular}", "lineHeight": "{font.lineHeight.card}", "letterSpacing": "{font.letterSpacing.card}"}, "$extensions": {"source": "composed from the plan-name measurements"}},
            "ui": {"$type": "typography", "$value": {"fontFamily": "{font.family.ui}", "fontSize": "{font.size.ui}", "fontWeight": "{font.weight.regular}", "lineHeight": "{font.lineHeight.ui}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the nav-cta measurements"}},
        },
        "radius": {
            "none": val(st("hero-h1")["borderTopLeftRadius"], "dimension", mm("hero-h1", "borderTopLeftRadius"), description="Text and prose blocks are square."),
            "card": val(st("help-card")["borderTopLeftRadius"], "dimension", mm("help-card", "borderTopLeftRadius"), description="The soft card corner: collection cards on the help landing."),
            "cta": val(st("plan-cta")["borderTopLeftRadius"], "dimension", mm("plan-cta", "borderTopLeftRadius"), description="The plan cards' 56px CTAs are fully rounded at 100px."),
            "pill": val(st("nav-cta")["borderTopLeftRadius"], "dimension", mm("nav-cta", "borderTopLeftRadius"), description="Pills: nav links, hero CTAs, the Join pill, drawer links — 1000px, effectively a capsule."),
        },
        "space": {
            "4": val(st("m-drawer-link")["paddingTop"], "dimension", mm("m-drawer-link", "paddingTop"), description="Drawer link vertical padding."),
            "6": val(st("m-join")["paddingTop"], "dimension", mm("m-join", "paddingTop"), description="Join pill and sidebar-link vertical padding."),
            "8": val(st("nav-link")["paddingTop"], "dimension", mm("nav-link", "paddingTop"), description="Nav link vertical padding and footer side padding."),
            "12": val(st("nav-link")["paddingRight"], "dimension", mm("nav-link", "paddingRight"), description="Nav link horizontal padding."),
            "16": val(st("nav-cta")["paddingRight"], "dimension", mm("nav-cta", "paddingRight"), description="Header pill and drawer-link horizontal padding."),
            "18": val(st("hero-cta")["paddingTop"], "dimension", mm("hero-cta", "paddingTop"), description="CTA vertical padding."),
            "24": val(st("hero-cta")["paddingRight"], "dimension", mm("hero-cta", "paddingRight"), description="CTA horizontal padding; the sidebar's side padding."),
            "40": val(st("help-card")["paddingTop"], "dimension", mm("help-card", "paddingTop"), description="Card padding (collection cards, the compare bar's vertical padding)."),
        },
        "duration": {
            "fast": val(st("footer-link")["transitionDuration"], "duration", mm("footer-link", "transitionDuration"), description="The link colour transition (footer and article links)."),
        },
    },
    "light": {
        "canvas": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="Page canvas — white on every signed-out route."),
        "ink": var("--token-6bd2bf74-c0db-460d-af58-5af6b5254b54", description="Primary text and the dark pill fill."),
        "ink-deep": var("--token-b0f4d26e-7fc3-444b-98ee-f5c162ef3422", description="True black: the footer canvas."),
        "muted": var("--token-fc8120db-7707-4e3b-a78e-7fe0b0fa7602", description="Placeholder and muted text (Search… caption, industry meta)."),
        "muted-strong": var("--token-6c14e0fb-f377-48f9-8e72-c2739403571a", description="Secondary text: the plan price line."),
        "surface": {
            "card": var("--token-bd46276e-f33e-4c99-835d-b15019849f13", description="#f7f7f7 card fill."),
            "chip": var("--token-65e1419e-26fc-4200-9266-4d550957818c", description="rgba(124,124,124,.08): the Search… field, collection cards, Read-study pill."),
            "milk": var("--token-97a5b36a-40e1-41a1-b620-975afa509dc7", description="rgba(235,235,235,.85) milky surface."),
        },
        "accent": var("--token-60e752ab-0c0a-4597-9846-dec051a62533", description="#fb411f: the Start-for-free pill on interior pages and the For-free chip."),
        "on-accent": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="White text on the accent pill."),
        "pill": {
            "light": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="The white pill: nav CTA over the hero, hero Start-for-free, mobile Join."),
            "light-ink": var("--token-b0f4d26e-7fc3-444b-98ee-f5c162ef3422", description="Black text on the white pill (nav CTA over the hero)."),
            "dark": var("--token-6bd2bf74-c0db-460d-af58-5af6b5254b54", description="The #1e1e1e pill: plan-card CTAs."),
            "dark-ink": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="White text on the dark pill."),
        },
        "on-image": {
            "ink": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="White text over the photo hero."),
            "muted": var("--token-3a806071-b041-43a8-b489-4903bdd7258c", description="rgba(255,255,255,.6): the hero sub and footer text."),
            "soft": var("--token-e48c39d2-dcde-49d6-a9ce-92b2b7d12341", description="rgba(255,255,255,.4)."),
            "glass": var("--token-faf5189b-ad03-49a0-aa02-6413224fcc45", description="rgba(255,255,255,.1): the Book-a-demo glass pill."),
            "line": var("--token-43760daa-8737-46ce-9555-3aba75b59bb4", description="rgba(255,255,255,.2): the industry-card image border."),
        },
        "footer": {
            "bg": var("--token-b0f4d26e-7fc3-444b-98ee-f5c162ef3422", description="The footer's black canvas."),
            "ink": var("--token-ca1cbd0d-a33b-4062-9b3e-175f9be495d4", description="Footer link text."),
            "muted": var("--token-3a806071-b041-43a8-b489-4903bdd7258c", description="rgba(255,255,255,.6) footer body text."),
        },
        "focus": {
            # Both rings are `outline: auto` in the colour Chrome uses for its own focus ring (#101010 on
            # the desktop pass, #e59700 under the phone emulation): the browser picks it, not the site.
            "ring": val(st("nav-cta", "focus-visible")["outlineColor"], "color",
                        mm("nav-cta", "outlineColor", "focus-visible") + "; outline-style " + st("nav-cta", "focus-visible")["outlineStyle"]
                        + ", in Chrome's own default focus-ring colour, so the browser chose it, not the site",
                        description="The 1px auto focus ring the browser draws on interactive elements (desktop pass); the site sets no focus colour of its own."),
            "ring-mobile": val(st("m-join", "focus-visible")["outlineColor"], "color",
                               mm("m-join", "outlineColor", "focus-visible") + "; outline-style " + st("m-join", "focus-visible")["outlineStyle"]
                               + ", in the colour Chrome's phone emulation uses for its own focus ring, so the browser chose it, not the site",
                               description="The same browser-drawn ring at 390 wide: Chrome's phone emulation draws it in #e59700; the site sets no focus colour of its own."),
            "width": val(st("nav-cta", "focus-visible")["outlineWidth"], "dimension", mm("nav-cta", "outlineWidth", "focus-visible")),
            "offset": val(st("nav-cta", "focus-visible")["outlineOffset"], "dimension", mm("nav-cta", "outlineOffset", "focus-visible")),
        },
    },
    "component": {
        "nav": {
            "height": val(rect("nav-header", "h"), "dimension", mm("nav-header", "rect height"), description="The fixed desktop header."),
            "pill-height": val(rect("nav-cta", "h"), "dimension", mm("nav-cta", "rect height"), description="Header link and pill height."),
        },
        "cta": {
            "height": val(rect("hero-cta", "h"), "dimension", mm("hero-cta", "rect height"), description="The large pill CTAs."),
            "padding-x": val(st("hero-cta")["paddingRight"], "dimension", mm("hero-cta", "paddingRight")),
            "padding-y": val(st("hero-cta")["paddingTop"], "dimension", mm("hero-cta", "paddingTop")),
        },
        "card": {
            "plan-width": val(rect("plan-card", "w"), "dimension", mm("plan-card", "rect width"), description="A plan card at 1440."),
            "plan-height": val(rect("plan-card", "h"), "dimension", mm("plan-card", "rect height")),
            "help-width": val(rect("help-card", "w"), "dimension", mm("help-card", "rect width"), description="A help collection card."),
            "showcase-width": val(rect("showcase-card", "w"), "dimension", mm("showcase-card", "rect width"), description="A showcase brand card at 1440 (two-column grid)."),
            "case-width": val(rect("case-card", "w"), "dimension", mm("case-card", "rect width"), description="A case-study row's text block."),
        },
        "field": {
            "search-width": val(rect("help-search", "w"), "dimension", mm("help-search", "rect width"), description="The Search… trigger field."),
            "search-height": val(rect("help-search", "h"), "dimension", mm("help-search", "rect height")),
            "modal-input-width": val(rect("help-search-input", "w"), "dimension", mm("help-search-input", "rect width"), description="The real input inside the Framer search modal."),
            "modal-input-height": val(rect("help-search-input", "h"), "dimension", mm("help-search-input", "rect height")),
        },
        "mobile": {
            "topbar-height": val(rect("m-topbar", "h"), "dimension", mm("m-topbar", "rect height")),
            "hamburger": val(rect("m-hamburger", "w"), "dimension", mm("m-hamburger", "rect width"), description="The 32 x 32 menu toggle."),
            "drawer-link-height": val(rect("m-drawer-link", "h"), "dimension", mm("m-drawer-link", "rect height")),
        },
        "scheduler": {
            "height": val(rect("demo-scheduler", "h"), "dimension", mm("demo-scheduler", "rect height"), description="The embedded booking iframe's height."),
        },
        "sidebar": {
            "width": val(rect("help-sidebar", "w"), "dimension", mm("help-sidebar", "rect width"), description="The help-center doc rail."),
        },
    },
}

out = RAW / "component-tokens.json"
out.write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "type" not in d and "$value" not in d else 1


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
