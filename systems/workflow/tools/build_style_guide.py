#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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


def resolve(value, seen=None):
    seen = seen or set()
    if not isinstance(value, str):
        return value
    def repl(m):
        path = m.group(1)
        if path in seen:
            return m.group(0)
        for tree in (T["core"], T["light"]):
            node = tree
            ok = True
            for part in path.split("."):
                if isinstance(node, dict) and part in node:
                    node = node[part]
                else:
                    ok = False
                    break
            if ok and isinstance(node, dict) and "$value" in node:
                return str(resolve(node["$value"], seen | {path}))
        return m.group(0)
    return re.sub(r"\{([^{}]+)\}", repl, value)


rows = []
for set_name in ("core", "light"):
    for path, tok in flat(T[set_name]):
        if tok.get("$type") != "color":
            continue
        val = resolve(tok["$value"])
        rows.append((set_name + "." + path, val))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{html.escape(val)}"></i><div><div class="nm">{html.escape(name)}</div><div class="vl">{html.escape(str(val))}</div></div></div>'
    for name, val in rows
)

type_rows = []
for path, tok in flat(T["core"]):
    if tok.get("$type") != "typography":
        continue
    v = tok["$value"]
    family = resolve(v.get("fontFamily", "Inter, Arial, sans-serif"))
    sample = f'<div class="sample" style="font-family:{html.escape(family)};font-size:{html.escape(str(v.get("fontSize","")))};font-weight:{html.escape(str(v.get("fontWeight","")))};line-height:{html.escape(str(v.get("lineHeight","")))}">Design feedback, all in one place</div>'
    type_rows.append(f'<div class="typerow"><div class="k">{html.escape(path)}</div>{sample}</div>')

space_rows = []
for path, tok in flat(T["core"]):
    if not path.startswith("space.") or tok.get("$type") != "dimension":
        continue
    space_rows.append(
        f'<div class="space"><span>{html.escape(path)} {html.escape(str(tok["$value"]))}</span><i style="width:{html.escape(str(tok["$value"]))}"></i></div>'
    )

page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Workflow style guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@300;400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body { margin: 0; background: #f6f4f0; color: #1a1a1a; font: 400 14px/21px Inter, Arial, sans-serif; }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }
  h1 { font: 300 32px/32px "Crimson Pro", "Times New Roman", serif; margin: 0 0 8px; }
  h2 { font: 300 24px/28px "Crimson Pro", "Times New Roman", serif; margin: 40px 0 12px; }
  p { max-width: 68ch; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px; }
  .sw { display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; background: #fff; border-radius: 8px; padding: 8px; }
  .sw i { display: block; width: 40px; height: 40px; border-radius: 4px; box-shadow: inset 0 0 0 1px #1a1a1a1f; }
  .nm { font-size: 12px; }
  .vl { font-size: 12px; color: #1a1a1aa6; }
  .typerow { display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 12px 0; border-bottom: 1px solid #1a1a1a1f; }
  .k { font-size: 12px; }
  .space { display: flex; align-items: center; gap: 12px; margin: 6px 0; }
  .space i { display: block; height: 12px; background: #1a1a1a; }
  button.demo { height: 40px; padding: 8px 16px; border: 0; border-radius: 8px; background: #f6f6f6; color: #1a1a1a; font: 400 14px/21px Inter, Arial, sans-serif; }
  button.demo:hover { background: #ececec; }
  a.nav { color: #1a1a1a; text-decoration: none; }
  a.nav:hover { color: #353532; }
  .note { color: #1a1a1aa6; font-size: 13px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Workflow</h1>
  <p class="note">Public marketing tokens from www.workflow.design, 2026-11-21. One light theme. Values come from tokens.json.</p>
  <h2>Colour</h2>
  <div class="grid">
""" + swatches + """
  </div>
  <h2>Type</h2>
""" + "\n".join(type_rows) + """
  <h2>Space</h2>
""" + "\n".join(space_rows) + """
  <h2>Controls</h2>
  <p><button class="demo">Try now</button></p>
  <p><a class="nav" href="#colour">Features</a></p>
  <p class="note">The button matches the measured Try now control: 40px tall, 8px radius, #f6f6f6 fill, #ececec on hover. No dark theme toggle: the site does not publish one.</p>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("style-guide.html", len(page))
