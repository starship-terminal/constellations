#!/usr/bin/env python3
"""Write style-guide.html from tokens.json.

The kit template still describes Claude. This builder writes a Quizlet page
from the night tokens so the package has a guide without inventing a light theme.
PRODUCT (adapt): colours come only from tokens.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def swatches(group, prefix):
    rows = []
    for name, token in group.items():
        value = token["$value"]
        rows.append(
            '<div class="sw"><i style="background:%s"></i><code>%s</code><span>%s</span></div>'
            % (value, prefix + name, value)
        )
    return "\n".join(rows)


def hue_blocks():
    blocks = []
    for hue, steps in TOKENS["core"]["color"].items():
        cells = []
        for step, token in steps.items():
            value = token["$value"]
            cells.append(
                '<div class="step"><i style="background:%s"></i><small>%s</small></div>' % (value, step)
            )
        blocks.append('<div class="hue"><h3>%s</h3><div class="ramp">%s</div></div>' % (hue, "".join(cells)))
    return "\n".join(blocks)


def main():
    night = TOKENS["night"]
    page = night["page"]["$value"]
    text = night["text"]["$value"]
    accent = night["accent"]["$value"]
    trial = night["trial"]["$value"]
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quizlet style guide</title>
<style>
  :root {
    --page: %s;
    --text: %s;
    --accent: %s;
    --trial: %s;
    --surface: %s;
    --muted: %s;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--page); color: var(--text); font: 400 16px/26px -apple-system, system-ui, sans-serif; }
  main { max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }
  h1 { font-size: 32px; line-height: 40px; font-weight: 700; }
  h2 { font-size: 20px; line-height: 28px; font-weight: 600; margin-top: 40px; }
  p { max-width: 68ch; }
  .swatches, .roles { display: flex; flex-wrap: wrap; gap: 12px; }
  .sw, .role { width: 140px; }
  .sw i, .role i, .step i { display: block; height: 48px; border-radius: 8px; }
  code, small { display: block; font: 12px/16px ui-monospace, Menlo, monospace; color: var(--muted); }
  .hue { margin: 16px 0; }
  .ramp { display: flex; gap: 6px; }
  .step { width: 64px; }
  button.primary, a.trial { display: inline-block; border: 0; border-radius: 200px; padding: 10px 16px; font: 600 14px/20px -apple-system, system-ui, sans-serif; text-decoration: none; }
  button.primary { background: var(--accent); color: #FFFFFF; }
  a.trial { background: var(--trial); color: #282E3E; margin-left: 8px; }
  .search { margin-top: 16px; background: var(--surface); border-radius: 8px; padding: 10px 16px; width: 280px; color: var(--text); }
</style>
</head>
<body>
<main>
  <h1>Quizlet, night</h1>
  <p>Rendered from tokens.json. Values were computed on the signed-in page while body had theme-night. Light mode was offered and not switched. Hurme Geometric Sans 2 is the product face and is not loaded here.</p>
  <h2>Roles</h2>
  <div class="roles">
    %s
  </div>
  <h2>Ramps</h2>
  %s
  <h2>Controls</h2>
  <button class="primary" type="button">Create a flashcard set</button>
  <a class="trial" href="#trial">Upgrade: free 7-day trial</a>
  <div class="search">Search</div>
</main>
</body>
</html>
""" % (
        page, text, accent, trial, night["surface"]["$value"], night["text-muted"]["$value"],
        swatches(night, "night."),
        hue_blocks(),
    )
    (HERE / "style-guide.html").write_text(html)
    print("wrote", HERE / "style-guide.html")


if __name__ == "__main__":
    main()
