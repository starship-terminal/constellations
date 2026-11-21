#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light theme only."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())


def resolve(value, seen=()):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        path = value[1:-1].split(".")
        node = tokens
        for part in path:
            node = node[part]
        if path in seen:
            raise SystemExit("alias cycle " + value)
        return resolve(node["$value"], seen + (tuple(path),))
    return value


def css(value):
    value = resolve(value)
    if isinstance(value, dict) and "fontFamily" in value:
        return value
    return value


rows = []
for group, node in tokens["light"].items():
    for name, leaf in node.items():
        rows.append((f"light.{group}.{name}", css(leaf["$value"])))

swatches = "\n".join(
    f'<div class="swatch"><i style="background:{val}"></i><code>{name}</code><span>{val}</span></div>'
    for name, val in rows
)
type_rows = []
for name, leaf in tokens["core"]["typography"].items():
    v = leaf["$value"]
    type_rows.append(
        f'<p class="t" style="font-size:{v["fontSize"]};font-weight:{v["fontWeight"]};line-height:{v["lineHeight"]}">{name} {v["fontSize"]} / {v["lineHeight"]}</p>'
    )

html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<title>Pixso style guide</title>
<style>
  :root {{
    --page: {css(tokens["light"]["background"]["page"]["$value"])};
    --text: {css(tokens["light"]["text"]["primary"]["$value"])};
    --muted: {css(tokens["light"]["text"]["muted"]["$value"])};
    --button: {css(tokens["light"]["background"]["button"]["$value"])};
    --on-button: {css(tokens["light"]["text"]["onButton"]["$value"])};
    --brand: {css(tokens["light"]["background"]["brand"]["$value"])};
    --field: {css(tokens["light"]["background"]["surface"]["$value"])};
    --border: {css(tokens["light"]["border"]["default"]["$value"])};
    --font: Figtree, Arial, "Helvetica Neue", sans-serif;
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 16px/24px var(--font); }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px; }}
  h1 {{ font-size: 40px; line-height: 46px; font-weight: 600; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .swatch {{ border: 1px solid var(--border); border-radius: 8px; padding: 10px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; border: 1px solid var(--border); }}
  code {{ display: block; margin-top: 8px; font-size: 12px; }}
  .btn {{ display: inline-block; background: var(--button); color: var(--on-button); border-radius: 7px; padding: 6px 15px; font-size: 14px; font-weight: 600; text-decoration: none; }}
  .brand {{ display: inline-block; background: var(--brand); color: white; border-radius: 7px; padding: 6px 15px; margin-left: 8px; }}
  input {{ background: var(--field); border: 1px solid rgba(0,0,0,.1); border-radius: 6px; height: 40px; padding: 0 16px; font: 14px var(--font); }}
  .note {{ color: var(--muted); }}
</style>
</head>
<body>
<main>
  <h1>Pixso public site</h1>
  <p class="note">Rendered from tokens.json. One light theme. Values were read from pixso.net CSS on 2026-11-21.</p>
  <p><a class="btn" href="#">Get started</a><span class="brand">Brand</span></p>
  <p><input placeholder="Enter your name" readonly></p>
  {''.join(type_rows)}
  <h2>Light roles</h2>
  <div class="swatches">{swatches}</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
