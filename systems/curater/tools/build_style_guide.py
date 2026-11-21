#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


rows = []
for path, token in walk(T["light"]):
    if token.get("$type") != "color":
        continue
    value = token["$value"]
    if not isinstance(value, str) or value == "Not captured":
        continue
    rows.append((path, value))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{v}"></i><div><b>{p}</b><span>{v}</span></div></div>'
    for p, v in rows
)
brand = "\n".join(
    f'<div class="sw"><i style="background:{v["$value"]}"></i><div><b>{k}</b><span>{v["$value"]}</span></div></div>'
    for k, v in T["core"]["color"].items()
    if isinstance(v.get("$value"), str) and v["$value"].startswith(("#", "oklch", "rgb"))
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curater style guide</title>
<style>
  :root {{
    --page: {T["light"]["page"]["$value"]};
    --text: {T["light"]["text"]["primary"]["$value"]};
    --muted: {T["light"]["text"]["secondary"]["$value"]};
    --border: {T["light"]["border"]["default"]["$value"]};
    --sans: {T["core"]["fontFamily"]["sans"]["$value"]};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.5 var(--sans); }}
  main {{ max-width: 980px; margin: 0 auto; padding: 40px 24px 80px; }}
  h1 {{ font-size: 32px; line-height: 1.2; margin: 0 0 8px; }}
  h2 {{ font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 40px 0 12px; }}
  p {{ max-width: 68ch; color: var(--muted); }}
  .grid {{ display: flex; flex-wrap: wrap; gap: 10px; }}
  .sw {{ display: flex; gap: 8px; align-items: center; min-width: 220px; }}
  .sw i {{ width: 28px; height: 28px; border-radius: 8px; border: 1px solid var(--border); display: block; }}
  .sw b {{ display: block; font-size: 12px; font-weight: 500; }}
  .sw span {{ display: block; font-size: 11px; color: var(--muted); }}
  .pill {{ display: inline-flex; align-items: center; gap: 8px; height: 58px; padding: 0 24px; border: 1px solid {T["light"]["component"]["button"]["border"]["$value"]}; border-radius: 9999px; background: #fff; color: {T["light"]["component"]["button"]["text"]["$value"]}; font-weight: 500; }}
  .fill {{ display: inline-flex; align-items: center; justify-content: center; height: 52px; min-width: 240px; padding: 0 24px; border-radius: 9999px; background: {T["light"]["accent"]["default"]["$value"]}; color: {T["light"]["text"]["onAccent"]["$value"]}; font-weight: 500; }}
  .menu {{ width: 180px; background: #fff; border: 1px solid {T["light"]["border"]["default"]["$value"]}; border-radius: 12px; padding: 4px; }}
  .menu div {{ padding: 10px 12px; font-size: 14px; color: var(--muted); }}
  .note {{ font-size: 13px; }}
</style>
</head>
<body>
<main>
  <h1>Curater</h1>
  <p>Public signed-out surface, captured 2026-11-21 from curater.org. One light theme. Values come from tokens.json.</p>
  <h2>Roles</h2>
  <div class="grid">{swatches}</div>
  <h2>Brand</h2>
  <div class="grid">{brand}</div>
  <h2>Controls</h2>
  <p class="pill">Sign in or create account</p>
  <p><span class="fill">Search</span></p>
  <div class="menu"><div>Settings</div><div>Extension</div><div>Privacy</div><div>Terms</div><div>About</div><div>Sign in</div></div>
  <p class="note">The pill is the signed-out Google action. The filled pill is the phone search submit. The menu is the settings menu. Hover, pressed, disabled, and dark theme were not captured as separate painted states.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
