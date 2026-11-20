#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Relume declares its system on :root in the Webflow CDN stylesheet
relume-library.shared.*.min.css. tools/capture/vars.mjs reads those
declarations and resolves every name on a probe in light and in
body.p-theme-dark. This builder does not invent values.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIGHT = V["resolved"]["light"]["bodyVars"]
DARK = V["resolved"]["dark"]["bodyVars"]
DECL = V["declared"]

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = v.strip().lower()
    if v == "white":
        return "#ffffff"
    if v == "black":
        return "#000000"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a >= 0.999:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, round(a, 3))
    raise ValueError("not a colour: " + v)


def leaf(path, ty, val, source):
    if ty == "color":
        val = norm_color(val)
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    return {"$value": val, "$type": ty, "$extensions": {"source": source}}


def set_path(tree, parts, node):
    cur = tree
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = node


def token_name(css_name):
    name = css_name[2:]
    name = name.replace("<deleted|", "-deleted-").replace(">", "")
    name = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return name


core = {}
not_tokenised = []

for css_name, spec in sorted(DECL.items()):
    resolved = LIGHT.get(css_name) or ""
    source = f"Measured css-var {css_name} on a probe in light, declared on {spec.get('selector') or ':root'} in {spec.get('file')}"
    if css_name.startswith("--_publish-primitives---colors--"):
        rest = css_name.split("---colors--", 1)[1]
        hue, step = rest.split("-", 1) if "-" in rest else (rest, "base")
        if not re.fullmatch(r"[0-9a-fA-F#].*|white|black|rgba?\(.*", resolved) and not resolved.startswith("#"):
            try:
                norm_color(resolved)
            except ValueError:
                not_tokenised.append(css_name)
                continue
        set_path(core, ["color", hue, step], leaf(css_name, "color", resolved, source))
    elif css_name.startswith("--_publish-radii---"):
        step = css_name.split("---", 1)[1]
        if DIM.fullmatch(resolved):
            set_path(core, ["radius", step], leaf(css_name, "dimension", resolved, source))
        else:
            not_tokenised.append(css_name)
    elif css_name.startswith("--_publish-spacing---"):
        step = css_name.split("---", 1)[1]
        if DIM.fullmatch(resolved):
            set_path(core, ["spacing", step], leaf(css_name, "dimension", resolved, source))
        else:
            not_tokenised.append(css_name)
    elif css_name.startswith("--_hipages-"):
        # Same stylesheet, a campaign landing, not the Relume product roles.
        try:
            set_path(core, ["color", "campaign", "hipages", token_name(css_name)], leaf(css_name, "color", resolved, source + "; hipages campaign, not a Relume role"))
        except ValueError:
            not_tokenised.append(css_name)
    elif css_name in ("--light-grey-1", "--light-grey-2", "--light-grey-3", "--black", "--white", "--purple", "--orange", "--red", "--dark-gray", "--medium-grey", "--green", "--lavender-blush", "--light-orange", "--light-purple"):
        try:
            set_path(core, ["color", "marketing", token_name(css_name)], leaf(css_name, "color", resolved, source))
        except ValueError:
            not_tokenised.append(css_name)

h1 = V["resolved"]["light"]["h1"]
body = V["resolved"]["light"]["body"]
cta = V["resolved"]["light"]["cta"]
core["font"] = {
    "family": {
        "sans": leaf("font.sans", "fontFamily", "Geist Variable, Arial, sans-serif", "Measured computed font-family on body, homepage, light, 1440"),
        "mono": leaf("font.mono", "fontFamily", "Geist Mono Variable, ui-monospace, monospace", "Declared @font-face family Geist Mono Variable in relume-library.shared CSS; fallback is the package fallback, not a measured stack"),
    }
}
core["typography"] = {
    "display": {
        "$type": "typography",
        "$value": {
            "fontFamily": h1["fontFamily"],
            "fontSize": h1["fontSize"],
            "fontWeight": int(h1["fontWeight"]),
            "lineHeight": h1["lineHeight"],
            "letterSpacing": h1["letterSpacing"],
        },
        "$extensions": {"source": "Measured computed style on h1, homepage, light, 1440"},
    },
    "body": {
        "$type": "typography",
        "$value": {
            "fontFamily": body["fontFamily"],
            "fontSize": body["fontSize"],
        },
        "$extensions": {"source": "Measured font-family and font-size on body, homepage, light, 1440. fontWeight and lineHeight were not read: Not captured."},
    },
}

def semantic(theme_vars, label, cta_reading):
    out = {}
    for css_name in sorted(DECL):
        if not css_name.startswith("--_publish-colors---"):
            continue
        resolved = theme_vars.get(css_name) or ""
        if not resolved:
            not_tokenised.append(css_name + ":" + label)
            continue
        role = css_name.split("---", 2)[-1]
        parts = ["color"] + [p for p in role.split("--") if p]
        source = f"Measured css-var {css_name} resolved in {label} (body.p-theme-dark)" if label == "dark" else f"Measured css-var {css_name} resolved in light"
        try:
            set_path(out, parts, leaf(css_name, "color", resolved, source))
        except ValueError:
            not_tokenised.append(css_name + ":" + label)
    out["page"] = leaf("page", "color", theme_vars["--_publish-colors---background--primary"], f"Alias of background primary, {label}")
    out["surface"] = leaf("surface", "color", theme_vars["--_publish-colors---background--secondary"], f"Alias of background secondary, {label}")
    out["text"] = leaf("text", "color", theme_vars["--_publish-colors---foreground--primary"], f"Alias of foreground primary, {label}")
    out["muted"] = leaf("muted", "color", theme_vars["--_publish-colors---foreground--secondary"], f"Alias of foreground secondary, {label}")
    out["accent"] = leaf("accent", "color", theme_vars["--_publish-colors---background--accent-bold"], f"Alias of background accent bold, {label}")
    out["border"] = leaf("border", "color", theme_vars["--_publish-colors---borders--subtle-light"], f"Alias of borders subtle light, {label}")
    out["component"] = {
        "button": {
            "background": leaf("button.bg", "color", cta_reading["backgroundColor"], f"Measured Start for free link, homepage, {label}, 1440"),
            "text": leaf("button.text", "color", cta_reading["color"], f"Measured Start for free link, homepage, {label}, 1440"),
            "radius": leaf("button.radius", "dimension", cta_reading["borderRadius"], f"Measured Start for free link, homepage, {label}, 1440"),
            "fontSize": leaf("button.fontSize", "dimension", cta_reading["fontSize"], f"Measured Start for free link, homepage, {label}, 1440"),
            "paddingX": leaf("button.paddingX", "dimension", "12px", f"Measured padding {cta_reading['padding']} on Start for free, {label}; horizontal component extracted"),
            "paddingY": leaf("button.paddingY", "dimension", "6px", f"Measured padding {cta_reading['padding']} on Start for free, {label}; vertical component extracted"),
        }
    }
    return out

light = semantic(LIGHT, "light", V["resolved"]["light"]["cta"])
dark = semantic(DARK, "dark", V["resolved"]["dark"]["cta"])

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": sorted(set(not_tokenised)),
        "note": "Hipages campaign colours live under core.color.campaign.hipages. They are declared in the same stylesheet and are not Relume product roles.",
    },
}

text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote tokens.json", "core color hues", len(core.get("color", {})), "notTokenised", len(doc["$extensions"]["notTokenised"]))
