#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

doctronic.ai is a Next.js app whose stylesheets declare a real, named design-
token layer (harvested to raw/css-vars.json by tools/capture/vars.mjs):

  primitives   --color-neutral/blue/sage/lime/success/warning/error-50..950
               and --color-white, literal hex on :root
  semantics    --color-surface-*/fg-*/border-*/divider-*/solid-*/link-*/
               accent-*/success-*/warning-*/error-*/info-*/icon-*/
               graphic-blue-*/wash-* — declared on :root (light) and
               redeclared on [data-theme="dark"], each either a plain
               var(--primitive) or an hsl(from <prim> … / α) derivation
  type         --font-display/-sans/-mono stacks (declared on the font-
               loader's ._variable classes) and the 70 --text-* composite
               font shorthands (400 1rem/1.4 var(--font-sans) …) on :root
               in @layer tokens
  shadow       --shadow-xs..xl, --shadow-focus-ring (themed), the
               --shadow-brand-glow pair
  extras       --header-height, --tap-target-min, --tracking-*, the
               --chat-sheet-accent-gradient sweep and the skeleton gradient

A leaf is {"var": ...} (resolved per theme by build_tokens.py) or
{"value": ..., "source": ...} for a parsed/measured value. A semantic whose
declaration is a plain var(--x) becomes an alias {color.<path>} into the
core ramp or a sibling semantic; the hsl(from …) derivations stay var-
referenced, which records the relationship in the source string. Values
that are not colours on a surface — the measured component readings in
raw/components-computed.json — land under core.measured and component.*.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
RULES = V["theme"]
C = {}
_cp = RAW / "components-computed.json"
if _cp.exists():
    C = json.loads(_cp.read_text()).get("components", {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. doctronic.ai's "
    "stylesheets declare a named token layer (@layer tokens): the colour "
    "ramps and the composite --text-* font tokens on :root, the semantic "
    "--color-* roles on :root for light and redeclared under "
    "[data-theme=\"dark\"] for the site's real dark theme "
    "(localStorage.theme, applied to data-theme by an init script). "
    "Semantic declarations that are a plain var(--primitive) become "
    "{color.*} aliases; the hsl(from … / alpha) derivations stay "
    "var-referenced. The measured extras under core.measured and "
    "light.component.* come from raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def declared(sel):
    """Last declaration of each name on the given selector (stylesheet order)."""
    out = {}
    for r in RULES:
        if r["selector"] == sel:
            out.update(r["properties"])
    return out


DECL_ROOT = declared(":root")
DECL_DARK = declared('[data-theme="dark"]')
DECL_ANY = {}   # names on other selectors (the font-loader ._variable classes)
for r in RULES:
    for k, v in r["properties"].items():
        if k not in DECL_ROOT and k not in DECL_DARK:
            DECL_ANY[k] = (v, r["selector"])


def px_of(v):
    m = re.fullmatch(r"([\d.]+)px", str(v).strip())
    return "%gpx" % float(m.group(1)) if m else None


def res(name, theme="light"):
    e = RES.get(theme, {}).get(name)
    return (e or {}).get("value", (e or {}).get("raw"))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    return node, parts[-1]


def emit(root, path, leaf):
    node, last = descend(root, path.split("."))
    node[last] = leaf


# ---------------------------------------------------------------- core colours

RAMP = re.compile(r"^--color-(neutral|blue|sage|lime|success|warning|error)-(\d+)$")
core_color = {}
SPEC["core"]["color"] = core_color
for name in sorted(DECL_ROOT):
    m = RAMP.match(name)
    if m:
        emit(core_color, f"{m.group(1)}.{m.group(2)}",
             var(name, "color", source=f"css-var {name} (:root @layer tokens)",
                 description=f"The {m.group(1)} ramp's {m.group(2)} step."))
if "--color-white" in DECL_ROOT:
    emit(core_color, "white", var("--color-white", "color",
        source="css-var --color-white (:root)",
        description="The white every raised surface and accent label paints."))
# the decorative washes and the graphic-blue tint ramp, declared as literals/aliases
for name, desc in [
    ("--color-wash-lavender-soft", "A soft lavender decorative wash."),
    ("--color-wash-lavender-deep", "The deeper lavender wash."),
    ("--color-wash-sky", "A pale sky wash."),
    ("--color-wash-sage", "A pale sage wash."),
]:
    if name in DECL_ROOT:
        emit(core_color, name[len("--color-"):].replace("-", "."),
             var(name, "color", source=f"css-var {name} (:root @layer tokens)", description=desc))
for name in sorted(DECL_ROOT):
    m = re.fullmatch(r"--color-graphic-blue-(\w+)", name)
    if m:
        decl = DECL_ROOT[name].strip()
        tgt = re.fullmatch(r"var\(--color-blue-(\d+)\)", decl)
        leaf = {"value": "{color.blue.%s}" % tgt.group(1), "type": "color",
                "source": f"css-var {name} = var(--color-blue-{tgt.group(1)})",
                "description": f"The blue illustration ramp's {m.group(1)} step, the blue ramp's {tgt.group(1)}."} if tgt \
            else var(name, "color", source=f"css-var {name}", description=f"The blue illustration ramp's {m.group(1)} step.")
        emit(core_color, f"graphic-blue.{m.group(1)}", leaf)

# ------------------------------------------------------------------ semantics

# Map a css-var name to its token path: primitives live in core, semantics in
# the theme set — a plain var() declaration becomes an alias to either.
def path_of(name):
    s = name[len("--color-"):] if name.startswith("--color-") else name.lstrip("-")
    m = RAMP.match(name)
    if m:
        return f"color.{m.group(1)}.{m.group(2)}"
    if s == "white":
        return "color.white"
    if s.startswith("graphic-blue-"):
        return "color.graphic-blue." + s[len("graphic-blue-"):]
    if s.startswith("wash-"):
        return "color.wash." + s[len("wash-"):]
    # semantic: first segment is the group, the rest joined with '-'
    parts = s.split("-", 1)
    return f"color.{parts[0]}.{parts[1]}" if len(parts) == 2 else f"color.{parts[0]}"


GROUPS = ("surface", "fg", "border", "divider", "solid", "link", "accent",
          "success", "warning", "error", "info", "icon", "chat-sheet")
for theme, decls in (("light", DECL_ROOT), ("dark", DECL_DARK)):
    bag = SPEC[theme].setdefault("color", {})
    for name, decl in sorted(decls.items()):
        if not name.startswith("--color-") or RAMP.match(name) or name == "--color-white" \
                or name.startswith(("--color-graphic-", "--color-wash-")):
            continue
        path = path_of(name)
        d = decl.strip()
        tgt = re.fullmatch(r"var\((--color-[\w-]+)\)", d)
        if tgt and tgt.group(1) in DECL_ROOT:
            tp = path_of(tgt.group(1))
            leaf = {"value": "{" + tp + "}", "type": "color",
                    "source": f"css-var {name} = var({tgt.group(1)}) ({theme})",
                    "description": f"The {name[len('--color-'):]} role, declared over {tgt.group(1)}."}
        else:
            how = "an hsl(from …) derivation of " + re.search(r"var\((--[\w-]+)\)", d).group(1) \
                if "hsl(from" in d and re.search(r"var\((--[\w-]+)\)", d) \
                else ("a literal declaration" if not d.startswith("var(") else d[:60])
            leaf = var(name, "color",
                       source=f"css-var {name} ({theme}): {how}",
                       description=f"The {name[len('--color-'):]} role.")
        node, last = descend(bag, path.split(".")[1:])
        node[last] = leaf

# chat-sheet accent sweep (the animated gradient under the chat input card)
grad = DECL_ROOT.get("--chat-sheet-accent-gradient", "")
if grad:
    stops = []
    for i, m in enumerate(re.finditer(r"(var\((--[\w-]+)\)|#[0-9a-fA-F]{3,8})\s+([\d.]+)%", grad)):
        c = m.group(1)
        if c.startswith("var("):
            cn = m.group(2)
            c = "{" + path_of(cn) + "}" if cn.startswith("--color-") else res(cn) or c
        stops.append({"color": c, "position": float(m.group(3)) / 100})
    if stops:
        emit(SPEC["core"], "gradient.chat-sheet-accent",
             {"value": stops, "type": "gradient", "angle": "90deg",
              "source": "css-var --chat-sheet-accent-gradient (:root @layer tokens): the blue→sky→green→lime sweep the chat input card's accent border animates",
              "description": "The accent sweep painted around the hero chat input card."})
for theme, decls in (("light", DECL_ROOT), ("dark", DECL_DARK)):
    sk = decls.get("--skeleton-loader-gradient", "")
    stops = []
    for m in re.finditer(r"(var\((--[\w-]+)\)|#[0-9a-fA-F]{3,8})\s+([\d.]+)%", sk):
        c = m.group(1)
        if c.startswith("var("):
            cn = m.group(2)
            c = "{" + path_of(cn) + "}" if cn.startswith("--color-") else res(cn) or c
        stops.append({"color": c, "position": float(m.group(3)) / 100})
    if stops:
        emit(SPEC[theme], "gradient.skeleton",
             {"value": stops, "type": "gradient", "angle": "90deg",
              "source": f"css-var --skeleton-loader-gradient ({theme}): the loading shimmer sweep",
              "description": "The skeleton shimmer sweep."})

# ------------------------------------------------------------------ typography

fam = {}
SPEC["core"]["font"] = {"family": fam}
for key, name, desc in [
    ("display", "--font-display", "The Fraunces face the display, italic and oath text is set in."),
    ("sans", "--font-sans", "The Geist face the UI, headings, body and label text is set in."),
    ("mono", "--font-mono", "The Geist Mono face the mono tokens are set in."),
    ("body", "--font-body", "The system fallback stack the plain body font reads."),
]:
    if name in DECL_ANY:
        v, sel = DECL_ANY[name]
        fam[key] = {"value": v.strip(), "type": "fontFamily",
                    "source": f"css-var {name} declared on {sel}; the @font-face blocks (self-hosted woff2) are in raw/css-vars.json fonts",
                    "description": desc}
    elif name in DECL_ROOT:
        fam[key] = {"value": DECL_ROOT[name].strip(), "type": "fontFamily",
                    "source": f"css-var {name} (:root)", "description": desc}

# the --text-* composite shorthands: "italic? WEIGHT SIZErem/LH var(--font-x)"
SHORT = re.compile(r"^(italic )?(\d{3}) ([\d.]+)rem/([\d.]+) var\(--font-(\w+)\)$")
typ = {}
SPEC["core"]["typography"] = typ
GROUP_LABEL = {"display": "Display (Fraunces)", "italic": "Italic display (Fraunces)",
               "heading": "Heading (Geist 600)", "heading-italic": "Italic heading (Geist 600)",
               "body": "Body (Geist 400)", "label": "Label (Geist 500)",
               "mono": "Mono (Geist Mono 400)", "mono-bold": "Mono bold (Geist Mono 600)"}
for name, decl in sorted(DECL_ROOT.items()):
    m = re.fullmatch(r"--text-((?:heading-)?(?:italic|display|body|label|mono|mono-bold))-(\d+)", name)
    if not m:
        continue
    g = SHORT.match(decl.strip())
    if not g:
        continue
    italic, weight, size, lh, ff = g.groups()
    role, step = m.group(1), m.group(2)
    node = typ.setdefault(role, {})
    node[step] = {"type": "typography",
                  "value": {"fontFamily": "{font.family.%s}" % ff,
                            "fontSize": "%gpx" % (float(size) * 16),
                            "lineHeight": "%gpx" % round(float(size) * 16 * float(lh), 2),
                            "fontWeight": int(weight)} | ({"fontStyle": "italic"} if italic else {}),
                  "source": f"css-var {name} (:root @layer tokens): \"{decl.strip()}\"",
                  "description": f"{GROUP_LABEL.get(role, role)} at {float(size)*16:g}px."}

track = {}
for name in ("--tracking-display", "--tracking-tight"):
    if name in DECL_ROOT:
        track[name[len("--tracking-"):]] = {"value": DECL_ROOT[name].strip(), "type": "other",
                                           "source": f"css-var {name} (:root @layer tokens)",
                                           "description": "The display/tight letter-spacing."}
if track:
    SPEC["core"]["tracking"] = track

# -------------------------------------------------------------------- shadows

SH = re.compile(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?( inset)?")


def parse_shadow(v):
    layers = []
    for a, x, y, b, sp, i in SH.findall(str(v)):
        layers.append({"color": a, "offsetX": x + "px", "offsetY": y + "px",
                       "blur": b + "px", "spread": (sp or "0") + "px", "inset": bool(i)})
    return layers or None


shadow = {}
for name, desc in [
    ("--shadow-xs", "The hairline 1px lift."),
    ("--shadow-sm", "The 1px/12px soft lift."),
    ("--shadow-md", "The 2px/12px card lift — the chat input card carries it."),
    ("--shadow-lg", "The 2px/24px raised lift."),
    ("--shadow-xl", "The 5px/32px overlay lift."),
    ("--shadow-brand-glow", "The blue glow the accent button paints."),
    ("--shadow-brand-glow-hover", "The stronger glow on hover."),
]:
    e = RES["light"].get(name)
    if e and e.get("value"):
        layers = parse_shadow(e["value"])
        if layers:
            shadow[name[len("--shadow-"):]] = {"value": layers, "type": "shadow",
                                               "source": f"css-var {name} resolved (:root @layer tokens): \"{e['raw']}\"",
                                               "description": desc}
if shadow:
    SPEC["core"]["shadow"] = shadow
for theme in ("light", "dark"):
    e = RES[theme].get("--shadow-focus-ring")
    if e and e.get("value"):
        layers = parse_shadow(e["value"])
        if layers:
            emit(SPEC[theme], "shadow.focus-ring",
                 {"value": layers, "type": "shadow",
                  "source": f"css-var --shadow-focus-ring resolved {theme}: \"{e['raw']}\"",
                  "description": "The 2px accent keyboard ring."})

# -------------------------------------------------------------------- sizing

for name, path, desc in [
    ("--header-height", "layout.header-height", "The 72px marketing top bar."),
    ("--tap-target-min", "layout.tap-target-min", "The 44px minimum tap target."),
]:
    if name in DECL_ROOT:
        emit(SPEC["core"], path,
             var(name, "dimension", source=f"css-var {name} (:root)", description=desc))


# ------------------------------------------------------------------ measured

def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    try:
        c = C[comp]["states"][state]
        v = (c.get("textStyle") or {}).get(prop)
        return v or c["style"].get(prop)
    except KeyError:
        return None


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, desc in [
    ("control-transition", "signup-button", "default", "The control transition the header actions run."),
    ("navlink-transition", "nav-pill", "default", "The pill link's transition."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"].split(",")[0].strip()
        if d and d != "0s":
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} default (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "signup-button", "focus-visible", "outlineColor", "color", "The keyboard focus colour on the header actions (auto outline)."),
]:
    if have(comp, state, prop):
        meas[key] = {"value": norm_color(st(comp, state)[prop]), "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

# ------------------------------------------------------------ component sizes

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "signup-button", "default", "height", "The header Sign up button height."),
    ("button-cta.height", "start-chat-button", "default", "height", "The hero Start chat button height."),
    ("button-cta.radius", "start-chat-button", "default", "borderTopLeftRadius", "The Start chat button radius."),
    ("send.height", "send-button", "default", "height", "The chat composer Send control height."),
    ("inputcard.radius", "input-card", "default", "borderTopLeftRadius", "The chat input card's radius."),
    ("inputcard.height", "input-card", "default", "height", "The chat input card's resting height."),
    ("starter.height", "starter", "default", "height", "A suggestion chip's height."),
    ("starter.radius", "starter", "default", "borderTopLeftRadius", "The suggestion chip's pill radius."),
    ("navpill.radius", "nav-pill", "default", "borderTopLeftRadius", "The top-bar pill link's radius."),
    ("sidebar.width", "chat-sidebar-open", "default", "width", "The expanded chat rail's width."),
    ("sidebar-collapsed.width", "chat-sidebar", "default", "width", "The collapsed rail's width."),
    ("dialog.radius", "signin-dialog", "default", "borderTopLeftRadius", "The sign-in dialog's radius."),
    ("dialog.width", "signin-dialog", "default", "width", "The sign-in dialog's width."),
    ("header.height", "header", "default", "height", "The measured top-bar height (the declared --header-height is 72px)."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
