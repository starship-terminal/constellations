#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

appwrite.io's SvelteKit + Tailwind v4 bundle (raw/css-vars.json, read by
tools/capture/vars.mjs from the cdn.appwrite.io stylesheet) declares:

  @layer theme   the Tailwind v4 token layer on :root,:host: --color-* ramps,
                 --font-*, --text-* + --text-*--line-height, --spacing,
                 --radius-*, --container-*, --ease-*, --animate-*, --blur-*,
                 --leading-*, --tracking-*, --default-transition-*,
                 --aspect-*, --font-weight-*  ->  the core scales
  :root / .dark  the shadcn-style semantic layer: --background, --foreground,
                 --card*, --popover*, --primary*, --secondary*, --muted*,
                 --accent*, --destructive*, --border, --input, --ring,
                 --chart-*, --sidebar-*, --editor-bg, --code-*,
                 --selection-*, --brand-cta*, --network-globe-*, --tone*-rgb
                 ->  the light and dark sets, resolved per theme
  html           --brand-cta* and the globe colours
  skins (.crazy, .stealth, .premium, .high-contrast, .barbie, .nineties,
  .legacy)       easter-egg console themes: recorded in css-vars.json, not
                 tokenised — they are not the marketing system
  vendor         sonner's --toast-*/--gray*: not appwrite's system either

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py through
css-vars.json's resolved light/dark maps) or {"value": ..., "source": "..."}
for a measured value (focus ring, the nav link's keyboard outline), or a ready
DTCG node for composites (type styles, the brand gradient). Deterministic:
same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL, RD = V["resolved"]["light"], V["resolved"]["dark"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]

R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def val(name):
    if name not in R:
        raise KeyError(name + " not in resolved light vars")
    return R[name]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def src(name):
    return f"css-var {name}"


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. appwrite.io styles "
    "itself with a Tailwind v4 theme layer (the --color-*/--text-*/--font-* "
    "scales, tokenised under core) and a shadcn-style semantic layer on :root "
    "(light) and .dark (dark): background/foreground/card/popover/primary/"
    "secondary/muted/accent/destructive/border/input/ring/chart/sidebar/code/"
    "selection/brand-cta/network-globe/tone. A leaf with \"var\" resolves "
    "through the live document in that theme (css-vars.json resolved maps); "
    "\"value\" leaves are measured on the running page. The marketing site "
    "pins .dark on every captured route; the light set is the declared :root "
    "system the console app paints."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    """Walk parts into nested groups; a leaf already at a node is promoted to
    its 'default' child so a name can be both a token and a group."""
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


# ------------------------------------------------------------------ core ramps

for name in sorted(n for n in R if re.fullmatch(r"--color-[a-z]+-\d+", n)):
    fam, step = name[len("--color-"):].rsplit("-", 1)
    node, last = descend(SPEC["core"].setdefault("color", {}).setdefault(fam, {}), [step])
    node[last] = var(name)

# --------------------------------------------------------------------- fonts

FONTS = {"--font-sans": "sans", "--font-mono": "mono", "--font-aeonik-pro": "aeonik",
         "--font-inter": "inter", "--font-inter-overview": "inter-overview"}
for name, key in FONTS.items():
    if name in R:
        SPEC["core"].setdefault("font", {}).setdefault("family", {})[key] = var(name, "fontFamily")

for name in sorted(n for n in R if n.startswith("--font-weight-")):
    key = name[len("--font-weight-"):]
    SPEC["core"].setdefault("font", {}).setdefault("weight", {})[key] = var(name, "fontWeight")

# --------------------------------------------------------------- type scales
# --text-<step> is a font-size; --text-<step>--line-height its leading. The
# steps land under core.text.* and the named composites under core.typography.*.

for name in sorted(n for n in R if re.fullmatch(r"--text-(xs|sm|base|lg|xl|\d+xl)", n)):
    step = name[len("--text-"):]
    node = SPEC["core"].setdefault("text", {})
    node[step] = var(name, "dimension")
    lh = name + "--line-height"
    if lh in R:
        node[step] = {"fontSize": var(name, "dimension"), "lineHeight": var(lh, "other")}
        SPEC["core"].setdefault("typography", {})[step] = {
            "$value": {"fontFamily": "{font.family.sans}", "fontSize": "{text." + step + ".fontSize}",
                       "fontWeight": "{font.weight.normal}", "lineHeight": "{text." + step + ".lineHeight}"},
            "$type": "typography",
            "$extensions": {"source": f"css-var {name} + {lh} (@layer theme)"}}

for name in sorted(n for n in R if n.startswith("--leading-")):
    SPEC["core"].setdefault("leading", {})[name[len("--leading-"):]] = var(name, "number")
for name in sorted(n for n in R if n.startswith("--tracking-")):
    SPEC["core"].setdefault("tracking", {})[name[len("--tracking-"):]] = \
        {"value": str(R[name]), "type": "other", "source": src(name)}  # em units: not a DTCG dimension

# -------------------------------------------------------------------- scales

if "--spacing" in R:
    SPEC["core"].setdefault("spacing", {})["base"] = var("--spacing", "dimension")

for name in sorted(n for n in R if re.fullmatch(r"--radius(-[a-z0-9]+)?", n)):
    key = name[len("--radius"):].lstrip("-") or "default"
    SPEC["core"].setdefault("radius", {})[key] = var(name, "dimension")

for name in sorted(n for n in R if n.startswith("--container-")):
    SPEC["core"].setdefault("container", {})[name[len("--container-"):]] = var(name, "dimension")

for name in sorted(n for n in R if n.startswith("--ease-")):
    v = str(R[name])
    SPEC["core"].setdefault("ease", {})[name[len("--ease-"):]] = \
        var(name, "cubicBezier") if "cubic-bezier" in v else {"value": v, "type": "other", "source": src(name)}

if "--default-transition-duration" in R:
    SPEC["core"].setdefault("motion", {}).setdefault("duration", {})["default"] = var("--default-transition-duration", "duration")
if "--default-transition-timing-function" in R:
    SPEC["core"].setdefault("motion", {}).setdefault("easing", {})["default"] = var("--default-transition-timing-function", "cubicBezier")
for name in sorted(n for n in R if n.startswith("--animate-")):
    SPEC["core"].setdefault("animate", {})[name[len("--animate-"):]] = \
        {"value": str(R[name]), "type": "other", "source": src(name)}
for name in sorted(n for n in R if n.startswith("--blur-")):
    SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = var(name, "dimension")
for name in sorted(n for n in R if n.startswith("--aspect-")):
    SPEC["core"].setdefault("aspect", {})[name[len("--aspect-"):]] = \
        {"value": str(R[name]), "type": "other", "source": src(name)}

# ------------------------------------------------------- semantic (per theme)

# Names come from both resolved maps: a variable declared only under .dark
# (appwrite's --editor-bg) exists in no light declaration but still tokens.
SEMANTIC = [n for n in sorted(set(RL) | set(RD)) if not re.match(
    r"--(color|font|text|spacing|radius|container|ease|animate|blur|aspect|leading|tracking|default|shadow|inset|drop|tw|gray\d|toast|y$|lift|gap|offset|mobile|width|height|scale|swipe)-?", n)]
for name in sorted(SEMANTIC):
    if name in ("--lightningcss-light", "--lightningcss-dark"):
        continue
    parts = name[2:].split("-")
    for side in ("light", "dark"):
        resolved = RD if side == "dark" else RL
        if name not in resolved:
            continue
        node, last = descend(SPEC[side], parts)
        node[last] = var(name)

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})


def state_style(comp, state):
    return C[comp]["states"][state]["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"(ok)?lab\(([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+%?))?\)", v)
    if m:
        # CSS Color 4 conversions, the same math tools/capture/css-colour.mjs
        # uses: oklab() takes the Oklab LMS path, lab() the CIELAB D50 one with
        # the Bradford adaptation to D65; the alpha after / is preserved.
        ok, L, a_, b_, al = m.groups()
        pct = L.endswith("%")
        Lf = float(L[:-1] if pct else L) * (0.01 if pct else 1)
        a_, b_ = float(a_), float(b_)
        if ok:
            l = (Lf + 0.3963377774 * a_ + 0.2158037573 * b_) ** 3
            m2 = (Lf - 0.1055613458 * a_ - 0.0638541728 * b_) ** 3
            s = (Lf - 0.0894841775 * a_ - 1.2914855480 * b_) ** 3
            rgb = (4.0767416621 * l - 3.3077115913 * m2 + 0.2309699292 * s,
                   -1.2684380046 * l + 2.6097574011 * m2 - 0.3413193965 * s,
                   -0.0041960863 * l - 0.7034186147 * m2 + 1.7076147010 * s)
        else:
            fy = (Lf + 16) / 116
            fx, fz = fy + a_ / 500, fy - b_ / 200
            eps, kap = 216 / 24389, 24389 / 27
            f = lambda t: t ** 3 if t ** 3 > eps else (116 * t - 16) / kap
            X, Y, Z = f(fx) * 0.3457 / 0.3585, (fy ** 3 if Lf > kap * eps else Lf / kap), f(fz) * (1 - 0.3457 - 0.3585) / 0.3585
            x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
            y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
            z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
            rgb = (3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z,
                   -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z,
                   0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z)
        alpha = 1.0 if al is None else (float(al[:-1]) / 100 if al.endswith("%") else float(al))
        chan = lambda c: round((12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) * 255)
        r, g, bl = (chan(max(0.0, min(1.0, c))) for c in rgb)
        if alpha >= 1:
            return "#%02x%02x%02x" % (r, g, bl)
        return f"rgba({r}, {g}, {bl}, {'%g' % round(alpha, 3)})"
    return v


# The keyboard-focus ring: shadcn draws it as a ring-* outline/faint border on
# :focus-visible. No app var names the painted ring, so it is measured.
s = state_style("nav-link", "focus-visible")
ring = s.get("outlineColor", "")
if ring and ring != "rgba(0, 0, 0, 0)":
    meas["focus-outline"] = {"value": norm_color(ring), "type": "color",
                             "source": "computed outlineColor of nav-link focus-visible (raw/components-computed.json)",
                             "description": "The keyboard-focus ring colour on nav links."}

# The brand gradient text on the hero: no var holds the stop pair.
bg = state_style("hero-title", "default").get("backgroundImage", "")
meas["hero-gradient"] = {"value": bg[:220] if bg and bg != "none" else "linear-gradient(90deg, #fd366e, #fe9567)",
                         "type": "other",
                         "source": "computed backgroundImage of hero-title default (raw/components-computed.json)",
                         "description": "The pink-to-orange gradient clipped into the hero headline."}

# Card tint: the plan/feature card's muted-alpha fill (a color-mix over
# --muted-foreground), which no single var names.
bg = state_style("plan-card", "default").get("backgroundColor", "")
if bg:
    meas["card-tint"] = {"value": norm_color(bg), "type": "color",
                         "source": "computed backgroundColor of plan-card default (raw/components-computed.json)",
                         "description": "The translucent muted fill the pricing cards paint."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
comp["control"] = {
    "height": {"type": "dimension", "value": state_style("cta-primary", "default")["height"], "source": "rendered height of cta-primary default (raw/components-computed.json)", "description": "Primary buttons are 40px at desktop."},
    "heightSmall": {"type": "dimension", "value": state_style("nav-link", "default")["height"], "source": "rendered height of nav-link default (raw/components-computed.json)", "description": "Nav rows, icon buttons and OAuth rows: 36px."},
    "radius": {"type": "dimension", "value": state_style("cta-primary", "default")["borderTopLeftRadius"], "source": "computed borderTopLeftRadius of cta-primary default (raw/components-computed.json)"},
    "fieldHeight": {"type": "dimension", "value": state_style("email-input", "default")["height"], "source": "rendered height of email-input default (raw/components-computed.json)"},
}
comp["header"] = {"height": {"type": "dimension", "value": state_style("header", "default")["height"], "source": "rendered height of header default at 1440px (raw/components-computed.json)"}}
comp["card"] = {"radius": {"type": "dimension", "value": state_style("plan-card", "default")["borderTopLeftRadius"], "source": "computed borderTopLeftRadius of plan-card default (raw/components-computed.json)"}}

# ------------------------------------------------------------------ write

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
