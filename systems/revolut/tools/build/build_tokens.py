#!/usr/bin/env python3
"""Build tokens.json from the Revolut public-surface readings in raw/.

Sources, read on 2026-11-19 from the live pages (T3 preview, computed style):

  raw/light-colors.json   --rui-color-* resolved on https://www.revolut.com/
                          with html[data-theme=light]
  raw/dark-colors.json    the same names resolved on
                          https://www.revolut.com/our-pricing-plans/ with
                          html[data-theme=dark]
  foundation()            type, radius, space, size, shadow, motion and focus,
                          resolved on :root of https://www.revolut.com/ and typed
                          in here: no raw/foundation.json was kept, so these and
                          the painted-chrome values are labelled Reconstruction
                          unless raw/ holds the same value

The marketing site and the signed-out SSO wall both ship Revolut UI (`--rui-*`).
A token is the computed value, never a guessed one. Empty computed values
(radius-none, a couple of gradients) are listed under $extensions.notTokenised.
Every token carries $extensions.source. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = HERE / "raw"

LIGHT_PAGE = "https://www.revolut.com/ html[data-theme=light] computed style, 2026-11-19"
DARK_PAGE = "https://www.revolut.com/our-pricing-plans/ html[data-theme=dark] computed style, 2026-11-19"
ROOT_PAGE = "https://www.revolut.com/ :root computed style, 2026-11-19"
HOME_CHROME = "https://www.revolut.com/ painted chrome, computed style, 2026-11-19"
SSO_CHROME = "https://sso.revolut.com/signin signed-out wall, computed style, 2026-11-19. Phone field was not filled. No account was created."

SOURCE = "Measured"


def tok(value, type_, source, evidence="Measured"):
    return {
        "$value": value,
        "$type": type_,
        "$extensions": {"source": source, "evidence": evidence},
    }


def hex_of(value):
    """A computed colour as #rrggbb or #rrggbbaa. rgb()/rgba() with spaces or
    commas both appear in the readings. A slash alpha (`rgb(35 79 166/0.5)`)
    is kept as a colour too."""
    v = value.strip()
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", v):
        h = v.lower()
        if len(h) == 4:
            h = "#" + "".join(c * 2 for c in h[1:])
        return h
    m = re.fullmatch(
        r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*/\s*|\s*,\s*)(\d*\.?\d+)\s*\)",
        v,
    )
    if not m:
        m3 = re.fullmatch(r"rgb\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*\)", v)
        if not m3:
            return None
        r, g, b = (int(m3.group(i)) for i in (1, 2, 3))
        return "#%02x%02x%02x" % (r, g, b)
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    a = float(m.group(4))
    if a >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    ai = max(0, min(255, round(a * 255)))
    return "#%02x%02x%02x%02x" % (r, g, b, ai)


def rem_to_px(value):
    """1rem is 16px on both measured pages (body font-size 16px)."""
    v = value.strip()
    if v in ("0", "0px"):
        return "0px"
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", v)
    if m:
        px = float(m.group(1)) * 16
        return ("%g" % round(px, 3)) + "px"
    m = re.fullmatch(r"(-?\d*\.?\d+)px", v)
    if m:
        return ("%g" % round(float(m.group(1)), 3)) + "px"
    return None


def name_of(prop):
    return prop.removeprefix("--rui-").replace("-", ".")


def colour_group(colors, source):
    out, skipped = {}, []
    for prop in sorted(colors):
        if not prop.startswith("--rui-color-"):
            continue
        raw = colors[prop]
        if not raw:
            skipped.append(prop)
            continue
        hx = hex_of(raw)
        if not hx:
            skipped.append(prop + "=" + raw)
            continue
        key = prop.removeprefix("--rui-color-").replace("-", ".")
        out[key] = tok(hx, "color", source + " " + prop + "=" + raw)
    return out, skipped


def foundation():
    """Type, radius, space, size, shadow, motion. Shared by both themes."""
    # Computed on https://www.revolut.com/ :root, 2026-11-19.
    font = {
        "marketing": tok(
            "Aeonik Pro, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Helvetica, Arial, Arimo, sans-serif",
            "fontFamily",
            ROOT_PAGE + " --rui-font-marketing",
        ),
        "brand": tok(
            "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Helvetica, Arial, Arimo, sans-serif",
            "fontFamily",
            ROOT_PAGE + " --rui-font-brand",
        ),
        "system": tok(
            "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Helvetica, Arial, Arimo, sans-serif",
            "fontFamily",
            ROOT_PAGE + " --rui-font-default",
        ),
    }
    # Composite styles. Sizes are the declared rem scale (body 16px, so 1rem = 16px).
    # Weights are the *resolved* weights, which differ from the declared ones on
    # the marketing site (body declared 400, computed 500).
    styles = {
        "marketing-display1": ("3.5rem", "500", "1", "calc(-0.5em / 56)", "marketing"),
        "marketing-display2": ("2.5rem", "500", "1", "calc(-0.5em / 40)", "marketing"),
        "marketing-display3": ("2rem", "500", "1.125", "calc(-0.35em / 32)", "marketing"),
        "display1": ("3.5rem", "800", "1.1818181818181819", "0", "marketing"),
        "display2": ("2.75rem", "800", "1.1818181818181819", "0", "marketing"),
        "heading1": ("1.5rem", "800", "1.25", "0", "marketing"),
        "heading2": ("1.5rem", "800", "1.25", "0", "marketing"),
        "heading3": ("1.25rem", "800", "1.4", "0", "marketing"),
        "subheader": ("1.125rem", "700", "1.3333333333333333", "0", "brand"),
        "emphasis1": ("1rem", "700", "1.375", "0", "brand"),
        "emphasis2": ("0.875rem", "700", "1.4285714285714286", "0", "brand"),
        "emphasis3": ("0.75rem", "700", "1.5", "0", "brand"),
        "emphasis4": ("0.6875rem", "700", "1.2727272727272727", "0", "brand"),
        "body1": ("1rem", "500", "1.375", "0", "brand"),
        "body2": ("0.875rem", "500", "1.4285714285714286", "0", "brand"),
        "body3": ("0.75rem", "500", "1.5", "0", "brand"),
    }
    typography = {}
    for name, (size, weight, lh, ls, family) in styles.items():
        px = rem_to_px(size)
        style = {
            "fontFamily": "{core.font." + family + "}",
            "fontSize": px,
            "fontWeight": int(weight),
            "lineHeight": round(float(lh), 4),
        }
        if ls not in ("0", "normal"):
            # Marketing display tracking is a calc the spec cannot hold as em.
            # Keep the declared calc in the source and omit letterSpacing here.
            pass
        typography[name] = {
            "$value": style,
            "$type": "typography",
            "$extensions": {
                "source": ROOT_PAGE + " --rui-font-size-" + name + " and the matching weight, line-height, letter-spacing",
                "evidence": "Measured",
                "letterSpacing": ls,
            },
        }
    radii = {
        "r2": "0.125rem", "r4": "0.25rem", "r6": "0.375rem", "r8": "0.5rem",
        "r12": "0.75rem", "r16": "1rem", "r24": "1.5rem", "r32": "2rem",
        "round": "9999px", "widget": "1rem", "popup": "1.5rem",
        "status-popup": "2.75rem", "nested-widget": "0.75rem", "cell": "1rem",
        "nested-cell": "0.75rem",
    }
    radius = {}
    for name, value in radii.items():
        radius[name] = tok(rem_to_px(value), "dimension", ROOT_PAGE + " --rui-radius-" + name + "=" + value)
    spaces = {
        "sp50": "0.125rem", "sp100": "0.25rem", "sp150": "0.375rem", "sp200": "0.5rem",
        "sp300": "0.75rem", "sp400": "1rem", "sp500": "1.25rem", "sp600": "1.5rem",
        "sp800": "2rem", "sp1000": "2.5rem",
        "s2": "0.125rem", "s4": "0.25rem", "s6": "0.375rem", "s8": "0.5rem",
        "s12": "0.75rem", "s16": "1rem", "s20": "1.25rem", "s24": "1.5rem",
        "s32": "2rem", "s40": "2.5rem",
    }
    space = {}
    for name, value in spaces.items():
        space[name] = tok(rem_to_px(value), "dimension", ROOT_PAGE + " --rui-space-" + name + "=" + value)
    sizes = {
        "s2": "0.125rem", "s4": "0.25rem", "s6": "0.375rem", "s8": "0.5rem",
        "s12": "0.75rem", "s16": "1rem", "s20": "1.25rem", "s24": "1.5rem",
        "s32": "2rem", "s40": "2.5rem", "s48": "3rem", "s56": "3.5rem",
        "s64": "4rem", "s72": "4.5rem",
        "button-xs": "1.875rem", "button-sm": "2.5rem", "button-md": "3.25rem",
        "control-sm": "2.25rem",
    }
    size = {}
    for name, value in sizes.items():
        size[name] = tok(rem_to_px(value), "dimension", ROOT_PAGE + " --rui-size-" + name + "=" + value)
    shadows = {
        "level1": "0 2px 3px #0000000d",
        "level2": "0 3px 8px #0000001a",
        "level3": "0 3px 30px #00000014",
        "level4": "0 16px 64px #0000001f",
        "side": "0 2px 4px #0000000d, 0 3px 16px #0000001a",
        "popover": "0 4px 4px #00000000, 0 16px 48px #00000029",
    }
    # The computed forms were rem. Converted at 16px, which is the measured root size.
    shadow_src = {
        "level1": "0 0.125rem 0.1875rem rgb(0 0 0/0.05)",
        "level2": "0 0.1875rem 0.5rem rgb(0 0 0/0.1)",
        "level3": "0 0.1875rem 1.875rem rgb(0 0 0/0.08)",
        "level4": "0 1rem 4rem rgb(0 0 0/0.12)",
        "side": "0 0.125rem 0.25rem rgb(0 0 0/0.05), 0 0.1875rem 1rem rgb(0 0 0/0.1)",
        "popover": "0 0.25rem 0.25rem rgb(0 0 0/0), 0 1rem 3rem rgb(0 0 0/0.16)",
    }
    shadow = {}
    for name, value in shadows.items():
        shadow[name] = tok(value, "shadow", ROOT_PAGE + " --rui-shadow-" + name + "=" + shadow_src[name])
    duration = {
        "xs": "100ms", "sm": "200ms", "md": "300ms", "lg": "450ms", "xl": "900ms",
        "skeleton": "1500ms",
    }
    motion_duration = {
        name: tok(value, "duration", ROOT_PAGE + " --rui-duration-" + name)
        for name, value in duration.items()
    }
    easing = {
        "default": "cubic-bezier(0.15, 0.5, 0.5, 1)",
        "shadow": "cubic-bezier(0.4, 0.3, 0.8, 0.6)",
        "toast": "cubic-bezier(0.175, 0.885, 0.21, 1.65)",
    }
    # DTCG cubicBezier is four numbers, not the CSS function text.
    motion_easing = {
        name: tok([float(x) for x in re.fullmatch(r"cubic-bezier\(([^)]*)\)", value).group(1).split(",")],
                  "cubicBezier", ROOT_PAGE + " --rui-easing-" + name + " " + value)
        for name, value in easing.items()
    }
    return {
        "font": font,
        "typography": typography,
        "radius": radius,
        "space": space,
        "size": size,
        "shadow": shadow,
        "motion": {"duration": motion_duration, "easing": motion_easing},
    }


def semantic(colors, source, chrome):
    group, skipped = colour_group(colors, source)
    group["focus"] = {
        "outline": tok(
            "2px solid #234fa680" if "light" in source else "2px solid #6fa0ff80",
            "shadow",
            source + " --rui-focus-outline",
        )
    }
    # Painted chrome, measured on the element, not only the token.
    for key, (value, type_, src) in chrome.items():
        node = group
        parts = key.split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = tok(value, type_, src)
    return group, skipped


def light_chrome():
    return {
        "text.hero": ("#ffffff", "color", HOME_CHROME + " h1 Banking & Beyond on the dark hero, color rgb(255, 255, 255), font Aeonik Pro 500, size 82.6351px, tracking -2.08px"),
        "text.section": ("#1f1f1f", "color", HOME_CHROME + " h2 Your salary, reimagined, color rgb(31, 31, 31), Aeonik Pro 500, size 49.3176px"),
        "text.meta": ("#717173", "color", HOME_CHROME + " h2 Join 80+ million customers, color rgb(113, 113, 115), Inter 400, 16px"),
        "text.lede": ("#ffffff", "color", HOME_CHROME + " hero paragraph, Aeonik Pro 400, 18px, line-height 24px"),
        "button.login.background": ("#000000", "color", HOME_CHROME + " header Log in, background rgb(0, 0, 0), color rgb(255, 255, 255), padding 10px 24px, radius 9999px, Aeonik Pro 500 16px/22px"),
        "button.login.text": ("#ffffff", "color", HOME_CHROME + " header Log in label"),
        "button.signup.background": ("#ffffff", "color", HOME_CHROME + " header Sign up, background rgb(255, 255, 255), color rgb(0, 0, 0), padding 10px 24px, radius 9999px"),
        "button.signup.text": ("#000000", "color", HOME_CHROME + " header Sign up label"),
        "button.download.background": ("#1f1f1f", "color", HOME_CHROME + " Download the app, background rgb(31, 31, 31), color rgb(255, 255, 255), padding 10px 24px, radius 9999px, height 42px"),
        "button.download.text": ("#ffffff", "color", HOME_CHROME + " Download the app label"),
        "footer.background": ("#191c1f", "color", HOME_CHROME + " footer background rgb(25, 28, 31), padding 20px 84.5px"),
        "nav.height": ("56px", "dimension", HOME_CHROME + " header height 56px, width 1169px at the measured viewport"),
    }


def dark_chrome():
    return {
        "sso.page": ("#00010a", "color", SSO_CHROME + " html background rgb(0, 1, 10), color-scheme dark, data-theme=dark"),
        "sso.heading": ("#ffffff", "color", SSO_CHROME + " h1 Welcome back, Aeonik Pro 400, 21px / 26px, color rgb(255, 255, 255)"),
        "sso.continue.background": ("#ffffff", "color", SSO_CHROME + " Continue button, background rgb(255, 255, 255), color rgb(0, 0, 0), height 44px, padding 0 16px, radius 9999px, Inter 500 15px"),
        "sso.continue.text": ("#000000", "color", SSO_CHROME + " Continue label"),
        "sso.create.background": ("#191c1f", "color", SSO_CHROME + " Create account button, background rgb(25, 28, 31), color rgb(255, 255, 255), height 44px, radius 9999px"),
        "sso.create.text": ("#ffffff", "color", SSO_CHROME + " Create account label"),
        "sso.phone.well": ("#ffffff3d", "color", SSO_CHROME + " phone field wrapper background rgba(255, 255, 255, 0.24), radius 12px, padding 12px, height 48px. The input itself was transparent and was not filled."),
        "sso.alt.background": ("#ffffff12", "color", SSO_CHROME + " Continue with email icon button, background rgba(255, 255, 255, 0.07), 40px circle"),
    }


def build():
    light_colors = json.loads((RAW / "light-colors.json").read_text())
    dark_doc = json.loads((RAW / "dark-colors.json").read_text())
    dark_colors = dark_doc["colors"]
    # Focus outline lives in the light dump; the dark page resolved the same
    # property to a blue at 50% alpha. Recorded here from that read.
    dark_colors["--rui-focus-outline"] = "0.125rem solid rgb(111 160 255/0.5)"
    light, light_skip = semantic(light_colors, LIGHT_PAGE, light_chrome())
    dark, dark_skip = semantic(dark_colors, DARK_PAGE, dark_chrome())
    core = foundation()
    doc = {
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
        "$extensions": {
            "notTokenised": {
                "light": light_skip,
                "dark": dark_skip,
                "shared": [
                    "--rui-radius-none computed empty on :root",
                    "--rui-easing-linear computed as the string \"linear\" (quoted), not a cubic-bezier",
                    "--rui-letter-spacing-marketing-display1 calc(-0.5em / 56), display2 calc(-0.5em / 40), display3 calc(-0.35em / 32): kept on the type token's $extensions.letterSpacing",
                    "hero h1 on the home page computed to 82.6351px / -2.08px, which is the marketing-display1 role at the measured 1169px viewport, not the 3.5rem token",
                ],
            },
            "viewport": {
                "innerWidth": 1169,
                "innerHeight": 731,
                "devicePixelRatio": 2,
                "visualViewport": {"width": 1169, "height": 731, "scale": 1},
                "note": "The preview tab was in fill mode. These are the measured CSS pixels, not a requested 1440 or 390.",
            },
        },
    }
    relabel_unread(doc)
    return doc


# raw/ holds only the --rui-color-* dumps. A Measured token whose value raw/ does not hold (as hex or
# rgb()) was typed in from the capture session: the foundation scales, the focus outlines and most
# painted-chrome values. Its evidence becomes Reconstruction (docs/EVIDENCE.md).
RAW_TEXT = re.sub(r"\s+", "", "".join(f.read_text().lower() for f in sorted(RAW.glob("*.json"))))
HAND = "Entered by hand at capture time; raw/ holds no reading of this value. Capture note: "



def _colours(text):
    """Every colour written in raw/, as (r, g, b, alpha): rgb()/rgba() with commas, spaces or a slash
    alpha, and #rgb/#rrggbb/#rrggbbaa."""
    out = []
    for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*(?:[,/]\s*(\d*\.?\d+)(%?))?\s*\)", text):
        a = 1.0 if m.group(4) is None else float(m.group(4)) / (100 if m.group(5) else 1)
        out.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), a))
    for m in re.finditer(r"#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{3})(?![0-9a-z])", text):
        out.append(_hex(m.group(0)))
    return out


def _hex(value):
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


RAW_COLOURS = _colours("".join(f.read_text().lower() for f in sorted(RAW.glob("*.json"))))


def colour_in_raw(value):
    """A hex colour is backed only by a raw colour with the same channels and the same opacity."""
    r, g, b, a = _hex(value)
    return any((r, g, b) == c[:3] and abs(a - c[3]) <= 0.01 for c in RAW_COLOURS)

def in_raw(value):
    v = str(value).strip().lower()
    if " " in v and "," not in v and not v.startswith(("#", "rgb")):
        # a compound such as "2px solid #234fa680": every part must be in raw/
        return all(in_raw(part) for part in v.split() if part not in ("solid", "dashed", "dotted", "inset"))
    forms = {v.replace(" ", "")}
    if re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", v):
        return colour_in_raw(v)
    m = re.fullmatch(r"(\d*\.?\d+)px", v)
    if m:
        forms.add(f"{float(m.group(1)) / 16:g}rem")
    return any(f in RAW_TEXT for f in forms)


def relabel_unread(doc):
    def walk(node):
        for k, v in node.items():
            if k.startswith("$") or not isinstance(v, dict):
                continue
            if "$value" in v:
                yield v
            else:
                yield from walk(v)
    for setname in ("core", "light", "dark"):
        for tok_ in walk(doc[setname]):
            ext, value = tok_["$extensions"], tok_["$value"]
            if ext.get("evidence") != "Measured" or (isinstance(value, str) and value.startswith("{")):
                continue
            if not isinstance(value, (str, int, float)) or not in_raw(value):
                ext["evidence"] = "Reconstruction"
                ext["source"] = HAND + ext["source"]


def write():
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    (HERE / "tokens.json").write_text(text)
    print(f"wrote tokens.json ({text.count(chr(10))} lines)")


if __name__ == "__main__":
    write()
