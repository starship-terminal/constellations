#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

glassnode.com is five public surfaces signed out, each declaring a real
design-token layer in its stylesheets (raw/css-vars.json):

  marketing (glassnode.com/...)   a Next.js + SCSS-modules site on :root:
      --base_grey_*/--base_ultramarine_*   the brand palette steps
      --light_*                            the light semantic roles
      --grey_*/--light_util_grey_*         a second grey ramp + utility steps
      --accent_80, --error*, --section-bg-dark, --vector-*
      --button-*, --light-text-link*
      --space-*, --screen_*, --nav-height-*, --px-*, --section-py-*,
      --grid-width, --form-width, --footer-height, --shadow-*,
      --transition_*, --z_index_*, --font-family, --font_size_base
      Painted light only — dark in-page sections, no global theme.
  studio (studio.glassnode.com)   the React product shell on TWO scopes:
      :root --gds-*          the Glassnode Design System: --gds-color-*
                             palette + semantic roles (background/content/
                             border/button/link/tag/chart/...), --gds-font-*,
                             --gds-spacing-*, --gds-border-radius-*/,
                             --gds-shadow-*, --gds-zindex-*, --gds-opacity-*,
                             --gds-page-width-*, --gds-navbar-height,
                             --gds-sidebar-width
      html[data-theme="dark-theme"]   a real dark redeclaration of the same
                             --gds-* roles plus Ant Design --ant-* component
                             vars. Declared but NOT publicly reachable: no
                             public theme control exists on the signed-out
                             shell, so the dark set is labelled
                             declared-not-painted.
  research (research.glassnode.com)  a Ghost publication on two scopes:
      :root/[data-theme="light"]   the --rf-* theme roles, the --gds-*
                             palette primitives it shares with studio, and
                             the Ghost --color-*/--font-*/--container-* layer
      default (no data-theme)      the dark --rf-* redeclaration — painted by
                             the "Switch to dark mode" toggle.
  docs (docs.glassnode.com)       a GitBook site — the GitBook platform's own
                             token layer (RGB-triplet ramps, --text-*/--radius-*
                             Tailwind names, --font-content Roboto). Kept out
                             of the token tree like the other third-party
                             stacks; its measured values land under
                             component.docs.*.
  tokenization (tokenization.glassnode.com)  a dark-by-default registry app:
      [data-theme="dark"]/:root    --color-* roles, --c1--c7 chart palette,
                             --container-*, --font-*, --radius-*, --shadow*
      [data-theme="light"]         the light redeclaration, painted by the
                             "Switch to light theme" button.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# Resolved declarations per surface/theme profile.
R = {p: {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v)
         for n, v in prof.items()} for p, prof in RES.items()}


def var(name, profile, ty="color", **kw):
    d = {"var": name, "profile": profile, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. glassnode.com's "
    "public surfaces are five stacks: the marketing site's --base_*/--light_* "
    "layer (palette.* and light.theme.*), the studio shell's declared --gds-* "
    "design system in light and dark scopes (light.studio.* and "
    "dark.studio.* — the dark scope is declared but has no public theme "
    "control, so it is labelled declared-not-painted), the Ghost research "
    "publication's --rf-* roles in both painted themes (light.research.* and "
    "dark.research.*), the tokenization registry's --color-* roles "
    "(dark.tokenization.* painted by default, light.tokenization.* via the "
    "theme button), and the type/space/radius/shadow/layout scales under "
    "core.*. The GitBook docs stack stays outside the token tree; its "
    "measured values are component.docs.*. Measured roles alias the declared "
    "values they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        return t.get(prop) or c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}
_OWNER = {}


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit_at(root, path, leaf, name=None):
    node = root
    parts = path.split(".")
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        prefix = ".".join(parts[:i + 1])
        if nxt is None:
            nxt = node[p] = {}
        elif _leaf(nxt):
            owner = _OWNER.pop(prefix, None)
            nxt = node[p] = {"default": nxt}
            if owner:
                EMITTED[owner] = prefix + ".default"
                _OWNER[prefix + ".default"] = owner
        node = nxt
    last = parts[-1]
    full = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                full += "." + key
                break
        else:
            raise ValueError(f"{path}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{path}: duplicate token path")
        node[last] = leaf
    if name:
        EMITTED[name] = full
        _OWNER[full] = name


def decl_src(profile):
    return f"declared design-system variable in the {profile} stylesheets (raw/css-vars.json)"


def declared(name, profile):
    v = R.get(profile, {}).get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


COLOR_V = re.compile(r"^(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))$")
DIM_V = re.compile(r"^-?\d+(\.\d+)?(px|rem)$")


def tyof(v):
    v = str(v or "").strip()
    if COLOR_V.fullmatch(v):
        return "color"
    if DIM_V.fullmatch(v):
        return "dimension"
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        return "number"
    if re.fullmatch(r"cubic-bezier\([^)]*\)", v):
        return "cubicBezier"
    if re.fullmatch(r"\d+(\.\d+)?m?s", v):
        return "duration"
    if re.fullmatch(r"rgba?\([^)]*\)[^)]*inset", v) or re.fullmatch(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))\s+-?[\d.]+px.*", v):
        return "shadow"
    return "other"


def emit_group(root, prefix, names, profile, desc, skip=()):
    """Emit every resolved variable into nested token groups by name parts."""
    for name in sorted(names):
        if name in skip:
            continue
        key = name.lstrip("-").split("-", 1)[-1]  # drop the prefix family
        parts = [p for p in re.split(r"[-_]", key) if p]
        path = ".".join([prefix] + parts)
        v = declared(name, profile)
        emit_at(root, path, var(name, profile, tyof(v), description=desc(name, v)), name)


# =============================================================== core
#
# The GDS palette primitives the studio declares and every other surface
# shares: the grey ramp, ultramarine (the brand blue #4559dc), green/red/
# yellow/rose status ramps, the darken alpha scale and the lone indigo.

pal = SPEC["core"].setdefault("palette", {})
RL = R.get("studioLight", {})
RM = R.get("marketing", {})
for fam, pat in [
    ("grey", r"--gds-color-grey-(\d+)"), ("ultramarine", r"--gds-color-ultramarine-(\d+)"),
    ("green", r"--gds-color-green-(\d+)"), ("red", r"--gds-color-red-(\d+)"),
    ("yellow", r"--gds-color-yellow-(\d+)"), ("rose", r"--gds-color-rose-(\d+)"),
]:
    node = pal.setdefault(fam, {})
    for name in sorted(k for k in RL if re.fullmatch(pat, k)):
        node[re.fullmatch(pat, name).group(1)] = var(
            name, "studioLight", "color",
            description=f"The declared `{name}` palette step — the same ramp the marketing site declares as --base_{fam}_* and research declares as --gds-{fam}-*.")
for name, key, desc in [
    ("--gds-color-indigo-600", "indigo.600", "The lone indigo step."),
    ("--gds-color-black", "black", "Pure black."),
    ("--gds-color-white", "white", "Pure white."),
]:
    if name in RL:
        emit_at(pal, key, var(name, "studioLight", "color", description=f"The declared `{name}` — {desc}"), name)
dk = pal.setdefault("darken", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-color-darken-\d+", k)):
    dk[name.rsplit("-", 1)[1].lstrip("0") or "0"] = var(
        name, "studioLight", "color",
        description=f"The declared `{name}` — a black overlay alpha step.")
for name in sorted(k for k in RM if re.fullmatch(r"--accent_\d+", k)):
    pal["accent"] = var(name, "marketing", "color",
                        description=f"The declared `{name}` — the green accent (#16cc8c family) used on marketing CTAs and the tokenization accent.")
pal.setdefault("vector", {})
for name, key in [("--vector-risk-on", "riskOn"), ("--vector-risk-off", "riskOff")]:
    if name in RM:
        pal["vector"][key] = var(name, "marketing", "color",
            description=f"The declared `{name}` — a Vector risk-gauge colour.")
for name in sorted(k for k in RM if re.fullmatch(r"--grey_\d+", k)):
    emit_at(pal, "greyAlt." + name.rsplit("_", 1)[1], var(name, "marketing", "color",
        description=f"The declared `{name}` — the marketing site's second grey ramp."), name)
for name in sorted(k for k in RM if re.fullmatch(r"--light_util_grey_\d+", k)):
    emit_at(pal, "utilGrey." + name.rsplit("_", 1)[1], var(name, "marketing", "color",
        description=f"The declared `{name}` utility grey step."), name)
# The Ghost publication palette (research.glassnode.com).
gh = pal.setdefault("ghost", {})
RR = R.get("researchLight", {})
for name, key in [("--color-green", "green"), ("--color-red", "red"), ("--color-yellow", "yellow"),
                  ("--color-darkgrey", "darkgrey"), ("--color-midgrey", "midgrey"),
                  ("--color-lightgrey", "lightgrey"), ("--color-wash", "wash"),
                  ("--color-darkmode", "darkmode")]:
    if name in RR:
        gh[key] = var(name, "researchLight", "color",
                      description=f"The declared `{name}` — the Ghost theme's palette step (darkmode is the dark surface's field).")
# The registry's chart palette (tokenization.glassnode.com, dark default).
RT = R.get("tokenizationDark", {})
ch = pal.setdefault("chart", {})
for name in sorted(k for k in RT if re.fullmatch(r"--c(\d|other)$", k)):
    ch[name[len("--c"):].replace("other", "other")] = var(name, "tokenizationDark", "color",
        description=f"The declared `{name}` — a registry chart/series colour.")

# ------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, profile, desc in [
    ("default", "--gds-font-family-default", "studioLight", "Inter Variable + Inter fallbacks — the product shell's family."),
    ("mono", "--gds-font-family-mono", "studioLight", "SF Mono/Monaco/Cascadia Code/Roboto Mono — the product shell's mono."),
    ("marketing", "--font-family", "marketing", "The marketing site's system stack; headings paint the webfont 'fraktion', body 'Inter' (raw/measurements.md)."),
    ("research", "--rf-font", "researchLight", "Inter/Inter Variable — the research publication's family."),
    ("researchSerif", "--font-serif", "researchLight", "Georgia/Times — the Ghost serif."),
    ("researchMono", "--font-mono", "researchLight", "Menlo/Courier — the Ghost mono."),
    ("tokenization", "--font-sans", "tokenizationDark", "Inter — the registry's family."),
    ("tokenizationMono", "--font-mono", "tokenizationDark", "JetBrains Mono — the registry's mono."),
    ("docs", "--font-content", "docsLight", "Roboto — the GitBook docs platform's family."),
    ("docsMono", "--font-mono", "docsLight", "IBM Plex Mono — the docs' mono."),
]:
    if name in R.get(profile, {}):
        fam[key] = var(name, profile, "fontFamily", description=desc)

weights = SPEC["core"]["font"].setdefault("weight", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-font-weight-[a-z]+", k)):
    w = RL[name]
    try:
        w = int(w)
    except (TypeError, ValueError):
        pass
    weights[name.rsplit("-", 1)[1]] = lit(w if isinstance(w, int) else RL[name], "fontWeight" if isinstance(w, int) else "other",
        f"{decl_src('studioLight')}: {name}", f"The declared `{name}`.")
for name in sorted(k for k in RT if re.fullmatch(r"--font-weight-[a-z]+", k)):
    w = RT[name]
    try:
        w = int(w)
    except (TypeError, ValueError):
        pass
    emit_at(weights, "tokenization." + name.rsplit("-", 1)[1], lit(w if isinstance(w, int) else RT[name],
        "fontWeight" if isinstance(w, int) else "other", f"{decl_src('tokenizationDark')}: {name}", f"The declared `{name}` (registry)."), name)

sizes = SPEC["core"]["font"].setdefault("size", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-font-size-\d+", k)):
    sizes[name.rsplit("-", 1)[1]] = var(name, "studioLight", "dimension",
        description=f"The declared `{name}` — the GDS type ramp step ({RL[name]}).")
if declared("--font_size_base", "marketing"):
    emit_at(sizes, "marketing.base", var("--font_size_base", "marketing", "dimension",
        description="The marketing site's declared base size."), "--font_size_base")

lh = SPEC["core"]["font"].setdefault("lineHeight", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-line-height-\d+|--gds-line-height-default", k)):
    key = name.replace("--gds-line-height-", "")
    v = RL[name]
    lh[key] = lit(float(v) if re.fullmatch(r"-?\d+(\.\d+)?", str(v)) else v, "number" if re.fullmatch(r"-?\d+(\.\d+)?", str(v)) else "other",
        f"{decl_src('studioLight')}: {name}", f"The declared `{name}`.")
for name in sorted(k for k in RT if re.fullmatch(r"--leading-[a-z]+", k)):
    v = RT[name]
    emit_at(lh, "tokenization." + name.replace("--leading-", ""), lit(float(v) if re.fullmatch(r"-?\d+(\.\d+)?", str(v)) else v,
        "number" if re.fullmatch(r"-?\d+(\.\d+)?", str(v)) else "other", f"{decl_src('tokenizationDark')}: {name}", f"The declared `{name}` (registry)."), name)

tr = SPEC["core"]["font"].setdefault("tracking", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-letter-spacing-[a-z0-9-]+", k)):
    key = name.replace("--gds-letter-spacing-", "")
    v = RL[name]
    tr[key] = lit(v, "dimension" if DIM_V.fullmatch(str(v)) else "other", f"{decl_src('studioLight')}: {name}", f"The declared `{name}`.")

# ---------------------------------------------------------- core scales

spacing = SPEC["core"].setdefault("spacing", {})
for name in sorted(k for k in RM if re.fullmatch(r"--space-\d+", k)):
    key = name[len("--space-"):]
    spacing[key] = var(name, "marketing", "dimension",
        description=f"The declared `{name}` ({RM[name]}) — the shared 4px-based space ramp the studio redeclares as --gds-spacing-{key}.")
if declared("--spacing", "tokenizationDark"):
    spacing["base"] = var("--spacing", "tokenizationDark", "dimension",
        description="The declared `--spacing` base — 4px; the registry's space unit.")

radii = SPEC["core"].setdefault("radius", {})
radius_alias = {}
for name in sorted(k for k in RL if re.fullmatch(r"--gds-border-radius-\d+|--gds-border-radius-(full|none)", k)):
    key = name.replace("--gds-border-radius-", "")
    v = RL[name]
    radii[key] = lit(v, "dimension" if DIM_V.fullmatch(str(v)) else "other",
        f"{decl_src('studioLight')}: {name}", f"The declared `{name}` ({v}).")
    radius_alias[str(v)] = key
for name in sorted(k for k in RT if re.fullmatch(r"--radius-(md|lg)", k)):
    emit_at(radii, "tokenization." + name.replace("--radius-", ""), lit(RT[name], "dimension",
        f"{decl_src('tokenizationDark')}: {name}", f"The declared `{name}` (registry)."), name)

bord = SPEC["core"].setdefault("border", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-border-width-\d+", k)):
    bord.setdefault("width", {})[name.rsplit("-", 1)[1]] = lit(RL[name], "dimension",
        f"{decl_src('studioLight')}: {name}", f"The declared `{name}`.")

layout = SPEC["core"].setdefault("layout", {})
for name, path, profile, desc in [
    ("--grid-width", "gridWidth", "marketing", "The marketing content grid width."),
    ("--form-width", "formWidth", "marketing", "The marketing form column width."),
    ("--footer-height", "footerHeight", "marketing", "The marketing footer height."),
    ("--nav-height-desktop", "navHeight.desktop", "marketing", "The marketing header height on desktop."),
    ("--nav-height-mobile", "navHeight.mobile", "marketing", "The marketing header height on phones."),
    ("--px-desktop", "gutter.desktop", "marketing", "The marketing page gutter on desktop."),
    ("--px-mobile", "gutter.mobile", "marketing", "The marketing page gutter on phones."),
    ("--section-py-desktop", "sectionPy.desktop", "marketing", "The marketing section vertical rhythm on desktop."),
    ("--section-py-mobile", "sectionPy.mobile", "marketing", "The marketing section vertical rhythm on phones."),
    ("--gds-navbar-height", "studio.navbarHeight", "studioLight", "The product shell's navbar height."),
    ("--gds-sidebar-width", "studio.sidebarWidth", "studioLight", "The product shell's sidebar width."),
    ("--gds-page-width-default", "studio.pageWidth.default", "studioLight", "The product shell's default page width."),
    ("--gds-page-width-narrow", "studio.pageWidth.narrow", "studioLight", "The product shell's narrow page width."),
    ("--gds-page-width-wide", "studio.pageWidth.wide", "studioLight", "The product shell's wide page width."),
    ("--container-primary", "research.container.primary", "researchLight", "The Ghost container width."),
    ("--container-article", "research.container.article", "researchLight", "The Ghost article measure."),
    ("--rf-container", "research.container.rf", "researchLight", "The research theme's container width."),
    ("--rf-prose-w", "research.proseWidth", "researchLight", "The research theme's prose measure."),
    ("--container-md", "tokenization.container.md", "tokenizationDark", "The registry's md container step."),
    ("--container-xl", "tokenization.container.xl", "tokenizationDark", "The registry's xl container step."),
    ("--container-2xl", "tokenization.container.2xl", "tokenizationDark", "The registry's 2xl container step."),
    ("--container-3xl", "tokenization.container.3xl", "tokenizationDark", "The registry's 3xl container step."),
    ("--container-4xl", "tokenization.container.4xl", "tokenizationDark", "The registry's 4xl container step."),
    ("--ai-chat-width", "docs.aiChatWidth", "docsLight", "The GitBook AI-chat pane width."),
]:
    if name in R.get(profile, {}):
        v = R[profile][name]
        emit_at(layout, path, lit(v, "dimension" if DIM_V.fullmatch(str(v)) else "other",
            f"{decl_src(profile)}: {name}", f"The declared `{name}` — {desc}"), name)

bp = SPEC["core"].setdefault("breakpoint", {})
for name in sorted(k for k in RM if re.fullmatch(r"--screen_\w+", k)):
    bp[name[len("--screen_"):]] = var(name, "marketing", "dimension",
        description=f"The declared `{name}` breakpoint ({RM[name]}).")

def shadow_lit(name, profile):
    raw = declared(name, profile)
    if not raw:
        return None
    layers = []
    for layer in re.split(r"(?<!\d),\s+(?=rgba?\(|#)", str(raw)):
        m = re.fullmatch(
            r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\))\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?", layer.strip())
        if not m:
            return lit(raw, "other", f"{decl_src(profile)}: {name}", f"The declared `{name}` shadow.")
        col, x, y, blur, spread, inset = m.groups()
        d = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
             "blur": f"{blur}px", "spread": f"{spread}px"}
        if inset:
            d["inset"] = True
        layers.append(d)
    return lit(layers, "shadow", f"{decl_src(profile)}: {name}",
               f"The declared `{name}` shadow ({len(layers)} layer{'s' if len(layers) > 1 else ''}).")

elevation = SPEC["core"].setdefault("elevation", {})
for name, path, profile in [
    ("--shadow-low", "marketing.low", "marketing"),
    ("--shadow-cookie-banner", "marketing.cookieBanner", "marketing"),
    ("--shadow-01", "studio.01", "studioLight"),
    ("--shadow-02", "studio.02", "studioLight"),
    ("--shadow-03", "studio.03", "studioLight"),
    ("--gds-shadow-005", "studio.gds005", "studioLight"),
    ("--gds-shadow-01", "studio.gds01", "studioLight"),
    ("--gds-shadow-02", "studio.gds02", "studioLight"),
    ("--gds-border-shadow", "studio.borderShadow", "studioLight"),
    ("--gds-border-inset-shadow", "studio.borderShadowInset", "studioLight"),
    ("--shadow-sm", "tokenization.sm", "tokenizationDark"),
    ("--shadow", "tokenization.default", "tokenizationDark"),
]:
    sl = shadow_lit(name, profile)
    if sl:
        emit_at(elevation, path, sl, name)

zi = SPEC["core"].setdefault("zIndex", {})
for name in sorted(k for k in RM if re.fullmatch(r"--z_index_\w+", k)):
    zi[name[len("--z_index_"):]] = var(name, "marketing", "number", description=f"The declared `{name}`.")
for name in sorted(k for k in RL if re.fullmatch(r"--gds-zindex-[a-z-]+", k)):
    emit_at(zi, "studio." + name[len("--gds-zindex-"):], var(name, "studioLight", "number",
        description=f"The declared `{name}`."), name)

op = SPEC["core"].setdefault("opacity", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-opacity-\d+|--gds-opacity-none", k)):
    op[name[len("--gds-opacity-"):]] = lit(RL[name], "number", f"{decl_src('studioLight')}: {name}", f"The declared `{name}`.")

motion = SPEC["core"].setdefault("motion", {})
for name, path, profile, desc in [
    ("--transition_default", "marketing.default", "marketing", "The marketing control transition shorthand."),
    ("--transition_slow", "marketing.slow", "marketing", "The marketing slow transition shorthand."),
    ("--default-transition-duration", "tokenization.duration", "tokenizationDark", "The registry's transition duration."),
    ("--default-transition-timing-function", "tokenization.easing", "tokenizationDark", "The registry's transition easing."),
    ("--default-transition-duration", "docs.duration", "docsLight", "The docs' transition duration."),
    ("--ease-in-out", "docs.easeInOut", "docsLight", "The docs' ease-in-out."),
]:
    if name in R.get(profile, {}):
        v = R[profile][name]
        ty = "cubicBezier" if re.fullmatch(r"cubic-bezier\([^)]*\)", str(v)) else "duration" if re.fullmatch(r"\d+(\.\d+)?m?s", str(v)) else "other"
        emit_at(motion, path, lit(v, ty, f"{decl_src(profile)}: {name}", f"The declared `{name}` — {desc}"), name)

# ============================================================ light set
#
# Marketing's --light_* semantic roles plus its button/link/section/error
# roles — the painted light theme of every marketing page.

sem0 = SPEC["light"]
th = sem0.setdefault("theme", {})
for name in sorted(k for k in RM if re.fullmatch(r"--light_(bg|text|border)[a-z_]*", k)):
    key = name[len("--light_"):]
    parts = [p for p in key.split("_") if p]
    path = ".".join(parts)
    v = RM[name]
    emit_at(th, path, var(name, "marketing", "color", description=f"The declared `{name}` semantic role ({v})."), name)
for name in sorted(k for k in RM if re.fullmatch(r"--light-text-link[a-z-]*", k)):
    emit_at(th, "text." + name[len("--light-text-"):].replace("-", "."), var(name, "marketing", "color",
        description=f"The declared `{name}` ({RM[name]})."), name)
for name in sorted(k for k in RM if re.fullmatch(r"--button-[a-z-]+", k)):
    emit_at(th, "button." + name[len("--button-"):].replace("-", "."), var(name, "marketing", "color",
        description=f"The declared `{name}` ({RM[name]}) — a marketing button role."), name)
for name, path in [("--section-bg-dark", "section.bgDark"), ("--error", "feedback.error"), ("--error_on_dark", "feedback.errorOnDark")]:
    if name in RM:
        emit_at(th, path, var(name, "marketing", "color",
            description=f"The declared `{name}` ({RM[name]})."), name)

# The studio's light --gds-* roles (the shell's painted light theme) —
# grouped background/content/border/button/link/tag/chart/logo/illustration/
# skeleton plus the focus/overlay/transparent singles.
stG = {"background", "content", "border", "button", "link", "tag", "chart", "logo", "illustration", "skeleton"}
stu = sem0.setdefault("studio", {})
for name in sorted(k for k in RL if re.fullmatch(r"--gds-color-[a-z].*", k)):
    if re.fullmatch(r"--gds-color-(grey|ultramarine|green|red|yellow|rose|darken|indigo)-\d+|--gds-color-(black|white)", name):
        continue  # palette primitives live under core.palette.*
    rest = name[len("--gds-color-"):]
    head, _, tail = rest.partition("-")
    if head in stG and tail:
        path = head + "." + tail.replace("-", ".")
    else:
        path = rest.replace("-", ".")
    emit_at(stu, path, var(name, "studioLight", "color",
        description=f"The declared `{name}` ({RL[name]}) — the product shell's painted light theme."), name)

# The Ghost publication's painted light --rf-* roles (research light theme:
# html[data-theme="light"] plus the :root defaults the toggle repaints).
# A var leaf whose value is a shadow string must be emitted as parsed layers
# (the DTCG shadow type is a list, not a string), via shadow_lit.
def emit_var(root, path, name, profile, desc):
    v = declared(name, profile)
    if tyof(v) == "shadow":
        sl = shadow_lit(name, profile)
        if sl:
            sl["description"] = desc
            emit_at(root, path, sl, name)
            return
        emit_at(root, path, lit(v, "other", f"{decl_src(profile)}: {name}", desc), name)
        return
    emit_at(root, path, var(name, profile, tyof(v), description=desc), name)


res = sem0.setdefault("research", {})
for name in sorted(k for k in RR if re.fullmatch(r"--rf-[a-z0-9-]+", k)):
    if name in ("--rf-container", "--rf-prose-w", "--rf-font"):
        continue  # layout + family under core.*
    key = name[len("--rf-"):].replace("-", ".")
    v = RR[name]
    emit_var(res, key, name, "researchLight",
        f"The declared `{name}` ({v}) — the research site's painted light theme.")
for name, path in [("--ghost-accent-color", "ghostAccent"), ("--color-secondary-text", "secondaryText")]:
    if name in RR:
        emit_at(res, path, var(name, "researchLight", "color",
            description=f"The declared `{name}` ({RR[name]}) on the research publication."), name)

# The registry's light redeclaration — painted by its "Switch to light theme"
# button (screenshots/tokenization-dark-theme-light.png).
tok = sem0.setdefault("tokenization", {})
RTL = R.get("tokenizationLight", {})
for name in sorted(k for k in RTL if re.fullmatch(r"--(color|accent|link|overlay|bad|warn)-[a-z-]+", k)):
    key = name.lstrip("-").replace("-", ".")
    v = RTL[name]
    emit_at(tok, key, var(name, "tokenizationLight", "color",
        description=f"The declared `{name}` ({v}) — the registry's painted light theme."), name)

# ============================================================ dark set
#
# Three painted/declared dark themes, namespaced per surface.

# Studio: html[data-theme="dark-theme"] — DECLARED, never painted publicly
# (no theme control on the signed-out shell). Labelled so on every token.
DSRC = ("declared under html[data-theme=\"dark-theme\"] in the studio stylesheets "
        "(raw/css-vars.json) — DECLARED-NOT-PAINTED: no public theme control exists "
        "on the signed-out shell, so this value is a stylesheet declaration, not a painted page")
RD = R.get("studioDark", {})
stuD = SPEC["dark"].setdefault("studio", {})
for name in sorted(k for k in RD if re.fullmatch(r"--gds-color-[a-z].*", k)):
    if re.fullmatch(r"--gds-color-(grey|ultramarine|green|red|yellow|rose|darken|indigo)-\d+|--gds-color-(black|white)", name):
        continue
    rest = name[len("--gds-color-"):]
    head, _, tail = rest.partition("-")
    path = head + "." + tail.replace("-", ".") if head in stG and tail else rest.replace("-", ".")
    emit_at(stuD, path, {"value": norm_color(RD[name]), "type": "color", "source": f"{DSRC}: {name}",
        "description": f"The dark-theme redeclaration of `{name}` ({RD[name]}) — declared, not painted publicly."}, name)
for name in sorted(k for k in RD if re.fullmatch(r"--ant-[a-z-]+", k)):
    key = name[len("--ant-"):].replace("-", ".")
    v = RD[name]
    ty = tyof(v)
    if ty == "shadow":
        ty = "other"  # a shorthand string, not parsed layers — kept literal
    emit_at(stuD, "ant." + key, {"value": norm_color(v) if COLOR_V.fullmatch(str(v)) else v,
        "type": ty, "source": f"{DSRC}: {name}",
        "description": f"The declared `{name}` Ant Design component variable under the dark theme ({v}) — declared, not painted publicly."}, name)

# Research: the dark --rf-* roles — the painted dark surface the Ghost toggle
# switches to (screenshots/research-home-light-theme-dark.png).
resD = SPEC["dark"].setdefault("research", {})
RRD = R.get("researchDark", {})
for name in sorted(k for k in RRD if re.fullmatch(r"--rf-[a-z0-9-]+", k)):
    if name in ("--rf-container", "--rf-prose-w", "--rf-font"):
        continue
    key = name[len("--rf-"):].replace("-", ".")
    v = RRD[name]
    emit_var(resD, key, name, "researchDark",
        f"The dark redeclaration of `{name}` ({v}) — painted by the research theme toggle.")

# Tokenization: the painted dark default surface.
tokD = SPEC["dark"].setdefault("tokenization", {})
for name in sorted(k for k in RT if re.fullmatch(r"--(color|accent|link|overlay|bad|warn)-[a-z-]+", k)):
    key = name.lstrip("-").replace("-", ".")
    v = RT[name]
    emit_at(tokD, key, var(name, "tokenizationDark", "color",
        description=f"The declared `{name}` ({v}) — the registry's painted dark default."), name)

# ----------------------------------------------------- measured roles

# Map every emitted var leaf to its real token path (as build_tokens.py will
# print it — paths are relative to the set root). core is walked first so a
# colour shared by a palette step and a semantic role aliases the palette.
def _walk_vars(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict):
            if "var" in v:
                yield v["var"], prefix + k
            else:
                yield from _walk_vars(v, prefix + k + ".")


VAR_PATH = {}
for _tree in (SPEC["core"], SPEC["light"]):
    for _vn, _p in _walk_vars(_tree):
        VAR_PATH.setdefault(_vn, _p)

role_alias = {}
for _prof in ("marketing", "studioLight", "researchLight", "tokenizationLight"):
    for _name, _v in R.get(_prof, {}).items():
        _p = VAR_PATH.get(_name)
        if _p and isinstance(_v, str) and COLOR_V.fullmatch(norm_color(_v) or ""):
            role_alias.setdefault(norm_color(_v), _p)


def semcolor(raw, src, desc):
    alias = role_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"].setdefault("measured", {})
DARK_PAINTED = {"tokenization"}  # tokenization.glassnode.com paints dark by default (raw _meta.viewport)
for key, comp, state, prop, group, desc in [
    ("heroInk", "hero-h1", "default", "color", "text", "The hero headline ink — 'Pioneering digital asset market intelligence'."),
    ("navInk", "nav-link", "default", "color", "text", "The header link ink."),
    ("ctaInk", "nav-cta", "default", "color", "action", "The 'Launch Studio' CTA text."),
    ("ctaHover", "nav-cta", "hover", "backgroundColor", "action", "The 'Launch Studio' CTA hover fill."),
    ("ctaFill", "nav-cta", "default", "backgroundColor", "action", "The 'Launch Studio' CTA fill."),
    ("focusRing", "nav-link", "focus-visible", "outlineColor", "border", "The keyboard focus ring on a marketing nav link."),
    ("fieldBg", "newsletter-field", "default", "backgroundColor", "form", "The 'Enter your email' field fill."),
    ("fieldInk", "newsletter-field", "default", "color", "form", "The newsletter field text ink."),
    ("placeholder", "newsletter-field", "default", "placeholder", "form", "The 'Enter your email' placeholder ink."),
    ("submitFill", "newsletter-btn", "default", "backgroundColor", "action", "The 'Send me free research' button fill."),
    ("submitInk", "newsletter-btn", "default", "color", "action", "The subscribe button text."),
    ("studioLoginBg", "st-login-btn", "default", "backgroundColor", "studio", "The studio navbar 'Log in' fill."),
    ("studioSignupFill", "st-signup-btn", "default", "backgroundColor", "studio", "The studio navbar 'Sign up' fill — the product shell's primary action."),
    ("planCardBg", "st-plan-card", "default", "backgroundColor", "studio", "A studio plan card's fill."),
    ("authCardBg", "auth-card", "default", "backgroundColor", "auth", "The Auth0 login card's fill."),
    ("authContinueFill", "auth-continue", "default", "backgroundColor", "auth", "The Auth0 'Continue' submit fill."),
    ("authGoogleFill", "auth-google", "default", "backgroundColor", "auth", "The 'Continue with Google' fill."),
    ("researchCardBg", "res-post-card", "default", "backgroundColor", "research", "A research article card's fill."),
    ("tokNavInk", "tok-nav-item", "default", "color", "tokenization", "The registry nav item ink on the painted dark surface."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        if group in DARK_PAINTED:
            # read on a surface that paints dark (the registry's default): the dark set, never an alias into light roles
            SPEC["dark"].setdefault("measured", {}).setdefault(group, {})[key] = lit(norm_color(raw), "color", src, desc)
        else:
            sem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# ----------------------------------------------------- measured type size

size_alias = {}
for name in sorted(k for k in RL if re.fullmatch(r"--gds-font-size-\d+", k)):
    size_alias.setdefault(str(RL[name]), f"font.size.{name[len('--gds-font-size-'):]}")
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The marketing hero display size."),
    ("section", "section-h2", "default", "A marketing section heading size."),
    ("body", "footer-link", "default", "A footer link's body size."),
    ("studioPlan", "st-h1", "default", "The studio 'Plans & Pricing' heading size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        sizes.setdefault("measured", {})[key] = lit(
            f"{{{alias}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias}" if alias else ""), desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The 'Launch Studio' CTA radius."),
    ("navLink", "nav-link", "default", "borderTopLeftRadius", "The header link radius."),
    ("planCard", "st-plan-card", "default", "borderTopLeftRadius", "A studio plan card's radius."),
    ("field", "newsletter-field", "default", "borderTopLeftRadius", "The newsletter field radius."),
    ("authCard", "auth-card", "default", "borderTopLeftRadius", "The Auth0 card radius."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --gds-border-radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for comp, what in [("nav-cta", "nav CTA"), ("st-login-btn", "studio Log in")]:
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
            durs = [d.strip() for d in dur.split(",")]
            tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", ease or "")
            parts = []
            for i, p in enumerate(props):
                d = durs[i % len(durs)]
                if d == "0s":
                    continue
                parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
            if parts:
                mo["control" + comp.replace("-", " ").title().replace(" ", "")] = lit(", ".join(parts), "other",
                    f"computed transition of {comp} default (raw/components-computed.json)",
                    f"The control transition on the {what}.")
                break
    except KeyError:
        continue

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The 'Launch Studio' CTA height."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("field-height", "newsletter-field", "default", "h", "dimension", "The newsletter field height."),
    ("subscribe-btn-width", "newsletter-btn", "default", "w", "dimension", "The 'Send me free research' button width."),
    ("studio-navbar-height", "st-navbar", "default", "h", "dimension", "The product shell navbar height."),
    ("plan-card-width", "st-plan-card", "default", "w", "dimension", "A studio plan card's column width."),
    ("auth-card-width", "auth-card", "default", "w", "dimension", "The Auth0 login card width."),
    ("research-card-width", "res-post-card", "default", "w", "dimension", "A research article card's width."),
    ("tok-nav-height", "tok-shell", "default", "h", "dimension", "The registry nav height."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# docs.glassnode.com (GitBook) — a different stack that does not share the
# GDS layer; its measured values are kept as literals, honestly labelled.
docs = comp.setdefault("docs", {})
for name, cname, state, prop, ty_, desc in [
    ("sidebar-link-ink", "docs-side-link", "default", "color", "color", "A docs sidebar link's ink."),
    ("search-field-bg", "docs-search", "default", "backgroundColor", "color", "The docs search field fill."),
    ("theme-btn-bg", "docs-theme-btn", "default", "backgroundColor", "color", "The docs 'Switch to dark theme' button fill."),
    ("code-bg", "docs-code", "default", "backgroundColor", "color", "A docs code/metric label's fill."),
]:
    try:
        docs[name] = lit(norm_color(st(cname, state)[prop]), "color",
            f"computed {prop} of {cname} {state} on docs.glassnode.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
