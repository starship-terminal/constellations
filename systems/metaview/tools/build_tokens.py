#!/usr/bin/env python3
"""Build tokens.json from Metaview's published custom properties.

Sources, read on 2026-11-19:
  raw/marketing-root.css   the :root block inlined in www.metaview.ai HTML
                           (--mv-color-*, --mv-radius-*, --mv-font-*, --mv-typography-*,
                           --mv-shadow-*, --mv-border-*, --mv-ui-maxWidth)
  raw/app-vars.json        the 131 --mv-* names declared on :root and again on
                           :root[data-theme="dark"] in app.metaview.ai/static/css/root.*.css,
                           read from the signed-out sign-in page (light values are the
                           unconditioned :root block; dark values are the data-theme block)

Marketing ships one theme (warm paper, Euclid Circular A). The signed-out app
ships light and dark (Inter, Radix-style ramps). Both are tokenised. A value
DTCG cannot carry (a multi-layer shadow, a border shorthand, a percentage
radius) is listed under $extensions.notTokenised. Every token carries
$extensions.source. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SRC_M = "www.metaview.ai inline :root, 2026-11-19, raw/marketing-root.css"
SRC_A = "app.metaview.ai sign-in stylesheet :root, 2026-11-19, raw/app-vars.json"

css = (RAW / "marketing-root.css").read_text()
m = re.search(r":root\{([^}]+)\}", css)
if not m:
    raise SystemExit("marketing :root block missing")
MARK = {}
for part in m.group(1).split(";"):
    part = part.strip()
    if not part or ":" not in part:
        continue
    name, value = part.split(":", 1)
    MARK[name.strip()] = value.strip()

APP = json.loads((RAW / "app-vars.json").read_text())


def color_token(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim_token(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font_token(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def num_token(value, source, type_="number"):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def nest(tree, path, token):
    node = tree
    for part in path[:-1]:
        node = node.setdefault(part, {})
    node[path[-1]] = token


def camel_parts(name):
    # --mv-color-light-lime0 -> color.light.lime0
    body = name[len("--mv-"):]
    return body.split("-")


core = {}
light = {}
not_tokenised = []

# Marketing colours, radii, fonts, type, one layout length.
for name, value in MARK.items():
    parts = camel_parts(name)
    group = parts[0]
    if group == "color":
        nest(core, ["color", "marketing", *parts[1:]], color_token(value, f"{SRC_M} {name}"))
    elif group == "radius":
        if value.endswith("%"):
            not_tokenised.append({"name": name, "value": value, "reason": "percentage radius; DTCG dimension is px or rem"})
            continue
        nest(core, ["radius", *parts[1:]], dim_token(value, f"{SRC_M} {name}"))
    elif group == "font" and parts[1] == "family":
        families = [p.strip().strip("'\"") for p in value.split(",")]
        nest(core, ["font", "family", parts[2]], font_token(families, f"{SRC_M} {name}"))
    elif group == "typography" and parts[1] == "common":
        nest(core, ["font", "common", parts[2]], {"$type": "other", "$value": value, "$extensions": {"source": f"{SRC_M} {name}"}})
    elif group == "typography":
        role, prop = parts[1], parts[2]
        bucket = core.setdefault("typography", {}).setdefault(role, {"$type": "typography", "$value": {}, "$extensions": {"source": f"{SRC_M} --mv-typography-{role}-*"}})
        key = {"fontWeight": "fontWeight", "fontSize": "fontSize", "lineHeight": "lineHeight",
               "letterSpacing": "letterSpacing", "textTransform": "textCase"}.get(prop)
        if key == "fontSize":
            bucket["$value"]["fontSize"] = value
            bucket["$value"].setdefault("fontFamily", "{font.family.sans}")
        elif key == "fontWeight":
            bucket["$value"]["fontWeight"] = value
        elif key == "lineHeight":
            if value.endswith("%"):
                bucket["$value"]["lineHeight"] = str(round(float(value[:-1]) / 100, 4)).rstrip("0").rstrip(".")
            else:
                bucket["$value"]["lineHeight"] = value
        elif key == "letterSpacing":
            bucket["$value"]["letterSpacing"] = value
        elif key == "textCase":
            bucket["$extensions"]["textCase"] = value
        else:
            not_tokenised.append({"name": name, "value": value, "reason": "typography property not mapped"})
    elif group == "ui" and name == "--mv-ui-maxWidth":
        nest(core, ["layout", "maxWidth"], dim_token(value, f"{SRC_M} {name}"))
    elif group in ("shadow", "border"):
        not_tokenised.append({"name": name, "value": value, "reason": "multi-layer shadow or border shorthand; kept verbatim, not a single DTCG token"})
    else:
        not_tokenised.append({"name": name, "value": value, "reason": "not mapped"})

# A DTCG typography composite needs every member. --mv-typography declares no letter-spacing for
# some roles; CSS reads that as normal, written here as 0 and said so in the source. Any other
# missing member fails the build instead of taking a typed default.
for role, token in core["typography"].items():
    if "letterSpacing" not in token["$value"]:
        token["$value"]["letterSpacing"] = "0"
        token["$extensions"]["source"] += "; letter-spacing is not declared for this role, 0 stands for normal"
    missing = [k for k in ("fontFamily", "fontWeight", "fontSize", "lineHeight") if k not in token["$value"]]
    if missing:
        raise SystemExit(f"typography.{role}: {missing} not declared in raw/marketing-root.css")

# App ramps. Light from the unconditioned :root, dark from [data-theme=dark].
# Stable names (same in both themes) go to core so a theme set does not repeat them.
light_app = APP["light"]
dark_app = APP["dark"]


def ramp_of(name):
    body = name[len("--mv-"):]
    m = re.fullmatch(r"([a-z]+)(\d+|A\d+)", body)
    if m:
        return m.group(1), m.group(2)
    return None, body


stable = []
themed = []
for name in sorted(light_app):
    if light_app[name] == dark_app[name]:
        stable.append(name)
    else:
        themed.append(name)

for name in stable:
    ramp, step = ramp_of(name)
    if ramp:
        nest(core, ["color", "app", ramp, step], color_token(light_app[name], f"{SRC_A} {name} (same in light and dark)"))
    else:
        nest(core, ["color", "app", ramp_of(name)[1]], color_token(light_app[name], f"{SRC_A} {name} (same in light and dark)"))

dark = {}
for name in themed:
    ramp, step = ramp_of(name)
    path = ["color", ramp, step] if ramp else ["color", step]
    nest(light, path, color_token(light_app[name], f"{SRC_A} {name} on :root"))
    nest(dark, path, color_token(dark_app[name], f"{SRC_A} {name} on :root[data-theme=dark]"))

# Semantic roles an agent reads first, aliased to the measured names.
light.setdefault("background", {})
light["background"]["page"] = {"$type": "color", "$value": "{color.marketing.background}", "$extensions": {"source": "alias of --mv-color-background, the marketing page fill"}}
light["background"]["surface"] = {"$type": "color", "$value": "{color.marketing.white}", "$extensions": {"source": "alias of --mv-color-white; header and menu panel computed rgb(255, 255, 255)"}}
light["background"]["ink"] = {"$type": "color", "$value": "{color.marketing.light.color8}", "$extensions": {"source": "alias of --mv-color-light-color8; announcement bar and primary pill computed rgb(0, 8, 5)"}}
light["background"]["forest"] = {"$type": "color", "$value": "{color.marketing.dark.color}", "$extensions": {"source": "alias of --mv-color-dark-color; a home section computed rgb(10, 33, 25)"}}
light["text"] = {
    "primary": {"$type": "color", "$value": "{color.marketing.text}", "$extensions": {"source": "alias of --mv-color-text"}},
    "onInk": {"$type": "color", "$value": "{color.marketing.textLight}", "$extensions": {"source": "alias of --mv-color-textLight; primary pill label computed rgb(255, 255, 255)"}},
    "faded": {"$type": "color", "$value": "{color.marketing.textFaded}", "$extensions": {"source": "alias of --mv-color-textFaded"}},
}
light["border"] = {
    "divider": {"$type": "color", "$value": "{color.marketing.divider}", "$extensions": {"source": "alias of --mv-color-divider"}},
    "stroke": {"$type": "color", "$value": "{color.marketing.light.fg4}", "$extensions": {"source": "alias of --mv-color-light-fg4; outline pill computed border rgba(1, 5, 27, 0.06) is a sibling alpha"}},
}
light["accent"] = {
    "mint": {"$type": "color", "$value": "{color.marketing.color4}", "$extensions": {"source": "alias of --mv-color-color4"}},
    "lime": {"$type": "color", "$value": "{color.marketing.light.lime3}", "$extensions": {"source": "alias of --mv-color-light-lime3"}},
}

# App semantic roles, themed.
light["app"] = {
    "page": {"$type": "color", "$value": "{color.ui.1}", "$extensions": {"source": "alias of --mv-ui1; sign-in body computed rgb(253, 253, 253) in light"}},
    "surface": {"$type": "color", "$value": "{color.uiBase}", "$extensions": {"source": "alias of --mv-uiBase; email field computed rgb(255, 255, 255) in light"}},
    "text": {"$type": "color", "$value": "{color.text}", "$extensions": {"source": "alias of --mv-text"}},
    "muted": {"$type": "color", "$value": "{color.textFaded}", "$extensions": {"source": "alias of --mv-textFaded"}},
    "border": {"$type": "color", "$value": "{color.ui.A4}", "$extensions": {"source": "alias of --mv-uiA4; field border computed rgba(0, 0, 0, 0.08) in light"}},
    "action": {"$type": "color", "$value": "{color.primaryButtonBackground}", "$extensions": {"source": "alias of --mv-primaryButtonBackground"}},
}
dark["app"] = {
    "page": {"$type": "color", "$value": "{color.ui.1}", "$extensions": {"source": "alias of --mv-ui1; sign-in body computed rgb(5, 6, 6) in dark"}},
    "surface": {"$type": "color", "$value": "{color.uiBase}", "$extensions": {"source": "alias of --mv-uiBase; email field computed rgb(13, 14, 14) in dark"}},
    "text": {"$type": "color", "$value": "{color.text}", "$extensions": {"source": "alias of --mv-text"}},
    "muted": {"$type": "color", "$value": "{color.textFaded}", "$extensions": {"source": "alias of --mv-textFaded"}},
    "border": {"$type": "color", "$value": "{color.ui.A4}", "$extensions": {"source": "alias of --mv-uiA4; field border computed rgba(234, 248, 254, 0.15) in dark"}},
    "action": {"$type": "color", "$value": "{color.primaryButtonBackground}", "$extensions": {"source": "alias of --mv-primaryButtonBackground"}},
}

UNREAD = "Reconstruction: typed from the 2026-11-19 sign-in page; raw/ holds no computed reading of it (raw/app-vars.json has custom properties only). "

# App type, measured on the sign-in heading, field and buttons. One scale; the
# app does not publish a type ramp the way the marketing site does.
core["font"]["family"]["inter"] = font_token(
    ["Inter-v3_19", "-apple-system", "system-ui", "Segoe UI", "Roboto", "Helvetica Neue", "sans-serif"],
    "%sComputed font-family on app.metaview.ai/auth/sign-in body; files are /static/font/Inter-*.woff2" % UNREAD,
)
core["typography"]["appHeading"] = {
    "$type": "typography",
    "$value": {"fontFamily": "{font.family.inter}", "fontWeight": "600", "fontSize": "22px", "lineHeight": "1.3", "letterSpacing": "0"},
    "$extensions": {"source": UNREAD + "Computed style of the sign-in h1"},
}
core["typography"]["appControl"] = {
    "$type": "typography",
    "$value": {"fontFamily": "{font.family.inter}", "fontWeight": "500", "fontSize": "13px", "lineHeight": "18px", "letterSpacing": "0"},
    "$extensions": {"source": UNREAD + "Computed style of the sign-in submit button"},
}
core["typography"]["appField"] = {
    "$type": "typography",
    "$value": {"fontFamily": "{font.family.inter}", "fontWeight": "400", "fontSize": "13px", "lineHeight": "18px", "letterSpacing": "0"},
    "$extensions": {"source": UNREAD + "Computed style of the sign-in email input"},
}
core["radius"]["appControl"] = dim_token("8px", UNREAD + "Computed border-radius of the sign-in email input and buttons")
core["radius"]["appIconButton"] = dim_token("6px", UNREAD + "Computed border-radius of the sign-in theme buttons")

doc = {
    "$schema": "https://tr.designtokens.org/format/dtcg.schema.json",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled", "dark": "disabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "light": "disabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": "Measured from www.metaview.ai and the signed-out app.metaview.ai/auth/sign-in page on 2026-11-19. Marketing is one theme. The app theme set is the product's own :root / :root[data-theme=dark] sheets.",
        "notTokenised": not_tokenised,
    },
}

text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(text)
    print(f"tokens.json {len(text)} bytes, marketing names {len(MARK)}, app names {len(light_app)}, notTokenised {len(not_tokenised)}")
