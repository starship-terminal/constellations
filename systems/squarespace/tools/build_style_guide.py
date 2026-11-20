#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only. Deterministic."""
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + "-")


def resolve(value, seen=None):
    seen = seen or set()
    if not isinstance(value, str):
        return value

    def repl(match):
        path = match.group(1)
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
        return "cubic-bezier(%s)" % ", ".join(str(item) for item in value)
    if typ == "typography":
        return {key: resolve(item) if isinstance(item, str) else item for key, item in value.items()}
    return value


rows_color = [(name, css(tok["$value"], tok["$type"])) for name, tok in flat(T["light"]["color"])]
type_rows = [(name, css(tok["$value"], "typography")) for name, tok in flat(T["core"]["typography"])]
radius_rows = [(name, css(tok["$value"], tok["$type"])) for name, tok in flat(T["core"]["radius"])]
space_rows = [(name, css(tok["$value"], tok["$type"])) for name, tok in flat(T["core"]["space"])]


def swatch(name, value):
    return (
        f'<div class="sw"><i style="background:{value}"></i>'
        f"<div><b>{name}</b><span>{value}</span></div></div>"
    )


def specimen_style(value):
    """The specimen's style attribute, escaped: a quoted family would otherwise close it."""
    css = ";".join(f"{prop}:{value[key]}" for prop, key in (
        ("font-family", "fontFamily"), ("font-size", "fontSize"), ("font-weight", "fontWeight"),
        ("line-height", "lineHeight"), ("letter-spacing", "letterSpacing")))
    return html.escape(css, quote=True)


color_html = "\n".join(swatch(name, value) for name, value in rows_color)
type_html = "\n".join(
    f'<div class="ty"><div class="k">{name}<small>{value["fontSize"]} / {value["lineHeight"]} · {value["fontWeight"]}</small></div>'
    f'<div style="{specimen_style(value)}">A website makes it real</div></div>'
    for name, value in type_rows
)
radius_html = "\n".join(
    f'<div class="sw"><i style="background:#000000;border-radius:{value}"></i><div><b>{name}</b><span>{value}</span></div></div>'
    for name, value in radius_rows
)
space_html = "\n".join(
    f'<div class="sp"><i style="width:{value}"></i><span>{name} · {value}</span></div>'
    for name, value in space_rows
)

page = css(T["light"]["color"]["page"]["$value"], "color")
ink = css(T["light"]["color"]["ink"]["$value"], "color")
muted = css(T["light"]["color"]["muted"]["$value"], "color")
accent = css(T["light"]["color"]["accent"]["$value"], "color")
line = css(T["light"]["color"]["line"]["$value"], "color")
sans = css(T["core"]["font"]["family"]["clarkson"]["$value"], "fontFamily")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Squarespace style guide</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: {page}; color: {ink}; font: 400 15px/21px {sans}; }}
  header, main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px; }}
  h1 {{ font-weight: 300; font-size: 56px; line-height: 60px; letter-spacing: -2.24px; margin: 0 0 8px; }}
  h2 {{ font-size: 20px; font-weight: 500; margin: 36px 0 12px; }}
  p.lead {{ color: {muted}; max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
  .sw i {{ width: 44px; height: 44px; border-radius: 4px; box-shadow: inset 0 0 0 1px {line}; display: block; }}
  .sw b, .ty .k {{ display: block; font-size: 12px; }}
  .sw span, .ty small {{ color: {muted}; font-size: 12px; font-weight: 400; }}
  .ty {{ display: grid; grid-template-columns: 200px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid {line}; align-items: baseline; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 6px 0; }}
  .sp i {{ height: 12px; background: {accent}; display: block; }}
  .btn {{ display: inline-flex; align-items: center; justify-content: center; height: 60px; padding: 23px 28px; border-radius: 4px; background: #000; color: #fff; font: 500 14px/14px {sans}; letter-spacing: 0; text-transform: uppercase; border: 0; }}
  .btn-inv {{ display: inline-flex; align-items: center; justify-content: center; height: 60px; padding: 23px 28px; border-radius: 4px; background: #fff; color: #000; font: 500 14px/14px {sans}; text-transform: uppercase; border: 0; box-shadow: inset 0 0 0 1px {line}; }}
  .login {{ display: inline-flex; align-items: center; justify-content: center; height: 44px; width: 327px; background: #f2f2f2; color: #b7b7b7; font: 500 12px/22px {sans}; letter-spacing: 0.5px; text-transform: uppercase; border: 0; }}
  .oauth {{ display: flex; align-items: center; height: 55px; width: 327px; padding: 0 22px; border: 1px solid #000; background: transparent; color: #000; font: 500 14px/22px {sans}; }}
  .field {{ width: 327px; border-bottom: 1px solid {line}; padding: 11px 0; color: {muted}; font: 500 9.75px/16px {sans}; letter-spacing: 0.75px; text-transform: uppercase; }}
  .field b {{ display: block; margin-top: 8px; color: #0e0e0e; font: 400 14px/22px {sans}; letter-spacing: 0; text-transform: none; }}
  .row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
  .stack {{ display: grid; gap: 12px; justify-items: start; }}
</style>
</head>
<body>
<header>
  <h1>Squarespace</h1>
  <p class="lead">Public marketing and signed-out login chrome, measured 2026-11-19. Clarkson is not bundled, so specimens fall back to Helvetica.</p>
</header>
<main>
  <h2>Colour</h2>
  <div class="grid">{color_html}</div>
  <h2>Type</h2>
  {type_html}
  <h2>Radius</h2>
  <div class="grid">{radius_html}</div>
  <h2>Space</h2>
  {space_html}
  <h2>Controls</h2>
  <div class="stack">
    <div class="row"><span class="btn">Get started</span><span class="btn-inv">Get started</span></div>
    <div class="field">Email address<b>name@example.com</b></div>
    <span class="login">Log in</span>
    <span class="oauth">Continue with Google</span>
  </div>
</main>
</body>
</html>
"""

(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
