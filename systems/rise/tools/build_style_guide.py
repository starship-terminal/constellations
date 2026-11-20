#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light only. Rise does not publish a dark theme, so the toggle stays off.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}{key}"
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path + ".")


def css_name(path):
    return "--" + path.replace(".", "-")


def alias(value):
    if not isinstance(value, str):
        return value
    out = value
    while "{" in out:
        start = out.index("{")
        end = out.index("}", start)
        out = out[:start] + f"var({css_name(out[start+1:end])})" + out[end+1:]
    return out


def css_value(token):
    value, kind = token["$value"], token["$type"]
    if kind == "color":
        return alias(value)
    if kind == "dimension":
        return value
    if kind == "number":
        return str(value)
    if kind == "fontFamily":
        return value
    if kind == "fontWeight":
        return str(value)
    if kind == "duration":
        return value
    if kind == "cubicBezier":
        return "cubic-bezier(" + ", ".join(str(part) for part in value) + ")"
    if kind == "shadow":
        return f'{value["offsetX"]} {value["offsetY"]} {value["blur"]} {value["spread"]} {alias(value["color"])}'
    if kind == "typography":
        return None
    return None


def block(set_name):
    lines = []
    for path, token in walk(T[set_name]):
        value = css_value(token)
        if value is None:
            continue
        lines.append(f"  {css_name(path)}: {value};")
    return "\n".join(lines)


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rise style guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
/*LIGHT*/
  color-scheme: light;
  --sg-sans: Inter, ui-sans-serif, system-ui, sans-serif;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/24px var(--sg-sans); }
.wrap { max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }
h1 { font: 700 36px/40px var(--sg-sans); letter-spacing: -1.8px; margin: 0 0 8px; }
h2 { font: 600 24px/32px var(--sg-sans); margin: 40px 0 12px; }
p { color: var(--text-secondary); margin: 0 0 16px; max-width: 68ch; }
code { font-size: 13px; }
.swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }
.sw { display: flex; gap: 10px; align-items: center; }
.sw i { width: 36px; height: 36px; border-radius: 4px; box-shadow: inset 0 0 0 1px var(--border-default); display: block; }
.sw b { display: block; font-size: 12px; font-weight: 600; }
.sw span { display: block; font-size: 12px; color: var(--text-secondary); }
.row { display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid var(--border-default); align-items: baseline; }
.row small { display: block; color: var(--text-secondary); font-weight: 400; }
.btn { display: inline-flex; align-items: center; justify-content: center; height: 34px; padding: 8px 16px; border-radius: 4px; font: 500 14px/16px var(--sg-sans); text-decoration: none; border: 1px solid transparent; }
.btn.primary { background: var(--component-button-primary-bg); color: var(--component-button-primary-text); }
.btn.primary:hover { background: var(--background-primary-hover); }
.btn.secondary { background: var(--component-button-secondary-bg); color: var(--component-button-secondary-text); border-color: var(--border-default); }
.btn.secondary:hover { background: var(--background-input); }
.badge { display: inline-flex; padding: 2px 8px; border: 1px solid var(--border-default); border-radius: 4px; color: var(--text-secondary); font: 600 10px/15px var(--sg-sans); letter-spacing: 0.5px; text-transform: uppercase; }
.cards { display: flex; gap: 16px; flex-wrap: wrap; }
.card { width: 280px; padding: 36px; border-radius: 6px; border: 1px solid var(--border-quiet); background: var(--background-canvas); }
.card.raised { background: var(--background-white); border-color: var(--border-default); box-shadow: var(--shadow-sm); }
.card h3 { margin: 0 0 8px; font: 600 24px/32px var(--sg-sans); }
.note { font-size: 13px; color: var(--text-secondary); }
</style>
</head>
<body>
<div class="wrap">
  <h1>Rise</h1>
  <p>Public marketing site, measured 2026-11-19. One light theme. The signed-in calendar was already shut down, so these specimens are the marketing controls, not the app.</p>

  <h2>Colour</h2>
  <div class="swatches" id="swatches"></div>

  <h2>Type</h2>
  <div class="row"><div>Display<small>48 / 48, -2.4px, 700</small></div><div style="font:700 48px/48px var(--sg-sans);letter-spacing:-2.4px">Sunsetting Rise</div></div>
  <div class="row"><div>Title<small>36 / 40, -1.8px, 700</small></div><div style="font:700 36px/40px var(--sg-sans);letter-spacing:-1.8px">Pricing</div></div>
  <div class="row"><div>Heading<small>24 / 32, 600</small></div><div style="font:600 24px/32px var(--sg-sans)">Solo</div></div>
  <div class="row"><div>Lede<small>20 / 28, offset-dark</small></div><div style="font:400 20px/28px var(--sg-sans);color:var(--text-secondary)">Free for personal use or ready and equipped for your team.</div></div>
  <div class="row"><div>Body<small>16 / 28, foreground at 80%</small></div><div style="font:400 16px/28px var(--sg-sans);color:var(--text-body)">Projects, tasks and time, in one column of Inter.</div></div>
  <div class="row"><div>Eyebrow<small>10px, 600, +0.5px</small></div><div><span class="badge">Announcement</span></div></div>

  <h2>Controls</h2>
  <p><a class="btn primary" href="#components">Upgrade</a> <a class="btn secondary" href="#components">Get Started</a></p>
  <p class="note">Primary hover is primary at 80%. Secondary hover is the input fill, rgb(241, 242, 248). Radius is 4px. Height is 34px.</p>

  <h2>Cards</h2>
  <div class="cards">
    <div class="card"><h3>Solo</h3><p>Quiet card. Background token, border at 50%.</p></div>
    <div class="card raised"><h3>Teams</h3><p>White card, full border, shadow-sm.</p></div>
  </div>
</div>
<script>
const box = document.getElementById("swatches");
const names = ["background-page","background-canvas","background-surface","background-input","background-primary","text-primary","text-secondary","text-link","border-default"];
for (const name of names) {
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = "<i></i><div><b></b><span></span></div>";
  el.querySelector("i").style.background = "var(--" + name + ")";
  el.querySelector("b").textContent = name;
  el.querySelector("span").textContent = getComputedStyle(document.documentElement).getPropertyValue("--" + name).trim();
  box.appendChild(el);
}
</script>
</body>
</html>
"""


def main():
    # The swatches read the custom properties, so no copy of the token tree is inlined (the old one was
    # unused, and unescaped inside <script>).
    html = HTML.replace("/*LIGHT*/", block("core") + "\n" + block("light"))
    (HERE / "style-guide.html").write_text(html)
    print("style-guide.html", len(html.encode()), "bytes")


if __name__ == "__main__":
    main()
