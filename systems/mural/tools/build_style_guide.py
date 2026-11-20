#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: Mural's public pages
ship one theme. Specimens use the token values, with Arial and Times New Roman
standing in for the proprietary ABC Social and STK Bureau faces.
"""
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def resolve(path, seen=None):
    seen = seen or set()
    if path in seen:
        return None
    parts = path.split(".")
    node = T
    for p in parts:
        if not isinstance(node, dict) or p not in node:
            return None
        node = node[p]
    if not isinstance(node, dict) or "$value" not in node:
        return None
    value = node["$value"]
    if isinstance(value, str):
        m = re.fullmatch(r"\{([^{}]+)\}", value.strip())
        if m:
            return resolve(parts[0] + "." + m.group(1) if "." not in m.group(1) else m.group(1), seen | {path}) or resolve("core." + m.group(1), seen | {path})
    return value


def css_color(value):
    if isinstance(value, str) and value.startswith("{") :
        got = resolve("light." + value.strip("{}")) or resolve("core." + value.strip("{}"))
        return got or "#000"
    return value


def swatch(name, token):
    value = css_color(token["$value"])
    return f'<div class="sw"><i style="background:{html.escape(value)}"></i><div><b>{html.escape(name)}</b><code>{html.escape(value)}</code></div></div>'


colors = []
for name, token in flat(T["core"]["color"]):
    if token["$type"] == "color":
        colors.append(swatch(name, token))

roles = []
for name in ("page", "pageInverse", "surface", "surfaceMuted", "text", "textBody", "textInverse", "textMuted", "accent", "border", "borderHover", "focus", "danger"):
    roles.append(swatch(name, T["light"][name]))

type_rows = []
for name, token in T["core"]["typography"].items():
    v = token["$value"]
    family = "Times New Roman, serif" if "STK" in v["fontFamily"] else "Arial, sans-serif"
    sample = "Sync up. Speed up." if "display" in name or "Title" in name or "title" in name else "The visual workspace for a team."
    # Escaped, so a value holding a quote cannot close the style attribute.
    style = html.escape(f"font-family:{family};font-size:{v['fontSize']};font-weight:{v['fontWeight']};line-height:{v['lineHeight']};letter-spacing:{v['letterSpacing']}", quote=True)
    type_rows.append(
        f'<div class="ty"><div><b>{html.escape(name)}</b><code>{html.escape(v["fontSize"])} / {html.escape(v["lineHeight"])} {v["fontWeight"]}</code></div>'
        f'<p style="{style}">{html.escape(sample)}</p></div>'
    )

space_rows = []
for name, token in T["core"]["spacing"].items():
    space_rows.append(f'<div class="sp"><i style="width:{token["$value"]}"></i><code>{html.escape(name)} {html.escape(token["$value"])}</code></div>')

radius_rows = []
for name, token in T["core"]["radius"].items():
    radius_rows.append(f'<div class="rd" style="border-radius:{token["$value"]}"><code>{html.escape(name)} {html.escape(token["$value"])}</code></div>')

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mural style guide</title>
<style>
:root {{ color-scheme: light; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #fff; color: #000; font: 400 16px/24px Arial, sans-serif; }}
header {{ padding: 24px 32px; border-bottom: 1px solid #dce1e5; display: flex; justify-content: space-between; align-items: baseline; }}
h1 {{ margin: 0; font: 300 32px/1.1 "Times New Roman", serif; letter-spacing: -0.8px; }}
header p {{ margin: 0; color: #828c92; font-size: 14px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px; }}
h2 {{ font: 300 28px/1.2 "Times New Roman", serif; margin: 40px 0 12px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 44px; height: 44px; border-radius: 8px; box-shadow: inset 0 0 0 1px #dce1e5; display: block; }}
.sw b, .ty b {{ display: block; font-size: 13px; }}
code {{ font: 12px/1.4 ui-monospace, Menlo, monospace; color: #4f5457; }}
.ty {{ display: grid; grid-template-columns: 180px 1fr; gap: 16px; align-items: baseline; border-bottom: 1px solid #dce1e5; padding: 10px 0; }}
.ty p {{ margin: 0; }}
.sp {{ display: flex; align-items: center; gap: 12px; margin: 6px 0; }}
.sp i {{ height: 12px; background: #00c27a; display: block; }}
.radii {{ display: flex; gap: 16px; flex-wrap: wrap; }}
.rd {{ width: 96px; height: 64px; border: 2px solid #dce1e5; display: flex; align-items: end; padding: 6px; }}
.spec {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; background: #000; padding: 24px; border-radius: 16px; }}
.spec.light {{ background: #f9fafa; }}
.btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 8px; font: 500 16px/24px Arial, sans-serif; text-decoration: none; }}
.btn.jade {{ background: #00c27a; color: #000; }}
.btn.outline {{ background: transparent; color: #000; border: 2px solid #dce1e5; }}
.btn.dark {{ background: #000; color: #fff; }}
.btn.red {{ background: #e02935; color: #fff; font-weight: 700; font-size: 14px; }}
.field {{ height: 40px; border-radius: 8px; border: 2px solid #282e34; padding: 8px 10px; font: 400 14px/20px Arial, sans-serif; width: 280px; }}
.nav {{ height: 64px; background: #fff; border-radius: 16px; box-shadow: 0 0 1px rgba(11,41,70,.32), 0 24px 20px rgba(42,82,121,.08); display: flex; align-items: center; gap: 16px; padding: 0 16px; }}
.card {{ background: #fff; border-radius: 20px; padding: 32px 24px; width: 240px; border: 3px solid #fff; }}
.card b {{ font: 300 28px/1 "Times New Roman", serif; }}
.note {{ color: #4f5457; font-size: 14px; max-width: 70ch; }}
</style>
</head>
<body>
<header>
  <h1>Mural</h1>
  <p>Public site and signed-out login. Light only. Measured 2026-11-19.</p>
</header>
<main>
  <h2>Roles</h2>
  <div class="grid">{''.join(roles)}</div>
  <h2>Palette</h2>
  <div class="grid">{''.join(colors)}</div>
  <h2>Type</h2>
  <p class="note">STK Bureau and ABC Social are proprietary. These specimens use Times New Roman and Arial, the fallbacks named in the stylesheets.</p>
  {''.join(type_rows)}
  <h2>Spacing</h2>
  {''.join(space_rows)}
  <h2>Radius</h2>
  <div class="radii">{''.join(radius_rows)}</div>
  <h2>Controls</h2>
  <p class="note">Drawn from the token values. The marketing hero sits on black. The auth form sits on the measured page grey.</p>
  <div class="nav" style="margin-bottom:16px"><b>Mural</b><span>Product</span><span>Pricing</span><span style="margin-left:auto">Login</span><a class="btn outline" href="#demo">Book a demo</a><a class="btn dark" href="#signup">Sign up free</a></div>
  <div class="spec">
    <input class="field" style="background:#000;color:#fff;border-color:#4f5457" placeholder="Enter your email" aria-label="Email">
    <a class="btn jade" href="#start">Get started free</a>
  </div>
  <div class="spec light" style="margin-top:16px">
    <input class="field" placeholder="Enter your work email" aria-label="Work email">
    <a class="btn red" href="#login">Log in</a>
  </div>
  <div class="card" style="margin-top:16px"><b>Business</b><p>$17.99</p><p class="note">Pricing card, 20px radius, 32px 24px padding.</p></div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote style-guide.html", len(page))
