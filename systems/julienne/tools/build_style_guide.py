#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Every swatch is a CSS custom property generated from tokens.json. Light is
the boot theme; the toggle sets data-theme=dark, which is the class the
product's own Toggle theme control sets on html. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: "var(" + cssname(m.group(1)) + ")", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty in ("transition", "animation", "string"):
        return None
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow" and isinstance(v, list):
        parts = []
        for s in v:
            parts.append(("inset " if s.get("inset") else "") + f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}')
        return ", ".join(parts)
    if isinstance(v, (dict, list)):
        return None
    return alias(v)


def block(name):
    lines = []
    for n, t in flat(T[name]):
        val = css_val(t)
        if val:
            lines.append(f"  {cssname(n)}: {val};")
    return "\n".join(lines)


html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Julienne style guide</title>
<!-- No web font is fetched: opening the guide contacts no third party. EB Garamond and Inter
     render when installed locally, otherwise the token stacks fall back to system faces. -->
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
}}
[data-theme="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-page); color: var(--color-ink); font: 400 16px/24px Inter, ui-sans-serif, system-ui, sans-serif; }}
header {{ display: flex; align-items: center; gap: 16px; height: var(--size-header); padding: 0 24px; border-bottom: 1px solid var(--color-fieldBorder); position: sticky; top: 0; background: var(--color-page); }}
header h1 {{ font: 400 28px/32px "EB Garamond", serif; margin: 0; }}
header button {{ margin-left: auto; height: 44px; padding: 0 16px; border-radius: var(--radius-pill); border: 1px solid var(--color-fieldBorder); background: var(--color-glass); color: var(--color-ink); }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font: 400 32px/36px "EB Garamond", serif; margin: 40px 0 12px; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
.swatch {{ border: 1px solid var(--color-fieldBorder); border-radius: 12px; overflow: hidden; }}
.swatch i {{ display: block; height: 64px; }}
.swatch span {{ display: block; padding: 8px; font-size: 12px; color: var(--color-muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0; }}
.brand {{ background: var(--color-brand); color: var(--color-onBrand); height: var(--size-button); padding: 0 20px; border: 0; border-radius: var(--radius-control); font: 400 14px/20px Inter, sans-serif; }}
.pill {{ background: var(--color-glass); color: var(--color-ink); height: var(--size-glass); padding: 0 16px; border-radius: var(--radius-pill); border: 1px solid var(--color-fieldBorder); box-shadow: var(--shadow-glassLift); }}
.chip {{ background: var(--color-chipOn); color: var(--color-onBrand); height: var(--size-chip); padding: 0 14px; border: 0; border-radius: var(--radius-pill); }}
.field {{ height: var(--size-field); width: 280px; border-radius: var(--radius-control); border: var(--border-hairline) solid var(--color-fieldBorder); background: var(--color-field); padding: 0 16px; color: var(--color-ink); }}
.card {{ background: var(--color-footer); padding: 16px; border-radius: 16px; max-width: 280px; }}
.display {{ font: 400 var(--font-size-display)/var(--font-lineHeight-display) "EB Garamond", serif; margin: 0; }}
.small {{ font: 400 var(--font-size-display-sm)/var(--font-lineHeight-display-sm) "EB Garamond", serif; }}
.caption {{ color: var(--color-muted); font-size: var(--font-size-caption); }}
a {{ color: var(--color-link); }}
</style>
</head>
<body>
<header>
  <h1>Julienne</h1>
  <button type="button" id="theme">Toggle theme</button>
</header>
<main>
  <p>Rendered from tokens.json. Light is the boot theme. Dark is the header Toggle theme control.</p>
  <h2>Colour</h2>
  <div class="swatches" id="swatches"></div>
  <h2>Type</h2>
  <p class="display">Creamy leek and mushroom soup</p>
  <p class="small">Discover and save the latest trending recipes.</p>
  <p>Body copy sits in the system sans. Filter labels and auth buttons use Inter.</p>
  <p class="caption">30m Total Time</p>
  <h2>Controls</h2>
  <div class="row">
    <button class="brand" type="button">See more recipes</button>
    <button class="pill" type="button">Search all recipes</button>
    <button class="chip" type="button">Breakfast</button>
  </div>
  <div class="row">
    <input class="field" placeholder="Your email" aria-label="Email">
  </div>
  <div class="card">
    <p class="small" style="margin:0">Newest recipes</p>
    <p class="caption">Footer surface</p>
  </div>
</main>
<script>
const root = document.documentElement;
document.getElementById("theme").onclick = () => {{
  root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
}};
const roles = ["page","ink","nav","muted","prose","brand","onBrand","link","footer","field","fieldBorder","disabledFill","disabledInk","glass","chipOn","cook"];
const box = document.getElementById("swatches");
for (const role of roles) {{
  const el = document.createElement("div");
  el.className = "swatch";
  el.innerHTML = "<i></i><span></span>";
  el.querySelector("i").style.background = "var(--color-" + role + ")";
  el.querySelector("span").textContent = role;
  box.appendChild(el);
}}
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
