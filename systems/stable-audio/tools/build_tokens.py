#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Sources, read from https://stableaudio.com/ on 2026-11-21, signed out:
  raw/css-vars.json              every --sx-* and --hn-* declaration in the same-origin
                                 stylesheets, plus resolved.marketing (computed on
                                 .homePage_page__pMG82, which carries sx-scope sx-platform sx-dark)
  raw/components-computed.json   getComputedStyle on the public controls

The public marketing page paints the platform-dark set. :root still declares a paper
palette that the homepage does not use; those values are core.color.paper and are
labelled as the :root declaration, not as the painted page. There is no light theme
on the public site, so tokens.json has core and dark only.

Deterministic: same inputs, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())

ROOT = {}
PLATFORM = {}
for rule in V["rules"]:
    sel = rule["selector"]
    if sel == ":root" and "--sx-p-000" in rule["properties"] and rule["properties"]["--sx-p-000"] == "#f2efe6":
        ROOT.update(rule["properties"])
    if sel == ".sx-scope.sx-platform, :root.sx-platform .sx-scope":
        PLATFORM.update(rule["properties"])
RESOLVED = V["resolved"]["marketing"]


def src_var(name, where):
    return {"source": f"css-var {name} declared on {where}, stableaudio.com 2026-11-21"}


def src_measured(where):
    return {"source": f"measured {where}, stableaudio.com 2026-11-21, raw/components-computed.json"}


def color(value):
    return {"$type": "color", "$value": value}


def dim(value):
    return {"$type": "dimension", "$value": value}


def token(value, ty, source):
    return {"$type": ty, "$value": value, "$extensions": source}


def norm_color(value):
    value = value.strip()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", value)
    if not m:
        return value
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def comp(label):
    for item in C["components"]:
        if item.get("label") == label:
            return item
    raise KeyError(label)


def put(tree, path, node):
    cur = tree
    parts = path.split(".")
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = node


core = {}
# Paper :root palette. Not what the public page paints.
for name, value in sorted(ROOT.items()):
    if name.startswith("--sx-p-") or name in ("--sx-paper", "--sx-ink-900", "--sx-ink-800", "--sx-ink-700", "--sx-ink-600", "--sx-ink-500", "--sx-ink-400", "--sx-accent", "--sx-primary", "--sx-ok", "--sx-warn", "--sx-danger", "--sx-info"):
        key = name.removeprefix("--sx-").replace("-", ".")
        put(core, "color.paper." + key, token(value, "color", src_var(name, ":root")))

for name in ("--sx-sp-1", "--sx-sp-2", "--sx-sp-3", "--sx-sp-4", "--sx-sp-5", "--sx-sp-6", "--sx-sp-8", "--sx-sp-10", "--sx-sp-12", "--sx-sp-16"):
    put(core, "spacing." + name.removeprefix("--sx-sp-"), token(ROOT[name], "dimension", src_var(name, ":root")))

for name in ("--sx-dur-1", "--sx-dur-2", "--sx-dur-3", "--sx-dur-4", "--sx-dur-5", "--sx-dur-pop", "--sx-dur-wipe", "--sx-dur-stagger"):
    put(core, "motion." + name.removeprefix("--sx-dur-"), token(ROOT[name], "duration", src_var(name, ":root")))

for name, key in (("--sx-ease-out", "out"), ("--sx-ease-in", "in"), ("--sx-ease-in-out", "in-out")):
    nums = [float(x) for x in re.findall(r"-?\d*\.?\d+", ROOT[name])]
    put(core, "motion.ease-" + key, token(nums, "cubicBezier", src_var(name, ":root")))

put(core, "font.ui", token(
    '"Neue Haas Grotesk Text Pro", "SX Inter", "Helvetica Neue", Helvetica, Arial, sans-serif',
    "fontFamily",
    {"source": "computed font-family on .homePage_page__pMG82, 2026-11-21. --sx-ff-ui on :root names Suisse Int'l first; the painted page substitutes Neue Haas Grotesk Text Pro."},
))
put(core, "font.display", token(
    '"Neue Haas Grotesk Text Pro", "SX Inter", "Helvetica Neue", Helvetica, Arial, sans-serif',
    "fontFamily",
    {"source": "computed font-family on h1, homepage, 2026-11-21"},
))
put(core, "font.mono", token(
    RESOLVED.get("--sx-ff-mono", ROOT.get("--sx-ff-mono")),
    "fontFamily",
    src_var("--sx-ff-mono", ":root, resolved on the marketing scope"),
))
put(core, "sizing.tap-min", token("44px", "dimension", src_var("--sx-tap-min", ":root")))
put(core, "radius.control", token("0px", "dimension", src_var("--sx-r-control", ".sx-scope.sx-platform (value 0, stored as 0px)")))
put(core, "radius.card", token("0px", "dimension", src_var("--sx-r-card", ".sx-scope.sx-platform (value 0, stored as 0px)")))
put(core, "radius.menu", token("0px", "dimension", src_var("--sx-r-menu", ".sx-scope.sx-platform (value 0, stored as 0px)")))
put(core, "radius.pill", token("999px", "dimension", src_var("--sx-r-pill", ".sx-scope.sx-platform")))

# Painted platform colours, the public page.
dark = {}
for name, value in sorted(PLATFORM.items()):
    if not name.startswith("--sx-"):
        continue
    if name.startswith("--sx-grain") or "gradient" in value or value.startswith("url(") or "clamp(" in value or value.startswith("min("):
        continue
    if name.startswith("--sx-r-") or name.startswith("--sx-dur") or name.startswith("--sx-ease") or name.startswith("--sx-ff") or name.startswith("--sx-fs") or name.startswith("--sx-sp") or name.startswith("--sx-deck") or name.startswith("--sx-hub") or name.startswith("--sx-zoom") or name.startswith("--sx-rail") or name.startswith("--sx-tracking") or name.startswith("--sx-fw"):
        continue
    key = name.removeprefix("--sx-").replace("-", ".")
    ty = "color" if value.startswith("#") or value.startswith("rgb") or value.startswith("color-mix") else "other"
    if ty != "color":
        continue
    put(dark, "color." + key, token(value, "color", src_var(name, ".sx-scope.sx-platform")))

# Semantic roles from the painted page, measured where the CSS variable is not the paint.
primary = comp("button-primary")["states"]["default"]
secondary = comp("button-secondary")["states"]["default"]
nav = comp("link-pricing")["states"]["default"]
dialog = comp("dialog-signup")["dialog"]
menu = comp("menu-presets")["menu"]
card = comp("pricing")["card"]
put(dark, "page", token("#000000", "color", {"source": "computed background-color on html.bg-[#000], homepage, 2026-11-21"}))
put(dark, "surface", token(norm_color(card["backgroundColor"]), "color", src_measured("pricing card .PricingNext_card background")))
put(dark, "text.muted", token(norm_color(nav["color"]), "color", src_measured("nav link Pricing color, default")))
put(dark, "text.strong", token("#ffffff", "color", src_var("--sx-ink-900", ".sx-scope.sx-platform, resolved #ffffff on the homepage scope")))
put(dark, "accent", token(norm_color(primary["backgroundColor"]), "color", src_measured("homepage Start free button background, this load. The fill changes between loads; see What to distrust")))
put(dark, "border", token("rgba(255, 255, 255, 0.22)", "color", src_var("--sx-rule-soft", ".sx-scope.sx-platform") | {"note": "also the Sign in button border"}))
put(dark, "overlay", token(norm_color(dialog["backgroundColor"]), "color", src_measured("signup dialog background")))
put(dark, "component.button.primary.background", token(norm_color(primary["backgroundColor"]), "color", src_measured("button.Button_primary Start free, default")))
put(dark, "component.button.primary.color", token(norm_color(primary["color"]), "color", src_measured("button.Button_primary Start free, default")))
put(dark, "component.button.primary.height", token(primary["height"], "dimension", src_measured("button.Button_primary Start free, default")))
put(dark, "component.button.primary.font-size", token(primary["fontSize"], "dimension", src_measured("button.Button_primary Start free, default")))
put(dark, "component.button.secondary.color", token(norm_color(secondary["color"]), "color", src_measured("button.Button_secondary Sign in, default")))
put(dark, "component.button.secondary.height", token(secondary["height"], "dimension", src_measured("button.Button_secondary Sign in, default")))
put(dark, "component.control.radius", token("0px", "dimension", src_measured("button border-radius, homepage")))
put(dark, "component.dialog.radius", token(dialog["borderRadius"], "dimension", src_measured("signup dialog border-radius")))
put(dark, "component.dialog.background", token(norm_color(dialog["backgroundColor"]), "color", src_measured("signup dialog background")))
put(dark, "component.menu.background", token("rgba(31, 31, 31, 0.8)", "color", src_measured("Presets menu background, color(srgb 0.121569 0.121569 0.121569 / 0.8)")))
put(dark, "component.card.radius", token(card["borderRadius"], "dimension", src_measured("pricing card border-radius")))
put(dark, "typography.display.size", token("72px", "dimension", {"source": "computed font-size on homepage h1, 2026-11-21"}))
put(dark, "typography.display.weight", token("600", "fontWeight", {"source": "computed font-weight on homepage h1, 2026-11-21"}))
put(dark, "typography.display.line-height", token("73.44px", "dimension", {"source": "computed line-height on homepage h1, 2026-11-21"}))
put(dark, "typography.nav.size", token(nav["fontSize"], "dimension", src_measured("nav link Pricing font-size")))
put(dark, "typography.body.size", token("16px", "dimension", {"source": "computed font-size on body, homepage, 2026-11-21"}))

doc = {
    "$description": "Stable Audio public site, measured 2026-11-21. core holds the :root paper palette and shared scales. dark holds the platform set the public pages paint. No light theme was offered.",
    "core": core,
    "dark": dark,
    "$themes": [{"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}}],
}

# Checks
DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")
def walk(node, path=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            if "source" not in v.get("$extensions", {}):
                raise SystemExit("missing source " + p)
            if v["$type"] == "dimension" and not DIM.fullmatch(str(v["$value"])):
                raise SystemExit(f"{p}: bad dimension {v['$value']!r}")
            if v["$type"] == "color" and not re.match(r"^(#|rgb|rgba|color-mix)", str(v["$value"])):
                raise SystemExit(f"{p}: bad color {v['$value']!r}")
        elif isinstance(v, dict):
            walk(v, p)
walk(core)
walk(dark)
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")

def count(node):
    n = 0
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            n += 1
        elif isinstance(v, dict):
            n += count(v)
    return n
print("core", count(core), "dark", count(dark))
