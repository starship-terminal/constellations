#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only. Deterministic."""
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
            yield from flat(v, prefix + k + ".")


def cssname(path):
    return "--" + path.replace(".", "-")


names = {}
for set_name in ("core", "light"):
    for path, tok in flat(T[set_name]):
        names[path] = tok

def resolve(val, seen=None):
    seen = seen or set()
    if not isinstance(val, str) or not val.startswith("{"):
        return val
    key = val.strip("{}")
    if key in seen:
        return val
    seen.add(key)
    return resolve(names[key]["$value"], seen)


rows = []
for path, tok in flat(T["core"]):
    if tok["$type"] == "color":
        rows.append(f'<div class="sw"><i style="background:{resolve(tok["$value"])}"></i><span>{path}<br><code>{resolve(tok["$value"])}</code></span></div>')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Dopper style guide</title>
<style>
body {{ margin: 0; font: 400 16px/1.4 Gilroy, system-ui, sans-serif; background: #fcfaf2; color: #000f2e; }}
main {{ max-width: 960px; margin: 0 auto; padding: 40px 24px 80px; }}
h1 {{ font: 400 48px/1 Georgia, serif; margin: 0 0 8px; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ display: flex; gap: 8px; align-items: center; min-width: 220px; }}
.sw i {{ width: 36px; height: 36px; border-radius: 50%; border: 1px solid #000f2e22; display: block; }}
.btn {{ display: inline-block; background: #0067e5; color: #f9f3df; border-radius: 20px; padding: 13px 25px; font-weight: 600; }}
.ink {{ display: inline-block; background: #000; color: #f6ecc8; border-radius: 999px; padding: 12px 20px; }}
.ghost {{ display: inline-block; color: #f6ecc8; border: 1px solid #f6ecc8; border-radius: 999px; padding: 12px 20px; }}
.hero {{ background: #0067e5; color: #f6ecc8; padding: 32px; border-radius: 16px; margin: 24px 0; }}
</style>
</head>
<body>
<main>
<h1>Dopper</h1>
<p>Measured from dopper.com and shop.dopper.com on 2026-11-21. Light only. Take values from tokens.json.</p>
<div class="hero">
  <p style="font:400 48px/1 Georgia,serif;margin:0 0 16px">Whatever the season</p>
  <span class="ink">Shop our collection</span>
  <span class="ghost">Watch now</span>
</div>
<p><span class="btn">Add to cart</span></p>
<h2>Colours</h2>
<div class="swatches">
{''.join(rows)}
</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
