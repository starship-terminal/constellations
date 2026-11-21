#!/usr/bin/env python3
"""Render style-guide.html from tokens.json + tools/style-guide.template.html.

Every colour, radius, shadow and type style on the page is a CSS custom property generated from
tokens.json, so the guide cannot drift from the token file. The `core` and `light` sets go on
`:root`. Fourthwall publishes one light theme, so the dark toggle is unused. Aliases like
{color.ink} become var(--color-ink).

Placeholders in the template:
  /*CORE*/ /*LIGHT*/ /*DARK*/     CSS custom property blocks
  /*TOKENS*/null                  a compact copy of the token tree for the JS tables
  <!--icon:NAME[:SIZE]-->         an SVG from icons/NAME.svg, inlined

Deterministic: same inputs, byte-identical output. Adapted from the Manus kit's builder.
"""
import json, pathlib, re

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


def block(setname):
    """A set's custom properties; a set the product lacks renders as nothing."""
    if setname not in T:
        return ""
    lines = [f"  {cssname(n)}: {css_val(n, t)};" for n, t in flat(T[setname])]
    if setname == "light":
        # The shared template was written for Claude's names. Map the roles it
        # paints with onto Fourthwall's measured roles. Unmapped chrome stays
        # on paper and ink rather than inventing a second theme.
        lines += [
            "  --surface-1: var(--color-paper);",
            "  --surface-2: var(--color-paperSoft);",
            "  --surface-3: var(--color-paperSunken);",
            "  --text-secondary: var(--color-inkAlpha60);",
            "  --text-muted: var(--color-muted);",
            "  --border-strong: var(--color-ink);",
            "  --fill-primary: var(--color-ink);",
            "  --text-on-primary: var(--color-paper);",
            "  --fill-ghost-hover: var(--color-inkAlpha06);",
            "  --fill-ghost-selected: var(--color-inkAlpha11);",
            "  --fill-secondary: var(--color-paperSoft);",
            "  --fill-field: var(--color-paper);",
            "  --radius-card: var(--radius-lg);",
            "  --radius-row: var(--radius-sm);",
            "  --radius-template-card: var(--radius-md);",
        ]
    return "\n".join(lines)


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
    # Brand artwork is not kept (docs/RIGHTS.md). A missing icon renders as nothing.
    name = m.group(1)
    src_path = HERE / "icons" / f"{name}.svg"
    if not src_path.exists():
        return ""
    src = ICON_SRC.setdefault(name, src_path.read_text())
    return clean_svg(src, m.group(2))


tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = (tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", block("dark"))
        .replace("/*TOKENS*/null", data))
html = re.sub(r"<!--icon:([a-z0-9-]+)(?::(\d+))?-->", icon, html)
(HERE / "style-guide.html").write_text(html)
print("style-guide.html:", len(html.encode()), "bytes;",
      " + ".join(f"{len(list(flat(T[s])))} {s}" for s in SETS), "tokens;", len(ICON_SRC), "icons")
