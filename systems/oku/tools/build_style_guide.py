#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The kit template names Butter's token paths. This copy renders Oku's measured
roles with a light/dark toggle. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def css_block(tree, prefix=""):
    lines = []
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}{k}"
        if isinstance(v, dict) and "$value" in v:
            val = v["$value"]
            if v["$type"] == "shadow" and isinstance(val, dict):
                val = f'{val["offsetX"]} {val["offsetY"]} {val["blur"]} {val["spread"]} {val["color"]}'
            name = "--" + path.replace(".", "-")
            lines.append(f"  {name}: {val};")
        elif isinstance(v, dict):
            lines.extend(css_block(v, path + "-"))
    return lines


core = "\n".join(css_block(T["core"]))
light = "\n".join(css_block(T["light"]))
dark = "\n".join(css_block(T["dark"]))

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Oku style guide</title>
<style>
:root {{
{core}
{light}
  --page: var(--color-page);
  --text: var(--color-text);
  --accent: var(--color-accent);
  --on: var(--color-on-accent);
  --surface: var(--color-page);
  --border: var(--color-border);
}}
[data-mode="dark"] {{
{dark}
  --page: var(--color-page);
  --text: var(--color-text);
  --accent: var(--color-accent);
  --on: var(--color-on-accent);
  --surface: var(--color-page);
  --border: var(--color-field-border);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.5 var(--font-family-body); }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 400 48px/1.3 var(--font-family-display); letter-spacing: -0.288px; margin: 0 0 8px; }}
h2 {{ font: 500 13px/1 var(--font-family-body); letter-spacing: 0.08em; text-transform: uppercase; margin: 40px 0 12px; }}
button.theme {{ float: right; height: 40px; padding: 0 24px; border-radius: 8px; border: 0; background: var(--accent); color: var(--on); font: 500 14px/40px var(--font-family-body); }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 48px; border-radius: 8px; border: 1px solid var(--border); }}
.sw span {{ display: block; font: 12px/1.4 ui-monospace, Menlo, monospace; margin-top: 4px; }}
.btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 24px; border-radius: 8px; background: var(--accent); color: var(--on); font: 500 14px/40px var(--font-family-body); box-shadow: var(--shadow-button); }}
.ghost {{ background: var(--page); color: var(--text); box-shadow: inset 0 0 0 1px var(--border); }}
.field {{ display: block; width: 280px; height: 46px; margin-top: 8px; padding: 0 16px; border-radius: 8px; border: 1px solid var(--color-field-border); background: var(--page); color: var(--text); font: 14px var(--font-family-body); }}
.dialog {{ width: 320px; padding: 24px; border-radius: 20px; background: var(--page); border: 1px solid var(--border); }}
.note {{ max-width: 62ch; opacity: 0.75; }}
</style>
</head>
<body>
<main>
<button class="theme" type="button" id="theme">Dark</button>
<h1>Oku</h1>
<p class="note">Public surface, measured 2026-11-21. Values come from tokens.json. The signed-in library was not captured.</p>
<h2>Colour</h2>
<div class="row" id="swatches"></div>
<h2>Type</h2>
<p style="font: 400 48px/1.3 var(--font-family-display); letter-spacing: -0.288px; margin: 0;">The companion app for every book</p>
<p style="font: 400 24px/1.3 var(--font-family-display);">Book title</p>
<p>Body at 16px Inter. Nav at 16px. Buttons at 14px medium.</p>
<h2>Controls</h2>
<p><span class="btn">Join</span> <span class="btn ghost">Sign in</span></p>
<label>Email address<input class="field" placeholder="" readonly></label>
<h2>Dialog</h2>
<div class="dialog">
  <p style="font: 400 20px/1.3 var(--font-family-display); text-align: center;">Join our book community</p>
  <label>Email address<input class="field" readonly></label>
  <p><span class="btn">Create a free account</span></p>
</div>
</main>
<script>
const tokens = {json.dumps({"light": T["light"]["color"], "dark": T["dark"]["color"]})};
const root = document.documentElement;
const btn = document.getElementById("theme");
function paint() {{
  const mode = root.getAttribute("data-mode");
  const box = document.getElementById("swatches");
  box.innerHTML = "";
  for (const [name, token] of Object.entries(tokens[mode])) {{
    const el = document.createElement("div");
    el.className = "sw";
    el.innerHTML = "<i></i><span></span>";
    el.querySelector("i").style.background = token.$value;
    el.querySelector("span").textContent = name + " " + token.$value;
    box.appendChild(el);
  }}
  btn.textContent = mode === "dark" ? "Light" : "Dark";
}}
btn.addEventListener("click", () => {{
  root.setAttribute("data-mode", root.getAttribute("data-mode") === "dark" ? "light" : "dark");
  paint();
}});
paint();
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
