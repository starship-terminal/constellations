#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. No network."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
light = tokens["light"]["color"]
core = tokens["core"]


def v(node):
    return node["$value"]


colors = [
    ("Page", v(light["page"])),
    ("Text", v(light["text"])),
    ("Muted", v(light["muted"])),
    ("Accent", v(light["accent"])),
    ("On accent", v(light["onAccent"])),
    ("Surface", v(light["surface"])),
    ("Border", v(light["border"])),
    ("Focus", v(light["focus"])),
    ("Success", v(light["success"])),
    ("Warning", v(light["warning"])),
    ("Info", v(light["info"])),
]
chips = "\n".join(
    f'<div class="chip"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in colors
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Target style guide</title>
<style>
  body {{ margin: 24px; font-family: Helvetica, Arial, sans-serif; color: {v(light["text"])}; background: {v(light["page"])}; }}
  h1 {{ font-size: 28px; }}
  .row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .chip {{ width: 140px; }}
  .chip i {{ display: block; height: 56px; border-radius: 8px; border: 1px solid {v(light["border"])}; }}
  code {{ font-size: 12px; color: {v(light["muted"])}; }}
  button {{ background: {v(light["accent"])}; color: {v(light["onAccent"])}; border: 0; border-radius: 999px; height: 44px; padding: 0 16px; font-weight: 700; }}
  input {{ height: 44px; border-radius: 999px; border: 0; background: {v(light["surface"])}; padding: 0 16px; width: 280px; }}
</style>
</head>
<body>
  <h1>Target</h1>
  <p>Public tokens measured on target.com, 2026-11-22. Helvetica for Target is the UI face. The file is not in this package.</p>
  <div class="row">{chips}</div>
  <p><input placeholder="What can we help you find?" aria-label="Search"> <button>Sign up</button></p>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("style guide ok")
