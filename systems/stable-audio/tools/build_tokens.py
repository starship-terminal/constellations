#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json for the Stable Audio public capture.

PRODUCT (adapt): core() and semantic() map the readings. Helpers, check() and
build() stay generic. The public marketing site paints one dark theme
(html.bg-[#000], .sx-scope.sx-dark). The paper --sx-p-* ramp is declared on
:root and was not the painted page, so it stays in core.palette and is not a
light semantic set.

    python3 tools/build_tokens.py

Every token carries $extensions.source.evidence and .capture. Colours are
#RRGGBB or #RRGGBBAA. Dimensions are one px length. A light set is omitted
because no light theme was painted on the captured surfaces.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw" / "readings.json"
READ = json.loads(RAW.read_text())


class CheckError(AssertionError):
    pass


def require(ok, message):
    if not ok:
        raise CheckError(message)


def tok(value, typ, desc, evidence, capture):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


def color(rid):
    r = READ["colors"][rid]
    return tok(r["value"], "color", r["desc"], r["evidence"], r["capture"])


def dim(rid):
    r = READ["dimensions"][rid]
    return tok(r["value"], "dimension", r["desc"], r["evidence"], r["capture"])


def font(rid):
    r = READ["fonts"][rid]
    return tok(r["value"], "fontFamily", r["desc"], r["evidence"], r["capture"])


def weight(rid):
    r = READ["weights"][rid]
    return tok(r["value"], "fontWeight", r["desc"], r["evidence"], r["capture"])


def number(rid):
    r = READ["numbers"][rid]
    return tok(r["value"], "number", r["desc"], r["evidence"], r["capture"])


def cubic(rid):
    r = READ["easings"][rid]
    return tok(r["value"], "cubicBezier", r["desc"], r["evidence"], r["capture"])


def duration(rid):
    r = READ["durations"][rid]
    return tok(r["value"], "duration", r["desc"], r["evidence"], r["capture"])


def shadow(rid):
    r = READ["shadows"][rid]
    return tok(r["value"], "shadow", r["desc"], r["evidence"], r["capture"])


def other(rid, typ):
    r = READ["other"][rid]
    return tok(r["value"], typ, r["desc"], r["evidence"], r["capture"])


def type_style(family, weight, size, line, tracking, desc, capture):
    """Composite type style. Arguments are token names under font.*."""
    value = {
        "fontFamily": "{font.family." + family + "}",
        "fontWeight": "{font.weight." + weight + "}",
        "fontSize": "{font.size." + size + "}",
        "lineHeight": "{font.lineHeight." + line + "}",
        "letterSpacing": "{font.tracking." + tracking + "}",
    }
    return tok(value, "typography", desc, "Derived", capture)


def core():
    c = READ["colors"]
    d = READ["dimensions"]
    return {
        "palette": {k: color(k) for k in c if k.startswith("sx") or k.startswith("hn") or k.startswith("app")},
        "font": {
            "family": {
                "ui": font("uiComputed"),
                "uiDeclared": font("uiDeclared"),
                "displayDeclared": font("displayDeclared"),
                "monoDeclared": font("monoDeclared"),
                "monoKicker": font("monoKicker"),
                "bodyFallback": font("bodyFallback"),
                "auth": font("auth"),
            },
            "weight": {k: weight(k) for k in READ["weights"]},
            "size": {
                "kicker": dim("fsKicker"),
                "nav": dim("fsNav"),
                "body": dim("fsBody"),
                "lede": dim("fsLede"),
                "section": dim("fsSection"),
                "display": dim("fsDisplay"),
                "price": dim("fsPrice"),
                "authHeading": dim("fsAuthHeading"),
            },
            "lineHeight": {
                "kicker": number("lhKicker"),
                "nav": number("lhNav"),
                "body": number("lhBody"),
                "display": number("lhDisplay"),
                "textToken": number("lhTextToken"),
            },
            "tracking": {
                "kicker": dim("lsKicker"),
                "display": dim("lsDisplay"),
                "snug": dim("lsSnug"),
                "wide": dim("lsWide"),
                "none": dim("lsNone"),
            },
        },
        "typography": {
            "display": type_style(
                "ui", "semibold", "display", "display", "display",
                "Hero h1 at 1440: 72px, weight 600, line 73.44px, tracking -2.52px.",
                "h1.MixHero_title computed at 1440",
            ),
            "section": type_style(
                "ui", "semibold", "section", "display", "display",
                "Section title is 46px weight 600. Tracking is the display step (-2.52px). The computed section tracking was -1.38px, which is not its own token.",
                ".HomeSection_title computed 46px at 1440",
            ),
            "nav": type_style(
                "ui", "medium", "nav", "nav", "none",
                "Nav link and medium button: 13px, weight 500, line equal to the size.",
                ".HomeTopNav_link computed 13px",
            ),
            "body": type_style(
                "ui", "regular", "body", "body", "none",
                "Body: 16px, weight 400, line 24px.",
                "body computed 16px/24px",
            ),
            "kicker": type_style(
                "monoKicker", "medium", "kicker", "kicker", "kicker",
                "Mono kicker: 11px SX Plex Mono, weight 500, tracking 0.44px.",
                ".MixHero_kicker computed 11px",
            ),
        },
        "space": {k: dim(k) for k in d if k.startswith("sp")},
        "radius": {
            "control": dim("rControl"),
            "card": dim("rCard"),
            "chip": dim("rChip"),
            "menu": dim("rMenu"),
            "dialog": dim("rDialog"),
            "large": dim("rLarge"),
            "pill": dim("rPill"),
            "pricingCard": dim("rPricingCard"),
            "authCard": dim("rAuthCard"),
            "authField": dim("rAuthField"),
            "authButton": dim("rAuthButton"),
        },
        "size": {
            "navBar": dim("navBarH"),
            "buttonMd": dim("buttonMdH"),
            "buttonLg": dim("buttonLgH"),
            "iconButton": dim("iconButton"),
            "tapMin": dim("tapMin"),
            "badge": dim("badgeH"),
            "field": dim("fieldH"),
            "faqQuestion": dim("faqQuestionH"),
            "menuLink": dim("menuLinkH"),
            "authCard": dim("authCardW"),
        },
        "motion": {
            "duration": {k: duration(k) for k in READ["durations"]},
            "easing": {k: cubic(k) for k in READ["easings"]},
        },
        "elevation": {
            "nav": shadow("nav"),
            "wordUnderline": shadow("wordUnderline"),
            "authCard": shadow("authCard"),
            "authPrimary": shadow("authPrimary"),
            "focus": other("focusRing", "shadow"),
        },
    }


def semantic():
    """The painted dark marketing theme, plus the AuthKit sign-in card."""
    return {
        "background": {
            "page": color("page"),
            "bar": color("bar"),
            "card": color("card"),
            "menu": color("menu"),
            "navGround": color("navGround"),
            "chatPanel": color("chatPanel"),
            "deckPanel": color("deckPanel"),
            "bowl": color("bowl"),
            "authPage": color("authPage"),
            "primary": color("primaryPainted"),
            "primaryHome": color("primaryHome"),
            "primaryHover": color("primaryHover"),
        },
        "text": {
            "primary": color("textPrimary"),
            "secondary": color("textSecondary"),
            "muted": color("textMuted"),
            "accent": color("textAccent"),
            "onPrimary": color("onPrimary"),
            "kicker": color("textKicker"),
            "link": color("textLink"),
            "authHeading": color("authHeading"),
            "authLink": color("authLink"),
            "authMuted": color("authMuted"),
        },
        "border": {
            "faint": color("ruleFaint"),
            "soft": color("ruleSoft"),
            "strong": color("rule"),
            "badge": color("badgeBorder"),
            "recommended": color("recommendedBorder"),
            "focus": color("focus"),
        },
        "status": {
            "ok": color("ok"),
            "warn": color("warn"),
            "danger": color("danger"),
            "info": color("info"),
            "accentToken": color("accentToken"),
        },
    }


def walk(node, prefix=()):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from walk(v, prefix + (k,))


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            require(src.get("evidence") and src.get("capture"), f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                require(a in paths, f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            if t["$type"] == "color":
                require(re.fullmatch(r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", v), f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                require(re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}")
            elif t["$type"] == "duration":
                require(re.fullmatch(r"\d+(\.\d+)?ms", v), f"{where}: bad duration {v}")
            elif t["$type"] == "cubicBezier":
                require(isinstance(v, list) and len(v) == 4, f"{where}: bad easing")
    if "light" in doc and "dark" in doc:
        keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
        require(keys("light") == keys("dark"), "light and dark keys differ")


def build():
    doc = {
        "core": core(),
        "dark": semantic(),
        "$themes": [{
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "The public marketing site paints html.bg-[#000] and .sx-scope.sx-dark. No light theme was switched on the captured pages.",
        }],
        "$metadata": {"tokenSetOrder": ["core", "dark"]},
    }
    check(doc)
    out = PKG / "tokens.json"
    out.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {out} ({sum(1 for _ in walk(doc['core']))} core, {sum(1 for _ in walk(doc['dark']))} dark)")


if __name__ == "__main__":
    build()
