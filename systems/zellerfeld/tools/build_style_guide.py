#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + "-")


def css_name(path):
    return "--" + path.replace(".", "-")


def alias(value):
    text = str(value)
    while "{" in text:
        start = text.find("{")
        end = text.find("}", start)
        if end < 0:
            break
        text = text[:start] + f"var({css_name(text[start + 1:end])})" + text[end + 1:]
    return text


def css_block(group):
    lines = []
    for path, token in flat(T[group]):
        value = token["$value"]
        kind = token.get("$type")
        if kind == "typography":
            continue
        if kind == "shadow" and not isinstance(value, str):
            continue
        lines.append(f"  {css_name(path)}: {alias(value)};")
    return "\n".join(lines)


DARK = css_block("dark")
CORE = css_block("core")

swatches = []
for path, token in flat(T["dark"]):
    if token.get("$type") != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{alias(token["$value"])}"></i>'
        f"<span><code>{path}</code><small>{alias(token['$value'])}</small></span></div>"
    )

type_rows = []
for path, token in flat(T["core"]):
    if token.get("$type") != "typography":
        continue
    value = token["$value"]
    type_rows.append(
        "<tr><td><code>{path}</code></td><td style=\"font-family:{family};font-size:{size};"
        "font-weight:{weight};line-height:{line};letter-spacing:{tracking};color:#fff\">"
        "Printed shoes</td><td>{size} / {weight}</td></tr>".format(
            path=path,
            family=alias(value["fontFamily"]),
            size=value["fontSize"],
            weight=value["fontWeight"],
            line=value["lineHeight"],
            tracking=value["letterSpacing"],
        )
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zellerfeld style guide</title>
<style>
:root {{
{CORE}
{DARK}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px Exposure, ui-sans-serif, system-ui, sans-serif; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 40px 24px 80px; }}
h1 {{ font-family: "Lateral Zeller TM", Lateral, ui-sans-serif, system-ui, sans-serif; font-size: 32px; line-height: 28px; margin: 0 0 8px; }}
h2 {{ font-size: 18px; margin: 40px 0 12px; }}
p {{ color: var(--text-muted); max-width: 68ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: flex; gap: 12px; align-items: center; }}
.sw i {{ width: 44px; height: 44px; border-radius: 4px; box-shadow: inset 0 0 0 1px #ffffff33; display: block; }}
.sw code {{ display: block; font-size: 12px; }}
.sw small {{ color: var(--text-muted); font-size: 12px; }}
table {{ width: 100%; border-collapse: collapse; }}
td {{ border-bottom: 1px solid #ffffff1a; padding: 10px 8px; vertical-align: baseline; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 16px; border-radius: 4px; font-family: Phonic, ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; letter-spacing: -0.01em; text-transform: uppercase; text-decoration: none; }}
.btn.primary {{ background: var(--accent); color: var(--accent-foreground); border: 0; }}
.btn.outline {{ background: transparent; color: var(--accent); border: 1px solid var(--accent); }}
.btn.ghost {{ background: var(--muted); color: var(--text); border: 0; }}
.card {{ background: var(--signin-card); color: var(--signin-ink); border-radius: 8px; padding: 24px; max-width: 402px; }}
.card h3 {{ margin: 0 0 8px; font-size: 20px; }}
.field {{ display: block; width: 100%; height: 40px; border-radius: 6px; border: 1px solid #e0e0e0; padding: 8px 16px; font-family: Phonic, ui-monospace, monospace; }}
</style>
</head>
<body>
<main>
<h1>Zellerfeld</h1>
<p>Public signed-out surfaces measured on 2026-11-19. One theme: dark. The store paints black; the published semantic background is #171717.</p>
<h2>Colour</h2>
<div class="swatches">{''.join(swatches)}</div>
<h2>Type</h2>
<table>{''.join(type_rows)}</table>
<h2>Buttons</h2>
<div class="row">
  <a class="btn outline">Create</a>
  <button class="btn ghost">Sign in</button>
  <a class="btn primary">Start onboarding</a>
</div>
<h2>Sign-in card</h2>
<div class="card">
  <h3>Sign in</h3>
  <p style="color:#171717">Welcome back. The phone control was not used.</p>
  <input class="field" placeholder="Enter your email address" readonly>
</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
