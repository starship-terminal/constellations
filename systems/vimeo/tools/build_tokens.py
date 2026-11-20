#!/usr/bin/env python3
"""Build tokens.json from the live Vimeo readings in raw/.

Read on 2026-11-19 from signed-out pages in the T3 preview browser:

  raw/css-vars.json              computed --vimeo-* custom properties on
                                 https://vimeo.com/watch (class "light",
                                 color-scheme light, 1169x731, dpr 2)
  raw/components-computed.json   computed styles of the visible controls
  raw/marketing-vars.json        a subset of --colors-chroma-* and
                                 --colors-btn-* on
                                 https://vimeo.com/solutions/marketing

The product app (watch, pricing, login) ships one light token set. Dark
custom properties were not present on these signed-out pages, so there is
no dark set. Marketing pages use a second, triplet-valued palette; those
colours are recorded under core.color.marketing and are not aliased into
the app semantic set.

Every token carries $extensions.source. A value the browser computed is
Measured. A rem converted at 16px, or an alias to another token, is
Derived. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["computed"]
COMP = json.loads((RAW / "components-computed.json").read_text())
MKT = json.loads((RAW / "marketing-vars.json").read_text())["computed"]

SRC_VARS = (
    "Computed custom property on documentElement, "
    "https://vimeo.com/watch, class light, 2026-11-19"
)
SRC_MKT = (
    "Computed custom property on documentElement, "
    "https://vimeo.com/solutions/marketing, 2026-11-19"
)


def src(note):
    return {"source": note}


def color_token(value, note):
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return {"$type": "color", "$value": value.lower(), "$extensions": src(note)}
    return {"$type": "color", "$value": norm_color(value), "$extensions": src(note)}


def dim_token(value, note):
    return {"$type": "dimension", "$value": value, "$extensions": src(note)}


def num_token(value, note):
    return {"$type": "number", "$value": value, "$extensions": src(note)}


def font_token(value, note):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(note)}


def cubic_token(value, note):
    return {"$type": "cubicBezier", "$value": value, "$extensions": src(note)}


def duration_token(value, note):
    return {"$type": "duration", "$value": value, "$extensions": src(note)}


def shadow_token(value, note):
    return {"$type": "shadow", "$value": value, "$extensions": src(note)}


def text_token(value, note, typ="other"):
    return {"$type": typ, "$value": value, "$extensions": src(note)}


def norm_color(value):
    value = value.strip()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", value)
    if not m:
        m = re.fullmatch(r"rgba?\(\s*(\d+)\s+(\d+)\s+(\d+)\s*(?:/\s*([\d.]+)\s*)?\)", value)
    if not m:
        raise ValueError("colour not understood: " + value)
    rgb = [int(m.group(i)) for i in (1, 2, 3)]
    alpha = m.group(4)
    if alpha is None or float(alpha) >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    a = float(alpha)
    a_s = "%g" % round(a, 3)
    return "rgba(%d, %d, %d, %s)" % (rgb[0], rgb[1], rgb[2], a_s)


def triplet(value):
    parts = [int(p) for p in value.split(",")]
    if len(parts) != 3:
        raise ValueError(value)
    return "#%02x%02x%02x" % tuple(parts)


def rem_px(value):
    value = value.strip()
    if value.endswith("px"):
        return value
    if value.endswith("rem"):
        n = float(value[:-3])
        px = n * 16
        text = ("%g" % round(px, 3)) + "px"
        return text
    raise ValueError("not a length: " + value)


def nest(tree, parts, token):
    node = tree
    for part in parts[:-1]:
        child = node.get(part)
        if not isinstance(child, dict) or "$value" in child:
            child = {}
            node[part] = child
        node = child
    node[parts[-1]] = token


def camel_parts(name):
    """--vimeo-colors-vimeoBlueAlpha-400 -> colors, vimeo-blue-alpha, 400."""
    body = name[len("--vimeo-"):]
    # split the first camel segment group from the rest by the first hyphen
    # after a letter run that may contain capitals.
    head, _, tail = body.partition("-")
    head = re.sub(r"([a-z])([A-Z])", r"\1-\2", head).lower()
    tail = re.sub(r"([a-z])([A-Z])", r"\1-\2", tail).lower()
    parts = [p for p in (head + "-" + tail).split("-") if p]
    return parts


def build_core():
    core = {
        "color": {},
        "font": {"family": {}, "weight": {}, "size": {}, "lineHeight": {}, "letterSpacing": {}},
        "space": {},
        "radius": {},
        "size": {},
        "shadow": {},
        "motion": {"duration": {}, "easing": {}},
        "z": {},
        "blur": {},
        "breakpoint": {},
    }
    not_tokenised = []
    for name in sorted(VARS):
        value = VARS[name]
        parts = camel_parts(name)
        group = parts[0]
        rest = parts[1:]
        if group == "colors":
            try:
                token = color_token(value, SRC_VARS + f"; {name}")
            except ValueError:
                not_tokenised.append({"name": name, "value": value, "reason": "colour not parsed"})
                continue
            # One hyphenated key. Nesting would hide --vimeo-colors-background
            # once --vimeo-colors-background-blur arrives as its child.
            core["color"]["-".join(rest)] = token
        elif group == "fonts":
            family = value.strip("'").replace("'", "")
            core["font"]["family"][rest[0]] = font_token(
                family, SRC_VARS + f"; {name}. Proprietary; tokens fall back to system-ui."
            )
        elif group == "font-weights":
            core["font"]["weight"][rest[0]] = num_token(float(value) if "." in value else int(value), SRC_VARS + f"; {name}")
        elif group == "font-sizes":
            core["font"]["size"]["-".join(rest)] = dim_token(value, SRC_VARS + f"; {name}")
        elif group == "line-heights":
            core["font"]["lineHeight"]["-".join(rest)] = num_token(float(value), SRC_VARS + f"; {name}")
        elif group == "letter-spacings":
            core["font"]["letterSpacing"]["-".join(rest)] = dim_token(value, SRC_VARS + f"; {name}")
        elif group == "space":
            core["space"]["-".join(rest)] = dim_token(value, SRC_VARS + f"; {name}")
        elif group == "radii":
            if value.endswith("%"):
                not_tokenised.append({"name": name, "value": value, "reason": "percentage radius"})
                continue
            core["radius"]["-".join(rest)] = dim_token(value if value.endswith("px") else value, SRC_VARS + f"; {name}")
        elif group == "sizes":
            core["size"]["-".join(rest)] = dim_token(value, SRC_VARS + f"; {name}")
        elif group == "shadows":
            core["shadow"]["-".join(rest)] = shadow_token(value, SRC_VARS + f"; {name}")
        elif group == "transition":
            kind = rest[0]
            key = "-".join(rest[1:])
            if kind == "duration":
                if value in ("0", "0s", "0ms"):
                    core["motion"]["duration"][key] = duration_token("0ms", SRC_VARS + f"; {name}")
                else:
                    core["motion"]["duration"][key] = duration_token(value, SRC_VARS + f"; {name}")
            elif kind == "easing":
                m = re.fullmatch(r"cubic-bezier\(([^)]+)\)", value.replace(" ", ""))
                if m:
                    nums = [float(x) for x in m.group(1).split(",")]
                    core["motion"]["easing"][key] = cubic_token(nums, SRC_VARS + f"; {name}")
                else:
                    not_tokenised.append({"name": name, "value": value, "reason": "easing is linear(), not cubic-bezier"})
        elif group == "z-indices":
            if value == "auto":
                not_tokenised.append({"name": name, "value": value, "reason": "keyword"})
            else:
                core["z"]["-".join(rest)] = num_token(int(value), SRC_VARS + f"; {name}")
        elif group == "blur":
            core["blur"]["-".join(rest)] = dim_token(value, SRC_VARS + f"; {name}")
        elif group == "breakpoints":
            # A media-query em is the browser's 16px default, whatever the root font size.
            if not value.endswith("em"):
                raise ValueError(f"{name}: breakpoint {value!r} is not em")
            px = ("%g" % (float(value[:-2]) * 16)) + "px"
            core["breakpoint"]["-".join(rest)] = dim_token(
                px, SRC_VARS + f"; {name} {value}, converted at the 16px media-query em")
        else:
            not_tokenised.append({"name": name, "value": value, "reason": "unmapped group " + group})

    marketing = {}
    for name in sorted(MKT):
        value = MKT[name]
        if name.startswith("--colors-chroma-") and re.fullmatch(r"\d+,\d+,\d+", value):
            key = name[len("--colors-chroma-"):].replace("-", ".")
            # keep hyphen path, not dots, so nest() works
            parts = name[len("--colors-chroma-"):].split("-")
            nest(marketing, parts, color_token(triplet(value), SRC_MKT + f"; {name} (rgb triplet {value})"))
        elif name.startswith("--colors-btn-") or name.startswith("--colors-form-") or name.startswith("--colors-global-nav-"):
            try:
                token = color_token(value, SRC_MKT + f"; {name}")
            except ValueError:
                not_tokenised.append({"name": name, "value": value, "reason": "marketing colour not parsed"})
                continue
            nest(marketing, name[len("--colors-"):].split("-"), token)
    core["color"]["marketing"] = marketing
    core["$extensions"] = {"notTokenised": not_tokenised}
    return core


def alias(path):
    return {"$value": "{" + path + "}", "$extensions": src("Derived alias of " + path)}


def semantic():
    """Roles used by the signed-out app, each an alias of a measured core colour."""
    roles = {
        "background": {
            "page": "color.background",
            "surface": "color.surface",
            "blur": "color.background-blur",
            "fill-brand": "color.fill-brand",
            "fill-surface": "color.fill-surface",
            "overlay": "color.fill-page-overlay",
            "skeleton": "color.fill-skeleton",
            "input": "color.input-fill",
            "secondary-button": "color.button-secondary-default",
            "upsell": "color.upsell-primary",
            "positive": "color.status-positive-primary",
            "destructive": "color.status-destructive-primary",
        },
        "text": {
            "primary": "color.text-primary",
            "secondary": "color.text-secondary",
            "tertiary": "color.text-tertiary",
            "inverted": "color.text-button-inverted",
            "on-brand": "color.black",
            "link": "color.vimeo-blue-600",
        },
        "border": {
            "stroke": "color.stroke",
            "input": "color.input-stroke",
            "input-hover": "color.input-stroke-hover",
            "focus": "color.focus",
            "popover": "color.popover-border",
        },
        "button": {
            "brand": "color.fill-brand",
            "brand-text": "color.black",
            "primary": "color.gray-900",
            "primary-text": "color.text-button-inverted",
            "secondary": "color.button-secondary-default",
            "secondary-hover": "color.button-secondary-hover",
            "social-face": "color.white",
            "social-border": "color.stroke",
        },
    }
    light = {}
    for group, items in roles.items():
        light[group] = {}
        for key, path in items.items():
            token = alias(path)
            token["$type"] = "color"
            light[group][key] = token
    light["component"] = component_tokens()
    return light


def measured(name, field, typ):
    row = COMP[name]
    return {
        "$type": typ,
        "$value": row[field],
        "$extensions": src(row["source"] + f"; computed {field}"),
    }


def component_tokens():
    """Computed control metrics. Colours alias the semantic set when they match."""
    return {
        "button-brand": {
            "background": alias_color("color.fill-brand"),
            "text": alias_color("color.black"),
            "radius": measured("button-brand", "radius", "dimension"),
            "height": measured("button-brand", "height", "dimension"),
            "padding": text_token(COMP["button-brand"]["padding"], COMP["button-brand"]["source"], "other"),
            "font-size": measured("button-brand", "fontSize", "dimension"),
        },
        "button-primary": {
            "background": alias_color("color.gray-900"),
            "text": alias_color("color.text-button-inverted"),
            "radius": measured("button-primary", "radius", "dimension"),
            "height": measured("button-primary", "height", "dimension"),
            "padding": text_token(COMP["button-primary"]["padding"], COMP["button-primary"]["source"], "other"),
            "font-size": measured("button-primary", "fontSize", "dimension"),
        },
        "button-secondary": {
            "background": alias_color("color.button-secondary-default"),
            "text": alias_color("color.text-primary"),
            "radius": measured("button-secondary", "radius", "dimension"),
            "height": measured("button-secondary", "height", "dimension"),
            "padding": text_token(COMP["button-secondary"]["padding"], COMP["button-secondary"]["source"], "other"),
            "font-size": measured("button-secondary", "fontSize", "dimension"),
        },
        "button-social": {
            "background": alias_color("color.white"),
            "text": alias_color("color.text-primary"),
            "border": alias_color("color.stroke"),
            "radius": measured("button-social", "radius", "dimension"),
            "height": measured("button-social", "height", "dimension"),
        },
        "button-marketing": {
            "background": alias_color("color.fill-brand"),
            "text": text_token("#141a20", COMP["button-marketing"]["source"] + "; computed color, marketing ink", "color"),
            "radius": measured("button-marketing", "radius", "dimension"),
            "height": measured("button-marketing", "height", "dimension"),
            "padding": text_token(COMP["button-marketing"]["padding"], COMP["button-marketing"]["source"], "other"),
            "font-size": measured("button-marketing", "fontSize", "dimension"),
        },
        "field": {
            "background": alias_color("color.input-fill"),
            "text": alias_color("color.text-primary"),
            "stroke": text_token(COMP["field"]["outlineColor"], COMP["field"]["source"] + "; computed outline-color", "color"),
            "radius": measured("field", "radius", "dimension"),
            "height": measured("field", "height", "dimension"),
            "font-size": measured("field", "fontSize", "dimension"),
        },
        "dialog": {
            "background": alias_color("color.white"),
            "radius": measured("dialog", "radius", "dimension"),
            "shadow": shadow_token(COMP["dialog"]["shadow"], COMP["dialog"]["source"] + "; computed box-shadow"),
        },
        "switch": {
            "track": measured("switch", "track", "color"),
            "thumb": measured("switch", "thumb", "color"),
            "width": measured("switch", "width", "dimension"),
            "height": measured("switch", "height", "dimension"),
        },
        "badge": {
            "background": alias_color("color.status-positive-primary"),
            "text": alias_color("color.black"),
            "radius": measured("badge", "radius", "dimension"),
        },
        "plan-card": {
            "background": alias_color("color.white"),
            "radius": measured("plan-card", "radius", "dimension"),
        },
        "nav-selected": {
            "background": alias_color("color.button-secondary-default"),
            "radius": measured("nav-selected", "radius", "dimension"),
            "height": measured("nav-selected", "height", "dimension"),
        },
    }


def alias_color(path):
    token = alias(path)
    token["$type"] = "color"
    return token


def typography():
    """A few faces actually used on the captured pages, as composite tokens."""
    faces = {
        "heading-marketing": {
            "fontFamily": "{font.family.marketing}",
            "fontSize": "72px",
            "fontWeight": "500",
            "lineHeight": "72px",
            "letterSpacing": "-3.6px",
        },
        "heading-app": {
            "fontFamily": "{font.family.heading}",
            "fontSize": "20px",
            "fontWeight": "500",
            "lineHeight": "28px",
            "letterSpacing": "0px",
        },
        "price": {
            "fontFamily": "{font.family.heading}",
            "fontSize": "48px",
            "fontWeight": "500",
            "lineHeight": "67.2px",
            "letterSpacing": "-0.48px",
        },
        "body": {
            "fontFamily": "{font.family.body}",
            "fontSize": "16px",
            "fontWeight": "400",
            "lineHeight": "24px",
            "letterSpacing": "0px",
        },
        "body-sm": {
            "fontFamily": "{font.family.body}",
            "fontSize": "14px",
            "fontWeight": "350",
            "lineHeight": "20px",
            "letterSpacing": "0px",
        },
        "eyebrow": {
            "fontFamily": "{font.family.mono}",
            "fontSize": "20px",
            "fontWeight": "400",
            "lineHeight": "20px",
            "letterSpacing": "-0.6px",
        },
        "button": {
            "fontFamily": "{font.family.heading}",
            "fontSize": "16px",
            "fontWeight": "400",
            "lineHeight": "24px",
            "letterSpacing": "0px",
        },
        "link": {
            "fontFamily": "{font.family.body}",
            "fontSize": "12px",
            "fontWeight": "500",
            "lineHeight": "20px",
            "letterSpacing": "0px",
        },
    }
    note = "Derived from computed styles in raw/components-computed.json, 2026-11-19"
    out = {}
    for key, value in faces.items():
        out[key] = {"$type": "typography", "$value": value, "$extensions": src(note)}
    return out


def check(tokens):
    def walk(node, path=""):
        if isinstance(node, dict) and "$value" in node:
            yield path, node
        elif isinstance(node, dict):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                yield from walk(v, f"{path}.{k}" if path else k)
    names = {path for path, _ in walk(tokens)}
    for path, token in walk(tokens):
        value = token["$value"]
        if isinstance(value, str):
            for ref in re.findall(r"\{([^{}]+)\}", value):
                candidates = {ref, "core." + ref, path.split(".")[0] + "." + ref}
                if not candidates & names:
                    raise SystemExit(f"alias {ref} from {path} is missing")


def main():
    core = build_core()
    core["font"]["family"]["marketing"] = font_token(
        "ABCRepro, InterTight, Helvetica, Arial, sans-serif",
        "Computed font-family on body, https://vimeo.com/solutions/marketing, 2026-11-19. "
        "The page also lists ABCRepro Fallback and InterTight Fallback.",
    )
    core["font"]["family"]["mono"] = font_token(
        "ABCReproMono, Helvetica, Arial, sans-serif",
        "Computed font-family on the marketing eyebrow, https://vimeo.com/solutions/marketing, 2026-11-19.",
    )
    core["typography"] = typography()
    light = semantic()
    tokens = {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    check(tokens)
    out = HERE / "tokens.json"
    out.write_text(json.dumps(tokens, indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
