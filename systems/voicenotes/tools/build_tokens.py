#!/usr/bin/env python3
"""Build tokens.json from raw/computed.json.

Every colour, size and font name below is a value read on 2026-11-19 from
voicenotes.com with getComputedStyle, or a colour utility declared in the
page's own stylesheet. A value that was not on the page is not invented.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "computed.json").read_text())


def src(evidence, where, note=None):
    out = {"evidence": evidence, "where": where, "captured": RAW["captured"]}
    if note:
        out["note"] = note
    return {"source": out}


def to_hex(value):
    """A computed rgba(r, g, b, a) as #rrggbbaa (hex and aliases pass unchanged)."""
    m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", value)
    if not m:
        return value
    rgb = "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    a = float(m.group(4))
    return rgb if a >= 1 else rgb + "%02x" % round(a * 255)


def color(value, where, note=None):
    # The where text keeps the computed reading; the value is written as hex.
    note = note or (f"computed {value}" if value.startswith("rgba") else None)
    return {"$type": "color", "$value": to_hex(value), "$extensions": src("Measured", where, note)}


def dim(value, where, note=None):
    return {"$type": "dimension", "$value": value, "$extensions": src("Measured", where, note)}


def font(value, where, note=None):
    return {"$type": "fontFamily", "$value": value, "$extensions": src("Measured", where, note)}


def num(value, where, note=None):
    return {"$type": "number", "$value": value, "$extensions": src("Measured", where, note)}


def typo(value, where, note=None):
    return {"$type": "typography", "$value": value, "$extensions": src("Measured", where, note)}


def shadow(value, where, note=None):
    return {"$type": "shadow", "$value": value, "$extensions": src("Measured", where, note)}


def duration(value, where, note=None):
    return {"$type": "duration", "$value": value, "$extensions": src("Measured", where, note)}


def cubic(value, where, note=None):
    return {"$type": "cubicBezier", "$value": value, "$extensions": src("Measured", where, note)}


HOME = "https://voicenotes.com/ computed style, viewport 1169x731"
PRICING = "https://voicenotes.com/pricing computed style"
BLOG = "https://voicenotes.com/blog/ computed style"
LOGIN = "login modal on https://voicenotes.com/"
SHEET = "stylesheet colour utility on voicenotes.com"

doc = {
    "core": {
        "font": {
            "family": {
                "inter": font(
                    "Inter, -apple-system, system-ui, Segoe UI, Roboto, sans-serif",
                    BLOG,
                    "Blog body computed Inter. Marketing pages load separate faces named Inter Regular, Inter Medium, Inter SemiBold.",
                ),
                "inter-regular": font('"Inter Regular", serif', HOME + " lede"),
                "inter-medium": font('"Inter Medium", serif', HOME + " nav link"),
                "inter-semibold": font('"Inter SemiBold", serif', HOME + " hero button"),
                "mackinac": font(
                    '"P22 Mackinac Pro", Georgia, "Times New Roman", serif',
                    BLOG + " h1",
                    "Home h1 computed P22MackinacPro-Medium. Pricing h1 computed P22MackinacPro-Book. Both files are @font-face on the marketing page.",
                ),
                "instrument": font("InstrumentSerif-Regular, serif", HOME + " h2"),
            }
        },
        "fontWeight": {
            "book": num(400, HOME + " h1 fontWeight"),
            "medium": num(500, BLOG + " post title fontWeight"),
        },
        "typography": {
            "display-home": typo(
                {
                    "fontFamily": "{font.family.mackinac}",
                    "fontSize": "48px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "56px",
                    "letterSpacing": "-1.4px",
                },
                HOME + " h1",
                "Class asks for 60px/68px/-1.8px. At 1169px the computed size is 48px/56px/-1.4px.",
            ),
            "display-section": typo(
                {
                    "fontFamily": "{font.family.instrument}",
                    "fontSize": "60px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "60px",
                    "letterSpacing": "-1.2px",
                },
                HOME + " h2",
            ),
            "display-blog": typo(
                {
                    "fontFamily": "{font.family.mackinac}",
                    "fontSize": "80px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "86px",
                    "letterSpacing": "-1.6px",
                },
                BLOG + " h1",
            ),
            "title-pricing": typo(
                {
                    "fontFamily": "{font.family.mackinac}",
                    "fontSize": "44px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "66px",
                    "letterSpacing": "-0.8px",
                },
                PRICING + " h1",
            ),
            "title-price": typo(
                {
                    "fontFamily": "{font.family.mackinac}",
                    "fontSize": "36px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "44px",
                    "letterSpacing": "-2px",
                },
                PRICING + " price",
            ),
            "title-modal": typo(
                {
                    "fontFamily": "{font.family.inter-medium}",
                    "fontSize": "24px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "32px",
                },
                LOGIN + " title",
            ),
            "body": typo(
                {
                    "fontFamily": "{font.family.inter-regular}",
                    "fontSize": "18px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "28px",
                },
                HOME + " lede",
            ),
            "body-blog": typo(
                {
                    "fontFamily": "{font.family.inter}",
                    "fontSize": "18px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "28.8px",
                },
                "blog post paragraph",
            ),
            "ui": typo(
                {
                    "fontFamily": "{font.family.inter-medium}",
                    "fontSize": "16px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "21px",
                },
                HOME + " nav link",
            ),
            "label": typo(
                {
                    "fontFamily": "{font.family.inter-medium}",
                    "fontSize": "14px",
                    "fontWeight": "{fontWeight.book}",
                    "lineHeight": "20px",
                },
                HOME + " nav primary button",
            ),
        },
        "radius": {
            "pricing-card": dim("4px", PRICING + " plan card borderRadius"),
            "sm": dim("6px", HOME + " .rounded-md"),
            "md": dim("8px", HOME + " .rounded-lg"),
            "lg": dim("12px", HOME + " .rounded-xl and login provider button"),
            "xl": dim("16px", HOME + " .rounded-2xl and login card"),
            "2xl": dim("24px", HOME + " .rounded-3xl"),
            "pill": dim("9999px", HOME + " nav and hero buttons"),
        },
        "spacing": {
            "1": dim("4px", HOME + " .gap-1"),
            "2": dim("8px", HOME + " .gap-2"),
            "3": dim("12px", HOME + " .gap-3 and nav link padding-inline"),
            "4": dim("16px", HOME + " .gap-4 and .p-4"),
            "5": dim("20px", HOME + " .p-5"),
            "6": dim("24px", HOME + " .gap-6 and login card padding-inline"),
            "10": dim("40px", HOME + " .gap-10 and login card padding-block-start"),
            "header": dim("70px", HOME + " header height"),
            "control-nav": dim("36px", HOME + " nav primary button height"),
            "control-hero": dim("46px", HOME + " hero button height"),
            "control-field": dim("48px", LOGIN + " email field height"),
        },
        "shadow": {
            "demo-card": shadow(
                {
                    "color": "rgba(0, 0, 0, 0.35)",
                    "offsetX": "0px",
                    "offsetY": "30px",
                    "blur": "70px",
                    "spread": "0px",
                },
                HOME + " demo card box-shadow, truncated in the reading at 70px",
                "The computed string was cut at 100 characters. Offset and blur after 30px 70px were not fully read.",
            )
        },
        "motion": {
            "duration": {
                "fast": duration("150ms", HOME + " button transition-duration 0.15s"),
                "base": duration("200ms", HOME + " other transition-duration 0.2s"),
            },
            "easing": {
                "standard": cubic([0.4, 0, 0.2, 1], HOME + " transition-timing-function"),
            },
        },
        "layout": {
            "content-narrow": dim("520px", HOME + " max-w-[520px]"),
            "content": dim("873px", HOME + " h1 max-w-[873px]"),
            "content-wide": dim("1240px", HOME + " max-w-[1240px]"),
            "modal": dim("450px", LOGIN + " card width"),
            "breakpoint-phone": dim("768px", "stylesheet @media (max-width: 768px)"),
            "breakpoint-desktop": dim("1024px", "stylesheet @media (min-width: 1024px)"),
        },
    },
    "light": {
        "color": {
            "page": color("#FAF9F5", HOME + " html backgroundColor"),
            "surface": color("#FFFFFF", LOGIN + " card backgroundColor"),
            "sand": color("#F2F1ED", PRICING + " billing track backgroundColor"),
            "quiet": color("#E6E5E0", PRICING + " quiet Get started backgroundColor"),
            "wash": color("#EAF2F8", HOME + " .bg-[#EAF2F8]"),
            "text": color("#0D0D0D", HOME + " .text-dark computed and stylesheet"),
            "text-soft": color("#222222", HOME + " h2 .text-dark22"),
            "ink": color("#1D1D1D", BLOG + " body color"),
            "muted": color("#717171", HOME + " .text-grey71"),
            "muted-60": color("rgba(13, 13, 13, 0.6)", HOME + " .text-dark/60 and pricing Monthly tab"),
            "on-accent": color("#FFFFFF", HOME + " nav primary button color"),
            "border": color("rgba(13, 13, 13, 0.1)", LOGIN + " provider button border"),
            "border-strong": color("#0D0D0D", HOME + " hero secondary button border"),
            "border-card": color("rgba(34, 34, 34, 0.08)", PRICING + " plan card border"),
            "accent": color("#0D0D0D", HOME + " nav primary button backgroundColor"),
            "link": color("#0088FF", "blog post link color"),
            "info": color("#00B3F8", HOME + " .bg-[#00B3F8]"),
            "success-bg": color("#E6F9EB", PRICING + " 2 months free badge background"),
            "success-text": color("#006119", PRICING + " badge color"),
            "danger": color("#FF4538", SHEET + " .text-red38"),
            "scrim": color("rgba(0, 0, 0, 0.5)", LOGIN + " scrim"),
            "field": color("rgba(13, 13, 13, 0.05)", LOGIN + " email field background"),
            "focus": color("#0D0D0D", LOGIN + " .tw-input-common-v2:focus border-color"),
        },
        "component": {
            "button-primary-bg": color("{color.accent}", HOME + " nav primary"),
            "button-primary-text": color("{color.on-accent}", HOME + " nav primary"),
            "button-primary-radius": dim("9999px", HOME + " nav primary borderRadius"),
            "button-secondary-text": color("{color.text}", HOME + " hero secondary"),
            "field-bg": color("{color.field}", LOGIN),
            "field-text": color("{color.text}", LOGIN),
            "field-radius": dim("16px", LOGIN + " email field"),
            "field-height": dim("48px", LOGIN + " email field"),
            "card-bg": color("{color.surface}", LOGIN),
            "card-radius": dim("16px", LOGIN + " card"),
            "button-primary-height": dim("36px", HOME + " nav primary height"),
            "button-secondary-bg": color("rgba(0, 0, 0, 0)", HOME + " hero secondary background"),
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

# The truncated demo-card shadow is not a full measurement. Keep it out of tokens.
del doc["core"]["shadow"]



# ---------------------------------------------------------------- check (finding 16-6)

def _token_paths(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield f"{path}{key}", value
        else:
            yield from _token_paths(value, f"{path}{key}.")


def _aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        return [a for v in value.values() for a in _aliases(v)]
    if isinstance(value, list):
        return [a for v in value for a in _aliases(v)]
    return []


def _follow(flat, s, ref, seen):
    """Follow an alias chain: each name resolves in the set it is read from, then core, then the
    root (the Resolver's order). Returns a problem string for a dead alias or a repeated token,
    else None."""
    # Own set, then core, then the root, where a set-qualified name such as core.color.white.solid
    # names a token in that set. The next hop resolves from the set the target was found in.
    candidates = [(s, ref), ("core", ref)]
    if "." in ref:
        candidates.append(tuple(ref.split(".", 1)))
    found = next(((fs, fp) for fs, fp in candidates if fp in flat.get(fs, {})), None)
    if found is None:
        return f"alias {{{ref}}} resolves nowhere"
    if found in seen:
        return f"alias loop through {{{ref}}}"
    target_set, target_path = found
    for nxt in _aliases(flat[target_set][target_path]["$value"]):
        err = _follow(flat, target_set, nxt, seen | {found})
        if err:
            return err
    return None


def check(doc):
    """Refuse a token with no source, a colour that is neither #rrggbb(aa) nor one whole alias, an
    alias that resolves in neither its own set nor core (the order tools/catalog.py's Resolver
    uses), and an alias chain that comes back to a token it already passed. Raises SystemExit."""
    sets = [s for s, v in doc.items() if not s.startswith("$") and isinstance(v, dict)]
    flat = {s: dict(_token_paths(doc[s])) for s in sets}
    core = flat.get("core", {})
    problems = []
    for s in sets:
        for path, token in flat[s].items():
            where = f"{s}.{path}"
            if not token.get("$extensions", {}).get("source"):
                problems.append(f"{where}: no source")
            value = token["$value"]
            for ref in _aliases(value):
                err = _follow(flat, s, ref, {(s, path)})
                if err:
                    problems.append(f"{where}: {err}")
            if token.get("$type") == "color":
                whole_alias = isinstance(value, str) and re.fullmatch(r"\{[^{}]+\}", value)
                if not whole_alias and not (isinstance(value, str) and re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", value)):
                    problems.append(f"{where}: colour {value!r} is not #rrggbb(aa) or one whole alias")
    if problems:
        raise SystemExit("token check failed:\n" + "\n".join(problems))


def render():
    """tokens.json's exact text, after the check; importing this module writes nothing."""
    check(doc)
    return json.dumps(doc, indent=2) + "\n"


if __name__ == "__main__":
    out = ROOT / "tokens.json"
    out.write_text(render())
    print("wrote", out)
