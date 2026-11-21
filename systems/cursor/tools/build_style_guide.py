#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Adapted for the Cursor public site."""
import json
import pathlib

ADAPTED_FOR = "cursor"
HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())

def val(token):
    if isinstance(token, dict) and "$value" in token:
        return token["$value"]
    return token

core = TOKENS["core"]["color"]
swatches = [
    ("Page", val(core["page"]["$value"]) if False else core["page"]["$value"]),
]
# tokens use $value
rows = []
for name, token in core.items():
    rows.append((name, token["$value"]))

dark = TOKENS["dark"]["color"]
roles = []
for group, items in dark.items():
    for name, token in items.items():
        roles.append((f"{group}.{name}", token["$value"]))

def chip(name, value):
    paint = value if str(value).startswith("#") else "#888"
    return f'<div class="chip"><i style="background:{paint}"></i><span>{name}</span><code>{value}</code></div>'

html = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<title>Cursor public tokens</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin: 0; background: #14120b; color: #edecec; font: 16px/1.5 ui-sans-serif, system-ui, sans-serif; padding: 32px; }}
  h1 {{ font-weight: 400; font-size: 26px; margin: 0 0 8px; }}
  p {{ color: #d7d6d5; max-width: 42rem; }}
  h2 {{ font-weight: 400; font-size: 16px; margin: 32px 0 12px; }}
  .row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .chip {{ width: 140px; }}
  .chip i {{ display: block; height: 48px; border-radius: 8px; border: 1px solid rgba(237,236,236,.15); }}
  .chip span, .chip code {{ display: block; font-size: 12px; }}
  .chip code {{ color: #d7d6d5; }}
  button {{ background: #edecec; color: #14120b; border: 0; border-radius: 9999px; padding: 6px 11px; font: 14px/1 ui-sans-serif, system-ui, sans-serif; }}
  a {{ color: #f54e00; }}
</style>
</head>
<body>
  <h1>Cursor public site</h1>
  <p>Declared colours from cursor.com on 2026-11-22. One dark theme. The accent is the orange the site declares. The primary button is a light pill.</p>
  <button>Download</button>
  <h2>Declared swatches</h2>
  <div class="row">{''.join(chip(n, v) for n, v in rows)}</div>
  <h2>Roles</h2>
  <div class="row">{''.join(chip(n, v) for n, v in roles)}</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
