#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Reflect ships one dark marketing theme."""
import json
import pathlib

ADAPTED_FOR = "reflect"
HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def color_rows(node, prefix=""):
    rows = []
    for key, value in node.items():
        path = f"{prefix}{key}"
        if isinstance(value, dict) and "$value" in value and value.get("$type") == "color":
            rows.append((path, value["$value"]))
        elif isinstance(value, dict) and "$value" not in value:
            rows.extend(color_rows(value, path + "."))
    return rows


colors = color_rows(T["light"]["color"])
swatches = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><code>{path}</code><span>{value}</span></div>'
    for path, value in colors
)
type_rows = []
for name, token in T["core"]["typography"].items():
    v = token["$value"]
    type_rows.append(
        f'<p style="font-family:{v["fontFamily"]};font-size:{v["fontSize"]};font-weight:{v["fontWeight"]};line-height:{v["lineHeight"]};margin:12px 0">{name}: Think better with Reflect</p>'
    )

page = T["light"]["color"]["bg"]["page"]["$value"]
text = T["light"]["color"]["text"]["primary"]["$value"]
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Reflect style guide</title>
<style>
  body {{ margin: 0; background: {page}; color: {text}; font: 16px/1.5 "Inter V", system-ui, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-weight: 500; letter-spacing: 0; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .swatch {{ display: flex; gap: 10px; align-items: center; }}
  .swatch i {{ width: 36px; height: 36px; border-radius: 8px; border: 1px solid rgba(255,255,255,.15); display: block; }}
  code {{ color: #efedfd; }}
  .note {{ color: rgba(239,237,253,.6); }}
</style>
</head>
<body>
<main>
  <h1>Reflect</h1>
  <p class="note">Public marketing theme only. One painted theme. AeonikPro and Inter V are not loaded here, so type falls back.</p>
  <h2>Colour</h2>
  <div class="swatches">{swatches}</div>
  <h2>Type</h2>
  {''.join(type_rows)}
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
