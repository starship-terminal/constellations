#!/usr/bin/env python3
"""Build tokens.json from Literal's declared custom properties.

Source: raw/css-vars.json, harvested from literal.club on 2026-11-18.
Light is :root, :root.light. Dark is :root.dark and :root:not(.light),
and it resolves when prefers-color-scheme is dark. No public theme
toggle was found. Spacing is --size-N (4px steps). Motion comes from
raw/motion.json via tools/motion.py.

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
    motion = {}
    motion_path = HERE / "raw" / "motion.json"
    if motion_path.exists():
        motion, _skipped = motion_build(json.loads(motion_path.read_text()))
    return {
        "font": {
            "family": {
                "sans": font("Inter, sans-serif", "computed body font-family on literal.club"),
                "serif": font("Libre Baskerville, Georgia, serif", "computed h1 font-family on the home hero"),
            }
        },
        "typography": {
            "body": typography("14px", "20px", "400", "{font.family.sans}", "computed body on literal.club"),
            "hero": typography("40px", "54px", "500", "{font.family.serif}", "computed h1.LandingPage_heroTitle on /"),
            "display": typography("24px", "36px", "400", "{font.family.serif}", "computed h1.displayHeader on /signin"),
            "book-title": typography("32px", "42px", "400", "{font.family.serif}", "computed h1 on /book/the-midnight-library-mrpx0"),
        },
        "spacing": spacing,
        "radius": {
            "none": {"$type": "dimension", "$value": "0px", "$extensions": {"source": "computed border-radius on header Join and the sign-in submit"}},
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
