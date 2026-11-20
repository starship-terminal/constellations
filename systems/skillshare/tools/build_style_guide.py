#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only. Deterministic."""
import html
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


def resolve(value, seen=None):
    seen = seen or set()
    if not isinstance(value, str):
        return value
    def repl(m):
        path = m.group(1)
        if path in seen:
            return path
        node = T["core"]
        for part in path.split("."):
            node = node[part]
        return str(resolve(node["$value"], seen | {path}))
    return re.sub(r"\{([^{}]+)\}", repl, value)


def css(value, typ):
    value = resolve(value)
    if typ == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in value)
    if typ == "typography":
        v = {k: resolve(val) if isinstance(val, str) else val for k, val in value.items()}
        return v
    return value


rows_color = []
for name, tok in flat(T["light"]["color"]):
    rows_color.append((name, css(tok["$value"], tok["$type"])))

type_rows = []
for name, tok in flat(T["core"]["typography"]):
    type_rows.append((name, css(tok["$value"], "typography")))

radius_rows = [(n, css(t["$value"], t["$type"])) for n, t in flat(T["core"]["radius"])]
space_rows = [(n, css(t["$value"], t["$type"])) for n, t in flat(T["core"]["space"])]

def swatch(name, value):
    return f'<div class="sw"><i style="background:{value}"></i><div><b>{name}</b><span>{value}</span></div></div>'

def specimen_style(v):
    """The specimen's style attribute, escaped: the quoted family would otherwise close it."""
    css = ";".join(f"{prop}:{v[key]}" for prop, key in (
        ("font-family", "fontFamily"), ("font-size", "fontSize"), ("font-weight", "fontWeight"),
        ("line-height", "lineHeight")))
    return html.escape(css, quote=True)


color_html = "\n".join(swatch(n, v) for n, v in rows_color)
type_html = "\n".join(
    f'<div class="ty"><div class="k">{n}<small>{v["fontSize"]} / {v["lineHeight"]} · {v["fontWeight"]}</small></div>'
    f'<div style="{specimen_style(v)}">Creative classes</div></div>'
    for n, v in type_rows
)
radius_html = "\n".join(
    f'<div class="sw"><i style="background:#55da9b;border-radius:{v}"></i><div><b>{n}</b><span>{v}</span></div></div>'
    for n, v in radius_rows
)
space_html = "\n".join(
    f'<div class="sp"><i style="width:{v}"></i><span>{n} · {v}</span></div>' for n, v in space_rows
)

page = css(T["light"]["color"]["page"]["$value"], "color")
ink = css(T["light"]["color"]["ink-soft"]["$value"], "color")
muted = css(T["light"]["color"]["muted"]["$value"], "color")
accent = css(T["light"]["color"]["accent"]["$value"], "color")
link = css(T["light"]["color"]["link"]["$value"], "color")
border = css(T["light"]["color"]["border"]["$value"], "color")
sans = css(T["core"]["font"]["family"]["sans"]["$value"], "fontFamily")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skillshare style guide</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: {page}; color: {ink}; font: 400 15px/22px {sans}; }}
  header, main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px; }}
  h1 {{ font-size: 36px; line-height: 43px; margin: 0 0 8px; }}
  h2 {{ font-size: 22px; margin: 36px 0 12px; }}
  p.lead {{ color: {muted}; max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
  .sw i {{ width: 44px; height: 44px; border-radius: 4px; box-shadow: inset 0 0 0 1px {border}; display: block; }}
  .sw b, .ty .k {{ display: block; font-size: 12px; }}
  .sw span, .ty small {{ color: {muted}; font-size: 12px; font-weight: 400; }}
  .ty {{ display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid {border}; align-items: baseline; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 6px 0; }}
  .sp i {{ height: 12px; background: {accent}; display: block; }}
  .btn {{ display: inline-flex; align-items: center; justify-content: center; height: 40px; padding: 0 20px; border-radius: 4px; background: {accent}; color: {ink}; font-weight: 700; border: 1px solid {accent}; }}
  .oauth {{ display: inline-flex; align-items: center; justify-content: center; height: 40px; width: 240px; border-radius: 4px; background: #fff; color: {ink}; font-weight: 700; border: 1px solid {muted}; }}
  .textbtn {{ color: {link}; font-weight: 700; background: transparent; border: 0; height: 40px; }}
  .row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
  code {{ font-size: 12px; }}
</style>
</head>
<body>
<header>
  <h1>Skillshare</h1>
  <p class="lead">Public signed-out surfaces, measured 2026-11-19. Light only. GT Walsheim Pro is proprietary and falls back to the system sans here. Values come from tokens.json.</p>
</header>
<main>
  <h2>Colour</h2>
  <div class="grid">
    {color_html}
  </div>
  <h2>Type</h2>
  {type_html}
  <h2>Radius</h2>
  <div class="grid">{radius_html}</div>
  <h2>Space</h2>
  {space_html}
  <h2>Controls</h2>
  <div class="row">
    <span class="btn">Sign Up</span>
    <span class="oauth">Continue with Google</span>
    <span class="textbtn">Continue with email</span>
  </div>
  <p class="lead">Sign Up hover fills #50cf93. Google hover fills rgba(11, 18, 21, 0.04). Email hover underlines and fills rgba(85, 218, 155, 0.04). Focus outline is #5620c1.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
