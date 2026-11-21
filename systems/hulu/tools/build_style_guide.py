#!/usr/bin/env python3
"""Write systems/hulu/style-guide.html from tokens.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
color = tokens["light"]["color"]
font = tokens["core"]["font"]["family"]["sans"]["$value"]

def v(name):
    return color[name]["$value"]

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hulu style guide</title>
  <style>
    :root {{
      --page: {v("page")};
      --text: {v("text")};
      --ink: {v("ink")};
      --on-ink: {v("onInk")};
      --accent: {v("accent")};
      --wordmark: {v("wordmark")};
      --field: {v("field")};
      --link: {v("link")};
    }}
    body {{
      margin: 0;
      background: var(--page);
      color: var(--text);
      font-family: {font};
      font-size: 16px;
      line-height: 24px;
    }}
    main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
    h1 {{ font-size: 32px; line-height: 40px; font-weight: 600; }}
    h2 {{ font-size: 20px; margin-top: 40px; }}
    .swatch {{
      display: inline-block;
      width: 88px;
      height: 48px;
      border-radius: 4px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .row {{ margin: 12px 0; }}
    .pill {{
      display: inline-block;
      background: var(--ink);
      color: var(--on-ink);
      border-radius: 1000px;
      height: 48px;
      line-height: 48px;
      padding: 0 24px;
      font-size: 14px;
      font-weight: 600;
    }}
    .field {{
      background: var(--field);
      border-radius: 4px;
      padding: 16px;
      color: #252526;
    }}
    .search {{
      background: #fff;
      border: 2px solid var(--accent);
      border-radius: 4px;
      padding: 12px 16px;
    }}
    a {{ color: var(--link); }}
  </style>
</head>
<body>
  <main>
    <h1>Hulu</h1>
    <p>Public plan chooser, empty login wall, Help Center, and press site. Signed out, 2026-11-22.</p>
    <h2>Colour</h2>
    <div class="row"><span class="swatch" style="background: var(--page); border: 1px solid #ddd"></span> Page {v("page")}</div>
    <div class="row"><span class="swatch" style="background: var(--text)"></span> Text {v("text")}</div>
    <div class="row"><span class="swatch" style="background: var(--ink)"></span> Ink {v("ink")}</div>
    <div class="row"><span class="swatch" style="background: var(--accent)"></span> Accent {v("accent")}</div>
    <div class="row"><span class="swatch" style="background: var(--wordmark)"></span> Wordmark {v("wordmark")}</div>
    <div class="row"><span class="swatch" style="background: var(--field)"></span> Field {v("field")}</div>
    <h2>Controls</h2>
    <p><span class="pill">SELECT</span></p>
    <p class="field">Email</p>
    <p class="search">Enter a question or topic</p>
    <p><a href="#plans">Terms apply</a></p>
  </main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("style guide written")
