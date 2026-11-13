#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

docusign.com is three surfaces signed out. The marketing site (Next.js +
Emotion) declares almost no custom properties of its own — its values come from
atomic css-* classes — so most leaves are *measured* from
raw/components-computed.json (tools/capture/public/measure.mjs). Two declared
layers do exist and are tokenised as {"var": ...} leaves resolved in the
probe's light pass (raw/css-vars.json, tools/capture/vars.mjs):

  signature generator   an inline sheet on /signature-generator declares the
                        --ds-* brand set (cobalt, inkwell, deep-violet, mist,
                        poppy, ecru) plus shadcn-style roles (--background,
                        --primary, --ring, --radius)
  ecom storefront       the /en-SG/ plans-and-pricing page declares
                        --dxp-primary #0069ec on body
  assistant agent       the embedded Docusign Assistant (sierra.chat) sheet
                        declares a full --color-accent*/--color-foreground*/
                        --color-background* ramp ("kraken" org theme); kept
                        under core.color.assistant.* with vendor provenance

A leaf is {"var": "--name"} (resolved by build_tokens.py in the pass "resolve"
names) or {"value": ..., "source": "measured ..."} for a computed value. Only a
light theme was ever painted or captured, so "dark" is empty.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = {n: v.get("value", v.get("raw")) for n, v in V.get("resolved", {}).get("light", {}).items()}
json.loads((RAW / "components-computed.json").read_text())  # sanity: file exists


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty, "resolve": "light"}
    d.update(kw)
    if name not in R:
        raise KeyError(f"{name} not resolved in raw/css-vars.json")
    return d


def val(value, ty, source, **kw):
    d = {"value": value, "type": ty, "source": source}
    d.update(kw)
    return d


MS = "measured components-computed.json: "


def st(key, state="default"):
    return MS + f"{key} {state}"


SPEC = {
    "core": {}, "light": {}, "dark": {}, "component": {},
    "_meta": "docusign.com public signed-out surfaces; Emotion atomic CSS plus the signature-generator --ds-* layer and the ecom --dxp-* var; most values are computed-style measurements",
}

c = SPEC["core"].setdefault("color", {})

# ------------------------------------------------------------- declared brand
for name, vn, desc in [
    ("cobalt", "--ds-cobalt", "Cobalt #4c00ff: the action colour — primary fills, links and the 2px focus ring."),
    ("inkwell", "--ds-inkwell", "Inkwell #130032: the body/headline ink and the dark button fill."),
    ("deep-violet", "--ds-deep-violet", "Deep violet #26065d: the painted hero/footer bands and muted ink."),
    ("mist", "--ds-mist", "Mist #cbc2ff: secondary fills, field borders on the generator, dark-band focus ring."),
    ("poppy", "--ds-poppy", "Poppy #ff5252: the Coral signature swatch and warm accent."),
    ("ecru", "--ds-ecru", "Ecru #f8f3f0: the warm field surface (signature-generator page ground)."),
]:
    c[name] = var(vn, description=desc)

# -------------------------------------------------------------- measured ramp
for name, v, desc, src in [
    ("cobalt-hover", "#4000cc", "Cobalt hover/pressed fill (rgb(64,0,204)) on primary buttons.", [st("nav-cta", "hover"), st("buy-now", "hover")]),
    ("cobalt-pressed", "#330099", "Cobalt pressed fill (rgb(51,0,153)) on the ecom Buy-now.", [st("buy-now", "pressed")]),
    ("mist-soft", "#ede5ff", "Soft violet #ede5ff hover wash behind ecom outline buttons.", [st("see-all", "hover")]),
    ("auth-deep", "#260559", "Dark violet #260559 fill of the account sign-in Next button.", [st("auth-next", "default")]),
    ("auth-deep-hover", "#2b047f", "Sign-in Next hover (rgb(43,4,127)).", [st("auth-next", "hover")]),
    ("auth-deep-pressed", "#37039e", "Sign-in Next pressed (rgb(55,3,158)).", [st("auth-next", "pressed")]),
    ("inkwell-hover", "#4e4067", "Ink-button hover on the dark hero band (rgb(78,64,103)).", [st("hero-cta", "pressed")]),
    ("assistant", "#4014ea", "Assistant launcher fill (rgb(64,20,234)); the sierra.chat agent's violet.", [st("assistant", "default")]),
    ("white", "#ffffff", "Page field, cards, inputs and text on the dark bands.", [st("header"), st("hero-field")]),
    ("black", "#000000", "Generator canvas ink and the Black signature swatch.", [st("sg-font")]),
]:
    c[name] = val(v, "color", "; ".join(src), description=desc)

# Ink alphas (measured rgba() literals)
for name, v, desc, src in [
    ("ink-90", "rgba(19, 0, 50, 0.9)", "90% ink: ecom/account body ink.", [st("auth-card"), st("ec-billing-annual")]),
    ("ink-75", "rgba(19, 0, 50, 0.75)", "75% ink: nav/meta text, pressed ink button.", [st("nav-trigger"), st("contact-sales", "pressed")]),
    ("ink-70", "rgba(19, 0, 50, 0.7)", "70% ink.", [st("filter-button", "hover")]),
    ("ink-50", "rgba(19, 0, 50, 0.5)", "50% ink: ecom plan-card hairline.", [st("plan-card")]),
    ("ink-15", "rgba(19, 0, 50, 0.15)", "15% ink: field hairlines and ghost-button inset hover.", [st("hero-field"), st("nav-buy", "hover")]),
    ("ink-10", "rgba(19, 0, 50, 0.1)", "10% ink wash.", [st("hero-checkbox", "hover")]),
    ("ink-05", "rgba(19, 0, 50, 0.05)", "5% ink: ecom toggle track and subtle fills.", [st("ec-billing-annual")]),
    ("violet-30", "rgba(38, 6, 93, 0.3)", "30% deep-violet: disabled/quiet text on the generator.", [st("sg-download")]),
    ("violet-50", "rgba(38, 6, 93, 0.5)", "50% deep-violet: quiet generator text.", [st("sg-font")]),
]:
    c[name] = val(v, "color", "; ".join(src), description=desc)

# Roles only measured once
for name, v, desc, src in [
    ("scrim", "rgba(19, 0, 50, 0.898)", "90% ink scrim behind the video dialog.", [st("video-dialog")]),
    ("hairline-ecom", "#e5e7eb", "Ecom hairline #e5e7eb on toggles and feature rows.", [st("feature-row"), st("ec-billing-annual")]),
    ("hairline-auth", "rgba(25, 24, 35, 0.15)", "Account card border rgba(25,24,35,.15).", [st("auth-card")]),
    ("focus-green", "#089b57", "Assistant widget's own focus ring #089b57 (sierra.chat sheet).", [st("assistant", "focus-visible")]),
    ("focus-auto", "#005fcc", "Browser/auto focus #005fcc used by ecom toggles and generator controls.", [st("ec-billing-annual", "focus-visible"), st("sg-tab-draw", "focus-visible")]),
    ("error", "#ff0000", "Pure red seen once (generator canvas stroke default); distrust.", [st("sg-canvas")]),
]:
    c[name] = val(v, "color", "; ".join(src), description=desc)

# Ecom declared var
c["dxp-primary"] = var("--dxp-primary",
                       description="DXP #0069ec: declared on the ecom storefront body (its links/actions blue).")

# Assistant (sierra.chat 'kraken' theme) declared accent ramp — the only
# 10-step ramp in evidence; kept under its own group with vendor provenance.
asrc = "css-var declared in the embedded Docusign Assistant (sierra.chat) stylesheet; vendor surface, DocuSign org theme 'kraken'"
acc = c.setdefault("assistant-ramp", {})
for step in (50, 100, 200, 300, 400, 500, 600, 700, 800, 900):
    nm = f"--color-accentBlue-{step}"
    if nm in R:
        acc[f"blue-{step}"] = var(nm, description="Assistant accentBlue ramp (sierra.chat kraken theme).",
                                  source=asrc)
for name, vn in [("ink-1", "--color-foreground-1"), ("ink-2", "--color-foreground-2"),
                 ("surface-1", "--color-background-1"), ("surface-2", "--color-background-2")]:
    if vn in R:
        acc[name] = var(vn, description="Assistant foreground/background role (sierra.chat kraken theme).",
                        source=asrc)

# --------------------------------------------------------------- type + fonts
f = SPEC["core"].setdefault("font", {}).setdefault("family", {})
f["sans"] = val("DSIndigo, Helvetica, Arial, sans-serif", "fontFamily",
                "measured components-computed.json: every marketing component",
                description="DS Indigo: headings, body, buttons on the marketing site; DSIndigo woff2 weights 300-600.")
f["sans-app"] = val('"DS Indigo", DSIndigo, Helvetica, Arial, sans-serif', "fontFamily",
                    "measured components-computed.json: ecom plan-card / auth-card",
                    description='"DS Indigo": the storefront and account stacks lead with the spaced family name.')
f["mono"] = val('"Noto Sans Mono", monospace', "fontFamily",
                "@font-face declared in the marketing site sheets",
                description="Noto Sans Mono: declared monospace face (code snippets).")
f["icon"] = val('"7_Docusign", sans-serif', "fontFamily",
                "@font-face declared in the marketing site sheets",
                description="7_Docusign icon font (a 2_Docusign face is also declared).")
f["signature"] = val("STFelicetteScript-Regular, cursive", "fontFamily",
                     "@font-face declared in the signature-generator sheet",
                     description="One of six script/display faces the generator renders names in (STFelicetteScript, TDNStockinette, TDNRhubarbTart, STAmpersandist, STConstant-UltraItalic, STNebulith-Display).")

# ------------------------------------------------------------------- measures
r = SPEC["core"].setdefault("radius", {})
for name, v, desc, src in [
    ("2", "2px", "Tight 2px corner.", [MS + "small controls"]),
    ("4", "4px", "The workhorse corner: links, toggles, trial CTA, account card.", [st("nav-link"), st("trial-cta"), st("auth-card")]),
    ("6", "6px", "Generator tab pills.", [st("sg-tab-draw")]),
    ("8", "8px", "Buttons, fields and generator cards.", [st("nav-cta"), st("hero-field"), st("sg-field")]),
    ("10", None, "Declared --radius 0.625rem on the generator sheet.", []),
    ("16", "16px", "Ecom plan card corner.", [st("plan-card")]),
    ("pill", "9999px", "Full pill: the floating Assistant launcher.", [st("assistant")]),
]:
    r[name] = var("--radius", "dimension", description=desc) if v is None else val(v, "dimension", "; ".join(src), description=desc)

s = SPEC["core"].setdefault("spacing", {})
for n in (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 80, 96):
    s[str(n)] = val(f"{n}px", "dimension", f"measured components-computed.json: paddings/gaps across captured components (e.g. {n}px grid step)",
                    description=f"{n}px grid step observed across captured surfaces.")

sh = SPEC["core"].setdefault("shadow", {})
sh["hairline-inset"] = val([{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "rgba(19, 0, 50, 0.15)", "inset": True}], "shadow",
                           st("nav-buy", "hover"), description="Ghost button hover: a 1px ink-15 inset ring, no lift.")
sh["field-focus"] = val([{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "#4c00ff", "inset": True}], "shadow",
                        st("hero-field", "focused"), description="Focused field: a 1px cobalt inset ring over the hairline.")
sh["ring-double"] = val([{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "2px", "color": "#ffffff"},
                         {"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "4px", "color": "#4c00ff"}], "shadow",
                        st("buy-now", "focus-visible"), description="Ecom focus-visible: 2px white + 4px cobalt double ring.")
sh["mist-ring"] = val([{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "2px", "color": "#cbc2ff"}], "shadow",
                      st("hero-country", "focus-visible"), description="Focus on the dark band: a 2px mist ring.")
sh["soft"] = val([{"offsetX": "0px", "offsetY": "1px", "blur": "3px", "spread": "0px", "color": "rgba(0, 0, 0, 0.04)"}], "shadow",
                 st("sg-tab-draw"), description="Generator tab lift: 0 1px 3px rgba(0,0,0,.04).")
sh["launcher"] = val([{"offsetX": "0px", "offsetY": "10px", "blur": "15px", "spread": "-3px", "color": "rgba(0, 0, 0, 0.1)"},
                      {"offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-4px", "color": "rgba(0, 0, 0, 0.1)"}], "shadow",
                     st("assistant"), description="Floating launcher shadow (Tailwind shadow-lg).")

mo = SPEC["core"].setdefault("duration", {})
mo["fast"] = val("100ms", "duration", st("nav-cta"), description="Buttons: 0.1s on background/border/shadow/color.")
mo["colour"] = val("150ms", "duration", st("menu-link"), description="Link/toggle colour transitions 0.15s (ecom buttons 0.15s all).")
mo["field"] = val("200ms", "duration", st("hero-field"), description="Field border transitions 0.2s.")
mo["panel"] = val("300ms", "duration", st("sg-font"), description="Generator controls 0.3s all.")

# ----------------------------------------------------------------- typography
t = SPEC["core"]["font"].setdefault("size", {})
lh = SPEC["core"]["font"].setdefault("lineHeight", {})
ls = SPEC["core"]["font"].setdefault("tracking", {})
for name, px, line, src in [
    ("display", "80px", "86.4px", st("hero-title")),
    ("h2", "58px", "62.64px", st("h2-section")),
    ("h3", "48px", "51.84px", st("e-title")),
    ("h4", "40px", "48px", st("trial-card")),
    ("price", "30px", "37.2px", st("plan-card")),
    ("card-title", "24px", "29.76px", st("faq-button")),
    ("lede", "18px", "27px", st("hero-lede")),
    ("body", "16px", "24px", st("header")),
    ("meta", "14px", "21px", st("nav-link")),
    ("label", "12px", "18px", st("utilitynav")),
    ("tiny", "10px", "12px", MS + "eyebrow labels"),
]:
    t[name] = val(px, "dimension", src)
    lh[name] = val(line, "dimension", src)
for name, v, src in [
    ("display", "-1.5px", st("hero-title")),
    ("h2", "-1.25px", st("h2-section")),
    ("h3", "-1px", st("e-title")),
    ("h4", "-0.5px", st("trial-card")),
    ("card-title", "-0.25px", st("faq-button")),
    ("caps", "0.2px", st("nav-cta")),
    ("eyebrow", "0.8px", st("footer")),
]:
    ls[name] = val(v, "dimension", src)

SPEC["core"]["font"]["weight"] = {
    "light": val(300, "fontWeight", st("hero-title"), description="DSIndigo 300: display headings."),
    "regular": val(400, "fontWeight", st("header"), description="Body copy."),
    "medium": val(500, "fontWeight", st("nav-link"), description="Nav, labels, buttons."),
    "semibold": val(600, "fontWeight", st("nav-cta"), description="Uppercase CTAs, footer headings."),
}

# ------------------------------------------------------------------ light set
L = SPEC["light"]
L["color"] = {
    "page": val("{color.white}", "color", st("header"), description="The marketing page field is pure white; the generator paints ecru instead (color.ecru)."),
    "text": {
        "primary": val("{color.inkwell}", "color", st("header"), description="Inkwell body/headline ink."),
        "secondary": val("{color.ink-75}", "color", st("nav-link"), description="75% ink for nav, meta and secondary copy."),
        "tertiary": val("{color.violet-50}", "color", st("sg-font"), description="50% deep-violet quiet text (generator)."),
        "on-dark": val("{color.white}", "color", st("hero-title"), description="Text on the deep-violet bands and cobalt fills."),
        "on-violet-quiet": val("{color.violet-30}", "color", st("sg-download"), description="30% violet on the generator."),
    },
    "surface": {
        "card": val("{color.white}", "color", st("plan-card"), description="Plan cards and fields paint white."),
        "ecru": val("{color.ecru}", "color", "css-var --ds-ecru; measured signgen page", description="The warm signature-generator ground."),
        "band": val("{color.deep-violet}", "color", "css-var --ds-deep-violet; measured hero-section", description="The deep-violet hero/footer bands."),
        "wash": val("{color.ink-05}", "color", st("ec-billing-annual"), description="5% ink wash: toggle tracks, subtle fills."),
        "violet": val("{color.mist-soft}", "color", st("see-all", "hover"), description="Soft-violet hover wash behind outline buttons."),
        "mist": val("{color.mist}", "color", "css-var --ds-mist; measured sg-download bg", description="Mist secondary fill (download buttons, accents)."),
    },
    "action": {
        "primary-bg": val("{color.cobalt}", "color", st("nav-cta"), description="Cobalt primary button fill."),
        "primary-bg-hover": val("{color.cobalt-hover}", "color", st("nav-cta", "hover"), description="#4000cc on hover and some pressed states."),
        "primary-bg-pressed": val("{color.cobalt-pressed}", "color", st("buy-now", "pressed"), description="#330099 ecom pressed."),
        "primary-text": val("{color.white}", "color", st("nav-cta")),
        "ink-bg": val("{color.inkwell}", "color", st("contact-sales"), description="Inkwell dark-button fill (hero CTA on the violet band, Contact sales)."),
        "ink-bg-hover": val("{color.ink-90}", "color", st("contact-sales", "hover")),
        "ink-bg-pressed": val("{color.ink-75}", "color", st("contact-sales", "pressed")),
        "ink-bg-onband-pressed": val("{color.inkwell-hover}", "color", st("hero-cta", "pressed"), description="Hero ink-button hover #4e4067."),
        "outline-border": val("{color.cobalt}", "color", st("see-all"), description="Cobalt 1px outline-button border and text."),
        "outline-bg-hover": val("{color.mist-soft}", "color", st("see-all", "hover")),
        "outline-text-pressed": val("{color.inkwell}", "color", st("see-all", "pressed")),
        "link": val("{color.cobalt}", "color", st("hero-link"), description="Cobalt links; pressed goes inkwell."),
        "link-pressed": val("{color.inkwell}", "color", st("hero-link", "pressed")),
    },
    "border": {
        "default": val("{color.ink-15}", "color", st("hero-field"), description="15% ink hairline on fields."),
        "strong": val("{color.ink-50}", "color", st("plan-card"), description="50% ink plan-card border."),
        "ecom": val("{color.hairline-ecom}", "color", st("feature-row"), description="#e5e7eb Tailwind hairline on the storefront."),
        "auth": val("{color.hairline-auth}", "color", st("auth-card"), description="Account card border rgba(25,24,35,.15)."),
        "mist": val("{color.mist}", "color", st("sg-field"), description="Mist borders on generator fields/tabs."),
        "focus": val("{color.cobalt}", "color", st("hero-field", "focused"), description="Cobalt border on focused fields."),
    },
    "focus": {
        "ring": val("{color.cobalt}", "color", st("nav-trigger", "focus-visible"), description="2px solid cobalt, 2px offset, on marketing controls."),
        "ring-on-band": val("{color.mist}", "color", st("hero-country", "focus-visible"), description="2px mist ring on the violet band."),
        "ring-auth": val("{color.inkwell}", "color", st("auth-next", "focus-visible"), description="2px inkwell ring, 2px offset, on the account page."),
        "ring-auto": val("{color.focus-auto}", "color", st("ec-billing-annual", "focus-visible"), description="1px auto #005fcc ring on ecom/generator controls."),
        "ring-green": val("{color.focus-green}", "color", st("assistant", "focus-visible"), description="Assistant widget's own #089b57 ring (vendor)."),
    },
    "overlay": {
        "scrim": val("{color.scrim}", "color", st("video-dialog"), description="Video dialog scrim rgba(19,0,50,.898)."),
    },
}

# ---------------------------------------------------------- component tokens
CP = SPEC["component"]
CP["nav"] = {
    "utility-height": val("30px", "dimension", st("utilitynav")),
    "header-height": val("69px", "dimension", st("header"), description="Sticky header; 77px at 390 wide."),
    "dropdown-gap": val("64px", "dimension", st("nav-dropdown"), description="Mega-menu column gap."),
    "item-tracking": val("0.2px", "dimension", st("nav-link"), description="Nav/label letter spacing."),
}
CP["button"] = {
    "height": val("45px", "dimension", st("nav-cta"), description="Header pills are 45px; hero pill 61px paired with the field."),
    "radius": val("{radius.8}", "dimension", st("nav-cta")),
    "radius-small": val("{radius.4}", "dimension", st("trial-cta"), description="4px corners on the trial/account submit."),
    "padding-y": val("12px", "dimension", st("nav-cta"), description="Header pill vertical padding; ecom buttons pad 8px."),
    "padding-x": val("16px", "dimension", st("nav-cta")),
    "tracking": val("0.2px", "dimension", st("nav-cta"), description="Uppercase CTA tracking (+0.2px, weight 600)."),
}
CP["field"] = {
    "height": val("61px", "dimension", st("hero-field"), description="Floating-label fields are 61px tall (hero + trial)."),
    "radius": val("{radius.8}", "dimension", st("hero-field")),
    "border": val("{color.ink-15}", "color", st("hero-field")),
    "border-focus": val("{color.cobalt}", "color", st("hero-field", "focused")),
    "padding-top": val("24px", "dimension", st("hero-field"), description="Floating-label padding: the label sits in the 24px top."),
    "padding-x": val("16px", "dimension", st("hero-field")),
    "padding-bottom": val("8px", "dimension", st("hero-field")),
}
CP["card"] = {
    "radius": val("{radius.16}", "dimension", st("plan-card"), description="Ecom plan card 16px; generator cards 8px; account card 4px."),
    "radius-generator": val("{radius.8}", "dimension", st("sg-font")),
    "radius-auth": val("{radius.4}", "dimension", st("auth-card")),
    "border": val("{color.ink-50}", "color", st("plan-card")),
    "padding-y-auth": val("64px", "dimension", st("auth-card"), description="Account card vertical padding."),
}
CP["modal"] = {
    "scrim": val("{color.scrim}", "color", st("video-dialog")),
}
CP["type"] = {
    "display": {"value": {"fontFamily": "DSIndigo", "fontSize": "80px", "lineHeight": "86.4px", "fontWeight": 300, "letterSpacing": "-1.5px"}, "type": "typography", "source": st("hero-title"), "description": "Hero display: 80/86.4 weight 300, -1.5px tracking."},
    "h2": {"value": {"fontFamily": "DSIndigo", "fontSize": "58px", "lineHeight": "62.64px", "fontWeight": 300, "letterSpacing": "-1.25px"}, "type": "typography", "source": st("h2-section")},
    "h3": {"value": {"fontFamily": "DSIndigo", "fontSize": "48px", "lineHeight": "51.84px", "fontWeight": 300, "letterSpacing": "-1px"}, "type": "typography", "source": st("e-title")},
    "card-title": {"value": {"fontFamily": "DSIndigo", "fontSize": "24px", "lineHeight": "29.76px", "fontWeight": 500, "letterSpacing": "-0.25px"}, "type": "typography", "source": st("faq-button")},
    "lede": {"value": {"fontFamily": "DSIndigo", "fontSize": "18px", "lineHeight": "27px", "fontWeight": 400}, "type": "typography", "source": st("hero-lede")},
    "body": {"value": {"fontFamily": "DSIndigo", "fontSize": "16px", "lineHeight": "24px", "fontWeight": 400}, "type": "typography", "source": st("header")},
    "meta": {"value": {"fontFamily": "DSIndigo", "fontSize": "14px", "lineHeight": "21px", "fontWeight": 500, "letterSpacing": "0.2px"}, "type": "typography", "source": st("nav-link")},
    "caps": {"value": {"fontFamily": "DSIndigo", "fontSize": "14px", "lineHeight": "21px", "fontWeight": 600, "letterSpacing": "0.2px", "textTransform": "uppercase"}, "type": "typography", "source": st("nav-cta")},
}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("component-tokens.json written")
