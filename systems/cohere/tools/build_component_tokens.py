"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cohere.com is a Next.js (App Router)/Tailwind v3 build backed by Sanity CMS:
the design layer lives in the CONFIG, not custom properties — a named
palette ships as utility classes (.bg-volcanic-500 { background-color:
rgb(158 158 158) }), the web3-* type scale as .text-web3-N utility rules,
the family stacks as .font-body/.font-code/.font-eyebrow/.font-variable,
the z and content-width layers as .z-*/.max-w-web3-* rules, and durations
as the standard .duration-* scale. vars.mjs's utilities bin keeps those
literal declarations, so the core below is a NAMED declared ramp (volcanic,
neutral, quartz, coral, mushroom, marble, blue, green, danger, success,
onyx, pureBlack, pureWhite) with real provenance — plus the measured roles
read off the painted chrome in raw/components-computed.json.

The site paints ONE light theme; the footer band and the promo banner are
dark islands inside it. dashboard.cohere.com/welcome/login is a separate
app surface (the sign-in boundary), measured at rest and never submitted.

The declared palette (family anchors):

  neutral   the workhorse: 15 #17171c (dark CTA), 90 #f2f2f2, 95 #fafafa
  volcanic  the brand greys: 900 #212121 ink down to 500 #9e9e9e
  quartz    the purple accent: 500 #d18ee2 to 900 #3e2644
  coral     the warm accent: 500 #ff7759, 700 #ca492d, 900 #511d12
  mushroom  warm olive greys; marble light greys; blue 500 #4c6ee6;
            green sage; danger red; success green; onyx #0c1210
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# cohere paints light only (catalog theme list): resolve against the light pass, never a dark probe.
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# cohere declares no useful :root var layer: the named palette ships as
# Tailwind config utilities (.bg-<family>-<step> rules), which vars.mjs's
# `utilities` bin preserves verbatim. util() looks a literal declaration up
# by class name so the core below is a DECLARED ramp with class provenance.
UTIL = {}
for _u in V.get("utilities", []):
    _sel = (_u.get("selector") or "").lstrip(".")
    if _sel:
        UTIL.setdefault(_sel, _u.get("literal") or {})


def util(cls, prop):
    """Literal declaration of utility class `cls` (e.g. bg-volcanic-500 ->
    background-color). None when the harvest never saw the rule."""
    return (UTIL.get(cls) or {}).get(prop)


def rgb_of(v):
    """`rgb(158 158 158/var(--tw-bg-opacity,1))` -> `rgb(158 158 158)` —
    strip the /alpha tail and the var() inside."""
    v = (v or "").strip()
    # The Tailwind opacity var carries its own default (1 in every utility here): use it, and keep a
    # numeric slash alpha instead of dropping it.
    v = re.sub(r"/\s*var\([^,)]*,\s*([\d.]+%?)\s*\)", r"/\1", v)
    m = re.fullmatch(r"rgb\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)\s*/\s*([\d.]+)(%?)\s*\)", v)
    if m:
        a = float(m.group(4)) / (100 if m.group(5) else 1)
        return "rgb(%s %s %s)" % m.group(1, 2, 3) if a >= 1 else "rgba(%s, %s, %s, %g)" % (m.group(1), m.group(2), m.group(3), a)
    return v.strip()


#   (token path, utility class, description) — the declared colour ramp.
#   Family anchors come from .bg-* rules; every step is emitted under
#   core.color.<family>.<step>.
PALETTE_FAMILIES = {
    "volcanic": "The brand grey ramp (volcanic-900 #212121 is the ink the site paints everywhere).",
    "neutral": "The workhorse ramp: neutral-15 #17171c is the dark CTA, 90 #f2f2f2 a panel fill, 95 #fafafa near-white.",
    "quartz": "The purple accent ramp (quartz-500 #d18ee2 to quartz-900 #3e2644).",
    "coral": "The warm accent ramp (coral-500 #ff7759, coral-700 #ca492d, coral-900 #511d12).",
    "mushroom": "The warm olive-grey ramp.",
    "marble": "The light marble-grey ramp.",
    "blue": "The blue ramp (blue-500 #4c6ee6, blue-900 #121e4a navy).",
    "green": "The muted sage-green ramp.",
    "danger": "The error red ramp.",
    "success": "The success green ramp.",
}
DECLARED_SOLIDS = [
    ("pureBlack", "bg-pureBlack", "Declared pureBlack (#000) — the promo banner fill."),
    ("pureWhite", "bg-pureWhite", "Declared pureWhite (#fff) — the page ground and CTA pill."),
    ("onyx", "bg-onyx", "Declared onyx (#0c1210) — the near-black green-tinted ink."),
]
#   (token path, component, state, style prop, description) — literal
#   colours measured on the paint where a named step is not the source.
CORE = []
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. cohere.com "
    "declares its design layer as Tailwind config utility classes "
    "(raw/css-vars.json's utilities bin): a named palette (volcanic, neutral, "
    "quartz, coral, mushroom, marble, blue, green, danger, success, onyx, "
    "pureBlack/pureWhite), the web3-* type scale, the font stacks, the "
    "z/content-width layers and the duration/ease steps. Semantic roles are "
    "measured on the painted chrome in raw/components-computed.json and "
    "alias the declared ramp when the value matches. One theme exists "
    "(light); the footer and promo banner are dark islands inside it."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


# ------------------------------------------------------------- light roles
#
# The bundle declares no semantic role names of its own; every role below is
# measured on the painted chrome (header, hero, callout cards, footer
# filters, footer) and aliases a core token when the value matches. The
# marketing site paints one light theme, emitted under `light`; the footer
# is a black island inside it, so its text role is named onDark.
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer) or the special `ringShadow`: resolve the dotted path
    inside the measured state (the anchors keep UA-default colour, so painted
    text/fill lives on the text child, a sibling layer or a pseudo).
    `ringShadow` returns the colour of the `0 0 0 Npx` ring layer in the
    element's own boxShadow — the hairline many Framer controls paint instead
    of a real border."""
    d = C[comp]["states"][state]
    # `.firstColor`/`.lastColor` pull the first/last colour literal out of a
    # string property (gradient stops in backgroundImage, shadow layers).
    for suffix, pick in ((".firstColor", 0), (".lastColor", -1)):
        if prop.endswith(suffix):
            v = stprop(comp, state, prop[: -len(suffix)])
            cols = re.findall(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
            return cols[pick] if cols else ""
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    # A bare property reads the computed style block (backgroundColor); a
    # dotted path walks the state dict (textStyle.color, paint.2.bg,
    # ancestors.0.bg), a numeric step indexing a list. A `.border` tail reads
    # the colour out of the "T:1px solid rgba(...)" string styleOf records.
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\)", v)
    if m:
        r, g, b = m.groups()
        return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    m = re.fullmatch(r"lab\(\s*([\d.]+%?)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Tailwind v4 declares colours as lab() (D50 white); convert through
        # XYZ with Bradford adaptation to D65 so the token is an sRGB value.
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        a_, b_ = float(m.group(2)), float(m.group(3))
        fy = (L * 100 + 16) / 116
        fx, fz = fy + a_ / 500, fy - b_ / 200
        d = 6 / 29
        finv = lambda t: t ** 3 if t > d else 3 * d * d * (t - 4 / 29)
        X, Y, Z = 0.964212 * finv(fx), finv(fy), 0.825188 * finv(fz)
        # Bradford D50 -> D65
        X, Y, Z = (0.9555766 * X - 0.0230393 * Y + 0.0631636 * Z,
                   -0.0282895 * X + 1.0099416 * Y + 0.0210077 * Z,
                   0.0122982 * X - 0.020483 * Y + 1.3299098 * Z)
        R_ = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
        G_ = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
        B_ = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        al = m.group(4)
        al = float(al[:-1]) / 100 if al and al.endswith("%") else float(al) if al else 1
        if al >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % al})"
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Framer paints some alpha greys as oklab(); convert to sRGB.
        L, A, B = (float(m.group(i)) for i in (1, 2, 3))
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541729 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        R_ = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        G_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        B_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        a = m.group(4)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % a})"
    m = re.fullmatch(r"oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Sheets can paint oklch(); convert through OKLab to sRGB so the
        # token is a usable colour value.
        import math
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        C_, H = float(m.group(2)), math.radians(float(m.group(3)))
        A, B = C_ * math.cos(H), C_ * math.sin(H)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541729 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        R_ = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        G_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        B_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        a = m.group(4)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and ("var" in v or "value" in v):
            val = norm_color(R[v["var"]]) if "var" in v else norm_color(v["value"])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
core_color = SPEC["core"].setdefault("color", {})
# The declared ramp: every .bg-<family>-<step> rule becomes
# color.<family>.<step> with the utility class as its provenance.
for _fam, _desc in PALETTE_FAMILIES.items():
    _steps = sorted(
        (int(_k.rsplit("-", 1)[1]), _k)
        for _k in UTIL
        if re.fullmatch(rf"bg-{_fam}-\d+", _k)
    )
    for _n, _cls in _steps:
        _v = rgb_of(util(_cls, "background-color"))
        if not _v:
            continue
        node, last = descend(core_color, [_fam, str(_n)])
        node[last] = {"value": norm_color(_v), "type": "color",
                      "source": f"declared .{_cls} background-color (raw/css-vars.json utilities)",
                      "description": f"Declared {_fam}-{_n}. {_desc}"}
for _path, _cls, _desc in DECLARED_SOLIDS:
    _v = rgb_of(util(_cls, "background-color"))
    if not _v:
        continue
    node, last = descend(core_color, [_path])
    node[last] = {"value": norm_color(_v), "type": "color",
                  "source": f"declared .{_cls} background-color (raw/css-vars.json utilities)",
                  "description": _desc}
for path, cname, state, prop, desc in CORE:
    v = stprop(cname, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        raise SystemExit(f"core palette source missing: {cname} {state} {prop}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": v, "type": "color",
                  "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                  "description": desc}
collect(core_color, "color.")


def role(path, comp, state, prop, desc):
    v = stprop(comp, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "dark"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf



for path, comp, state, prop, desc in [
    # ----- the single light surface (footer/promo are dark islands inside it)
    ("light:surface.page", "page-ground", "default", "backgroundColor", "The page ground — painted by the body (pureWhite #fff)."),
    ("light:surface.raised", "callout-card", "default", "paint.0.bg", "A raised card ground in page content — the callout card's #f0eee9 fill (a marble-family tint)."),
    ("light:surface.dark", "footer", "default", "paint.3.bg", "The footer band's dark island fill (neutral-15 #17171c)."),
    ("light:surface.band", "footer", "default", "paint.0.bg", "The \u201cReady to put AI to work\u201d CTA band inside the footer — a deep green #355146."),
    ("light:surface.banner", "promo-banner", "default", "backgroundColor", "The promo banner's pureBlack fill above the nav."),
    ("light:text.primary", "hero-title", "default", "color", "The primary ink on the page ground (volcanic-900 #212121)."),
    ("light:text.nav", "nav-item", "default", "color", "The nav-link ink at rest (pureBlack)."),
    ("light:text.onDark", "footer-link", "default", "color", "Text on the dark footer band (neutral-95 #fafafa)."),
    ("light:text.onAccent", "cta-dark", "default", "color", "White text on the dark CTA pills (neutral-15 #17171c)."),
    ("light:text.banner", "promo-banner", "default", "color", "White text on the promo banner."),
    ("light:accent", "cta-dark", "default", "backgroundColor", "The dark CTA fill — the surface's accent control (neutral-15 #17171c)."),
    ("light:accentHover", "nav-cta", "hover", "backgroundColor", "The dark CTA's hover fill — pureBlack #000."),
    ("light:border.subtle", "signin-oauth", "default", "borderTopColor", "The 1px hairline on the sign-in OAuth rows (#dadce0)."),
    ("light:border.input", "signin-field", "default", "borderTopColor", "The sign-in field's 1px border (#bdbdbd)."),
    ("light:focus", "nav-item", "focus-visible", "outlineColor", "The 1px auto focus outline on nav links (#101010)."),
    ("light:focusAlt", "cta-dark", "focus-visible", "borderTopColor", "The CTA pill's focus repaint: the transparent 2px border swaps to neutral-95 #fafafa."),
    ("light:focusOnDark", "signin-oauth", "focus-visible", "outlineColor", "The sign-in OAuth row's 1px solid focus outline (#616161)."),
]:

    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# The visited-link colour the sheet declares sits beside the measured link
# role: coral-700 visited on volcanic-900 text.
_v = rgb_of(util("text-coral-700", "color"))
if _v:
    SPEC["light"].setdefault("text", {})["visited"] = {
        "type": "color", "value": norm_color(_v),
        "source": "declared .text-coral-700 color (raw/css-vars.json utilities) — applied to content links under :visited",
        "description": "The visited-link colour (coral-700 #ca492d) the sheet declares on content links."}
# No muted/secondary text paints signed out, but the sign-in field declares
# `disabled:text-volcanic-700`, and the same volcanic-700 #616161 is measured on
# the OAuth row's focus outline — dual provenance for the muted shade.
_v = rgb_of(util("bg-volcanic-700", "background-color"))
if _v:
    SPEC["light"].setdefault("text", {})["muted"] = {
        "type": "color", "value": norm_color(_v),
        "source": "declared .bg-volcanic-700 background-color (raw/css-vars.json utilities); also measured as the signin-oauth focus-visible outlineColor (raw/components-computed.json)",
        "description": "The muted shade (volcanic-700 #616161) — what the sign-in field's disabled:text-volcanic-700 applies under :disabled; never paints as body text signed out."}
# The footer accordion rows (li.border-b) are hidden clones at 1440 but carry
# the 1px neutral-40 separator they paint at mobile widths — labelled, not
# passed off as a painted desktop border.
_v = stprop("footer", "default", "paint.4.border")
if _v:
    SPEC["light"].setdefault("border", {})["onDark"] = {
        "type": "color", "value": norm_color(re.search(r"rgba?\([^)]*\)", _v).group(0)),
        "source": "computed border of the footer's li.border-b accordion rows, hidden 0x0 clones at 1440 (raw/components-computed.json); declared neutral-40 (raw/css-vars.json utilities)",
        "description": "The 1px row separator the footer's mobile accordion layout declares (neutral-40 #525260); measured on its hidden desktop clones — it paints where the same rows render at mobile widths."}
# The mobile-menu scrim tint is a declared utility: .bg-black\\/20 paints
# volcanic-900 at 20%.
_v = rgb_of(util("bg-black\\/20", "background-color"))
if _v:
    SPEC["light"].setdefault("overlay", {})["scrim"] = {
        "type": "color", "value": norm_color(_v),
        "source": "declared .bg-black/20 background-color (raw/css-vars.json utilities)",
        "description": "The mobile-menu scrim tint — volcanic-900 at 20% (declared .bg-black/20)."}

# The CTA pill's ::before paints the "ease-button-gradient" sweep:
# linear-gradient(270deg, quartz-500 #d18ee2, coral-500 #ff7759).
try:
    _img = stprop("footer-cta", "default", "paint.1.bgImage") or ""
    _m = re.match(r"linear-gradient\((\d+)deg,\s*(.+)\)", _img)
    if _m:
        _cols = re.findall(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", _m.group(2))
        _stops = [{"color": norm_color(c), "position": round(i / max(len(_cols) - 1, 1), 2)} for i, c in enumerate(_cols)]
        if _stops:
            SPEC["core"].setdefault("gradient", {})["cta"] = {
                "type": "gradient", "value": _stops, "angle": _m.group(1) + "deg",
                "source": "computed backgroundImage of the footer CTA's ::before layer (raw/components-computed.json, footer-cta default)",
                "description": "The CTA pill's gradient sweep (::before) — quartz-500 #d18ee2 to coral-500 #ff7759 at 270deg, revealed through the ease-button-gradient mask."}
except KeyError:
    pass


# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# The surface's painted elevations: whatever shadow the cards, pills or
# banner actually paint. The first component with a real shadow wins the
# slot.
for _cname in ("callout-card", "cta-dark", "promo-banner", "signin-card"):
    try:
        _sh = stprop(_cname, "default", "boxShadow") or ""
        if _sh and _sh != "none":
            _layers = []
            for _ly in re.split(r",(?![^(]*\))", _sh):
                m = re.match(
                    r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?",
                    _ly)
                if m:
                    _layer = {"color": m.group(1), "offsetX": m.group(2) + "px",
                              "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                              "spread": m.group(5) + "px"}
                    if m.group(6):
                        _layer["inset"] = True
                    _layers.append(_layer)
            if _layers:
                SPEC["light"]["shadow"] = {"card" if _cname == "callout-card" else "control": {
                    "type": "shadow", "value": _layers,
                    "source": f"computed boxShadow of {_cname} default (raw/components-computed.json)",
                    "description": f"The {_cname}'s layered shadow — the surface's painted elevation (inset edge lights + ambient drops)."}}
            break
    except KeyError:
        continue

# Declared radii: the Tailwind v3 scale ships sm→3xl + full; measured
# control radii sit beside them.
rad = SPEC["core"].setdefault("radius", {})
# Declared radius steps: cohere's Tailwind config overrides the default scale
# (md 6.8px, lg 12px, xl 22px, 2xl 30px, 3xl 1.5rem); the browser decomposes
# the shorthand into the four corner longhands, so read a corner prop.
for key, cls, desc in [
    ("sm", "rounded-sm", "Declared rounded-sm (4px)."),
    ("md", "rounded-md", "Declared rounded-md (6.8px)."),
    ("lg", "rounded-lg", "Declared rounded-lg (12px)."),
    ("xl", "rounded-xl", "Declared rounded-xl (22px)."),
    ("xxl", "rounded-2xl", "Declared rounded-2xl (30px)."),
    ("xxxl", "rounded-3xl", "Declared rounded-3xl (1.5rem = 24px)."),
    ("full", "rounded-full", "Declared rounded-full (9999px) — the pill controls."),
]:
    v = util(cls, "border-radius") or util(cls, "border-top-left-radius")
    if v:
        rad[key] = {"value": v, "type": "dimension",
                    "source": f"declared .{cls} border-radius (raw/css-vars.json utilities)",
                    "description": desc}
for key, cname, desc in [
    ("control", "nav-cta", "The measured CTA-pill corner radius."),
    ("card", "callout-card", "The measured callout-card corner."),
]:
    try:
        v = stprop(cname, "default", "borderTopLeftRadius")
        if v:
            rad[key] = {"value": v, "type": "dimension",
                        "source": f"computed borderTopLeftRadius of {cname} default (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# Declared motion: the Tailwind duration/ease scale ships as .duration-*/
# .ease-* utilities; measured transitions on the paint sit beside them.
for key, cls, desc in [
    ("fast", "duration-150", "Declared duration-150 (.15s)."),
    ("default", "duration-200", "Declared duration-200 (.2s) — the nav-link and button colour swaps."),
    ("slow", "duration-300", "Declared duration-300 (.3s) — the banner-close rotation and menu scrim."),
    ("slower", "duration-500", "Declared duration-500 (.5s)."),
]:
    v = util(cls, "transition-duration")
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
            "value": v, "type": "duration",
            "source": f"declared .{cls} transition-duration (raw/css-vars.json utilities)",
            "description": desc}
for key, cname, prop, desc in [
    ("control", "nav-cta", "transitionDuration", "The measured CTA transition."),
    ("nav", "nav-item", "transitionDuration", "The measured nav-link transition."),
]:
    try:
        v = stprop(cname, "default", prop)
        if v and v != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("duration", {})["measured" + key.title()] = {
                "value": v.split(",")[0].strip(), "type": "duration",
                "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass
for key, cls in [("in_", "ease-in"), ("out", "ease-out"), ("inOut", "ease-in-out")]:
    v = util(cls, "transition-timing-function")
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
            "value": v, "type": "cubicBezier",
            "source": f"declared .{cls} transition-timing-function (raw/css-vars.json utilities)",
            "description": f"Declared {cls}."}
for key, cname, desc in [
    ("button", "nav-cta", "The `ease` curve on the CTA pills\u2019 background/color swap (0.3s)."),
]:
    try:
        v = stprop(cname, "default", "transitionTimingFunction")
        m = re.search(r"cubic-bezier\([^)]+\)", v or "")
        if m:
            SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
                "value": m.group(0), "type": "cubicBezier",
                "source": f"computed transitionTimingFunction of {cname} default (raw/components-computed.json)",
                "description": desc}
        elif v and v.strip().split(",")[0].strip() in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
            SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
                "value": v.strip().split(",")[0].strip(), "type": "cubicBezier",
                "source": f"computed transitionTimingFunction of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Spacing: Tailwind v3's 4px base ships as gap/p-* steps (gap-1 = .25rem).
v = util("gap-1", "gap") or util("gap-1", "row-gap")
if v:
    SPEC["core"].setdefault("spacing", {})["unit"] = {
        "value": v, "type": "dimension",
        "source": "declared .gap-1 gap (raw/css-vars.json utilities)",
        "description": "The spacing base unit (.25rem = 4px) — every gap/padding multiplies it."}
# The declared z and content-width layers.
for key, cls, desc in [
    ("background", "z-background", "Declared z-background (0)."),
    ("content", "z-content", "Declared z-content (20)."),
    ("nav", "z-nav", "Declared z-nav (100) — the fixed chrome layer."),
]:
    v = util(cls, "z-index")
    if v:
        SPEC["core"].setdefault("z", {})[key] = {
            "value": v, "type": "number",
            "source": f"declared .{cls} z-index (raw/css-vars.json utilities)",
            "description": desc}
for key, cls, desc in [
    ("fullScreen", "max-w-web3-full-screen", "Declared max-w-web3-full-screen (2280px) — the outermost content measure."),
    ("internal", "max-w-web3-internal-wrapper", "Declared max-w-web3-internal-wrapper (1920px) — the inner column."),
    ("blog", "max-w-web3-blog-lp-wrapper", "Declared max-w-web3-blog-lp-wrapper (1390px)."),
]:
    v = util(cls, "max-width")
    if v:
        SPEC["core"].setdefault("layout", {}).setdefault("maxWidth", {})[key] = {
            "value": v, "type": "dimension",
            "source": f"declared .{cls} max-width (raw/css-vars.json utilities)",
            "description": desc}

# Type: the web3-* scale declares size/leading/tracking per step.
for _cls, _lit in sorted(UTIL.items()):
    _m = re.fullmatch(r"text-web3-(\d+)", _cls)
    if _m and _lit.get("font-size"):
        _n = _m.group(1)
        _d = f"Declared text-web3-{_n} (font-size {_lit['font-size']}, line-height {_lit.get('line-height','?')}"
        if _lit.get("letter-spacing") and _lit["letter-spacing"] != "0":
            _d += f", tracking {_lit['letter-spacing']}"
        _d += ")."
        SPEC["core"].setdefault("fontSize", {})[f"web3{_n}"] = {
            "value": _lit["font-size"], "type": "dimension",
            "source": f"declared .{_cls} font-size (raw/css-vars.json utilities)",
            "description": _d}
for key, cls in [("normal", "font-normal"), ("medium", "font-medium"), ("semibold", "font-semibold")]:
    v = util(cls, "font-weight")
    if v:
        SPEC["core"].setdefault("fontWeight", {})[key] = {
            "value": int(v), "type": "fontWeight",
            "source": f"declared .{cls} font-weight (raw/css-vars.json utilities)",
            "description": f"Declared {cls}."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Request-a-demo pill."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav links (py-1.5)."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The hero CTA pill."),
    ("control.heightMenuButton", "m-menu-button", "default", "height", "The mobile menu toggle."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "CTA-pill corner radius."),
    ("control.heightOAuth", "signin-oauth", "default", "height", "The sign-in OAuth row."),
    ("banner.height", "promo-banner", "default", "height", "The promo banner strip."),
    ("nav.height", "header", "default", "height", "The fixed nav bar at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.width", "m-menu-open", "default", "width", "The mobile menu overlay at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure."),
    ("card.widthCallout", "callout-card", "default", "width", "A callout card at 1440px."),
    ("field.widthSignin", "signin-field", "default", "width", "The sign-in email field."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------- typography
#
# Families are declared as .font-* utility stacks (Unica77 Cohere Web body,
# CohereMono code/eyebrow, CohereVariable display) — the harvest carries
# them verbatim. Measured display sizes sit beside the declared web3-* steps.

font = SPEC["core"].setdefault("font", {})
for key, cls, desc in [
    ("ui", "font-body", "Declared font-body: Unica77 Cohere Web + Inter/Arial/system fallbacks — the UI face."),
    ("mono", "font-code", "Declared font-code: CohereMono + ui-monospace fallbacks — the code face."),
    ("eyebrow", "font-eyebrow", "Declared font-eyebrow: CohereMono + sans fallbacks — the eyebrow/label face."),
    ("display", "font-variable", "Declared font-variable: CohereVariable + Space Grotesk fallbacks — the display face."),
]:
    v = util(cls, "font-family")
    if v:
        font.setdefault("family", {})[key] = {"type": "fontFamily", "value": v.replace("'", '"'),
            "source": f"declared .{cls} font-family (raw/css-vars.json utilities)",
            "description": desc}
try:
    f = (stprop("hero-title", "default", "fontFamily") or "").strip()
    if f:
        font.setdefault("family", {})["displayMeasured"] = {"type": "fontFamily", "value": f,
            "source": "computed fontFamily of hero-title default (raw/components-computed.json)",
            "description": "The face the hero headline actually paints."}
except KeyError:
    pass

for key, cname, desc in [
    ("hero", "hero-title", "The hero display headline at 1440px (96px, CohereText)."),
    ("h1Pricing", "pricing-title", "The pricing headline (72px)."),
    ("h2", "section-title", "Section headings."),
    ("mHero", "m-hero", "The hero headline at 390px."),
    ("nav", "nav-item", "Nav labels (web3-14)."),
    ("footer", "footer-link", "Footer links."),
    ("banner", "promo-banner", "The promo banner line (web3-16)."),
    ("rate", "price-rate", "The pricing rate figure."),
    ("cta", "cta-dark", "CTA pill labels (18px)."),
    ("faq", "faq-item", "FAQ rows (18px)."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            font.setdefault("size", {})[key] = {"type": "dimension", "value": sz,
                "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("wrote raw/component-tokens.json")
