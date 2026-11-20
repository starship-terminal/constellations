#!/usr/bin/env python3
"""Build raw/component-tokens.json, the token tree build_tokens.py resolves.

hume.ai's signed-out surfaces carry four token layers on four origins:

  www.hume.ai (Next.js + Tailwind v4, LIGHT ONLY — no theme control):
    :root declares the product layer —
      --background #fdfdfc / --foreground #1b1918
      --font-sans 'Inter' / --font-serif 'Martina Plantijn' /
        --font-mono 'PP Fraktion Mono' / --font-japanese 'M PLUS 1'
      --accent-{pink,magenta,purple,blue,sky,mint,green,lime,orange,coral,salmon}
        the eleven-pastel brand ramp
      --gradient-{cream,pink,peach,apricot,lilac}   hero/section wash stops
      --title-{2xl,xl,lg,sm}                        display sizes
      --surface-radius 0.25rem, --code-background
      --color-spectrum-{amber,sky,blue,violet,peach}
        the audio-visualisation spectrum hues
    :root,:host beside it holds the Tailwind v4 default theme
    (--color-*, --spacing, --container-*, --text-*, --radius-*, --ease-*,
    --animate-*). The product layer is tokenised; the Tailwind default
    stays evidence in css-vars.json — it is the library's stock palette,
    not Hume's choice, so only --spacing and the --radius-*/--ease-* scales
    it actually composes are emitted under core.tailwind.

  dev.hume.ai (a Fern docs build — the only surface with a theme control;
    the header Theme button's Light / Dark / System menu repaints
    html.dark): --gray-1..12 / --grayscale-*, --accent-*, --background,
    --border, --card-*/--sidebar-*/--header-background, --code-background,
    --hume-gradient, --primitive-{noul,choice,score,span,ink},
    --font-body 'Fellix' / --font-code 'Fraktion'. Everything resolved
    under both class scopes is emitted into light.docs.* and dark.docs.*.

  demo.hume.ai (the invitation gate — the playground it guards is a
    documented boundary): --hume-white/-black, --neutral-950..50, --tan-*,
    the six --<hue>-100..400 families, --background-*/--border-* roles.
    Light only -> light.demo.*.

  app.hume.ai (/log-in is public; nothing past it was entered): an
    oklch-based shadcn layer — --background-body/-elevated, --foreground,
    --muted-foreground, --border, --primary, Fellix. Light only ->
    light.app.*.

Theme: www, demo and app paint a single light theme — a .dark class and a
dark colour-scheme emulation leave them unchanged. The `dark` token set
holds only the docs' painted dark (html.dark through the Theme menu); its
$description says so.

Each leaf: {"type", "var", "surface"} resolved by build_tokens.py from that
surface's resolved set, or a measured {"type", "value", "source"} for
geometry and literals the DOM measurement or the palette harvest recorded.
Every leaf carries $extensions.source.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
S = V["surfaces"]
R = {k: s["resolved"] for k, s in S.items()}          # R["www"]["light"][name]
TREE = {"core": {}, "light": {}, "dark": {}, "component": {}}

# The surface key is an internal label, not a hostname: docs lives on
# dev.hume.ai, not docs.hume.ai.
HOST = {"www": "www.hume.ai", "docs": "dev.hume.ai", "demo": "demo.hume.ai", "app": "app.hume.ai"}


def _is_leaf(node):
    return isinstance(node, dict) and "type" in node and ("value" in node or "var" in node)


def emit_at(root, path, leaf):
    """Place a leaf at path. A leaf already sitting at an intermediate node
    is moved under a `default` child first, so a child name can never
    clobber a leaf field (--accent vs --accent-surface: the child's key
    `surface` would otherwise overwrite the leaf's own `surface` field)."""
    cur = TREE[root]
    parts = path.split(".")
    for p in parts[:-1]:
        nxt = cur.setdefault(p, {})
        if _is_leaf(nxt):
            cur[p] = {"default": nxt}
            nxt = cur[p]
        cur = nxt
    last = parts[-1]
    existing = cur.get(last)
    if isinstance(existing, dict) and not _is_leaf(existing):
        existing["default"] = leaf
    else:
        cur[last] = leaf


def cam(name):
    """--foo-bar-baz -> fooBarBaz (a token key, not a CSS name)."""
    parts = name.lstrip("-").split("-")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


KIND_TY = {"color": "color", "dimension": "dimension", "duration": "duration",
           "easing": "cubicBezier", "number": "number", "fontFamily": "fontFamily",
           "shadow": "shadow"}


def VAR(name, ty, path, surface="www", themes=("light",), root="core", desc=None):
    """Leaf resolved from the surface's own resolved set for each theme."""
    leaf = {"type": ty, "var": name, "surface": surface}
    if desc:
        leaf["description"] = desc
    for t in themes:
        emit_at(t if root == "theme" else root, path, leaf)


def lit(value, ty, src, root="component", path=None, desc=None):
    leaf = {"type": ty, "value": value, "source": src}
    if desc:
        leaf["description"] = desc
    emit_at(root, path, leaf)


def exotic(c):
    """CSS lab() (D50, Bradford-adapted) and oklab()/oklch() -> 'rgb(r, g, b)' or
    'rgba(r, g, b, a)', so colour() can label it like any other reading. The
    palette's lab()/oklch() literals become tokens instead of being dropped
    (2026-11 audit, finding 14-20). Returns c unchanged when it cannot convert."""
    import math
    gam = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
    alpha = lambda a: 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))

    def out(lin, a):
        r, g, b = (max(0, min(255, round(gam(max(0.0, v)) * 255))) for v in lin)
        al = alpha(a)
        return f"rgb({r}, {g}, {b})" if al == 1 else f"rgba({r}, {g}, {b}, {al:g})"

    m = re.fullmatch(r"lab\(\s*([\d.]+)%?\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        L, A, B, a = m.groups()
        fy = (float(L) + 16) / 116
        fx, fz = fy + float(A) / 500, fy - float(B) / 200
        d = 6 / 29
        f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
        x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
        return out((3.1338561 * x - 1.6168667 * y - 0.4906146 * z,
                    -0.9787684 * x + 1.9161415 * y + 0.0334540 * z,
                    0.0719453 * x - 0.2289914 * y + 1.4052427 * z), a)
    m = re.fullmatch(r"okl(ch|ab)\(\s*([\d.]+%?)\s+(none|-?[\d.]+%?)\s+(none|-?[\d.]+(?:deg)?)\s*(?:/\s*([\d.]+%?))?\s*\)", c.strip())
    if m:
        kind, L, x, y, a = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        num_ = lambda v, scale: 0.0 if v == "none" else (float(v[:-1]) / 100 * scale if v.endswith("%") else float(v.replace("deg", "")))
        if kind == "ch":
            C_, h = num_(x, 0.4), num_(y, 1)
            A, B = C_ * math.cos(math.radians(h)), C_ * math.sin(math.radians(h))
        else:
            A, B = num_(x, 0.4), num_(y, 0.4)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        return out((4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
                    -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
                    -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_), a)
    return c


def norm_lit(c):
    """A palette literal -> '#rrggbb' or 'rgba(r, g, b, a)'."""
    c = re.sub(r"/\s*var\(--[\w-]+\)", "", c.strip().lower())
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
    if re.match(r"(oklch|oklab|lab)\(", c):
        v = exotic(c)
        return norm_lit(v) if v != c else None
    return None


# ------------------------------------------------- www product layer
W = R["www"]["light"]

def wvar(name, ty, path, root="core", themes=("light",), desc=None):
    if name in W:
        VAR(name, ty, path, surface="www", themes=themes, root=root, desc=desc)

# The semantic roles the product layer declares — the only painted theme.
wvar("--background", "color", "bg.default", root="theme",
     desc="www.hume.ai page ground — the warm off-white #fdfdfc")
wvar("--foreground", "color", "ink.default", root="theme",
     desc="www.hume.ai body ink — the warm near-black #1b1918")
wvar("--code-background", "color", "code.background", root="theme",
     desc="code surface on www (white on the off-white ground)")

# The eleven-pastel brand ramp — core, theme-independent declarations.
for n in sorted(k for k in W if re.fullmatch(r"--accent-[a-z]+", k)):
    VAR(n, "color", f"accent.{cam(n[len('--accent-'):])}",
        desc="a pastel of the www brand ramp — section washes, chips, illustration fills")
# The hero/section gradient stops.
for n in sorted(k for k in W if re.fullmatch(r"--gradient-[a-z]+", k)):
    VAR(n, "color", f"gradientStop.{cam(n[len('--gradient-'):])}",
        desc="a stop of the www gradient washes")
# The audio-visualisation spectrum hues.
for n in sorted(k for k in W if re.fullmatch(r"--color-spectrum-[a-z]+", k)):
    VAR(n, "color", f"spectrum.{cam(n[len('--color-spectrum-'):])}",
        desc="a spectrum hue — the prosody/expression visualisation colours")
# The display type sizes.
for n in sorted(k for k in W if re.fullmatch(r"--title-[a-z0-9]+", k)):
    VAR(n, KIND_TY.get(W[n].get("kind"), "dimension"), f"title.{cam(n[len('--title-'):])}",
        desc="a display title size on www")
# The brand families.
for n, leaf_name in [("--font-sans", "sans"), ("--font-serif", "serif"),
                     ("--font-mono", "mono"), ("--font-japanese", "japanese")]:
    wvar(n, "fontFamily", f"font.family.{leaf_name}")
wvar("--surface-radius", "dimension", "radius.surface")

# The Tailwind v4 default theme is the library's stock palette, not Hume's
# choice — only the scales the product composes are tokens; the rest is
# evidence in raw/css-vars.json.
for n in sorted(k for k in W if re.fullmatch(r"--radius-[a-z0-9]+", k)):
    VAR(n, "dimension", f"tailwind.radius.{cam(n[len('--radius-'):])}",
        desc="a step of the Tailwind v4 default radius scale the site ships")
if "--spacing" in W:
    VAR("--spacing", "dimension", "tailwind.spacing", desc="the Tailwind v4 spacing base — every --spacing-* multiple")
for n in sorted(k for k in W if re.fullmatch(r"--ease-[a-z-]+", k)):
    VAR(n, KIND_TY.get(W[n].get("kind"), "cubicBezier"), f"tailwind.ease.{cam(n[len('--ease-'):])}",
        desc="a step of the Tailwind v4 default easing scale")

# --------------------------------------------------- docs token layer
# Everything the docs resolve under both class scopes lands in light.docs.*
# and dark.docs.*; a light-only name lands in light alone.
DL = R["docs"]["light"]
DD = R["docs"]["dark"]
DOCS_SKIP = re.compile(r"^--(tw-|_|radix-|fern-|typography-(table|code-block-|code-comment)|syntax-|docsearch|ais-|search-|algolia)")
for n in sorted(set(DL) | set(DD)):
    if DOCS_SKIP.match(n):
        continue
    themes = tuple(t for t in ("light", "dark") if n in (DL if t == "light" else DD))
    if not themes:
        continue
    rec = DL.get(n) or DD.get(n)
    ty = KIND_TY.get(rec.get("kind"), "other")
    if ty == "other" and re.fullmatch(r"-?\d*\.?\d+px", str(rec.get("raw", "")).strip()):
        ty = "dimension"
    # keep the token path flat and readable under the docs group
    m = re.match(r"--([a-z]+)-?(.*)", n)
    grp, rest = (m.group(1), m.group(2)) if m else ("misc", n.lstrip("-"))
    desc = "a dev.hume.ai token (the Fern docs layer) — resolved per theme through the header Theme menu"
    if n == "--hume-gradient":
        ty, desc = "other", "the Hume spectrum gradient — the audio-decision brand bar"
    if n.startswith("--primitive-"):
        desc = "a decision-model primitive hue (the ADM marker colours)"
    VAR(n, ty, f"docs.{grp}.{cam(rest) if rest else 'default'}" if rest else f"docs.{grp}", surface="docs",
        themes=themes, root="theme", desc=desc)

# --------------------------------------------------- demo + app layers
def surface_vars(surf, skip_re, root_path):
    res = R[surf]["light"]
    for n in sorted(res):
        if skip_re.match(n):
            continue
        rec = res[n]
        m = re.match(r"--([a-z]+)-?(.*)", n)
        grp, rest = (m.group(1), m.group(2)) if m else ("misc", n.lstrip("-"))
        path = f"{surf}.{grp}.{cam(rest)}" if rest else f"{surf}.{grp}"
        ty = KIND_TY.get(rec.get("kind"), "other")
        # A var declared as an `R G B` channel triplet (Tailwind's
        # `rgb(var(--x) / <alpha>)` idiom) resolves through box-shadow in the
        # probe and is misclassified "shadow"; its honest value is rgb().
        chan = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", str(rec.get("raw", "")).strip())
        if ty == "shadow" and chan:
            lit("#%02x%02x%02x" % tuple(int(g) for g in chan.groups()), "color",
                f"css-var {n} channel triplet '{rec['raw']}' ({surf}.hume.ai, light) — declared for rgb(var(--{n.lstrip('-')}) / <alpha>) composition",
                "light", path,
                desc=f"a {surf}.hume.ai token — that surface paints a single light theme")
            continue
        if ty == "other" and re.fullmatch(r"-?\d*\.?\d+px", str(rec.get("raw", "")).strip()):
            ty = "dimension"
        VAR(n, ty, path, surface=surf, themes=("light",), root="theme",
            desc=f"a {surf}.hume.ai token — that surface paints a single light theme")

surface_vars("demo", re.compile(r"^--(tw-|_)"), "demo")
surface_vars("app", re.compile(r"^--(tw-|_|radix-)"), "app")

# ------------------------------------------------- literal palette
# The www surface also hard-codes rgb()/hex literals in utility classes and
# component styles. css-vars.json's palette harvests each with the
# selectors that use it; literals a resolved var already covers are
# skipped, the rest become core.palette.<name> primitives.
covered = set()
for surf_res in R.values():
    for theme in surf_res.values():
        for rec in theme.values():
            v = rec.get("value") or rec.get("raw")
            if rec.get("kind") == "color" and isinstance(v, str):
                nv = norm_lit(v)
                covered.add((nv or v).lower())

seen_names = set()
for surf in ("www", "docs", "demo", "app"):
    if surf not in S:
        continue
    for literal, d in sorted(S[surf].get("palette", {}).items(), key=lambda kv: -kv[1]["count"]):
        v = norm_lit(literal)
        if v is None or v.lower() in covered or literal in ("#0000", "rgba(0, 0, 0, 0)", "#ffffff", "#fff"):
            continue
        if d["count"] < 3:
            continue
        name = "p" + re.sub(r"[^0-9a-f]", "", (v if v.startswith("#") else literal).lstrip("#"))[:6]
        while name in seen_names:
            name += "x"
        seen_names.add(name)
        uses = "; ".join(u["selector"][:100] for u in d["uses"][:3])
        lit(v, "color",
            f"literal in {HOST.get(surf, surf + '.hume.ai')}'s stylesheets (raw/css-vars.json palette, {d['count']} declarations; e.g. {uses})",
            "core", f"palette.{name}")

# ------------------------------------------------- measured type scale
# Required: without it every measured token would drop silently.
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
    geom("nav-cta", "default", "h", "button.cta.height", "'See a Demo' button")
    geom("hero-headline", "default", "h", "hero.height", "home hero h1")
    geom("player-card", "default", "h", "playerCard.height", "customer-call player")
    geom("newsletter-input", "default", "h", "input.height", "newsletter field")
    geom("contact-field", "default", "h", "contactField.height", "contact form field")
    geom("post-card", "default", "h", "postCard.height", "blog index card")
    geom("prose-pre", "default", "h", "codeBlock.height", "article code block")
    geom("docs-code-block", "default", "h", "docsCodeBlock.height", "docs code block")
    geom("docs-nav", "default", "w", "docsSidebar.width", "docs left nav rail")
    geom("docs-toc", "default", "w", "docsToc.width", "docs table of contents")
    geom("demo-gate-card", "default", "h", "demoGate.height", "invitation gate card")
    geom("login-card", "default", "h", "loginCard.height", "log-in card")
    geom("login-email-field", "default", "h", "loginField.height", "log-in field")
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

    def measured_fill(comp, prop, path, label, note=None):
        """The component's painted fill recorded per theme from the
        measurement — each theme set gets the value measured under it (the
        'dark' docs state where the recording has one, else the painted
        light default; www components have no dark state because the
        surface has no dark theme)."""
        st = C.get(comp, {}).get("states", {})
        light_v = (st.get("default", {}).get("style") or {}).get(prop)
        dark_v = (st.get("dark", {}).get("style") or {}).get(prop)
        if light_v is None and dark_v is None:
            return
        for t, v, src_state in (("light", light_v, "default"), ("dark", dark_v, "dark")):
            if v is None:
                continue
            leaf = {"type": "color", "value": norm_lit(v) or v,
                    "source": f"measured {comp} {src_state} on {C[comp].get('page')} ({label})" + (f" — {note}" if note else ""),
                    "description": label}
            emit_at(t, path, leaf)

    radius_tok("nav-cta", "default", "button.cta.radius", "'See a Demo' corner")
    radius_tok("newsletter-input", "default", "input.radius", "newsletter field corner")
    radius_tok("newsletter-button", "default", "newsletterButton.radius", "Subscribe corner")
    radius_tok("contact-field", "default", "contactField.radius", "contact field corner")
    radius_tok("contact-submit", "default", "contactSubmit.radius", "contact submit corner")
    radius_tok("player-transport", "default", "playerTransport.radius", "Play corner")
    radius_tok("benchmark-tab", "default", "benchmarkTab.radius", "benchmark tab corner")
    radius_tok("post-card", "default", "postCard.radius", "post card corner")
    radius_tok("docs-code-block", "default", "docsCodeBlock.radius", "docs code block corner")
    radius_tok("docs-search-button", "default", "docsSearch.radius", "docs search field corner")
    radius_tok("demo-gate-card", "default", "demoGate.radius", "gate card corner")
    radius_tok("login-card", "default", "loginCard.radius", "log-in card corner")
    radius_tok("login-email-field", "default", "loginField.radius", "log-in field corner")
    radius_tok("login-submit", "default", "loginSubmit.radius", "LOG IN corner")

    # Painted fills: www components paint the only theme they have; the
    # docs' dark set gets the reading taken after the Theme menu repainted.
    measured_fill("nav-cta", "backgroundColor", "component.button.cta.bg", "primary button fill")
    measured_fill("site-nav", "backgroundColor", "component.nav.bg", "nav bar fill")
    measured_fill("newsletter-button", "backgroundColor", "component.newsletterButton.bg", "Subscribe fill")
    measured_fill("docs-code-block", "backgroundColor", "component.docsCode.bg", "docs code block fill")
    measured_fill("demo-gate-card", "backgroundColor", "component.demoGate.bg", "gate card fill")
    measured_fill("login-card", "backgroundColor", "component.loginCard.bg", "log-in card fill")
    measured_fill("login-submit", "backgroundColor", "component.loginSubmit.bg", "LOG IN fill")
    style_tok("nav-menu-button", "hover", "color", "type.navLinkHover.color", "color", "nav menu button on hover")
    style_tok("post-title-link", "hover", "color", "type.linkHover.color", "color", "post title on hover")
    style_tok("prose-h1", "default", "fontSize", "type.articleTitle.size", "other", "article h1")
    style_tok("hero-headline", "default", "letterSpacing", "type.hero.tracking", "other", "hero headline tracking")
    style_tok("newsletter-input", "focused", "outlineColor", "focus.outline.color", "color", "field focus ring")
    style_tok("contact-field", "focused", "outlineColor", "focus.contactOutline.color", "color", "contact field focus ring")

    # Measured type styles as DTCG typography composites — DESIGN.md reads
    # tokens under core.typography. letterSpacing stays in px as measured.
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

    typ("hero-headline", "typography.hero", "the home hero display — Inter")
    typ("section-heading", "typography.sectionTitle", "a home section heading")
    typ("prose-h1", "typography.articleTitle", "the blog post title")
    typ("prose-p", "typography.body", "article body text — Inter")
    typ("prose-link", "typography.bodyLink", "a body-text link inside the article")
    typ("prose-code", "typography.inlineCode", "an inline code span — PP Fraktion Mono")
    typ("prose-pre", "typography.codeBlock", "code inside a fenced block")
    typ("nav-menu-button", "typography.navLink", "a nav menu button")
    typ("nav-cta", "typography.button", "the primary button label")
    typ("newsletter-input", "typography.input", "the newsletter email field")
    typ("docs-side-link", "typography.docsNavLink", "a docs nav link — Fellix")
    typ("docs-code-block", "typography.docsCode", "docs code — Fraktion")
    typ("login-email-field", "typography.loginField", "the log-in field — Fellix")

# --------------------------------------------------------- font faces
# The faces are proprietary and never shipped. Each stack is the computed
# fontFamily of an element that paints it, verbatim; the @font-face harvest
# (raw/css-vars.json fonts) names the faces. The Japanese face is the declared
# --font-japanese var leaf above (no element paints it).
def measured_family(comp, path, face, host, desc):
    st = C[comp]["states"]["default"]
    v = (st.get("textStyle") or {}).get("fontFamily") or st["style"]["fontFamily"]
    if face.lower() not in v.lower():
        raise ValueError(f"{comp}: computed fontFamily {v!r} does not name {face}")
    lit(v, "fontFamily",
        f"computed fontFamily of {comp} default on {C[comp].get('page')} (raw/components-computed.json); {face} is declared by @font-face in {host}'s sheets",
        "core", path, desc=desc)


measured_family("site-nav", "font.family.body", "Inter", "www.hume.ai", "the body/UI face on www.hume.ai (open-licensed)")
measured_family("hero-headline", "font.family.display", "Martina Plantijn", "www.hume.ai", "the serif display face — a licensed face, not shipped")
measured_family("player-card", "font.family.monoWww", "PP Fraktion Mono", "www.hume.ai", "the code face on www.hume.ai — licensed, not shipped")
measured_family("docs-side-link", "font.family.docs", "Fellix", "dev.hume.ai", "the docs/app body face — licensed, not shipped")
measured_family("docs-code-block", "font.family.code", "Fraktion", "dev.hume.ai", "the docs code face — licensed, not shipped")

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(TREE, indent=1, ensure_ascii=False) + "\n")
    print({k: sum(1 for _ in json.dumps(v).split('"type"')) - 1 for k, v in TREE.items()})
