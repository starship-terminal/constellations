#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from fresha.com's four signed-out surfaces:
  raw/css-vars.json            every custom property the surfaces' stylesheets declare, plus
                               `tokenMap` (hashed Panda var -> readable Panda token name, mapped
                               through the atomic class names) and `resolved`: each name as the
                               browser resolves it in probe documents carrying the real sheets
                               (light, [data-theme=dark], [data-theme=accent], the /lp/ sheet)
                               (tools/capture/vars.mjs)
  raw/components-computed.json computed styles and geometry of measured components
                               (tools/capture/public/measure.mjs)
  raw/motion.json              the motion probe's transition/animation/reduced-motion readings
                               (tools/capture/motion-probe.mjs -> tools/motion.py)

Fresha ships one Panda CSS system (--made-with-panda) across the consumer marketplace, the B2B
marketing app and partners.fresha.com. Two vocabularies sit side by side:
  * the hashed Panda layer every host shares (`--cDETHm` = colors.border.neutralFaded), mapped
    back to readable names through the atomic classes; and
  * the partner portal's readable theme layer (`--color-foreground-neutral`, `--typography-*`,
    `--sizing-*`, component vars like `--avatar-*`/`--wizard-*`), declared per data-theme.
The legacy /lp/ microsite declares only two own vars and paints literal values instead; its
literal colours are not in any stylesheet token scope, so the LP set holds its two vars and a
measured accent.

Sets:
  core    theme-invariant scales (spacing, sizes, borderWidths, durations, easings,
          aspectRatios, backdropBlurs, the six theme-stable shadows), the font stacks,
          measured component geometry and the motion group
  light   the signed-out default everywhere: mapped `colors.*`, the 127 unmapped hashed vars,
          shadows.level1/level2, and the partner named layer's light values
  dark    same names, [data-theme=dark] values — painted on partners.fresha.com sign-in, which
          sets data-theme="auto", under prefers-color-scheme: dark (screenshot evidence); on
          the consumer and B2B routes it is declared-only (nothing sets data-theme)
  accent  the [data-theme=accent] scope the partner sheets declare (the consumer and B2B sheets
          ship no accent scope); no signed-out element was observed carrying data-theme=accent
  app     the loose named vars the surfaces put on :root/html outside the theme layer
          (safe-area insets, side edges, --svh, translucency, the two /lp/ panel offsets)

Class-scoped vars (selectors like `.--final-step-center_…`, component internals) and vendor vars
(--yarl__*, --lightningcss-*, --made-with-panda, --csstools-*) are not tokens; their names and
values sit under each set's $extensions.notTokenised / .vendor.

Every token carries $extensions.source naming what it was read from ("css-var <name>, resolved
in the <scope> probe" or "measured <component> <state> on <page>"). Deterministic: same inputs,
same bytes. Edit the raw inputs, never tokens.json.
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod  # tools/motion.py -> core.motion

V = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None
TM = V["tokenMap"]            # hashed var -> {token: 'colors.foreground.neutral', classes: [...]}
RES = V["resolved"]           # scope -> {name: {raw, kind, value, note?}}

# ----------------------------------------------------------------------------- value helpers

def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = int(m[1]), int(m[2]), int(m[3]), m[4]
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, float(a))
    return v  # leave colour() functions and unresolved spellings verbatim


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")


def shadow_layers(v):
    """'rgba(19,19,19,.1) 0px 0px 0px 1px, …' -> DTCG shadow layers. Splits top-level commas only."""
    parts, depth, cur = [], 0, ""
    for ch in v:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    layers = []
    for p in parts:
        p = p.strip()
        inset = p.startswith("inset ")
        if inset:
            p = p[6:]
        m = re.match(r"^(.*?)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)$", p)
        if not m:
            return None
        color, x, y, blur, spread = m.groups()
        layers.append({"color": norm_color(color), "offsetX": x, "offsetY": y,
                       "blur": blur, "spread": spread, "inset": inset} if inset else
                      {"color": norm_color(color), "offsetX": x, "offsetY": y,
                       "blur": blur, "spread": spread})
    return layers


def duration_ms(v):
    m = re.fullmatch(r"([\d.]+)(m?s)", str(v).strip())
    return ("%gms" % (float(m[1]) * (1000 if m[2] == "s" else 1))) if m else None


def bezier(v):
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)",
                     str(v).strip())
    if m:
        return [float("%g" % float(x)) for x in m.groups()]
    kw = {"linear": [0, 0, 1, 1], "ease": [.25, .1, .25, 1], "ease-in": [.42, 0, 1, 1],
          "ease-out": [0, 0, .58, 1], "ease-in-out": [.42, 0, .58, 1]}
    return kw.get(str(v).strip())


def tokenise(name, raw_val, kind, path, src):
    """(token, reason-not-tokenised). kind comes from the probe; fall back to the value's shape."""
    v = raw_val
    if kind == "color":
        return {"$value": norm_color(v), "$type": "color", "$extensions": {"source": src}}, None
    if kind == "shadow":
        layers = shadow_layers(str(v))
        if layers is None:
            return None, f"{path}: shadow {v!r} did not parse"
        return {"$value": layers, "$type": "shadow", "$extensions": {"source": src}}, None
    if kind == "duration":
        ms = duration_ms(v)
        if ms:
            return {"$value": ms, "$type": "duration", "$extensions": {"source": src}}, None
    if kind == "easing":
        b = bezier(v)
        if b:
            return {"$value": b, "$type": "cubicBezier", "$extensions": {"source": src}}, None
    if kind == "dimension":
        if DIM.fullmatch(str(v)):
            return {"$value": str(v), "$type": "dimension", "$extensions": {"source": src}}, None
        return {"$value": str(v), "$type": "other", "$extensions": {"source": src},
                "$description": f"not a plain px/rem/em length: {v!r}"}, None
    if kind == "number":
        return {"$value": v if isinstance(v, (int, float)) else float(v),
                "$type": "number", "$extensions": {"source": src}}, None
    if kind == "fontFamily":
        return {"$value": [s.strip().strip('"\'') for s in str(v).split(",")],
                "$type": "fontFamily", "$extensions": {"source": src}}, None
    # kind == 'other' or unknown: keep the verbatim resolved/declared value
    return {"$value": v, "$type": "other", "$extensions": {"source": src}}, None


def put(tree, path_parts, leaf):
    node = tree
    for p in path_parts[:-1]:
        node = node.setdefault(p, {})
    node[path_parts[-1]] = leaf


def set_path(parts):
    """A dotted Panda token path -> nested dict keys, sanitised."""
    return [p.replace("*", "x").replace(" ", "-") for p in parts if p != ""]


# ----------------------------------------------------------------------------- core scales

core = {}
light, dark, accent = {}, {}, {}
app = {"consumer": {}, "b2b": {}, "partner": {}, "lp": {}}
not_tokenised = {"core": [], "light": [], "dark": [], "accent": [], "app": []}
vendor = []

FAM_TYPE = {"colors": "color", "borderWidths": "dimension", "spacing": "dimension",
            "sizes": "dimension", "durations": "duration", "easings": "cubicBezier",
            "aspectRatios": "number", "backdropBlurs": "dimension", "shadows": "shadow",
            "breakpoints": "dimension", "zIndex": "number", "opacity": "number",
            "fonts": "fontFamily", "fontSizes": "dimension", "fontWeights": "fontWeight",
            "lineHeights": "dimension", "letterSpacings": "dimension", "radii": "dimension",
            "blurs": "dimension", "animations": "other", "keyframes": "other",
            "borderStyles": "other"}

for h, m in sorted(TM.items(), key=lambda kv: kv[1]["token"]):
    tname = m["token"]                      # e.g. colors.border.neutralFaded
    fam = tname.split(".")[0]
    parts = set_path(tname.split("."))
    src_l = f"css-var {h} ({tname}), resolved in the light probe; mapped via atomic classes {', '.join(m['classes'][:2])}"
    if fam == "colors" or tname in ("shadows.level1", "shadows.level2"):
        for tree, scope in ((light, "light"), (dark, "dark"), (accent, "accent")):
            r = RES.get(scope, {}).get(h)
            if not r:
                continue
            src = f"css-var {h} ({tname}), resolved in the [data-theme={scope}] probe" \
                  + (" (painted on partners.fresha.com sign-in under prefers-color-scheme: dark)"
                     if scope == "dark" else "")
            leaf, why = tokenise(h, r.get("value", r["raw"]), r["kind"], tname, src)
            if leaf:
                if scope == "accent":
                    leaf.setdefault("$extensions", {})["painted"] = \
                        "declared scope: no signed-out element was observed carrying data-theme=accent"
                put(tree, parts, leaf)
            else:
                not_tokenised[scope].append({"name": tname, "var": h, "value": r.get("raw"), "why": why})
    else:
        r = RES["light"].get(h)
        if not r:
            continue
        leaf, why = tokenise(h, r.get("value", r["raw"]), r["kind"], tname, src_l)
        if leaf:
            put(core, parts, leaf)
        else:
            not_tokenised["core"].append({"name": tname, "var": h, "value": r.get("raw"), "why": why})

# hashed vars no atomic class maps to a readable name — real theme values, named by their var.
# Named vars that also live on app selectors (--svh, --scale-x, …) are not Panda hashes.
APP_NAMES = {n for r in V["app"] for n in r["properties"]}
HASHED = [n for n in RES["light"] if len(n) <= 10 and n not in TM and n not in APP_NAMES]
for h in sorted(HASHED):
    for tree, scope in ((light, "light"), (dark, "dark"), (accent, "accent")):
        r = RES.get(scope, {}).get(h)
        if not r:
            continue
        leaf, why = tokenise(h, r.get("value", r["raw"]), r["kind"], "hashed." + h[2:],
                             f"css-var {h}, resolved in the [data-theme={scope}] probe; "
                             "no atomic class maps it to a readable Panda token name")
        if leaf:
            put(tree, ["hashed", h[2:]], leaf)
        else:
            not_tokenised[scope].append({"name": h, "value": r.get("raw"), "why": why})

# ----------------------------------------------------------------------------- partner named theme layer

# theme bin: the partner sheet's readable layer, per data-theme scope
partner_rules = {}
for r in V["theme"]:
    if not r["file"].startswith("partner"):
        continue
    sel = r["selector"]
    if sel == ':root, [data-theme="light"]':
        partner_rules["light"] = r["properties"]
    elif sel == '[data-theme="dark"]':
        partner_rules["dark"] = r["properties"]
    elif sel == '[data-theme="accent"]':
        partner_rules["accent"] = r["properties"]

for scope, tree in (("light", light), ("dark", dark), ("accent", accent)):
    props = partner_rules.get(scope, {})
    for name in sorted(props):
        if name.startswith(("--yarl__", "--lightningcss-", "--made-with-panda", "--csstools-")):
            vendor.append({"name": name, "scope": scope, "value": props[name]})
            continue
        r = RES.get(scope, {}).get(name)
        raw = r.get("value", r["raw"]) if r else props[name]
        kind = r["kind"] if r else "other"
        src = f"css-var {name}, declared on {dict((('light', ':root, [data-theme=light]'), ('dark', '[data-theme=dark]'), ('accent', '[data-theme=accent]')))[scope]}, resolved in the {scope} probe" if r else \
              f"css-var {name}, declared on {scope} scope (unresolved: {props[name]!r})"
        leaf, why = tokenise(name, raw, kind, name[2:], src)
        if scope == "accent" and leaf:
            leaf.setdefault("$extensions", {})["painted"] = \
                "declared scope: no signed-out element was observed carrying data-theme=accent"
        if scope == "dark" and leaf:
            leaf.setdefault("$extensions", {})["painted"] = \
                "partners.fresha.com sign-in paints this under prefers-color-scheme: dark (data-theme=auto)"
        # --color-x -> partner.color.x ; --avatar-group-y -> partner.avatar.group-y
        parts = name[2:].split("-", 1)
        group = parts[0]
        rest = parts[1] if len(parts) > 1 else "value"
        if leaf:
            put(tree, ["partner", group, rest], leaf)
        else:
            not_tokenised[scope].append({"name": name, "value": raw, "why": why})

# ----------------------------------------------------------------------------- fonts + app vars

for n in ("--font-body", "--font-header", "--font-link", "--font-display"):
    r = RES["light"].get(n)
    if r:
        put(core, ["font", n[7:]], {"$value": [s.strip().strip('"\'') for s in r["value"].split(",")],
                                    "$type": "fontFamily",
                                    "$extensions": {"source": f"css-var {n} on html, resolved in the light probe"}})

# loose named vars on root-ish selectors (not the partner theme layer, not class-scoped)
FONT_VARS = {"--font-body", "--font-header", "--font-link", "--font-display"}
ROOTISH = re.compile(r"^(:root|html|:where\(:root|\[dir=)")
for r in V["app"]:
    sel = r["selector"]
    if not ROOTISH.match(sel) or sel.startswith(".--"):
        continue
    surface = r["file"].split(" ")[0]
    for name, raw in sorted(r["properties"].items()):
        if name in FONT_VARS or name.startswith(("--yarl__", "--lightningcss-", "--made-with-panda",
                                                 "--csstools-", "--env-safe-area-inset")):
            if name.startswith(("--yarl__", "--lightningcss-", "--made-with-panda", "--csstools-")):
                vendor.append({"name": name, "scope": surface, "value": raw})
            continue
        rr = RES["light"].get(name) or RES["lp"].get(name)
        val, kind = (rr.get("value", rr["raw"]), rr["kind"]) if rr else (raw, "other")
        leaf, why = tokenise(name, val, kind, name[2:],
                             f"css-var {name} on {sel} ({surface} sheet)" +
                             (f", resolved to {val!r}" if rr else " (declared value, unresolved)"))
        if leaf:
            put(app.setdefault(surface, {}), [name[2:]], leaf)
        else:
            not_tokenised["app"].append({"name": name, "value": raw, "why": why})

# class-scoped component vars are internals, not tokens — count them into notTokenised once
class_scoped = sorted({n for r in V["app"] if r["selector"].startswith(".--")
                       for n in r["properties"]})
app = {k: v for k, v in app.items() if v}   # drop surfaces with no loose root vars (lp)
not_tokenised["app"].append({
    "name": f"{len(class_scoped)} class-scoped vars (.--name_value selectors)",
    "value": ", ".join(class_scoped[:12]) + (" …" if len(class_scoped) > 12 else ""),
    "why": "component-internal custom properties on utility classes, not design tokens; "
           "the declarations are preserved in raw/css-vars.json under `app`"})

# ----------------------------------------------------------------------------- measured component geometry

COMP_TOKENS = [
    # (token path suffix, component key, state, property: 'w'|'h', description)
    ("header.height", "shell-header", "default", "h", "the consumer marketplace header bar"),
    ("header.heightMobile", "m-header", "default", "h", "the mobile sticky header"),
    ("button.height", "b2b-cta", "default", "h", "the standard 48 px marketing/app button"),
    ("field.height", "auth-email-field", "default", "h", "the sign-in email field"),
    ("field.heightPartner", "partner-email-field", "default", "h", "the partner sign-in email field"),
    ("field.searchHelp.width", "help-search", "default", "w", "the help-centre search pill at 1440"),
    ("card.venue.width", "lp-venue-card", "default", "w", "a browse-card column at 1440"),
    ("card.plan.width", "plan-card", "default", "w", "a /pricing plan card"),
    ("card.businessType", "business-type-card", "default", "w", "a /for-business business-type tile"),
    ("cart.booking.width", "booking-cart", "default", "w", "the booking wizard's summary column"),
    ("nav.flyout.width", "nav-flyout", "default", "w", "the 'Business types' mega-menu"),
]
for suffix, key, state, dim, desc in COMP_TOKENS:
    st = (COMP["components"].get(key, {}).get("states") or {}).get(state)
    if not st or not st.get("rect"):
        continue
    v = st["rect"][dim]
    put(core, ["component"] + suffix.split("."),
        {"$value": "%gpx" % v, "$type": "dimension",
         "$description": desc,
         "$extensions": {"source": f"measured {key} {state} on {COMP['components'][key].get('page', 'the captured page')}"
                                  f" (raw/components-computed.json)"}})

# ----------------------------------------------------------------------------- motion

if MOTION:
    group, nt = motion_mod.build(MOTION)
    core["motion"] = group
    not_tokenised["core"].extend(nt)

# ----------------------------------------------------------------------------- checks

def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


CORE_NAMES = {n for n, _ in tokens_of(core)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for setname, tree in (("light", light), ("dark", dark), ("accent", accent),
                      ("app", app), ("core", core)):
    names = CORE_NAMES | {n for n, _ in tokens_of(tree)}
    for n, t in tokens_of(tree):
        for a in aliases(t["$value"]):
            if a not in names:
                raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")

# theme sets should name the same tokens; warn (never fail) where a scope genuinely
# lacks a declaration — the accent probe carries no consumer sheets, for one.
lnames, dnames, anames = ({n for n, _ in tokens_of(s)} for s in (light, dark, accent))
if lnames != dnames:
    print("warn: dark lacks:", sorted(lnames - dnames)[:8], "… has extra:", sorted(dnames - lnames)[:8])
if lnames != anames:
    print("warn: accent lacks:", sorted(lnames - anames)[:8], "… has extra:", sorted(anames - lnames)[:8])

for tree, nt in ((light, not_tokenised["light"]), (dark, not_tokenised["dark"]),
                 (accent, not_tokenised["accent"]), (core, not_tokenised["core"]),
                 (app, not_tokenised["app"])):
    if nt:
        tree.setdefault("$extensions", {})["notTokenised"] = nt

tokens = {
    "core": core, "light": light, "dark": dark, "accent": accent, "app": app,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled", "app": "enabled"},
         "$description": "The signed-out default on every captured surface: www.fresha.com, the B2B marketing app, the /lp/ microsite and partners.fresha.com's light state all paint these values."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled", "app": "enabled"},
         "$description": "Painted on the partners.fresha.com sign-in, which sets data-theme=\"auto\", under prefers-color-scheme: dark. On the consumer and B2B routes the same declarations exist but nothing signed out sets data-theme, so there they are declared-only evidence."},
        {"id": "accent", "name": "Accent", "selectedTokenSets": {"core": "source", "accent": "enabled", "app": "enabled"},
         "$description": "The [data-theme=accent] scope the partner sheets declare (a violet section theme). No signed-out element was observed carrying data-theme=accent — declared-only evidence."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark", "accent", "app"]},
}
if vendor:
    tokens["$extensions"] = {"vendor": vendor[:200]}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")

print({k: sum(1 for _ in tokens_of(tokens[k])) for k in ("core", "light", "dark", "accent", "app")})
print("notTokenised:", {k: len(v) for k, v in not_tokenised.items()}, "vendor:", len(vendor))
