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
<title>Zoom public tokens</title>
<style>
  :root {{
    --page: {v("dark","page")};
    --surface: {v("dark","surface")};
    --text: {v("dark","text")};
    --muted: rgba(255, 255, 255, 0.7);
    --accent: {v("dark","accent")};
    --on: {v("dark","onAccent")};
    --border: {v("dark","border")};
    --secondary: {v("dark","secondary")};
    --focus: {v("dark","focus")};
  }}
  body.light {{
    --page: {v("light","page")};
    --surface: {v("light","surface")};
    --text: {v("light","text")};
    --muted: rgba(34, 35, 37, 0.7);
    --accent: {v("light","accent")};
    --on: {v("light","onAccent")};
    --border: {v("light","border")};
    --secondary: {v("light","secondary")};
    --focus: {v("light","focus")};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 16px/1.45 Inter, Helvetica, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 32px 20px 64px; }}
  h1 {{ font-family: Newsreader, Georgia, serif; font-weight: 500; font-size: 40px; letter-spacing: -0.02em; }}
  button.toggle {{ background: transparent; color: var(--text); border: 1px solid var(--border); border-radius: 12px; padding: 8px 12px; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0 28px; }}
  .swatch {{ width: 120px; }}
  .chip {{ height: 64px; border-radius: 12px; border: 1px solid var(--border); }}
  .label {{ font-size: 12px; color: var(--muted); margin-top: 6px; }}
  .btn {{ display: inline-flex; align-items: center; height: 46px; padding: 0 20px; border-radius: 12px; background: var(--accent); color: var(--on); font-weight: 600; border: 0; }}
  .pale {{ background: var(--secondary); color: #00053d; }}
  .card {{ background: var(--surface); color: #222325; border-radius: 16px; padding: 20px; max-width: 420px; }}
  input {{ width: 100%; box-sizing: border-box; height: 48px; border-radius: 12px; border: 1px solid var(--focus); background: #fff; color: #222325; padding: 0 12px; }}
  .disabled {{ background: rgba(173, 177, 184, 0.25); color: #adb1b8; }}
</style>
<body>
<main>
  <button class="toggle" onclick="document.body.classList.toggle('light')">Toggle theme</button>
  <h1>Zoom public</h1>
  <p>Roles from the public marketing site and the empty auth walls. Take values from tokens.json.</p>
  <div class="row">
    <div class="swatch"><div class="chip" style="background:var(--page)"></div><div class="label">page</div></div>
    <div class="swatch"><div class="chip" style="background:var(--surface)"></div><div class="label">surface</div></div>
    <div class="swatch"><div class="chip" style="background:var(--text)"></div><div class="label">text</div></div>
    <div class="swatch"><div class="chip" style="background:var(--accent)"></div><div class="label">accent</div></div>
    <div class="swatch"><div class="chip" style="background:var(--secondary)"></div><div class="label">secondary</div></div>
    <div class="swatch"><div class="chip" style="background:var(--focus)"></div><div class="label">focus</div></div>
  </div>
  <p><button class="btn">Sign Up Free</button> <button class="btn pale">Contact Sales</button> <button class="btn disabled">Continue</button></p>
  <div class="card">
    <h2 style="font-family:Newsreader,Georgia,serif;font-weight:500">Sign in</h2>
    <input placeholder="Enter email, Zoom Mail or phone number" aria-label="Email">
  </div>
</main>
</body>
"""
(PKG / "style-guide.html").write_text(html)
print("wrote", PKG / "style-guide.html")
