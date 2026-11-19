#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Self-contained. No network fonts.

Windy's UI face is the system stack. Bariol is proprietary and is not loaded;
the big-number specimen falls back to Arial, which the login button already uses.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        if isinstance(v, str):
            return alias(v)
        return f'{v["offsetX"]} {v["offsetY"]} {v["blur"]} {v["spread"]} {alias(v["color"])}'
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    if ty in ("number",):
        return str(v)
    return alias(v)


def block(set_name):
    lines = []
    for path, tok in flat(T[set_name]):
        val = css_val(tok)
        if val is None:
            continue
        lines.append(f"  {cssname(path)}: {val};")
    return "\n".join(lines)


CORE = block("core")
LIGHT = block("light")
DARK = block("dark")

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Windy style guide</title>
<style>
:root {{
{CORE}
{LIGHT}
  color-scheme: light;
  --sg-sans: -apple-system, system-ui, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
}}
[data-mode="dark"] {{
{DARK}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--background-page);
  color: var(--text-primary);
  font: 400 14px/20px var(--sg-sans);
}}
header {{
  display: flex; gap: 16px; align-items: center; flex-wrap: wrap;
  padding: 16px 24px; border-bottom: 1px solid var(--border-stroke);
}}
header h1 {{ margin: 0; font-size: 28px; font-weight: 300; line-height: 28px; }}
header button {{
  margin-left: auto; background: var(--background-action); color: var(--text-on-action);
  border: 0; border-radius: 24px; padding: 4px 16px; font: inherit; cursor: pointer;
}}
main {{ max-width: 1080px; margin: 0 auto; padding: 24px; }}
h2 {{ font-weight: 300; font-size: 28px; margin: 32px 0 8px; }}
p {{ max-width: 70ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--border-stroke); }}
.sw b {{ font-size: 12px; }}
.sw span {{ display: block; font-size: 12px; color: var(--text-secondary); }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; margin: 12px 0; }}
.search {{
  background: var(--component-search-bg); color: var(--component-search-text);
  height: var(--component-search-height); border-radius: var(--component-search-radius);
  padding: 0 var(--component-search-padding); border: 0;
  box-shadow: var(--shadow-lift); font-size: 18px; width: 280px;
}}
.btn {{
  background: var(--component-button-bg); color: var(--component-button-text);
  height: var(--component-button-height); border-radius: var(--component-button-radius);
  padding: 0 var(--component-button-padding); border: 0; font: 300 18px/1 Arial, sans-serif;
}}
.chip {{
  background: var(--component-chip-bg); color: var(--component-chip-text);
  height: var(--component-chip-height); border-radius: var(--component-chip-radius);
  padding: 0 12px; display: inline-flex; align-items: center; font-size: 12px; font-weight: 700;
  box-shadow: var(--shadow-lift);
}}
.menu {{
  background: var(--component-menu-bg); color: var(--component-menu-text);
  border-radius: var(--component-menu-radius); padding: 10px; width: 280px;
  border: 1px solid var(--border-stroke);
}}
.field {{
  background: var(--component-field-bg); color: var(--component-field-text);
  height: var(--component-field-height); border-radius: var(--component-field-radius);
  border: 1px solid var(--component-field-bg); padding: 0 8px; width: 240px; font-size: 18px;
}}
.card {{
  background: var(--background-surface); color: var(--text-primary);
  border-radius: 8px; padding: 16px; width: 280px;
}}
</style>
</head>
<body>
<header>
  <h1>Windy</h1>
  <span>Signed-out map, 2026-11-19</span>
  <button type="button" id="theme">Theme</button>
</header>
<main>
  <p>Colours, type, and controls from tokens.json. The map canvas is not a token. Dark is the chrome you see. Light is the :root binding and the white detail table.</p>
  <h2>Colour</h2>
  <div class="swatches" id="swatches"></div>
  <h2>Type</h2>
  <div style="font: var(--typography-title)">Oslo, 22:00</div>
  <div style="font: var(--typography-search); margin-top: 8px">Search...</div>
  <div style="font: var(--typography-body); margin-top: 8px">Wind, rain, temperature. Body is 14px system sans.</div>
  <div style="font: 400 67px/67px Arial, Helvetica, sans-serif; margin-top: 8px">25°</div>
  <p>The 67px figure is bariolnumbers on the product. Arial is the fallback, and the face used by the login button.</p>
  <h2>Controls</h2>
  <div class="row"><input class="search" value="Search..."></div>
  <div class="row"><button class="btn" type="button">Login</button><span class="chip">ECMWF 9km</span></div>
  <div class="row"><input class="field" placeholder="Email Address"></div>
  <div class="menu"><div>My Favorites</div><div>My Alerts</div><div>Settings</div></div>
  <div class="card" style="margin-top:16px">Detail table sits on the light surface, #f8f8f8, even while the map is dark.</div>
</main>
<script>
const root = document.documentElement;
const names = ["background-page","background-surface","background-ui","background-action","text-primary","text-secondary","text-link","text-on-action","border-stroke","border-selected","status-error","status-ok","status-premium"];
const box = document.getElementById("swatches");
function paint() {{
  box.innerHTML = "";
  for (const n of names) {{
    const v = getComputedStyle(root).getPropertyValue("--" + n).trim();
    const el = document.createElement("div");
    el.className = "sw";
    el.innerHTML = "<i></i><div><b></b><span></span></div>";
    el.querySelector("i").style.background = v;
    el.querySelector("b").textContent = n;
    el.querySelector("span").textContent = v;
    box.appendChild(el);
  }}
}}
document.getElementById("theme").addEventListener("click", () => {{
  root.dataset.mode = root.dataset.mode === "dark" ? "light" : "dark";
  paint();
}});
paint();
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
