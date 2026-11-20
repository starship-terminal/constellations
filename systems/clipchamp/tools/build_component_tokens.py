"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

clipchamp.com is a Microsoft React/Fluent-UI build: the page carries TWO
declared token layers — the marketing sheet's own `--color-*` ramps
(the purple brand ramp, blue and pink accents, the grey ink steps,
link roles and social colours) and a full Fluent v9 layer on
`fui-FluentProvider` (colorBrand*/colorNeutral*, the borderRadius*,
spacing*, duration*, curve*, shadowN*, fontSize*/fontWeight*/lineHeight*
scales, fontFamilyBase = Segoe UI) — plus the site's --font-segoe and
friends for the language-specific faces. Every role below is still
measured on the painted chrome and cited back to
raw/components-computed.json — declarations say what Clipchamp named, the
measurements say what it paints.

The site paints ONE light theme; dark content bands exist inside it.
app.clipchamp.com/login is a separate app surface (the sign-in boundary),
measured at rest and never submitted.

The declared palette (marketing layer):

  purple    #6453e4 brand (purple-80 = Fluent colorBrandBackground) ->
            #4d43de hover (purple-70), #433ac7 pressed (purple-60),
            #f3f0ff tint (purple-160)
  blue      #3a5af4 accent-2 (blue-80) -> #242da0 deep (blue-50),
            #8893ff light (blue-110), #dee2ff tint (blue-150)
  pink      #b50ac1 accent-1 (pink-80) -> #6e006c deep (pink-50),
            #e560ff light (pink-110), #f6d9ff tint (pink-150)
  grey      #313242 primary ink (grey-20) -> #2c2d3c (grey-18),
            #64647c muted (grey-40), #6e6e86 (grey-44)
  offwhite  #fbfbfc secondary ground; links: purple-70 inactive ->
            purple-60 hover
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# clipchamp paints light only (catalog theme list), so declarations resolve against the light pass; a dark
# probe added by a recapture must not silently become the light values.
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
# The Fluent v9 layer declares on .fui-FluentProvider (not :root), so its
# names never reach `resolved`: read their static declarations from the
# harvested app rules. Marketing-layer names stay resolved.
for _r in V.get("app", []):
    if "FluentProvider" in (_r.get("selector") or ""):
        for _n, _val in _r.get("properties", {}).items():
            R.setdefault(_n, _val)

# The Webflow sheet declares the whole ramp, so core names follow the
# declaration: declared leaves resolve through R (the var name stays the
# provenance). The few core shades the site paints without declaring
# (the #1b1bbc hover step lives under a deleted variable, the #101010
# focus ring is a UA colour) are measured leaves cited to the component.
#   (token path, declared var name OR component tuple, description)
DECLARED = [
    ("purple.60", "--color-purple-60", "Declared purple-60 (#433ac7) — brand-dark, the pressed/hover-deep step and hover link colour."),
    ("purple.70", "--color-purple-70", "Declared purple-70 (#4d43de) — brand-light, the hover step and inactive link colour."),
    ("purple.80", "--color-purple-80", "Declared purple-80 (#6453e4) — the brand purple: primary CTAs, logo mark, Fluent colorBrandBackground."),
    ("purple.160", "--color-purple-160", "Declared purple-160 (#f3f0ff) — brand-background, the purple tint wash."),
    ("blue.50", "--color-blue-50", "Declared blue-50 (#242da0) — accent-2 dark."),
    ("blue.80", "--color-blue-80", "Declared blue-80 (#3a5af4) — accent-2 standard, the second brand family."),
    ("blue.110", "--color-blue-110", "Declared blue-110 (#8893ff) — accent-2 light."),
    ("blue.150", "--color-blue-150", "Declared blue-150 (#dee2ff) — accent-2 background tint."),
    ("pink.50", "--color-pink-50", "Declared pink-50 (#6e006c) — accent-1 dark."),
    ("pink.80", "--color-pink-80", "Declared pink-80 (#b50ac1) — accent-1 standard."),
    ("pink.110", "--color-pink-110", "Declared pink-110 (#e560ff) — accent-1 light."),
    ("pink.150", "--color-pink-150", "Declared pink-150 (#f6d9ff) — accent-1 background tint."),
    ("grey.18", "--color-grey-18", "Declared grey-18 (#2c2d3c) — the deepest ink."),
    ("grey.20", "--color-grey-20", "Declared grey-20 (#313242) — color-text-dark, the primary ink."),
    ("grey.40", "--color-grey-40", "Declared grey-40 (#64647c) — color-text-light, muted text."),
    ("grey.44", "--color-grey-44", "Declared grey-44 (#6e6e86) — the lightest grey step."),
    ("offWhite", "--color-background-off-white", "Declared off-white (#fbfbfc) — the secondary page ground."),
    ("collapsible.header", "--color-collapsible-header", "Declared collapsible-header (#5d6276) — FAQ header ink."),
    ("collapsible.content", "--color-collapsible-content", "Declared collapsible-content (#1c1c26b3) — FAQ body ink at alpha."),
]
CORE = []
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. clipchamp.com "
    "declares TWO token layers: its own --color-* marketing ramps and a "
    "full Fluent v9 set on fui-FluentProvider (raw/css-vars.json). The "
    "core ramps below are the marketing layer's declared values; the "
    "Fluent layer's brand colour is the same purple. Semantic roles are "
    "measured on the painted chrome in raw/components-computed.json and "
    "alias the core when the value matches. One theme exists (light); "
    "dark content bands live inside it."),
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
# measured on the painted chrome (header, hero cards, plan carousel, search
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
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
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
for path, var, desc in DECLARED:
    v = R.get(var)
    if not v:
        raise SystemExit(f"declared var missing: {var}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": norm_color(v), "type": "color",
                  "source": f"declared {var} (raw/css-vars.json)",
                  "description": desc}
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
    # ----- the single light surface (marketing routes, footer)
    ("light:surface.page", "page-ground", "default", "backgroundColor", "The page ground — painted by the body."),
    ("light:text.primary", "section-title", "default", "color", "The primary ink (declared --color-text-dark = grey-20 #313242)."),
    ("light:text.muted", "feature-cell", "default", "color", "Muted text (declared --color-text-light = grey-40 #64647c)."),
    ("light:text.nav", "nav-item", "default", "color", "The nav-item ink at rest — lighter than body ink."),
    ("light:text.onAccent", "nav-cta", "default", "color", "White text on the purple controls."),
    ("light:text.link", "inline-link", "default", "color", "Link ink at rest (declared --color-inactive-links = purple-70)."),
    ("light:text.linkHover", "inline-link", "hover", "color", "Link ink on hover (declared --color-hover-links = purple-60)."),
    ("light:accent", "nav-cta", "default", "backgroundColor", "The brand purple where a solid fill shows (declared --color-brand-standard = purple-80 #6453e4 = Fluent colorBrandBackground)."),
    ("light:accentHover", "cta-secondary", "hover", "backgroundColor", "The hover fill on the solid-purple controls (#4d43de = purple-70)."),
    ("light:border.subtle", "header", "default", "paint.0.border", "The hairline under the sticky header."),
    ("light:border.outlineCta", "cta-secondary", "default", "borderTopColor", "The outline button's border colour."),
    ("light:focus", "nav-cta", "focus-visible", "outlineColor", "The focus ring on the surface's controls (Fluent colorStrokeFocus2 = #000000)."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# surface.offWhite is declared (--color-background-off-white #fbfbfc, the
# secondary band ground) but no measured component's own backgroundColor
# reads it — cards are white. The dark band is painted by a section wrapper
# no capture measured (the ContentBlockDark element itself is transparent),
# so its fill is a pixel sample: labelled Sampled and kept out of the light
# semantic set (docs/EVIDENCE.md), under core.sampled.
SPEC["light"]["surface"]["offWhite"] = {
    "type": "color", "value": "{color.offWhite}",
    "source": "declared --color-background-off-white (raw/css-vars.json); the secondary band ground — sections only, no component's bg reads it",
    "description": "The off-white secondary band ground (#fbfbfc)."}
SPEC["core"].setdefault("sampled", {})["surfaceDark"] = {
    "type": "color", "value": "{color.grey.20}",
    "source": "Sampled: a screenshot pixel of the full-colour home capture (kept outside the repo) at (720, 3520), not a reading of any element; the band's own element is transparent and the section wrapper that paints it was not measured; the sample equals declared --color-grey-20",
    "description": "The dark content band's fill inside the single light theme (#313242 = grey-20), from a pixel sample."}

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

# The surface's one tokenised painted elevation (Fluent declares shadow2..shadow64,
# several near-identical steps, so the measured shadow is kept verbatim). The first
# component in this list that paints a shadow supplies it, and the token is named for
# that component: on this capture the nav dropdown paints none, so the feature card's
# shadow is the one read, and it is light.shadow.card, not a menu shadow.
SHADOW_ROLE = {"nav-submenu": "menu", "feature-card": "card", "faq-item": "faq"}
for _cname in ("nav-submenu", "feature-card", "faq-item"):
    try:
        _sh = stprop(_cname, "default", "boxShadow") or ""
        if _sh and _sh != "none":
            _layers = []
            for _ly in re.split(r",(?![^(]*\))", _sh):
                m = re.fullmatch(
                    r"\s*(rgb[a]?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?\s*",
                    _ly)
                if not m:
                    # A layer that cannot be read refuses the build instead of being dropped.
                    raise SystemExit(f"build_component_tokens: cannot read {_cname} box-shadow layer {_ly!r}")
                _layers.append({"color": m.group(1), "offsetX": m.group(2) + "px",
                                "offsetY": m.group(3) + "px", "blur": m.group(4) + "px",
                                "spread": m.group(5) + "px"})
                if m.group(6):
                    _layers[-1]["inset"] = True
            SPEC["light"]["shadow"] = {SHADOW_ROLE[_cname]: {
                "type": "shadow", "value": _layers,
                "source": f"computed boxShadow of {_cname} default (raw/components-computed.json)",
                "description": f"The {_cname}'s drop shadow — the surface's painted elevation."}}
            # Only a component that paints a shadow ends the search; one reading "none" falls through.
            break
    except KeyError:
        continue

# Declared radii: the Fluent layer ships the full scale (None 0, Small 2,
# Medium 4, Large 6, XLarge 8, Circular 10000).
rad = SPEC["core"].setdefault("radius", {})
for key, var, desc in [
    ("small", "--borderRadiusSmall", "Fluent borderRadiusSmall (2px)."),
    ("medium", "--borderRadiusMedium", "Fluent borderRadiusMedium (4px) — buttons, cards."),
    ("large", "--borderRadiusLarge", "Fluent borderRadiusLarge (6px)."),
    ("xlarge", "--borderRadiusXLarge", "Fluent borderRadiusXLarge (8px)."),
    ("circular", "--borderRadiusCircular", "Fluent borderRadiusCircular (10000px) — the pill cap."),
]:
    v = R.get(var)
    if v:
        rad[key] = {"value": v, "type": "dimension",
                    "source": f"declared {var} (raw/css-vars.json)",
                    "description": desc}

# Fluent motion: the duration and curve scales are declared on the provider.
for key, var in [
    ("ultraFast", "--durationUltraFast"), ("faster", "--durationFaster"),
    ("fast", "--durationFast"), ("normal", "--durationNormal"),
    ("gentle", "--durationGentle"), ("slow", "--durationSlow"),
    ("slower", "--durationSlower"), ("ultraSlow", "--durationUltraSlow"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("duration", {})[key] = {
            "value": v, "type": "duration",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Fluent {var[2:]}."}
for key, var in [
    ("linear", "--curveLinear"), ("easyEase", "--curveEasyEase"),
    ("easyEaseMax", "--curveEasyEaseMax"),
    ("accelerateMin", "--curveAccelerateMin"), ("accelerateMid", "--curveAccelerateMid"),
    ("accelerateMax", "--curveAccelerateMax"),
    ("decelerateMin", "--curveDecelerateMin"), ("decelerateMid", "--curveDecelerateMid"),
    ("decelerateMax", "--curveDecelerateMax"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("motion", {}).setdefault("curve", {})[key] = {
            "value": v, "type": "cubicBezier",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Fluent {var[2:]}."}

# Fluent spacing scale (declared on the provider).
for key, var in [
    ("none", "--spacingHorizontalNone"), ("xxs", "--spacingHorizontalXXS"),
    ("xs", "--spacingHorizontalXS"), ("snudge", "--spacingHorizontalSNudge"),
    ("s", "--spacingHorizontalS"), ("mnudge", "--spacingHorizontalMNudge"),
    ("m", "--spacingHorizontalM"), ("l", "--spacingHorizontalL"),
    ("xl", "--spacingHorizontalXL"), ("xxl", "--spacingHorizontalXXL"),
    ("xxxl", "--spacingHorizontalXXXL"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("spacing", {})[key] = {
            "value": v, "type": "dimension",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Fluent {var[2:]} (the horizontal ladder; the vertical ladder matches)."}

# Fluent type scale: sizes, weights and line-heights are all declared.
for key, var in [
    ("100", "--fontSizeBase100"), ("200", "--fontSizeBase200"),
    ("300", "--fontSizeBase300"), ("400", "--fontSizeBase400"),
    ("500", "--fontSizeBase500"), ("600", "--fontSizeBase600"),
    ("h700", "--fontSizeHero700"), ("h800", "--fontSizeHero800"),
    ("h900", "--fontSizeHero900"), ("h1000", "--fontSizeHero1000"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("fontSize", {})[key] = {
            "value": v, "type": "dimension",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Fluent {var[2:]}."}
for key, var in [
    ("regular", "--fontWeightRegular"), ("medium", "--fontWeightMedium"),
    ("semibold", "--fontWeightSemibold"), ("bold", "--fontWeightBold"),
]:
    v = R.get(var)
    if v:
        SPEC["core"].setdefault("fontWeight", {})[key] = {
            "value": int(v), "type": "fontWeight",
            "source": f"declared {var} (raw/css-vars.json)",
            "description": f"Fluent {var[2:]}."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Try-for-free button."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav menu triggers."),
    ("control.heightHeroCta", "hero-cta", "default", "height", "The hero Create-a-video button."),
    ("control.heightOutlineCta", "cta-secondary", "default", "height", "The outline secondary button."),
    ("control.radiusCta", "nav-cta", "default", "borderTopLeftRadius", "Button corner radius."),
    ("card.radiusLink", "feature-card", "default", "borderTopLeftRadius", "Feature link-card corners."),
    ("nav.height", "header", "default", "height", "The sticky nav bar at 1440px (declared --header-height 3.75rem = 60px)."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.width", "m-menu-open", "default", "width", "The mobile side-bar drawer at 390px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero headline's measure."),
    ("table.width", "plan-table", "default", "width", "The pricing comparison table at 1440px."),
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
# Families are declared (--fontFamilyBase = Segoe UI on the provider;
# --font-segoe/--font-kinto-sans and the language faces on the marketing
# layer); the measured display sizes on headings are kept beside the
# declared Fluent scale.

font = SPEC["core"].setdefault("font", {})
_v = R.get("--fontFamilyBase")
if _v:
    font.setdefault("family", {})["ui"] = {"type": "fontFamily", "value": _v.replace("'", '"'),
        "source": "declared --fontFamilyBase (raw/css-vars.json)",
        "description": "Segoe UI stack — the declared Fluent base family."}
_v = R.get("--font-segoe")
if _v:
    font.setdefault("family", {})["segoe"] = {"type": "fontFamily", "value": _v.replace("'", '"'),
        "source": "declared --font-segoe (raw/css-vars.json)",
        "description": "The site's own Segoe webfont alias."}
for key, cname, prop, desc in [
    ("family.display", "hero-title", "fontFamily", "The display face on the hero headline."),
]:
    try:
        f = (stprop(cname, "default", prop) or stprop(cname, "default", "textStyle.fontFamily") or "").strip()
        if f:
            font.setdefault("family", {})[key.split(".")[-1]] = {"type": "fontFamily", "value": f,
                                        "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

for key, cname, desc in [
    ("size.hero", "hero-title", "The hero display headline at 1440px."),
    ("size.h2", "section-title", "Section headings."),
    ("size.mHero", "m-hero", "The hero headline at 390px."),
    ("size.nav", "nav-item", "Nav labels and buttons."),
    ("size.footer", "footer-link", "Footer links."),
    ("size.subtitle", "hero-subtitle", "The hero subline."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            font.setdefault("size", {})[key.split(".")[-1]] = {"type": "dimension", "value": sz,
                                        "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
