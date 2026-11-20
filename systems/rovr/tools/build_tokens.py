#!/usr/bin/env python3
"""Write systems/rovr/tokens.json from the measured readings in raw/computed.json.

The mapping is ROVR's. Helpers and the check are the kit's. Values that were
not on the page are not invented: light semantic colours come from the
stylesheet's :root block (the live page was html.dark), and component colours
come from getComputedStyle on the signed-out pages.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "computed.json").read_text())


def tok(value, ty, source, **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source, "evidence": "Measured"}}
    t["$extensions"].update(ext)
    return t


def put(tree, path, token):
    node = tree
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = token


def hsl(raw):
    """An HSL triplet from the stylesheet, as the browser resolved it on html.dark
    or as the same conversion for the declared :root block."""
    parts = raw.replace("%", "").split()
    h, s, l = float(parts[0]), float(parts[1]) / 100, float(parts[2]) / 100
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    m = l - c / 2
    if hp < 1:
        r, g, b = c, x, 0
    elif hp < 2:
        r, g, b = x, c, 0
    elif hp < 3:
        r, g, b = 0, c, x
    elif hp < 4:
        r, g, b = 0, x, c
    elif hp < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    def channel(v):
        return round((v + m) * 255)

    return "#%02X%02X%02X" % (channel(r), channel(g), channel(b))


# Browser-resolved dark values, kept so a rounding drift fails the build.
RESOLVED = {
    "--background": "#000000",
    "--foreground": "#FAFAFA",
    "--card": "#0A0A0A",
    "--primary": "#FFFF57",
    "--primary-foreground": "#000000",
    "--secondary": "#262626",
    "--muted-foreground": "#A3A3A3",
    "--destructive": "#7F1D1D",
    "--ring": "#D4D4D4",
}


def semantic(theme, declared, source):
    tree = {}
    for name, raw in declared.items():
        if name == "--radius":
            continue
        leaf = name[2:].replace("-", ".")
        # card-foreground -> color.card.foreground is awkward; keep the css name.
        hex_value = hsl(raw)
        if theme == "dark" and name in RESOLVED and hex_value != RESOLVED[name]:
            raise SystemExit(f"{name} converts to {hex_value}, browser resolved {RESOLVED[name]}")
        put(tree, ["color", name[2:]], tok(hex_value, "color", f"{source} {name} {raw}"))
    return tree


core = {}
put(core, ["font", "family", "kern"], tok(
    'kernStandard, "kernStandard Fallback", system-ui, sans-serif', "fontFamily",
    "computed font-family on body, nav, buttons and headings"))
put(core, ["font", "family", "alpina"], tok(
    'gtAlpina, "gtAlpina Fallback", serif', "fontFamily",
    "computed font-family on the curator name (Dina J) and the track Label"))
put(core, ["font", "family", "roboto"], tok(
    'Roboto, "Roboto Fallback", sans-serif', "fontFamily",
    "computed font-family on the player clock"))
put(core, ["font", "weight", "thin"], tok(100, "fontWeight", "@font-face Roboto 100; clock uses 300"))
put(core, ["font", "weight", "light"], tok(300, "fontWeight", "computed font-weight 300 on the 60px clock"))
put(core, ["font", "weight", "regular"], tok(400, "fontWeight", "computed font-weight on body"))
put(core, ["font", "weight", "semibold"], tok(600, "fontWeight", "computed font-weight on the AM/PM label"))
put(core, ["font", "weight", "bold"], tok(700, "fontWeight", "computed font-weight on nav current, MENU, show meta"))
put(core, ["font", "weight", "extrabold"], tok(800, "fontWeight", "computed font-weight on schedule titles and about hero"))

put(core, ["font", "size", "micro"], tok("10px", "dimension", "computed font-size on the footer copyright and V0.1.103"))
put(core, ["font", "size", "caption"], tok("12px", "dimension", "computed font-size on day labels and the Message label"))
put(core, ["font", "size", "body-sm"], tok("14px", "dimension", "computed font-size on privacy body and schedule descriptions"))
put(core, ["font", "size", "nav"], tok("15px", "dimension", "computed font-size on RADIO / MOODS / MENU"))
put(core, ["font", "size", "body"], tok("16px", "dimension", "computed font-size on body"))
put(core, ["font", "size", "section"], tok("20px", "dimension", "computed font-size on privacy h2 and ABOUT US"))
put(core, ["font", "size", "show"], tok("24px", "dimension", "computed font-size on schedule show titles"))
put(core, ["font", "size", "curator"], tok("28.8px", "dimension", "computed font-size on the curator name"))
put(core, ["font", "size", "hour"], tok("36px", "dimension", "computed font-size on the schedule hour and PRIVACY NOTICE"))
put(core, ["font", "size", "player"], tok("51px", "dimension", "computed font-size on the home show title"))
put(core, ["font", "size", "hero"], tok("60px", "dimension", "computed font-size on the about manifesto and the clock"))

put(core, ["lineHeight", "tight"], tok("36px", "dimension", "computed line-height on the 36px hour"))
put(core, ["lineHeight", "body"], tok("24px", "dimension", "computed line-height on body"))
put(core, ["lineHeight", "body-sm"], tok("20px", "dimension", "computed line-height on privacy body"))
put(core, ["lineHeight", "show"], tok("32px", "dimension", "computed line-height on schedule titles"))
put(core, ["lineHeight", "hero"], tok("64px", "dimension", "computed line-height on the about manifesto"))

put(core, ["letterSpacing", "button"], tok("0.8px", "dimension", "computed letter-spacing on SIGN UP / SIGN IN"))
put(core, ["letterSpacing", "privacy-body"], tok("-0.19px", "dimension", "computed letter-spacing on the about body paragraph"))

put(core, ["radius", "none"], tok("0px", "dimension", "computed border-radius on SIGN UP, the track card and the header"))
put(core, ["radius", "token"], tok("8px", "dimension", "computed --radius .5rem on :root (8px at 16px root)"))
put(core, ["radius", "menu"], tok("30px", "dimension", "computed border-radius on the MENU button"))
put(core, ["radius", "pill"], tok("9999px", "dimension", "computed border-radius on Message, Listen and the 40px icon buttons"))

put(core, ["space", "2"], tok("2px", "dimension", "computed border-width on SIGN UP and the icon buttons"))
put(core, ["space", "7"], tok("7px", "dimension", "computed padding-block on the Message button"))
put(core, ["space", "8"], tok("8px", "dimension", "computed padding on a schedule row"))
put(core, ["space", "12"], tok("12px", "dimension", "computed padding-inline on Message, and gap on a schedule row"))
put(core, ["space", "16"], tok("16px", "dimension", "computed padding-block on the track card"))
put(core, ["space", "24"], tok("24px", "dimension", "computed nav gap and the login panel padding-inline"))
put(core, ["space", "28"], tok("28px", "dimension", "computed padding-inline on the track card"))
put(core, ["space", "32"], tok("32px", "dimension", "computed padding-bottom on the schedule list"))

put(core, ["size", "header"], tok("70px", "dimension", "computed header height on the home page"))
put(core, ["size", "menu"], tok("24px", "dimension", "computed MENU button height"))
put(core, ["size", "auth"], tok("36px", "dimension", "computed SIGN UP / SIGN IN height"))
put(core, ["size", "icon"], tok("40px", "dimension", "computed like and share button size"))
put(core, ["size", "oauth"], tok("48px", "dimension", "computed Continue with Google / Apple button size"))
put(core, ["size", "listen"], tok("65px", "dimension", "computed Listen to music button size"))

put(core, ["motion", "duration", "fast"], tok("150ms", "duration", "computed transition-duration 0.15s on icon buttons; .transition-colors"))
put(core, ["motion", "duration", "nav"], tok("300ms", "duration", "computed transition-duration 0.3s on nav links and MENU"))
put(core, ["motion", "duration", "mood"], tok("500ms", "duration", "class duration-500 on the mood titles"))
put(core, ["motion", "easing", "standard"], tok(
    [0.4, 0, 0.2, 1], "cubicBezier",
    "computed transition-timing-function cubic-bezier(0.4, 0, 0.2, 1)"))
put(core, ["typography", "body"], tok({
    "fontFamily": "{font.family.kern}",
    "fontWeight": "{font.weight.regular}",
    "fontSize": "{font.size.body}",
    "lineHeight": "{lineHeight.body}",
}, "typography", "computed body font"))
put(core, ["typography", "nav"], tok({
    "fontFamily": "{font.family.kern}",
    "fontWeight": "{font.weight.bold}",
    "fontSize": "{font.size.nav}",
    "lineHeight": "22.5px",
}, "typography", "computed RADIO link"))
put(core, ["typography", "show"], tok({
    "fontFamily": "{font.family.kern}",
    "fontWeight": "{font.weight.extrabold}",
    "fontSize": "{font.size.show}",
    "lineHeight": "{lineHeight.show}",
}, "typography", "computed schedule show title"))
put(core, ["typography", "hero"], tok({
    "fontFamily": "{font.family.kern}",
    "fontWeight": "{font.weight.extrabold}",
    "fontSize": "{font.size.hero}",
    "lineHeight": "{lineHeight.hero}",
}, "typography", "computed about manifesto heading"))
put(core, ["typography", "curator"], tok({
    "fontFamily": "{font.family.alpina}",
    "fontWeight": "{font.weight.regular}",
    "fontSize": "{font.size.curator}",
    "lineHeight": "40px",
}, "typography", "computed curator name"))

light_declared = {k: v for k, v in RAW["declaredLightTokens"].items() if k.startswith("--")}
dark_declared = {k: v["raw"] for k, v in RAW["resolvedDarkTokens"].items() if k.startswith("--") and k != "--radius"}
light = semantic("light", light_declared, "stylesheet :root, not the live theme")
dark = semantic("dark", dark_declared, "computed on html.dark")

# Live brand yellow is what buttons and rules paint. The token --primary resolves
# to #FFFF57; the painted yellow is rgb(255, 240, 87).
put(dark, ["color", "brand"], tok("#FFF057", "color", "computed rgb(255, 240, 87) on header rule, MENU, nav, SIGN UP text, about and privacy text"))
put(dark, ["color", "mood"], tok("#F2E84A", "color", "computed rgb(242, 232, 74) on THINK / FEEL / MOVE; class literal text-[#F2E84A]"))
put(light, ["color", "brand"], tok("#FFF057", "color", "same painted yellow; light theme was declared, not shown"))
put(light, ["color", "mood"], tok("#F2E84A", "color", "mood title literal; light theme was not shown"))

put(dark, ["component", "button", "bg"], tok("{color.brand}", "color", "MENU, Message, Listen fills"))
put(dark, ["component", "button", "text"], tok("{color.primary-foreground}", "color", "computed color rgb(0, 0, 0) on those buttons"))
put(dark, ["component", "button", "radius"], tok("{radius.pill}", "dimension", "Message and Listen"))
put(dark, ["component", "auth", "bg"], tok("{color.background}", "color", "SIGN UP fill"))
put(dark, ["component", "auth", "text"], tok("{color.brand}", "color", "SIGN UP text"))
put(dark, ["component", "auth", "height"], tok("{size.auth}", "dimension", "SIGN UP height 36px"))
put(light, ["component", "button", "bg"], tok("{color.primary}", "color", "light --primary; the live button fill was not shown in light"))
put(light, ["component", "button", "text"], tok("{color.primary-foreground}", "color", "light --primary-foreground"))
put(light, ["component", "button", "radius"], tok("{radius.pill}", "dimension", "shared radius token"))

core["$extensions"] = {"notTokenised": [
    {"name": "screenshots", "why": "The preview browser returned 'The browser is not producing screenshot frames'. No PNG was invented."},
    {"name": "hover, focus, pressed, disabled", "why": "States were not forced. A global :focus, :focus-visible rule sets outline none and box-shadow none."},
    {"name": "390 and 1440 widths", "why": "The attached pane measured 1169 by 731. The viewport was not resized."},
    {"name": "signed-in app", "why": "/login offers Continue with Google and Continue with Apple. Those were not pressed. No email field was on the page."},
    {"name": "nav rest and clock alpha", "why": "MOODS computed to rgba(255, 240, 87, 0.5) and the clock to rgba(255, 240, 87, 0.3). Left out of tokens.json because the catalog colour parser accepts hex and rgb() only."},
]}

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "html.dark, the class on every page visited. color-scheme computed to dark."},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Stylesheet :root block. Not the live theme. Do not treat these as a captured surface."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}


def tokens_of(tree, prefix=""):
    for key, value in tree.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from tokens_of(value, prefix + key + ".")


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [item for child in value.values() for item in aliases(child)]
    if isinstance(value, list):
        return [item for child in value for item in aliases(child)]
    return []


def check(tree):
    """Every token has a source, and every alias resolves in its own set or core, as the catalog
    Resolver does. The old check also let a dark alias resolve against light-only names."""
    count = 0
    for setname in ("core", "light", "dark"):
        if setname not in tree:
            continue
        local = dict(tokens_of(tree["core"]))
        local.update(dict(tokens_of(tree[setname])))
        for name, token in tokens_of(tree[setname]):
            count += 1
            if "source" not in token.get("$extensions", {}):
                raise ValueError(f"{setname}.{name} has no source")
            for alias in aliases(token["$value"]):
                if alias not in local:
                    raise KeyError(f"{setname}.{name}: alias {{{alias}}} points at nothing in core or {setname}")
    return count


def main():
    check(tokens)
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", HERE / "tokens.json", "tokens", check(tokens))


if __name__ == "__main__":
    main()
