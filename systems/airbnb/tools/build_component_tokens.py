#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Airbnb's variables resolve on the home page at each breakpoint
(raw/css-vars.json -> resolved.home.<width>, written by tools/capture/vars.mjs).
The token tree mirrors the site's own --palette-*, --corner-radius-*,
--spacing-*, --motion-*, --elevation-*, --material-* and --typography-*
families:

  core.palette   the raw ramps every semantic name is built on (rausch, beige,
                 grey, the blue/green/orange/purple/magenta/red scales, the
                 legacy named colours and the brand gradients)
  light.color    the semantic --palette-bg/-text/-border/-icon/-status/-logo/
                 -loading/-overlay names, as they apply in the light theme
                 airbnb.com actually paints (the page sets
                 data-color-scheme="light"; the stylesheets' prefers-dark
                 values are captured the same way into the dark set)
  light.radius/space/motion/elevation/material
                 the non-colour scales
  light.type     the named text styles, as DTCG typography composites
  plus a small measured group for values no variable holds (the focus ring,
  the tab underline), each naming the measurement it came from.

A leaf is {"var": "--name"} (resolved through the declarations in
css-vars.json) or {"value": ..., "source": "..."} for measured values, or a
ready DTCG node for composites a single --var cannot express (typography
styles, gradients, parsed shadows). Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]["home"]
R1440 = RES["1440"]

C = json.loads((RAW / "components-computed.json").read_text())["components"]


def val(name):
    if name not in R1440:
        raise KeyError(name + " not in resolved home vars")
    return R1440[name]


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def src(name):
    return f"css-var {name} (:root)"


def dark_decl(name):
    """The value the always-dark .c12bynq4 class declares for name (the dark
    set's first-ranked scope, as build_tokens.py ranks it)."""
    vals = {d["value"] for d in V["decls"] if d["name"] == name and d["selector"] == ".c12bynq4" and not d["media"]}
    if len(vals) != 1:
        raise KeyError(f"{name}: expected one .c12bynq4 declaration, found {sorted(vals)}")
    return vals.pop()


# ---------------------------------------------------------------- colour helpers


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"color-mix\(in srgb,\s*(#[0-9a-fA-F]{3,8}|[a-z]+)\s+([\d.]+)%,\s*transparent\)", v)
    if m:
        base, pct = norm_color(m.group(1)), float(m.group(2)) / 100
        h = base.lstrip("#")[:6]
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return f"rgba({r}, {g}, {b}, {'%g' % round(pct, 3)})"
    return v


def colour_of(name):
    return norm_color(val(name))


# ---------------------------------------------------------------- spec tree

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Airbnb styles itself "
    "with the --palette-* variables (ramps plus a semantic bg/text/border/icon "
    "layer) resolved on :root, and the --typography-*, --spacing-*, "
    "--corner-radius-*, --motion-*, --elevation-* and --material-* scales beside "
    "them. A leaf with \"var\" takes its value from that variable's declaration "
    "in raw/css-vars.json; a leaf with \"value\" carries a value measured on the "
    "running page and names the measurement in \"source\". core.palette holds "
    "the ramps; light.color holds the semantic names. The stylesheets also "
    "declare every palette name under prefers-color-scheme: dark (and on the "
    "always-dark .c12bynq4 class): those become the dark set, though the site "
    "itself pins data-color-scheme=\"light\" and never applies them."),
    "core": {"palette": {}}, "light": {"color": {}}, "dark": {"color": {}}}

# ------------------------------------------------------------------ core ramps

RAMP = re.compile(r"--palette-([a-z]+?)(\d+)\Z")


def ramp_key(name):
    """--palette-beige600 -> ('beige', '600'); --palette-always-white -> ('always', 'white')."""
    m = RAMP.fullmatch(name)
    if m:
        return m.group(1), m.group(2)
    n = name[len("--palette-"):]
    if "-" in n:
        head, tail = n.split("-", 1)
        return head, tail
    return n, "default"


# names that carry no colour value (gradients handled separately)
GRAD_NAMES = [n for n in R1440 if n.startswith("--palette-") and "gradient" in n]
SEMANTIC_PREFIXES = ("bg", "text", "border", "icon", "status", "logo",
                     "loading", "overlay", "on", "shadow", "focus", "link")

for name in sorted(k for k in R1440 if k.startswith("--palette-")):
    if name in GRAD_NAMES:
        continue
    first = name[len("--palette-"):].split("-", 1)[0]
    if first in SEMANTIC_PREFIXES:
        continue
    grp, step = ramp_key(name)
    SPEC["core"]["palette"].setdefault(grp, {})[step] = var(name)

# ------------------------------------------------------------ semantic colours
# --palette-bg-primary -> light.color.bg.primary (nested on the dashes)

def descend(root, parts):
    """Walk parts into nested groups, promoting a leaf already at a node to
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
        node = cur  # name already a group: the bare name lands on 'default'
        node.setdefault("default", None)
        last = "default"
    return node, last


for name in sorted(k for k in R1440 if k.startswith("--palette-")):
    rest = name[len("--palette-"):]
    first = rest.split("-", 1)[0]
    if first not in SEMANTIC_PREFIXES or name in GRAD_NAMES:
        continue
    v = val(name)
    if "gradient" in str(v) or "color-mix" in str(v):
        # a colour DTCG cannot carry (a gradient or a color-mix): keep the var
        # reference anyway so each theme resolves its own declared value — a
        # literal copied from the light page would misreport the dark value
        # (the always-dark class declares 60% black where light resolves 30%)
        leaf = {"var": name, "type": "other"}
    else:
        leaf = {"var": name, "type": "color"}
    for side in ("light", "dark"):
        node, last = descend(SPEC[side]["color"], rest.split("-"))
        node[last] = dict(leaf)

# --------------------------------------------------------------- corner radius

for name in sorted(k for k in R1440 if k.startswith("--corner-radius-")):
    label = name.split("--corner-radius-")[1].replace("-border-radius", "")
    pxv = re.search(r"(\d+)px$", label).group(1)
    label = re.sub(r"\d+px$", "", label)
    grp = SPEC["core"].setdefault("radius", {})
    key = label if label not in grp else f"{label}-{pxv}"
    grp[key] = var(name, "dimension")

# -------------------------------------------------------------------- spacing

for name in sorted(k for k in R1440 if k.startswith("--spacing-")):
    label = name.split("--spacing-")[1]
    m = re.fullmatch(r"(macro|micro)(\d+)px", label)
    grp, step = (m.group(1), m.group(2)) if m else ("misc", label)
    SPEC["core"].setdefault("space", {}).setdefault(grp, {})[step] = var(name, "dimension")

# --------------------------------------------------------------------- motion

for name in sorted(k for k in R1440 if k.startswith("--motion-")):
    label = name.split("--motion-")[1]
    v = val(name)
    if name.endswith("-duration"):
        label, leaf = label[:-len("-duration")], var(name, "duration")
        kind = "duration"
    elif name.endswith("-easing") or name.endswith("-animation-timing-function"):
        label = label.replace("-animation-timing-function", "")
        label = re.sub(r"-(curve|easing)$", "", label)
        if "cubic-bezier" in str(v):
            leaf, kind = var(name, "cubicBezier"), "curve"
        else:
            # linear() spring easings: DTCG has no type for them
            leaf, kind = {"value": str(v), "type": "other", "source": src(name)}, "easing"
    else:
        leaf, kind = {"value": str(v), "type": "other", "source": src(name)}, "misc"
    node, last = descend(SPEC["core"].setdefault("motion", {}), label.split("-") + [kind])
    node[last] = leaf
# motion is theme-independent: the same declarations resolve either way

# ------------------------------------------------------------------ elevation

def px(x):
    return ("%g" % round(float(x), 2)) + "px"


def parse_shadow(v):
    """'0 0 0 1px #313131, 0 8px 28px rgba(0,0,0,0.96)' -> DTCG shadow layers."""
    layers = []
    for part in re.split(r",(?![^(]*\))", v.strip()):
        toks = part.strip().split()
        inset = "inset" in toks
        nums = [t for t in toks if re.fullmatch(r"-?[\d.]+(px)?", t)]
        col = " ".join(t for t in toks if t != "inset" and not re.fullmatch(r"-?[\d.]+(px)?", t))
        if not nums or not col:
            return None
        nums = (nums + ["0"] * 4)[:4]
        layers.append({"color": norm_color(col), "offsetX": px(nums[0].rstrip("px") or 0),
                       "offsetY": px(nums[1].rstrip("px") or 0), "blur": px(nums[2].rstrip("px") or 0),
                       "spread": px(nums[3].rstrip("px") or 0), "inset": inset})
    return layers


for name in sorted(k for k in R1440 if k.startswith("--elevation-")):
    label = name.split("--elevation-")[1]
    if label.endswith("-box-shadow"):
        label = label[:-len("-box-shadow")]
        layers = parse_shadow(val(name))
        if layers is None:
            node = {"value": val(name), "type": "other", "source": src(name)}
        else:
            node = {"$value": layers, "$type": "shadow",
                    "$extensions": {"source": src(name)}}
        grp, step = ("level", label) if re.fullmatch(r"(dark-)?elevation\d", label) else ("named", label)
        SPEC["core"].setdefault("elevation", {}).setdefault(grp, {})[step] = node
    elif label.endswith("-border"):
        # light is the :root value the home page resolves; dark is the value the
        # always-dark .c12bynq4 class declares (1px solid #313131), not a copy
        # of the light one
        for side, decl, where in (("light", val(name), ":root"), ("dark", dark_decl(name), ".c12bynq4")):
            SPEC[side].setdefault("elevation", {}).setdefault("named", {})[label] = \
                {"value": norm_color(decl.split("solid")[-1].strip()), "type": "color",
                 "source": f"css-var {name} ({where})", "description": "1px solid, from " + name}

# ------------------------------------------------------------------- material

for name in sorted(k for k in R1440 if k.startswith("--material-")):
    label = name.split("--material-backgrounds-")[1] if "-backgrounds-" in name else name.split("--material-")[1]
    # 'extra-thick-backdrop-filter' -> group 'extra-thick', leaf 'backdrop'
    prop = "backdrop" if label.endswith("-backdrop-filter") else "color" if label.endswith("-background-color") else "misc"
    key = re.sub(r"-(backdrop-filter|background-color)$", "", label)
    node = SPEC["core"].setdefault("material", {}).setdefault(key, {})
    if prop == "backdrop":
        node[prop] = {"value": val(name), "type": "other", "source": src(name)}
    elif prop == "color":
        node[prop] = var(name)
    else:
        node[label] = {"value": val(name), "type": "other", "source": src(name)}

# ------------------------------------------------------------------ typography
# each named style is a font-size + line-height + letter-spacing triple; the
# family and the weights are their own vars.

# the whole stack, quotes kept — it publishes as core.typography.family, a
# valid CSS font-family list; quotes are stripped only where one family name
# is picked out of it (typo_leaf below)
FAM = val("--typography-font-family-cereal-font-family").strip()


def typo_leaf(base, weight_name=None):
    fs = val(base + "-font-size")
    lh = val(base + "-line-height")
    ls = val(base + "-letter-spacing")
    if weight_name:
        fw = int(re.search(r"\d+", val(weight_name)).group(0))
    else:
        fw = 400
    return {"$value": {"fontFamily": FAM.split(",")[0].strip().strip('"\''),
                       "fontSize": fs, "lineHeight": lh,
                       "fontWeight": fw,
                       "letterSpacing": "0px" if ls == "normal" else ls},
            "$type": "typography",
            "$extensions": {"source": f"css-var {base}-font-size/-line-height/-letter-spacing (:root)"
                            + (f", weight {weight_name}" if weight_name else "")}}


def typo_key(base):
    n = base.split("--typography-")[1]
    return n.replace("_", "-")


WEIGHT_OF = {
    "titles-medium": "medium", "titles-semibold": "semibold",
    "subtitles-book": "book", "special-display-medium": "medium",
}
seen = set()
for name in sorted(k for k in R1440 if k.startswith("--typography-")):
    if name.endswith(("-letter-spacing", "-line-height", "-font-weight")):
        continue
    base = name[:-len("-font-size")] if name.endswith("-font-size") else name
    if base in seen or base + "-font-size" not in R1440:
        continue
    seen.add(base)
    key = typo_key(base)
    # the style's own -font-weight var when it declares one (the display
    # styles declare 600, which no name fragment maps to); the name-based map
    # is only a fallback
    wvar = base + "-font-weight"
    wname = wvar if wvar in R1440 else None
    if wname is None:
        for frag, w in WEIGHT_OF.items():
            if frag in key:
                cand = "--typography-weight-" + w + ("500" if w == "medium" else "600" if w == "semibold" else "400")
                wname = cand if cand in R1440 else None
                break
    SPEC["core"].setdefault("typography", {})[key] = typo_leaf(base, wname)

# weights + tracking + family as their own tokens
for name in sorted(k for k in R1440 if k.startswith("--typography-weight-")):
    label = name.split("--typography-weight-")[1]
    SPEC["core"].setdefault("typography", {}).setdefault("weight", {})[re.sub(r"\d+", "", label)] = \
        {"value": int(re.search(r"\d+", val(name)).group(0)), "type": "fontWeight", "source": src(name)}
for name in sorted(k for k in R1440 if k.startswith("--typography-tracking-")):
    label = name.split("--typography-tracking-")[1]
    SPEC["core"]["typography"].setdefault("tracking", {})[label] = \
        var(name, "dimension" if re.fullmatch(r"-?\d*\.?\d+(px|rem)", str(val(name))) else "other")
# the family's full stack as a fontFamily token, so the catalog can name a font
SPEC["core"]["typography"]["family"] = \
    {"value": FAM, "type": "fontFamily", "source": src("--typography-font-family-cereal-font-family")}

# ------------------------------------------------------------------ gradients

def parse_gradient(v):
    m = re.fullmatch(r"linear-gradient\(to (right|left),\s*(.*)\)", v.strip())
    if not m:
        return None, None
    stops = []
    for st in re.split(r",(?![^(]*\))", m.group(2)):
        c, _, pct = st.strip().partition(" ")
        stops.append({"color": norm_color(c), "position": round(float(pct.rstrip("%")) / 100, 4)})
    angle = "90deg" if m.group(1) == "right" else "270deg"
    return stops, angle


for name in sorted(GRAD_NAMES + ["--palette-bg-secondary-core"]):
    if name not in R1440:
        continue
    v = val(name)
    stops, angle = parse_gradient(v)
    if stops is None:
        leaf = {"value": v, "type": "other", "source": src(name)}
    else:
        leaf = {"$value": stops, "$type": "gradient",
                "$extensions": {"source": src(name), "angle": angle}}
    label = (name.split("--palette-")[1]
             .replace("bg-secondary-core", "brand-core")
             .replace("-gradient-linear-gradient", "-linear")
             .replace("-gradient-radial-gradient", "-radial")
             .replace("-linear-gradient", "-linear"))
    SPEC["core"].setdefault("gradient", {})[label] = leaf

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})


def state_style(comp, state):
    return C[comp]["states"][state]["style"]


# The focus ring every header control draws on keyboard focus: a 2px #222
# shadow hugging the shape. No --palette name holds the ring. The computed
# value comes colour-first ("rgb(34, 34, 34) 0px 0px 0px 2px"), so it goes
# through the same layer parser the --elevation-* vars use — taking the last
# word as the colour would publish "2px" as a colour and a zero spread.
s = state_style("header-host-link", "focus-visible")
ring_layers = parse_shadow(s["boxShadow"])
if not ring_layers or any(not re.fullmatch(r"-?\d*\.?\d+px", l["spread"]) for l in ring_layers):
    raise ValueError("focus ring shadow did not parse: " + s["boxShadow"])
meas["focus-ring"] = {"$value": ring_layers,
                      "$type": "shadow",
                      "$description": "The keyboard-focus ring drawn on every header control.",
                      "$extensions": {"source": "measured header-host-link focus-visible, raw/components-computed.json"}}

# The wishlist heart over a card photo: the glyph is black at 50% with a white
# stroke, so it reads on any image; no --palette name holds the pairing.
# The capture records the glyph's paint on the state itself (state["icon"]),
# not inside its computed style; a missing reading publishes nothing.
ic = C["card-heart"]["states"]["default"].get("icon") or {}
if ic.get("fill") and ic.get("stroke"):
    meas["heart-idle"] = {"value": norm_color(ic["fill"]), "type": "color",
                          "source": "measured card-heart default icon fill, raw/components-computed.json",
                          "description": "The wishlist heart glyph's resting fill over a photo."}
    meas["heart-stroke"] = {"value": norm_color(ic["stroke"]), "type": "color",
                            "source": "measured card-heart default icon stroke, raw/components-computed.json",
                            "description": "The white stroke that keeps the heart readable over photos."}


# ------------------------------------------------------------------ write

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
