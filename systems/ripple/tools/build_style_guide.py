#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: the public site has one scheme."""
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
    if ty == "shadow":
        return ", ".join(
            ("inset " if s.get("inset") else "")
            + f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}'
            for s in v
        )
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    if ty == "gradient":
        return "linear-gradient(92deg, " + ", ".join(
            f'{alias(s["color"])} {round(s["position"] * 100, 2)}%' for s in v
        ) + ")"
    if ty == "fontWeight":
        return str(v)
    return alias(v)


def block(setname):
    lines = []
    for n, t in flat(T[setname]):
        val = css_val(t)
        if val:
            lines.append(f"  {cssname(n)}: {val};")
    return "\n".join(lines)


css = block("core") + "\n" + block("light")


def js(value):
    """A JS string literal for a token value: quoted and escaped by json, with < as \\u003c so a
    value holding </script> cannot end the script."""
    return json.dumps(str(value)).replace("<", "\\u003c")


html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ripple style guide</title>
<style>
:root {{
{css}
  color-scheme: light;
  --sg: "rippleFont", "Avenir Next", "Segoe UI", sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--surface-page); color: var(--text-primary); font: 400 16px/24px var(--sg); }}
header {{ position: sticky; top: 0; background: var(--surface-white); border-bottom: 1px solid var(--border-subtle); padding: 16px 32px; display: flex; gap: 24px; align-items: center; }}
header strong {{ font-weight: 500; }}
header span {{ color: var(--text-muted); font-size: 14px; }}
main {{ max-width: 1152px; margin: 0 auto; padding: 32px 32px 80px; }}
h2 {{ font: 500 36px/48px var(--sg); letter-spacing: -0.5px; margin: 48px 0 12px; }}
p {{ max-width: 70ch; }}
.hero {{ background: var(--surface-hero); color: var(--text-on-dark); border-radius: 12px; padding: 48px 32px; }}
.hero h1 {{ margin: 0 0 12px; font: var(--typography-display); letter-spacing: -1px; }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.btn {{ display: inline-flex; align-items: center; height: var(--component-button-primary-height); padding: 8px 16px; border-radius: var(--component-button-primary-radius); background: var(--accent-deep); color: var(--text-on-accent); font: var(--typography-button); border: 0; box-shadow: var(--shadow-button-inset); }}
.btn-quiet {{ display: inline-flex; align-items: center; height: 40px; padding: 6px 18px; border-radius: 9999px; border: 2px solid var(--text-ink); color: var(--text-ink); background: transparent; font: var(--typography-ui); text-decoration: none; }}
.icon {{ width: 40px; height: 40px; border-radius: 9999px; background: var(--component-icon-button-background); border: 0; }}
.field {{ height: 40px; width: 280px; border: 0; border-radius: 4px; background: var(--component-text-field-background); color: var(--component-text-field-text); padding: 8px 16px; font: var(--typography-body); box-shadow: var(--shadow-focus); }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
.sw {{ border-radius: 8px; overflow: hidden; border: 1px solid var(--border-subtle); }}
.sw i {{ display: block; height: 56px; }}
.sw b, .sw small {{ display: block; padding: 6px 8px 0; font-size: 12px; }}
.sw small {{ color: var(--text-muted); padding-bottom: 8px; }}
.card {{ background: var(--surface-raised); border-radius: 8px; padding: 16px; max-width: 360px; }}
.grad {{ font: var(--typography-hero); letter-spacing: -1px; background: var(--gradient-hero); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0; }}
</style>
</head>
<body>
<header>
  <strong>Ripple</strong>
  <span>Public marketing, light only. Values from tokens.json.</span>
</header>
<main>
  <section class="hero">
    <h1>The new standard for modern finance</h1>
    <p>Ripple gives businesses everything they need to operate across traditional and digital finance.</p>
    <div class="row">
      <button class="btn">Explore Our Solutions</button>
    </div>
  </section>
  <h2>Colour</h2>
  <div class="swatches" id="swatches"></div>
  <h2>Type</h2>
  <p class="grad">Enabling the Internet of Value</p>
  <p style="font: var(--typography-lede)">Lede at 19px / 28px, weight 350.</p>
  <p>Body at 16px / 24px.</p>
  <h2>Controls</h2>
  <div class="row">
    <button class="btn">Talk to Our Team</button>
    <a class="btn-quiet" href="#contact">Contact Sales</a>
    <button class="icon" aria-label="Open search"></button>
    <input class="field" placeholder="Search ripple.com" value="payments">
  </div>
  <div class="card">
    <strong>Payments</strong>
    <p style="color: var(--text-muted); font-size: 14px;">One platform for all your payments infrastructure needs</p>
  </div>
</main>
<script>
const roles = [
  ["page", "var(--surface-page)", {js(T['light']['surface']['page']['$value'])}],
  ["hero", "var(--surface-hero)", {js(T['light']['surface']['hero']['$value'])}],
  ["raised", "var(--surface-raised)", {js(T['light']['surface']['raised']['$value'])}],
  ["text", "var(--text-primary)", {js(T['light']['text']['primary']['$value'])}],
  ["muted", "var(--text-muted)", {js(T['light']['text']['muted']['$value'])}],
  ["accent", "var(--accent)", {js(T['light']['accent']['$value'])}],
  ["on accent", "var(--text-on-accent)", {js(T['light']['text']['on-accent']['$value'])}],
  ["link", "var(--text-link)", {js(T['light']['text']['link']['$value'])}]
];
const box = document.getElementById("swatches");
for (const [name, bg, hex] of roles) {{
  const d = document.createElement("div");
  d.className = "sw";
  d.innerHTML = "<i></i><b></b><small></small>";
  d.querySelector("i").style.background = bg;
  d.querySelector("b").textContent = name;
  d.querySelector("small").textContent = hex;
  box.appendChild(d);
}}
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
