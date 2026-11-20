#!/usr/bin/env python3
"""Render style-guide.html from tokens.json + tools/style-guide.template.html.

Every colour, radius, shadow and type style on the page is a CSS custom property generated from
tokens.json, so the guide cannot drift from the token file. The `core` and `light` sets go on
`:root` and the `dark` set on `[data-mode="dark"]`, which is how Claude itself switches: the guide's
theme toggle sets data-mode on <html>. Aliases like {text.primary} become var(--text-primary).

Placeholders in the template:
  /*CORE*/ /*LIGHT*/ /*DARK*/     CSS custom property blocks
  /*TOKENS*/null                  a compact copy of the token tree for the JS tables
  <!--icon:NAME[:SIZE]-->         an SVG from icons/NAME.svg, inlined

Deterministic: same inputs, byte-identical output. Adapted from the Manus kit's builder.
"""
import json, os, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(name, t):
    v, ty = t["$value"], t["$type"]
    if ty in ("transition", "animation"):
        return None   # composites with no single CSS value; the Motion section reads them from the token tree
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        if isinstance(v, str):
            return alias(v)
        return ", ".join(("inset " if s.get("inset") else "") + f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}' for s in v)
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    if ty == "gradient":
        angle = t["$extensions"].get("angle", "180deg")
        return f"linear-gradient({angle}, " + ", ".join(f'{alias(s["color"])} {round(s["position"] * 100, 2)}%' for s in v) + ")"
    return alias(v)


# A light-only product has no dark set; every set that is missing renders as empty.
SETS = [s for s in ("core", "light", "dark") if s in T]
THEMES = [s for s in SETS if s != "core"]


# Only "</style" ends a <style> element early (an svg data URI's "<svg" or "</svg>" does not), so that
# one sequence is written "<\/style": a CSS escape that reads back as the same "/" in a string or url().
END_STYLE = re.compile(r"</(style)", re.I)
ESCAPED = r"<\\/\1"


def block(setname):
    """A set's custom properties; a set the product lacks renders as nothing."""
    if setname not in T:
        return ""
    return "\n".join(f"  {cssname(n)}: {END_STYLE.sub(ESCAPED, css_val(n, t))};" for n, t in flat(T[setname]) if css_val(n, t) is not None)


# a core name and a themed name must not land on the same custom property
_core = {cssname(n) for n, _ in flat(T["core"])}
for _set in THEMES:
    _clash = _core & {cssname(n) for n, _ in flat(T[_set])}
    if _clash:
        raise SystemExit(f"core and {_set} share custom properties: {sorted(_clash)[:5]}")


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        out = {"v": node["$value"], "t": node["$type"], "s": node["$extensions"]["source"]}
        for k in ("compact", "darkVariationAxis"):
            if k in node["$extensions"]:
                out[k] = node["$extensions"][k]
        if node.get("$description"):
            out["d"] = node["$description"]
        return out
    return {k: slim(v) for k, v in node.items() if not k.startswith("$")}


# Inlined into a <script>: "<" as \u003c keeps a value holding "</script>" or "<!--"
# from ending the script early. JSON.parse and a JS literal read it back unchanged.
data = json.dumps({k: slim(T[k]) if k in T else {} for k in ("core", "light", "dark")},
                  ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")

_uid = [0]
ICON_SRC = {}


def clean_svg(svg, size):
    svg = re.sub(r"<\?xml[^>]*>\s*", "", svg).strip()
    svg = re.sub(r"\s+", " ", svg).replace("> <", "><")
    for i in sorted(set(re.findall(r'id="([^"]+)"', svg))):
        _uid[0] += 1
        svg = svg.replace(f'id="{i}"', f'id="i{_uid[0]}"').replace(f"url(#{i})", f"url(#i{_uid[0]})")
    svg = re.sub(r"<svg\b", '<svg aria-hidden="true" focusable="false" class="ic"', svg, count=1)
    if size:
        svg = re.sub(r'\swidth="[^"]*"', "", svg, count=1)
        svg = re.sub(r'\sheight="[^"]*"', "", svg, count=1)
        svg = svg.replace("<svg ", f'<svg width="{size}" height="{size}" ', 1)
    return svg


def icon(m):
    name, size = m.group(1), m.group(2)
    src = ICON_SRC.setdefault(name, (HERE / "icons" / f"{name}.svg").read_text())
    return clean_svg(src, size)


tpl = (HERE / "tools" / "style-guide.template.html").read_text()
# A template's ADAPTED_FOR line names the product it was adapted for. The kit's says none: it is
# Claude's example, and a guide rendered from it would carry Claude's title and components. The line
# itself never reaches style-guide.html. A template with no such line renders as before.
adapted = re.search(r"^<!-- ADAPTED_FOR: ([^|]*?) *(?:\|.*)?-->\n", tpl, re.M)
if adapted and adapted.group(1).strip().lower() in ("", "none") and not os.environ.get("KIT_EXAMPLE"):
    raise SystemExit("style-guide.template.html is the kit's Claude example, not adapted: rewrite the parts marked PRODUCT (adapt), then name the product on its ADAPTED_FOR line")
if adapted:
    tpl = tpl[:adapted.start()] + tpl[adapted.end():]
html = (tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", block("dark"))
        .replace("/*TOKENS*/null", data))
html = re.sub(r"<!--icon:([a-z0-9-]+)(?::(\d+))?-->", icon, html)
(HERE / "style-guide.html").write_text(html)
print("style-guide.html:", len(html.encode()), "bytes;",
      " + ".join(f"{len(list(flat(T[s])))} {s}" for s in SETS), "tokens;", len(ICON_SRC), "icons")
