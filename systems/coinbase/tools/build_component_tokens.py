"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

coinbase.com is a styled-components/CDS (Coinbase Design System) build: the
full theme is declared inline on the page's theme elements — div.coinbase
.light carries ~830 custom properties (the eleven primitive ramps
--light-<family><step>, the 54-role --color-*/--lightColor-* semantic layer,
the --space-*/--borderRadius-*/--borderWidth-*/--fontSize-* type scales and
the --shadow-elevation* ladder), and div.coinbase.dark carries the dark
scheme of the same shape. vars.mjs records both sets under `themes`, so the
core below is a NAMED declared layer with theme-element provenance, plus the
measured roles read off the painted chrome in raw/components-computed.json.

The marketing site paints the light scheme; a .coinbase.dark band mounts
inside it (the dark CTA section). login.coinbase.com is a separate app
surface (the sign-in boundary), measured at rest and never submitted.

The declared palette (family anchors, light scheme):

  blue      the brand ramp: 60 #0052ff Coinbase blue, 90 #001a8a
  gray      the neutral ramp: 0 #ffffff, 10 #eef0f3, 100 #0a0b0d
  green     the positive ramp; orange warning; red negative; indigo,
            pink, purple, teal, yellow, chartreuse accents
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"].get("light") or {}
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# The declared CDS theme: vars.mjs read div.coinbase.light's and
# div.coinbase.dark's inline styles — each --* name to its raw and resolved
# values. tvar() looks a declaration up by name.
THEMES = V.get("themes") or {}
LIGHT_VARS = THEMES.get(".coinbase.light") or {}
DARK_VARS = THEMES.get(".coinbase.dark") or {}


def tvar(name, theme="light"):
    """Declared value of custom property `name` on the .coinbase.<theme>
    theme element (resolved where the harvest recorded it)."""
    v = (LIGHT_VARS if theme == "light" else DARK_VARS).get(name) or {}
    return v.get("resolved") or v.get("raw") or ""


UTIL = {}
for _u in V.get("utilities", []):
    _sel = (_u.get("selector") or "").lstrip(".")
    if _sel:
        UTIL.setdefault(_sel, _u.get("literal") or {})


def util(cls, prop):
    """Literal declaration of utility class `cls`. None when the harvest
    never saw the rule."""
    return (UTIL.get(cls) or {}).get(prop)


def rgb_of(v):
    """`rgb(158 158 158/var(--tw-bg-opacity,1))` -> `rgb(158 158 158)` —
    strip the /alpha tail and the var() inside."""
    v = (v or "").strip()
    v = re.sub(r"/\s*var\([^)]*\)", "", v)
    v = re.sub(r"/\s*[\d.]+%?\s*\)", ")", v)
    return v.strip()


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. coinbase.com "
    "declares its design layer as the CDS theme on div.coinbase.light and "
    "div.coinbase.dark (raw/css-vars.json's themes bin): the eleven "
    "primitive ramps (blue, gray, green, orange, red, indigo, pink, purple, "
    "teal, yellow, chartreuse), the 54-role semantic colour layer, the "
    "space/border-radius/border-width/type scales and the shadow "
    "elevations. Semantic roles are emitted from the declared "
    "--lightColor-*/--darkColor-* sets and aliased to the measured chrome "
    "in raw/components-computed.json where they agree."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


# ------------------------------------------------------------- light roles
#
# The measured roles below are read off the painted chrome (page ground,
# footer band, dark asset panel, nav, chips, sign-in surface) and alias a
# core token when the value matches. The marketing site paints the
# .coinbase.light scheme; the .coinbase.dark asset band is a theme island
# inside it, so its text role is named onDark.
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
    m = re.fullmatch(r"\d{1,3},\s*\d{1,3},\s*\d{1,3}", v)
    if m:
        # CDS declares the primitive ramps as bare "r,g,b" triplets (for
        # rgba(var(--blue60), a) consumption) — read them as opaque sRGB.
        r, g, b = (int(x) for x in v.split(","))
        return "#%02x%02x%02x" % (r, g, b)
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
# The declared primitive ramp: every --light-<family><step> on
# div.coinbase.light becomes color.<family>.<step> (the active scheme
# aliases --blue50 -> --light-blue50 etc., same values).
for _name in LIGHT_VARS:
    _m = re.fullmatch(r"--light-([a-z]+)(\d+)", _name)
    if not _m:
        continue
    _v = norm_color(tvar(_name))
    if not _v or _v in ("transparent", ""):
        continue
    _fam, _n = _m.group(1), _m.group(2)
    node, last = descend(core_color, [_fam, _n])
    node[last] = {"value": _v, "type": "color",
                  "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
                  "description": f"Declared {_fam} {_n} (light scheme)."}
# The declared semantic colour roles: every --color-<role> on
# div.coinbase.light becomes color.<role>.
for _name in LIGHT_VARS:
    _m = re.fullmatch(r"--color-([a-zA-Z0-9]+)", _name)
    if not _m:
        continue
    _v = norm_color(tvar(_name))
    if not _v or _v in ("transparent", "currentColor", ""):
        continue
    node, last = descend(core_color, ["role", _m.group(1)])
    node[last] = {"value": _v, "type": "color",
                  "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
                  "description": f"Declared active-scheme colour role {_m.group(1)}."}
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
    # ----- the painted light surface (the .coinbase.dark band is an island)
    ("light:surface.page", "page-ground", "default", "paint.0.bg", "The page ground — the .coinbase.light wrapper's white fill."),
    ("light:surface.raised", "footer", "default", "paint.0.bg", "The footer's section ground (bgAlternate #eef0f3)."),
    ("light:surface.dark", "dark-band", "default", "paint.0.bg", "The .coinbase.dark band's fill (bgInverse #0a0b0d)."),
    ("light:text.primary", "hero-title", "default", "color", "The primary ink on the page ground (fg #0a0b0d)."),
    ("light:text.muted", "footer-link", "default", "color", "The secondary text role (fgMuted #5b616e) painted by footer links."),
    ("light:text.nav", "nav-item", "default", "textStyle.color", "The nav-link ink at rest (the anchors hold the UA link colour; the painted label is fg)."),
    ("light:text.onDark", "chip", "default", "textStyle.color", "White text inside the dark asset panel's chips (fgInverse)."),
    ("light:text.onAccent", "nav-cta", "default", "color", "White text on the blue Sign-up pill (fgInverse)."),
    ("light:text.banner", "promo-banner", "default", "textStyle.color", "The promo banner's navy link line."),
    ("light:accent", "nav-cta", "default", "backgroundColor", "The Sign-up pill fill — Coinbase blue (bgPrimary #0052ff)."),
    ("light:accentHover", "nav-cta", "hover", "backgroundColor", "The Sign-up pill's hover fill (bgBrandHovered, #0048e0 @ .88)."),
    ("light:border.input", "signin-card", "default", "paint.0.border", "The sign-in email field's border (bgLineHeavy, fgMuted @ 66%)."),
    ("light:focus", "nav-item", "focus-visible", "outlineColor", "The focus outline painted on nav links."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass
# The hairline and scrim exist signed out but as declared theme values — the
# nav-bar hairline and footer/rules all paint --color-bgLine; the scrim only
# paints behind a real overlay (never opened signed out).
for _path, _var, _desc in [
    ("border.subtle", "--color-bgLine", "The hairline rule painted by the nav bar, footer rules and the sign-in OR divider (bgLine, fgMuted @ 20%)."),
    ("overlay.scrim", "--color-bgOverlay", "The modal/menu scrim role (bgOverlay, bgInverse @ 33%) — declared only; no overlay was opened signed out."),
]:
    _v = norm_color(tvar(_var))
    if _v:
        _grp, _leaf = _path.split(".")
        SPEC["light"].setdefault(_grp, {})[_leaf] = {
            "type": "color", "value": _v,
            "source": f"declared {_var} on div.coinbase.light (raw/css-vars.json themes)",
            "description": _desc}
# The declared light-scheme roles the chrome never painted signed out —
# emitted with theme-element provenance, not measured claims.
for _name in LIGHT_VARS:
    _m = re.fullmatch(r"--lightColor-(bgPrimaryWash|bgPositiveWash|bgNegativeWash|bgWarningWash|fgWarning|fgPositive|fgNegative|bgSecondaryWash|bgTertiary|accentSubtle\w+|accentBold\w+|bgLinePrimarySubtle|bgLinePrimary|bgLineInverse|bgElevation1|bgElevation2|bgSecondaryPressed|bgPrimaryHovered|bgPrimaryPressed|bgSecondaryHovered|bgTertiaryHovered|bgTertiaryPressed|bgBrandPressed|backgroundAltHovered|backgroundAltPressed|backgroundInverseDisabled)", _name)
    if not _m:
        continue
    _v = norm_color(tvar(_name))
    if not _v:
        continue
    _role = _m.group(1)
    _grp = ("wash" if "Wash" in _role else
            "status" if _role.startswith("fg") else
            "line" if _role.startswith("bgLine") else
            "elevation" if _role.startswith("bgElevation") else
            "interactive" if _role.endswith(("Hovered", "Pressed", "Disabled")) else
            "accentVariants" if _role.startswith("accent") else "other")
    node = SPEC["light"].setdefault(_grp, {})
    node[_role] = {"type": "color", "value": _v,
                   "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
                   "description": f"Declared light-scheme role {_role}."}
# The declared dark-scheme roles: the .coinbase.dark band mounts on home and
# redeclares every --color-<role> name remapped to the dark scheme.
for _name in DARK_VARS:
    _m = re.fullmatch(r"--color-([a-zA-Z0-9]+)", _name)
    if not _m:
        continue
    _v = norm_color(tvar(_name, "dark"))
    if not _v:
        continue
    _role = _m.group(1)
    if _role in ("currentColor", "transparent"):
        continue
    _grp = ("text" if _role.startswith("fg") else
            "surface" if _role.startswith("bg") and not _role.startswith("bgLine") else
            "line" if _role.startswith("bgLine") else
            "accentVariants" if _role.startswith("accent") else "other")
    node = SPEC["dark"].setdefault(_grp, {})
    node[_role] = {"type": "color", "value": _v,
                   "source": f"declared {_name} on div.coinbase.dark (raw/css-vars.json themes)",
                   "description": f"Declared dark-scheme role {_role} (the band's remapped --color-* layer)."}
# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})

# The declared shadow ladder: --shadow-elevation1/2 on div.coinbase.light,
# plus the first real shadow measured on the paint.
for _lv in ("1", "2"):
    _v = tvar(f"--shadow-elevation{_lv}")
    if _v and _v != "none":
        _layers = []
        for _ly in re.split(r",(?![^(]*\))", _v):
            # CDS declares offsets-then-colour (`0px 8px 12px rgba(...)`);
            # some stacks declare colour first — accept both orders.
            m = (re.match(r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?", _ly)
                 or re.match(r"\s*(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?\s+(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})(\s+inset)?", _ly))
            if m:
                if re.match(r"\s*rgb", _ly) or re.match(r"\s*#", _ly):
                    g = lambda i: m.group(i)
                    col, ox, oy, bl, sp, ins = g(1), g(2), g(3), g(4), g(5), g(6)
                else:
                    ox, oy, bl, sp, col, ins = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)
                _layer = {"color": norm_color(col), "offsetX": ox + "px",
                          "offsetY": oy + "px", "blur": bl + "px",
                          "spread": (sp or "0") + "px"}
                if ins:
                    _layer["inset"] = True
                _layers.append(_layer)
        if _layers:
            SPEC["core"].setdefault("shadow", {})[f"elevation{_lv}"] = {
                "type": "shadow", "value": _layers,
                "source": f"declared --shadow-elevation{_lv} on div.coinbase.light (raw/css-vars.json themes)",
                "description": f"Declared shadow elevation {_lv}."}
for _cname in ("signin-card", "carousel-card", "header", "price-row"):
    try:
        _sh = stprop(_cname, "default", "boxShadow") or ""
        if _sh and _sh != "none":
            _layers = []
            for _ly in re.split(r",(?![^(]*\))", _sh):
                m = re.match(r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?", _ly)
                if m:
                    _layer = {"color": norm_color(m.group(1)), "offsetX": m.group(2) + "px",
                              "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                              "spread": m.group(5) + "px"}
                    if m.group(6):
                        _layer["inset"] = True
                    _layers.append(_layer)
            if _layers:
                SPEC["light"]["shadow"] = {"measured": {
                    "type": "shadow", "value": _layers,
                    "source": f"computed boxShadow of {_cname} default (raw/components-computed.json)",
                    "description": f"The {_cname}'s painted shadow — the surface's real elevation."}}
            break
    except KeyError:
        continue

# Declared radii: the CDS --borderRadius-0..1000 scale; measured control
# radii sit beside them.
rad = SPEC["core"].setdefault("radius", {})
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--borderRadius-(\d+)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v:
        rad[_m.group(1)] = {"value": _v, "type": "dimension",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared borderRadius {_m.group(1)}."}
for key, cname, desc in [
    ("control", "nav-cta", "The measured Sign-up pill corner radius."),
    ("card", "carousel-card", "The measured promo-card corner."),
]:
    try:
        v = stprop(cname, "default", "borderTopLeftRadius")
        if v:
            rad[key] = {"value": v, "type": "dimension",
                        "source": f"computed borderTopLeftRadius of {cname} default (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# Declared spacing: the CDS --space-0..10 (+ fraction steps) scale.
sp = SPEC["core"].setdefault("spacing", {})
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--space-(\d+(?:_\d+)?)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v:
        sp[_m.group(1).replace("_", ".")] = {"value": _v, "type": "dimension",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared space {_m.group(1).replace('_', '.')}."}

# Declared border widths: --borderWidth-0..500.
bw = SPEC["core"].setdefault("borderWidth", {})
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--borderWidth-(\d+)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v:
        bw[_m.group(1)] = {"value": _v, "type": "dimension",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared borderWidth {_m.group(1)}."}

# Motion: CDS declares no motion vars on the theme element. The measured
# CTA/nav controls all declare 0s transitions (no motion); the real
# animated chrome is the promo banner, the explore search field and the
# mobile menu link at 0.2s ease-in-out.
for key, cname, prop, desc in [
    ("ui", "promo-banner", "transitionDuration", "The measured promo-banner link transition — the real UI motion at 0.2s."),
    ("search", "explore-search", "transitionDuration", "The measured explore-search transition (0.2s)."),
]:
    try:
        v = stprop(cname, "default", prop)
        if v and v != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
                "value": v.split(",")[0].strip(), "type": "duration",
                "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass
for key, cname, desc in [
    ("ui", "promo-banner", "The ease-in-out curve on the animated chrome (promo banner, search, menu links)."),
]:
    try:
        v = stprop(cname, "default", "transitionTimingFunction")
        m = re.search(r"cubic-bezier\([^)]+\)", v or "")
        pick = m.group(0) if m else (v or "").strip().split(",")[0].strip()
        if pick and pick != "0s":
            SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
                "value": pick, "type": "cubicBezier",
                "source": f"computed transitionTimingFunction of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Declared icon/avatar/control sizes.
for _fam, _out in (("iconSize", "iconSize"), ("avatarSize", "avatarSize"), ("controlSize", "controlSize")):
    for _name in sorted(LIGHT_VARS):
        _m = re.fullmatch(rf"--{_fam}-(\w+)", _name)
        if not _m:
            continue
        _v = tvar(_name)
        if _v:
            SPEC["core"].setdefault(_out, {})[_m.group(1)] = {"value": _v, "type": "dimension",
                "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
                "description": f"Declared {_fam} {_m.group(1)}."}

# Measured chrome layers: nav z-index and content measure.
for key, cname, prop, desc in [
    ("nav", "header", "zIndex", "The fixed header's stacking order."),
]:
    try:
        v = stprop(cname, "default", prop)
        if v and v != "auto":
            SPEC["core"].setdefault("z", {})[key] = {
                "value": v, "type": "number",
                "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass
for key, cname, desc in [
    ("content", "hero-title", "The hero column's measure — the widest content element."),
]:
    try:
        v = stprop(cname, "default", "width")
        if v:
            SPEC["core"].setdefault("layout", {}).setdefault("maxWidth", {})[key] = {
                "value": v, "type": "dimension",
                "source": f"computed width of {cname} default (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# Type: the CDS per-variant scales ship as --fontSize-*/--fontWeight-*/
# --lineHeight-*/--textTransform-*/--fontFamily-* over the 15 text variants
# (display1-4, title1-5, headline, body, label1-3, caption, legal) plus the
# cdx* display mirror. Emit the family faces and the whole size/weight
# ladder.
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--fontSize-(\w+)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v and re.fullmatch(r"-?[\d.]+(px|rem)", _v):
        SPEC["core"].setdefault("fontSize", {})[_m.group(1)] = {
            "value": _v, "type": "dimension",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared fontSize {_m.group(1)}."}
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--fontWeight-(\w+)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v and re.fullmatch(r"\d+", _v):
        SPEC["core"].setdefault("fontWeight", {})[_m.group(1)] = {
            "value": _v, "type": "fontWeight",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared fontWeight {_m.group(1)}."}
for _name in sorted(LIGHT_VARS):
    _m = re.fullmatch(r"--lineHeight-(\w+)", _name)
    if not _m:
        continue
    _v = tvar(_name)
    if _v and re.fullmatch(r"-?[\d.]+(px|rem|%)?", _v):
        SPEC["core"].setdefault("lineHeight", {})[_m.group(1)] = {
            "value": _v, "type": "dimension" if _v.endswith(("px","rem")) else "number",
            "source": f"declared {_name} on div.coinbase.light (raw/css-vars.json themes)",
            "description": f"Declared lineHeight {_m.group(1)}."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Sign-up pill."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav links."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The hero CTA pill."),
    ("control.heightMenuButton", "m-menu-button", "default", "height", "The mobile menu toggle."),
    ("control.heightOAuth", "signin-oauth", "default", "height", "The sign-in OAuth row."),
    ("control.heightChip", "chip", "default", "height", "A filter chip."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "CTA-pill corner radius."),
    ("banner.height", "promo-banner", "default", "height", "The promo banner row."),
    ("nav.height", "header", "default", "height", "The fixed header at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.width", "m-menu-open", "default", "width", "The mobile menu overlay at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure."),
    ("row.heightPrice", "price-row", "default", "height", "A price-table row at 1440px."),
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
# Families are the CDS stacks: --cds-font-display/-sans/-text/-mono/
# -condensed at :root, referenced per-variant by --fontFamily-* on the theme
# element. Measured display sizes sit beside the declared fontSize ladder.

font = SPEC["core"].setdefault("font", {})
for key, var, desc in [
    ("display", "--cds-font-display", "Declared --cds-font-display: CoinbaseDisplay + system fallbacks — the display face."),
    ("sans", "--cds-font-sans", "Declared --cds-font-sans: CoinbaseSans + system fallbacks — the UI face."),
    ("text", "--cds-font-text", "Declared --cds-font-text: CoinbaseText + system fallbacks — the body face."),
    ("mono", "--cds-font-mono", "Declared --cds-font-mono: CoinbaseMono + system fallbacks — the code face."),
    ("condensed", "--cds-font-condensed", "Declared --cds-font-condensed: CoinbaseCondensed + system fallbacks — the condensed face."),
]:
    v = R.get(var)
    if v:
        font.setdefault("family", {})[key] = {"type": "fontFamily", "value": v.replace("'", '"'),
            "source": f"declared {var} at :root (raw/css-vars.json resolved)",
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
    ("hero", "hero-title", "The hero display headline at 1440px."),
    ("h1Explore", "explore-title", "The explore headline."),
    ("h2", "section-title", "Section headings."),
    ("mHero", "m-hero", "The hero headline at 390px."),
    ("nav", "nav-item", "Nav labels."),
    ("footer", "footer-link", "Footer links."),
    ("banner", "promo-banner", "The promo banner line."),
    ("price", "price-figure", "A price-table figure."),
    ("cta", "hero-cta", "CTA pill labels."),
    ("signin", "signin-oauth", "The sign-in OAuth row label."),
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
