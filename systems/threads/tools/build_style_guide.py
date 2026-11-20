#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Self-contained. No external fonts."""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def css_block(group):
    lines = []
    for name, tok in group.items():
        if not isinstance(tok, dict) or "$value" not in tok:
            continue
        if tok.get("$type") != "color":
            continue
        lines.append(f"  --{name}: {tok['$value']};")
    return "\n".join(lines)


light = css_block(T["light"])
dark = css_block(T["dark"])

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Threads style guide</title>
<style>
:root {{
{light}
  color-scheme: light;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}}
[data-mode="dark"] {{
{dark}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 15px/20px var(--sans); }}
header {{ display: flex; align-items: center; gap: 16px; padding: 16px 24px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--page); }}
h1 {{ font-size: 18px; margin: 0; font-weight: 600; }}
button.theme {{ margin-left: auto; background: var(--accent); color: var(--onAccent); border: 0; border-radius: 10px; height: 34px; padding: 0 14px; font: 600 15px/20px var(--sans); }}
main {{ max-width: 960px; margin: 0 auto; padding: 24px; }}
h2 {{ font-size: 15px; margin: 32px 0 12px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; border: 1px solid var(--border); display: block; }}
.sw b {{ font-size: 12px; }}
.sw span {{ display: block; color: var(--muted); font-size: 11px; }}
.row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin: 8px 0; }}
.pill {{ background: var(--accent); color: var(--onAccent); border-radius: 10px; height: 34px; padding: 0 16px; display: inline-flex; align-items: center; font-weight: 600; }}
.ghost {{ background: var(--secondaryButton); color: var(--text); border-radius: 10px; height: 34px; padding: 0 16px; display: inline-flex; align-items: center; }}
.field {{ height: 55px; border-radius: 18px; border: 1px solid var(--border); padding: 0 16px; display: inline-flex; align-items: center; color: var(--placeholder); min-width: 260px; background: var(--page); }}
.card {{ background: var(--elevated); border: 1px solid var(--border); border-radius: 16px; padding: 16px; max-width: 420px; }}
.card small {{ color: var(--muted); }}
a {{ color: var(--link); }}
.note {{ color: var(--muted); font-size: 13px; max-width: 68ch; }}
</style>
</head>
<body>
<header>
  <h1>Threads</h1>
  <span>Public signed-out capture, 2026-11-21</span>
  <button class="theme" type="button" id="theme">Dark</button>
</header>
<main>
  <p class="note">Values come from declared custom properties on <code>:root</code> and <code>.__fb-dark-mode</code>. The page background follows <code>--page</code>.</p>
  <h2>Colour roles</h2>
  <div class="grid" id="swatches"></div>
  <h2>Controls</h2>
  <div class="row">
    <span class="pill">Log in</span>
    <span class="ghost">Mention</span>
    <span class="field">Username, phone or email</span>
  </div>
  <h2>Card</h2>
  <div class="card">
    <b>threads</b> <small>4h</small>
    <p>A post sits on the elevated surface. Secondary text uses the muted role. <a href="#">A link uses the link role.</a></p>
  </div>
  <p class="note">Dialog radius, icon size, and pressed-button colour were not read. They are not drawn here.</p>
</main>
<script>
const roles = {json.dumps(list(T["light"].keys()))};
const box = document.getElementById("swatches");
for (const name of roles) {{
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = "<i style=\\"background:var(--" + name + ")\\"></i><div><b>" + name + "</b><span></span></div>";
  box.appendChild(el);
}}
document.getElementById("theme").onclick = () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light" : "Dark";
}};
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
