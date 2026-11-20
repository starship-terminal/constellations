#!/usr/bin/env python3
"""Build tokens.json from Literal's declared custom properties.

Source: raw/css-vars.json, harvested from literal.club on 2026-11-18.
Light is :root, :root.light. Dark is :root.dark and :root:not(.light),
and it resolves when prefers-color-scheme is dark. No public theme
toggle was found. Spacing is --size-N (4px steps). Motion comes from
raw/motion.json via tools/motion.py; easings DTCG cannot hold are listed under
core.$extensions.notTokenised. Type and radius come from the computed styles in
raw/components-computed.json; a value no raw file holds is labelled Reconstruction.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from motion import build as motion_build

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
LIGHT = RAW["resolved"]["light"]
DARK = RAW["resolved"]["dark"]
SRC = "css-var"


def norm_color(v):
    v = v.strip()
    if v.lower() == "transparent":
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)", v, re.I)
    if m:
        r, g, b = (int(round(float(m.group(i)))) for i in (1, 2, 3))
        a = m.group(4)
        if a is None or float(a) >= 0.999:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(float(a), 3))
    hm = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if not hm:
        raise ValueError("not a colour: " + v)
    h = hm.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if len(h) == 8:
        a = int(h[6:8], 16) / 255
        if a >= 0.999:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
    return "#%02x%02x%02x" % (r, g, b)


def color(name, table):
    return {
        "$type": "color",
        "$value": norm_color(table[name]),
        "$extensions": {"source": f"{SRC} {name}"},
    }


def dim(name, table=LIGHT):
    v = str(table[name]).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        v = v + "px"
    if not re.fullmatch(r"-?\d+(\.\d+)?px", v):
        raise ValueError(f"{name}: not a px dimension: {v}")
    return {"$type": "dimension", "$value": v, "$extensions": {"source": f"{SRC} {name}"}}


def font(family, source):
    return {"$type": "fontFamily", "$value": family, "$extensions": {"source": source}}


def reading(comp, state="default"):
    """The computed style of one measured component state; refuse a missing one."""
    try:
        return COMP[comp]["states"][state]["style"]
    except KeyError:
        raise SystemExit(f"raw/components-computed.json has no {comp}.{state} style reading")


def run_of(comp, state="default"):
    """The date the cited state was read: a state kept after a failed rerun keeps its own run."""
    return COMP[comp]["states"][state].get("run") or COMP[comp].get("run")


def measured_type(comp, family):
    s = reading(comp)
    src = f"Measured computed style on {comp}.default ({COMP[comp].get('page')}, {run_of(comp)}): fontSize, lineHeight, fontWeight"
    return typography(s["fontSize"], s["lineHeight"], s["fontWeight"], family, src)


def measured_radius(comp):
    s = reading(comp)
    v = s["borderTopLeftRadius"]
    corners = {s[k] for k in ("borderTopLeftRadius", "borderTopRightRadius", "borderBottomRightRadius", "borderBottomLeftRadius")}
    if len(corners) != 1 or not re.fullmatch(r"\d+(\.\d+)?px", v):
        raise SystemExit(f"{comp}: corners are not one px radius: {sorted(corners)}")
    return {"$type": "dimension", "$value": v,
            "$extensions": {"source": f"Measured computed borderTopLeftRadius on {comp}.default ({COMP[comp].get('page')}, {run_of(comp)})"}}


def typography(size, line, weight, family, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


TEXT = ["--textPrimary", "--textSecondary", "--textDiscreet", "--textBlack", "--textDisabled", "--textWhite"]
UI = ["--uiBase", "--uiInput", "--uiOutline", "--uiBaseLight", "--uiWhite", "--uiBlack", "--uiSecondary",
      "--uiBoxBackground", "--uiHover", "--uiOverlayBackground"]
ACCENT = ["--accentPrimary", "--accentPrimaryHover", "--accentPrimaryActive", "--accentPrimaryDisabled",
          "--accentAlert", "--accentDanger"]


def camel(name, prefix):
    rest = name.removeprefix(prefix)
    return rest[:1].lower() + rest[1:]


def semantic(table):
    """Emit a role only when that theme declares it and the value is a solid colour.
    Dark does not declare --accentPrimaryHover, Active or Disabled. Gradients and
    hsl() backdrops stay in raw/css-vars.json."""
    def group(names, prefix):
        out = {}
        for name in names:
            if name not in table:
                continue
            try:
                out[camel(name, prefix)] = color(name, table)
            except ValueError:
                continue
        return out

    out = {
        "text": group(TEXT, "--text"),
        "ui": group(UI, "--ui"),
        "accent": group(ACCENT, "--accent"),
    }
    if "--shadowColor" in table:
        try:
            out["shadow"] = color("--shadowColor", table)
        except ValueError:
            pass
    return out


def core():
    spacing = {}
    for i in range(1, 41):
        name = f"--size-{i}"
        spacing[str(i)] = dim(name)
    motion, not_tokenised = motion_build(json.loads((HERE / "raw" / "motion.json").read_text()))
    return {
        "$extensions": {"notTokenised": not_tokenised},
        "font": {
            "family": {
                "sans": font(reading("nav-explore")["fontFamily"], f"Measured computed fontFamily on nav-explore.default (home, {run_of('nav-explore')}), the Inter every UI control measures"),
                "serif": font(reading("hero-title")["fontFamily"], f"Measured computed fontFamily on hero-title.default (home, {run_of('hero-title')})"),
            }
        },
        "typography": {
            "body": typography("14px", "20px", "400", "{font.family.sans}",
                               "Reconstruction: entered by hand at capture time; no raw reading holds the body element's "
                               "style. Inherited Inter text measures 14px / 400 with a 20.3px line height (book-card, author-link)"),
            "hero": measured_type("hero-title", "{font.family.serif}"),
            "display": measured_type("signin-title", "{font.family.serif}"),
            "book-title": measured_type("book-title", "{font.family.serif}"),
        },
        "spacing": spacing,
        "radius": {
            "none": measured_radius("nav-join"),
            "sm": measured_radius("signin-submit"),
            "md": measured_radius("join-free"),
        },
        "border": {
            "outline": dim("--outlineWidth"),
        },
        "motion": motion,
    }


def build():
    tokens = {
        "core": core(),
        "light": semantic(LIGHT),
        "dark": semantic(DARK),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    out = HERE / "tokens.json"
    out.write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", out)


if __name__ == "__main__":
    build()
