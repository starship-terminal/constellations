#!/usr/bin/env python3
"""Build tokens.json from manychat.com's harvested custom properties.

Sources, read signed out on 2026-11-18:
  raw/css-vars.json   every custom property the marketing stylesheets declare,
                      resolved on a light probe (tools/capture/vars.mjs).

manychat.com paints one light theme. The export holds core (brand, raw
neutrals, type, radius, spacing, font, motion) and light (semantic roles
plus a few measured component values). The dark set stays empty.

Deterministic: same inputs, byte-identical output. Edit the harvest, never
tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = V["resolved"]["light"]


def resolved(name):
    rec = DECL.get(name)
    if not rec:
        raise KeyError(name)
    return rec.get("value", rec.get("raw"))


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def dim(v):
    v = str(v).strip()
    v = re.sub(r"^(-?)\.(\d)", r"\g<1>0.\2", v)
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        v = v + "px"
    if not DIM.fullmatch(v):
        raise ValueError("dimension " + v)
    return v


def color_token(name, source):
    return {"$value": norm_color(resolved(name)), "$type": "color", "$extensions": {"source": source}}


def dim_token(name, source):
    return {"$value": dim(resolved(name)), "$type": "dimension", "$extensions": {"source": source}}


def other(name):
    rec = DECL.get(name) or {}
    return rec.get("value", rec.get("raw"))


def pick(prefix):
    return sorted(n for n in DECL if n.startswith(prefix))


def group_colors(prefix, drop_prefix):
    out = {}
    for name in pick(prefix):
        rec = DECL[name]
        if rec.get("kind") != "color":
            continue
        key = name[len(drop_prefix):].strip("-")
        try:
            out[key] = color_token(name, f"css-var {name} (light)")
        except ValueError:
            continue
    return out


def font_stack(name):
    raw = other(name)
    if not raw:
        raise KeyError(name)
    return {"$value": raw, "$type": "fontFamily", "$extensions": {"source": f"css-var {name} (light)"}}


brand = group_colors("--brand-", "--brand-")
raw = group_colors("--raw-", "--raw-")
# semantic roles that resolve to a colour
semantic = {}
for name in pick("--semantic-"):
    rec = DECL[name]
    if rec.get("kind") != "color":
        continue
    key = name[len("--semantic-"):]
    try:
        semantic[key] = color_token(name, f"css-var {name} (light)")
    except ValueError:
        continue

named = {}
for name in ("--violet", "--pitch-black", "--dark-violet", "--pink", "--blue-grey", "--light-red", "--light-green", "--grey-green"):
    if name in DECL and DECL[name].get("kind") == "color":
        named[name[2:]] = color_token(name, f"css-var {name} (light)")

radii = {}
for name in pick("--radius-"):
    key = name[len("--radius-"):]
    if DECL[name].get("kind") != "dimension":
        continue
    radii[key] = dim_token(name, f"css-var {name} (light)")

spacing = {}
for name in ("--spacing-2rem", "--spacing-4rem", "--spacing-6rem", "--spacing-8rem", "--spacing-10rem",
             "--spacing-12rem", "--spacing-16rem", "--spacing-18rem", "--spacing-24rem",
             "--spacing-section-gap-default", "--spacing-section-gap-compact"):
    if name in DECL and DECL[name].get("kind") == "dimension":
        key = name[len("--spacing-"):]
        spacing[key] = dim_token(name, f"css-var {name} (light)")

# Type ramp. --text-h1 is a size; companions are --text-h1--line-height and so on.
TYPE_STEPS = ["h1", "h1-ai", "h2", "h3", "h3-regular", "h4", "h5", "h6", "body", "label", "caption",
              "ds-3xl", "ds-2xl", "ds-xl", "ds-l", "ds-m", "ds-base", "ds-s", "ds-xs", "ds-xs-mono", "ds-xss"]
typography = {}
for step in TYPE_STEPS:
    size_name = f"--text-{step}"
    if size_name not in DECL or DECL[size_name].get("kind") != "dimension":
        continue
    # The live site sets html { font-size: 10px }, so 1rem is 10px. The probe
    # resolved rem against a 16px root, so keep the authored rem.
    raw_size = (DECL[size_name].get("raw") or "").strip()
    size = dim(raw_size if raw_size.endswith("rem") else resolved(size_name))
    lh_name = f"--text-{step}--line-height"
    ls_name = f"--text-{step}--letter-spacing"
    fw_name = f"--text-{step}--font-weight"
    lh = other(lh_name)
    if isinstance(lh, str) and re.fullmatch(r"[\d.]+", lh.strip()):
        lh = float(lh) if "." in lh else int(lh)
    elif isinstance(lh, (int, float)):
        lh = lh
    else:
        lh = 1.2
    ls = other(ls_name) or "0"
    if isinstance(ls, (int, float)):
        ls = f"{ls}em" if ls else "0em"
    ls = str(ls).strip()
    if re.fullmatch(r"-?[\d.]+", ls):
        ls = ls + "em"
    fw_raw = other(fw_name)
    fw = 400
    if isinstance(fw_raw, (int, float)):
        fw = int(fw_raw)
    elif isinstance(fw_raw, str):
        fw = {"normal": 400, "bold": 700, "medium": 500}.get(fw_raw.strip(), None)
        if fw is None and re.fullmatch(r"\d+", fw_raw.strip()):
            fw = int(fw_raw.strip())
        if fw is None:
            fw = 400
    family = "{font.family.display}" if step.startswith("h") or step.startswith("ds-3") or step.startswith("ds-2") else "{font.family.sans}"
    if step.endswith("mono"):
        family = "{font.family.mono}"
    typography[step] = {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": fw,
            "lineHeight": lh,
            "letterSpacing": ls,
        },
        "$type": "typography",
        "$extensions": {"source": f"css-var {size_name} plus --line-height/--letter-spacing/--font-weight companions (light)"},
    }

ease_raw = other("--ease") or "cubic-bezier(.43, .195, .02, 1)"
m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", str(ease_raw).strip())
ease = [float(x) for x in m.groups()] if m else [0.43, 0.195, 0.02, 1]

core = {
    "color": {"brand": brand, "raw": raw, "named": named},
    "font": {
        "family": {
            "display": font_stack("--font-gravity"),
            "sans": font_stack("--font-rooftop"),
            "mono": font_stack("--font-cofo"),
        }
    },
    "typography": typography,
    "radius": radii,
    "spacing": spacing,
    "motion": {
        "ease": {"$value": ease, "$type": "cubicBezier", "$extensions": {"source": "css-var --ease (light)"}},
    },
}

light = {
    "background": {
        "page": {"$value": "{color.raw.neutral-0}", "$type": "color", "$extensions": {"source": "alias of --semantic-background-primary / --raw-neutral-0"}},
        "secondary": semantic.get("background-secondary") or color_token("--semantic-background-secondary", "css-var --semantic-background-secondary (light)"),
    },
    "surface": {
        "primary": semantic.get("surface-primary") or color_token("--semantic-surface-primary", "css-var --semantic-surface-primary (light)"),
        "secondary": semantic.get("surface-secondary") or color_token("--semantic-surface-secondary", "css-var --semantic-surface-secondary (light)"),
        "tertiary": semantic.get("surface-tertiary") or color_token("--semantic-surface-tertiary", "css-var --semantic-surface-tertiary (light)"),
    },
    "text": {
        "primary": semantic.get("text-primary") or color_token("--semantic-text-primary", "css-var --semantic-text-primary (light)"),
        "secondary": semantic.get("text-secondary") or color_token("--semantic-text-secondary", "css-var --semantic-text-secondary (light)"),
        "on-accent": {"$value": "#ffffff", "$type": "color", "$extensions": {"source": "measured: hero Get started label on --brand-neon-pink, home viewport"}},
        "on-ink": {"$value": "#ffffff", "$type": "color", "$extensions": {"source": "measured: header Get started and price CTA labels on --raw-neutral-900"}},
    },
    "border": {
        "default": semantic.get("border-default") or color_token("--semantic-border-default", "css-var --semantic-border-default (light)"),
    },
    "action": {
        "accent": {"$value": "{color.brand.neon-pink}", "$type": "color", "$extensions": {"source": "alias of --brand-neon-pink; the hero Get started fill"}},
        "ink": {"$value": "{color.raw.neutral-900}", "$type": "color", "$extensions": {"source": "alias of --raw-neutral-900; price CTAs and the pricing header Get started fill"}},
        "on-photo": {"$value": "{color.raw.neutral-0}", "$type": "color", "$extensions": {"source": "alias of --raw-neutral-0; the header Get started fill over the home hero photo"}},
    },
    "status": {
        "error": semantic.get("utility-error") or color_token("--semantic-utility-error", "css-var --semantic-utility-error (light)"),
        "success": semantic.get("utility-success") or color_token("--semantic-utility-success", "css-var --semantic-utility-success (light)"),
    },
    "component": {
        "button-radius": {"$value": "{radius.full}", "$type": "dimension", "$extensions": {"source": "measured: Get started and price CTAs paint border-radius 999px"}},
        "button-padding-y": {"$value": "14px", "$type": "dimension", "$extensions": {"source": "measured: header Get started padding-top, home viewport"}},
        "button-padding-x": {"$value": "20px", "$type": "dimension", "$extensions": {"source": "measured: header Get started padding-left, home viewport"}},
        "nav-height": {"$value": "92px", "$type": "dimension", "$extensions": {"source": "measured: header height on /pricing (no promo strip)"}},
        "card-radius": {"$value": "24px", "$type": "dimension", "$extensions": {"source": "measured: pricing card corner, /pricing"}},
    },
}

# Fix aliases that point at core paths. color.raw.neutral-0 lives under core.color.
def retarget(node):
    if isinstance(node, dict) and "$value" in node:
        v = node["$value"]
        if isinstance(v, str):
            node["$value"] = v.replace("{color.", "{color.").replace("{radius.", "{radius.")
        return
    if isinstance(node, dict):
        for child in node.values():
            retarget(child)


retarget(light)

tokens = {
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only painted theme on manychat.com: a white field, near-black ink, a neon-pink hero pill, pill CTAs, Rooftop for UI, ManyChatGravity for display, CoFo Sans Mono for nav labels. There is no theme switch.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# Alias check. Light aliases may point at core or light.
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(light)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in list(tokens_of(core)) + list(tokens_of(light)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise SystemExit(f"{n}: alias {{{a}}} points at nothing")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
