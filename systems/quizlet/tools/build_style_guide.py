#!/usr/bin/env python3
"""Write style-guide.html from tokens.json.

Colours come only from tokens.json. The page shows the public light roles
first, then the prior night roles. Hurme Geometric Sans 2 is not loaded.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def resolve(value):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        parts = value[1:-1].split(".")
        node = TOKENS["core"] if parts[0] in TOKENS["core"] else TOKENS
        for part in parts:
            node = node[part]
        return resolve(node["$value"])
    return value


def swatches(group, prefix):
    rows = []
    for name, token in group.items():
        value = resolve(token["$value"])
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
    light = TOKENS["light"]
    night = TOKENS["night"]
    page = resolve(light["page"]["$value"])
    text = resolve(light["text"]["$value"])
    accent = resolve(light["accent"]["$value"])
    hover = resolve(light["accent-hover"]["$value"])
    trial = resolve(light["trial"]["$value"])
    on_trial = resolve(light["on-trial"]["$value"])
    surface = resolve(light["surface"]["$value"])
    night_page = resolve(night["page"]["$value"])
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
    --hover: %s;
    --trial: %s;
    --on-trial: %s;
    --surface: %s;
    --night: %s;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--page); color: var(--text); font: 400 16px/26px -apple-system, system-ui, sans-serif; }
  main { max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }
  h1 { font-size: 44px; line-height: 56px; font-weight: 700; color: #000000; }
  h2 { font-size: 20px; line-height: 28px; font-weight: 600; margin-top: 40px; }
  p { max-width: 68ch; }
  .swatches, .roles { display: flex; flex-wrap: wrap; gap: 12px; }
  .sw, .role { width: 160px; }
  .sw i, .role i, .step i { display: block; height: 48px; border-radius: 8px; border: 1px solid #D9DDE8; }
  code, small { display: block; font: 12px/16px ui-monospace, Menlo, monospace; }
  .hue { margin: 16px 0; }
  .ramp { display: flex; gap: 6px; }
  .step { width: 64px; }
  button.login, button.signup, button.trial { display: inline-block; border: 2px solid transparent; border-radius: 200px; font-weight: 600; }
  button.login { background: var(--accent); color: #FFFFFF; padding: 10px 16px; height: 40px; font-size: 14px; }
  button.login:hover { background: var(--hover); }
  button.signup { background: var(--accent); color: #FFFFFF; padding: 12px 24px; height: 48px; font-size: 16px; margin-left: 8px; }
  button.trial { background: var(--trial); color: var(--on-trial); padding: 12px 24px; height: 48px; font-size: 16px; margin-left: 8px; }
  .search { margin-top: 16px; background: var(--surface); border: 2px solid transparent; border-radius: 8px; height: 40px; padding: 8px 16px; width: 320px; }
  .night { margin-top: 24px; background: var(--night); color: #F6F7FB; border-radius: 16px; padding: 24px; }
</style>
</head>
<body>
<main>
  <h1>Quizlet, public light</h1>
  <p>Rendered from tokens.json. Values were computed on the signed-out homepage while body had theme-default. The night panel uses the prior signed-in readings. This public pass did not open the signed-in app. Hurme Geometric Sans 2 is the product face and is not loaded here.</p>
  <h2>Light roles</h2>
  <div class="roles">
    %s
  </div>
  <h2>Controls</h2>
  <button class="login" type="button">Log in</button>
  <button class="signup" type="button">Sign up for free</button>
  <button class="trial" type="button">Start 7-day free trial</button>
  <div class="search">Search</div>
  <h2>Ramps</h2>
  %s
  <h2>Prior night roles</h2>
  <div class="night">
    <div class="roles">
      %s
    </div>
  </div>
</main>
</body>
</html>
""" % (
        page, text, accent, hover, trial, on_trial, surface, night_page,
        swatches(light, "light."),
        hue_blocks(),
        swatches(night, "night."),
    )
    (HERE / "style-guide.html").write_text(html)
    print("wrote", HERE / "style-guide.html")


if __name__ == "__main__":
    main()
