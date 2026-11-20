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
names) or {"value": ..., "source": ...}. Every measured value is read here from
raw/components-computed.json by component, state and property (rd() and the
helpers on it), so a recapture moves the tokens with it and a missing or
failed reading stops the build instead of shipping a stale number. A role that
aliases a palette colour is checked against the reading it cites. The few
values no reading holds were entered by hand at capture time; they carry the
Reconstruction label (docs/EVIDENCE.md) in their source. Only a light theme was
ever painted or captured, so "dark" is empty.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = {n: v.get("value", v.get("raw")) for n, v in V.get("resolved", {}).get("light", {}).items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]


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
TYPED = ("Reconstruction: entered by hand at capture time; no reading in raw/components-computed.json holds it")


def typed(value, ty, why, **kw):
    """A value no reading holds (docs/EVIDENCE.md: Reconstruction). Kept, never presented as measured."""
    return val(value, ty, f"{TYPED} ({why})", **kw)


# ------------------------------------------------------------------ readings


def not_captured(v):
    """A state whose reading is not what its name says: skipped, or a focus-visible reading taken
    where keyboard focus never landed (the element at rest). It is never a token source."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


def style(key, state="default"):
    c = C.get(key)
    if c is None or c.get("missing"):
        raise KeyError(f"{key}: not in raw/components-computed.json")
    if c.get("recaptureMissed"):
        raise ValueError(f"{key}: flagged recaptureMissed; its states are an earlier run's")
    v = c["states"].get(state)
    if not v or "style" not in v:
        raise KeyError(f"{key} {state}: no reading in raw/components-computed.json")
    if not_captured(v):
        raise ValueError(f"{key} {state}: keyboard focus never landed (via {v.get('via')!r}); not a reading")
    return v["style"]


def rd(key, state, prop):
    s = style(key, state)
    if prop not in s:
        raise KeyError(f"{key} {state}: no {prop} reading")
    return s[prop]


def norm(v):
    """rgb()/rgba()/#hex -> #rrggbb, or rgba(r, g, b, a) when translucent (build_tokens.py's form)."""
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{6})", v)
    if m:
        return v
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError(f"not an rgb colour: {v!r}")
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))


def where(refs):
    return MS + "; ".join(f"{k} {s} {p}" for k, s, p in refs)


def agree(refs, conv=lambda x: x):
    """The value of the first reading; every other cited reading must hold the same value."""
    vals = [conv(rd(*r)) for r in refs]
    if any(x != vals[0] for x in vals[1:]):
        raise ValueError(f"cited readings disagree: {list(zip(refs, vals))}")
    return vals[0]


def mc(refs, **kw):
    """A palette colour read from one or more (component, state, property) readings."""
    return val(agree(refs, norm), "color", where(refs), **kw)


def md(refs, ty="dimension", **kw):
    """A length, weight or duration read verbatim (build_tokens.py converts s to ms and "300" to 300)."""
    v = agree(refs)
    if ty == "duration" and "," in v:
        raise ValueError(f"{refs[0]}: several durations {v!r}; cite one property")
    return val(v, ty, where(refs), **kw)


def palette(name):
    leaf = SPEC["core"]["color"][name]
    return norm(R[leaf["var"]] if "var" in leaf else leaf["value"])


def role(alias, key, state, prop, **kw):
    """A role that aliases {color.<name>}: the reading it cites must paint that colour."""
    got = norm(rd(key, state, prop))
    want = palette(alias[len("{color."):-1])
    if got != want:
        raise ValueError(f"{alias} is {want} but {key} {state} {prop} reads {got}")
    return val(alias, "color", where([(key, state, prop)]), **kw)


def alias_dim(alias, group, key, state, prop, **kw):
    """A component dimension that aliases a core scale step, checked against its reading."""
    got = rd(key, state, prop)
    leaf = SPEC["core"][group][alias[len("{" + group + "."):-1]]
    want = leaf.get("value") or R[leaf["var"]]
    if got != want:
        raise ValueError(f"{alias} is {want} but {key} {state} {prop} reads {got}")
    return val(alias, "dimension", where([(key, state, prop)]), **kw)


def split_top(s):
    """Split a computed list on its top-level commas (not the ones inside rgb(...))."""
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += (ch == "(") - (ch == ")")
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()] if cur.strip() else out


def shadow(key, state, **kw):
    """A computed box-shadow as DTCG layers. Chromium writes `colour x y blur spread [inset]`; the
    inset keyword is kept wherever it sits, and a layer the parser cannot read stops the build.
    Fully transparent zero layers (Tailwind's ring placeholders) are dropped."""
    raw = rd(key, state, "boxShadow")
    layers = []
    for part in split_top(raw):
        inset = bool(re.search(r"(^|\s)inset(\s|$)", part))
        rest = re.sub(r"(^|\s)inset(\s|$)", " ", part).strip()
        m = re.fullmatch(r"(rgba?\([^)]*\)|#[0-9a-f]{6})\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)", rest)
        if not m:
            raise ValueError(f"{key} {state}: unreadable shadow layer {part!r}")
        col, x, y, blur, spread = m.groups()
        col = norm(col)
        if col == "rgba(0, 0, 0, 0)" and x == y == blur == spread == "0px":
            continue
        layer = {"offsetX": x, "offsetY": y, "blur": blur, "spread": spread, "color": col}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    if not layers:
        raise ValueError(f"{key} {state}: no visible shadow layer in {raw!r}")
    return val(layers, "shadow", where([(key, state, "boxShadow")]), **kw)


def typo(key, state="default", **kw):
    """A typography composite read from one component's computed text style."""
    s = style(key, state)
    v = {"fontFamily": s["fontFamily"], "fontSize": s["fontSize"], "lineHeight": s["lineHeight"],
         "fontWeight": int(s["fontWeight"])}
    if s["letterSpacing"] != "normal":
        v["letterSpacing"] = s["letterSpacing"]
    if s["textTransform"] != "none":
        v["textTransform"] = s["textTransform"]
    if v["lineHeight"] == "normal":
        raise ValueError(f"{key} {state}: lineHeight is normal; cite a component with a set line height")
    return {"value": v, "type": "typography", "source": where([(key, state, "font")]), **kw}


def face(family):
    """The stylesheet a declared @font-face of this family came from (raw/css-vars.json fonts)."""
    for f in V.get("fonts", []):
        if f.get("font-family", "").strip('"') == family:
            return f["file"]
    raise KeyError(f"@font-face {family} not in raw/css-vars.json fonts")


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
BG, FG, BD, OL = "backgroundColor", "color", "borderTopColor", "outlineColor"
for name, desc, refs in [
    ("cobalt-hover", "Cobalt hover/pressed fill (rgb(64,0,204)) on primary buttons.", [("nav-cta", "hover", BG), ("buy-now", "hover", BG)]),
    ("cobalt-pressed", "Cobalt pressed fill (rgb(51,0,153)) on the ecom Buy-now.", [("buy-now", "pressed", BG)]),
    ("mist-soft", "Soft violet #ede5ff hover wash behind ecom outline buttons.", [("see-all", "hover", BG)]),
    ("auth-deep", "Dark violet #260559 fill of the account sign-in Next button.", [("auth-next", "default", BG)]),
    ("auth-deep-hover", "Sign-in Next hover (rgb(43,4,127)).", [("auth-next", "hover", BG)]),
    ("auth-deep-pressed", "Sign-in Next pressed (rgb(55,3,158)).", [("auth-next", "pressed", BG)]),
    ("inkwell-hover", "Ink-button pressed fill on the dark hero band (rgb(78,64,103)); hover keeps the inkwell fill.", [("hero-cta", "pressed", BG)]),
    ("assistant", "Assistant launcher fill (rgb(64,20,234)); the sierra.chat agent's violet.", [("assistant", "default", BG)]),
    ("white", "Page field, cards, inputs and text on the dark bands.", [("header", "default", BG), ("hero-field", "default", BG)]),
    ("black", "Generator canvas ink and the Black signature swatch.", [("sg-font", "default", FG)]),
]:
    c[name] = mc(refs, description=desc)

# Ink alphas (measured rgba() literals)
for name, desc, refs in [
    ("ink-90", "90% ink: ecom/account body ink.", [("auth-card", "default", FG), ("ec-billing-annual", "default", FG)]),
    ("ink-75", "75% ink: nav/meta text, pressed ink button.", [("nav-trigger", "default", FG), ("contact-sales", "pressed", BG)]),
    ("ink-70", "70% ink: the unselected half of the ecom billing toggle.", [("ec-billing-monthly", "default", FG)]),
    ("ink-50", "50% ink: ecom plan-card hairline.", [("plan-card", "default", BD)]),
    ("ink-15", "15% ink: field hairlines and ghost-button inset hover.", [("hero-field", "default", BD)]),
    ("ink-10", "10% ink wash: hover fill of the account page's language picker and signup link.", [("auth-lang", "hover", BG), ("auth-signup", "hover", BG)]),
    ("ink-05", "5% ink: ecom toggle track and subtle fills.", [("ec-billing-annual", "default", BG)]),
    ("violet-30", "30% deep-violet: disabled/quiet text on the generator (the Clear action).", [("sg-clear", "default", FG)]),
    ("violet-50", "50% deep-violet: quiet generator text (the Download action).", [("sg-download", "default", FG)]),
]:
    c[name] = mc(refs, description=desc)

# Roles only measured once
for name, desc, refs in [
    ("scrim", "90% ink scrim behind the video dialog.", [("video-dialog", "default", BG)]),
    ("hairline-ecom", "Ecom hairline #e5e7eb on toggles and feature rows.", [("feature-row", "default", BD), ("ec-billing-annual", "default", BD)]),
    ("hairline-auth", "Account card border rgba(25,24,35,.15).", [("auth-card", "default", BD)]),
    ("focus-auto", "Browser/auto focus #005fcc used by ecom toggles and generator controls.", [("ec-billing-annual", "focus-visible", OL), ("sg-tab-draw", "focus-visible", OL)]),
]:
    c[name] = mc(refs, description=desc)
# The assistant launcher's focus-visible reading was taken where keyboard focus never landed
# (via "focus failed"), so its green outline is not a measurement of a keyboard focus ring.
c["focus-green"] = val("#089b57", "color",
                       "read from the wrong state: components-computed.json assistant focus-visible outlineColor, "
                       "recorded where keyboard focus never landed (via focus failed); recapture needed",
                       description="Assistant widget's own focus ring #089b57 (sierra.chat sheet); not confirmed under a real keyboard focus.")
if norm(C["assistant"]["states"]["focus-visible"]["style"][OL]) != c["focus-green"]["value"]:
    raise ValueError("assistant focus-visible outlineColor no longer reads #089b57")

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
FF = "fontFamily"
f = SPEC["core"].setdefault("font", {}).setdefault("family", {})
f["sans"] = md([("header", "default", FF), ("nav-cta", "default", FF), ("hero-title", "default", FF)], "fontFamily",
               description="DS Indigo: headings, body, buttons on the marketing site; DSIndigo woff2 weights 300-600.")
f["sans-app"] = md([("auth-card", "default", FF), ("auth-next", "default", FF)], "fontFamily",
                   description='"DS Indigo": the account stacks lead with the spaced family name (the storefront appends a system fallback list).')
for name, family, fallback, desc in [
    ("mono", "Noto Sans Mono", "monospace", "Noto Sans Mono: declared monospace face (code snippets)."),
    ("icon", "7_Docusign", "sans-serif", "7_Docusign icon font (a 2_Docusign face is also declared)."),
    ("signature", "STFelicetteScript-Regular", "cursive", "One of six script/display faces the generator renders names in (STFelicetteScript, TDNStockinette, TDNRhubarbTart, STAmpersandist, STConstant-UltraItalic, STNebulith-Display)."),
]:
    name_css = f'"{family}"' if " " in family or family[0].isdigit() else family
    f[name] = val(f"{name_css}, {fallback}", "fontFamily",
                  f"@font-face {family} declared in raw/css-vars.json fonts ({face(family)}); the generic fallback was added by hand",
                  description=desc)

# ------------------------------------------------------------------- measures
RAD = "borderTopLeftRadius"
r = SPEC["core"].setdefault("radius", {})
for name, desc, refs in [
    ("2", "Tight 2px corner (the footer locale button).", [("locale-button", "default", RAD)]),
    ("4", "The workhorse corner: links, toggles, trial CTA, account card.", [("nav-link", "default", RAD), ("trial-cta", "default", RAD), ("auth-card", "default", RAD)]),
    ("6", "Generator tab pills.", [("sg-tab-draw", "default", RAD)]),
    ("8", "Buttons, fields and generator cards.", [("nav-cta", "default", RAD), ("hero-field", "default", RAD), ("sg-field", "default", RAD)]),
    ("10", None, []),
    ("16", "Ecom plan card corner.", [("plan-card", "default", RAD)]),
    ("pill", "Full pill: the floating Assistant launcher.", [("assistant", "default", RAD)]),
]:
    r[name] = var("--radius", "dimension", description="Declared --radius 0.625rem on the generator sheet.") if desc is None else md(refs, description=desc)

# The spacing scale is the set of padding and gap lengths the default states read; each step
# cites the first readings that hold it, and a step no reading holds stops the build.
SP = ("paddingTop", "paddingRight", "paddingBottom", "paddingLeft", "rowGap", "columnGap")
s = SPEC["core"].setdefault("spacing", {})
for n in (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 80, 96):
    hits = [(k, p) for k, comp in C.items() if not comp.get("missing")
            for p in SP if (comp["states"].get("default") or {}).get("style", {}).get(p) == f"{n}px"]
    if not hits:
        raise ValueError(f"spacing {n}px: no padding or gap reading holds it")
    eg = []
    for k, p in hits:
        if k not in [x for x, _ in eg]:
            eg.append((k, p))
    s[str(n)] = val(f"{n}px", "dimension",
                    MS + f"{n}px in {len(hits)} default-state padding/gap readings, e.g. " + "; ".join(f"{k} {p}" for k, p in eg[:2]),
                    description=f"{n}px step of the padding and gap lengths read across captured surfaces.")

sh = SPEC["core"].setdefault("shadow", {})
sh["hairline-inset"] = shadow("nav-buy", "hover", description="Ghost button hover: a 1px ink-15 inset ring, no lift.")
sh["field-focus"] = shadow("hero-field", "focused", description="Focused field: a 1px cobalt inset ring over the hairline.")
sh["ring-double"] = shadow("buy-now", "focus-visible", description="Ecom focus-visible: 2px white + 4px cobalt double ring.")
sh["mist-ring"] = shadow("hero-country", "focus-visible", description="Focus on the dark band: a 2px mist ring.")
sh["soft"] = shadow("sg-tab-draw", "default", description="Generator tab lift: 0 1px 3px rgba(0,0,0,.04).")
sh["launcher"] = shadow("assistant", "default", description="Floating launcher shadow (Tailwind shadow-lg).")

TD = "transitionDuration"
mo = SPEC["core"].setdefault("duration", {})
mo["fast"] = md([("nav-cta", "default", TD)], "duration", description="Buttons: 0.1s on background/border/shadow/color.")
mo["colour"] = md([("menu-link", "default", TD)], "duration", description="Link/toggle colour transitions 0.15s (ecom buttons 0.15s all).")
mo["field"] = md([("hero-field", "default", TD)], "duration", description="Field border transitions 0.2s.")
mo["panel"] = md([("sg-download", "default", TD)], "duration", description="Generator Download buttons: 0.3s all.")

# ----------------------------------------------------------------- typography
t = SPEC["core"]["font"].setdefault("size", {})
lh = SPEC["core"]["font"].setdefault("lineHeight", {})
ls = SPEC["core"]["font"].setdefault("tracking", {})
for name, key in [
    ("display", "hero-title"), ("h2", "h2-section"), ("h3", "e-title"), ("price", "plan-name"),
    ("card-title", "faq-button"), ("lede", "hero-lede"), ("body", "nav-dropdown"), ("meta", "nav-link"),
    ("label", "nav-search"), ("tiny", "auth-lang"),
]:
    t[name] = md([(key, "default", "fontSize")])
    lh[name] = md([(key, "default", "lineHeight")])
# No captured component reads 40px: the h4 step was entered by hand.
t["h4"] = typed("40px", "dimension", "the 40px card heading step")
lh["h4"] = typed("48px", "dimension", "the 40px card heading step")
for name, key in [("display", "hero-title"), ("h2", "h2-section"), ("h3", "e-title"),
                  ("card-title", "faq-button"), ("caps", "nav-cta")]:
    ls[name] = md([(key, "default", "letterSpacing")])
ls["h4"] = typed("-0.5px", "dimension", "the 40px card heading step")
ls["eyebrow"] = typed("0.8px", "dimension", "eyebrow label tracking")

FW = "fontWeight"
SPEC["core"]["font"]["weight"] = {
    "light": md([("hero-title", "default", FW)], "fontWeight", description="DSIndigo 300: display headings."),
    "regular": md([("header", "default", FW)], "fontWeight", description="Body copy."),
    "medium": md([("nav-link", "default", FW)], "fontWeight", description="Nav, labels, buttons."),
    "semibold": md([("nav-cta", "default", FW)], "fontWeight", description="Uppercase CTAs, footer headings."),
}

# ------------------------------------------------------------------ light set
L = SPEC["light"]
L["color"] = {
    "page": role("{color.white}", "header", "default", BG, description="The marketing page field is pure white; the generator paints ecru instead (color.ecru)."),
    "text": {
        "primary": role("{color.inkwell}", "header", "default", FG, description="Inkwell body/headline ink."),
        "secondary": role("{color.ink-75}", "nav-link", "default", FG, description="75% ink for nav, meta and secondary copy."),
        "tertiary": role("{color.violet-50}", "sg-download", "default", FG, description="50% deep-violet quiet text (generator)."),
        "on-dark": role("{color.white}", "hero-title", "default", FG, description="Text on the deep-violet bands and cobalt fills."),
        "on-violet-quiet": role("{color.violet-30}", "sg-clear", "default", FG, description="30% violet on the generator."),
    },
    "surface": {
        "card": role("{color.white}", "plan-card", "default", BG, description="Plan cards and fields paint white."),
        "ecru": val("{color.ecru}", "color", "css-var --ds-ecru", description="The warm signature-generator ground."),
        "band": val("{color.deep-violet}", "color", "css-var --ds-deep-violet; " + MS + "hero-section default backgroundImage (the radial gradient's outer stop)", description="The deep-violet hero/footer bands."),
        "wash": role("{color.ink-05}", "ec-billing-annual", "default", BG, description="5% ink wash: toggle tracks, subtle fills."),
        "violet": role("{color.mist-soft}", "see-all", "hover", BG, description="Soft-violet hover wash behind outline buttons."),
        "mist": role("{color.mist}", "sg-download", "default", BG, description="Mist secondary fill (download buttons, accents)."),
    },
    "action": {
        "primary-bg": role("{color.cobalt}", "nav-cta", "default", BG, description="Cobalt primary button fill."),
        "primary-bg-hover": role("{color.cobalt-hover}", "nav-cta", "hover", BG, description="#4000cc on hover and some pressed states."),
        "primary-bg-pressed": role("{color.cobalt-pressed}", "buy-now", "pressed", BG, description="#330099 ecom pressed."),
        "primary-text": role("{color.white}", "nav-cta", "default", FG),
        "ink-bg": role("{color.inkwell}", "contact-sales", "default", BG, description="Inkwell dark-button fill (hero CTA on the violet band, Contact sales)."),
        "ink-bg-hover": role("{color.ink-90}", "contact-sales", "hover", BG),
        "ink-bg-pressed": role("{color.ink-75}", "contact-sales", "pressed", BG),
        "ink-bg-onband-pressed": role("{color.inkwell-hover}", "hero-cta", "pressed", BG, description="Hero ink-button pressed #4e4067."),
        "outline-border": role("{color.cobalt}", "see-all", "default", BD, description="Cobalt 1px outline-button border and text."),
        "outline-bg-hover": role("{color.mist-soft}", "see-all", "hover", BG),
        "outline-text-pressed": role("{color.inkwell}", "see-all", "pressed", FG),
        "link": role("{color.cobalt}", "hero-link", "default", FG, description="Cobalt links; pressed goes inkwell."),
        "link-pressed": role("{color.inkwell}", "hero-link", "pressed", FG),
    },
    "border": {
        "default": role("{color.ink-15}", "hero-field", "default", BD, description="15% ink hairline on fields."),
        "strong": role("{color.ink-50}", "plan-card", "default", BD, description="50% ink plan-card border."),
        "ecom": role("{color.hairline-ecom}", "feature-row", "default", BD, description="#e5e7eb Tailwind hairline on the storefront."),
        "auth": role("{color.hairline-auth}", "auth-card", "default", BD, description="Account card border rgba(25,24,35,.15)."),
        "mist": role("{color.mist}", "sg-field", "default", BD, description="Mist borders on generator fields/tabs."),
        "focus": role("{color.cobalt}", "hero-field", "focused", BD, description="Cobalt border on focused fields."),
    },
    "focus": {
        "ring": role("{color.cobalt}", "nav-trigger", "focus-visible", OL, description="2px solid cobalt, 2px offset, on marketing controls."),
        "ring-on-band": val("{color.mist}", "color", where([("hero-country", "focus-visible", "boxShadow")]), description="2px mist ring on the violet band."),
        "ring-auth": role("{color.inkwell}", "auth-next", "focus-visible", OL, description="2px inkwell ring, 2px offset, on the account page."),
        "ring-auto": role("{color.focus-auto}", "ec-billing-annual", "focus-visible", OL, description="1px auto #005fcc ring on ecom/generator controls."),
        "ring-green": val("{color.focus-green}", "color", c["focus-green"]["source"], description="Assistant widget's own #089b57 ring (vendor); not confirmed under a real keyboard focus."),
    },
    "overlay": {
        "scrim": role("{color.scrim}", "video-dialog", "default", BG, description="Video dialog scrim rgba(19,0,50,.898)."),
    },
}
if norm(re.findall(r"rgba?\([^)]*\)", rd("hero-section", "default", "backgroundImage"))[-1]) != palette("deep-violet"):
    raise ValueError("hero-section's gradient no longer ends in --ds-deep-violet")
if sh["mist-ring"]["value"][0]["color"] != palette("mist"):
    raise ValueError("hero-country focus-visible ring is no longer --ds-mist")

# ---------------------------------------------------------- component tokens
PT, PR, PB, H, LS = "paddingTop", "paddingRight", "paddingBottom", "height", "letterSpacing"
CP = SPEC["component"]
CP["nav"] = {
    "utility-height": md([("utilitynav", "default", H)]),
    "header-height": md([("header", "default", H)], description="Sticky header; 77px at 390 wide."),
    "dropdown-gap": md([("nav-dropdown", "default", "columnGap")], description="Mega-menu column gap."),
    "item-tracking": md([("nav-link", "default", LS)], description="Nav/label letter spacing."),
}
CP["button"] = {
    "height": md([("nav-cta", "default", H)], description="Header pills are 45px; hero pill 61px paired with the field."),
    "radius": alias_dim("{radius.8}", "radius", "nav-cta", "default", RAD),
    "radius-small": alias_dim("{radius.4}", "radius", "trial-cta", "default", RAD, description="4px corners on the trial/account submit."),
    "padding-y": md([("nav-cta", "default", PT)], description="Header pill vertical padding; ecom buttons pad 8px."),
    "padding-x": md([("nav-cta", "default", PR)]),
    "tracking": md([("nav-cta", "default", LS)], description="Uppercase CTA tracking (+0.2px, weight 600)."),
}
CP["field"] = {
    "height": md([("hero-field", "default", H)], description="Floating-label fields are 61px tall (hero + trial)."),
    "radius": alias_dim("{radius.8}", "radius", "hero-field", "default", RAD),
    "border": role("{color.ink-15}", "hero-field", "default", BD),
    "border-focus": role("{color.cobalt}", "hero-field", "focused", BD),
    "padding-top": md([("hero-field", "default", PT)], description="Floating-label padding: the label sits in the 24px top."),
    "padding-x": md([("hero-field", "default", PR)]),
    "padding-bottom": md([("hero-field", "default", PB)]),
}
CP["card"] = {
    "radius": alias_dim("{radius.16}", "radius", "plan-card", "default", RAD, description="Ecom plan card 16px; generator cards 8px; account card 4px."),
    "radius-generator": alias_dim("{radius.8}", "radius", "sg-font", "default", RAD),
    "radius-auth": alias_dim("{radius.4}", "radius", "auth-card", "default", RAD),
    "border": role("{color.ink-50}", "plan-card", "default", BD),
    "padding-y-auth": md([("auth-card", "default", PT)], description="Account card vertical padding."),
}
CP["modal"] = {
    "scrim": role("{color.scrim}", "video-dialog", "default", BG),
}
CP["type"] = {
    "display": typo("hero-title", description="Hero display: 80/86.4 weight 300, -1.5px tracking."),
    "h2": typo("h2-section"),
    "h3": typo("e-title"),
    "card-title": typo("faq-button"),
    "lede": typo("hero-lede"),
    "body": typo("nav-dropdown"),
    "meta": typo("nav-link"),
    "caps": typo("nav-cta"),
}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("component-tokens.json written")
