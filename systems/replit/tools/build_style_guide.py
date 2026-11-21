#!/usr/bin/env python3
"""Write style-guide.html from tokens.json.

    python3 tools/build_style_guide.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, prefix=""):
    if isinstance(node, dict) and "$value" in node:
        yield prefix, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            path = f"{prefix}.{key}" if prefix else key
            yield from walk(child, path)


def resolve(value, tokens):
    if not isinstance(value, str) or not value.startswith("{"):
        return value
    path = value.strip("{}")
    if path.startswith("core."):
        path = path[len("core."):]
    cursor = tokens["core"]
    for part in path.split("."):
        cursor = cursor[part]
    return resolve(cursor["$value"], tokens)


def swatch(path, value, source):
    shown = html.escape(str(value))
    label = html.escape(path)
    src = html.escape(source)
    return (
        f'<div class="sw"><i style="background:{html.escape(str(value))}"></i>'
        f"<span>{label}<br>{shown}</span><small>{src}</small></div>"
    )


def main() -> None:
    core = TOKENS["core"]
    light = TOKENS["light"]
    colors = []
    for path, token in walk(core["color"]):
        if token.get("$type") != "color":
            continue
        if path.startswith("accent-") and not path.endswith("-default"):
            continue
        colors.append(
            swatch(
                path,
                token["$value"],
                token["$extensions"]["source"].split(".")[0],
            )
        )
    roles = []
    for path, token in walk(light):
        if token.get("$type") != "color":
            continue
        value = resolve(token["$value"], TOKENS)
        roles.append(swatch("light." + path, value, token["$extensions"]["source"]))

    page = resolve(light["background"]["page"]["$value"], TOKENS)
    ink = resolve(light["text"]["primary"]["$value"], TOKENS)
    accent = resolve(light["accent"]["$value"], TOKENS)
    on_action = resolve(light["text"]["on-action"]["$value"], TOKENS)
    header = resolve(light["background"]["header"]["$value"], TOKENS)
    footer = resolve(light["background"]["footer"]["$value"], TOKENS)
    composer = resolve(light["background"]["composer"]["$value"], TOKENS)
    upgrade = resolve(light["background"]["upgrade"]["$value"], TOKENS)

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Replit style guide</title>
<style>
  :root {{
    --page: {page};
    --ink: {ink};
    --accent: {accent};
    --on-action: {on_action};
    --header: {header};
    --footer: {footer};
    --composer: {composer};
    --upgrade: {upgrade};
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--page);
    color: var(--ink);
    font: 400 14px/1.6 "Replit Diatype", "Segoe UI", sans-serif;
  }}
  header {{
    background: var(--header);
    padding: 20px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  header strong {{ font-weight: 500; letter-spacing: -0.28px; }}
  .signup {{
    background: var(--accent);
    color: var(--on-action);
    border: 0;
    border-radius: 8px;
    padding: 8px 12px;
    font: 500 14px/20px "Replit Diatype", "Segoe UI", sans-serif;
    letter-spacing: -0.28px;
  }}
  main {{ padding: 32px; max-width: 1100px; }}
  h1 {{
    margin: 0 0 8px;
    font: 400 64px/64px "Replit Diatype", "Segoe UI", sans-serif;
    letter-spacing: -3.84px;
    color: #37383c;
  }}
  h2 {{ font: 460 32px/40px "Replit Diatype", "Segoe UI", sans-serif; margin: 32px 0 12px; }}
  .composer {{
    background: var(--composer);
    border-radius: 20px;
    padding: 16px;
    max-width: 640px;
    box-shadow: inset 0 0 0 1px #d3d1c9;
  }}
  .start {{
    background: var(--accent);
    color: #ffffffe6;
    border: 0;
    border-radius: 9999px;
    padding: 8px 16px;
  }}
  .upgrade {{
    background: var(--upgrade);
    color: #fcfcfc;
    border: 0;
    border-radius: 6px;
    padding: 0 8px;
    height: 32px;
  }}
  .swatches {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
  }}
  .sw {{
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #d2d4d6;
  }}
  .sw i {{ display: block; height: 56px; }}
  .sw span, .sw small {{ display: block; padding: 8px 10px 0; }}
  .sw small {{ color: #5c5f66; padding-bottom: 10px; }}
  footer {{
    background: var(--footer);
    padding: 24px 32px;
    margin-top: 32px;
  }}
</style>
</head>
<body>
<header>
  <strong>Replit</strong>
  <button class="signup">Sign up</button>
</header>
<main>
  <h1>What will you build?</h1>
  <p>Measured from the signed-out public site on 22 November 2026. One light theme.</p>
  <div class="composer">
    <p>Start</p>
    <button class="start">Start</button>
  </div>
  <p><button class="upgrade">Upgrade to Pro</button></p>
  <h2>Roles</h2>
  <div class="swatches">
    {''.join(roles)}
  </div>
  <h2>Core colours</h2>
  <div class="swatches">
    {''.join(colors)}
  </div>
</main>
<footer>Footer surface, hsl(33 47% 96%), computed #faf5f0.</footer>
</body>
</html>
"""
    (ROOT / "style-guide.html").write_text(doc)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
