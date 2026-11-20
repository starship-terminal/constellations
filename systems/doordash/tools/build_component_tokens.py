#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Sources, captured from archived doordash.com SSR pages on 2026-11-13:
  raw/css-vars.json          every custom property the pages declare — the
                             prism design-token system scoped to
                             :where(.prism-theme): --base-* primitives
                             (colour ramps incl. the doordash/caviar/dashpass
                             brand palettes and a 28-step DD Norms type
                             scale), --usage-* semantic roles (colour, type,
                             space, size, radius, elevation, motion) and
                             --comp-* component tokens (button, field, tag,
                             toggle, banner, …) — declared as var() aliases
                             comp → usage → base. Plus the careers site's
                             WordPress/Tailwind layer, binned separately and
                             not tokenised here.
  raw/components-computed.json
                             measured components (the public surface's real
                             geometry and paints) for the values not carried
                             by a variable

DoorDash's consumer web paints one light theme — the prism sheet also ships
sibling brand themes (deliveroo, plus, each light and dark) under
[data-dt-theme][data-dt-mode] scopes a doordash.com visitor never gets, so
the export holds `core` (primitives + theme-invariant roles) and `light`
(semantic roles and the component layer) only.

A leaf is {"var": "--name"} (resolved by build_tokens.py from
css-vars.json's resolved.light), {"value": "{token.path}"} when the winning
declaration is a plain var() alias whose target is itself a token with the
same resolved value (the prism alias chain is preserved as DTCG aliases),
{"value": ..., "source": "..."} for a measured value, or a pre-built DTCG
leaf for typography composites built from the --usage-type-* slots.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
# computed value of each resolved name
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
KIND = {n: v.get("kind") for n, v in RL.items()}

# The winning declaration of each name across the prism theme blocks, in
# stylesheet order. Usage/comp vars are declared inside :where(.prism-theme)
# (and a few on :root / html.prism-theme); anything under a @media context
# other than the unparsed passes is noted as responsive in the source string.
DECL = {}
DECL_WHERE = {}
PRISM = re.compile(r":where\(\.prism-theme\)|^:root$|html\.prism-theme|\.prism-theme")
for r in V.get("theme", []) + V.get("app", []):
    sel = r.get("selector") or ""
    if not PRISM.search(sel):
        continue
    ctx = [c for c in r.get("context", []) if not c.startswith("@layer")]
    for k, v in r["properties"].items():
        DECL[k] = v.strip()
        DECL_WHERE[k] = (sel, ctx)

SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. DoorDash's "
        "consumer web declares the prism token system on :where(.prism-theme): "
        "--base-* primitives (brand/hue/neutral colour ramps, a DD Norms type "
        "scale, a 32-step size scale, weights, tracking, leading), --usage-* "
        "semantic roles aliasing them, and --comp-* component tokens aliasing "
        "the roles. The surface paints light only. Declared variables become "
        "var leaves (resolved values) or {path} leaves when the winning "
        "declaration is a plain var() alias of a token with the same resolved "
        "value; measured leaves come from raw/components-computed.json."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, parts, leaf):
    node, last = descend(root, parts)
    node[last] = leaf


# ------------------------------------------------------------- name -> path
# Map every prism variable name onto its (set, path-parts). Anything outside
# these prefixes (scoped --btn-*, --i3ez6m5-* generated vars, layout one-offs)
# stays evidence in css-vars.json, not a token.

def path_of(name):
    n = name[2:]
    def parts(pre, root):
        return root + n[len(pre):].split("-")
    def tail(pre, root):
        # single-suffix prefixes: the rest of the name is the last path part.
        # len(pre), never a magic offset — a hardcoded slice here dropped the
        # first suffix character once before (font.lineHeight.10 -> .0).
        return root + [n[len(pre):]]
    if n.startswith("base-color-"):
        return "core", parts("base-color-", ["color"])
    if n.startswith("base-font-family-"):
        return "core", tail("base-font-family-", ["font", "family"])
    if n.startswith("base-font-size-"):
        return "core", tail("base-font-size-", ["font", "size"])
    if n.startswith("base-font-weight-"):
        return "core", tail("base-font-weight-", ["font", "weight"])
    if n.startswith("base-line-height-"):
        return "core", tail("base-line-height-", ["font", "lineHeight"])
    if n.startswith("base-letter-spacing-"):
        return "core", tail("base-letter-spacing-", ["font", "tracking"])
    if n.startswith("base-size-"):
        return "core", tail("base-size-", ["size"])
    if n.startswith("base-motion-duration-"):
        return "core", tail("base-motion-duration-", ["motion", "duration"])
    if n.startswith("base-motion-easing-"):
        return "core", tail("base-motion-easing-", ["motion", "easing"])
    if n.startswith("usage-color-"):
        return "light", parts("usage-color-", ["color"])
    if n.startswith("usage-type-"):
        return "light", parts("usage-type-", ["type"])
    # The generic usage type aliases nest under light.type.* with the
    # per-role slots (a light.font.* would land on core.font.*'s CSS names).
    if n.startswith("usage-font-family-"):
        return "light", tail("usage-font-family-", ["type", "font", "family"])
    if n.startswith("usage-font-size-"):
        return "light", tail("usage-font-size-", ["type", "font", "size"])
    if n.startswith("usage-font-weight-"):
        return "light", tail("usage-font-weight-", ["type", "font", "weight"])
    if n.startswith("usage-line-height-"):
        return "light", tail("usage-line-height-", ["type", "lineHeight"])
    if n.startswith("usage-letter-spacing-"):
        return "light", tail("usage-letter-spacing-", ["type", "tracking"])
    if n.startswith("usage-space-"):
        return "core", tail("usage-space-", ["spacing"])
    if n.startswith("usage-size-"):
        return "light", tail("usage-size-", ["size"])
    if n.startswith("usage-border-radius-"):
        return "core", tail("usage-border-radius-", ["radius"])
    if n.startswith("usage-border-width-"):
        return "core", tail("usage-border-width-", ["borderWidth"])
    if n.startswith("usage-elevation-"):
        return "core", tail("usage-elevation-", ["elevation"])
    if n.startswith("usage-motion-duration-"):
        return "core", tail("usage-motion-duration-", ["motion", "duration"])
    if n.startswith("usage-motion-easing-"):
        return "core", tail("usage-motion-easing-", ["motion", "easing"])
    if n.startswith("usage-motion-delay-"):
        return "core", tail("usage-motion-delay-", ["motion", "delay"])
    if n.startswith("usage-motion-scale-"):
        return "core", tail("usage-motion-scale-", ["motion", "scale"])
    if n.startswith("comp-color-"):
        return "light", parts("comp-color-", ["comp", "color"])
    if n.startswith("comp-type-"):
        return "light", parts("comp-type-", ["comp", "type"])
    if n.startswith("comp-space-"):
        return "light", parts("comp-space-", ["comp", "space"])
    if n.startswith("comp-size-"):
        return "light", parts("comp-size-", ["comp", "size"])
    if n.startswith("comp-border-radius-"):
        return "light", tail("comp-border-radius-", ["comp", "radius"])
    if n.startswith("comp-border-width-"):
        return "light", tail("comp-border-width-", ["comp", "borderWidth"])
    if n.startswith("comp-elevation-"):
        return "light", tail("comp-elevation-", ["comp", "elevation"])
    if n.startswith("comp-motion-duration-"):
        return "light", tail("comp-motion-duration-", ["comp", "motion", "duration"])
    if n.startswith("comp-motion-easing-"):
        return "light", tail("comp-motion-easing-", ["comp", "motion", "easing"])
    if n.startswith("surface-color-"):
        return "light", parts("surface-color-", ["surface"])
    if n.startswith("prism-"):
        return "core", parts("prism-", ["prism"])
    return None, None


KIND_TYPE = {"color": "color", "dimension": "dimension", "duration": "duration",
             "easing": "cubicBezier", "shadow": "shadow", "fontFamily": "fontFamily",
             "number": "number"}


def ty_of(name):
    if re.match(r"--(base|usage)-font-weight-|--usage-type-.*-font-weight", name):
        return "fontWeight"
    if re.search(r"-(font-family)$", name):
        return "fontFamily"
    if name.startswith("--usage-elevation-") or name.startswith("--comp-elevation-"):
        return "shadow"
    if re.search(r"-(easing)(-|$)", name):
        return "cubicBezier"
    if re.search(r"-(duration|delay)(-|$)", name):
        return "duration"
    if re.search(r"-text-(decoration|transform)$", name):
        # "none"/"underline" resolve to the resolver's shadow bucket; they are
        # text keywords, not shadows.
        return "string"
    k = KIND.get(name)
    return KIND_TYPE.get(k, "string" if k in (None, "other") else k)


def src_of(name):
    sel, ctx = DECL_WHERE.get(name, (None, []))
    where = "css-var %s" % name
    if sel:
        where += " declared on `%s`" % sel[:90]
        if ctx:
            where += " under " + " ".join(ctx)[:80]
    return where


PATHS = {}   # css name -> (set, dotpath)
for name in R:
    st, parts = path_of(name)
    if st:
        PATHS[name] = (st, ".".join(parts))

SKIP = set()


def leaf_for(name):
    """var() alias -> {path} leaf when the target is tokenised and the resolved
    values agree; otherwise a var leaf the builder resolves."""
    d = DECL.get(name)
    if d:
        m = re.fullmatch(r"var\((--[\w-]+)\)", d)
        if m and m.group(1) in PATHS and m.group(1) not in SKIP:
            st, dp = PATHS[m.group(1)]
            if R.get(m.group(1)) == R.get(name):
                return {"value": "{%s}" % dp, "type": ty_of(name),
                        "source": "%s → `%s` (prism alias)" % (src_of(name), d)}
    return {"var": name, "type": ty_of(name), "source": src_of(name)}


EMITTED = {}   # (set, dotpath) -> css name; a repeat means path_of collapsed two names
for name in sorted(R):
    st, parts = path_of(name)
    if not st or name in SKIP:
        continue
    key = (st, ".".join(parts))
    if key in EMITTED:
        raise SystemExit("path_of maps %s and %s onto the same %s.%s token — fix the prefix slicing" % (EMITTED[key], name, st, key[1]))
    EMITTED[key] = name
    emit(SPEC[st], parts, leaf_for(name))

# ------------------------------------------------------------ typography
# The --usage-type-* slots compose into one DTCG typography token per
# role/size/variant (body-large, display-condensed-large, title-medium, …).

ROLE = re.compile(r"--usage-type-(.+?)-(font-family|font-weight|letter-spacing|line-height|size|text-decoration)$")


def resolve_to_path(name, hops=6):
    """Follow the var() chain to the token path of its base, else None."""
    seen = set()
    cur = name
    for _ in range(hops):
        if cur in seen:
            return None
        seen.add(cur)
        if cur not in PATHS:
            return None
        d = DECL.get(cur, "")
        m = re.fullmatch(r"var\((--[\w-]+)\)", d or "")
        if not m:
            return PATHS[cur][1]
        cur = m.group(1)
    return PATHS.get(cur, (None, None))[1] if cur in PATHS else None


PROP_TOKEN = {"font-family": "fontFamily", "font-size": "fontSize", "font-weight": "fontWeight",
              "line-height": "lineHeight", "letter-spacing": "letterSpacing", "size": "fontSize",
              "text-decoration": "textDecoration"}

combos = {}
for name in R:
    m = ROLE.match(name)
    if m:
        combos.setdefault(m.group(1), {})[m.group(2)] = name
typo = SPEC["core"].setdefault("typography", {})
for slot, props in sorted(combos.items()):
    key = re.sub(r"-default$", "", slot)
    style = {}
    order = [("font-family", "fontFamily"), ("size", "fontSize"), ("line-height", "lineHeight"),
             ("font-weight", "fontWeight"), ("letter-spacing", "letterSpacing")]
    srcs = []
    for prop, field in order:
        vname = props.get(prop)
        if not vname:
            continue
        srcs.append("%s %s" % (prop, vname))
        dp = resolve_to_path(vname)
        if field == "fontWeight":
            # weights stay literal numbers (DD Norms 400-800 scale)
            val = R.get(vname)
            try:
                style[field] = int(float(val))
            except (TypeError, ValueError):
                if dp:
                    style[field] = "{%s}" % dp
        elif dp:
            style[field] = "{%s}" % dp
        else:
            val = R.get(vname)
            if prop == "size":
                m2 = re.fullmatch(r"([\d.]+)px", str(val))
                if m2:
                    style[field] = m2.group(1) + "px"
            elif prop == "line-height":
                m2 = re.fullmatch(r"([\d.]+)px", str(val))
                if m2:
                    style[field] = m2.group(1) + "px"
            elif prop == "letter-spacing":
                style[field] = str(val)
            else:
                style[field] = str(val)
    if not style.get("fontSize"):
        continue
    typo[key] = {"$value": style, "$type": "typography",
                 "$extensions": {"source": "the declared --usage-type-%s-* slots (%s), resolved through the prism alias chain" % (slot, "; ".join(srcs))}}
typo["$description"] = ("The prism type roles (usage-type-*): body, display (condensed for campaign "
                        "headlines), label, link and title, each in large/medium/small and emphasis "
                        "variants, on DD Norms weights 400-800.")

# ------------------------------------------------------------ group docs
SPEC["core"]["color"] = {"$description": "The prism --base-color-* ramps: the doordash, caviar and dashpass brand palettes; neutral and warm/cool greys on a 0-100 scale (with half-steps 15/25/…/95); twelve hue ramps; plus black and white.", **SPEC["core"].get("color", {})}
SPEC["core"]["font"]["$description"] = "DD Norms (proprietary, served from web-assets.cdn4dd.com) over the system stack: --base-font-* families (default = brand = DD Norms, condensed for campaign display), the --base-font-size-* 28-step scale in px, weights 300-800, leading and tracking."
SPEC["core"]["size"]["$description"] = "The --base-size-* 32-step dimension scale (px) every space/size/radius role aliases."
SPEC["core"]["spacing"]["$description"] = "The --usage-space-* semantic spacing steps (none → xxx-large), aliases over the base size scale."
SPEC["core"]["radius"]["$description"] = "The --usage-border-radius-* roles (none → full), aliases over the base size scale — DoorDash pills use radius-full."
SPEC["core"]["borderWidth"]["$description"] = "The --usage-border-width-* roles (default, strong)."
SPEC["core"]["elevation"]["$description"] = "The --usage-elevation-* shadow ladder (none, 1-6)."
SPEC["core"]["motion"]["$description"] = "The --usage-motion-* ladder: auto/functional durations, cubic-bezier easings, delays and the pressed scale."
if "prism" in SPEC["core"]:
    SPEC["core"]["prism"]["$description"] = "Prism system plumbing vars (the font fallback stack and inline-children gap helper)."
SPEC["light"]["color"]["$description"] = "The --usage-color-* semantic roles: text/background/border/icon/action with default-hovered-pressed-disabled states, status (positive/negative/warning/highlight/selected), deal/dashpass/safedash brand roles, media/map/data-viz/overlay surfaces — aliases over the base ramps."
SPEC["light"]["type"]["$description"] = "The --usage-type-* per-role slots the core.typography composites are built from, plus the generic --usage-font-*/-line-height-*/-letter-spacing-* type aliases (all aliasing the base scale)."
SPEC["light"]["size"]["$description"] = "The --usage-size-* sizing scale plus the action-* control heights."
SPEC["light"]["comp"]["$description"] = "The --comp-* component token layer (button, field, tag, toggle, switch, banner, avatar, list, map, pagination, quantity-stepper, side-navigation, table, toast, tooltip, chat, date-picker, progress) — every name an alias down the prism chain."
SPEC["light"]["surface"]["$description"] = "The --surface-color-* brand-primary surface pair (background/foreground × state)."

# ------------------------------------------------------ measured geometry
# The public surface's real geometry and paints, from components-computed.json
# — the --comp-* layer declares the intent; these record what a visitor gets.

def st(comp, state):
    return C[comp]["states"][state]["style"]


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def px(v):
    m = re.fullmatch(r"([\d.]+)px", str(v or "").strip())
    return m.group(1) + "px" if m else None


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        return v.lower()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v or None


comp_tree = SPEC["component"]
comp_tree["$description"] = "Measured on the public components (raw/components-computed.json): the painted geometry the --comp-* token layer produces on the signed-out surface."


def measured(comp, state, prop, token, ty="dimension", transform=None):
    if not have(comp, state, prop):
        return
    v = st(comp, state)[prop]
    src = "computed %s of %s %s (raw/components-computed.json)" % (prop, comp, state)
    if prop == "color":
        # The text colour is the first text node's, as components.md reads it. In the Wayback
        # replay the wrappers kept the browser's inherited defaults (Times, #000000, link blue
        # #0000ee on anchors), which are not DoorDash values.
        t = C[comp]["states"][state].get("textStyle") or {}
        if t.get("color"):
            v = t["color"]
            src = "computed color of %s %s's first text node (%s) (raw/components-computed.json)" % (comp, state, t.get("node") or "text")
        elif st(comp, state).get("fontFamily", "").startswith("Times"):
            src += "; no text node was read and the element kept the browser's inherited defaults in the Wayback replay, so this is not confirmed as a DoorDash value"
    if transform:
        v = transform(v)
    if v is None or v == "none" or v == "rgba(0, 0, 0, 0)":
        return
    parts = token.split(".")
    emit(comp_tree, parts, {"value": v, "type": ty, "source": src})


def pad_lr(s):
    try:
        l, r = s["paddingLeft"], s["paddingRight"]
        if l == r:
            return px(l)
    except KeyError:
        pass
    return None


for key, comp_name in [("signinButton", "signin-btn"), ("signupButton", "signup-btn"),
                       ("ctaButton", "cta-btn"), ("addressPill", "address-pill"),
                       ("quickAdd", "quick-add"), ("cardCta", "card-cta"),
                       ("popularButton", "popular-btn"), ("nearbyCta", "nearby-cta")]:
    if not have(comp_name, "default"):
        continue
    s = st(comp_name, "default")
    measured(comp_name, "default", "height", f"{key}.height")
    measured(comp_name, "default", "width", f"{key}.width")
    lr = pad_lr(s)
    if lr:
        emit(comp_tree, [key, "padding"], {"value": lr, "type": "dimension",
             "source": "computed padding-left/right of %s default" % comp_name})
    measured(comp_name, "default", "borderTopLeftRadius", f"{key}.radius")
    measured(comp_name, "default", "backgroundColor", f"{key}.background", "color", norm_color)
    measured(comp_name, "default", "color", f"{key}.text", "color", norm_color)

for key, comp_name in [("heroBand", "hero-band"), ("appHeader", "app-header"), ("tab", "tab-selected"),
                       ("valueCard", "value-prop-card"), ("restaurantCard", "rest-card"),
                       ("menuItem", "menu-item"), ("offerBadge", "offer-badge"),
                       ("cookieBanner", "cookie-banner"), ("footer", "footer"),
                       ("fulfilToggle", "fulfil-toggle"), ("ctaBand", "cta-band"),
                       ("breadcrumb", "breadcrumb")]:
    if not have(comp_name, "default"):
        continue
    measured(comp_name, "default", "height", f"{key}.height")
    measured(comp_name, "default", "borderTopLeftRadius", f"{key}.radius")
    measured(comp_name, "default", "backgroundColor", f"{key}.background", "color", norm_color)
    measured(comp_name, "default", "color", f"{key}.text", "color", norm_color)

for key, comp_name in [("languageSelect", "language-select"), ("addressField", "address-field"),
                       ("searchField", "search-input"), ("hsaSearch", "hsa-search")]:
    if not have(comp_name, "default"):
        continue
    measured(comp_name, "default", "height", f"{key}.height")
    measured(comp_name, "default", "width", f"{key}.width")
    measured(comp_name, "default", "borderTopLeftRadius", f"{key}.radius")
    measured(comp_name, "default", "backgroundColor", f"{key}.background", "color", norm_color)
    measured(comp_name, "default", "color", f"{key}.text", "color", norm_color)
    measured(comp_name, "default", "borderTopColor", f"{key}.borderColor", "color", norm_color)

# Focus state evidence: the keyboard focus ring (outline) of the primary pill.
if have("signup-btn", "focus-visible", "outlineColor"):
    s = st("signup-btn", "focus-visible")
    emit(comp_tree, ["focusRing", "color"], {"value": norm_color(s["outlineColor"]) or s["outlineColor"],
         "type": "color", "source": "computed outline of signup-btn focus-visible"})
    emit(comp_tree, ["focusRing", "width"], {"value": px(s["outlineWidth"]) or s["outlineWidth"],
         "type": "dimension", "source": "computed outline-width of signup-btn focus-visible"})
elif have("signup-btn", "focus-visible"):
    s = st("signup-btn", "focus-visible")
    if s.get("boxShadow") and s["boxShadow"] != "none":
        emit(comp_tree, ["focusRing", "shadow"], {"value": s["boxShadow"], "type": "string",
             "source": "computed box-shadow of signup-btn focus-visible (prism paints focus as a shadow)"})

# ------------------------------------------------- alias repointing
# A {path} alias written from a var() chain can aim at a name that also
# carries children (--usage-color-background-selected AND
# --usage-color-background-selected-hovered): descend() parked the leaf at
# <name>.default. Repoint every alias that aims at a group to its .default.

def token_paths(root, prefix=""):
    for k, v in root.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict):
            if "var" in v or "value" in v or "$value" in v:
                yield prefix + k
            else:
                yield from token_paths(v, prefix + k + ".")


TOKP = {}
for s in ("core", "light", "component"):
    TOKP[s] = set(token_paths(SPEC[s]))


def repoint(node, avail):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict):
            if "value" in v and isinstance(v["value"], str) and v["value"].startswith("{"):
                p = v["value"][1:-1]
                if p not in avail and p + ".default" in avail:
                    v["value"] = "{%s}" % (p + ".default")
            elif "var" not in v and "value" not in v and "$value" not in v:
                repoint(v, avail)
            elif "$value" in v:
                for kk, vv in v["$value"].items() if isinstance(v["$value"], dict) else []:
                    if isinstance(vv, str) and vv.startswith("{"):
                        p = vv[1:-1]
                        if p not in avail and p + ".default" in avail:
                            v["$value"][kk] = "{%s}" % (p + ".default")


# A light alias may aim at a core token (usage → base), so each set repoints
# against its own paths plus core's.
for s in ("core", "light", "component"):
    repoint(SPEC[s], TOKP[s] | TOKP["core"])

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 0
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


for k in ("core", "light", "component"):
    print(k, count(SPEC[k]))
