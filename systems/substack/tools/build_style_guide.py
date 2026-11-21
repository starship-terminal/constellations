#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. python3 tools/build_style_guide.py"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((PKG / "tokens.json").read_text())

def v(group, name):
    return tokens[group][name]["$value"]

html = f"""<!doctype html>
<meta charset="utf-8">
<title>Substack public tokens</title>
<style>
  :root {{
    --page: {v("dark","page")};
    --surface: {v("dark","surface")};
    --text: {v("dark","text")};
    --muted: {v("dark","muted")};
    --accent: {v("dark","accent")};
    --on: {v("dark","onAccent")};
    --border: {v("dark","border")};
  }}
  body.light {{
    --page: {v("light","page")};
    --surface: {v("light","surface")};
    --text: {v("light","text")};
    --muted: {v("light","muted")};
    --accent: {v("light","accent")};
    --on: {v("light","onAccent")};
    --border: {v("light","border")};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 16px/1.4 system-ui, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 32px 20px 64px; }}
  h1 {{ font-weight: 800; letter-spacing: -0.03em; }}
  button.toggle {{ background: transparent; color: var(--text); border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0 28px; }}
  .swatch {{ width: 120px; }}
  .chip {{ height: 64px; border-radius: 12px; border: 1px solid var(--border); }}
  .label {{ font-size: 12px; color: var(--muted); margin-top: 6px; }}
  .btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 8px; background: var(--accent); color: var(--on); font-weight: 600; border: 0; }}
  .ghost {{ background: transparent; color: var(--text); }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 20px; max-width: 420px; }}
  input {{ width: 100%; box-sizing: border-box; height: 40px; border-radius: 8px; border: 1px solid var(--border); background: var(--page); color: var(--text); padding: 0 12px; }}
</style>
<body>
<main>
  <button class="toggle" onclick="document.body.classList.toggle('light')">Toggle theme</button>
  <h1>Substack public</h1>
  <p>Roles from the public site. Take values from tokens.json.</p>
  <div class="row">
    <div class="swatch"><div class="chip" style="background:var(--page)"></div><div class="label">page</div></div>
    <div class="swatch"><div class="chip" style="background:var(--surface)"></div><div class="label">surface</div></div>
    <div class="swatch"><div class="chip" style="background:var(--text)"></div><div class="label">text</div></div>
    <div class="swatch"><div class="chip" style="background:var(--muted)"></div><div class="label">muted</div></div>
    <div class="swatch"><div class="chip" style="background:var(--accent)"></div><div class="label">accent</div></div>
    <div class="swatch"><div class="chip" style="background:var(--border)"></div><div class="label">border</div></div>
  </div>
  <p><button class="btn">Start your Substack</button> <button class="btn ghost">Sign in</button></p>
  <div class="card">
    <strong>Sign in to Substack</strong>
    <p><input placeholder="Email" aria-label="Email"></p>
    <p><button class="btn" style="width:100%;justify-content:center;border-radius:12px;height:48px">Continue</button></p>
  </div>
</main>
</body>
"""
(PKG / "style-guide.html").write_text(html)
print("style-guide")
