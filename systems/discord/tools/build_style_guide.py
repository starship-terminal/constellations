#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. No values are typed here."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def css_value(token):
    v = token["$value"]
    if isinstance(v, (int, float)):
        return str(v)
    return str(v)


def declarations(tree, prefix):
    lines = []
    for key, node in tree.items():
        if key.startswith("$"):
            continue
        if isinstance(node, dict) and "$value" in node:
            name = "--" + prefix + key.replace(".", "-")
            lines.append(f"  {name}: {css_value(node)};")
        elif isinstance(node, dict):
            lines.extend(declarations(node, prefix + key + "-"))
    return lines


core = "\n".join(declarations(T["core"], ""))
light = "\n".join(declarations(T["light"], ""))
dark = "\n".join(declarations(T["dark"], ""))

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Discord style guide</title>
<style>
:root {{
{core}
{light}
  --sg-sans: var(--font-primary);
  --sg-display: var(--font-headline);
}}
[data-mode="dark"] {{
{dark}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 400 16px/1.5 var(--sg-sans); color: var(--text-default, #23272a); background: var(--page, #1a2081); }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; background: #fff; min-height: 100vh; }}
[data-mode="dark"] main {{ background: #1e1f22; color: var(--text-default, #fff); }}
h1 {{ font-family: var(--sg-display); font-weight: 700; font-size: 40px; line-height: 1; letter-spacing: -0.01em; text-transform: uppercase; margin: 0 0 8px; }}
h2 {{ font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; margin: 40px 0 8px; }}
.note {{ font-size: 14px; max-width: 62ch; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 48px; border-radius: var(--radius-sm); border: 1px solid rgba(0,0,0,.12); }}
.sw b, .sw span {{ display: block; font-size: 11px; font-family: ui-monospace, monospace; }}
button#mode {{ float: right; height: 36px; padding: 0 14px; border-radius: var(--radius-round); border: 0; background: var(--blurple); color: #fff; font: 600 14px var(--sg-sans); }}
</style>
</head>
<body>
<main>
<button id="mode" type="button">Dark</button>
<h1>Discord</h1>
<p class="note">Rendered from tokens.json. Swatches use the measured custom properties. A value stored as color-mix or hsl is painted as that string. The dark toggle applies the .theme-dark probe values. Marketing pages paint light.</p>
<h2>Brand</h2>
<div class="swatches" id="brand"></div>
<h2>Text and surface</h2>
<div class="swatches" id="roles"></div>
<h2>Type</h2>
<p class="display" style="font-family:var(--font-headline);font-size:56px;font-weight:700;line-height:48px;letter-spacing:-0.56px;text-transform:uppercase">Group chat</p>
<p class="note">Display size, weight, line height and letter spacing are the measured home h1. Body size was not captured.</p>
</main>
<script>
const root = document.documentElement;
const names = ["--blurple","--not-quite-black","--off-white","--greyple","--white","--black","--text-link","--themeColor","--page","--accent","--text-default","--text-muted","--background-accent","--background-scrim","--status-positive","--status-danger","--status-warning","--border-normal"];
function paint(id, list) {{
  const box = document.getElementById(id);
  box.innerHTML = "";
  for (const name of list) {{
    const v = getComputedStyle(root).getPropertyValue(name).trim();
    if (!v) continue;
    const el = document.createElement("div");
    el.className = "sw";
    el.innerHTML = "<i></i><b></b><span></span>";
    el.querySelector("i").style.background = v;
    el.querySelector("b").textContent = name;
    el.querySelector("span").textContent = v.slice(0, 42);
    box.appendChild(el);
  }}
}}
function draw() {{
  paint("brand", ["--blurple","--not-quite-black","--off-white","--greyple","--white","--black","--text-link","--themeColor","--page","--accent"]);
  paint("roles", ["--text-default","--text-muted","--text-strong","--background-accent","--background-scrim","--status-positive","--status-danger","--status-warning","--border-normal"]);
}}
document.getElementById("mode").onclick = () => {{
  const on = root.getAttribute("data-mode") === "dark";
  root.toggleAttribute ? null : null;
  if (on) root.removeAttribute("data-mode"); else root.setAttribute("data-mode", "dark");
  document.getElementById("mode").textContent = on ? "Dark" : "Light";
  draw();
}};
draw();
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
