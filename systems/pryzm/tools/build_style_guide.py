#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Edit tokens, then rerun. Never hand-edit the HTML."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())

def css_vars(group):
    lines = []
    for name, tok in tokens[group].items():
        if tok.get("$type") != "color":
            continue
        lines.append(f"  --{name}: {tok['$value']};")
    return "\n".join(lines)

swatches = "\n".join(
    f'<div class="swatch"><i style="background:var(--{name})"></i><span>{name}</span><code>{tokens["dark"][name]["$value"]}</code></div>'
    for name in tokens["dark"]
    if tokens["dark"][name].get("$type") == "color"
)

html = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pryzm style guide</title>
<style>
:root {{
{css_vars("dark")}
  --sans: Inter, ui-sans-serif, system-ui, sans-serif;
  --heading: Poppins, ui-sans-serif, system-ui, sans-serif;
  --mono: "Geist Mono", ui-monospace, monospace;
  color-scheme: dark;
}}
[data-theme="light"] {{
{css_vars("light")}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text-primary); font: 400 14px/1.5 var(--sans); }}
header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border-default); }}
h1 {{ font: 600 20px/1.2 var(--heading); margin: 0; letter-spacing: -0.02em; }}
button.theme {{ background: var(--accent); color: var(--accent-foreground); border: 0; border-radius: 8px; height: 32px; padding: 0 12px; font: 500 12px/1 var(--sans); }}
main {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font: 600 28px/1.15 var(--heading); letter-spacing: -0.02em; margin: 40px 0 12px; }}
p.note {{ color: var(--text-secondary); max-width: 68ch; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.swatch {{ background: var(--surface); border: 1px solid var(--border-default); border-radius: 18px; padding: 12px; }}
.swatch i {{ display: block; height: 48px; border-radius: 8px; border: 1px solid var(--border-default); }}
.swatch span, .swatch code {{ display: block; margin-top: 8px; font-size: 12px; }}
.swatch code {{ color: var(--text-secondary); font-family: var(--mono); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.btn {{ display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: 8px; background: var(--accent); color: var(--accent-foreground); font: 500 12px/1 var(--sans); text-decoration: none; }}
.btn.quiet {{ background: var(--secondary); color: var(--text-primary); }}
.field {{ height: 44px; width: 280px; border-radius: 8px; border: 1px solid var(--border-input); background: var(--page); color: var(--text-primary); padding: 0 12px; font: 400 14px/1 var(--sans); }}
.card {{ width: 220px; background: var(--surface); border-radius: 18px; padding: 12px; }}
.card .art {{ height: 120px; border-radius: 12px; background: linear-gradient(180deg, #ff4d2e, #2a1240); }}
.badge {{ display: inline-flex; height: 16px; padding: 0 6px; border-radius: 999px; background: var(--muted); color: var(--text-primary); font: 600 10px/16px var(--sans); }}
.dialog {{ width: min(420px, 100%); background: var(--surface); border-radius: 18px; padding: 16px; border: 1px solid var(--border-default); }}
</style>
</head>
<body>
<header>
  <h1>Pryzm</h1>
  <button class="theme" type="button" id="theme">Show declared light</button>
</header>
<main>
  <p class="note">Values come from tokens.json. The live public site paints the dark set. The light set is declared on :root and is not what the public pages paint. Hover, focus, pressed, disabled and error states that were not measured are not drawn here.</p>
  <h2>Colour</h2>
  <div class="grid">{swatches}</div>
  <h2>Type</h2>
  <p style="font: 600 48px/1.05 var(--heading); letter-spacing: -0.02em; margin: 0;">Backgrounds nobody else has</p>
  <p>Body is Inter 14px. Labels are Inter 12px / 500. The PRO badge is Inter 10px / 600.</p>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn" href="#controls">Open studio</a>
    <a class="btn quiet" href="#controls">Sign in</a>
    <span class="badge">PRO</span>
  </div>
  <p></p>
  <input class="field" placeholder="Email address" readonly>
  <h2>Card and dialog</h2>
  <div class="row">
    <article class="card"><div class="art"></div><p><span class="badge">PRO</span> Bright Spark</p></article>
    <div class="dialog"><strong>Export</strong><p class="note">Free PNG export is capped at Preview size. This specimen uses measured surface, radius and type. It is not a screenshot.</p><a class="btn" href="#controls">Download PNG</a></div>
  </div>
</main>
<script>
document.getElementById('theme').onclick = () => {{
  const html = document.documentElement;
  const next = html.dataset.theme === 'dark' ? 'light' : 'dark';
  html.dataset.theme = next;
  document.getElementById('theme').textContent = next === 'dark' ? 'Show declared light' : 'Show live dark';
}};
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
