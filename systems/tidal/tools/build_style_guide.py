#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Specimens use tokens only."""
import html
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def css_name(path):
    return "--" + "-".join(path)


def css_value(value):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return "var(" + css_name(value[1:-1].split(".")) + ")"
    if isinstance(value, list):
        return "cubic-bezier(" + ", ".join(str(v) for v in value) + ")"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return str(value)


def declarations(group):
    lines = []
    for path, token in walk(TOKENS[group]):
        if token["$type"] in ("color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier"):
            lines.append(f"  {css_name(path)}: {css_value(token['$value'])};")
    return "\n".join(lines)


def rows(group, prefix):
    out = []
    for path, token in walk(TOKENS[group]):
        if path[:1] != (prefix,):
            continue
        name = ".".join(path)
        value = token["$value"]
        shown = value if not isinstance(value, list) else "cubic-bezier(" + ", ".join(str(v) for v in value) + ")"
        swatch = ""
        if token["$type"] == "color":
            swatch = f'<i style="background:{css_value(value)}"></i>'
        out.append(
            f"<tr><td>{html.escape(name)}</td><td>{swatch}</td>"
            f"<td><code>{html.escape(str(shown))}</code></td>"
            f"<td>{html.escape(token['$extensions']['source']['evidence'])}</td></tr>"
        )
    return "\n".join(out)


def main():
    dark = declarations("dark")
    core = declarations("core")
    page = html.escape("TIDAL")
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIDAL style guide</title>
<style>
:root {{
{core}
{dark}
  --sans: var(--font-text);
  --display: var(--font-display);
  --login: var(--font-login);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-bg-page); color: var(--color-text-primary); font: 400 14px/20px var(--sans); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 700 24px/28px var(--sans); margin: 0 0 8px; }}
h2 {{ font: 700 19px/26px var(--display); margin: 40px 0 12px; }}
p {{ color: var(--color-text-secondary); max-width: 68ch; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
td, th {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--color-border-divider); vertical-align: middle; }}
th {{ color: var(--color-text-tertiary); font-weight: 500; }}
td i {{ display: inline-block; width: 28px; height: 28px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--color-border-divider); }}
code {{ font-family: ui-monospace, Menlo, monospace; font-size: 12px; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.pill {{ display: inline-flex; align-items: center; height: var(--component-button-height); padding: 0 var(--component-button-padding); border-radius: var(--component-button-radius); font: 600 14px/22px var(--sans); }}
.primary {{ background: var(--color-button-primaryBg); color: var(--color-button-primaryText); }}
.secondary {{ background: var(--color-button-secondaryBg); color: var(--color-button-secondaryText); }}
.login {{ display: inline-flex; align-items: center; height: var(--component-loginButton-height); padding: 0 var(--component-loginButton-padding); border-radius: var(--component-loginButton-radius); background: var(--color-button-loginBg); color: var(--color-button-loginText); font: 600 16px/24px var(--login); }}
.field {{ display: flex; align-items: center; height: var(--component-field-height); width: 280px; padding: 0 16px; border-radius: var(--component-field-radius); box-shadow: inset 0 0 0 1px var(--color-border-field); color: var(--color-text-secondary); font: 600 16px/24px var(--login); }}
.side {{ width: var(--component-sidebar-width); background: var(--color-bg-sidebar); padding: 16px; }}
.side a {{ display: flex; align-items: center; height: var(--component-sidebar-rowHeight); padding: 0 8px; border-radius: var(--component-sidebar-radius); color: var(--color-text-secondary); text-decoration: none; }}
.side a.on {{ background: var(--color-bg-selected); color: var(--color-text-primary); }}
.note {{ font-size: 12px; line-height: 18px; color: var(--color-text-tertiary); }}
</style>
</head>
<body>
<main>
<h1>{page}</h1>
<p>Signed-out web chrome, measured on 2026-11-19. Specimens use the tokens. Square Sans and Nationale are not loaded here, so the stacks fall through to Helvetica and Arial.</p>
<h2>Controls</h2>
<div class="row">
  <span class="pill primary">Create a free account</span>
  <span class="pill secondary">Log in</span>
  <span class="login">Continue</span>
  <span class="field">Enter your email or login name</span>
</div>
<p class="note">The player pills are 32px with a 1000px radius. The login Continue button is 50px with a 12px radius. The email field wrapper is 54px with a 16px radius and a 1px inset white stroke.</p>
<h2>Sidebar</h2>
<div class="side">
  <a class="on">Music</a>
  <a>Explore</a>
  <a>Playlists</a>
</div>
<h2>Colour</h2>
<table>
<tr><th>Token</th><th></th><th>Value</th><th>Evidence</th></tr>
{rows("dark", "color")}
{rows("core", "color")}
</table>
<h2>Type</h2>
<table>
<tr><th>Token</th><th></th><th>Value</th><th>Evidence</th></tr>
{rows("core", "typography")}
{rows("core", "font")}
{rows("core", "fontWeight")}
</table>
<h2>Radius, space, motion</h2>
<table>
<tr><th>Token</th><th></th><th>Value</th><th>Evidence</th></tr>
{rows("core", "radius")}
{rows("core", "space")}
{rows("core", "motion")}
{rows("dark", "component")}
</table>
</main>
</body>
</html>
"""
    OUT.write_text(doc)
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
