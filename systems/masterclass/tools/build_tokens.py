#!/usr/bin/env python3
"""Build tokens.json from raw/computed-vars.json.

MasterClass declares a large --mc-* custom-property layer on :root. This
builder keeps the semantic roles, the colour ramps (steps only, not the
parallel *-rgb channels), the spacing scale, radii and type stacks. Every
leaf cites the custom property it was read from on www.masterclass.com,
signed out, on 2026-11-18. The product paints one dark theme, so the
semantic set is named dark.

Deterministic. Edit the raw file, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "computed-vars.json").read_text())
APPLIED = RAW["applied"]
SRC = "css-var on :root, www.masterclass.com signed out (raw/computed-vars.json)"


def leaf(value, ty, name, description=""):
    out = {
        "$value": value,
        "$type": ty,
        "$extensions": {"source": f"{SRC}; {name}"},
    }
    if description:
        out["$description"] = description
    return out


def color(name):
    v = APPLIED[name]
    if re.fullmatch(r"#[0-9a-fA-F]{3}$", v):
        v = "#" + "".join(c * 2 for c in v[1:])
    return v.lower() if v.startswith("#") else v


def put_color(bag, key, name, description=""):
    bag[key] = leaf(color(name), "color", name, description)


core = {"color": {}, "font": {"family": {}}, "spacing": {}, "radius": {}, "lineHeight": {}, "breakpoint": {}}
dark = {"color": {}}

# Ramps: --mc-color-{hue}-{step}, skip *-rgb.
ramps = {}
for name, value in APPLIED.items():
    m = re.fullmatch(r"--mc-color-([a-z]+)-(\d{2,3})", name)
    if not m or name.endswith("-rgb"):
        continue
    hue, step = m.group(1), m.group(2)
    if hue in ("text", "bg", "icon"):
        continue
    ramps.setdefault(hue, {})[step] = leaf(color(name), "color", name)
for hue in sorted(ramps):
    core["color"][hue] = dict(sorted(ramps[hue].items(), key=lambda kv: int(kv[0])))

# Neutrals that are not a numbered ramp.
for name in sorted(APPLIED):
    m = re.fullmatch(r"--mc-color-neutral-([a-z0-9-]+)", name)
    if m and not name.endswith("-rgb") and not m.group(1).isdigit():
        core["color"].setdefault("neutralNamed", {})[m.group(1)] = leaf(color(name), "color", name)

core["font"]["family"]["sohne"] = leaf(
    'Sohne, "Helvetica Neue", Helvetica, Arial, sans-serif',
    "fontFamily",
    "--font-sohne",
    "Computed --font-sohne is the family name Sohne. The fallback stack is the one the captured buttons computed.",
)
core["font"]["family"]["display"] = leaf(
    '"Ivar Display Condensed", "Times New Roman", serif',
    "fontFamily",
    '@font-face "Ivar Display Condensed"',
    "The only @font-face family the home stylesheet registered. Fallback is a system serif, not a MasterClass token.",
)
core["font"]["family"]["sohneKraftig"] = leaf(
    '"Sohne Kraftig", Sohne, "Helvetica Neue", Helvetica, Arial, sans-serif',
    "fontFamily",
    "--font-sohne-kraftig",
)

for name in sorted(APPLIED):
    m = re.fullmatch(r"--spacing-scale-(\d+)", name)
    if m:
        core["spacing"][m.group(1)] = leaf(APPLIED[name], "dimension", name)
    m = re.fullmatch(r"--mc-corners--([a-z]+)", name)
    if m:
        core["radius"][m.group(1)] = leaf(APPLIED[name], "dimension", name)
    m = re.fullmatch(r"--mc-lh-([a-z-]+)", name)
    if m:
        key = m.group(1).replace("--", "-")
        # A unitless line height is a DTCG number, not the string the variable holds.
        lh = float(APPLIED[name])
        core["lineHeight"][key] = leaf(int(lh) if lh.is_integer() else lh, "number", name)
    m = re.fullmatch(r"--mc-bp-([a-z]+)", name)
    if m:
        # A bare "0" is not a DTCG dimension; it is 0px.
        value = APPLIED[name].strip()
        core["breakpoint"][m.group(1)] = leaf("0px" if value == "0" else value, "dimension", name)

# Semantic dark roles, aliases where the value matches a ramp step exactly.
put_color(dark["color"].setdefault("page", {}), "default", "--mc-color-bg-page-default", "Page ground.")
put_color(dark["color"].setdefault("surface", {}), "default", "--mc-color-bg-container-default")
put_color(dark["color"].setdefault("surface", {}), "raised", "--mc-theme-dropdown-bg", "Dropdown and form surface.")
put_color(dark["color"].setdefault("surface", {}), "overlay", "--mc-theme-tooltip-bg")
dark["color"]["scrim"] = leaf(APPLIED["--mc-theme-dropdown-backdrop"], "color", "--mc-theme-dropdown-backdrop")
put_color(dark["color"].setdefault("text", {}), "primary", "--mc-color-text-default")
put_color(dark["color"]["text"], "secondary", "--mc-color-text-medium")
put_color(dark["color"]["text"], "muted", "--mc-color-text-tint")
put_color(dark["color"]["text"], "disabled", "--mc-color-text-disabled-medium")
put_color(dark["color"]["text"], "onAccent", "--mc-color-accent-text")
put_color(dark["color"]["text"], "link", "--mc-color-text-link-default-default")
put_color(dark["color"].setdefault("border", {}), "default", "--mc-color-divider-subtle")
put_color(dark["color"]["border"], "strong", "--mc-color-divider-strong")
put_color(dark["color"]["border"], "focus", "--mc-color-element-focus")
put_color(dark["color"].setdefault("accent", {}), "default", "--mc-color-accent-default")
put_color(dark["color"]["accent"], "hover", "--mc-color-accent-hover")
put_color(dark["color"]["accent"], "pressed", "--mc-color-accent-pressed")
put_color(dark["color"].setdefault("brand", {}), "default", "--mc-color-brand")
put_color(dark["color"].setdefault("status", {}), "success", "--mc-color-success-500")
put_color(dark["color"]["status"], "warning", "--mc-color-warning-500")
put_color(dark["color"]["status"], "danger", "--mc-color-error-500")
put_color(dark["color"]["status"], "info", "--mc-color-focus", "Focus blue is the closest declared info colour. No separate info ramp was applied.")
put_color(dark["color"].setdefault("control", {}), "field", "--mc-theme-form-bg")
put_color(dark["color"]["control"], "fieldBorder", "--mc-theme-form-border")
put_color(dark["color"]["control"], "placeholder", "--mc-theme-form-elem-placehold-color")
put_color(dark["color"].setdefault("plan", {}), "selected", "--mc-theme-checkout-selected-bg-color")
put_color(dark["color"]["plan"], "unselectedText", "--mc-theme-checkout-unselected-text-color")
put_color(dark["color"].setdefault("badge", {}), "fill", "--mc-theme-badge-dim-bg")
put_color(dark["color"]["badge"], "text", "--mc-theme-badge-dim-text")

tokens = {
    "$metadata": {"tokenSetOrder": ["core", "dark"]},
    "core": core,
    "dark": dark,
    "$themes": [{
        "id": "dark",
        "name": "dark",
        "selectedTokenSets": {"core": "source", "dark": "enabled"},
        "$extensions": {"howSet": "The signed-out site paints this palette with no theme toggle. No light set was applied on :root."},
    }],
}

def tally(node):
    n = 0
    for v in node.values():
        if isinstance(v, dict) and "$value" in v:
            n += 1
        elif isinstance(v, dict):
            n += tally(v)
    return n

DIMENSION = re.compile(r"-?\d*\.?\d+(px|rem)")
COLOR = re.compile(r"#[0-9a-f]{6}([0-9a-f]{2})?|rgba?\([^)]*\)")


def check(node, path=""):
    """The DTCG shape checks the kit's builder runs: every leaf has a source, and its
    value is the shape its $type says. Raises instead of writing a bad file."""
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        here = f"{path}.{k}" if path else k
        if "$value" not in v:
            check(v, here)
            continue
        value, ty = v["$value"], v["$type"]
        if not v.get("$extensions", {}).get("source"):
            raise SystemExit(f"{here}: no source")
        ok = {"color": lambda: isinstance(value, str) and COLOR.fullmatch(value),
              "dimension": lambda: isinstance(value, str) and DIMENSION.fullmatch(value),
              "number": lambda: isinstance(value, (int, float)),
              "fontFamily": lambda: isinstance(value, str) and value}.get(ty)
        if ok is None or not ok():
            raise SystemExit(f"{here}: {ty} {value!r} is not a valid DTCG value")


check({"core": core, "dark": dark})

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("tokens.json", tally(tokens), "tokens")
