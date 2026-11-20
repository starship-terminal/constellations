#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. ROVR's own template, not the Claude one.

Every colour on the page comes from tokens.json. The page opens on dark, which
is the theme that was on screen.
"""
import json
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


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


def css_value(token):
    value, kind = token["$value"], token["$type"]
    if kind == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(n) for n in value)
    if kind == "typography":
        return None
    if isinstance(value, (dict, list)):
        return None
    # Only an alias's own dots become dashes: 28.8px stays 28.8px (it used to become 28-8px).
    return re.sub(r"\{([^{}]+)\}", lambda m: "var(--" + m.group(1).replace(".", "-") + ")", str(value))


def block(name):
    lines = []
    for path, token in flat(TOKENS[name]):
        value = css_value(token)
        if value is None:
            continue
        lines.append(f"  {css_name(path)}: {value};")
    return "\n".join(lines)


DARK = block("dark")
LIGHT = block("light")
CORE = block("core")

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ROVR style guide</title>
<style>
:root {{
{CORE}
{DARK}
  color-scheme: dark;
  --sans: var(--font-family-kern);
}}
[data-mode="light"] {{
{LIGHT}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-background); color: var(--color-foreground); font: 400 16px/24px var(--sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--color-brand); }}
header h1 {{ margin: 0; font-size: 20px; letter-spacing: 0.8px; text-transform: uppercase; }}
button.theme {{ margin-left: auto; background: var(--color-brand); color: #000; border: 0; border-radius: 30px; padding: 4px 12px; font: italic 700 15px/15px var(--sans); }}
main {{ padding: 24px; max-width: 960px; }}
h2 {{ font-size: 24px; line-height: 32px; font-weight: 800; text-transform: uppercase; }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; margin: 16px 0 32px; }}
.swatch {{ width: 140px; }}
.swatch i {{ display: block; height: 56px; border: 1px solid var(--color-border); }}
.swatch span {{ display: block; font-size: 12px; line-height: 16px; margin-top: 4px; }}
.pill {{ display: inline-flex; align-items: center; justify-content: center; background: var(--color-brand); color: #000; border-radius: 9999px; padding: 7px 12px; font: 700 12px/12px var(--sans); }}
.auth {{ display: flex; align-items: center; justify-content: center; width: 256px; height: 36px; background: #000; color: var(--color-brand); border: 2px solid #000; font: 700 16px/24px var(--sans); letter-spacing: 0.8px; }}
.note {{ color: var(--color-muted-foreground); font-size: 14px; max-width: 68ch; }}
</style>
</head>
<body>
<header>
  <h1>ROVR</h1>
  <button class="theme" type="button" id="theme">Light tokens</button>
</header>
<main>
  <p class="note">Dark is the theme that was on screen (html.dark). Light values are the stylesheet :root block, not a page that was shown. Brand yellow is the painted rgb(255, 240, 87), which is not the same as --primary.</p>
  <h2>Colour</h2>
  <div class="row" id="swatches"></div>
  <h2>Controls</h2>
  <div class="row">
    <span class="pill">Message</span>
    <span class="auth">SIGN UP</span>
  </div>
</main>
<script>
const tokens = {json.dumps({"dark": TOKENS["dark"]["color"], "light": TOKENS["light"]["color"]}).replace("<", "\\u003c")};
const box = document.getElementById("swatches");
function paint(mode) {{
  box.replaceChildren();
  for (const [name, token] of Object.entries(tokens[mode])) {{
    const el = document.createElement("div");
    el.className = "swatch";
    el.innerHTML = "<i></i><span></span>";
    el.querySelector("i").style.background = token.$value;
    el.querySelector("span").textContent = name + " " + token.$value;
    box.appendChild(el);
  }}
}}
let mode = "dark";
paint(mode);
document.getElementById("theme").addEventListener("click", () => {{
  mode = mode === "dark" ? "light" : "dark";
  document.documentElement.dataset.mode = mode;
  document.getElementById("theme").textContent = mode === "dark" ? "Light tokens" : "Dark tokens";
  paint(mode);
}});
</script>
</body>
</html>
"""
if __name__ == "__main__":
    (HERE / "style-guide.html").write_text(html)
    print("wrote", HERE / "style-guide.html")
