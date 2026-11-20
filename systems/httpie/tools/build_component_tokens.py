#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

httpie.io — the marketing surface and the signed-out /app client, one
design system — declares a compact hand-written token layer on :root,
re-pointed under .dark:root:

  Semantic roles (re-pointed per theme):
    --color-bg-z0..z3          the z-stack of surfaces (light: warm paper
                               -> white; dark: warm near-black -> raised)
    --color-primary            ink
    --color-inverted-primary   ink on an inverted fill
    --color-secondary          ink @ 60%
    --color-tertiary           ink @ 20%
    --color-placeholders       placeholder ink
    --color-accent             the green brand/action accent
    --color-hover              accent hover
    --color-alt-accent(-hover) the blue accent
    --color-warning(-hover)    the red/destructive hue
    --color-focus              the focus-ring colour
    --color-borders(-subtle)   hairline borders
    --color-header-hover       header row hover fill
    --color-item-hover/-selected(-hover)
                               list/menu states
    --color-selection          text selection wash
    --color-draggable/-droppable
                               drag & drop surfaces
    --color-backdrop           modal scrim
    --color-shadows            shadow colour
    --color-code-{primary,gray,green,pink,blue,red,orange,purple,aqua,yellow}
                               the syntax palette
  App-local vars (not re-pointed per theme):
    --app-cursor(-tiny|-link)  custom cursor names
    VariablesTable's --cell-*  the environments table cells
    --shadowed-container-*     scroll-shadow tint on the tab container

  Everything else is literal: an old-Tailwind + CSS Modules stack whose
  utility classes hard-code rgb() values — the warm darks (30 25 25,
  54 54 54, 79 77 77), the warm off-whites (245 245 240, 237 237 235,
  209 209 207, 181 181 178), the pink 250 155 250, the blues 75 120 230 /
  59 94 186 / 105 143 235, the greens 115 220 140 / 99 194 122 / 161 232
  176. vars.mjs harvests every literal into css-vars.json's `palette`;
  literals not already covered by a resolved --color-* are emitted under
  core.palette named after the utility class that uses them (or p<hex>).

Theme is html.light / html.dark: the site boots html.dark (AUTO follows
prefers-color-scheme and headless Chromium's light preference still
resolves dark — the product's painted default), and the footer's own
ThemeToggle radios (LIGHT MODE / AUTO / DARK MODE) repaint html.light,
persisting to localStorage.theme. The `.dark:root` rule re-points the
same names, so `light` and `dark` token sets resolve the same
declarations under each class.

Each leaf: {"type": ..., "var": "--name"} resolved per theme by
build_tokens.py, or a measured {"type", "value", "source"} for geometry
and palette literals the DOM measurement pass or the stylesheet harvest
recorded. Every leaf carries $extensions.source.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V["resolved"]["light"]
RD = V["resolved"]["dark"]
TREE = {"core": {}, "light": {}, "dark": {}, "component": {}}


def emit_at(root, path, leaf):
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = leaf


def cam(name):
    """--foo-bar-baz -> fooBarBaz (a token key, not a CSS name)."""
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


KIND_TY = {"color": "color", "dimension": "dimension", "duration": "duration",
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily"}

emitted = set()


def VAR(name, ty, path, root="core", desc=None, themes=None):
    """Leaf resolved per theme from the var's declaration. themes limits which
    theme sets it lands in ('light'/'dark'/both) — a .dark-only name exists in
    dark alone."""
    leaf = {"type": ty, "var": name}
    if desc:
        leaf["description"] = desc
    for t in (themes or ("light", "dark")):
        emit_at(t if root == "theme" else root, path, leaf)
    emitted.add(name)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


DIM_RE = re.compile(r"-?\d+(\.\d+)?(px|rem)$")


def dim_or_other(name):
    r = R.get(name) or RD.get(name)
    if r["kind"] == "dimension" or DIM_RE.fullmatch(str(r.get("value", r.get("raw", ""))).strip()):
        return "dimension"
    return "other"


def both_themes(name):
    return tuple(t for t in ("light", "dark") if name in (R if t == "light" else RD))


def norm_lit(c):
    """A palette literal -> '#rrggbb' or 'rgba(r, g, b, a)': strips the
    /var(--tw-*-opacity) channel syntax and normalises hex."""
    c = re.sub(r"/\s*var\(--tw-[\w-]+\)", "", c).strip().lower()
    c = re.sub(r"\s*,\s*", ", ", c)
    m = re.fullmatch(r"#([0-9a-f]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(x * 2 for x in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)\s*(?:[,/]\s*([\d.]+%?))?\)", c)
    if m:
        r, g, b, a = m.groups()
        r, g, b = int(float(r)), int(float(g)), int(float(b))
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    return None


# ------------------------------------------------------- semantic roles
# Re-pointed per theme under .dark:root: emitted into both `light` and
# `dark` sets.
GROUPS = [
    ("bg", re.compile(r"--color-bg-z\d")),
    ("text", re.compile(r"--color-(primary|inverted-primary|secondary|tertiary|placeholders)")),
    ("accent", re.compile(r"--color-(accent|hover)")),
    ("altAccent", re.compile(r"--color-alt-accent(-hover)?")),
    ("warning", re.compile(r"--color-warning(-hover)?")),
    ("focus", re.compile(r"--color-focus")),
    ("border", re.compile(r"--color-borders(-subtle)?")),
    ("header", re.compile(r"--color-header-hover")),
    ("item", re.compile(r"--color-item-(hover|selected|selected-hover)")),
    ("selection", re.compile(r"--color-selection")),
    ("drag", re.compile(r"--color-(draggable|droppable)")),
    ("backdrop", re.compile(r"--color-backdrop")),
    ("shadow", re.compile(r"--color-shadows")),
    ("code", re.compile(r"--color-code-[a-z]+")),
]
FIXED_LEAF = {
    "--color-bg-z0": "z0", "--color-bg-z1": "z1", "--color-bg-z2": "z2", "--color-bg-z3": "z3",
    "--color-primary": "primary", "--color-inverted-primary": "invertedPrimary",
    "--color-secondary": "secondary", "--color-tertiary": "tertiary",
    "--color-placeholders": "placeholders", "--color-accent": "default",
    "--color-hover": "hover", "--color-focus": "ring",
    "--color-alt-accent": "default", "--color-alt-accent-hover": "hover",
    "--color-warning": "default", "--color-warning-hover": "hover",
    "--color-borders": "default", "--color-borders-subtle": "subtle",
    "--color-header-hover": "hover", "--color-item-hover": "hover",
    "--color-item-selected": "selected", "--color-item-selected-hover": "selectedHover",
    "--color-selection": "default", "--color-draggable": "draggable",
    "--color-droppable": "droppable", "--color-backdrop": "default",
    "--color-shadows": "color",
}
for group, pat in GROUPS:
    for n in sorted(k for k in set(R) | set(RD) if pat.fullmatch(k)):
        if n in emitted:
            continue
        if n in FIXED_LEAF:
            leaf_name = FIXED_LEAF[n]
        elif n.startswith("--color-code-"):
            leaf_name = cam(n[len("--color-code-"):])
        elif n.startswith("--color-"):
            leaf_name = cam(n[len("--color-"):])
        else:
            leaf_name = cam(n)
        themes = both_themes(n)
        kind = (R.get(n) or RD.get(n)).get("kind", "color")
        desc = "declared under .dark:root only" if "light" not in themes else None
        VAR(n, KIND_TY.get(kind, "other"), f"{group}.{leaf_name}", root="theme", themes=themes, desc=desc)

# ------------------------------------------------------------------ misc
# The app-local vars that are not re-pointed per theme (the custom cursor
# names, the environments table cells, the tab strip's scroll-shadow tint)
# keep their evidence under misc; the --tw-* internals stay out.
declared = set()
for bin_name in ("theme", "skins", "app"):
    for rule in V.get(bin_name, []):
        declared.update(rule.get("properties", {}))
for n in sorted(declared):
    if n in emitted or (n not in R and n not in RD):
        continue
    if n.startswith("--tw-"):
        continue  # Tailwind internals — evidence in css-vars.json
    kind = (R.get(n) or RD.get(n)).get("kind", "other")
    themes = both_themes(n)
    VAR(n, KIND_TY.get(kind, "other"), f"misc.{cam(n)}", root="theme", themes=themes,
        desc="declared under .dark only" if "light" not in themes else None)

# ----------------------------------------------------- literal palette
# The marketing surface hard-codes rgb() literals in utility classes — the
# warm darks and off-whites, the pink pill, the brand ramps. css-vars.json's
# palette harvests every one with the selectors that use it; literals whose
# value a --color-* already covers are skipped (the role is the token), the
# rest become core.palette.<name> primitives.
covered = set()
for theme in (R, RD):
    for rec in theme.values():
        v = rec.get("value") or rec.get("raw")
        if rec.get("kind") == "color" and isinstance(v, str):
            covered.add(v.lower())

PAL_NAMES = [  # utility/marketing class fragment -> token name
    ("code-pink-dark", "pink"), ("pink", "pink"),
    ("code-green-dark", "green"), ("code-red-dark", "red"), ("code-orange-dark", "orange"),
    ("code-blue-dark", "blue"), ("code-aqua-dark", "aqua"), ("code-yellow-dark", "yellow"),
    ("code-purple-dark", "purple"), ("code-gray", "codeGray"),
]
def pal_name(literal, uses):
    joined = " ".join(u["selector"] for u in uses)
    for frag, name in PAL_NAMES:
        if frag in joined:
            return name
    hexv = (norm_lit(literal) or "").lstrip("#")
    return "p" + re.sub(r"[^0-9a-f]", "", hexv)[:6]

palette_items = sorted(V.get("palette", {}).items(), key=lambda kv: -kv[1]["count"])
seen_names = set()
for literal, d in palette_items:
    v = norm_lit(literal)
    if v is None:
        continue
    if v.lower() in covered or literal == "#0000":
        continue
    if d["count"] < 2:
        continue
    name = pal_name(literal, d["uses"])
    while name in seen_names:
        name += "2"
    seen_names.add(name)
    uses = "; ".join(u["selector"][:110] for u in d["uses"][:3])
    lit(v, "color",
        f"literal in httpie.io's stylesheets (raw/css-vars.json palette, {d['count']} declarations; e.g. {uses})",
        "core", f"palette.{name}")

TRANSPARENT = re.compile(r"transparent|rgba\(\s*[\d.]+[,\s]+[\d.]+[,\s]+[\d.]+\s*[,/]\s*0(\.0+)?%?\s*\)")

# ------------------------------------------------- measured type scale
# Required: a build without the measurements would silently drop every
# measured token, so a missing file is an error.
C_PATH = RAW / "components-computed.json"
if True:
    C = json.loads(C_PATH.read_text())["components"]

    def geom(comp, state, field, path, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        rect = st.get("rect") or {}
        style = st.get("style") or {}
        v = rect.get(field) if field in rect else style.get(field)
        if v is None:
            return
        try:
            px = float(re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:px)?", str(v)).group(1))
        except Exception:
            return
        lit(f"{px:g}px", "dimension",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    geom("site-nav", "default", "h", "nav.height", "top navigation bar")
    geom("nav-cta", "default", "h", "button.cta.height", "'Go to App' button")
    geom("nav-link", "default", "h", "navLink.height", "nav link row")
    geom("app-sidebar", "default", "w", "appSidebar.width", "/app left rail")
    geom("app-request-tab", "default", "h", "tabCard.height", "request tab card")
    geom("app-url-field", "default", "h", "urlField.height", "the URL field")
    geom("app-send-button", "default", "h", "sendButton.height", "the Send button")
    geom("app-panel-tabs", "default", "h", "panelTabs.height", "request panel tablist")
    geom("app-method-button", "default", "h", "methodButton.height", "method select")
    geom("testimonial-card", "default", "h", "testimonialCard.height", "tweet card")
    geom("newsletter-input", "default", "h", "input.height", "newsletter field")
    geom("post-card", "default", "h", "postCard.height", "blog index card")
    geom("prose-pre", "default", "h", "codeBlock.height", "article code block")
    geom("docs-toc", "default", "w", "docsToc.width", "docs table of contents")
    geom("m-nav", "default", "h", "mobileNav.height", "mobile top bar")

    def style_tok(comp, state, prop, path, ty, label):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        v = (st.get("style") or {}).get(prop)
        if v is None:
            return
        lit(v, ty, f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path)

    def radius_tok(comp, state, path, label):
        """The capture records the four corner properties, never the shorthand;
        emit the shared radius when all four agree. Chromium reports a fully
        rounded corner as its infinity clamp — that reads as a pill, emitted
        at the full-radius bound."""
        st = C.get(comp, {}).get("states", {}).get(state, {})
        s = st.get("style") or {}
        corners = [s.get(f"border{p}Radius") for p in
                   ("TopLeft", "TopRight", "BottomRight", "BottomLeft")]
        if not all(corners) or len(set(corners)) != 1:
            return
        v = corners[0]
        desc = None
        try:
            if float(re.fullmatch(r"(-?\d+(?:\.\d+)?(?:e\+?\d+)?)px", v).group(1)) >= 9999:
                v, desc = "9999px", "all four corners measure the full-radius clamp — a pill"
        except Exception:
            pass
        lit(v, "dimension",
            f"measured {comp} {state} on {C[comp].get('page')} ({label})",
            "component", path, desc=desc)

    def theme_alias(comp, state, prop, path, role, label):
        """A measured fill that lands on a declared semantic role. Each theme
        the element was measured under gets the alias: the default reading is
        the dark site, a 'light' state the light one. A theme with no reading
        gets no token."""
        sts = C.get(comp, {}).get("states", {})
        for t, s in (("dark", state), ("light", "light")):
            if (sts.get(s, {}).get("style") or {}).get(prop) is None:
                continue
            emit_at(t, path, {"type": "color", "value": "{" + role + "}",
                    "source": f"measured {comp} {s} on {C[comp].get('page')} ({label}) — the element's class paints the {role} role",
                    "description": label})

    def measured_fill(comp, prop, path, label, note=None):
        """The component's painted fill recorded per theme from the
        measurement, for elements whose class paints a literal (or is
        transparent over the page) rather than a themed role — each theme
        set gets the value measured under it ('light' state where the
        recording has one, else the default read)."""
        st = C.get(comp, {}).get("states", {})
        for t, src_state in (("light", "light"), ("dark", "default")):
            v = (st.get(src_state, {}).get("style") or {}).get(prop)
            # a theme with no reading gets no token; a transparent reading is
            # no fill (the page shows through) and is never committed
            if v is None or TRANSPARENT.fullmatch(str(v).strip()):
                continue
            leaf = {"type": "color", "value": norm_lit(v) or v,
                    "source": f"measured {comp} {src_state} on {C[comp].get('page')} ({label})" + (f" — {note}" if note else ""),
                    "description": label}
            emit_at(t, path, leaf)

    radius_tok("nav-cta", "default", "button.cta.radius", "CTA corner")
    radius_tok("button-secondary", "default", "button.secondary.radius", "secondary button corner")
    radius_tok("early-access-badge", "default", "badge.radius", "beta pill corner")
    radius_tok("testimonial-card", "default", "testimonialCard.radius", "tweet card corner")
    radius_tok("newsletter-input", "default", "input.radius", "newsletter field corner")
    radius_tok("app-request-tab", "default", "tabCard.radius", "request tab corner")
    radius_tok("app-send-button", "default", "sendButton.radius", "Send corner")
    radius_tok("app-url-field", "default", "urlField.radius", "URL field corner")
    radius_tok("prose-pre", "default", "codeblock.radius", "code block corner")
    radius_tok("theme-toggle", "default", "themeToggle.radius", "theme control corner")

    # The 'Go to App' button hard-codes the accent green in both painted
    # themes — it does NOT follow the accent role (light.accent.default is a
    # different green), so the measured literal is the honest token.
    measured_fill("nav-cta", "backgroundColor", "component.button.cta.bg", "primary button fill",
                  "the class hard-codes this green in both themes; it is not the themed accent role")
    # The Send button's dark measurement lands exactly on dark.accent.default
    # — the app control paints var(--color-accent), so the alias stays; its
    # light state was not measured.
    theme_alias("app-send-button", "default", "backgroundColor", "component.sendButton.bg", "accent.default", "Send fill")
    # site-nav and app-sidebar paint transparent in both themes (the page's
    # bg.z0 shows through), so neither has a fill token.
    style_tok("nav-link", "hover", "color", "type.navLinkHover.color", "color", "nav link on hover")
    style_tok("post-title-link", "hover", "color", "type.linkHover.color", "color", "post title on hover")
    style_tok("prose-h1", "default", "fontSize", "type.articleTitle.size", "other", "article h1")
    style_tok("hero-headline", "default", "letterSpacing", "type.hero.tracking", "other", "hero headline tracking")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography. letterSpacing stays in px as measured.
    # The recording holds two type reads: `style` is the component element's
    # own computed style, `textStyle` the first real text node inside it.
    # Where a wrapper's font differs from the label it holds (a tab card's
    # 16px chrome vs its 8.5px mono label), the text node's reading is the
    # token's honest value.
    def typ(comp, path, name, state="default"):
        st = C.get(comp, {}).get("states", {}).get(state, {})
        s = st.get("textStyle") or st.get("style") or {}
        if not s.get("fontSize"):
            return
        style = {
            "fontFamily": s["fontFamily"],
            "fontSize": s["fontSize"],
            "fontWeight": int(float(s["fontWeight"])),
            "lineHeight": s["lineHeight"],
        }
        if s.get("letterSpacing") and s["letterSpacing"] != "normal":
            style["letterSpacing"] = s["letterSpacing"]
        leaf = {"$value": style, "$type": "typography",
                "$description": name,
                "$extensions": {"source": f"measured {comp} on {C[comp].get('page')} ({state} state)"}}
        emit_at("core", path, leaf)

    typ("hero-headline", "typography.hero", "the home hero display — Pie Headline (FK Screamer)")
    typ("section-heading", "typography.sectionTitle", "a home section heading")
    typ("prose-h1", "typography.articleTitle", "the changelog article title")
    typ("prose-p", "typography.body", "article body text — Pie Body (PolyPie)")
    typ("prose-link", "typography.bodyLink", "a body-text link inside the article")
    typ("prose-pre", "typography.codeBlock", "code inside a fenced block — Pie Monospace")
    typ("nav-link", "typography.navLink", "a nav link")
    typ("nav-cta", "typography.button", "the primary button label")
    typ("app-url-field", "typography.urlField", "the request URL field — Pie Monospace")
    typ("app-request-tab", "typography.tabLabel", "a request tab label")
    typ("newsletter-input", "typography.input", "the newsletter email field")

# --------------------------------------------------------- font faces
# The faces are proprietary and never shipped. Each stack is the computed
# fontFamily of an element that paints it, verbatim; the @font-face harvest
# (raw/css-vars.json fonts) names the faces.
def measured_family(comp, path, face, desc):
    st = C[comp]["states"]["default"]
    v = (st.get("textStyle") or {}).get("fontFamily") or st["style"]["fontFamily"]
    if face not in v:
        raise ValueError(f"{comp}: computed fontFamily {v!r} does not name {face}")
    lit(v, "fontFamily",
        f"computed fontFamily of {comp} default on {C[comp].get('page')} (raw/components-computed.json); {face} is declared by @font-face in httpie.io's sheets, a licensed face (the name is evidence, the font file is not shipped)",
        "core", path, desc=desc)


measured_family("hero-headline", "font.family.headline", "Pie Headline", "the display face — hero and section headlines (FK Screamer)")
measured_family("prose-p", "font.family.body", "Pie Body", "the body/UI face (PolyPie)")
measured_family("cli-code-block", "font.family.mono", "Pie Monospace", "the code face — terminal blocks, the URL field, JSON")
lit('"Pie Symbols"', "fontFamily",
    "@font-face in httpie.io's sheets (raw/css-vars.json fonts): 'Pie Symbols', licensed icon face — the name is evidence, the font file is not shipped",
    "core", "font.family.symbols", desc="the icon/symbol face")

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
    print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
