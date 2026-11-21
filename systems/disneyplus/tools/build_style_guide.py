#!/usr/bin/env python3
"""Write style-guide.html from the measured Disney+ tokens."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
color = tokens["light"]["color"]


def v(name):
    return color[name]["$value"]


html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Disney+ style guide</title>
  <style>
    :root {{
      --page: {v("page")};
      --text: {v("text")};
      --muted: {v("muted")};
      --accent: {v("accent")};
      --on-accent: {v("onAccent")};
      --border: {v("border")};
      --link: {v("link")};
      --wall: {v("wall")};
      --ink: {v("ink")};
    }}
    body {{
      margin: 0;
      background: var(--page);
      color: var(--text);
      font-family: Inspire, sans-serif;
      font-size: 18px;
      line-height: 1.4;
    }}
    main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
    h1 {{ font-size: 40px; line-height: 48px; letter-spacing: -0.16px; font-weight: 700; }}
    h2 {{ font-size: 24px; margin-top: 40px; }}
    .muted {{ color: var(--muted); font-size: 16px; }}
    .row {{ display: flex; gap: 16px; flex-wrap: wrap; margin: 16px 0; }}
    .swatch {{
      width: 140px;
      background: var(--wall);
      border-radius: 12px;
      overflow: hidden;
    }}
    .swatch i {{ display: block; height: 64px; }}
    .swatch span {{ display: block; padding: 8px 10px; font-size: 13px; color: var(--text); }}
    .cta {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 200px;
      height: 48px;
      padding: 12px 16px;
      border-radius: 1000px;
      background: var(--accent);
      color: var(--on-accent);
      letter-spacing: 0.4px;
      text-decoration: none;
    }}
    .login {{
      display: inline-flex;
      align-items: center;
      height: 36px;
      padding: 8px 12px;
      border-radius: 1000px;
      border: 2px solid var(--border);
      background: rgba(0, 0, 0, 0.8);
      color: var(--text);
      letter-spacing: 0.35px;
      font-size: 14px;
      text-decoration: none;
    }}
    a.quiet {{ color: var(--link); }}
    .card {{
      background: #fff;
      color: var(--ink);
      border-radius: 16px;
      padding: 24px;
      max-width: 360px;
    }}
    .field {{
      margin-top: 16px;
      height: 48px;
      border-radius: 4px;
      background: #e8e8ed;
      color: #6b6b70;
      display: flex;
      align-items: center;
      padding: 0 16px;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Disney+</h1>
    <p class="muted">Public marketing specimens from measured tokens. 22 November 2026.</p>
    <h2>Colour</h2>
    <div class="row">
      <div class="swatch"><i style="background:{v("page")}"></i><span>Page {v("page")}</span></div>
      <div class="swatch"><i style="background:{v("text")}"></i><span>Text {v("text")}</span></div>
      <div class="swatch"><i style="background:{v("muted")}"></i><span>Muted {v("muted")}</span></div>
      <div class="swatch"><i style="background:{v("accent")}"></i><span>Accent {v("accent")}</span></div>
      <div class="swatch"><i style="background:{v("onAccent")}"></i><span>On accent {v("onAccent")}</span></div>
      <div class="swatch"><i style="background:{v("border")}"></i><span>Border {v("border")}</span></div>
      <div class="swatch"><i style="background:{v("wall")}"></i><span>Wall {v("wall")}</span></div>
      <div class="swatch"><i style="background:{v("ink")}"></i><span>Ink {v("ink")}</span></div>
    </div>
    <h2>Controls</h2>
    <p><a class="cta" href="#plans">DISNEY+ ANNUAL</a></p>
    <p><a class="login" href="#login">LOG IN</a></p>
    <p><a class="quiet" href="#plans">View plan details</a></p>
    <h2>Login card</h2>
    <div class="card">
      <strong>Enter your email address to continue</strong>
      <div class="field">Email</div>
    </div>
  </main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
