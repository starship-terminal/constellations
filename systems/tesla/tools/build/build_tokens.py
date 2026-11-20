#!/usr/bin/env python3
"""Build tokens.json from the Tesla Design System readings in raw/tds-extracted.json.

The readings are getComputedStyle values of --tds-* custom properties on
.tds-colorscheme--light and .tds-colorscheme--dark, taken from the public
tesla.com homepage on 2026-11-19. Marketing pages override four primary tokens
through .tds-theme--marketing; those overrides are recorded on the light and
dark primary tokens as $extensions.marketing, not as a third theme.

Every colour is normalised to #RRGGBB or #RRGGBBAA. calc() lengths are resolved
against the 4px spacer base and the 8px size base that the same dump records.
A value that is not a colour or a px length (a font stack, a shadow, an easing,
a percentage radius) is stored as the type the builder names, or listed under
$extensions.notTokenised when DTCG cannot hold it.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = HERE / "raw" / "tds-extracted.json"
SRC_FILE = "raw/tds-extracted.json"

# Names the homepage computed on both colour schemes. Marketing overrides are
# applied after the base semantic map.
KEEP_PREFIXES = (
    "--tds-color",
    "--tds-theme-",
    "--tds-text--",
    "--tds-heading--color",
    "--tds-caption--color",
    "--tds-form-label",
    "--tds-code-",
    "--tds-dialog--",
    "--tds-scrim--",
    "--tds-toggle--",
    "--tds-outline--focus",
    "--tds-box-shadow",
    "--tds-ui-box-shadow",
    "--tds-font-family-text",
    "--tds-font-family-display",
    "--tds-font-family-monospace",
    "--tds-font-family-latin-",
    "--tds-font-family-base-",
    "--tds-font-family-fallback-text",
    "--tds-font-family-fallback-display",
    "--tds-font-family-fallback-monospace",
    "--tds-font-size-",
    "--tds-line-height-",
    "--tds-font-weight-",
    "--tds-size",
    "--tds-spacer-",
    "--tds-border-radius",
    "--tds-border-width--hairline",
    "--tds-border-width-hairline",
    "--tds-height--pill",
    "--tds-height--choice",
    "--tds-card--",
    "--tds-padding--card",
    "--tds-btn--",
    "--tds-form--gap",
    "--tds-form-input",
    "--tds-icon--size",
    "--tds-chip--",
    "--tds-site-header--height",
    "--tds-animate-",
    "--tds-animation-bezier",
    "--tds-bezier",
    "--tds-opacity--",
    "--tds-blur--",
    "--tds-paragraph-gap",
    "--tds-gutter",
)


def keep(name):
    return name.startswith(KEEP_PREFIXES)


def hex_byte(n):
    return "%02x" % max(0, min(255, int(round(n))))


def colour(value):
    """A computed colour to #rrggbb or #rrggbbaa. None when it is not a colour."""
    v = value.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        if len(h) == 4:
            h = "".join(c * 2 for c in h)
        if len(h) == 6:
            return "#" + h
        if len(h) == 8:
            return "#" + h if h[6:] != "ff" else "#" + h[:6]
        return None
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)", v)
    if m:
        r, g, b = (float(m.group(i)) for i in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1
        if a >= 1:
            return "#%s%s%s" % (hex_byte(r), hex_byte(g), hex_byte(b))
        return "#%s%s%s%s" % (hex_byte(r), hex_byte(g), hex_byte(b), hex_byte(a * 255))
    # The dark probe resolved one surface as hsla(0,0%,100%,.135). That is
    # white at 13.5% alpha: #ffffff22. Other hsla() values are left unparsed.
    m = re.fullmatch(r"hsla\(\s*0\s*,\s*0%\s*,\s*100%\s*,\s*\.135\s*\)", v)
    if m:
        return "#ffffff22"
    return None


def length_px(value):
    """A px length, or a calc() of the 4px spacer / 8px size base, as Npx."""
    v = value.strip()
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", v)
    if m:
        n = float(m.group(1))
        return ("%g" % (round(n, 3) if n != int(n) else int(n))) + "px"
    # calc(4px*N) and calc(4px * N)
    m = re.fullmatch(r"calc\(4px\s*\*\s*(\d+(?:\.\d+)?)\)", v)
    if m:
        return "%gpx" % (4 * float(m.group(1)))
    m = re.fullmatch(r"calc\(8px\s*\*\s*(\d+(?:\.\d+)?)\)", v)
    if m:
        return "%gpx" % (8 * float(m.group(1)))
    return None


def tok(type_, value, source, **extra):
    ext = {"source": source}
    ext.update(extra)
    return {"$type": type_, "$value": value, "$extensions": ext}


def source(name, theme):
    return {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, getComputedStyle(%s) of %s" % (theme, name),
        "file": SRC_FILE,
    }


def put(tree, path, token):
    node = tree
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = token


def leaf(name):
    """--tds-theme-foreground-high-contrast -> theme-foreground-high-contrast."""
    return name[len("--tds-"):].replace("--", "-")


def build():
    data = json.loads(RAW.read_text())
    light, dark = data["light"], data["dark"]
    names = sorted(n for n in light if keep(n) and n in dark)

    core = {}
    light_set = {}
    dark_set = {}
    not_tokenised = []

    # Shared scales: a name whose resolved value is the same in both schemes,
    # and that is a size, type, motion or radius token rather than a colour.
    shared_prefixes = (
        "--tds-font-size-", "--tds-line-height-", "--tds-font-weight-",
        "--tds-size", "--tds-spacer-", "--tds-border-radius",
        "--tds-border-width", "--tds-height--", "--tds-card--padding",
        "--tds-padding--card", "--tds-btn--", "--tds-form--gap",
        "--tds-form-input", "--tds-icon--size", "--tds-chip--height",
        "--tds-chip--font-size", "--tds-chip--padding",
        "--tds-site-header--height", "--tds-animate-", "--tds-animation-bezier",
        "--tds-bezier", "--tds-opacity--", "--tds-blur--",
        "--tds-paragraph-gap", "--tds-gutter", "--tds-font-family-",
    )

    def is_shared_name(name):
        return name.startswith(shared_prefixes) and light[name] == dark[name]

    # Fonts
    families = {
        "text": "--tds-font-family-text",
        "display": "--tds-font-family-display",
        "monospace": "--tds-font-family-monospace",
        "latin-text": "--tds-font-family-latin-text",
        "latin-display": "--tds-font-family-latin-display",
        "fallback-text": "--tds-font-family-fallback-text",
    }
    for key, name in families.items():
        if name in light:
            put(core, ["font", "family", key], tok(
                "fontFamily", light[name], source(name, ":root"),
                note="Universal Sans is Tesla's proprietary face. The stack falls back to -apple-system, Arial, sans-serif. The font files are not in this package.",
            ))

    weights = {
        "thin": "--tds-font-weight-thin",
        "light": "--tds-font-weight-light",
        "regular": "--tds-font-weight-regular",
        "medium": "--tds-font-weight-medium",
        "bold": "--tds-font-weight-bold",
    }
    for key, name in weights.items():
        if name in light and light[name].isdigit():
            put(core, ["font", "weight", key], tok("fontWeight", int(light[name]), source(name, ":root")))

    # Type scale: pair each --tds-font-size-N with --tds-line-height-N when both exist.
    sizes = {}
    for name, value in light.items():
        m = re.fullmatch(r"--tds-font-size-(\d+)", name)
        if m and is_shared_name(name):
            px = length_px(value)
            if px:
                sizes[m.group(1)] = px
    for step, px in sorted(sizes.items(), key=lambda kv: int(kv[0])):
        lh_name = "--tds-line-height-" + step
        lh = length_px(light.get(lh_name, "")) if lh_name in light else None
        style = {
            "fontFamily": "{font.family.text}",
            "fontSize": "{font.size." + step + "}",
            "fontWeight": "{font.weight.regular}",
            "letterSpacing": "0px",
        }
        put(core, ["font", "size", step], tok("dimension", px, source("--tds-font-size-" + step, ":root")))
        if lh:
            style["lineHeight"] = "{font.line-height." + step + "}"
            put(core, ["font", "line-height", step], tok("dimension", lh, source(lh_name, ":root")))
        # Steps 70 and up (28px and larger) take the display family. This is a rule, not a per-step
        # reading: the marketing headings read 40px and 56px in Universal Sans Display.
        if int(step) >= 70:
            style["fontFamily"] = "{font.family.display}"
            style["fontWeight"] = "{font.weight.medium}"
        put(core, ["typography", "size-" + step], tok(
            "typography", style,
            source("--tds-font-size-" + step, ":root"),
        ))

    # Measured roles that are not a numbered step.
    put(core, ["typography", "body"], tok("typography", {
        "fontFamily": "{font.family.text}",
        "fontSize": "14px",
        "lineHeight": "20px",
        "fontWeight": "{font.weight.regular}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, computed style of body and p.tds-text--body",
        "file": "raw/components.json",
    }))
    put(core, ["typography", "caption"], tok("typography", {
        "fontFamily": "{font.family.text}",
        "fontSize": "12px",
        "lineHeight": "18px",
        "fontWeight": "{font.weight.regular}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, computed style of .tds-text--caption",
        "file": "raw/components.json",
    }))
    put(core, ["typography", "hero"], tok("typography", {
        "fontFamily": "{font.family.display}",
        "fontSize": "40px",
        "lineHeight": "48px",
        "fontWeight": "{font.weight.medium}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, computed style of h2.tcl-text--h1 on the homepage",
        "file": "raw/components.json",
    }))
    put(core, ["typography", "display"], tok("typography", {
        "fontFamily": "{font.family.display}",
        "fontSize": "56px",
        "lineHeight": "64px",
        "fontWeight": "{font.weight.medium}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com/solarpanels 2026-11-19, computed style of h1.tcl-text--f56l64",
        "file": "raw/components.json",
    }))
    put(core, ["typography", "button"], tok("typography", {
        "fontFamily": "{font.family.text}",
        "fontSize": "14px",
        "lineHeight": "20px",
        "fontWeight": "{font.weight.medium}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, computed style of a.tds-btn--primary (Order Now)",
        "file": "raw/components.json",
    }))
    put(core, ["typography", "nav"], tok("typography", {
        "fontFamily": "{font.family.text}",
        "fontSize": "14px",
        "lineHeight": "20px",
        "fontWeight": "{font.weight.medium}",
        "letterSpacing": "0px",
    }, {
        "evidence": "Measured",
        "capture": "tesla.com 2026-11-19, computed style of .tds-site-nav-item-text (Menu)",
        "file": "raw/components.json",
    }))

    # Spacing: the 4px spacer steps and the 8px size steps, resolved.
    for name in names:
        if not is_shared_name(name):
            continue
        if name.startswith("--tds-spacer-") or re.fullmatch(r"--tds-size(-\d+x|--\d+x)?", name) or name in (
            "--tds-size", "--tds-size-base", "--tds-size-half", "--tds-size-base-plus",
            "--tds-gutter", "--tds-paragraph-gap", "--tds-site-header--height",
            "--tds-height--pill", "--tds-height--choice", "--tds-icon--size",
            "--tds-card--padding", "--tds-padding--card", "--tds-padding--card--dense",
            "--tds-form--gap", "--tds-btn--font-size", "--tds-btn--min-width",
            "--tds-form-input--collapsed-inline-size",
            "--tds-form-input--collapsed-padding-inline-start",
            "--tds-form-input-choice--radio-size", "--tds-form-input-choice--check-size",
            "--tds-chip--height", "--tds-blur--small", "--tds-blur--large", "--tds-blur--button",
            "--tds-border-width--hairline", "--tds-border-width-hairline",
        ):
            px = length_px(light[name])
            if not px:
                not_tokenised.append({"name": name, "value": light[name], "reason": "not a px length"})
                continue
            group = "spacing" if name.startswith(("--tds-spacer-", "--tds-gutter", "--tds-paragraph")) or "padding" in name or name.endswith("--gap") else "size"
            if name.startswith("--tds-border-width"):
                group = "border"
            if name.startswith("--tds-blur"):
                group = "blur"
            put(core, [group, leaf(name)], tok("dimension", px, source(name, ":root")))

    # Radius. 100% and 0.001px are recorded, not forced into a step.
    for name in names:
        if not name.startswith("--tds-border-radius") or not is_shared_name(name):
            continue
        px = length_px(light[name])
        if px:
            put(core, ["radius", leaf(name)], tok("dimension", px, source(name, ":root")))
        else:
            not_tokenised.append({"name": name, "value": light[name], "reason": "radius is not a px length"})

    # Motion.
    for name in ("--tds-bezier", "--tds-animation-bezier-base", "--tds-animate-transition-function--base",
                 "--tds-animate-transition-function--mktg", "--tds-animate-transition-duration--short",
                 "--tds-animate-transition-duration--medium", "--tds-animate-transition_duration--long",
                 "--tds-animate-transition-property"):
        if name not in light:
            continue
        value = light[name]
        kind = "cubicBezier" if "cubic-bezier" in value or value in ("linear", "ease") else "other"
        if value.endswith("ms"):
            put(core, ["motion", "duration", leaf(name)], tok("duration", value, source(name, ":root")))
        elif kind == "cubicBezier" or value == "linear":
            put(core, ["motion", "easing", leaf(name)], tok("cubicBezier", value, source(name, ":root")))
        else:
            not_tokenised.append({"name": name, "value": value, "reason": "motion value is not a duration or easing"})

    # Colours and shadows, per theme.
    colour_names = [n for n in names if n.startswith((
        "--tds-color", "--tds-theme-", "--tds-text--", "--tds-heading--color",
        "--tds-caption--color", "--tds-form-label", "--tds-code-", "--tds-dialog--",
        "--tds-scrim--", "--tds-toggle--", "--tds-outline--focus",
    ))]
    shadow_names = [n for n in names if "shadow" in n]

    marketing = {
        "--tds-color--primary": "#171a20",
        "--tds-color--primary-highlight": "#393c41",
        "--tds-theme-primary": "#171a20",
        "--tds-theme-primary-highlight": "#393c41",
    }
    marketing_dark = {
        "--tds-color--primary": "#ffffff",
        "--tds-color--primary-highlight": "#e2e3e3",
        "--tds-theme-primary": "#ffffff",
        "--tds-theme-primary-highlight": "#e2e3e3",
        "--tds-theme-foreground-on-primary": "#000000",
    }

    for theme, values, overrides, tree in (
        ("light", light, marketing, light_set),
        ("dark", dark, marketing_dark, dark_set),
    ):
        selector = ".tds-colorscheme--%s" % theme
        for name in colour_names:
            raw = values.get(name, "")
            if not raw or raw in ("currentcolor", "transparent") or raw.startswith("url("):
                if raw:
                    not_tokenised.append({"name": name, "theme": theme, "value": raw[:80], "reason": "not a flat colour"})
                continue
            parsed = colour(raw)
            if not parsed:
                # rgb triplet "255,255,255" is a component list, not a colour.
                if re.fullmatch(r"\d+,\d+,\d+", raw):
                    not_tokenised.append({"name": name, "theme": theme, "value": raw, "reason": "RGB component list, not a colour"})
                elif raw:
                    not_tokenised.append({"name": name, "theme": theme, "value": raw[:80], "reason": "colour not parsed"})
                continue
            extra = {}
            if name in overrides:
                extra["marketing"] = overrides[name]
                extra["marketingSource"] = ".tds-theme--marketing.%s on tesla.com 2026-11-19" % selector
            put(tree, ["color", leaf(name)], tok("color", parsed, source(name, selector), **extra))
        for name in shadow_names:
            raw = values.get(name, "")
            if not raw or raw == "none":
                continue
            put(tree, ["shadow", leaf(name)], tok("shadow", raw, source(name, selector)))

    # Component tokens from the live elements, both themes where the product
    # paints them. Light values are the live page; dark values are the TDS
    # tokens the same components read (the marketing site does not ship a
    # theme toggle, so dark component chrome is the token, labelled as such).
    components = {
        "button-primary": {
            "light": {"background": "#3e6ae1", "text": "#ffffff", "radius": "4px", "height": "40px", "padding": "4px 24px"},
            "dark": {"background": "#3e6ae1", "text": "#ffffff", "radius": "4px", "height": "40px", "padding": "4px 24px"},
            "source": "a.tcl-button.tds-btn--primary (Order Now) on tesla.com",
        },
        "button-secondary": {
            "light": {"background": "#ffffff", "text": "#393c41", "radius": "4px", "height": "40px"},
            "dark": {"background": "#171a20", "text": "#eeeeee", "radius": "4px", "height": "40px"},
            "source": "a.tcl-btn--high-contrast (Learn More on a light hero; Schedule Demo on a dark band)",
        },
        "button-tertiary": {
            "light": {"background": "#f4f4f4", "text": "#393c41", "radius": "4px", "height": "40px", "border": "#d0d1d2"},
            "dark": {"background": "#222222", "text": "#eeeeee", "radius": "4px", "height": "40px", "border": "#5c5e62"},
            "source": "button.tcl-sticky-bar__drive-cta and .tds-btn--tertiary",
        },
        "text-field": {
            "light": {"background": "#f4f4f4", "text": "#5c5e62", "radius": "4px", "height": "40px"},
            "dark": {"background": "#222222", "text": "#a2a3a5", "radius": "4px", "height": "40px"},
            "source": ".tds-form-input.tds-form-input--default wrapping input.tds-form-input-search on /support",
        },
        "header": {
            "light": {"background": "#ffffff", "text": "#171a20", "height": "56px"},
            "dark": {"background": "#000000", "text": "#ffffff", "height": "56px"},
            "source": "header.tds-site-header, height 56px; background is transparent over a hero and white once scrolled (tds-scrim--white)",
        },
    }
    for name, spec in components.items():
        for theme, tree in (("light", light_set), ("dark", dark_set)):
            for prop, value in spec[theme].items():
                kind = "color" if prop in ("background", "text", "border") else "dimension"
                if prop == "padding":
                    # "4px 24px" is not one dimension. Store the block padding.
                    value = value.split()[0]
                put(tree, ["component", name, prop], tok(kind, value, {
                    "evidence": "Measured" if theme == "light" else "Derived",
                    "capture": spec["source"] + ("" if theme == "light" else "; dark face from the .tds-colorscheme--dark tokens the same classes read"),
                    "file": "raw/components.json",
                }))

    if not_tokenised:
        core.setdefault("$extensions", {})["notTokenised"] = not_tokenised

    doc = {
        "core": core,
        "light": light_set,
        "dark": dark_set,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "The public marketing site as it loaded: color-scheme light, body background #ffffff. .tds-theme--marketing overrides primary to #171a20."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Resolved on a .tds-colorscheme--dark probe in the same page. The marketing site has no theme toggle; this palette is the design system's dark scheme, not a second live marketing theme."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    check(doc)
    text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    (HERE / "tokens.json").write_text(text)
    print("wrote tokens.json", len(text), "bytes")


class CheckError(AssertionError):
    pass


def require(ok, message):
    if not ok:
        raise CheckError(message)


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, path + (key,))


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [a for v in value.values() for a in aliases(v)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            require(src.get("evidence") and src.get("capture"), "%s: no source" % where)
            v = t["$value"]
            for a in aliases(v):
                require(a in paths, "%s: alias {%s} points at nothing" % (where, a))
            if isinstance(v, str) and v.startswith("{"):
                continue
            if t["$type"] == "color":
                require(re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", v), "%s: bad colour %s" % (where, v))
            elif t["$type"] == "dimension":
                require(re.fullmatch(r"-?\d+(\.\d+)?px", v), "%s: bad dimension %s" % (where, v))
    if "light" in doc and "dark" in doc:
        keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
        require(keys("light") == keys("dark"), "light and dark keys differ")


if __name__ == "__main__":
    build()
