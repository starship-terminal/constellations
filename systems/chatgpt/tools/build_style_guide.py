#!/usr/bin/env python3
"""Render style-guide.html from tokens.json + tools/style-guide.template.html.

Every colour, radius, shadow, size, duration and type style on the page is a CSS custom property
generated from tokens.json, so the guide cannot drift from the token file. The `core` set goes on
`:root`, the `light` set on `:root, [data-theme="light"]` and the `dark` set on `[data-theme="dark"]`,
which mirrors ChatGPT's own `.chatgpt-theme[data-theme=...]` switch: the guide's Dark toggle flips
`data-theme` on <html>, and any element can carry `data-theme` to show one theme beside the other.
A token `a.b-c` becomes `--a-b-c` (any character outside [A-Za-z0-9-] becomes `-`, so `spacing.1_5`
is `--spacing-1-5`), and an alias like {text.primary} becomes var(--text-primary).

How each $type is written:
  color, dimension, duration, number, fontWeight   the value as is (aliases become var())
  fontFamily                                       a font-family list, quoting names that need it
  cubicBezier                                      cubic-bezier(x1, y1, x2, y2)
  shadow                                           a box-shadow list (an alias becomes var())
  typography                                       the `font` shorthand (weight size/line-height family);
                                                   the letter spacing, which `font` cannot carry, goes
                                                   in a sibling property `--<name>-letterSpacing`
Any other $type stops the build, and so does a var() in the template naming a property that is
neither generated here nor a guide-local `--g-*` one.

Placeholders in the template:
  /*CORE*/ /*LIGHT*/ /*DARK*/     CSS custom property blocks
  /*TOKENS*/null                  a compact copy of the three sets and $themes for the JS tables
  <!--icon:NAME[:SIZE]-->         an SVG from icons/NAME.svg, inlined at SIZE px (default: its viewBox size);
                                  a missing file stops the build
  <!--icons:all-->                every icon in icons/, grouped by its role in icons/INDEX.tsv

Deterministic: same inputs, byte-identical output. Adapted from the Gauth kit's builder.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
SETS = ("core", "light", "dark")
GENERIC_FAMILIES = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "ui-serif", "ui-sans-serif",
                    "ui-monospace", "ui-rounded", "emoji", "math", "fangsong"}


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def family(v):
    if isinstance(v, str):
        return alias(v)
    out = []
    for f in v:
        if f in GENERIC_FAMILIES or re.fullmatch(r"-?[A-Za-z_][A-Za-z0-9_-]*", f):
            out.append(f)
        else:
            out.append('"' + f.replace('"', '\\"') + '"')
    return ", ".join(out)


KNOWN_TYPES = {"color", "dimension", "duration", "number", "fontWeight", "fontFamily", "cubicBezier", "shadow", "typography"}


def css_val(name, t):
    v, ty = t["$value"], t["$type"]
    if ty not in KNOWN_TYPES:
        raise SystemExit(f"build_style_guide: no CSS form for $type {ty!r} ({name})")
    if ty == "fontFamily":
        return family(v)
    if isinstance(v, str) or ty in ("color", "dimension", "duration", "number", "fontWeight"):
        return alias(v)
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        layers = v if isinstance(v, list) else [v]
        return ", ".join(("inset " if s.get("inset") else "") + f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}'
                         for s in layers)
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {family(v["fontFamily"])}'


def decls(setname):
    for n, t in flat(T[setname]):
        yield cssname(n), css_val(n, t)
        if t["$type"] == "typography" and isinstance(t["$value"], dict):
            yield cssname(n) + "-letterSpacing", alias(t["$value"].get("letterSpacing", "normal"))


BLOCKS = {s: list(decls(s)) for s in SETS}
DEFINED = set()
for s in SETS:
    names = [n for n, _ in BLOCKS[s]]
    if len(names) != len(set(names)):
        raise SystemExit(f"build_style_guide: two tokens in {s} map to one CSS name")
    DEFINED.update(names)


def block(setname):
    return "\n".join(f"  {n}: {v};" for n, v in BLOCKS[setname])


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"], "s": node["$extensions"]["source"]}
    return {k: slim(v) for k, v in node.items() if not k.startswith("$")}


payload = {k: slim(T[k]) for k in SETS}
payload["themes"] = [{"id": t["id"], "name": t["name"], "d": t.get("$description", "")} for t in T.get("$themes", [])]
data = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

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


def load_icon(name):
    path = HERE / "icons" / f"{name}.svg"
    if not path.is_file():
        raise SystemExit(f"build_style_guide: the template asks for icons/{name}.svg, which does not exist")
    return ICON_SRC.setdefault(name, path.read_text())


def icon(m):
    name, size = m.group(1), m.group(2)
    src = load_icon(name)
    return clean_svg(src, size or native_size(name, src))


def native_size(name, svg):
    m = re.search(r'viewBox="0 0 ([\d.]+) ', svg)
    return m.group(1) if m else "20"


def icon_gallery(_m):
    roles, order = {}, []
    index = HERE / "icons" / "INDEX.tsv"
    rows = [l.split("\t") for l in index.read_text().splitlines() if l and not l.startswith("#")] if index.is_file() else []
    for r in rows[1:]:
        name = r[0].removesuffix(".svg")
        if (HERE / "icons" / r[0]).is_file():
            role = r[1] if len(r) > 1 and r[1] else "other"
            if role not in roles:
                roles[role] = []
                order.append(role)
            roles[role].append(name)
    listed = {n for v in roles.values() for n in v}
    rest = sorted(p.stem for p in (HERE / "icons").glob("*.svg") if p.stem not in listed)
    if rest:
        roles.setdefault("other", []).extend(rest)
        if "other" not in order:
            order.append("other")
    out = []
    for role in order:
        cells = "".join(f'<figure class="icn">{clean_svg(load_icon(n), native_size(n, load_icon(n)))}<figcaption>{n}</figcaption></figure>'
                        for n in roles[role])
        out.append(f'<h4 class="lbl">{role} ({len(roles[role])})</h4><div class="icons">{cells}</div>')
    return "".join(out)


tpl = (HERE / "tools" / "style-guide.template.html").read_text()
unknown = sorted({n for n in re.findall(r"var\((--[A-Za-z0-9-]+)", tpl) if n not in DEFINED and not n.startswith("--g-")})
if unknown:
    raise SystemExit("build_style_guide: the template reads properties no token defines: " + ", ".join(unknown))
html = (tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", block("dark"))
        .replace("/*TOKENS*/null", data))
html = re.sub(r"<!--icons:all-->", icon_gallery, html)
html = re.sub(r"<!--icon:([a-z0-9-]+)(?::(\d+))?-->", icon, html)
(HERE / "style-guide.html").write_text(html)
print("style-guide.html:", len(html.encode()), "bytes;", " + ".join(f"{len(list(flat(T[s])))} {s}" for s in SETS), "tokens;",
      len(ICON_SRC), "icons")
