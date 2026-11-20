"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

intercom.com's marketing site is a Next.js + Tailwind v4 build. Its design
layer is declared on :root inside @layer theme (raw/css-vars.json's `theme`
bin): the warm neutral ramp (cream/chalk/canvas/linen/clay around an
off-white/off-black pair), the brand blues (brand #000ce1, the blueprint ramp
peaking at helpdesk #0007cb), the product accents (fin #ff5600, sales #055895,
ecom, operator, voice), a responsive --text-{style}-{breakpoint} type scale, a
--radius-*/--blur-*/--container-*/--z-index-* geometry and a full --ease-*
scale. Component tokens (--button-*) sit on :root unlayered. Named scopes
carry their own sets, resolved on matching probes: .theme-light (the nav's
semantic colours), .brand-i2y4 (the i2y4 campaign's palette and the
Saans/Serrif/SaansMono stacks), .intercom-legacy (the older MediumLL-era
palette) and [data-media-player].

The core below is that declared layer with var-name provenance; the light set
is the semantic role layer read off the painted chrome in
raw/components-computed.json (page ground, nav, buttons, the billing toggle,
the form fields, the promo badge). There is one theme: body.theme-light and
no dark control anywhere (themeChecks in raw/css-vars.json), so tokens.json
ships no dark set.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
RL = V["resolved"].get("light") or {}
SC = V["resolved"].get("scopes") or {}
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
RS = {scope: {n: v.get("value", v.get("raw")) for n, v in (SC.get(scope) or {}).items()} for scope in ("brand", "legacy", "media")}


def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` or
    `placeholder.prop`: resolve the dotted path inside the measured state.
    `.firstColor`/`.lastColor` pull a colour literal out of a string."""
    d = C[comp]["states"][state]
    for suffix, pick in ((".firstColor", 0), (".lastColor", -1)):
        if prop.endswith(suffix):
            v = stprop(comp, state, prop[: -len(suffix)])
            cols = re.findall(r"rgba?\([^)]*\)|okl(?:ab|ch)\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
            return cols[pick] if cols else ""
    parts = prop.split(".")
    cur = d
    for p in parts:
        if isinstance(cur, list):
            cur = cur[int(p)]
        elif isinstance(cur, dict):
            cur = cur.get(p)
        else:
            return None
    return cur


SPEC = {"_about": (
        "The token tree build_tokens.py turns into tokens.json. "
        "intercom.com declares its design layer on :root in @layer theme plus "
        "unlayered component vars, scoped sets on .theme-light, .brand-i2y4, "
        ".intercom-legacy and [data-media-player] (raw/css-vars.json); the "
        "semantic roles are read off the painted chrome in "
        "raw/components-computed.json. One theme (light)."),
        "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    return node, parts[-1]


def var_(ty, name, scope=None, **kw):
    d = {"type": ty, "var": name}
    if scope:
        d["scope"] = scope
    d.update(kw)
    return d


def val_(ty, value, source, **kw):
    return {"type": ty, "value": value, "source": source, **kw}


def put(root, path, leaf):
    node, last = descend(root, path.split("."))
    node[last] = leaf


def decl_where(name):
    """Which selector/bin declared a name, for the provenance string."""
    for bin_ in ("theme", "nav", "brand", "legacy", "media", "component", "utility"):
        for r in V.get(bin_, []):
            if name in (r.get("properties") or {}):
                return f"{r.get('selector','?')} [{bin_}]"
    return ":root"


# --------------------------------------------------------------------- core
# Colour ramps, grouped by family. `var` names resolve against the matching
# probe's declarations in build_tokens.py.
NEUTRAL = [
    ("white", "--color-white"), ("offWhite", "--color-off-white"), ("cream", "--color-cream"),
    ("chalk", "--color-chalk"), ("canvas", "--color-canvas"), ("linen", "--color-linen"),
    ("clay", "--color-clay"), ("gray-50", "--color-gray-50"), ("gray-100", "--color-gray-100"),
    ("gray-200", "--color-gray-200"), ("gray-500", "--color-gray-500"), ("gray-600", "--color-gray-600"),
    ("gray-700", "--color-gray-700"), ("gray-800", "--color-gray-800"),
    ("offBlack", "--color-off-black"), ("black", "--color-black"), ("navy", "--color-navy"),
]
BLUE = [
    ("pale", "--color-blueprint-pale-blue", "brand"), ("light", "--color-blueprint-light-blue", "brand"),
    ("soft", "--color-blueprint-soft-blue", "brand"), ("600", "--color-blue-600", None),
    ("rich", "--color-blueprint-rich-blue", "brand"), ("helpdesk", "--color-helpdesk", "brand"),
    ("core", "--color-blueprint-core-blue", "brand"), ("bright", "--color-blueprint-bright-blue", "brand"),
    ("brand", "--color-blue", None), ("800", "--color-blue-800", None),
    ("deep", "--color-blueprint-deep-blue", "brand"), ("dark", "--color-blueprint-dark-blue", "brand"),
    ("black", "--color-blueprint-black-blue", "brand"),
]
ACCENT = [
    ("fin", "--color-fin", "brand"), ("sales", "--color-sales", "brand"),
    ("salesAccent", "--color-sales-accent", "brand"),
    ("ecom", "--color-ecom", "brand"), ("ecomAccent", "--color-ecom-accent", "brand"),
    ("operator", "--color-operator", "brand"),
    ("voice", "--color-voice-accent", "brand"), ("voiceGreen", "--color-voice-accent-green", None),
]
SUPPORT = [
    ("error", "--color-error", "brand"), ("red-500", "--color-red-500", None),
    ("red-600", "--color-red-600", None), ("red-700", "--color-red-700", None),
    ("green", "--color-green", None), ("green-400", "--color-green-400", None),
    ("amber-100", "--color-amber-100", None), ("amber-400", "--color-amber-400", None),
    ("sky-100", "--color-sky-100", None), ("violet-100", "--color-violet-100", None),
    ("rose-100", "--color-rose-100", None), ("emerald-100", "--color-emerald-100", None),
]
LEGACY = [
    ("black", "--color-black"), ("dark", "--color-dark"), ("navy", "--color-navy"),
    ("cream-light", "--color-cream-light"), ("blue", "--color-blue"), ("blue-light", "--color-blue-light"),
    ("blue-lightest", "--color-blue-lightest"), ("green", "--color-green"), ("green-light", "--color-green-light"),
    ("green-lightest", "--color-green-lightest"), ("orange", "--color-orange"), ("orange-light", "--color-orange-light"),
    ("orange-lightest", "--color-orange-lightest"), ("pink", "--color-pink"),
    ("pink-light", "--color-pink-light"), ("pink-lightest", "--color-pink-lightest"),
    ("teal", "--color-teal"), ("teal-light", "--color-teal-light"), ("teal-lightest", "--color-teal-lightest"),
    ("yellow", "--color-yellow"), ("yellow-light", "--color-yellow-light"), ("yellow-lightest", "--color-yellow-lightest"),
    ("success", "--color-success"), ("success-dark", "--color-success-dark"), ("success-light", "--color-success-light"),
    ("warning", "--color-warning"), ("warning-dark", "--color-warning-dark"), ("warning-light", "--color-warning-light"),
    ("error", "--color-error"), ("error-dark", "--color-error-dark"), ("error-light", "--color-error-light"),
    ("nav-dark", "--color-nav-dark"), ("nav-light", "--color-nav-light"),
    ("nav-light-secondary", "--color-nav-light-secondary"), ("nav-tray-light", "--color-nav-tray-light"),
    ("border-nav-dark", "--color-border-nav-dark"), ("border-nav-light", "--color-border-nav-light"),
    ("focus-outline", "--color-focus-outline"),
]
for key, name in NEUTRAL:
    put(SPEC["core"], f"color.neutral.{key}", var_("color", name, description=f"the warm neutral ramp's {key}"))
for key, name, scope in BLUE:
    put(SPEC["core"], f"color.blue.{key}", var_("color", name, scope=scope))
for key, name, scope in ACCENT:
    put(SPEC["core"], f"color.accent.{key}", var_("color", name, scope=scope))
for key, name, scope in SUPPORT:
    put(SPEC["core"], f"color.support.{key}", var_("color", name, scope=scope))
for key, name in LEGACY:
    put(SPEC["core"], f"color.legacy.{key}", var_("color", name, scope="legacy"))


def _px(x):
    return ("%g" % round(float(x), 2)) + "px"


def _shadow_layers(v):
    """'rgba(0,0,0,.25) 0px 4px 37px 0px' -> DTCG shadow layers."""
    layers = []
    for part in re.split(r",(?![^(]*\))", v.strip()):
        toks = part.strip().split()
        inset = "inset" in toks
        nums = [t for t in toks if re.fullmatch(r"-?[\d.]+(px|rem)?", t)]
        col = " ".join(t for t in toks if t != "inset" and not re.fullmatch(r"-?[\d.]+(px|rem)?", t))
        if not nums or not col:
            return None
        nums = (nums + ["0"] * 4)[:4]
        layers.append({"color": col, "offsetX": _px(nums[0].rstrip("pxrem") or 0),
                       "offsetY": _px(nums[1].rstrip("pxrem") or 0), "blur": _px(nums[2].rstrip("pxrem") or 0),
                       "spread": _px(nums[3].rstrip("pxrem") or 0), "inset": inset})
    return layers


_snm = (SC["legacy"] or {}).get("--shadow-nav-light-menu") or {}
if _shadow_layers(str(_snm.get("value") or _snm.get("raw") or "")):
    put(SPEC["core"], "shadow.legacyNavMenu",
        {"$value": _shadow_layers(str(_snm.get("value") or _snm.get("raw"))), "$type": "shadow",
         "$extensions": {"source": "css-var --shadow-nav-light-menu (legacy scope: the old nav menu's drop shadow)"}})

# The nav's own semantic layer, declared on .theme-light.
for key, name in [
    ("background", "--color-nav-background"), ("background-highlight", "--color-nav-background-highlight"),
    ("border", "--color-nav-border"), ("button-hover", "--color-nav-button-hover"),
    ("content-primary", "--color-nav-content-primary"), ("content-secondary", "--color-nav-content-secondary"),
    ("content-tertiary", "--color-nav-content-tertiary"), ("control", "--color-nav-control"),
    ("hover", "--color-nav-hover"),
]:
    put(SPEC["core"], f"color.nav.{key}", var_("color", name))

# ------------------------------------------------------------- type & fonts
# Font stacks: --font-sans/--font-serif/--font-mono resolve to a guaranteed-
# invalid value off the next/font variable classes, so the stacks are the
# declared compositions (theme bin) with --font-<Name> expanded to its
# <Name>, "<Name> Fallback" pair, cross-checked against the measured
# fontFamily of the hero title, the eyebrow and the changelog title.
def fam(primary):
    return {
        "saans": 'Saans, "Saans Fallback", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", Meiryo, "Noto Sans JP", ui-sans-serif, system-ui, sans-serif',
        "serrif": 'Serrif, "Serrif Fallback", "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", ui-serif, Georgia, serif',
        "serrif-condensed": '"Serrif Condensed", "Serrif Fallback", "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", ui-serif, Georgia, serif',
        "saansmono": 'SaansMono, "SaansMono Fallback", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", Meiryo, "Noto Sans JP", ui-monospace, monospace',
        "mediumll": 'MediumLL, "MediumLL Fallback", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", Meiryo, "Noto Sans JP", ui-sans-serif, system-ui, sans-serif',
        "ivoryll": 'IvoryLL, "IvoryLL Fallback", "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", ui-serif, Georgia, serif',
        "dmmono": 'DmMono, "DmMono Fallback", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", Meiryo, "Noto Sans JP", ui-monospace, monospace',
        "inter": 'Inter, "Inter Fallback", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", Meiryo, "Noto Sans JP", ui-sans-serif, system-ui, sans-serif',
        "beretta": 'Beretta, "Beretta Fallback"',
        "honey": 'Honey, "Honey Fallback"',
        "maxi": 'Maxi, "Maxi Fallback"',
        "ozik": 'Ozik, "Ozik Fallback"',
        "planar": 'Planar, "Planar Fallback"',
        "raster": 'Raster, "Raster Fallback"',
    }[primary]


FAM_SRC = {
    "saans": 'declared --font-sans = var(--font-Saans), var(--font-fallback-jp), … (@layer theme :root / .brand-i2y4); matches computed fontFamily of hero-title, nav, buttons and fields',
    "serrif": 'declared --font-serif = var(--font-Serrif), var(--font-fallback-jp-serif), … (@layer theme :root / .brand-i2y4); Serrif faces declared in the font harvest, unloaded on captured pages',
    "serrif-condensed": 'declared --font-serif-condensed (.brand-i2y4); its variable class exists but no @font-face for it appeared in the harvest',
    "saansmono": 'declared --font-mono = var(--font-SaansMono), var(--font-fallback-jp), … (@layer theme :root / .brand-i2y4); matches computed fontFamily of eyebrow ("TRUSTED BY 30,000+ LEADING BRANDS")',
    "mediumll": 'declared --font-sans = var(--font-MediumLL), … (.intercom-legacy); the older help/changelog surfaces',
    "ivoryll": 'declared --font-serif = var(--font-IvoryLL), … (.intercom-legacy)',
    "dmmono": 'declared --font-mono = var(--font-DmMono), … (.intercom-legacy)',
    "inter": 'declared --font-Inter (:root) for the Japanese fallback stack',
    "beretta": 'declared --font-Beretta on .iP2mxq_variable (next/font); campaign display face',
    "honey": 'declared --font-Honey on ._3Y33_a_variable; campaign display face',
    "maxi": 'declared --font-Maxi on .OFy0YG_variable; campaign display face',
    "ozik": 'declared --font-Ozik on .u2QQta_variable; campaign display face',
    "planar": 'declared --font-Planar on .gVc2cG_variable; campaign display face',
    "raster": 'declared --font-Raster on .LhItRa_variable; campaign display face',
}
for key in ("saans", "serrif", "serrif-condensed", "saansmono", "mediumll", "ivoryll", "dmmono", "inter", "beretta", "honey", "maxi", "ozik", "planar", "raster"):
    put(SPEC["core"], f"fontFamily.{key}", val_("fontFamily", fam(key), FAM_SRC[key]))
put(SPEC["core"], "fontFamily.system", val_("fontFamily", 'ui-sans-serif, system-ui, sans-serif', 'computed fontFamily of document.body (what the unbranded page ground paints)'))

for key, name in [("light", "--font-weight-light"), ("normal", "--font-weight-normal"), ("medium", "--font-weight-medium"), ("semibold", "--font-weight-semibold"), ("bold", "--font-weight-bold")]:
    put(SPEC["core"], f"fontWeight.{key}", var_("fontWeight", name))

# The declared type scale: --text-{style}-{breakpoint}[--{line-height,
# letter-spacing, font-weight}] for styles heading-1..6, callout, body-xl,
# body-lg, body, label-lg, button-lg, button-sm across mobile/tablet/
# small-desktop/desktop, plus Tailwind's own --text-{xs..5xl}.
BP = ("mobile", "tablet", "small-desktop", "desktop")
STYLES = ["heading-1", "heading-2", "heading-3", "heading-4", "heading-5", "heading-6",
          "callout", "body-xl", "body-lg", "body", "label-lg", "button-lg", "button-sm"]
group_of = {"callout": "callout", "body-xl": "body", "body-lg": "body", "body": "body", "label-lg": "label",
            "button-lg": "button", "button-sm": "button"}
sub_of = {"callout": "base", "body-xl": "xl", "body-lg": "lg", "body": "base", "label-lg": "lg",
          "button-lg": "lg", "button-sm": "sm"}
DIM_RE = re.compile(r"-?\d*\.?\d+(px|rem)")
not_tok = []
TYPO = {}   # (style, bp) -> dict of token paths for the composite pass
for style in STYLES:
    for bp in BP:
        name = f"--text-{style}-{bp}"
        if name not in R:
            continue
        grp = group_of.get(style, "heading")
        sub = style.split("-")[1] if grp == "heading" else sub_of[style]
        put(SPEC["core"], f"fontSize.{grp}.{sub}.{bp}", var_("dimension", name))
        TYPO[(style, bp)] = {"fontSize": f"fontSize.{grp}.{sub}.{bp}"}
        for prop, ty, bucket in (("line-height", "number", "lineHeight"), ("letter-spacing", "dimension", "letterSpacing")):
            vn = f"{name}--{prop}"
            rv = RL.get(vn)
            if rv is None:
                continue
            val = rv.get("value", rv.get("raw"))
            ok = (ty == "number" and isinstance(val, (int, float))) or (ty == "dimension" and DIM_RE.fullmatch(str(val or "")))
            if not ok:
                if rv.get("raw"):
                    not_tok.append((vn, rv["raw"]))
                continue
            put(SPEC["core"], f"{bucket}.{grp}.{sub}.{bp}", var_(ty, vn))
            TYPO[(style, bp)][bucket] = f"{bucket}.{grp}.{sub}.{bp}"
        TYPO[(style, bp)]["fontWeight"] = "fontWeight.normal"
# Tailwind's own scale (the utility --text-* names carry rem sizes).
TAIL = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]
for size in TAIL:
    n = f"--text-{size}"
    if n not in R:
        continue
    put(SPEC["core"], f"fontSize.tailwind.{size}", var_("dimension", n))
    rv = RL.get(f"{n}--line-height")
    if rv is not None:
        if isinstance(rv.get("value"), (int, float)):
            put(SPEC["core"], f"lineHeight.tailwind.{size}", var_("number", f"{n}--line-height"))
        elif rv.get("raw"):
            not_tok.append((f"{n}--line-height", rv["raw"]))

# Typography composites: one per style per breakpoint, aliasing the scale
# tokens so each level reads as the full role the site applies.
def typo(style, bp):
    parts = TYPO[(style, bp)]
    v = {
        "fontFamily": "{fontFamily.saansmono}" if style == "label-lg" else "{fontFamily.saans}",
        "fontWeight": "{fontWeight.normal}",
        "fontSize": "{%s}" % parts["fontSize"],
    }
    if parts.get("lineHeight"):
        v["lineHeight"] = "{%s}" % parts["lineHeight"]
    if parts.get("letterSpacing"):
        v["letterSpacing"] = "{%s}" % parts["letterSpacing"]
    return v


for (style, bp), parts in sorted(TYPO.items()):
    grp = group_of.get(style, "heading")
    sub = style.split("-")[1] if grp == "heading" else sub_of[style]
    leaf = {"$value": typo(style, bp), "$type": "typography",
            "$extensions": {"source": f"declared --text-{style}-{bp} and its --line-height/--letter-spacing parts (@layer theme :root)"}}
    node, last = descend(SPEC["core"], f"typography.{grp}.{sub}.{bp}".split("."))
    node[last] = leaf

# --------------------------------------------------------------- geometry
for key, name in [("xs", "--radius-xs"), ("sm", "--radius-sm"), ("md", "--radius-md"), ("lg", "--radius-lg"), ("xl", "--radius-xl"), ("2xl", "--radius-2xl")]:
    put(SPEC["core"], f"radius.{key}", var_("dimension", name))
put(SPEC["core"], "spacing.base", var_("dimension", "--spacing"))
for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"):
    put(SPEC["core"], f"container.{key}", var_("dimension", f"--container-{key}"))
put(SPEC["core"], "container.screen-3xl", var_("dimension", "--container-screen-3xl"))
for key, name in [("md", "--breakpoint-md"), ("3xl", "--breakpoint-3xl")]:
    put(SPEC["core"], f"breakpoint.{key}", var_("dimension", name))
for key, name in [("xs", "--blur-xs"), ("sm", "--blur-sm"), ("lg", "--blur-lg"), ("3xl", "--blur-3xl")]:
    put(SPEC["core"], f"blur.{key}", var_("dimension", name))
for key, name in [("nav", "--z-index-nav"), ("nav-menu", "--z-index-nav-menu"), ("nav-tooltip", "--z-index-nav-tooltip"),
                  ("overlay", "--z-index-overlay"), ("modal", "--z-index-modal"), ("modal-control", "--z-index-modal-control")]:
    put(SPEC["core"], f"zIndex.{key}", var_("number", name))

# ------------------------------------------------------------- motion layer
for n in sorted(R):
    if n.startswith("--ease-") and R.get(n):
        put(SPEC["core"], f"easing.{n[7:]}", var_("cubicBezier", n))
put(SPEC["core"], "duration.default", var_("duration", "--default-transition-duration"))
put(SPEC["core"], "easing.default", var_("cubicBezier", "--default-transition-timing-function"))
# --animate-* are full shorthands (name duration easing count): evidence in
# raw/css-vars.json, not a DTCG shape — listed under notTokenised.
for n in ("--animate-spin", "--animate-pulse"):
    if R.get(n):
        not_tok.append((n, R[n]))
# --aspect-video and --scroll-behavior are not DTCG shapes either.
for n in ("--aspect-video", "--scroll-behavior"):
    if R.get(n):
        not_tok.append((n, R[n]))

# -------------------------------------------------------- component tokens
# The declared --button-* set on :root (the site buttons' full state matrix)
# and the [data-media-player] vars that are dimensions or numbers.
for n in sorted(R):
    if n.startswith("--button-") and R.get(n) is not None:
        kind = RL[n].get("kind")
        ty = {"dimension": "dimension", "color": "color", "number": "number"}.get(kind)
        if ty:
            put(SPEC["component"], f"button.{n[9:]}", var_(ty, n))
for n in sorted(RS.get("media", {})):
    if n.startswith("--media-") or n.startswith("--z-index-slot"):
        rv = (SC["media"] or {})[n]
        kind = rv.get("kind")
        ty = {"dimension": "dimension", "color": "color", "number": "number"}.get(kind)
        if ty:
            path = f"zIndex.{n[len('--z-index-'):]}" if n.startswith("--z-index") else f"media.{n[len('--media-'):]}"
            put(SPEC["component"], path, var_(ty, n, scope="media"))
        else:
            not_tok.append((n + " [media]", rv.get("raw")))

# ------------------------------------------------------------- light roles
# The semantic layer, read off the painted chrome. Each leaf either aliases a
# core token ({"value": "{path}"}) or carries the measured value; the source
# names the measurement. Measured oklab() colours are converted by
# build_tokens.py's normaliser.
def L_(path, ty, value, source):
    put(SPEC["light"], path, val_(ty, value, source))


L_("background.page", "color", "{color.neutral.cream}", "--body-bg = var(--color-cream) (:root), the page ground; body itself paints transparent")
L_("background.chalk", "color", "{color.neutral.chalk}", "nav-item/nav-link hover fill = --color-chalk (measured)")
L_("background.canvas", "color", "{color.neutral.canvas}", "billing-toggle selected fill (measured) = --color-canvas")
L_("background.card", "color", "{color.neutral.white}", "header/nav and card surfaces paint white (measured header, nav-menu)")
L_("background.inset", "color", "{color.neutral.offWhite}", "input/select field fill (measured) = --color-off-white")
L_("background.banner", "color", stprop("promo-banner", "default", "style.backgroundColor"), "computed promo-banner backgroundColor (the Fin 4 top banner's gray)")
L_("background.helpGround", "color", "#f3f5f7", "computed body background of /changes/en (the older header__lite surface's ground)")
L_("text.primary", "color", "{color.neutral.offBlack}", "computed color of hero-title, nav, buttons, fields and footer = --color-off-black")
L_("text.onDark", "color", "{color.neutral.white}", "computed color on the primary button = --color-white")
L_("text.muted", "color", "{color.neutral.gray-500}", "--color-gray-500, the muted copy step of the Tailwind ramp")
L_("text.nav-secondary", "color", "{color.nav.content-secondary}", "--color-nav-content-secondary (.theme-light)")
L_("text.nav-tertiary", "color", "{color.nav.content-tertiary}", "--color-nav-content-tertiary (.theme-light)")
L_("text.accent", "color", "{color.blue.helpdesk}", "promo-badge text/helpdesk-blue accent = --color-helpdesk")
L_("text.error", "color", "{color.support.error}", "--color-error (brand scope)")
L_("text.link", "color", "{color.neutral.offBlack}", "computed nav-link/footer-link colour; links paint the primary ink")
L_("border.default", "color", "{color.neutral.clay}", "border-clay utility = --color-clay; plan cards and FAQ rules")
L_("border.strong", "color", "{color.neutral.offBlack}", "hero-secondary border (measured) = --color-off-black")
L_("border.subtle", "color", stprop("feature-card", "default", "style.borderTopColor"), "computed feature-card border (black at 6% over the cream ground)")
L_("border.field", "color", stprop("input", "default", "style.borderTopColor"), "computed input/select border (translucent black)")
L_("focus.ring", "color", "{color.blue.brand}", "--color-focus-outline = --color-blue; the keyboard focus outline")
L_("accent.helpdesk", "color", "{color.blue.helpdesk}", "--color-helpdesk: the helpdesk-blue product accent (CTA hover, promo badge)")
L_("accent.fin", "color", "{color.accent.fin}", "--color-fin: the Fin orange (#ff5600)")
L_("accent.sales", "color", "{color.accent.sales}", "--color-sales")
L_("status.error", "color", "{color.support.error}", "--color-error")
L_("nav.background", "color", "{color.nav.background}", "--color-nav-background (.theme-light)")
L_("nav.background-highlight", "color", "{color.nav.background-highlight}", "nav-item hover fill (measured = --color-chalk) declared as --color-nav-background-highlight")
L_("nav.hover", "color", "{color.nav.hover}", "--color-nav-hover (.theme-light)")
L_("nav.border", "color", "{color.nav.border}", "--color-nav-border (.theme-light)")
L_("nav.content-primary", "color", "{color.nav.content-primary}", "--color-nav-content-primary")
L_("badge.helpdesk-fill", "color", stprop("promo-badge", "default", "style.backgroundColor"), "computed promo-badge background = --color-helpdesk at 15% (bg-helpdesk/15)")
L_("badge.helpdesk-text", "color", stprop("promo-badge", "default", "style.color"), "computed promo-badge text = --color-helpdesk")
L_("field.background", "color", "{color.neutral.offWhite}", "computed input/select field fill = --color-off-white")
L_("field.border", "color", stprop("input", "default", "style.borderTopColor"), "computed input/select border (translucent black)")
L_("field.placeholder", "color", stprop("select", "default", "style.color"), "computed select placeholder colour (translucent black)")

# Button roles alias the declared --button-* component set.
for role, varname in [
    ("primary.background", "--button-primary-background"), ("primary.foreground", "--button-primary-foreground"),
    ("primary.hover-background", "--button-primary-hover-background"), ("primary.hover-foreground", "--button-primary-hover-foreground"),
    ("primary.hover-border", "--button-primary-hover-border"),
    ("primary.active-background", "--button-primary-active-background"), ("primary.active-foreground", "--button-primary-active-foreground"),
    ("primary.disabled-background", "--button-primary-disabled-background"), ("primary.disabled-foreground", "--button-primary-disabled-foreground"),
    ("secondary.background", "--button-secondary-background"), ("secondary.foreground", "--button-secondary-foreground"),
    ("secondary.border", "--button-secondary-border"),
    ("secondary.hover-background", "--button-secondary-hover-background"), ("secondary.hover-foreground", "--button-secondary-hover-foreground"),
    ("secondary.hover-border", "--button-secondary-hover-border"),
    ("secondary.active-background", "--button-secondary-active-background"), ("secondary.active-foreground", "--button-secondary-active-foreground"),
    ("secondary.disabled-background", "--button-secondary-disabled-background"), ("secondary.disabled-foreground", "--button-secondary-disabled-foreground"),
    ("secondary.disabled-border", "--button-secondary-disabled-border"),
]:
    src = (f"declared {varname} (:root); matches measured hero-cta/nav-cta/next-button states"
           if "primary" in role else f"declared {varname} (:root); matches measured hero-secondary")
    L_(f"action.{role}", "color", "{component.button.%s}" % varname[9:], src)

# --------------------------------------------------------- not tokenised
seen_nt = set()
SPEC["_notTokenised"] = []
for n, v in not_tok:
    if not v or n in seen_nt:
        continue
    seen_nt.add(n)
    SPEC["_notTokenised"].append({"name": n, "value": str(v), "source": f"css-var {n} ({decl_where(n.split(' ')[0])})"})

out = SPEC
(RAW / "component-tokens.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")


def count(d):
    if isinstance(d, dict) and ("type" in d or "$value" in d):
        return 1
    return sum(count(v) for v in d.values()) if isinstance(d, dict) else 0


print({k: count(v) for k, v in out.items() if k in ("core", "light", "component")}, "notTokenised:", len(out["_notTokenised"]))
