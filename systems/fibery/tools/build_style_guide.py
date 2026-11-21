#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: the public site had no dark theme."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from flat(value, path)


def resolve(value, seen=None):
    seen = seen or set()
    text = str(value)
    if text in seen:
        return text
    match = re.fullmatch(r"\{([^{}]+)\}", text)
    if not match:
        return text
    seen.add(text)
    node = T
    for part in match.group(1).split("."):
        node = node[part]
    return resolve(node["$value"], seen)


rows = []
for path, token in list(flat(T["core"])) + list(flat(T["light"])):
    if token.get("$type") != "color":
        continue
    rows.append((path, resolve(token["$value"])))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{value}"></i><div><code>{path}</code><span>{value}</span></div></div>'
    for path, value in rows
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fibery style guide</title>
<style>
  :root {{
    --page: {resolve(T["light"]["background"]["page"]["$value"])};
    --surface: {resolve(T["light"]["background"]["surface"]["$value"])};
    --ink: {resolve(T["light"]["text"]["primary"]["$value"])};
    --accent: {resolve(T["light"]["accent"]["default"]["$value"])};
    --font: {resolve(T["core"]["font"]["family"]["sans"]["$value"])};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--ink); font: 16px/1.4 var(--font), sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 20px 64px; }}
  h1 {{ font-size: 40px; line-height: 1; font-weight: 800; margin: 0 0 8px; }}
  p {{ max-width: 68ch; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; background: var(--surface); padding: 8px; border-radius: 6px; }}
  .sw i {{ width: 44px; height: 44px; border-radius: 6px; display: block; box-shadow: inset 0 0 0 1px rgba(37,29,26,.15); }}
  code {{ font-size: 12px; display: block; }}
  span {{ font-size: 12px; opacity: .7; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
  button, .quiet {{
    height: 40px; padding: 0 16px; border-radius: 6px; border: 0; font: 600 16px/40px var(--font), sans-serif;
  }}
  button.primary {{ background: {resolve(T["light"]["background"]["action"]["$value"])}; color: {resolve(T["light"]["text"]["on-action"]["$value"])}; }}
  .quiet {{ background: {resolve(T["light"]["background"]["quiet"]["$value"])}; color: var(--ink); display: inline-flex; align-items: center; }}
  .pill {{ height: 34px; padding: 6px 12px; border-radius: 48px; background: {resolve(T["light"]["background"]["pill"]["$value"])}; color: #000; font-size: 13px; }}
</style>
</head>
<body>
<main>
  <h1>Fibery</h1>
  <p>Public marketing site, light only. Values are the custom properties and computed styles read on 2026-11-21. Suisse Intl is not loaded here, so the page falls back to the system sans.</p>
  <h2>Colour</h2>
  <div class="swatches">{swatches}</div>
  <h2>Controls</h2>
  <div class="row">
    <button class="primary">Sign up for free</button>
    <span class="quiet">Log in</span>
    <span class="pill">Startup</span>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
