#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

kit.com signed out is two surfaces:

  kit.com — a light-only Next.js marketing site on Tailwind CSS v4. The
  declared theme layer (raw/css-vars.json) is a real ramp: --color-soft-black,
  --color-warm-white*, --color-blue-*, --color-orange-*, --color-green-*,
  --color-purple-*, --color-gray-*, --color-red-*, plus --font-kit-sans,
  --font-libre-franklin, --text-*, --spacing, --radius-* and the 150ms
  default transition. There is no data-mode and no dark set.

  app.kit.com/users/login — a separate signed-out card (Inter, warm-white
  page, soft-black submit). Its values land under component.login.* as
  measured literals. Signup is Cloudflare-gated and is not measured.

Deterministic: same inputs, byte-identical output.
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. kit.com's "
        "declared custom-property layer is a Tailwind v4 theme ramp plus "
        "Kit's own soft-black, warm-white and brand blue. Declared scales "
        "land under core.* as {var} leaves. Measured component geometry "
        "lands as literals. The site is light-only: the dark set stays empty."
    ),
    "core": {}, "light": {}, "dark": {}, "component": {},
}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


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
        return "rgba(%d, %d, %d, %g)" % (int(float(r)), int(float(g)), int(float(b)), float(a))
    return v


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


DECL_SRC = "declared custom property in the site's css bundle (raw/css-vars.json)"


def declared_raw(name):
    """A custom property the stylesheets declare, even when the probe did not resolve it.

    Next.js sets --font-kit-sans and --font-libre-franklin on a hashed class, not on
    :root, so the probe's resolved map misses them. The declaration is still in the
    theme bin of css-vars.json.
    """
    if R.get(name) not in (None, ""):
        return R[name]
    for bucket in ("theme", "app", "tailwind"):
        for rule in V.get(bucket) or []:
            props = rule.get("properties") or {}
            if name in props and props[name] not in (None, ""):
                return props[name]
    return None


def declared(name):
    v = declared_raw(name)
    return v if v not in (None, "") else None


def decl(name, ty="dimension"):
    v = declared(name)
    if v is None:
        raise KeyError(name)
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    if ty == "fontWeight":
        v = int(float(v)) if re.fullmatch(r"\d+(\.0+)?", str(v)) else v
    if ty == "number" and re.fullmatch(r"-?\d+(\.\d+)?", str(v)):
        v = float(v) if "." in str(v) else int(v)
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def decl_color(name):
    v = declared(name)
    if v is None:
        raise KeyError(name)
    ty = "color" if re.fullmatch(r"#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)", str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# colours
def is_leaf(node):
    return isinstance(node, dict) and "type" in node and ("var" in node or "value" in node)


def emit(tree, parts, leaf, name):
    """Place a leaf at a dotted path without nesting it inside another leaf.

    --color-warm-white and --color-warm-white-100 both split on "-", so the second
    would land inside the first leaf's dict, where build_tokens.py treats the node as
    one leaf and drops it. When the walk reaches a leaf, the rest of the name stays
    joined with "-" as a sibling key (warm.white and warm.white-100). A path that is
    already taken raises instead of overwriting.
    """
    node = tree
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        if is_leaf(nxt):
            parts = parts[:i] + ["-".join(parts[i:])]
            break
        node = node.setdefault(p, {})
    key = parts[-1]
    if key in node:
        raise KeyError(f"{name}: token path {'.'.join(parts)} is already taken")
    node[key] = leaf


color = SPEC["core"].setdefault("color", {})
for name in sorted(k for k in R if k.startswith("--color-") and re.fullmatch(r"#[0-9a-fA-F]{3,8}", str(R.get(k) or ""))):
    emit(color, name[len("--color-"):].split("-"), var(name, "color"), name)

# fonts
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if declared("--font-kit-sans"):
    fam["display"] = var("--font-kit-sans", "fontFamily", description="KitSansFont, the display face on marketing headlines.")
if declared("--font-libre-franklin"):
    fam["sans"] = var("--font-libre-franklin", "fontFamily", description="Libre Franklin, the UI and body face on kit.com.")
# --font-sans is declared as var(--font-libre-franklin) and never resolves on
# :root. The family itself is core.font.family.sans. Do not emit the alias.
if declared("--font-mono"):
    fam["mono"] = var("--font-mono", "fontFamily", description="The declared mono stack.")
try:
    fam["app"] = lit(st("login-email", "default")["fontFamily"], "fontFamily",
                     "computed fontFamily of login-email default on app.kit.com/users/login",
                     "The log-in card's Inter stack. A different font layer from the marketing site.")
except KeyError:
    pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if re.fullmatch(r"--font-weight-[a-z]+", k)):
    weights[name[len("--font-weight-"):]] = decl(name, "fontWeight")

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+$", k)):
    sizes[name[len("--text-"):]] = var(name, "dimension")

measured = sizes.setdefault("measured", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The home hero masthead, KitSansFont."),
    ("pricing", "price-h1", "default", "The pricing masthead."),
    ("features", "feat-h1", "default", "The features masthead."),
    ("mobileHero", "m-hero", "default", "The home masthead at 390 wide."),
    ("nav", "nav-link", "default", "The nav link size."),
    ("cta", "nav-trial", "default", "The Start free trial pill size."),
    ("body", "footer-link", "default", "A footer link size."),
]:
    try:
        measured[key] = lit(st(comp, state)["fontSize"], "dimension",
                            f"computed fontSize of {comp} {state}", desc)
    except KeyError:
        pass

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in ("--leading-tight", "--leading-snug", "--leading-normal"):
    if declared(name):
        lineheights[name[len("--leading-"):]] = decl(name, "number")

# spacing, radius, motion, layout
spacing = SPEC["core"].setdefault("spacing", {})
if declared("--spacing"):
    spacing["base"] = decl("--spacing", "dimension")
for i, px in enumerate([4, 8, 12, 16, 24, 32, 48, 64, 80], start=1):
    spacing["s%d" % i] = lit("%dpx" % px, "dimension",
                             "Reconstruction: entered by hand at capture time. The step list was chosen "
                             "by hand on the declared --spacing of 4px (0.25rem); Tailwind multiplies "
                             "--spacing by any integer, so no reading names these nine steps",
                             "Step %d on the 4px base." % i)

radius = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--radius-[a-z0-9]+", k)):
    radius[name[len("--radius-"):]] = var(name, "dimension")

duration = SPEC["core"].setdefault("duration", {})
if declared("--default-transition-duration"):
    duration["default"] = decl("--default-transition-duration", "duration")
easing = SPEC["core"].setdefault("easing", {})
for name, key in (("--ease-out", "out"), ("--ease-in", "in"), ("--ease-in-out", "inOut"),
                  ("--default-transition-timing-function", "default")):
    if declared(name):
        easing[key] = lit(declared(name), "cubicBezier", f"{DECL_SRC}: {name}", f"The declared `{name}`.")

container = SPEC["core"].setdefault("container", {})
for name in sorted(k for k in R if k.startswith("--container-")):
    container[name[len("--container-"):]] = var(name, "dimension")

# semantic light roles, aliasing declared colours
light = SPEC["light"]
light["background"] = {
    "page": var("--color-white", "color", description="The marketing page field."),
    "ink": var("--color-soft-black", "color", description="The dark hero and footer band."),
    "warm": var("--color-warm-white", "color", description="Warm white, used as on-ink text and the log-in page field."),
    "warm100": var("--color-warm-white-100", "color", description="The lighter warm surface."),
    "warm300": var("--color-warm-white-300", "color", description="The deeper warm surface."),
}
light["text"] = {
    "primary": var("--color-soft-black", "color", description="Primary ink."),
    "onInk": var("--color-warm-white", "color", description="Text on the soft-black bands."),
    "onAccent": var("--color-soft-black", "color", description="Text on the blue trial pill."),
    "muted": var("--color-gray-700", "color", description="Secondary gray text."),
    "disabled": var("--color-gray-500", "color", description="The lightest gray that still reads as disabled text."),
    "link": var("--color-soft-black", "color", description="Links share the ink. Underline carries the link role."),
}
light["border"] = {
    "default": var("--color-gray-300", "color", description="The default hairline."),
    "strong": var("--color-gray-800", "color", description="The strong border."),
    "focus": var("--color-blue-500", "color", description="focus-visible:ring-blue-500 on the wordmark and controls."),
}
light["action"] = {
    "fill": var("--color-blue-500", "color", description="The Start free trial fill."),
    "ink": var("--color-soft-black", "color", description="The ink fill on Request demo and the log-in submit."),
    "hover": None,
}
# The trial pill's hover fill, read from the live pill and matched to the declared
# blue it paints (#a2d1f1 is --color-blue-200). Refuses to guess when no declared
# colour matches.
_hover = norm_color(st("nav-trial", "hover")["backgroundColor"])
_hover_vars = sorted(n for n in R if n.startswith("--color-") and norm_color(str(R[n])) == _hover)
if len(_hover_vars) != 1:
    raise SystemExit(f"nav-trial hover fill {_hover} matches {_hover_vars}, not exactly one declared colour")
light["action"]["hover"] = var(_hover_vars[0], "color",
                               source=f"the measured fill of nav-trial hover ({_hover}, computed backgroundColor)",
                               description="The Start free trial fill on hover, as measured on the live pill.")

light["status"] = {
    "danger": var("--color-red-500", "color"),
    "warning": var("--color-yellow-500", "color"),
    "success": var("--color-green-500", "color"),
    "info": var("--color-blue-500", "color"),
}

# component geometry from measurements, skipped when a selector missed
comp = SPEC["component"]
def height(name, key, state, desc):
    try:
        comp[name] = lit(st(key, state)["height"] if False else ("%gpx" % round(float(rc(key, state, "h")), 1)),
                         "dimension", f"measured height of {key} {state}", desc)
    except KeyError:
        pass

height("navHeight", "mega-nav", "default", "The fixed #mega-nav height.")
height("announceHeight", "announce-bar", "default", "The announcement strip height.")
height("trialHeight", "nav-trial", "default", "The Start free trial pill height.")
height("heroSize", "hero-h1", "default", "The hero headline box height.")
height("loginSubmitHeight", "login-submit", "default", "The log-in submit height.")
try:
    comp["trialRadius"] = lit(st("nav-trial", "default")["borderTopLeftRadius"], "dimension",
                              "computed border radius of nav-trial default", "The trial pill radius.")
except KeyError:
    pass
try:
    comp["loginRadius"] = lit(st("login-submit", "default")["borderTopLeftRadius"], "dimension",
                              "computed border radius of login-submit default", "The log-in submit radius.")
except KeyError:
    pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("component-tokens.json written", "colors", len(list(color)), "components", len(comp))
