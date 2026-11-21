#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())

def walk(node, prefix=""):
    found = []
    if isinstance(node, dict) and "$value" in node:
        found.append((prefix, node))
        return found
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            path = f"{prefix}.{key}" if prefix else key
            found.extend(walk(child, path))
    return found

def resolve(value, seen=None):
    seen = seen or set()
    if not isinstance(value, str) or not value.startswith("{") or not value.endswith("}"):
        return value
    if value in seen:
        raise SystemExit(f"alias loop {value}")
    seen.add(value)
    path = value[1:-1].split(".")
    node = tokens
    for part in path:
        node = node[part]
    return resolve(node["$value"], seen)

rows = []
for set_name in ("core", "light", "dark"):
    for path, token in walk(tokens[set_name], set_name):
        if token.get("$type") != "color":
            continue
        raw = token["$value"]
        paint = resolve(raw)
        rows.append((path, raw, paint, token["$extensions"]["source"]))

swatches = "\n".join(
    f'      <div class="swatch"><div class="chip" style="background:{paint}"></div>'
    f'<div class="label">{path}<br>{paint}</div></div>'
    for path, raw, paint, source in rows
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Evernote public tokens</title>
  <style>
    :root {{
      --cream: #f9f6f2;
      --ink: #141414;
      --sand: #f4eee5;
      --lime: #94e130;
      --white: #ffffff;
      --green: #00a82d;
      --stroke: #a1a1a1;
      --card: #e7e7e7;
      --display: Figtree, system-ui, sans-serif;
      --text: Inter, system-ui, sans-serif;
    }}
    body {{
      margin: 0;
      background: var(--cream);
      color: var(--ink);
      font-family: var(--text);
      font-size: 16px;
      line-height: 24px;
    }}
    main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
    h1 {{
      font-family: var(--display);
      font-weight: 600;
      font-size: 72px;
      line-height: 72px;
      letter-spacing: -3.6px;
      margin: 24px 0 8px;
    }}
    h2 {{
      font-family: var(--display);
      font-weight: 600;
      font-size: 32px;
      margin: 40px 0 12px;
    }}
    p {{ margin: 0 0 16px; color: #262626; }}
    .bar {{
      background: var(--cream);
      height: 81px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      border-bottom: 1px solid var(--card);
    }}
    .bar a {{
      color: #000;
      font-family: var(--display);
      font-size: 16px;
      text-decoration: none;
      margin-right: 16px;
    }}
    button, .btn {{
      background: var(--ink);
      color: var(--white);
      border: 0;
      border-radius: 5px;
      padding: 10px 28px;
      font: 600 16px/24px var(--display);
      height: 46px;
    }}
    .outline {{
      background: transparent;
      color: var(--ink);
      border: 1px solid var(--stroke);
    }}
    .lime {{
      background: var(--lime);
      color: var(--ink);
    }}
    .dark {{
      background: #141414;
      color: var(--white);
      padding: 32px 24px;
      border-radius: 16px;
    }}
    .dark h2 {{ color: var(--white); margin-top: 0; }}
    .dark p {{ color: var(--white); }}
    .swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
    .swatch {{ width: 180px; }}
    .chip {{ height: 56px; border-radius: 5px; border: 1px solid var(--card); }}
    .label {{ font-size: 12px; line-height: 16px; margin-top: 6px; }}
    .card {{
      background: var(--sand);
      border: 1px solid var(--card);
      border-radius: 16px;
      padding: 24px;
      margin: 16px 0 24px;
    }}
    .chip-pill {{
      display: inline-block;
      background: var(--lime);
      color: var(--ink);
      border-radius: 52px;
      padding: 4px 12px;
      font-family: var(--display);
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <div class="bar">
    <div><a>AI Features</a><a>Plans</a><a>Enterprise</a></div>
    <button type="button">Start for free</button>
  </div>
  <main>
    <h1>Your second brain</h1>
    <p>Public tokens measured on 2026-11-22 from computed styles. Figtree and Inter are not bundled, so this page falls back to the system face.</p>
    <div class="card">
      <span class="chip-pill">Capture</span>
      <p>The sand card is #f4eee5 with a #e7e7e7 hairline and a 16px radius.</p>
      <button class="lime" type="button">Discover more</button>
      <button class="outline" type="button">Choose Starter</button>
    </div>
    <div class="dark">
      <h2>Focus on what matters</h2>
      <p>The AI Features page paints this ink field. Start for free turns lime there.</p>
      <button class="lime" type="button">Start for free</button>
    </div>
    <h2>Colour</h2>
    <div class="swatches">
{swatches}
    </div>
    <h2>Green</h2>
    <p>The elephant mark is #00a82d. That green is the stylesheet hover fill. The buttons on the measured pages were not hovered, so the painted accent in this guide is the lime that was on screen.</p>
  </main>
</body>
</html>
"""

(ROOT / "style-guide.html").write_text(html)
print(f"wrote style-guide.html with {len(rows)} colour chips")
