#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def css_name(path):
    return "--" + path.replace(".", "-")


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def css_value(token):
    value = token["$value"]
    if token.get("$type") == "cubicBezier" and isinstance(value, list):
        return "cubic-bezier(" + ", ".join(str(n) for n in value) + ")"
    if isinstance(value, (int, float)) and token.get("$type") == "fontWeight":
        return str(value)
    return str(value)


def block(theme):
    lines = []
    for path, token in walk(T.get(theme, {})):
        lines.append(f"  {css_name(path)}: {css_value(token)};")
    return "\n".join(lines)


html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Deezer style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --sg-sans: Inter, Arial, sans-serif;
  --sg-display: "Deezer Brand", Tahoma, sans-serif;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page, #fff); color: var(--text-primary, #111); font: 400 14px/20px var(--sg-sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border-default, #ccc); }}
header h1 {{ font: 700 18px/24px var(--sg-display); margin: 0; letter-spacing: -0.03em; }}
button.toggle {{ margin-left: auto; border-radius: var(--radius-marketingButton); padding: 8px 14px; border: 1px solid var(--border-default, #555); background: transparent; color: inherit; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
h2 {{ font: 700 20px/24px var(--sg-display); margin: 32px 0 12px; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 8px; }}
.swatch {{ border-radius: 12px; overflow: hidden; border: 1px solid var(--border-default, #444); }}
.swatch i {{ display: block; height: 56px; }}
.swatch span {{ display: block; padding: 6px 8px; font-size: 12px; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.btn {{ display: inline-flex; align-items: center; height: 37px; padding: 0 20px; border-radius: 12px; font: 700 14px/1 var(--sg-sans); text-decoration: none; }}
.btn.primary {{ background: #a238ff; color: #fff; border: 0; }}
.btn.ghost {{ background: transparent; color: #fdfcfe; border: 1px solid #555257; }}
.btn.player {{ height: 48px; padding: 0 24px; border-radius: 16px; background: var(--background-accent); color: var(--text-onAccent); border: 0; }}
.field {{ height: 48px; width: 320px; border-radius: 16px; border: 0; background: var(--background-raised); color: var(--text-primary); padding: 0 16px; font: 400 15px/1 var(--sg-sans); }}
.hero {{ font: 800 64px/58px var(--sg-display); letter-spacing: -0.02em; text-transform: uppercase; margin: 12px 0; }}
</style>
</head>
<body>
<header>
  <h1>Deezer</h1>
  <span>Public capture, 2026-11-21. Signed out.</span>
  <button class="toggle" type="button" onclick="document.documentElement.dataset.mode = document.documentElement.dataset.mode === 'dark' ? 'light' : 'dark'">Toggle theme</button>
</header>
<main>
  <p>Dark tokens are Tempo semantic roles from the signed-out player. Light tokens are computed styles from the marketing homepage. The toggle swaps which set is applied to the page background and text.</p>
  <h2>Dark roles</h2>
  <div class="swatches" id="dark"></div>
  <h2>Light roles</h2>
  <div class="swatches" id="light"></div>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn ghost" href="#">Log in</a>
    <a class="btn primary" href="#">Sign up</a>
    <button class="btn player" type="button">Log in</button>
    <input class="field" placeholder="Artists, tracks, podcasts..." readonly>
  </div>
  <p class="hero">Where music comes to life</p>
</main>
<script>
const tokens = {json.dumps({"dark": T["dark"], "light": T["light"]})};
function paint(id, group) {{
  const root = document.getElementById(id);
  for (const [role, items] of Object.entries(group)) {{
    for (const [name, token] of Object.entries(items)) {{
      const el = document.createElement("div");
      el.className = "swatch";
      el.innerHTML = "<i></i><span></span>";
      el.querySelector("i").style.background = token.$value;
      el.querySelector("span").textContent = role + "." + name + " " + token.$value;
      root.appendChild(el);
    }}
  }}
}}
paint("dark", tokens.dark);
paint("light", tokens.light);
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
