#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Sunsama's public site is light. The guide still has a theme toggle because
the public CSS declares a dark app-demo set on .sslab[data-theme=dark].
Marketing colours do not change. Deterministic.
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


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "shadow" and isinstance(v, dict):
        return f'{v["offsetX"]} {v["offsetY"]} {v["blur"]} {v["spread"]} {v["color"]}'
    return str(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


def swatches(setname, prefix):
    rows = []
    for n, t in flat(T[setname]):
        if t["$type"] != "color":
            continue
        if prefix and not n.startswith(prefix):
            continue
        rows.append(
            f'<div class="sw"><i style="background:{t["$value"]}"></i>'
            f'<div><code>{n}</code><span>{t["$value"]}</span></div></div>'
        )
    return "\n".join(rows)


html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sunsama style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --sg-sans: "DM Sans", Avenir, ui-sans-serif, system-ui, sans-serif;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 15px/1.45 var(--sg-sans); }}
header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-size: 22px; margin: 0; }}
h2 {{ font-size: 18px; margin: 36px 0 12px; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
.sw {{ display: grid; grid-template-columns: 36px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--border); display: block; }}
code {{ font-size: 12px; }}
.sw span {{ display: block; color: var(--muted); font-size: 12px; }}
button.theme {{ border: 1px solid var(--border); background: var(--surface); color: var(--text); border-radius: 999px; padding: 8px 14px; }}
.specimen {{ display: flex; gap: 12px; align-items: center; margin: 12px 0; }}
.pill {{ background: var(--accent); color: #fff; border: 0; border-radius: 999px; padding: 10px 18px; font: 600 15px var(--sg-sans); }}
.card {{ background: var(--app-page); color: var(--app-text); border: 1px solid var(--app-border); border-radius: var(--size-radius); padding: 16px; max-width: 360px; box-shadow: var(--elevation-card); }}
.note {{ color: var(--muted); max-width: 70ch; }}
</style>
</head>
<body>
<header>
  <h1>Sunsama</h1>
  <button class="theme" type="button" id="theme">Dark app tokens</button>
</header>
<main>
  <p class="note">Rendered from tokens.json. Marketing colours stay on :root. The toggle swaps the app-demo colours declared on .sslab[data-theme=dark]. The public marketing pages do not paint that attribute.</p>
  <h2>Marketing colours</h2>
  <div class="swatches">
{swatches("light", "")}
  </div>
  <h2>App demo colours</h2>
  <div class="swatches">
{swatches("light", "app-")}
  </div>
  <h2>Specimens</h2>
  <div class="specimen"><button class="pill" type="button">Start for Free</button><span class="note">Orange pill, 44px, full radius. The only filled marketing action.</span></div>
  <div class="card">
    <strong>Monday</strong>
    <p>App demo card. Radius 4px. Text uses the .sslab colour, which changes with the toggle.</p>
  </div>
</main>
<script>
document.getElementById("theme").addEventListener("click", () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light app tokens" : "Dark app tokens";
}});
</script>
</body>
</html>
"""
# The swatches() call above used light only. Rebuild app swatches so the toggle
# can show dark by reading CSS variables instead of baked light values.
html = html.replace(swatches("light", "app-"), """<div class="sw"><i style="background:var(--app-page)"></i><div><code>app.page</code><span>var(--app-page)</span></div></div>
<div class="sw"><i style="background:var(--app-text)"></i><div><code>app.text</code><span>var(--app-text)</span></div></div>
<div class="sw"><i style="background:var(--app-accent)"></i><div><code>app.accent</code><span>var(--app-accent)</span></div></div>
<div class="sw"><i style="background:var(--app-success)"></i><div><code>app.success</code><span>var(--app-success)</span></div></div>
<div class="sw"><i style="background:var(--app-danger)"></i><div><code>app.danger</code><span>var(--app-danger)</span></div></div>
<div class="sw"><i style="background:var(--app-warning)"></i><div><code>app.warning</code><span>var(--app-warning)</span></div></div>
<div class="sw"><i style="background:var(--app-border)"></i><div><code>app.border</code><span>var(--app-border)</span></div></div>""")
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
