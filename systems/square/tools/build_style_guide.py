#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light is the live homepage theme.
Dark values are the declared color-mode-dark custom properties."""
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
    if ty == "typography":
        return f'{v["fontWeight"]} {alias(v["fontSize"])}/{v["lineHeight"]} {alias(v["fontFamily"])}'
    if isinstance(v, (int, float)):
        return str(v)
    return alias(v)


def block(name):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[name]))


swatches = []
for role, tok in T["light"].items():
    swatches.append(
        f'<div class="sw"><i style="background:{tok["$value"]}"></i><b>{role}</b><code>{tok["$value"]}</code></div>'
    )

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Square style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --sg-sans: "Square Sans Text VF", "Square Sans Text", Helvetica, Arial, sans-serif;
  --sg-display: "Square Sans Display VF", "Square Sans Display", Helvetica, Arial, sans-serif;
  --sg-serif: "Exact Block", Georgia, "Times New Roman", serif;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px var(--sg-sans); }}
header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 28px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--surface); }}
header h1 {{ margin: 0; font: 400 20px/28px var(--sg-display); }}
button.theme {{ border: 1px solid var(--border); background: var(--surface); color: var(--text); border-radius: 24px; padding: 8px 16px; font: inherit; cursor: pointer; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 28px 80px; }}
h2 {{ font: 400 32px/38px var(--sg-serif); margin: 40px 0 12px; }}
p.note {{ color: var(--muted); max-width: 68ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
.sw {{ border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: var(--surface); }}
.sw i {{ display: block; height: 64px; }}
.sw b, .sw code {{ display: block; padding: 6px 10px 0; font-size: 13px; }}
.sw code {{ padding-bottom: 10px; color: var(--muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.btn {{ display: inline-flex; align-items: center; height: 44px; padding: 0 18px; border-radius: 50px; background: var(--accent); color: var(--onAccent); text-decoration: none; font-weight: 500; }}
.btn.quiet {{ background: transparent; color: var(--text); border: 1px solid var(--border); }}
.field {{ height: 48px; border-radius: 8px; border: 1px solid var(--border); padding: 0 14px; background: var(--surface); color: var(--text); min-width: 240px; font: inherit; }}
.card {{ border: 1px solid var(--border); border-radius: 16px; padding: 20px; max-width: 280px; background: var(--surface); }}
.card strong {{ display: block; font: 400 22px/28px var(--sg-display); }}
footer.fake {{ margin-top: 28px; background: var(--accent); color: var(--onAccent); padding: 20px; border-radius: 12px; }}
</style>
</head>
<body>
<header>
  <h1>Square</h1>
  <button class="theme" type="button" id="theme">Dark tokens</button>
</header>
<main>
  <p class="note">Values from Square's public design-system custom properties on squareup.com, measured 2026-11-21. The live marketing site paints light. Dark is the declared <code>data-color-mode=dark</code> set, not a captured dark page.</p>
  <h2>Colour roles</h2>
  <div class="swatches">
    {''.join(swatches)}
  </div>
  <h2>Type</h2>
  <p style="font: 400 64px/1.05 var(--sg-display); letter-spacing: -0.5px; margin: 0;">Local legend or global icon.</p>
  <p style="font: 400 40px/45px var(--sg-serif); letter-spacing: -0.8px;">Whatever your flavor of business.</p>
  <p>Body copy uses Square Sans Text at 16px on 24px. Footer links use the muted grey.</p>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn" href="#roles">Get started</a>
    <a class="btn quiet" href="#roles">Contact sales</a>
  </div>
  <div class="row">
    <input class="field" placeholder="Search" aria-label="Search sample">
  </div>
  <div class="card">
    <strong>Square Plus</strong>
    <p>$49/mo. per location</p>
    <a class="btn" href="#roles">Try free for 30 days</a>
  </div>
  <footer class="fake">Footer band is black ink with white text on the live site.</footer>
</main>
<script>
document.getElementById("theme").onclick = () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light tokens" : "Dark tokens";
}};
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
