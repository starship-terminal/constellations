#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

foodnoms.com is a Framer-published marketing site for an iOS/macOS app — no
web sign-in exists, every surface below is reachable signed out. Its declared
design layer is a flat set of ~90 --token-<uuid> colour names on <body>
(raw/css-vars.json): the Framer "colour styles" the components read. 39 of
them are redeclared under a real (prefers-color-scheme: dark) media rule, so
the site paints an authored dark theme — the dark set below names the same
variables and resolves each through the dark pass. Everything either names
one of those variables ("var") or carries a computed value measured on the
real DOM (raw/components-computed.json) with the measurement it came from
("source").

Measured shape of the system, signed out at 1440 x 900 (mobile 390 x 844,
dark via emulated prefers-color-scheme):

  palette   #ff5406-class accent (the orange "Get the App" / "Search" /
            subscribe pills, accordion links, pricing checks — a full
            accent ramp 50-900 plus /0.12 and /0.16 alphas), a neutral ramp
            white -> #0d0d0d, a #2f2f2f ink scale with /0.8-0.06 alphas, and
            a per-nutrient hue set (red, orange, gold, green, teal, blue,
            indigo, violet, purple, pink, steel, brown, link-blue) that
            colours the hero ticker words and goal pills
  dark      the neutral ramp inverts (white->black, #f2f2f2->#1a1a1a, the
            .4/.2 text greys climb to .6/.8) and the accent ramp re-points
            (accent-600 <-> accent-300) — 39 variables repaint; accent-500
            pills and white text stay
  type      the uploaded Aquawax Pro family in three weights: Bold 700 for
            every heading (56px/61.6 hero ticker, 44/48.4 page h1, 36/43.2
            h2, 28/33.6 feature h3, 22/30.8 h4, 18/25.2 card title,
            17/23.8 label), DemiBold 600 16/16 for buttons and tags,
            Medium 500 for body/UI (18/28.8 lede, 16/25.6 body and links,
            15/15 nav, 17/34 search field). Fragment Mono is declared in
            @font-face but no measured surface paints it
  shape     20px-radius 40px pills (nav/hero CTAs, Search, mailto), 40px
            fields/pills (newsletter email + submit), 50px asset pills,
            18.8px feature cards, 12px table rows, square text
  motion    one declared transition: color 400ms cubic-bezier(0.44,0,0.56,1)
            on links; prefers-reduced-motion: reduce changes nothing
"""
import json, pathlib, re

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


M = "computed style of {k} {s} (raw/components-computed.json)"


def mm(key, prop, state="default"):
    return M.format(k=key, s=state) + " · " + prop


# ---- the declared palette: every --token-* the site ships, grouped by the
# colour each resolves to in light. Framer colour styles are duplicated per
# component, so identical colours appear several times; each declaration is
# kept under its own leaf and later duplicates are numbered.
def p3key(v):
    m = re.fullmatch(r"color\(display-p3\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s*(?:/\s*([0-9.eE+-]+%?))?\)", v.strip())
    if m:
        return tuple(round(float(x), 4) for x in m.groups() if x is not None)
    return ("other", v.strip())


ROLE = {
    # the Foodnoms orange ramp
    (0.9961, 0.8784, 0.8353): ("accent-50", "the palest accent tint"),
    (0.9882, 0.7529, 0.6706): ("accent-100", "a light accent tint"),
    (0.9843, 0.6314, 0.5098): ("accent-200", "the accent-pill hover colour and light accent"),
    (0.9765, 0.5059, 0.3451): ("accent-300", "a mid-light accent (the newsletter field's focus-ring placeholder)"),
    (0.9725, 0.3843, 0.1804): ("accent-500", "the brand orange: primary pills, accordion links, pricing checks"),
    (0.7765, 0.3059, 0.1451): ("accent-600", "a deep accent"),
    (0.5843, 0.2314, 0.1098): ("accent-700", "a deeper accent"),
    (0.3882, 0.1529, 0.0706): ("accent-800", "the darkest accent"),
    (0.1961, 0.0784, 0.0353): ("accent-900", "near-black accent"),
    (0.9725, 0.3843, 0.1804, 0.16): ("accent-16", "accent at 16% — a soft accent wash"),
    (0.9725, 0.3843, 0.1804, 0.12): ("accent-12", "accent at 12% — a fainter accent wash"),
    (0.9725, 0.2941, 0.0706): ("accent-deep", "a saturated red-orange beside the main ramp"),
    # neutral ramp
    (1.0, 1.0, 1.0): ("neutral-0", "white"),
    (0.9765, 0.9765, 0.9765): ("neutral-25", "near-white"),
    (0.9608, 0.9608, 0.9608): ("neutral-40", "a pale grey"),
    (0.9490, 0.9490, 0.9490): ("neutral-50", "#f2f2f2-class card and field fill"),
    (0.9020, 0.9020, 0.9020): ("neutral-100", "hairline/ring grey"),
    (0.8000, 0.8000, 0.8000): ("neutral-200", "light grey"),
    (0.7000, 0.7000, 0.7000): ("neutral-300", "mid-light grey"),
    (0.6000, 0.6000, 0.6000): ("neutral-400", "mid grey"),
    (0.5020, 0.5020, 0.5020): ("neutral-500", "grey"),
    (0.4000, 0.4000, 0.4000): ("neutral-600", "secondary text grey (nav links, dates)"),
    (0.3010, 0.3010, 0.3010): ("neutral-700", "deep grey"),
    (0.2000, 0.2000, 0.2000): ("neutral-800", "body text grey"),
    (0.1010, 0.1010, 0.1010): ("neutral-900", "near-black surface"),
    (0.0510, 0.0510, 0.0510): ("neutral-950", "#0d0d0d heading ink"),
    (0.0, 0.0, 0.0): ("neutral-1000", "black"),
    # the #2f2f2f ink scale with alphas
    (0.1843, 0.1843, 0.1843): ("ink", "#2f2f2f ink — the search-field text"),
    (0.1843, 0.1843, 0.1843, 0.8): ("ink-80", "ink at 80%"),
    (0.1843, 0.1843, 0.1843, 0.64): ("ink-64", "ink at 64%"),
    (0.1843, 0.1843, 0.1843, 0.26): ("ink-26", "ink at 26% — a hairline wash"),
    (0.1843, 0.1843, 0.1843, 0.06): ("ink-6", "ink at 6% — the faintest wash"),
    # black/white/grey alphas
    (0.0, 0.0, 0.0, 0.04): ("black-4", "black at 4% — a hairline wash"),
    (0.0, 0.0, 0.0, 0.08): ("black-8", "black at 8%"),
    (1.0, 1.0, 1.0, 0.16): ("white-16", "white at 16% — an on-dark hairline"),
    (0.8157, 0.8157, 0.8157, 0.36): ("wash-36", "a grey wash at 36%"),
    # the per-nutrient hue set (hero ticker words and goal pills)
    (0.9451, 0.1882, 0.1882): ("red", "goal hue — red"),
    (0.9647, 0.4667, 0.1412): ("orange", "goal hue — orange"),
    (1.0, 0.7490, 0.0078): ("yellow", "goal hue — gold"),
    (0.3020, 0.6902, 0.3098): ("green", "goal hue — green"),
    (0.1059, 0.6510, 0.8471): ("teal", "goal hue — teal (a values-card glyph tint)"),
    (0.1294, 0.5882, 0.9490): ("blue", "goal hue — blue (a feature-card title)"),
    (0.3451, 0.3373, 0.8392): ("indigo", "goal hue — indigo (a values-card glyph, a pricing check)"),
    (0.3882, 0.3922, 1.0): ("violet", "goal hue — violet"),
    (0.6863, 0.3216, 0.8706): ("purple", "goal hue — purple"),
    (0.7569, 0.2078, 0.5176): ("pink", "goal hue — pink"),
    (0.4863, 0.6314, 0.7608): ("steel", "goal hue — steel blue (the shield glyph)"),
    (0.5451, 0.3373, 0.1059): ("brown", "goal hue — brown"),
    (0.0, 0.4784, 1.0): ("link", "link blue"),
    (0.3451, 0.3373, 0.8392, 0.4): ("indigo-40", "indigo at 40%"),
    (0.3882, 0.3922, 1.0, 0.16): ("violet-16", "violet at 16%"),
    (0.7569, 0.2078, 0.5176, 0.16): ("pink-16", "pink at 16%"),
    (0.0, 0.4784, 1.0, 0.16): ("link-16", "link blue at 16%"),
    (0.0, 0.5216, 1.0, 0.16): ("link-alt-16", "a slightly brighter link blue at 16%"),
}

groups = {}
for n, v in R.items():
    if not n.startswith("--token-"):
        continue
    groups.setdefault(p3key(v), []).append(n)

palette = {}
for key, names in sorted(groups.items(), key=lambda kv: (str(kv[0]))):
    role, desc = ROLE.get(key, (f"misc-{len(palette)}", "a declared --token-* colour with no observed role"))
    for i, name in enumerate(sorted(names)):
        path = role if i == 0 else f"{role}-{i + 1}"
        d = desc if i == 0 else f"{desc} (a duplicate declaration — Framer colour styles repeat per component)"
        palette[path] = var(name, description=d)

SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. foodnoms.com's declared design layer is "
        "the ~90 --token-* colour names its Framer stylesheets put on <body> (raw/css-vars.json); "
        "everything else is measured computed style (raw/components-computed.json). Two authored themes: "
        "the same stylesheet redeclares 39 of those names under prefers-color-scheme: dark, so 'dark' "
        "names the same variables and resolves each through the emulated dark pass — the theme a "
        "dark-system visitor actually gets. Leaves either name a variable ('var', resolved in that "
        "theme) or carry a measured value with its source ('value' + 'source')."
    ),
    "core": {
        "color": {"palette": palette},
        "font": {
            "family": {
                "display": val(ff("hero-ticker"), "fontFamily", mm("hero-ticker", "fontFamily"), description="Aquawax Pro Bold with its 'Aquawax Pro Bold Placeholder' fallback — every heading: hero ticker, page h1s, h2-h4, labels, the wordmark."),
                "ui": val(ff("hero-lede"), "fontFamily", mm("hero-lede", "fontFamily"), description="Aquawax Pro Medium with its placeholder fallback — body and UI text."),
                "button": val(ff("nav-cta"), "fontFamily", mm("nav-cta", "fontFamily"), description="Aquawax Pro DemiBold with its placeholder fallback — every pill button and the pricing tag chip."),
                "mono": val('"Fragment Mono", monospace', "fontFamily", "the site declares a Fragment Mono @font-face (raw/css-vars.json fonts); no measured signed-out surface paints it", description="Declared mono face (unpainted on the measured surfaces)."),
            },
            "size": {
                "ticker": val("56px", "dimension", mm("hero-ticker", "fontSize"), description="The rotating hero headline."),
                "page": val("44px", "dimension", mm("help-h1", "fontSize"), description="Page headlines (h1 on help, news, press, articles, legal, the interstitial)."),
                "heading-2": val("36px", "dimension", mm("ha-h2", "fontSize"), description="Section headings (CTA, newsletter, article h2)."),
                "card": val("28px", "dimension", mm("feature-title", "fontSize"), description="Feature-card titles (22px at 390 wide).", responsive={"mobile": "22px"}),
                "heading-4": val("22px", "dimension", mm("featured-title", "fontSize"), description="h4 labels (As Featured By, values titles, mobile feature titles)."),
                "title": val("18px", "dimension", mm("review-card", "fontSize"), description="Card titles and accordion headers (18px); also the lede size."),
                "label": val("17px", "dimension", mm("ha-tag", "fontSize"), description="Labels: article tags, dates, footer headings, table headers."),
                "body": val("16px", "dimension", mm("ha-body", "fontSize"), description="Body text, accordion links, table rows, button labels."),
                "ui": val("15px", "dimension", mm("nav-link", "fontSize"), description="Small UI: nav links, footer links, date chips, tag note."),
            },
            "weight": {
                "bold": val(700, "fontWeight", mm("hero-ticker", "fontWeight"), description="Aquawax Pro Bold — every heading."),
                "demibold": val(600, "fontWeight", mm("nav-cta", "fontWeight"), description="Aquawax Pro DemiBold — buttons and the tag chip."),
                "medium": val(500, "fontWeight", mm("ha-body", "fontWeight"), description="Aquawax Pro Medium — body and UI text."),
            },
            "lineHeight": {
                "ticker": val("61.6px", "dimension", mm("hero-ticker", "lineHeight")),
                "page": val("48.4px", "dimension", mm("help-h1", "lineHeight")),
                "heading-2": val("43.2px", "dimension", mm("ha-h2", "lineHeight")),
                "card": val("33.6px", "dimension", mm("feature-title", "lineHeight")),
                "heading-4": val("30.8px", "dimension", mm("featured-title", "lineHeight")),
                "lede": val("28.8px", "dimension", mm("hero-lede", "lineHeight")),
                "title": val("25.2px", "dimension", mm("review-card", "lineHeight")),
                "body": val("25.6px", "dimension", mm("ha-body", "lineHeight")),
                "label": val("23.8px", "dimension", mm("ha-tag", "lineHeight")),
                "tag": val("21px", "dimension", mm("plus-tag", "lineHeight")),
                "button": val("16px", "dimension", mm("nav-cta", "lineHeight")),
                "ui": val("15px", "dimension", mm("nav-link", "lineHeight")),
                "field": val("34px", "dimension", mm("help-search-input", "lineHeight")),
            },
            "letterSpacing": {
                "none": val("0px", "dimension", "computed letterSpacing 'normal' resolves to 0 on every measured text element", description="The site tracks everything at normal."),
            },
        },
        "typography": {
            "ticker": {"$type": "typography", "$value": {"fontFamily": "{font.family.display}", "fontSize": "{font.size.ticker}", "fontWeight": "{font.weight.bold}", "lineHeight": "{font.lineHeight.ticker}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the hero-ticker measurements"}},
            "page": {"$type": "typography", "$value": {"fontFamily": "{font.family.display}", "fontSize": "{font.size.page}", "fontWeight": "{font.weight.bold}", "lineHeight": "{font.lineHeight.page}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the help-h1 measurements"}},
            "heading-2": {"$type": "typography", "$value": {"fontFamily": "{font.family.display}", "fontSize": "{font.size.heading-2}", "fontWeight": "{font.weight.bold}", "lineHeight": "{font.lineHeight.heading-2}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the ha-h2 measurements"}},
            "title": {"$type": "typography", "$value": {"fontFamily": "{font.family.display}", "fontSize": "{font.size.title}", "fontWeight": "{font.weight.bold}", "lineHeight": "{font.lineHeight.title}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the review-card measurements"}},
            "lede": {"$type": "typography", "$value": {"fontFamily": "{font.family.ui}", "fontSize": "{font.size.title}", "fontWeight": "{font.weight.medium}", "lineHeight": "{font.lineHeight.lede}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the hero-lede measurements"}},
            "body": {"$type": "typography", "$value": {"fontFamily": "{font.family.ui}", "fontSize": "{font.size.body}", "fontWeight": "{font.weight.medium}", "lineHeight": "{font.lineHeight.body}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the ha-body measurements"}},
            "button": {"$type": "typography", "$value": {"fontFamily": "{font.family.button}", "fontSize": "{font.size.body}", "fontWeight": "{font.weight.demibold}", "lineHeight": "{font.lineHeight.button}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the nav-cta measurements"}},
            "ui": {"$type": "typography", "$value": {"fontFamily": "{font.family.ui}", "fontSize": "{font.size.ui}", "fontWeight": "{font.weight.medium}", "lineHeight": "{font.lineHeight.ui}", "letterSpacing": "{font.letterSpacing.none}"}, "$extensions": {"source": "composed from the nav-link measurements"}},
        },
        "radius": {
            "none": val("0px", "dimension", mm("help-accordion-header", "borderTopLeftRadius"), description="Text and prose blocks are square."),
            "row": val("12px", "dimension", mm("pricing-row", "borderTopLeftRadius"), description="Table rows and small tiles."),
            "card": val("18.8px", "dimension", mm("feature-card", "borderTopLeftRadius"), description="The feature-card corner."),
            "button": val("20px", "dimension", mm("nav-cta", "borderTopLeftRadius"), description="The 40px pills: nav/hero CTAs, Search, mailto and secondary pills."),
            "pill": val("40px", "dimension", mm("nl-email", "borderTopLeftRadius"), description="Full capsules: the newsletter email field and its submit."),
            "pill-lg": val("50px", "dimension", mm("press-asset", "borderTopLeftRadius"), description="The wider asset-download pill on the press hub."),
        },
        "space": {
            "12": val("12px", "dimension", mm("nav-cta", "paddingTop"), description="Pill vertical padding."),
            "18": val("18px", "dimension", mm("nav-cta", "paddingRight"), description="Pill horizontal padding."),
            "40": val("40px", "dimension", mm("feature-card", "paddingTop"), description="Feature-card padding."),
        },
        "duration": {
            "link": val("0.4s", "duration", mm("help-accordion-link", "transitionDuration"), description="The link colour transition."),
        },
        "easing": {
            "link": val("cubic-bezier(0.44, 0, 0.56, 1)", "cubicBezier", "the transition easing declared for links (raw/motion.json)"),
        },
    },
    "light": {
        "canvas": var("--token-e4937171-542b-42ad-9ea7-f2313c1b2cba", description="Page canvas — white in light; this declaration repaints to black under the dark media rule."),
        "ink": var("--token-2baf03db-a9e4-46b9-91e4-c826d6094725", description="#0d0d0d heading ink; repaints to #f2f2f2 in dark."),
        "body": var("--token-123b8990-3ac2-43a6-a119-ec6d8f6d9209", description=".2 body text; repaints to .8 in dark."),
        "muted": var("--token-4ba80d30-a0fa-42f8-abce-e713387f72a1", description=".4 secondary text (nav links, dates, table cells); repaints to .6 in dark."),
        "field-ink": var("--token-ef9d6278-1ce6-4164-a9b5-b638331cd823", description="#2f2f2f — the search-field text."),
        "surface": {
            "card": var("--token-9ccde7da-e2d4-4bd3-a9a1-9d6f4670d0d9", description="#f2f2f2-class card and field fill (feature cards, the newsletter email field, secondary pills); repaints to #1a1a1a in dark."),
            "ring": var("--token-1d8715d1-f6b8-4f4a-943d-9eab1e8817be", description=".902 ring/hairline (the newsletter field's inset 1px shadow); repaints to .2 in dark."),
            "chip": var("--token-a5f25400-a132-4251-9bf4-a594a40d8751", description=".9608 pale grey."),
        },
        "accent": var("--token-68fc3b44-076f-4e15-8b8d-177d1c92d70c", description="The brand orange: primary pills, accordion links, pricing checks."),
        "accent-hover": var("--token-14ae3875-63fa-4a13-8b34-f91aaf1883fe", description="The lighter orange every accent pill hovers to."),
        "on-accent": var("--token-99c84fb2-564c-4f3b-9a25-6d6ecb66be27", description="White text on the accent pills (stays white in dark)."),
        "accent-text": var("--token-4b2e9d50-bfc7-4d49-a687-ea9eb6858bcf", description="The accent as text: secondary-pill and accordion-link labels."),
        "hue": {
            "red": var("--token-a8b17470-5760-49c5-b2d4-98a30eb6a57e", description="Goal hue red — a hero-ticker word colour."),
            "yellow": var("--token-948e6ba4-02b7-4acb-9029-7dd449d2bda1", description="Goal hue gold — a goal-pill colour."),
            "blue": var("--token-302ab92d-698f-4e54-b7ad-3e69309ecb79", description="Goal hue blue — the 'Effortlessly Scan Food' card title."),
            "indigo": var("--token-b8167313-229c-41eb-a782-380cb605abe8", description="Goal hue indigo — the eye-off value glyph, a pricing check."),
            "teal": var("--token-b71f95ad-3b6f-4f7d-ae68-18994668e09e", description="Goal hue teal — the cloud value glyph."),
            "steel": var("--token-e0f008f7-b89b-417a-9fef-4bf7c8cb8cc6", description="Goal hue steel — the shield value glyph."),
        },
        "on-dark": {
            "ink": var("--token-99c84fb2-564c-4f3b-9a25-6d6ecb66be27", description="Footer text is white in both themes."),
        },
        "focus": {
            "ring": val(st("nav-cta", "focus-visible")["outlineColor"], "color", mm("nav-cta", "outlineColor", "focus-visible"), description="The 1px browser-auto focus ring."),
            "width": val(st("nav-cta", "focus-visible")["outlineWidth"], "dimension", mm("nav-cta", "outlineWidth", "focus-visible")),
            "offset": val(st("nav-cta", "focus-visible")["outlineOffset"], "dimension", mm("nav-cta", "outlineOffset", "focus-visible")),
        },
    },
    "dark": {
        "canvas": var("--token-e4937171-542b-42ad-9ea7-f2313c1b2cba", description="Page canvas — repaints to black under the dark media rule."),
        "ink": var("--token-2baf03db-a9e4-46b9-91e4-c826d6094725", description="Heading ink — repaints to #f2f2f2 in dark."),
        "body": var("--token-123b8990-3ac2-43a6-a119-ec6d8f6d9209", description="Body text — repaints to .8 in dark."),
        "muted": var("--token-4ba80d30-a0fa-42f8-abce-e713387f72a1", description="Secondary text — repaints to .6 in dark."),
        "field-ink": var("--token-ef9d6278-1ce6-4164-a9b5-b638331cd823", description="#2f2f2f — unchanged under the dark media rule."),
        "surface": {
            "card": var("--token-9ccde7da-e2d4-4bd3-a9a1-9d6f4670d0d9", description="Card/field fill — repaints to #1a1a1a in dark."),
            "ring": var("--token-1d8715d1-f6b8-4f4a-943d-9eab1e8817be", description="Ring/hairline — repaints to .2 in dark."),
            "chip": var("--token-a5f25400-a132-4251-9bf4-a594a40d8751", description=".9608 pale grey — unchanged in dark."),
        },
        "accent": var("--token-68fc3b44-076f-4e15-8b8d-177d1c92d70c", description="The brand orange — unchanged: the pills stay #ff5406-class in dark."),
        "accent-hover": var("--token-14ae3875-63fa-4a13-8b34-f91aaf1883fe", description="The accent-pill hover colour — unchanged in dark."),
        "on-accent": var("--token-99c84fb2-564c-4f3b-9a25-6d6ecb66be27", description="White text on the accent pills — unchanged."),
        "accent-text": var("--token-4b2e9d50-bfc7-4d49-a687-ea9eb6858bcf", description="The accent as text — unchanged."),
        "hue": {
            "red": var("--token-a8b17470-5760-49c5-b2d4-98a30eb6a57e", description="Goal hue red — unchanged in dark."),
            "yellow": var("--token-948e6ba4-02b7-4acb-9029-7dd449d2bda1", description="Goal hue gold — unchanged in dark."),
            "blue": var("--token-302ab92d-698f-4e54-b7ad-3e69309ecb79", description="Goal hue blue — unchanged in dark."),
            "indigo": var("--token-b8167313-229c-41eb-a782-380cb605abe8", description="Goal hue indigo — repaints slightly lighter in dark."),
            "teal": var("--token-b71f95ad-3b6f-4f7d-ae68-18994668e09e", description="Goal hue teal — repaints slightly lighter in dark."),
            "steel": var("--token-e0f008f7-b89b-417a-9fef-4bf7c8cb8cc6", description="Goal hue steel — unchanged in dark."),
        },
        "on-dark": {
            "ink": var("--token-99c84fb2-564c-4f3b-9a25-6d6ecb66be27", description="Footer text stays white."),
        },
        "focus": {
            "ring": val(st("nav-cta", "focus-visible")["outlineColor"], "color", mm("nav-cta", "outlineColor", "focus-visible"), description="Focus ring, read in light — a dark pass paints the browser-auto ring on black."),
            "width": val(st("nav-cta", "focus-visible")["outlineWidth"], "dimension", mm("nav-cta", "outlineWidth", "focus-visible")),
            "offset": val(st("nav-cta", "focus-visible")["outlineOffset"], "dimension", mm("nav-cta", "outlineOffset", "focus-visible")),
        },
    },
    "component": {
        "pill": {
            "height": val("40px", "dimension", mm("nav-cta", "rect height"), description="The standard 40px button pill."),
            "padding-x": val("18px", "dimension", mm("nav-cta", "paddingRight")),
            "padding-y": val("12px", "dimension", mm("nav-cta", "paddingTop")),
        },
        "field": {
            "height": val("42px", "dimension", mm("nl-email", "rect height"), description="The newsletter email field (294px wide)."),
            "search-height": val("34px", "dimension", mm("help-search-input", "rect height"), description="The help search modal's input."),
        },
        "card": {
            "feature-width": val("590px", "dimension", mm("feature-card", "rect width"), description="A feature card at 1440."),
            "feature-height": val("400px", "dimension", mm("feature-card", "rect height")),
            "review-width": val("279px", "dimension", mm("review-card", "rect width"), description="A review marquee card."),
            "review-height": val("260px", "dimension", mm("review-card", "rect height")),
        },
        "table": {
            "width": val("1000px", "dimension", mm("pricing-table", "rect width"), description="The Free vs Foodnoms+ comparison table."),
        },
        "nav": {
            "hamburger": val("40px", "dimension", mm("m-hamburger", "rect height"), description="The mobile menu button."),
        },
    },
}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) else 1


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
