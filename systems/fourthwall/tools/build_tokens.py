#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from fourthwall.com, products.fourthwall.com,
auth.fourthwall.com (/get-started), docs.fourthwall.com and help.fourthwall.com:
  raw/css-vars.json          the custom properties the five public hosts'
                             stylesheets declare — the Webflow marketing
                             --_primitives---*/--_surface---*/--_rhythm---*
                             layers and flat --gs*/--b*/--g*/--r*/--y*/
                             --twitch* ramps, the catalogue's --color-*/
                             --bg-*/--text-*/--font-*/--space-*/--radius-*/
                             --shadow-*/--motion-* names (semantics as
                             light-dark()), the Mintlify --gray-*/--primary*/
                             tailwind-ish layer and the Docusaurus --ifm-*/
                             --fw-* layer (tools/capture/vars.mjs), binned
                             theme / app / skins / vendor / utility / tailwind
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py):
                             each leaf either names a variable ("var")
                             resolved per theme, or carries a measured value
                             and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

The sets keep each host's real architecture honest:
  core        theme-independent scales — the measured type ramp, families,
              weights, radii, motion and component geometry
  light       the marketing surface — the Webflow :root vocabulary resolved
              on the light shell (the only painted marketing surface)
  ink         the marketing dark sections — the names the on-ink scope
              (.on-ink/.site-footer/.leg-section) actually remaps, resolved
              under body.on-ink; painted dark bands, not a user theme
  catalog     the products shell — the catalogue DS in its light-dark()
              light branch (the only catalogue surface visitors paint)
  catalogDark the products shell under a forced color-scheme: dark — the
              declared dark branch, never painted signed out
  signup      /get-started's Keycloak shell — the same catalogue DS resolved
              light (what a light-preference visitor paints; its light-dark()
              pairs follow the system like the catalogue's)
  docs        the Mintlify shell, light
  docsDark    the Mintlify shell under html.dark — its own "Change theme
              preference" menu
  help        the Docusaurus shell, data-theme=light
  helpDark    the Docusaurus shell under data-theme=dark — its own toggle

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

RV = V["resolved"]
def decl_of(*shells):
    out = {}
    for s in shells:
        for n, v in RV.get(s, {}).items():
            out[n] = v.get("value", v["raw"])
    return out
DECL = {
    "light": decl_of("light"),
    "ink": decl_of("ink"),
    "catalog": decl_of("catalog"),
    "catalogDark": decl_of("catalogDark"),
    "signup": decl_of("signup"),
    "docs": decl_of("docs"),
    "docsDark": decl_of("docsDark"),
    "help": decl_of("help"),
    "helpDark": decl_of("helpDark"),
}
SETNAMES = list(DECL)


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), hsla() -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", v)
    if m:  # the Mintlify "R G B" channel triplets
        r, g, b = (int(x) for x in m.groups())
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"hsla?\(\s*0\s*,\s*0%\s*,\s*([\d.]+)%\s*(?:,\s*([\d.]+))?\)", v)
    if m:
        lvl = round(float(m.group(1)) * 2.55)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    """Refuse a value that is not the DTCG type it claims. An alias is checked by the alias pass."""
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val) if not str(val).startswith("{") else None
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "gradient":
        for stop in val:
            if not str(stop["color"]).startswith("{"):
                norm_color(stop["color"])
            if not 0 <= stop["position"] <= 1:
                raise ValueError(f"{path}: gradient position {stop['position']!r}")


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL[theme]:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({theme})")
        val = DECL[theme][name]
        src = f"css-var {name} ({theme})"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)", val.strip())
        if m:
            val = [float("%g" % float(x)) for x in m.groups()]
        elif val.strip() in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
            val = {"ease": [.25, .1, .25, 1], "ease-in": [.42, 0, 1, 1], "ease-out": [0, 0, .58, 1],
                   "ease-in-out": [.42, 0, .58, 1], "linear": [0, 0, 1, 1]}[val.strip()]
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:  # a calc(a/b) line-height ratio
            val = round(float(m.group(1)) / float(m.group(2)), 4)
        elif re.fullmatch(r"-?\d+(\.\d+)?", val):
            val = float(val) if "." in val else int(val)
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"([\d.]+)(m?s)", val.strip())
        if m:
            val = ("%g" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))) + "ms"
    if ty == "dimension":
        if isinstance(val, (int, float)):
            val = "%gpx" % val
        elif isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
            val = val.strip() + "px"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    if spec.get("angle"):
        t["$extensions"]["angle"] = spec["angle"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    # Only real metadata keys are skipped — the Webflow layer names begin with
    # an underscore (_primitives/_surface/_rhythm) and are genuine token groups.
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if k not in ("_about", "_meta")}


core = build(SPEC["core"], "light")  # scales — theme-independent measured readings
sets = {name: build(SPEC[name], name) for name in SETNAMES}
# The component tokens are theme-independent measured geometry (bar heights,
# card widths, field sizes), so they hang off core and reach every theme.
core["component"] = build(SPEC["component"], "light")

# motion, as measured on the page: durations, easing curves, which properties
# transition, animations and @keyframes, and what prefers-reduced-motion: reduce
# changes (raw/motion.json, written by tools/capture/motion-probe.mjs; motion.py
# is the product-free mapping). A package that has not run the probe has no
# motion group. The product's own named scales (--motion-* in the catalogue
# set) stay as they are: those are semantic names read from its variables,
# while `motion` is what its elements actually run.
not_core = []
if (RAW / "motion.json").exists():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], motion_not_core = motion.build(json.loads((RAW / "motion.json").read_text()))
    not_core += motion_not_core
if not_core:
    core["$extensions"] = {"notTokenised": not_core}


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


CORE_NAMES = {n for n, _ in tokens_of(core)}
NAMES = {name: CORE_NAMES | {n for n, _ in tokens_of(sets[name])} for name in SETNAMES}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for name in SETNAMES:
    for n, t in list(tokens_of(sets[name])):
        for a in aliases(t["$value"]):
            if a not in NAMES[name]:
                raise KeyError(f"{name}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    **sets,
    "$themes": [
        {"id": "light", "name": "Marketing", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The marketing surface: fourthwall.com's Webflow DS on :root — --_primitives---* ink/paper ramps, the --_surface---* semantic layer, --_rhythm---* spacing and the flat --gs*/--b*/--r* legacy ramps. The only painted marketing surface."},
        {"id": "ink", "name": "Marketing on-ink", "selectedTokenSets": {"core": "source", "light": "source", "ink": "enabled"},
         "$description": "The marketing dark sections: .on-ink/.site-footer/.leg-section redeclare the --_surface---* semantic layer on dark bands (bg.page #0a0a0a, text.body #ffffff). Painted sections, not a user-selectable theme — the ink set only carries the names the scope actually remaps."},
        {"id": "catalog", "name": "Catalogue", "selectedTokenSets": {"core": "source", "catalog": "enabled"},
         "$description": "The product catalogue: products.fourthwall.com's own DS (--color-*/--bg-*/--text-*/--font-*/--space-*/--radius-*/--motion-*) in its light-dark() light branch — the only catalogue surface visitors paint."},
        {"id": "catalogDark", "name": "Catalogue dark", "selectedTokenSets": {"core": "source", "catalogDark": "enabled"},
         "$description": "The catalogue DS's declared dark branch: the same semantic names resolve through light-dark() under a dark color-scheme (--bg-primary #161712). Declared but never painted signed out — the catalogue ships no theme toggle, so these are forced-probe resolutions, not an observed public theme (docsDark and helpDark are the genuinely toggled themes)."},
        {"id": "signup", "name": "Auth (signup)", "selectedTokenSets": {"core": "source", "signup": "enabled"},
         "$description": "The /get-started signup shell: auth.fourthwall.com's Keycloak pages ship the catalogue DS in light (--bg-primary #ffffff, --text-primary #161712 — its own light-dark() pairs follow the visitor's color-scheme like the catalogue's; the catalogDark set carries the same dark branch). Nothing was typed or submitted."},
        {"id": "docs", "name": "Docs", "selectedTokenSets": {"core": "source", "docs": "enabled"},
         "$description": "docs.fourthwall.com (Mintlify) in light: the --gray-* ramp, --color-*/--primary and the tailwind-ish --container-*/--ease-*/--leading-* layer."},
        {"id": "docsDark", "name": "Docs dark", "selectedTokenSets": {"core": "source", "docsDark": "enabled"},
         "$description": "docs.fourthwall.com under html.dark — reached through the site's own 'Change theme preference' menu, not a reconstruction."},
        {"id": "help", "name": "Help", "selectedTokenSets": {"core": "source", "help": "enabled"},
         "$description": "help.fourthwall.com (Docusaurus) in light: the --ifm-* Infima layer plus the product's --fw-*/--docusaurus-* names."},
        {"id": "helpDark", "name": "Help dark", "selectedTokenSets": {"core": "source", "helpDark": "enabled"},
         "$description": "help.fourthwall.com under data-theme=dark — reached through the navbar's real colour-mode toggle, not a reconstruction."},
    ],
    "$metadata": {"tokenSetOrder": ["core"] + SETNAMES},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core",) + tuple(SETNAMES)})
