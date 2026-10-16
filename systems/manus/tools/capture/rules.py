#!/usr/bin/env python3
"""Read the foundation values Manus keeps in utility classes rather than custom properties, and
write raw/css-rules.json. Added on the 2026-10-17 refresh to close the scorecard's foundation gaps.

    python3 tools/capture/rules.py <dir of the downloaded .css chunks> [SNAPS dir]

Manus is Tailwind 3 over CSS variables (see vars.mjs), so its shadows, spacing, z-index layers,
border widths, focus treatment and reduced-motion rules live in utility classes. This script reads
them from the same stylesheet chunks vars.mjs parses and, where a count says more than a list,
counts how many elements carry each class in the page copies (SNAPS, outside the repository; only
the counts are written). Every reading names where it came from:

  namedShadows    the shadow-* utilities Manus defines by name (shadow-card, shadow-layer,
                  shadow-menu) plus Tailwind's defaults it ships, parsed into layers
  measuredShadows the box-shadow each measured component paints (raw/components-computed.json),
                  grouped by value, with the shadow class that sets it
  focusVisible    every rule that styles :focus-visible / :focus-within, by what it changes
  reducedMotion   every rule inside @media (prefers-reduced-motion: ...)
  zIndex          every z-* utility and its value, and the z classes on the overlays in the copies
  spacing         Tailwind spacing utilities (p, m, gap, space) by step, with element counts
  borderWidth     every border-width utility, and the widths the measured components paint
  pressed         the active: utilities (what a pressed control changes)
  disabled        the disabled: utilities
  grid            grid-cols-* utilities with element counts
  brand           <meta name="theme-color"> from the page copies
Deterministic for the same inputs.
"""
import collections, json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parents[2]
RAW = HERE / "raw"
css_dir = pathlib.Path(sys.argv[1]).expanduser()
_snaps = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("SNAPS")
snaps = pathlib.Path(_snaps).expanduser() if _snaps else None
HTML = sorted(snaps.glob("*.html")) if snaps and snaps.is_dir() else []

CSS = {f.name: f.read_text() for f in sorted(css_dir.glob("*.css"))}


def unescape(sel):
    return re.sub(r"\\(.)", r"\1", sel)


def rules(css):
    """(context, selector, body) for every style rule, walking @media/@supports blocks."""
    out, stack, i, n, buf = [], [], 0, len(css), ""
    while i < n:
        ch = css[i]
        if ch == "{":
            head, buf = buf.strip(), ""
            if head.startswith("@"):
                stack.append(head)
            else:
                j = css.index("}", i)
                out.append((tuple(stack), head, css[i + 1:j]))
                i = j
        elif ch == "}":
            if stack:
                stack.pop()
            buf = ""
        else:
            buf += ch
        i += 1
    return [(c, s, b) for c, s, b in out if not any(x.startswith("@keyframes") for x in c)]


ALL = [(f, ctx, sel, body) for f, css in CSS.items() for ctx, sel, body in rules(css)]
CLS = collections.Counter()
for h in HTML:
    for m in re.finditer(r'\sclass="([^"]*)"', h.read_text()):
        for c in set(m.group(1).split()):
            CLS[c] += 1


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return [x for x in out if x]


def decl(body, prop):
    m = re.search(r"(?:^|;)\s*" + re.escape(prop) + r"\s*:\s*([^;]+)", body)
    return m.group(1).strip() if m else None


# ---------- shadows
named = {}
for f, ctx, sel, body in ALL:
    m = re.fullmatch(r"\.(shadow-[a-z][a-z0-9-]*)", unescape(sel))
    if m and not ctx and decl(body, "--tw-shadow"):
        v = decl(body, "--tw-shadow")
        named[m.group(1)] = {"file": f, "value": v, "layers": split_top(v), "elements": CLS[m.group(1)] + CLS["hover:" + m.group(1)]}

comps = json.loads((RAW / "components-computed.json").read_text())["components"]
measured = collections.defaultdict(lambda: {"components": set(), "classes": set()})
for key, c in sorted(comps.items()):
    for sname, s in c["states"].items():
        st = s.get("style")
        if not st or s.get("theme") != "dark":
            continue
        layers = [l for l in split_top(st.get("boxShadow", "none")) if l != "none" and not l.startswith("rgba(0, 0, 0, 0) 0px 0px 0px 0px")]
        if not layers:
            continue
        v = measured[", ".join(layers)]
        v["components"].add(f"{key}:{sname}")
        v["classes"].update(x for x in s.get("classes", "").split() if re.match(r"(hover:|focus[a-z-]*:)?shadow-", x))
measuredShadows = sorted(({"value": k, "components": sorted(v["components"]), "classes": sorted(v["classes"])} for k, v in measured.items()),
                         key=lambda x: (-len(x["components"]), x["value"]))

# ---------- focus, reduced motion, pressed, disabled
focus = collections.defaultdict(list)
reduced, pressed, disabled = [], collections.Counter(), collections.Counter()
for f, ctx, sel, body in ALL:
    u = unescape(sel)
    if ":focus-visible" in u or ":focus-within" in u:
        props = set(re.findall(r"(?:^|;)\s*([a-z-]+)\s*:", body))
        kind = ("outline" if any(p.startswith("outline") for p in props) else "ring" if any("ring" in p for p in props)
                else "shadow" if props & {"box-shadow", "--tw-shadow"} else "border" if any(p.startswith("border") for p in props)
                else "fill" if "background-color" in props else "other")
        focus[("focus-visible" if ":focus-visible" in u else "focus-within") + " " + kind].append({"selector": u[:160], "body": body[:200], "file": f})
    rm = [c for c in ctx if "prefers-reduced-motion" in c]
    if rm:
        reduced.append({"media": rm[0], "selector": u[:160], "body": body[:160], "file": f})
    m = re.fullmatch(r"\.active:(\S+):active", u)
    if m:
        pressed[m.group(1)] = CLS["active:" + m.group(1)]
    m = re.fullmatch(r"\.disabled:(\S+):disabled", u)
    if m:
        disabled[m.group(1)] = CLS["disabled:" + m.group(1)]
focusVisible = {k: {"rules": len(v), "examples": v[:6]} for k, v in sorted(focus.items())}

# ---------- z-index
z = {}
for f, ctx, sel, body in ALL:
    m = re.fullmatch(r"\.(-?z-(?:\[-?\d+\]|\d+))", unescape(sel))
    if m and decl(body, "z-index"):
        z[m.group(1)] = {"value": int(decl(body, "z-index")), "elements": CLS[m.group(1)]}
overlay_z = collections.Counter()
for h in HTML:
    for m in re.finditer(r'<(\w+)\s([^>]*)>', h.read_text()):
        attrs = m.group(2)
        cm = re.search(r'class="([^"]*)"', attrs)
        if not cm:
            continue
        cls = cm.group(1).split()
        zc = [c for c in cls if re.fullmatch(r"-?z-(\[-?\d+\]|\d+)", c)]
        if not zc:
            continue
        what = ("dialog" if 'role="dialog"' in attrs else "toast viewport" if m.group(1) == "ol" and "fixed" in cls
                else "sidebar" if m.group(1) == "nav" else "fixed layer" if "fixed" in cls else None)
        if what:
            for c in zc:
                overlay_z[f"{what}: {c}"] += 1

# ---------- spacing
STEP = re.compile(r"^-?(p|px|py|pt|pr|pb|pl|ps|pe|m|mx|my|mt|mr|mb|ml|ms|me|gap|gap-x|gap-y|space-x|space-y)-(\d+(?:\.\d+)?|\[\d+(?:\.\d+)?px\])$")
spacing = collections.Counter()
for c, n in CLS.items():
    m = STEP.match(c)
    if m:
        s = m.group(2)
        spacing[float(s[1:-3]) if s.startswith("[") else float(s) * 4] += n
spacingScale = [{"px": k, "elements": v, "onFourPxGrid": k % 4 == 0} for k, v in sorted(spacing.items())]

# ---------- border widths
bw_util = {}
for f, ctx, sel, body in ALL:
    m = re.fullmatch(r"\.(border(?:-[trblxyse])?(?:-\d+|-\[[\d.]+px\])?)", unescape(sel))
    w = re.search(r"border[a-z-]*-width\s*:\s*([^;]+)", body)
    if m and not ctx and w:
        bw_util[m.group(1)] = {"width": w.group(1).strip(), "elements": CLS[m.group(1)]}
bw_measured = collections.defaultdict(set)
for key, c in comps.items():
    for sname, s in c["states"].items():
        st = s.get("style") or {}
        for side in ("Top", "Right", "Bottom", "Left"):
            w = st.get(f"border{side}Width")
            if w and w != "0px" and st.get(f"border{side}Style") not in (None, "none"):
                bw_measured[w].add(key)

# ---------- grid
grid = {}
for f, ctx, sel, body in ALL:
    m = re.fullmatch(r"\.((?:[a-z0-9@\[\]:-]+:)?grid-cols-\S+)", unescape(sel))
    if m and decl(body, "grid-template-columns"):
        grid[m.group(1)] = {"value": decl(body, "grid-template-columns")[:80], "elements": CLS[m.group(1)]}

# ---------- brand
brand = collections.defaultdict(set)
for h in HTML:
    for m in re.finditer(r'<meta name="theme-color" content="([^"]+)"', h.read_text()):
        brand["theme-color"].add(m.group(1))

out = {
    "readAt": "2026-10-17",
    "source": f"{len(CSS)} stylesheet chunks from files.manuscdn.com (the list in vars.mjs), parsed as text; element counts from {len(HTML)} redacted page copies of the 2026-10-17 refresh; measured shadows and border widths from raw/components-computed.json (dark states)",
    "namedShadows": dict(sorted(named.items())),
    "measuredShadows": measuredShadows,
    "focusVisible": focusVisible,
    "reducedMotion": reduced,
    "zIndex": {"utilities": dict(sorted(z.items(), key=lambda x: (x[1]["value"], x[0]))), "overlays": dict(sorted(overlay_z.items()))},
    "spacing": spacingScale,
    "borderWidth": {"utilities": dict(sorted(bw_util.items())), "measured": {k: sorted(v) for k, v in sorted(bw_measured.items(), key=lambda x: float(x[0][:-2]))}},
    "pressed": dict(sorted(pressed.items())),
    "disabled": dict(sorted(disabled.items())),
    "grid": dict(sorted(grid.items())),
    "brand": {k: sorted(v) for k, v in brand.items()},
}
(RAW / "css-rules.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print({k: len(v) for k, v in out.items() if k not in ("readAt", "source")})
