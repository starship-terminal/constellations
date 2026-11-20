#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

elevenmusic.io is one product signed out: a Next.js App Router app shell over
Tailwind v4 that declares a shadcn-style semantic token layer — the
--background/--foreground/--card/--primary/--muted/--border/--sidebar-* roles
plus its own --surface-*, --lighten-*, --darken-*, --lift-*, --composer-* and
--gray-alpha-* extensions — harvested into raw/css-vars.json by
tools/capture/vars.mjs and resolved twice, once on the light probe and once on
the dark probe (the app paints dark by default: html.dark). Declared roles
become {"var": ...} leaves resolved per theme.

Scales that read identically in both themes — the Tailwind --color-* palette,
the --text-*/--radius-*/--blur-*/--tracking-*/--spacing scales and the font
weights — live in core. Geometry and the measured type ramp live under
component.*, as {"value": ..., "source": ...} leaves off
raw/components-computed.json:

  type         the hero display face is waldenburg light (declared
               --font-waldenburg); UI text is Inter (--font-sans ->
               --font-inter); GeistMono is declared for code/IDs.
               The text ramp is the Tailwind --text-* scale 12-72px.
  shape        --radius-xs 2px -> --radius-3xl 24px; controls paint 4px-24px
               radii and full circles; the composer field and prompt chips
               are pills.
  states       focus-visible draws a 2px outline (measured); pressed scales
               the control to 0.95-0.98 (measured transforms).
  themes       dark is the default paint; light is a real footer toggle
               remapping the same roles — the light page is the warm
               paper #fdfcfb, dark is true black with white-alpha ramps.

A leaf is {"var": "--name"} (resolved in the theme pass it sits in) or
{"value": ..., "source": ...} for a declared-but-unresolved or measured
value. Shadow variables resolve to full CSS shadow strings, so their leaves
carry the layer list parsed at spec time.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
RD = RES.get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
L = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
D = {n: v.get("value", v.get("raw")) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def decl(name):
    """The raw declaration of a custom property in the harvested sheets —
    for variables declared on a class (the font loader classes) that the
    :root resolution pass never sees."""
    for b in ("theme", "app", "utility", "vendor"):
        for e in V.get(b, []):
            if name in e.get("properties", {}):
                return e["properties"][name], f"{e['file'].split('/')[-1]} {e['selector']}"
    return None, None


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. elevenmusic.io "
    "declares a shadcn-style semantic token layer in its Next.js bundles and "
    "paints dark by default (html.dark); the footer theme control remaps the "
    "same roles to a warm-paper light theme. Declared roles become var leaves "
    "resolved per theme; scales identical in both themes live in core; "
    "geometry and the measured type ramp are measured leaves from "
    "raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h[6:] != "ff":  # keep the alpha of #rrggbbaa
            return f"rgba({int(h[0:2], 16)}, {int(h[2:4], 16)}, {int(h[4:6], 16)}, {'%g' % round(int(h[6:8], 16) / 255, 3)})"
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is not None and a.endswith("%"):  # a percentage alpha
            a = "%g" % (float(a[:-1]) / 100)
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


def measured(comp, state, prop, ty="dimension", desc=None):
    s = st(comp, state)
    v = s[prop]
    return {"value": v, "type": ty,
            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
            **({"description": desc} if desc else {})}


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp, ...' into DTCG shadow layers, dropping no-ops."""
    out = []
    for m in re.finditer(
            r"(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|lab\([^)]+\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?", spec):
        col, x, y, bl, sp, ins = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0)"):
            continue  # transparent placeholders
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue
        layer = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                 "blur": f"{bl}px", "spread": f"{sp or 0}px"}
        if ins:
            layer["inset"] = True
        out.append(layer)
    return out


def shadow_var(name, theme_map, theme, desc):
    """A shadow variable resolved on a theme pass: the leaf carries the parsed
    layer list because build_tokens.py checks DTCG shadow shape."""
    val = theme_map.get(name)
    if not val:
        return None
    layers = shadow_layers(val)
    if not layers:
        return None
    return {"value": layers, "type": "shadow",
            "source": f"css-var {name} ({theme})", "description": desc}


# ------------------------------------------------------------------- fonts
# The families are declared on the font-loader classes, not :root, so the
# resolution pass never sees them — read the declarations and note where.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, vname, fallback, desc in [
    ("sans", "--font-inter", "Inter, ui-sans-serif, system-ui, sans-serif",
     "Inter variable (100-900): the UI face — nav, labels, fields, track titles. --font-sans resolves to it."),
    ("display", "--font-waldenburg", "waldenburg, Arial, sans-serif",
     "waldenburg light/regular: the display face — the hero headline and page titles."),
    ("mono", "--font-geist-mono", "GeistMono, ui-monospace, monospace",
     "GeistMono variable: the declared mono stack for IDs and code."),
]:
    raw, where = decl(vname)
    if raw:
        stack = re.sub(r"var\(--font-[a-z-]+\)", fallback.split(",")[0], raw)
        # The declared stack keeps its per-family quotes: '"Inter", "Inter
        # Fallback"'. Stripping '"' off the whole string would leave the
        # inner quotes in place and mangle every family after the first.
        fam[key] = {"value": stack.strip(), "type": "fontFamily",
                    "source": f"declared {vname} ({where})", "description": desc}

wgt = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, vname, desc in [
    ("light", "--font-weight-light", "300: the display headline weight."),
    ("normal", "--font-weight-normal", "400: body and labels."),
    ("medium", "--font-weight-medium", "500: nav rows, buttons and track titles."),
    ("semibold", "--font-weight-semibold", "600: headings and emphasis."),
    ("bold", "--font-weight-bold", "700: declared, little used."),
]:
    if vname in L:
        fam_w = var(vname, "fontWeight", description=desc)
        wgt[key] = fam_w

# ------------------------------------------------- core scales (both themes)
# Values identical in the light and dark passes live in core.

palette = SPEC["core"].setdefault("color", {}).setdefault("tailwind", {})
for n in sorted(set(L) & set(D)):
    m = re.fullmatch(r"--color-([a-z]+)-(\d+)", n)
    if m and L[n] == D[n]:
        hue, step = m.groups()
        palette.setdefault(hue, {})[step] = var(n, "color",
            description=f"Tailwind {hue} {step} (declared palette, identical in both themes).")
for n in ("--color-black", "--color-white"):
    if n in L and L[n] == D[n]:
        palette[n.split("-")[-1]] = {"default": var(n, "color", description=f"Declared {n} (identical in both themes).")}

# The --darken-* overlay ramp is declared identically in both themes (black
# translucency); --lighten-* resolves only in the dark pass and lives there.
overlay = palette.setdefault("overlay", {})
for n in sorted(set(L) & set(D)):
    m = re.fullmatch(r"--darken-(\d+)", n)
    if m and L[n] == D[n]:
        overlay.setdefault("darken", {})[m.group(1)] = var(n, "color",
            description="Declared black-alpha overlay step (identical in both themes).")

spacing = SPEC["core"].setdefault("spacing", {})
if "--spacing" in L:
    spacing["base"] = var("--spacing", "dimension", description="The 4px spacing base.")

radius = SPEC["core"].setdefault("radius", {})
for key, vname in [("xs", "--radius-xs"), ("sm", "--radius-sm"), ("md", "--radius-md"),
                   ("lg", "--radius-lg"), ("default", "--radius"), ("xl", "--radius-xl"),
                   ("2xl", "--radius-2xl"), ("3xl", "--radius-3xl")]:
    if vname in L:
        radius[key] = var(vname, "dimension", description=f"Declared {vname}.")

text = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key in ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"]:
    vname = f"--text-{key}"
    if vname in L:
        text[key] = var(vname, "dimension", description=f"Declared {vname}.")

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key in ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"]:
    vname = f"--text-{key}--line-height"
    if vname in L:
        lh[key] = var(vname, "number", description=f"Declared line-height ratio for --text-{key}.")
for key, vname in [("tight", "--leading-tight"), ("snug", "--leading-snug"),
                   ("normal", "--leading-normal"), ("relaxed", "--leading-relaxed")]:
    if vname in L:
        lh[key] = var(vname, "number", description=f"Declared {vname}.")

trk = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for key, vname in [("tight", "--tracking-tight"), ("wide", "--tracking-wide"),
                   ("wider", "--tracking-wider"), ("widest", "--tracking-widest")]:
    if vname in L:
        # Keep the declared em: tracking must scale with the text it sits on.
        # The probe's resolved px reading (L[vname]) freezes the em at one
        # font size, so the raw declaration is the token's value.
        raw = RL[vname].get("raw") or L[vname]
        if raw.strip().endswith("em"):
            v = re.sub(r"^(-?)\.(\d)", r"\g<1>0.\2", raw.strip())
            trk[key] = {"value": v, "type": "dimension",
                        "source": f"declared {vname} (em, scales with the font size)", "description": f"Declared {vname}."}
        else:
            trk[key] = var(vname, "dimension", description=f"Declared {vname}.")

blur = SPEC["core"].setdefault("blur", {})
for key, vname in [("xs", "--blur-xs"), ("sm", "--blur-sm"), ("md", "--blur-md"),
                   ("lg", "--blur-lg"), ("xl", "--blur-xl"), ("2xl", "--blur-2xl"), ("3xl", "--blur-3xl")]:
    if vname in L:
        blur[key] = var(vname, "dimension", description=f"Declared {vname} (backdrop and glow blurs).")

cont = SPEC["core"].setdefault("container", {})
for key, vname in [("xs", "--container-xs"), ("sm", "--container-sm"), ("md", "--container-md"),
                   ("lg", "--container-lg"), ("xl", "--container-xl"), ("2xl", "--container-2xl"),
                   ("3xl", "--container-3xl"), ("4xl", "--container-4xl"), ("5xl", "--container-5xl"),
                   ("6xl", "--container-6xl")]:
    if vname in L:
        cont[key] = var(vname, "dimension", description=f"Declared {vname} max width.")

motion = SPEC["core"].setdefault("motion", {})
for key, vname, ty, desc in [
    ("ease-out", "--ease-out", "cubicBezier", "The default out-curve."),
    ("ease-in-out", "--ease-in-out", "cubicBezier", "The in-out curve."),
    ("duration", "--default-transition-duration", "duration", "The default 150ms transition duration."),
    ("timing", "--default-transition-timing-function", "cubicBezier", "The default transition curve."),
]:
    if vname in L:
        motion[key] = var(vname, ty, description=desc)

shadows_core = SPEC["core"].setdefault("shadow", {})
sv = shadow_var("--drop-shadow-sm", L, "light", "Declared --drop-shadow-sm (identical in both themes).")
if sv:
    shadows_core["drop-sm"] = sv

# ------------------------------------------------------- per-theme roles
# The semantic layer re-binds between the light and dark passes.

ROLE_GROUPS = {
    # (group key) -> [(token key, var name, description)]
    "surface": [
        ("background", "--background", "The page field: true black in dark, warm paper #fdfcfb in light."),
        ("card", "--card", "Card surfaces."),
        ("elevated", "--elevated", "Elevated surface (popovers, raised panels)."),
        ("elevated-hover", "--elevated-hover", "Elevated surface, hovered."),
        ("muted", "--muted", "Muted fill: quiet rows and chips."),
        ("secondary", "--secondary", "Secondary fill."),
        ("secondary-hover", "--secondary-hover", "Secondary fill, hovered."),
        ("accent", "--accent", "Accent fill (hover washes)."),
        ("popover", "--popover", "Popover/dropdown surface."),
        ("popover-solid", "--popover-solid", "Solid popover surface."),
        ("surface-1", "--surface-1", "The app's first raised surface."),
        ("surface-2", "--surface-2", "The app's second raised surface."),
        ("sidebar", "--sidebar", "The left-rail field."),
        ("overlay", "--overlay", "Translucent overlay wash."),
        ("overlay-backdrop", "--overlay-backdrop", "The modal scrim."),
        ("composer", "--composer", "The composer's translucent field."),
        ("composer-panel", "--composer-panel", "The composer panel surface."),
        ("composer-panel-inset", "--composer-panel-inset", "The composer panel's inset."),
        ("composer-surface", "--composer-surface", "The composer surface."),
        ("composer-solid", "--composer-solid", "The solid composer surface."),
        ("composer-chip", "--composer-chip", "Prompt-chip fill."),
        ("composer-chip-hover", "--composer-chip-hover", "Prompt-chip fill, hovered."),
        ("composer-button", "--composer-button", "The composer buttons' fill."),
        ("destructive-soft", "--destructive-soft", "Soft destructive surface."),
    ],
    "ink": [
        ("foreground", "--foreground", "Primary text and glyphs."),
        ("card-foreground", "--card-foreground", "Text on cards."),
        ("muted-foreground", "--muted-foreground", "Muted text: subtitles, metadata."),
        ("primary-foreground", "--primary-foreground", "Text on the primary fill."),
        ("secondary-foreground", "--secondary-foreground", "Text on the secondary fill."),
        ("accent-foreground", "--accent-foreground", "Text on the accent fill."),
        ("popover-foreground", "--popover-foreground", "Text on popovers."),
        ("sidebar-foreground", "--sidebar-foreground", "Rail text (the muted row labels)."),
        ("sidebar-accent-foreground", "--sidebar-accent-foreground", "Text on the rail's accent fill."),
        ("sidebar-primary-foreground", "--sidebar-primary-foreground", "Text on the rail's primary fill."),
        ("composer-fg-muted", "--composer-fg-muted", "Muted text inside the composer."),
        ("destructive-foreground", "--destructive-foreground", "Text on the destructive fill."),
        ("destructive-soft-foreground", "--destructive-soft-foreground", "Text on the soft destructive surface."),
        ("subtle", "--subtle", "The most quiet text/line tint."),
    ],
    "action": [
        ("primary", "--primary", "The primary fill — white in dark (inverted), black in light."),
        ("primary-hover", "--primary-hover", "The primary fill, hovered."),
        ("brand", "--brand", "The ElevenLabs brand blue (charts, links, the badge)."),
        ("brand-foreground", "--brand-foreground", "Text on the brand fill."),
        ("destructive", "--destructive", "Destructive fill."),
        ("success", "--success", "Success green."),
        ("sidebar-primary", "--sidebar-primary", "The rail's primary fill."),
    ],
    "border": [
        ("border", "--border", "The hairline: white 10% in dark, warm-brown 8% in light."),
        ("input", "--input", "Field and control outlines."),
        ("outline", "--outline", "The --outline hairline."),
        ("sidebar-border", "--sidebar-border", "The rail's hairline."),
        ("composer-hairline", "--composer-hairline", "The composer's hairline."),
        ("composer-ring", "--composer-ring", "The composer's ring."),
        ("slider-track", "--slider-track", "The slider/progress track."),
        ("field-border-focus", "--field-border-focus", "The field border on focus."),
    ],
    "focus": [
        ("ring", "--ring", "The focus-ring ink."),
        ("sidebar-ring", "--sidebar-ring", "The rail's focus ring."),
    ],
}

for theme, theme_map in (("light", L), ("dark", D)):
    tset = SPEC[theme]
    for gname, rows in ROLE_GROUPS.items():
        g = tset.setdefault("color", {}).setdefault(gname, {})
        for key, vname, desc in rows:
            if vname in theme_map:
                g[key] = var(vname, "color", description=desc)

    # The Tailwind aliases of the same roles (--color-background, ...).
    role = tset["color"].setdefault("role", {})
    for key, vname, desc in [
        ("background", "--color-background", "Tailwind alias of --background."),
        ("foreground", "--color-foreground", "Tailwind alias of --foreground."),
        ("primary", "--color-primary", "Tailwind alias of --primary."),
        ("muted-foreground", "--color-muted-foreground", "Tailwind alias of --muted-foreground."),
        ("border", "--color-border", "Tailwind alias of --border."),
        ("destructive", "--color-destructive", "Tailwind alias of --destructive."),
    ]:
        if vname in theme_map:
            role[key] = var(vname, "color", description=desc)

    chart = tset["color"].setdefault("chart", {})
    for i in range(1, 6):
        vname = f"--chart-{i}"
        if vname in theme_map:
            chart[str(i)] = var(vname, "color", description=f"Declared chart colour {i}.")

    alpha = tset["color"].setdefault("alpha", {})
    for n in sorted(theme_map):
        m = re.fullmatch(r"--gray-alpha-(\d+)", n)
        if m:
            alpha[f"gray-{m.group(1)}"] = var(n, "color",
                description="The warm-grey alpha ramp (light) / white-alpha ramp (dark).")
        m = re.fullmatch(r"--lighten-(\d+)", n)
        if m:
            alpha[f"lighten-{m.group(1)}"] = var(n, "color",
                description="White-alpha lift step; resolves in the dark theme only.")

    sh = tset.setdefault("shadow", {})
    for key, vname, desc in [
        ("e1", "--shadow-e1", "Elevation 1: the hairline-plus-drop pairing."),
        ("e2", "--shadow-e2", "Elevation 2: the popover/card drop."),
        ("lift-1", "--lift-1", "Lift 1."),
        ("lift-2", "--lift-2", "Lift 2: the card drop."),
        ("lift-3", "--lift-3", "Lift 3: the composer/dialog elevation."),
        ("surface", "--surface-shadow", "The surface shadow."),
        ("popover", "--popover-shadow", "The popover drop."),
        ("elevated", "--elevated-shadow", "The elevated-surface shadow."),
        ("app-card", "--app-card-shadow", "The app-card shadow."),
    ]:
        s = shadow_var(vname, theme_map, theme, desc)
        if s:
            sh[key] = s

# ------------------------------------------------------------ components
# Measured geometry and the type ramp, theme-independent.

comp = SPEC["component"]
geo = comp.setdefault("geometry", {})
for key, cname, state, prop, desc in [
    ("sidebar-width", "sidebar", "default", "rect.w", "The fixed left rail's width."),
    ("header-height", "header", "default", "rect.h", "The app header's height."),
    ("nav-row-height", "sidebar-nav", "default", "rect.h", "A primary nav row's height."),
    ("nav-pill-height", "nav-link", "default", "rect.h", "A header nav pill's height."),
    ("button-height", "signin-btn", "default", "rect.h", "The 32px button step (Sign in, Start free)."),
    ("icon-button", "icon-button", "default", "rect.h", "The 30px icon-button step."),
    ("icon-button-lg", "sidebar-collapse", "default", "rect.h", "The 32px icon-button step."),
    ("play-circle", "play-hero", "default", "rect.h", "The round play button's diameter."),
    ("chip-height", "prompt-chip", "default", "rect.h", "The prompt chip's height."),
    ("tab-height", "seg-tab-on", "default", "rect.h", "The segmented tab's height."),
    ("field-height", "composer-field", "default", "rect.h", "The composer field's height."),
    ("track-row-height", "track-row", "default", "rect.h", "A song row's height."),
    ("track-card-width", "track-card", "default", "rect.w", "A shelf track card's width."),
    ("auth-button-height", "sso-google", "default", "rect.h", "The SSO button's height."),
    ("mobile-tabbar", "m-tab-bar", "default", "rect.h", "The phone bottom tab bar's height."),
]:
    try:
        r = C[cname]["states"][state]["rect"]
        v = r["w"] if prop == "rect.w" else r["h"]
        geo[key] = {"value": v, "type": "dimension",
                    "source": f"computed rect of {cname} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass

rad = comp.setdefault("radius", {})
for key, cname, state, desc in [
    ("button", "signin-btn", "default", "The 32px buttons' radius."),
    ("nav-pill", "nav-link", "default", "The nav pills' radius."),
    ("chip", "prompt-chip", "default", "The prompt chips' radius."),
    ("field", "composer-field", "default", "The composer field's radius."),
    ("tab", "seg-tab-on", "default", "The segmented tab's radius."),
    ("track-card", "track-card", "default", "The track card's radius."),
    ("plan-card", "plan-card", "default", "The plan card's radius."),
    ("auth-card", "auth-card", "default", "The auth column's radius."),
    ("dropdown", "nav-dropdown", "default", "The dropdown panel's radius."),
]:
    try:
        v = st(cname, state)["borderTopLeftRadius"]
        m = re.fullmatch(r"(-?[\d.e+]+)px", v or "")
        if m and float(m.group(1)) > 9999:
            v = "9999px"  # calc(infinity*1px) — a full pill
        rad[key] = {"value": v, "type": "dimension",
                    "source": f"computed borderTopLeftRadius of {cname} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass

typ = comp.setdefault("typography", {})
for key, cname, state, props_, desc in [
    ("display", "hero-title", "default", ("fontFamily", "fontSize", "fontWeight", "letterSpacing"),
     "The waldenburg display headline."),
    ("page-title", "explore-title", "default", ("fontFamily", "fontSize", "fontWeight", "letterSpacing"),
     "A page heading."),
    ("body", "hero-lede", "default", ("fontFamily", "fontSize", "fontWeight", "letterSpacing"),
     "The muted lede/body text."),
    ("label", "nav-link", "default", ("fontFamily", "fontSize", "fontWeight", "letterSpacing"),
     "A nav/button label."),
    ("meta", "artist-link", "default", ("fontFamily", "fontSize", "fontWeight", "letterSpacing"),
     "Small metadata text."),
]:
    try:
        s = st(cname, state)
        t = C[cname]["states"][state].get("textStyle") or s
        entry = {}
        for p in props_:
            if p in t:
                ty = {"fontSize": "dimension", "fontWeight": "fontWeight",
                      "fontFamily": "fontFamily", "letterSpacing": "dimension"}[p]
                v = t[p]
                if p == "letterSpacing" and v in ("normal", ""):
                    continue
                entry[p] = {"value": v, "type": ty,
                            "source": f"computed {p} of {cname} {state} (raw/components-computed.json)",
                            "description": desc}
        typ[key] = entry
    except KeyError:
        pass

states = comp.setdefault("state", {})
try:
    s = st("nav-link", "focus-visible")
    if s.get("outlineStyle") not in (None, "none") and float(s["outlineWidth"].replace("px", "")) > 0:
        states["focus-width"] = {"value": s["outlineWidth"], "type": "dimension",
            "source": "computed outlineWidth of nav-link focus-visible (raw/components-computed.json)",
            "description": "The measured keyboard-focus outline width."}
        states["focus-offset"] = {"value": s["outlineOffset"], "type": "dimension",
            "source": "computed outlineOffset of nav-link focus-visible (raw/components-computed.json)",
            "description": "The measured keyboard-focus outline offset."}
except (KeyError, ValueError):
    pass
try:
    s = st("prompt-chip", "default")
    if s.get("transitionDuration") not in (None, "0s", ""):
        states["transition"] = {"value": s["transitionDuration"], "type": "duration",
            "source": "computed transitionDuration of prompt-chip default (raw/components-computed.json)",
            "description": "A measured control transition."}
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and not ("value" in d or "var" in d or "$value" in d) else 1


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
