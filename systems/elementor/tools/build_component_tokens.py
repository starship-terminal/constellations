#!/usr/bin/env python3
"""Build raw/component-tokens.json for the Elementor reference.

Reads raw/components-computed.json and emits the values that are not one CSS
variable: the semantic light/dark roles and component measures, each carrying
the measurement it came from ("source"). Deterministic.

Run: python3 tools/build_component_tokens.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]
META = J.get("_meta", {})


def st(k, state="default"):
    c = C.get(k) or {}
    v = (c.get("states") or {}).get(state)
    return v or {}


def style(k, state="default"):
    return st(k, state).get("style") or {}


def col(v):
    if not v:
        return None
    m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", str(v))
    if m:
        a = float(m.group(4))
        if a == 0:
            return "transparent"
        if a == 1:
            return "#%02x%02x%02x" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return f"rgba({m.group(1)}, {m.group(2)}, {m.group(3)}, {'%g' % a})"
    m = re.fullmatch(r"rgb\((\d+), (\d+), (\d+)\)", str(v))
    if m:
        return "#%02x%02x%02x" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return str(v)


def tok(value, ty, source, **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    t["$extensions"].update(ext)
    return t


def first_text(k, state="default"):
    return (st(k, state).get("textStyle") or {})


out = {"$meta": {"built": J["_meta"]["read"], "from": "raw/components-computed.json (computed styles read live on elementor.com)"}, "light": {}, "dark": {}, "component": {}}

page = META.get("page") or {}

L = out["light"]
L["page"] = tok("#ffffff", "color", "html/body compute to transparent and the canvas shows Blank-Canvas-White through; verified against the white ground in every screenshot and the #fff painted surfaces (header pill, plan cards, form fields)")
L["surface"] = tok(col(style("contact-card")["backgroundColor"]), "color", "computed backgroundColor on contact-card (the Key-contact-options tile), /contact")
L["surfaceRaised"] = tok(col(style("header")["backgroundColor"]), "color", "computed backgroundColor on the header pill bar, header.elementor-location-header")
L["text"] = tok(col(style("contact-h1")["color"]), "color", "computed color on the page headings/buttons (contact-h1, nav-cta, plan-cta) — Kernel-Black")
L["textStrong"] = tok(col(first_text("faq-answer")["color"] or style("nav-trigger")["color"]), "color", "computed color on FAQ answers, the nav trigger and mobile nav items — Grey-800 #212121")
L["textMuted"] = tok("#7a7a7a", "color", "declared --e-global-color-text on .elementor-kit-35 (the kit's text global); also the footer's small print")
L["iconMuted"] = tok(col(style("social-icon")["color"]), "color", "computed color on the footer social icons at rest")
L["border"] = tok(col(style("field-name")["borderTopColor"]), "color", "computed borderTopColor on the form fields — Grey-500 #d1d1d1")
L["borderStrong"] = tok(col(style("field-name", "focused")["borderTopColor"]), "color", "computed borderTopColor on a focused field and the outline plan-cta — Kernel-Black")
L["accent"] = tok(col(style("nav-cta")["backgroundColor"]), "color", "computed backgroundColor on the Get-started pill and Submit — Kernel-Black")
L["accentOn"] = tok(col(style("nav-cta")["color"]), "color", "computed color on the Get-started pill")
L["accentHover"] = tok(col(style("nav-cta", "hover")["backgroundColor"]), "color", "computed backgroundColor on hover of the Get-started pill, Submit and the plan CTA — Neon-Loop")
L["tintHover"] = tok(col(style("nav-trigger", "hover")["backgroundColor"]), "color", "computed hover background on the nav trigger and mega-menu links — Syntax-Glow")
L["focusRing"] = tok(col(style("nav-cta", "focus-visible")["outlineColor"]), "color", "computed outlineColor on keyboard focus — the browser focus ring the site leaves in place")
L["focusRingWidth"] = tok(style("nav-cta", "focus-visible")["outlineWidth"], "dimension", "computed outlineWidth on keyboard focus")
L["link"] = tok(col(style("nav-link")["color"]), "color", "computed color on the plain header link — the unvisited-link blue elementor.com leaves unset")
L["menuPanel"] = tok("#ffffff", "color", "the opened mega-menu panel's painted layer (nav-dropdown paint: #fff, radius 24px, ::before hairline #d1d1d1, shadow rgba(0,0,0,0.05) 0 0 15px 3px — the same shadow as the header pill)")
L["fieldSurface"] = tok(col(style("field-name")["backgroundColor"]), "color", "computed backgroundColor on the contact form inputs")
L["overlayScrim"] = tok("rgba(0, 0, 0, 0.4)", "color", "observed on the contact form popup: the page dims behind the open dialog (the modal layer's backdrop; the crop shows the dimmed page)", sampled=True)

D = out["dark"]
D["$description"] = "The .dark-mode island scope (photo/video hero, dark sections, the dsm-footer): `.dark-mode *` re-binds --Kernel-Black to #fff, --Blank-Canvas-White to #000 and --Grey-800 to --Grey-200, so the same named vars paint dark."
D["page"] = tok(col(style("footer")["backgroundColor"]), "color", "computed backgroundColor on .dsm-footer and the hero stage (section.dark-mode) — Kernel-Black")
D["surface"] = tok(col(style("card")["backgroundColor"]), "color", "computed backgroundColor on the dark stat card (the 22M+ tile)")
D["text"] = tok(col(style("hero-title")["color"]), "color", "computed color on the hero headline and dark-section headings — --Kernel-Black rebound to #fff")
D["textMuted"] = tok(col(style("hero-lede")["color"]), "color", "computed color on the hero lede — Grey-200")
D["accent"] = tok("#ffffff", "color", "declared .dark-mode scope: dsm-button-primary reads --Kernel-Black which re-binds to #fff (the white Get-started pill in the hero)")
D["accentOn"] = tok("#000000", "color", "declared .dark-mode scope: the pill's text reads --Blank-Canvas-White rebound to #000")
D["border"] = tok("#484848", "color", "Grey-700, the scale step for hairlines on dark ground (declared --Grey-700)")

CMP = out["component"]
CMP["header"] = {"radius": tok(style("header")["borderTopLeftRadius"], "dimension", "computed borderRadius on the header pill bar"),
                 "height": tok(style("header")["height"], "dimension", "computed height on the header pill bar"),
                 "shadow": tok(style("header")["boxShadow"], "shadow", "computed boxShadow on the header pill bar")}
CMP["buttonPrimary"] = {"radius": tok(style("nav-cta")["borderTopLeftRadius"], "dimension", "computed borderRadius on the Get-started pill / Submit"),
                        "height": tok(style("nav-cta")["height"], "dimension", "computed height on the header Get-started pill"),
                        "font": tok(style("nav-cta")["fontSize"] + " " + style("nav-cta")["fontWeight"], "other", "computed font on the Get-started pill (Roobert 18px/500)")}
CMP["buttonHero"] = {"radius": tok(style("hero-cta")["borderTopLeftRadius"], "dimension", "computed borderRadius on the hero Get-started pill"),
                     "height": tok(style("hero-cta")["height"], "dimension", "computed height on the hero Get-started pill"),
                     "font": tok(style("hero-cta")["fontSize"] + " " + style("hero-cta")["fontWeight"], "other", "computed font on the hero Get-started pill")}
def border(k, state="default"):
    """width + style + colour: a border token without the style word paints
    nothing where it is dropped into `border:` (the style defaults to none)."""
    s = style(k, state)
    return s["borderTopWidth"] + " " + s["borderTopStyle"] + " " + col(s["borderTopColor"])


CMP["planCta"] = {"border": tok(border("plan-cta"), "other", "computed border on the outline Buy-now button")}
CMP["field"] = {"radius": tok(style("field-name")["borderTopLeftRadius"], "dimension", "computed borderRadius on the contact form inputs"),
                "height": tok(style("field-name")["height"], "dimension", "computed height on the name input"),
                "border": tok(border("field-name"), "other", "computed border on the contact form inputs")}
CMP["card"] = {"radius": tok(style("card")["borderTopLeftRadius"], "dimension", "computed borderRadius on the dsm card tiles (stat tile, contact card, menu feature tile)")}
CMP["planCard"] = {"radius": tok(style("plan-card")["borderTopLeftRadius"], "dimension", "computed borderRadius on the pricing plan card")}
CMP["checkbox"] = {"size": tok(style("checkbox")["width"], "dimension", "computed size of the acceptance checkbox"),
                   "border": tok(border("checkbox"), "other", "computed border on the acceptance checkbox")}
CMP["type"] = {
    "display": tok(first_text("hero-title").get("fontSize") or style("hero-title")["fontSize"], "dimension", "computed fontSize on the hero h1 (Roobert 600)", weight=style("hero-title")["fontWeight"], lineHeight=style("hero-title")["lineHeight"]),
    "section": tok(first_text("h2-section").get("fontSize") or style("h2-section")["fontSize"], "dimension", "computed fontSize on the section h2", weight=style("h2-section")["fontWeight"]),
    "planPrice": tok(first_text("plan-price").get("fontSize") or "40px", "dimension", "computed fontSize on the plan price figure", weight=(first_text("plan-price").get("fontWeight") or "600")),
    "body": tok(first_text("faq-answer").get("fontSize") or "16px", "dimension", "computed fontSize on body copy (faq-answer)", lineHeight=first_text("faq-answer").get("lineHeight") or ""),
    "small": tok(first_text("m-nav-item").get("fontSize") or "14px", "dimension", "computed fontSize on small copy (mobile nav items)"),
}
CMP["motion"] = {
    "button": tok("0.2s ease", "other", "computed transition on the dsm primary buttons (background-color)"),
    "link": tok("0.3s ease-in-out", "other", "computed transition on header links (opacity)"),
    "panel": tok("0.5s ease", "other", "computed transition on the FAQ answer reveal (grid-template-rows) and 0.3s max-height on the mobile menu"),
}

(ROOT / "raw" / "component-tokens.json").write_text(json.dumps(out, indent=1) + "\n")
print("component-tokens.json:", sum(len(v) for v in out.values() if isinstance(v, dict)), "entries")
