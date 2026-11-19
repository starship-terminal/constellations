#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
T = json.loads((ROOT / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + ".")


def css_name(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(value):
    return re.sub(r"\{([^{}]+)\}", lambda match: f"var({css_name(match.group(1))})", str(value))


def css_value(token):
    value, kind = token["$value"], token["$type"]
    if kind == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(part) for part in value)
    if kind == "shadow" and isinstance(value, dict):
        return f'{value["offsetX"]} {value["offsetY"]} {value["blur"]} {value["spread"]} {value["color"]}'
    if kind == "typography":
        return None
    return alias(value)


def block(name, node):
    lines = []
    for path, token in flat(node):
        value = css_value(token)
        if value is None:
            continue
        lines.append(f"  {css_name(name + '.' + path)}: {value};")
    return "\n".join(lines)


def swatches(theme):
    roles = ["page", "surface", "text", "muted", "accent", "border", "button", "button-text", "critical"]
    cells = []
    for role in roles:
        cells.append(
            f'<div class="swatch"><i style="background:var(--{theme}-{role})"></i><span>{role}</span>'
            f'<code>var(--{theme}-{role})</code></div>'
        )
    return "\n".join(cells)


html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Retool style guide</title>
<style>
:root {{
{block("core", T["core"])}
{block("light", T["light"])}
  color-scheme: light;
  --page: var(--light-page);
  --surface: var(--light-surface);
  --text: var(--light-text);
  --muted: var(--light-muted);
  --accent: var(--light-accent);
  --border: var(--light-border);
  --button: var(--light-button);
  --button-text: var(--light-button-text);
}}
[data-mode="dark"] {{
{block("dark", T["dark"])}
  color-scheme: dark;
  --page: var(--dark-page);
  --surface: var(--dark-surface);
  --text: var(--dark-text);
  --muted: var(--dark-muted);
  --accent: var(--dark-accent);
  --border: var(--dark-border);
  --button: var(--dark-button);
  --button-text: var(--dark-button-text);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px Inter, ui-sans-serif, system-ui, sans-serif; }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
header {{ display: flex; justify-content: space-between; gap: 16px; align-items: center; }}
h1 {{ font: 300 40px/44px ui-sans-serif, system-ui, sans-serif; letter-spacing: -0.02em; margin: 0; }}
h2 {{ font: 380 22px/28px ui-sans-serif, system-ui, sans-serif; margin: 40px 0 12px; }}
p {{ max-width: 72ch; color: var(--muted); }}
button.theme {{ background: transparent; color: var(--text); border: 1px solid var(--border); border-radius: 9999px; height: 40px; padding: 0 20px; cursor: pointer; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.swatch {{ width: 140px; }}
.swatch i {{ display: block; height: 64px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--border); }}
.swatch span, .swatch code {{ display: block; font-size: 12px; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: 40px; padding: 0 20px; border-radius: 9999px; background: var(--button); color: var(--button-text); text-decoration: none; font-size: 13px; }}
.btn.line {{ background: transparent; color: var(--text); border: 1px solid #8b867f; }}
.field {{ display: block; width: 320px; height: 40px; padding: 0 16px; border: 0; border-radius: 8px; background: #f7f8f4; color: #151515; }}
.field:focus {{ outline: 2px solid #518dd2; outline-offset: 2px; }}
.card {{ border: 1px solid var(--border); border-radius: 12px; padding: 24px; max-width: 360px; }}
code {{ font-size: 12px; }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>Retool</h1>
  <button class="theme" type="button" id="theme">Theme</button>
</header>
<p>Values from computed styles on retool.com, login.retool.com and docs.retool.com, 2026-11-19. Saans and PX Grotesk are not loaded here. The light set is the class probe, not a painted marketing theme.</p>
<h2>Semantic</h2>
<div class="row" id="swatches">{swatches("dark")}</div>
<h2>Controls</h2>
<div class="row">
  <a class="btn" href="#buttons">Start for free</a>
  <a class="btn line" href="#buttons">Book a demo</a>
</div>
<h2>Login field</h2>
<input class="field" placeholder="name@company.com" aria-label="Email">
<h2>Pricing card</h2>
<div class="card">
  <strong>Free</strong>
  <p>AI credits per month</p>
  <a class="btn" href="#card">Get started for free</a>
</div>
</div>
<script>
const root = document.documentElement;
const button = document.getElementById("theme");
function paint() {{
  const mode = root.getAttribute("data-mode");
  button.textContent = mode === "dark" ? "Dark" : "Light";
  document.getElementById("swatches").innerHTML = `{swatches("dark")}`.replaceAll("dark-", mode + "-").replaceAll("var(--dark-", "var(--" + mode + "-");
}}
button.addEventListener("click", () => {{
  root.setAttribute("data-mode", root.getAttribute("data-mode") === "dark" ? "light" : "dark");
  paint();
}});
paint();
</script>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
