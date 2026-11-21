#!/usr/bin/env python3
"""Write style-guide.html from the hand-measured Dia tokens.

ADAPTED_FOR = "Dia"
"""
ADAPTED_FOR = "Dia"

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())

def val(node):
    if isinstance(node, dict) and "$value" in node:
        v = node["$value"]
        if isinstance(v, str) and v.startswith("{core.color."):
            key = v.split(".")[-1].rstrip("}")
            return tokens["core"]["color"][key]["$value"]
        return v
    return node

swatches = [
    ("Paper", val(tokens["core"]["color"]["paper"])),
    ("Ink", val(tokens["core"]["color"]["ink"])),
    ("White", val(tokens["core"]["color"]["white"])),
    ("Hero", val(tokens["core"]["color"]["hero"])),
    ("Blue", val(tokens["core"]["color"]["blue"])),
    ("Yellow", val(tokens["core"]["color"]["yellow"])),
    ("Pink", val(tokens["core"]["color"]["pink"])),
    ("Red", val(tokens["core"]["color"]["red"])),
    ("Brown", val(tokens["core"]["color"]["brown"])),
]
chips = "\n".join(
    f'<div class="chip"><i style="background:{c}"></i><span>{n}</span><code>{c}</code></div>'
    for n, c in swatches
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Dia public tokens</title>
<style>
  body {{ margin: 0; background: #FBFAF6; color: rgba(0,0,0,.85); font: 16px/1.4 Helvetica, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-weight: 500; letter-spacing: -0.04em; font-size: 40px; }}
  .band {{ background: #DCB017; color: #fff; border-radius: 28px; padding: 48px 32px; text-align: center; }}
  .band p {{ font-size: 28px; margin: 0 0 24px; }}
  .pill {{ display: inline-block; background: #000; color: #F8F8F8; border-radius: 9999px; padding: 16px 28px; }}
  .chips {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 32px; }}
  .chip {{ background: #fff; border-radius: 16px; padding: 12px; }}
  .chip i {{ display: block; height: 48px; border-radius: 10px; border: 1px solid rgba(0,0,0,.06); }}
  code {{ display: block; margin-top: 6px; font-size: 13px; }}
</style>
</head>
<body>
<main>
  <h1>Dia public tokens</h1>
  <p>Measured on www.diabrowser.com, signed out. One theme.</p>
  <div class="band">
    <p>More than a browser. A better workday.</p>
    <span class="pill">Download Dia for free</span>
  </div>
  <div class="chips">{chips}</div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
