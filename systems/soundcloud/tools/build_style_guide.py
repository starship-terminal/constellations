#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The kit template is Claude's. SoundCloud's token names do not match it, so
this builder writes the page itself. Every swatch and specimen uses a custom
property generated from tokens.json.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
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


def block(name):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[name]))


css = f"""
:root {{
{block("core")}
{block("dark")}
  color-scheme: dark;
  --sg-sans: var(--core-fontFamily-soehne);
}}
[data-mode="light"] {{
{block("light")}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--dark-color-page); color: var(--dark-color-text); font: 400 14px/20px var(--sg-sans); }}
[data-mode="light"] body {{ background: var(--light-color-page); color: var(--light-color-text); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
header {{ display: flex; justify-content: space-between; align-items: center; gap: 16px; }}
h1 {{ font: 600 28px/36px var(--sg-sans); margin: 0; }}
h2 {{ font: 600 22px/28px var(--sg-sans); margin: 40px 0 12px; }}
p {{ max-width: 70ch; color: var(--dark-color-muted); }}
[data-mode="light"] p {{ color: var(--light-color-muted); }}
button.theme {{ background: var(--dark-color-button); color: var(--dark-color-onAccent); border: 0; border-radius: var(--core-radius-pill); height: var(--core-size-button); padding: 6px 12px; font: 600 14px/20px var(--sg-sans); cursor: pointer; }}
[data-mode="light"] button.theme {{ background: var(--light-color-button); color: var(--light-color-onAccent); border-radius: var(--core-radius-mobileControl); }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 36px 1fr; gap: 8px; align-items: center; }}
.sw i {{ width: 36px; height: 36px; border-radius: 4px; box-shadow: inset 0 0 0 1px rgba(128,128,128,.4); }}
.sw b {{ font-size: 12px; }}
.sw span {{ display: block; font-size: 11px; opacity: .7; }}
.row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin: 12px 0; }}
.pill {{ height: var(--dark-component-button-height); padding: 6px 12px; border: 0; border-radius: var(--dark-component-button-radius); background: var(--dark-component-button-bg); color: var(--dark-component-button-text); font: 600 14px/20px var(--sg-sans); }}
[data-mode="light"] .pill {{ height: var(--light-component-button-height); border-radius: var(--light-component-button-radius); background: var(--light-component-button-bg); color: var(--light-component-button-text); font-weight: 400; }}
.quiet {{ background: transparent; color: var(--dark-color-text); }}
[data-mode="light"] .quiet {{ color: var(--light-color-text); }}
.field {{ height: var(--dark-component-field-height); width: 280px; border-radius: var(--dark-component-field-radius); background: var(--dark-component-field-bg); color: var(--dark-component-field-text); border: 1px solid transparent; padding: 8px 16px; font: 400 14px/20px var(--sg-sans); }}
[data-mode="light"] .field {{ height: var(--light-component-field-height); border-radius: var(--light-component-field-radius); background: var(--light-component-field-bg); color: var(--light-component-field-text); border-color: var(--light-color-border); }}
.field:focus {{ outline: none; box-shadow: inset 0 0 0 var(--core-size-focus) var(--dark-color-focus); }}
a.sample {{ color: var(--dark-color-link); }}
[data-mode="light"] a.sample {{ color: var(--light-color-link); }}
.card {{ background: var(--dark-color-surface); border-radius: 4px; padding: 16px; max-width: 360px; }}
[data-mode="light"] .card {{ background: var(--light-color-surface); box-shadow: inset 0 0 0 1px var(--light-color-border); }}
.note {{ font-size: 12px; }}
"""

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SoundCloud style guide</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>SoundCloud</h1>
  <button class="theme" type="button" id="theme">Light shell</button>
</header>
<p>Public capture, 2026-11-21. Dark is the signed-out desktop player. Light is the phone shell at m.soundcloud.com plus the Help Center orange. Values come from tokens.json.</p>
<h2>Colour</h2>
<div class="swatches" id="swatches"></div>
<h2>Type</h2>
<p style="font: var(--core-typography-display); color: inherit;">Discover. Get discovered.</p>
<p style="font: var(--core-typography-title); color: inherit;">Discover tracks and playlists</p>
<p style="font: var(--core-typography-body); color: inherit;">Body at 14px on 20px, Söhne with a system fallback.</p>
<h2>Controls</h2>
<div class="row">
  <button class="pill" type="button">Create account</button>
  <button class="pill quiet" type="button">Sign in</button>
  <input class="field" placeholder="Search for artists, bands, tracks, podcasts" aria-label="Search">
  <a class="sample" href="#colour">Learn more</a>
</div>
<div class="card">
  <strong>Create an account or sign in</strong>
  <p class="note">The real dialog is an iframe from secure.soundcloud.com. This card only shows the surface colour.</p>
</div>
<p class="note">Focus on the field uses the measured 2px inset blue. Hover on the real Create account button fades the label to 40% and does not change the fill. That opacity is listed under notTokenised.</p>
</div>
<script>
const tokens = {json.dumps({"dark": {k: v["$value"] if isinstance(v, dict) and "$value" in v else None for k, v in []}, "note": "swatches are CSS variables"})};
const roles = ["page", "surface", "text", "muted", "accent", "link", "border", "button", "onAccent", "focus"];
const box = document.getElementById("swatches");
for (const role of roles) {{
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = '<i></i><div><b>' + role + '</b><span></span></div>';
  el.querySelector("i").style.background = "var(--dark-color-" + role + ")";
  box.appendChild(el);
}}
document.getElementById("theme").addEventListener("click", () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light shell" : "Dark player";
  for (const sw of box.querySelectorAll(".sw")) {{
    const role = sw.querySelector("b").textContent;
    sw.querySelector("i").style.background = "var(--" + next + "-color-" + role + ")";
  }}
}});
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
