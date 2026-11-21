#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    return alias(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


css = block("core") + "\n" + block("light")
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mapbox style guide</title>
<style>
:root {{
{css}
  --sg-sans: "Cera pro", "Trebuchet MS", sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text-primary); font: 400 16px/1.6 var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-size: 2.25rem; line-height: 1.2; letter-spacing: -0.01em; margin: 0 0 8px; }}
h2 {{ font-size: 1.5rem; margin: 40px 0 12px; }}
p {{ color: var(--text-secondary); max-width: 70ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 64px; border-radius: 8px; box-shadow: inset 0 0 0 1px #d5dae2; }}
.sw b, .sw span {{ display: block; font-size: 12px; }}
.sw span {{ color: var(--text-muted); }}
.btn {{ display: inline-flex; align-items: center; height: var(--component-button-height); padding: 0 21px; border-radius: var(--component-button-radius); background: var(--component-button-bg); color: var(--component-button-text); border: 1px solid var(--component-button-bg); text-decoration: none; font-size: 18px; }}
.btn.stroke {{ background: var(--component-button-stroke-bg); color: var(--component-button-stroke-text); border-color: var(--component-button-stroke-border); height: 38px; padding: 0 16px; font-size: 15px; }}
.field {{ height: var(--component-field-height); width: 280px; border-radius: var(--component-field-radius); border: 1px solid var(--component-field-border); padding: 0 12px; font: inherit; color: var(--text-secondary); }}
.field:focus {{ outline: none; border-color: var(--component-field-focus); }}
.card {{ background: var(--surface); border-radius: var(--radius-medium); padding: 24px; max-width: 360px; }}
code {{ font-size: 12px; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Mapbox, measured</h1>
<p>Public marketing site, light theme only, read from mapbox.com on 2026-11-21. Cera Pro is Mapbox's licensed face and is not loaded here. The fallback is Trebuchet MS, which is the stack the site itself declares.</p>
<h2>Colour</h2>
<div class="row" id="roles"></div>
<h2>Blue ramp</h2>
<div class="row" id="blue"></div>
<h2>Gray ramp</h2>
<div class="row" id="gray"></div>
<h2>Controls</h2>
<p><a class="btn" href="#components">Get started for free</a> <a class="btn stroke" href="#components">Get started</a></p>
<p><input class="field" placeholder="How can we help you?" aria-label="Example field"></p>
<div class="card"><b>Pay as you go</b><p>Surface #f7f9fc behind ink #0e1012. Accent stays on the pill.</p></div>
</div>
<script>
const roles = [
  ["page", "--page"], ["surface", "--surface"], ["text", "--text-primary"],
  ["muted", "--text-muted"], ["accent", "--accent-default"], ["border", "--border-default"]
];
const root = getComputedStyle(document.documentElement);
function swatch(name, prop) {{
  const v = root.getPropertyValue(prop).trim();
  return `<div class="sw"><i style="background:${{v}}"></i><b>${{name}}</b><span>${{v}}</span></div>`;
}}
document.getElementById("roles").innerHTML = roles.map(([n,p]) => swatch(n,p)).join("");
function ramp(id, prefix) {{
  const steps = ["5","10","20","30","40","50","60","70","80","90"];
  document.getElementById(id).innerHTML = steps.map(s => swatch(s, prefix+s)).join("");
}}
ramp("blue", "--color-blue-");
ramp("gray", "--color-gray-");
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
