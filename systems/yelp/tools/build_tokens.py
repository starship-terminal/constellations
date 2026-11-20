#!/usr/bin/env python3
"""Build systems/yelp/tokens.json from the live computed custom properties.

Source: raw/css-vars.tsv, written from getComputedStyle(document.documentElement)
on https://www.yelp.com/about on 2026-11-19, signed out, light color-scheme.
Yelp stores colour channels as "R,G,B" triplets (used as rgba(var(--token), 1)).
There is no dark token set on the public pages, and no spacing, radius, or
type custom properties. Those component sizes live in raw/components.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SRC = "getComputedStyle(documentElement) on yelp.com/about, 2026-11-19, signed out, light"


def hex_of(triplet: str) -> str:
    parts = [int(p) for p in triplet.split(",")]
    if len(parts) != 3 or any(n < 0 or n > 255 for n in parts):
        raise ValueError(triplet)
    return "#{:02X}{:02X}{:02X}".format(*parts)


def color(value, source=SRC):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": source}},
    }


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?px", value):
        raise ValueError(value)
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": source}},
    }


def fontw(value, source):
    return {
        "$type": "fontWeight",
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": source}},
    }


def typography(value, source):
    return {
        "$type": "typography",
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": source}},
    }


def shadow(value, source):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": {"evidence": "Measured", "capture": source}},
    }


def load_vars():
    rows = {}
    for line in (RAW / "css-vars.tsv").read_text().splitlines():
        name, val = line.split("\t", 1)
        rows[name] = val.strip()
    return rows


def nest(tree, path, token):
    node = tree
    for part in path[:-1]:
        node = node.setdefault(part, {})
    node[path[-1]] = token


def build():
    vars_ = load_vars()
    core = {"color": {"ref": {}, "rating": {}}}
    light = {"color": {}}
    for name, raw in sorted(vars_.items()):
        if not re.fullmatch(r"\d{1,3},\d{1,3},\d{1,3}", raw):
            continue
        hx = hex_of(raw)
        if name.startswith("--ref-color-"):
            rest = name[len("--ref-color-"):]
            if rest.startswith("yelp-") or re.fullmatch(r"[a-z]+-\d+", rest) or rest in ("black-100", "white-100"):
                family, step = rest.rsplit("-", 1)
                core["color"]["ref"].setdefault(family, {})[step] = color(hx, f"{name} = {raw}")
            else:
                core["color"]["ref"].setdefault("named", {})[rest] = color(hx, f"{name} = {raw}")
        elif name.startswith("--sem-color-bg-rating-"):
            step = name.rsplit("-", 1)[-1]
            core["color"]["rating"][step] = color(hx, f"{name} = {raw}")
        elif name.startswith("--sem-color-"):
            path = name[len("--sem-color-"):].split("-")
            nest(light["color"], path, color(hx, f"{name} = {raw}"))

    # Component sizes measured on the live signed-out pages. Sources are in raw/components.json.
    home = "yelp.com homepage, computed style, 1169x731, 2026-11-19"
    search = "yelp.com/search coffee San Francisco, computed style, 1169x731, 2026-11-19"
    about = "yelp.com/about, computed style, 1169x731, 2026-11-19"
    login = "yelp.com/login, computed style, not submitted, 2026-11-19"
    biz = "yelp.com/biz/kope-house-san-francisco, computed style, 2026-11-19"
    core["font"] = {
        "family": {
            "display": {
                "$type": "fontFamily",
                "$value": 'Poppins, "Helvetica Neue", Helvetica, Arial, sans-serif',
                "$extensions": {"source": {"evidence": "Measured", "capture": home + " h1"}},
            },
            "ui": {
                "$type": "fontFamily",
                "$value": '"Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif',
                "$extensions": {"source": {"evidence": "Measured", "capture": home + " logo and search input"}},
            },
        }
    }
    core["fontWeight"] = {
        "regular": fontw(400, home + " body links"),
        "medium": fontw(500, "cookie Allow all button, Poppins 500 loaded"),
        "semibold": fontw(600, search + " filter chip and logo"),
        "bold": fontw(700, home + " hero h1"),
    }
    core["typography"] = {
        "hero": typography(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.bold}", "fontSize": "48px", "lineHeight": "56px", "letterSpacing": "-0.4px"},
            home + " h1",
        ),
        "display": typography(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.bold}", "fontSize": "60px", "lineHeight": "75px"},
            about + " h1",
        ),
        "pageTitle": typography(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.bold}", "fontSize": "24px", "lineHeight": "32px"},
            search + " h1",
        ),
        "notFound": typography(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.bold}", "fontSize": "28px", "lineHeight": "36px"},
            "yelp.com 404 h1",
        ),
        "resultName": typography(
            {"fontFamily": "{font.family.display}", "fontWeight": "{fontWeight.bold}", "fontSize": "20px", "lineHeight": "20px"},
            search + " result name",
        ),
        "ui": typography(
            {"fontFamily": "{font.family.ui}", "fontWeight": "{fontWeight.regular}", "fontSize": "16px", "lineHeight": "20px"},
            home + " search input",
        ),
        "chip": typography(
            {"fontFamily": "{font.family.ui}", "fontWeight": "{fontWeight.semibold}", "fontSize": "12px", "lineHeight": "16px"},
            search + " filter chip",
        ),
        "nav": typography(
            {"fontFamily": "{font.family.ui}", "fontWeight": "{fontWeight.semibold}", "fontSize": "14px", "lineHeight": "20px"},
            home + " logo link",
        ),
    }
    core["radius"] = {
        "link": dim("4px", home + " category link"),
        "search": dim("8px", home + " search form"),
        "loginField": dim("3px", login + " email input"),
        "pill": dim("20px", home + " Sign Up button"),
        "chip": dim("10000px", search + " Price filter"),
    }
    core["spacing"] = {
        "chipPadY": dim("7px", search + " filter chip padding-block"),
        "chipPadX": dim("11px", search + " filter chip padding-inline"),
        "buttonPadY": dim("8px", home + " Sign Up padding-block"),
        "buttonPadX": dim("16px", home + " Sign Up padding-inline"),
        "headerPadTop": dim("24px", home + " header padding-top"),
        "headerPadX": dim("40px", home + " header padding-inline"),
        "fieldPadY": dim("13px", home + " search input padding-block"),
        "fieldPadX": dim("15px", home + " search input padding-inline"),
    }
    core["size"] = {
        "button": dim("40px", home + " Sign Up height"),
        "search": dim("48px", home + " search form height"),
        "chip": dim("32px", search + " filter chip height"),
        "loginField": dim("30px", login + " email input height"),
        "star": dim("20px", search + " rating star svg"),
    }
    core["shadow"] = {
        "search": shadow(
            {"color": "#00000029", "offsetX": "0px", "offsetY": "0px", "blur": "18px", "spread": "0px"},
            home + " search form box-shadow rgba(0,0,0,0.16) 0 0 18px",
        )
    }
    light["component"] = {
        "signup": {
            "bg": color("{color.bg.brandPrimary.strong.default}", home + " Sign Up background"),
            "text": color("{color.text.onStrong}", home + " Sign Up color"),
            "radius": dim("20px", home + " Sign Up border-radius"),
            "height": dim("40px", home + " Sign Up height"),
            "padding": dim("8px", home + " Sign Up padding-block; inline is 16px"),
        },
        "login": {
            "bg": color("#F0F0F0", search + " Sign in background rgb(240,240,240)"),
            "text": color("{color.text.default}", search + " Sign in color"),
            "radius": dim("20px", search + " Sign in border-radius"),
            "height": dim("40px", search + " Sign in height"),
        },
        "search": {
            "bg": color("{color.surface.default}", home + " search field"),
            "text": color("{color.text.default}", home + " search input color"),
            "radius": dim("8px", home + " search form border-radius"),
            "height": dim("48px", home + " search form height"),
        },
        "searchButton": {
            "bg": color("{color.bg.brandPrimary.strong.default}", search + " Search button"),
            "text": color("{color.text.onStrong}", search + " Search button"),
            "radius": dim("8px", search + " Search button border-radius"),
            "height": dim("48px", search + " Search button height"),
        },
        "chip": {
            "bg": color("{color.surface.default}", search + " Price chip"),
            "text": color("{color.text.default}", search + " Price chip"),
            "radius": dim("10000px", search + " Price chip border-radius"),
            "height": dim("32px", search + " Price chip height"),
        },
        "focus": {
            "outline": color("{color.border.focused}", about + " Sign Up :focus outline rgb(0,118,146) solid 2px"),
        },
    }
    doc = {
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    check(doc)
    return json.dumps(doc, indent=2) + "\n"


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


if __name__ == "__main__":
    text = build()
    (HERE / "tokens.json").write_text(text)
    print(f"wrote {HERE / 'tokens.json'} ({text.count(chr(10))} lines)")
