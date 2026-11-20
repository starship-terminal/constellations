#!/usr/bin/env python3
"""Write raw/component-tokens.json, the spec build_tokens.py reads.

kitchenstories.com (Newspack / WordPress, FUNKE) paints one light theme.
Design values are the resolved --newspack-* and --wpds-* custom properties
in raw/css-vars.json. Component dimensions come from
raw/components-computed.json when that file exists.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
comp_path = RAW / "components-computed.json"
# Required: without it every measured component token would silently drop out of the build.
C = json.loads(comp_path.read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}

SPEC = {
    "_about": "Kitchen Stories public magazine tokens. One light theme. Newspack theme colours and WPDS scales from css-vars.json; component sizes from computed styles.",
    "core": {},
    "light": {},
    "dark": {},
    "component": {},
}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def norm_color(v):
    v = str(v or "").strip()
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


def has(n):
    return n in R and R[n] not in (None, "")


def ref(name, ty, desc):
    if not has(name):
        return None
    return var(name, ty, source=f"css-var {name} resolved (raw/css-vars.json)", description=desc)


def is_leaf(node):
    return isinstance(node, dict) and "type" in node and ("var" in node or "value" in node)


def put(tree, path, leaf):
    """Place a leaf without nesting it inside another leaf.

    --wpds-color-background-interactive-error and its -active/-disabled/-strong/-weak
    children split on "-", so the children would land inside the parent leaf, where
    build_tokens.py treats the node as one leaf and drops them. When the walk reaches
    a leaf, the rest of the path stays joined with "-" as a sibling key (error and
    error-active). A path that is already taken raises.
    """
    if leaf is None:
        return
    node = tree
    path = list(path)
    for i, k in enumerate(path[:-1]):
        if is_leaf(node.get(k)):
            path = path[:i] + ["-".join(path[i:])]
            break
        node = node.setdefault(k, {})
    if path[-1] in node:
        raise KeyError(f"token path {'.'.join(path)} is already taken")
    node[path[-1]] = leaf


def slug(name, prefix):
    return name[len(prefix):].strip("-").replace("--", "-") or "base"


# Fonts. The magazine paints Plus Jakarta Sans (the Newspack body/header preset).
# Barlow, Spectral, ttcommons and aime are also served as @font-face.
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
put(fam, ("sans",), ref("--wp--preset--font-family--newspack-body", "fontFamily",
                        "Plus Jakarta Sans, the body face the magazine paints."))
put(fam, ("display",), ref("--wp--preset--font-family--newspack-header", "fontFamily",
                           "Plus Jakarta Sans, the header preset."))
put(fam, ("system",), ref("--wpds-typography-font-family-body", "fontFamily",
                          "The WordPress Design System system stack, used where the theme does not override."))
put(fam, ("mono",), ref("--wpds-typography-font-family-mono", "fontFamily",
                        "The WPDS monospace stack."))

# Newspack type scale.
fs = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in sorted(R):
    if n.startswith("--newspack-theme-font-size-") or n.startswith("--wp--preset--font-size--") or n.startswith("--wpds-typography-font-size-"):
        put(fs, (slug(n, "--").replace("newspack-theme-font-size-", "theme-").replace("wp--preset--font-size--", "preset-").replace("wpds-typography-font-size-", "wpds-"),),
            ref(n, "dimension", f"Declared type size {n}."))

rad = SPEC["core"].setdefault("radius", {})
for n in sorted(R):
    if n.startswith("--wpds-border-radius-"):
        put(rad, (n[len("--wpds-border-radius-"):],), ref(n, "dimension", f"WPDS radius {n}."))

bw = SPEC["core"].setdefault("borderWidth", {})
for n in sorted(R):
    if n.startswith("--wpds-border-width-"):
        put(bw, (n[len("--wpds-border-width-"):],), ref(n, "dimension", f"WPDS border width {n}."))

# Semantic colours from the Newspack theme, which is what the magazine paints.
light = SPEC["light"]
COLOURS = {
    ("page",): ("--newspack-theme-color-bg-body", "Page background."),
    ("surface",): ("--newspack-theme-color-bg-light", "Light surface behind panels."),
    ("surface-input",): ("--newspack-theme-color-bg-input", "Field background."),
    ("header",): ("--newspack-header-color", "Header bar background."),
    ("footer",): ("--newspack-footer-color", "Footer background, the warm #fff5ea band."),
    ("ink",): ("--newspack-theme-color-text-main", "Primary text."),
    ("ink-strong",): ("--newspack-primary-color", "Primary brand ink, #212121."),
    ("muted",): ("--newspack-theme-color-text-light", "Secondary text."),
    ("hover",): ("--newspack-theme-color-text-hover", "Text hover."),
    ("link",): ("--newspack-theme-color-link", "Link colour."),
    ("border",): ("--newspack-theme-color-border", "Default border."),
    ("border-light",): ("--newspack-theme-color-border-light", "Lighter border."),
    ("highlight",): ("--newspack-theme-color-highlight", "Highlight yellow."),
    ("cta",): ("--newspack-cta-color", "Call-to-action red."),
    ("cta-text",): ("--newspack-cta-contrast-color", "Text on the call-to-action."),
    ("on-primary",): ("--newspack-primary-contrast-color", "Text on the primary ink."),
    ("dark",): ("--newspack-theme-color-bg-dark", "Dark surface used inside the light theme."),
    ("alert-red",): ("--newspack-theme-color-alert-red", "Alert red."),
    ("alert-green",): ("--newspack-theme-color-alert-green", "Alert green."),
    ("alert-yellow",): ("--newspack-theme-color-alert-yellow", "Alert yellow."),
    ("button-hover",): ("--newspack-theme-color-bg-button-hover", "Button hover fill."),
    ("menu",): ("--newspack-primary-menu-color", "Primary menu surface."),
}
for path, (name, desc) in COLOURS.items():
    put(light, path, ref(name, "color", desc))

# WPDS semantic colours that resolve on :root, grouped so a reader can find them.
wpds = light.setdefault("wpds", {})
for n in sorted(R):
    if not n.startswith("--wpds-color-"):
        continue
    rest = n[len("--wpds-color-"):]
    parts = rest.split("-")
    # keep the path short: role groups
    put(wpds, tuple(parts), ref(n, "color", f"WPDS colour {n}."))

# Component measurements, when the capture has them. Kept on core so the
# light set stays a colour palette the catalog swatches can point at.
comp = SPEC["core"].setdefault("component", {})


def measured(key, state, prop, ty, desc):
    try:
        style = C[key]["states"][state]["style"]
        val = style.get(prop)
    except KeyError:
        return None
    if not val or val in ("none", "auto", "normal", "0px"):
        return None
    if ty == "color":
        val = norm_color(val)
        if not val.startswith("#") and not val.startswith("rgba"):
            return None
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
        return None
    src = f"measured {key} {state} {prop} (raw/components-computed.json)"
    return {"value": val, "type": ty, "source": src, "description": desc}


for key, label, prop, ty in [
    ("header", "height", "height", "dimension"),
    ("search-field", "height", "height", "dimension"),
    ("search-field", "radius", "borderTopLeftRadius", "dimension"),
    ("nav-link", "size", "fontSize", "dimension"),
    ("recipe-h1", "size", "fontSize", "dimension"),
    ("card-title", "size", "fontSize", "dimension"),
]:
    leaf = measured(key, "default", prop, ty, f"{label} of {key}.")
    if leaf:
        put(comp, (key, label), leaf)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
print("wrote component-tokens.json", "colours", len(COLOURS), "components", len(C))
