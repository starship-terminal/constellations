#!/usr/bin/env python3
"""Render style-guide.html from tokens.json + tools/style-guide.template.html.

Every colour in the page is a CSS custom property generated from tokens.json, so the
guide cannot drift from the token file. Re-run after editing tokens.
"""
import json, pathlib, html
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

def family_key(v):
    return v["fontFamily"].strip("{}").split(".")[1]

def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        return ", ".join(f'{"inset " if s.get("type") == "innerShadow" else ""}{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {s["color"]}' for s in v)
    if isinstance(v, (int, float)) and ty in ("number",):
        return str(v)
    if ty == "typography":
        # Point at the page's font stack (--ff-*), not the bare family, so the public
        # fallbacks apply when Google Sans is not installed.
        return f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} var(--ff-{family_key(v)})'
    if ty == "fontFamily":
        return ", ".join(x if x in ("sans-serif", "serif", "monospace") else f'"{x}"' for x in (v if isinstance(v, list) else [v]))
    return str(v)

core_css = "\n".join(f"  --{n}: {css_val(t)};" for n, t in flat(T["core"]))
light_css = "\n".join(f"  --{n}: {css_val(t)};" for n, t in flat(T["light"]))
dark_css = "\n".join(f"  --{n}: {css_val(t)};" for n, t in flat(T["dark"]))

# swatch tables per group
def swatches(group):
    rows = []
    for n, t in flat(T["light"][group], group + "-"):
        d = dict(flat(T["dark"][group], group + "-"))[n]
        est = t["$extensions"]["source"].startswith("Derived") or d["$extensions"]["source"].startswith("Derived")
        rows.append(
            f'<div class="sw"><div class="chip" style="background:var(--{n})"></div>'
            f'<div class="sw-meta"><code>{n}</code><span>{t["$value"]} / {d["$value"]}</span>'
            f'<small>{html.escape(t.get("$description",""))}{" · <b>derived</b>" if est else ""}</small></div></div>')
    return "\n".join(rows)

def luminance(hexv):
    h = hexv.lstrip("#")
    ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def ink(hexv):
    # whichever label colour has the higher WCAG contrast against the swatch
    return max(("#1b1b1c", "#ffffff"), key=lambda c: contrast(c, hexv))

def palettes():
    return "\n".join(f'<h3>{fam}</h3><div class="ramp">{palette(fam)}</div>' for fam in T["core"]["palette"])

import pathlib as _p
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
def components():
    out, group = [], None
    for key, c in COMP.items():
        if c["group"] != group:
            group = c["group"]
            out.append(f"<h3>{html.escape(group)}</h3>")
        cells = []
        for st in [k for k in c["states"] if not k.startswith("light")]:
            lt = "light" if st == "default" else f"light-{st}"
            d, l = HERE / "components" / "crops" / f"{key}-{st}.png", HERE / "components" / "crops" / f"{key}-{lt}.png"
            if not d.exists():
                continue
            img = f'<img class="only-dark" src="components/crops/{d.name}" alt="{key} {st}, dark">'
            if l.exists():
                img += f'<img class="only-light" src="components/crops/{l.name}" alt="{key} {st}, light">'
            cells.append(f'<figure class="crop">{img}<figcaption>{html.escape(st)}</figcaption></figure>')
        if cells:
            out.append(f'<div class="comp"><h4 id="c-{key}">{html.escape(c["title"])}</h4><div class="row crops">{"".join(cells)}</div></div>')
    return "\n".join(out)

def icons():
    rows = []
    for line in (HERE / "icons" / "INDEX.tsv").read_text().splitlines()[1:]:
        f = line.split("\t")
        rows.append(f'<tr><td><span class="mi">{html.escape(f[0])}</span></td><td><code>{html.escape(f[0])}</code></td><td>{html.escape(f[1])}</td><td>{html.escape(f[2])}</td><td>{html.escape(f[3])}</td><td>{html.escape(f[5])}</td></tr>')
    return '<div class="scroll-x"><table class="spec"><tr><th></th><th>Ligature</th><th>Role</th><th>Where</th><th>Sizes</th><th>Font that drew it</th></tr>' + "".join(rows) + "</table></div>"

def palette(fam):
    return "\n".join(f'<div class="ramp-step" style="background:var(--palette-{fam}-{k});color:{ink(t["$value"])}"><span>{k}</span><span>{t["$value"]}</span></div>'
                     for k, t in T["core"]["palette"][fam].items())

type_rows = "\n".join(
    f'<tr><td><code>{k}</code></td><td style="font:var(--typography-{k});letter-spacing:{t["$value"]["letterSpacing"]};font-variation-settings:{html.escape(t["$extensions"].get("fontVariationSettings") or "normal", quote=True)}">The quick brown fox</td>'
    f'<td>{T["core"]["fontFamily"][family_key(t["$value"])]["$value"]} · {t["$value"]["fontSize"]}/{t["$value"]["lineHeight"]} · {t["$value"]["fontWeight"]} · {t["$value"]["letterSpacing"]}</td>'
    f'<td>{html.escape(t.get("$description",""))}</td></tr>'
    for k, t in T["core"]["typography"].items())

def dim_rows(group):
    return "\n".join(f'<tr><td><code>{group}.{k}</code></td><td>{t["$value"]}</td><td>{html.escape(t.get("$description",""))}</td><td class="src">{html.escape(t["$extensions"]["source"])}</td></tr>'
                     for k, t in T["core"][group].items())

radius_demo = "\n".join(f'<div class="rad" style="border-radius:var(--radius-{k})"><code>{k}</code><span>{t["$value"]}</span></div>' for k, t in T["core"]["radius"].items())
shadow_demo = "\n".join(f'<div class="shd" style="box-shadow:var(--shadow-{k})"><code>{k}</code><small>{html.escape(t.get("$description",""))}</small></div>' for k, t in T["core"]["shadow"].items())
spacing_demo = "\n".join(f'<div class="sp"><div style="width:var(--spacing-{k})"></div><code>{k}</code></div>' for k in T["core"]["spacing"])
motion_rows = "\n".join(f'<tr><td><code>easing.{k}</code></td><td>{css_val(t)}</td><td class="src">{t["$extensions"]["source"]}</td><td><div class="ease-track"><div class="ease-dot" style="transition-timing-function:var(--easing-{k})"></div></div></td></tr>' for k, t in T["core"]["easing"].items())
dur_rows = " · ".join(f'<code>{k}</code> {t["$value"]}' for k, t in T["core"]["duration"].items())

tpl = (HERE / "tools" / "style-guide.template.html").read_text()
for key, val in {
    "CORE_CSS": core_css, "LIGHT_CSS": light_css, "DARK_CSS": dark_css,
    "SW_BG": swatches("bg"), "SW_SURFACE": swatches("surface"), "SW_BORDER": swatches("border"),
    "SW_TEXT": swatches("text"), "SW_ACCENT": swatches("accent"), "SW_STATE": swatches("state"),
    "SW_STATUS": swatches("status"), "SW_TILE": swatches("tile"), "SW_PASTEL": swatches("pastel"),
    "SW_DATAVIZ": swatches("dataviz"), "SW_SKEL": swatches("skeleton"),
    "PALETTES": palettes(), "COMPONENTS": components(), "ICONS": icons(),
    "TYPE_ROWS": type_rows, "RADIUS": radius_demo, "SHADOWS": shadow_demo, "SPACING": spacing_demo,
    "SIZE_ROWS": dim_rows("size"), "BP_ROWS": dim_rows("breakpoint"), "BW_ROWS": dim_rows("borderWidth"),
    "BLUR_ROWS": dim_rows("blur"), "MOTION_ROWS": motion_rows, "DUR_ROWS": dur_rows,
}.items():
    tpl = tpl.replace("{{" + key + "}}", val)
tpl = tpl.replace("</style>", ".crop .only-light{display:none}[data-theme=light] .crop .only-light{display:block}[data-theme=light] .crop .only-dark{display:none}.crops{gap:12px;align-items:flex-end}.crop{margin:0}.crop img{max-width:340px;max-height:200px;display:block;border-radius:6px}.crop figcaption{font:12px/16px var(--ff-text);color:var(--text-secondary);margin-top:4px}.comp h4{margin:18px 0 6px;font:500 15px/20px var(--ff-text);color:var(--text-title)}\n</style>", 1)
(HERE / "style-guide.html").write_text(tpl)
print("wrote style-guide.html", len(tpl), "bytes")
