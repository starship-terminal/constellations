#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())

def val(token):
    return token["$value"] if isinstance(token, dict) and "$value" in token else token

rows = []
for theme in ("dark", "light"):
    for role in ("page", "surface", "text", "muted", "accent", "border", "link", "focus"):
        rows.append((theme, role, val(tokens[theme][role])))

gray = [(k, val(v)) for k, v in tokens["core"]["color"]["gray"].items()]
radii = [(k, val(v)) for k, v in tokens["core"]["radius"].items()]

def swatch(color):
    return f'<span class="sw" style="background:{color}"></span> <code>{color}</code>'

html = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<title>Resend style guide</title>
<style>
  :root {{ color-scheme: dark; font-family: ui-sans-serif, system-ui, sans-serif; background: #000; color: #f0f0f0; }}
  html[data-theme="light"] {{ color-scheme: light; background: #fff; color: #161616; }}
  body {{ margin: 0 auto; max-width: 880px; padding: 32px 20px 80px; }}
  h1 {{ font-weight: 400; letter-spacing: -0.02em; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0 28px; }}
  td, th {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid #333; font-size: 14px; }}
  .sw {{ display: inline-block; width: 18px; height: 18px; border-radius: 4px; vertical-align: middle; border: 1px solid #666; }}
  button.theme {{ border-radius: 16px; padding: 8px 16px; font-weight: 600; }}
  .specimen {{ display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 16px; font-size: 14px; font-weight: 600; margin-right: 8px; }}
</style>
</head>
<body>
<button class="theme" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">Toggle theme</button>
<h1>Resend</h1>
<p>Values from tokens.json. Marketing site is dark. Docs also has a light theme.</p>
<h2>Roles</h2>
<table>
<tr><th>Theme</th><th>Role</th><th>Value</th></tr>
{''.join(f'<tr><td>{t}</td><td>{r}</td><td>{swatch(c)}</td></tr>' for t, r, c in rows)}
</table>
<h2>Gray ramp</h2>
<table>
{''.join(f'<tr><td>{k}</td><td>{swatch(c)}</td></tr>' for k, c in gray)}
</table>
<h2>Radius</h2>
<table>
{''.join(f'<tr><td>{k}</td><td>{c}</td></tr>' for k, c in radii)}
</table>
<h2>Components</h2>
<p><span class="specimen" style="color:#fff;border:2px solid rgba(255,255,255,.05)">Get started</span>
<span class="specimen" style="background:#fff;color:#000">Get started hover</span></p>
<p>Display: domaine 96px. Body: Inter Website 16/24. Mono: Commit Mono Website.</p>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
