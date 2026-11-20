#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. No values of its own."""
from __future__ import annotations

import html as html_lib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())


def resolve(value, theme: str):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return lookup(value[1:-1], theme)
    return value


def lookup(path: str, theme: str):
    node = tokens
    for part in path.split("."):
        node = node[part]
    if "$value" in node:
        return resolve(node["$value"], theme)
    return node


def swatches(theme: str) -> str:
    colors = tokens[theme]["color"]
    rows = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node and node.get("$type") == "color":
            value = resolve(node["$value"], theme)
            rows.append(
                f'<div class="swatch"><i style="background:{value}"></i>'
                f"<code>{path}</code><span>{value}</span></div>"
            )
        elif isinstance(node, dict):
            for key, child in node.items():
                if key.startswith("$"):
                    continue
                walk(child, f"{path}.{key}" if path else key)

    walk(colors, "")
    return "\n".join(rows)


def type_row(name: str) -> str:
    style = tokens["core"]["typography"][name]["$value"]
    family = resolve(style["fontFamily"], "light")
    size = style["fontSize"]
    weight = style["fontWeight"]
    line = style["lineHeight"]
    # escape every value put in the attribute: a stack like "Graphik Web", ... would close it
    family, size, weight, line = (html_lib.escape(str(v), quote=True) for v in (family, size, weight, line))
    return (
        f'<div class="type" style="font-family:{family};font-size:{size};'
        f'font-weight:{weight};line-height:{line}">'
        f"<code>{name}</code> {size} / {line} · {weight}<br>So long, farewell</div>"
    )


html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<title>Pocket style guide</title>
<style>
  :root {{
    --canvas: {tokens["light"]["color"]["canvas"]["$value"]};
    --text: {tokens["light"]["color"]["text"]["primary"]["$value"]};
    --muted: {tokens["light"]["color"]["text"]["secondary"]["$value"]};
    --line: {tokens["light"]["color"]["divider"]["tertiary"]["$value"]};
    --accent: {tokens["light"]["color"]["action"]["primary"]["$value"]};
    --sans: {tokens["core"]["font"]["family"]["sans"]["$value"]};
    --serif: {tokens["core"]["font"]["family"]["serif-alt"]["$value"]};
  }}
  html[data-theme="dark"] {{
    --canvas: {tokens["dark"]["color"]["canvas"]["$value"]};
    --text: {tokens["dark"]["color"]["text"]["primary"]["$value"]};
    --muted: {tokens["dark"]["color"]["text"]["secondary"]["$value"]};
    --line: {tokens["dark"]["color"]["divider"]["tertiary"]["$value"]};
    --accent: {tokens["dark"]["color"]["action"]["focus"]["$value"]};
  }}
  body {{ margin: 0; background: var(--canvas); color: var(--text);
    font-family: {tokens["core"]["font"]["family"]["sans"]["$value"]}; font-size: 16px; line-height: 24px; }}
  main {{ max-width: 1128px; margin: 0 auto; padding: 48px 40px 80px; }}
  h1 {{ font-family: var(--serif); font-size: 38px; line-height: 42.75px; font-weight: 700; margin: 0 0 8px; }}
  h2 {{ font-family: var(--serif); font-size: 24px; line-height: 28.8px; margin: 40px 0 16px; }}
  p.note {{ color: var(--muted); max-width: 62ch; }}
  button.theme {{ border: 1px solid var(--text); background: var(--canvas); color: var(--text);
    border-radius: 8px; padding: 8px 16px; font: inherit; cursor: pointer; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
  .swatch {{ border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
  .swatch i {{ display: block; height: 48px; }}
  .swatch code, .swatch span {{ display: block; padding: 4px 8px; font-size: 12px; }}
  .type {{ border-bottom: 1px solid var(--line); padding: 12px 0; }}
  .type code {{ color: var(--muted); font-size: 12px; }}
  .buttons {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
  a.btn {{ display: inline-block; border-radius: 8px; padding: 16px 24px; font-size: 20px;
    line-height: 30px; text-decoration: none; }}
  a.primary {{ background: {tokens["light"]["color"]["action"]["primary"]["$value"]}; color: #fff;
    border: 1px solid {tokens["light"]["color"]["action"]["primary"]["$value"]}; }}
  a.secondary {{ background: var(--canvas); color: var(--text); border: 1px solid var(--text); }}
  a.btn:focus-visible {{ outline: 1px auto {tokens["light"]["color"]["action"]["focus"]["$value"]}; outline-offset: 1px; }}
</style>
</head>
<body>
<main>
  <button class="theme" type="button" id="theme">Dark tokens</button>
  <h1>Pocket</h1>
  <p class="note">Public shutdown page, 2026-11-19. Light values were computed on getpocket.com/home. Dark values are the stylesheet’s .colormode-dark declarations. The page did not paint dark.</p>
  <h2>Type</h2>
  {"".join(type_row(name) for name in tokens["core"]["typography"])}
  <h2>Buttons</h2>
  <div class="buttons">
    <a class="btn primary" href="#primary">Contact Support</a>
    <a class="btn secondary" href="#secondary">Additional details</a>
  </div>
  <h2>Colour</h2>
  <div class="swatches" id="swatches">{swatches("light")}</div>
</main>
<script>
  const light = {json.dumps(swatches("light")).replace("<", "\\u003c")};
  const dark = {json.dumps(swatches("dark")).replace("<", "\\u003c")};
  document.getElementById("theme").addEventListener("click", () => {{
    const html = document.documentElement;
    const next = html.dataset.theme === "light" ? "dark" : "light";
    html.dataset.theme = next;
    document.getElementById("swatches").innerHTML = next === "dark" ? dark : light;
    document.getElementById("theme").textContent = next === "dark" ? "Light tokens" : "Dark tokens";
  }});
</script>
</body>
</html>
"""

(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
