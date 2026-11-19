#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light only. Promova paints one theme: a black page with white and pastel
islands. The guide uses the token values and does not invent a dark set.
"""
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
        return (
            f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} '
            f'{alias(v["fontFamily"])}'
        )
    return alias(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


swatches = [
    ("page", "light.background.page", "#000000"),
    ("surface", "light.background.surface", "#ffffff"),
    ("hero", "light.background.hero", "#bec8ff"),
    ("action", "light.background.action", "#000000"),
    ("announcement", "light.background.announcement", "#fff584"),
    ("field border", "light.border.stroke", "rgba(0, 0, 0, 0.3)"),
]

rows = "\n".join(
    f'<div class="sw"><i style="background:{alias("{" + path + "}")}"></i><div><b>{name}</b><code>{path}</code></div></div>'
    for name, path, _ in swatches
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Promova style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--background-page);
  color: var(--text-on-action);
  font: 16px/1.45 var(--font-family-ui);
  padding: 24px;
}}
main {{
  max-width: 960px;
  margin: 0 auto;
  background: var(--background-surface);
  color: var(--text-primary);
  border-radius: var(--radius-section);
  padding: 32px;
}}
h1 {{ font-family: var(--font-family-display); font-weight: 700; font-size: 40px; line-height: 1; margin: 0 0 8px; }}
h2 {{ font-family: var(--font-family-display); font-weight: 400; font-size: 24px; margin: 32px 0 12px; }}
p {{ margin: 0 0 16px; }}
.swatches {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }}
.sw {{ display: flex; gap: 10px; align-items: center; }}
.sw i {{ width: 48px; height: 48px; border-radius: 8px; border: 1px solid rgba(0,0,0,.2); display: block; }}
code {{ display: block; font-size: 12px; color: rgba(0,0,0,.55); }}
.hero {{
  background: var(--background-hero);
  border-radius: var(--radius-section);
  padding: 28px;
  margin-top: 16px;
}}
.btn {{
  display: inline-flex; align-items: center; justify-content: center;
  height: var(--component-button-cta-height);
  padding: 0 28px;
  background: var(--background-action);
  color: var(--text-on-action);
  font-family: var(--font-family-display);
  font-size: var(--component-button-cta-font-size);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  border-radius: var(--radius-none);
  border: 0;
}}
.btn-line {{
  display: inline-flex; align-items: center; justify-content: center;
  height: 40px; padding: 0 10px;
  background: var(--background-surface);
  color: var(--text-primary);
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-none);
  font-family: var(--font-family-display);
  font-size: 14px;
  text-transform: uppercase;
}}
.field {{
  display: block; width: 280px; height: var(--component-field-height);
  border: 1px solid var(--border-stroke);
  border-radius: var(--radius-field);
  padding: 0 var(--spacing-field-pad);
  font: 500 15px/22px var(--font-family-ui);
}}
.row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
</style>
</head>
<body>
<main>
  <h1>Promova</h1>
  <p>Public signed-out surfaces, measured 2026-11-19. One light theme on a black page. Values come from tokens.json.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {rows}
  </div>
  <h2>Hero island</h2>
  <div class="hero">
    <h1 style="font-size:40px">Speak before you're ready</h1>
    <p>Speaking isn't the final step of learning a language.</p>
    <div class="row">
      <span class="btn">Try now</span>
      <span class="btn-line">Sign up</span>
    </div>
  </div>
  <h2>Field</h2>
  <input class="field" placeholder="example@gmail.com" aria-label="Email example">
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
