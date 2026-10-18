#!/usr/bin/env python3
"""Build components.md for the ChatGPT design reference.

Reads raw/components-computed.json (every component and state, measured in both themes),
raw/layout.json, tokens.json, screenshots/ and icons/INDEX.tsv, and writes components.md next to
them. Every value is a cell of the measurement file, condensed and written in tokens: a colour is the
token in the matching theme's set whose value is the same, a radius, padding or size the core token
that holds it; the raw value is written only where no token holds it. A state row shows only what
differs from the first state. Dark states come first (the pages were
captured dark); the light reading of the same state follows as `light`, `light-hover` and so on.
Adapted from the Manus kit's builder.

Deterministic: re-running it on the same inputs reproduces components.md byte for byte.
Run from anywhere: python3 tools/build_components_md.py
"""
import collections, json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
J = json.load(open("raw/components-computed.json"))
C = J["components"]
META = J["_meta"]
LAYOUT = json.load(open("raw/layout.json"))
T = json.load(open("tokens.json"))

# --------------------------------------------------------------------------- colours and tokens


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY_COLOR = {"dark": {}, "light": {}}


def resolved(theme, v, depth=0):
    while isinstance(v, str) and v.startswith("{") and depth < 12:
        node = T[theme]
        for k in v[1:-1].split("."):
            node = node.get(k) if isinstance(node, dict) else None
        if node is None:
            node = T["core"]
            for k in v[1:-1].split("."):
                node = node.get(k) if isinstance(node, dict) else None
        v, depth = (node or {}).get("$value"), depth + 1
    return v


for theme in ("dark", "light"):
    for n, t in flat(T[theme]):
        if t["$type"] == "color" and not n.startswith("chatTheme.") or n.startswith("chatTheme.blue."):
            v = resolved(theme, t["$value"])
            if not isinstance(v, str) or v.startswith("{"):
                continue
            # computed styles round alpha to two places (#ffffff0a reads back as rgba(255, 255, 255, 0.04))
            key = re.sub(r"(\d+\.\d+)\)", lambda m: f"{round(float(m.group(1)), 2):g})", v)
            BY_COLOR[theme].setdefault(key, []).append(n)

# Which token a colour is named after depends on what it paints: a fill prefers the interactive and
# surface names, a border the border names, text the text names. The captured accent is blue.
PREFER = {
    "bg": ["role.bg.", "surface.", "bg.", "variant.primary.", "variant.secondary.", "variant.", "scrim.", "token.", "gray.", "component."],
    "border": ["role.border.", "border.", "ring.", "token.border", "variant.", "gray."],
    "text": ["role.text.", "text.", "variant.", "token.text", "gray."],
    "icon": ["role.text.", "text.", "variant.", "token.text", "gray."],
}
# Names that hold a value for one specific place: chosen only when no general token holds the value.
SPECIFIC = re.compile(r"tooltip|mode-toggle|home-suggestion|other-user-message|activity|coachmark|composer-action|control-opaque|recovery|execution|attribution|internal-badge|business|viewer|artifact|codex|usage|file|avatar|media|device|chatgpt-blue|discovery|caution|unread|message-reaction|charts")


def pick(names, role):
    order = PREFER.get(role, PREFER["bg"])
    def rank(n):
        for i, pre in enumerate(order):
            if n == pre or (pre.endswith((".", "-")) and n.startswith(pre)):
                return (bool(SPECIFIC.search(n)), i, len(n), n)
        return (True, len(order), len(n), n)
    return sorted(names, key=rank)[0]

THEME = ["dark"]  # the theme the colour() helper looks tokens up in; set per state


def norm(r, g, b, a=None):
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), round(float(a), 2))


def _gam(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def _clamp255(v):
    return round(min(1, max(0, v)) * 255)


def oklab_rgb(L, a, b):
    l, m, s = ((L + 0.3963377774 * a + 0.2158037573 * b) ** 3, (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, (L - 0.0894841775 * a - 1.291485548 * b) ** 3)
    return [_clamp255(_gam(v)) for v in (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s)]


def lab_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    finv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X, Y, Z = finv(fx) * 0.3457 / 0.3585, (fy ** 3 if L > k * e else L / k), finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
    y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
    z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
    return [_clamp255(_gam(v)) for v in (3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z, -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z, 0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z)]


def unlab(c):
    """Tailwind 4 writes opacity modifiers as color-mix, which Chromium computes as lab() or oklab();
    both go back to rgb() here so they read like every other colour."""
    def f(m):
        L = float(m.group(2).rstrip("%")) * (0.01 if m.group(2).endswith("%") else 1)
        r, g, b = (oklab_rgb if m.group(1) else lab_rgb)(L, float(m.group(3)), float(m.group(4)))
        return f"rgba({r}, {g}, {b}, {m.group(5)})" if m.group(5) else f"rgb({r}, {g}, {b})"
    return re.sub(r"(ok)?lab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+))?\)", f, c)


# Core dimensions by value, so a padding, radius or height is written as the token that holds it.
BY_DIM = {}
for n, t in flat(T["core"]):
    if t["$type"] == "dimension" and isinstance(t["$value"], str) and t["$value"].endswith("px"):
        BY_DIM.setdefault(n.split(".")[0], {}).setdefault(t["$value"], []).append(n)


def dtok(v, group, prefer=()):
    """'8px' -> '`spacing.2`' when a core token in `group` holds it, else the value."""
    if v in ("0px", "0", "full"):
        return "0" if v != "full" else "`radius.full`"
    names = BY_DIM.get(group, {}).get(v)
    if not names:
        return v
    names = sorted(names, key=lambda n: (not any(n.startswith(p) for p in prefer), "named" in n or "-base" in n, len(n), n))
    return f"`{names[0]}`"


def dims(v, group, prefer=()):
    return " ".join(dtok(x, group, prefer) for x in v.split())


def full(r):
    """rounded-full is calc(infinity * 1px), which computes to 33554400px."""
    return re.sub(r"[\d.e+]+px", lambda m: "full" if float(m.group(0)[:-2]) >= 10000 else m.group(0), r)


def colour(c, tokens=True, role="bg"):
    """rgb()/rgba()/color(srgb)/lab()/oklab() -> '#hex `token`' or 'rgba(...)'."""
    def label(v):
        if re.fullmatch(r"rgba\(\d+, \d+, \d+, 0\)", v):
            return "transparent"
        names = BY_COLOR[THEME[0]].get(v) if tokens else None
        return f"`{pick(names, role)}`" if names else v

    c = unlab(c)
    c = re.sub(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)",
               lambda m: label(norm(*(round(float(x) * 255) for x in m.group(1, 2, 3)), m.group(4))), c)
    return re.sub(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", lambda m: label(norm(*m.group(1, 2, 3), m.group(4))), c)


def sides(t, r, b, l):
    if t == r == b == l:
        return t
    if t == b and r == l:
        return f"{t} {r}"
    return f"{t} {r} {b} {l}"


def fam(f):
    first = f.split(",")[0].replace('"', "").strip()
    return {"-apple-system-body": "System", "-apple-system": "System", "ui-sans-serif": "System", "ui-monospace": "Mono", "OpenAI Sans": "OpenAI Sans"}.get(first, first)


def num(x):
    return re.sub(r"(\d+\.\d\d)\d+", r"\1", str(x))


TYPE = {}
for n, t in flat(T["core"]):
    if t["$type"] == "typography":
        v = t["$value"]
        fam_ = "mono" if "mono" in str(v["fontFamily"]) else "sans"
        TYPE.setdefault((fam_, v["fontSize"], v["lineHeight"], str(v["fontWeight"])), []).append(n)


def font(fz, lh, fw, f):
    """A text style as the core typography token with the same family, size, line height and
    weight, else family size/line-height weight."""
    fam_ = "mono" if fam(f) == "Mono" else "sans"
    rank = lambda n: (not n.startswith("typography.text-") and not n.startswith("typography.heading-"), len(n), n)
    names = TYPE.get((fam_, fz, lh, str(fw)))
    if names:
        return f"`{sorted(names, key=rank)[0]}`"
    wt = next((f"`{n}`" for n, t in flat(T["core"]) if n.startswith("fontWeight.") and str(t["$value"]) == str(fw)), fw)
    same = sorted((n for (fm, z, l, w), ns in TYPE.items() for n in ns if fm == fam_ and z == fz and l == lh and re.match(r"typography\.(text|heading)-", n)), key=rank)
    if same:
        return f"`{same[0]}` at {wt}"
    size = next((f"`{n}`" for n, t in flat(T["core"]) if n.startswith("fontSize.") and t["$value"] == fz), None)
    lh_ = lh.replace("px", "") if lh != "normal" else "normal"
    if size:
        return f"{size}/{num(lh_)} {wt}" + (" mono" if fam_ == "mono" else "")
    return f"{fam(f)} {num(fz.replace('px', ''))}/{num(lh_)} {fw}"


def scale_of(t):
    m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), (-?[\d.]+), (-?[\d.]+)\)", t or "")
    if m and m.group(1) == m.group(2) and m.group(1) != "1":
        return f"scale({num(m.group(1))})"
    return None


def pseudo(p):
    """A painted ::before or ::after, in tokens; None when it paints nothing."""
    if not p or p.get("opacity") == "0":
        return None
    bits = []
    if p.get("backgroundColor") not in (None, "rgba(0, 0, 0, 0)", "transparent"):
        bits.append(colour(p["backgroundColor"]))
    if p.get("boxShadow") not in (None, "none"):
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", colour(p["boxShadow"], tokens=False))]
        layers = [x for x in layers if not x.startswith("transparent") and not re.fullmatch(r"(rgba\(0, 0, 0, 0\)|#0000|#00000000) 0px 0px 0px 0px( inset)?", x)]
        if layers:
            bits.append("shadow " + ", ".join(layers))
    if not bits:
        return None
    sc = scale_of(p.get("transform"))
    if sc:
        bits.append(sc)
    if p.get("opacity") not in (None, "1"):
        bits.append(f"opacity {p['opacity']}")
    return ", ".join(bits)


def props(v):
    s = v["style"]
    o = {}
    h = "%gpx" % round(v["rect"]["h"], 2)
    ht = dtok(h, "size", ("size.control.",))
    o["size"] = f"{num(v['rect']['w'])} x {ht if ht.startswith('`') else num(v['rect']['h'])}"
    pad = sides(s["paddingTop"], s["paddingRight"], s["paddingBottom"], s["paddingLeft"])
    if pad != "0px":
        o["padding"] = dims(pad, "spacing", ("spacing.",))
    bds = []
    for d in ("Top", "Right", "Bottom", "Left"):
        if float(s[f"border{d}Width"].replace("px", "")) > 0 and s[f"border{d}Style"] != "none":
            bds.append(f"{s[f'border{d}Width']} {s[f'border{d}Style']} {colour(s[f'border{d}Color'], role='border')}")
        else:
            bds.append("none")
    if any(b != "none" for b in bds):
        o["border"] = bds[0] if len(set(bds)) == 1 else "; ".join(f"{'TRBL'[i]}: {b}" for i, b in enumerate(bds) if b != "none")
    rad = full(sides(s["borderTopLeftRadius"], s["borderTopRightRadius"], s["borderBottomRightRadius"], s["borderBottomLeftRadius"]))
    if rad != "0px":
        o["radius"] = dims(rad, "radius", ("radius.",))
    o["background"] = colour(s["backgroundColor"])
    if s["backgroundImage"] != "none":
        img = re.sub(r'url\("data:[^)]*\)', "an image (data URI)", s["backgroundImage"])
        o["image"] = colour(img)[:200]
    if s["boxShadow"] != "none":
        sh = colour(s["boxShadow"], tokens=False)
        layers = [x.strip() for x in re.split(r",(?![^(]*\))", sh)]
        layers = [x for x in layers if not x.startswith("transparent") and not re.search(r" 0px 0px 0px [1-9]", x) and not re.fullmatch(r"#ffffff 0px 0px 0px 0px( inset)?", x)]
        if layers:
            o["shadow"] = ", ".join(layers)
    if s.get("backdropFilter", "none") != "none":
        o["backdrop"] = s["backdropFilter"]
    # ChatGPT's Button paints its fill on ::before (hover and pressed change that layer, not the
    # element), so both pseudo-elements are part of every state's values.
    for pe in ("::before", "::after"):
        layer = pseudo(v.get(pe))
        if layer:
            o[pe] = layer
    if s["outlineStyle"] != "none" and float(s["outlineWidth"].replace("px", "")) > 0:
        o["outline"] = f"{s['outlineWidth']} {s['outlineStyle']} {colour(s['outlineColor'], role='border')}, offset {s['outlineOffset']}"
    ring = re.search(r"(rgb\([^)]*\)) 0px 0px 0px ([1-9][\d.]*px)( inset)?", s["boxShadow"])
    if ring:
        o["focus ring"] = f"`size.focusRing.width` box-shadow ring{' (inset)' if ring.group(3) else ''} in {colour(ring.group(1), role='border')}" if ring.group(2) == "2px" else f"{ring.group(2)} ring in {colour(ring.group(1), role='border')}"
    t = v.get("textStyle")
    if t:
        o["text"] = f"{font(t['fontSize'], t['lineHeight'], t['fontWeight'], t['fontFamily'])}, {colour(t['color'], role='text')}"
    elif v.get("text"):
        o["text"] = f"{font(s['fontSize'], s['lineHeight'], s['fontWeight'], s['fontFamily'])}, {colour(s['color'], role='text')}"
    if s["transitionDuration"] not in ("0s", ""):
        props_ = [x.strip() for x in s["transitionProperty"].split(",")]
        durs = [x.strip() for x in s["transitionDuration"].split(",")]
        tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", s["transitionTimingFunction"])
        parts = []
        for i, p in enumerate(props_):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tf[i % len(tf)] if tf else ''}".strip())
        if parts:
            o["transition"] = ", ".join(parts) if len(parts) < 4 else f"{parts[0].split(' ')[0]} and {len(parts) - 1} more {' '.join(parts[0].split(' ')[1:])}"
    if s["transform"] not in ("none", "matrix(1, 0, 0, 1, 0, 0)"):
        m = re.fullmatch(r"matrix\(([\d.]+), 0, 0, ([\d.]+), (-?[\d.]+), (-?[\d.]+)\)", s["transform"])
        if m and m.group(1) == m.group(2) and m.group(3) == m.group(4) == "0":
            o["transform"] = f"scale({m.group(1)})"
        elif m and m.group(1) == m.group(2) == "1":
            o["transform"] = f"translate({m.group(3)}px, {m.group(4)}px)"
        else:
            o["transform"] = s["transform"]
    if s["opacity"] != "1":
        o["opacity"] = s["opacity"]
    ic = v.get("icon")
    if ic and ic.get("w", 0) > 0 and ic["w"] < 120:
        o["icon"] = f"{num(ic['w'])} x {num(ic['h'])}, {colour(ic.get('color') or ic.get('stroke') or ic.get('fill'), role='icon')}"
    if v.get("placeholder"):
        o["placeholder"] = colour(v["placeholder"]["color"], role="text")
    return o


ORDER = ["size", "padding", "border", "radius", "background", "image", "shadow", "::before", "::after", "backdrop", "outline", "focus ring", "text", "transition", "transform", "opacity", "icon", "placeholder"]


def state_rows(c):
    """Dark states first, then light. Each theme has its own base row (the first state of that
    theme), later rows of the same theme list only what changed."""
    rows = []
    for theme in ("dark", "light"):
        states = [s for s, v in c["states"].items() if "style" in v and v.get("theme") == theme]
        if not states:
            continue
        THEME[0] = theme
        base = props(c["states"][states[0]])
        trows = [(states[0], base)]
        same = []
        for st in states[1:]:
            p = props(c["states"][st])
            diff = {k: p[k] for k in ORDER if k in p and p.get(k) != base.get(k)}
            for k in ORDER:
                if k in base and k not in p:
                    diff[k] = "none"
            if not diff:
                same.append(st)
                continue
            if trows[-1][0] != states[0] and trows[-1][1] == diff:
                trows[-1] = (trows[-1][0] + ", " + st, diff)
            else:
                trows.append((st, diff))
        if same:
            trows[0] = (f"{states[0]} (same: {', '.join(same)})", base)
        rows += trows
    return rows


def fmt(d):
    return "; ".join(f"{k} {d[k]}" for k in ORDER if k in d).replace("|", "/")


def child_layers(c, theme="dark"):
    st = next((s for s in c["states"].values() if "style" in s and s.get("theme") == theme), None)
    if not st or not st.get("paint"):
        return None
    s = st["style"]
    if s["backgroundColor"] != "rgba(0, 0, 0, 0)" or s["boxShadow"] != "none" or s["borderTopWidth"] != "0px" or s["backgroundImage"] != "none":
        return None
    THEME[0] = theme
    out = []
    for p in st["paint"][:3]:
        node = p["node"].split(".")[0] + ("::" + p["node"].split("::")[1] if "::" in p["node"] else "")
        bits = [node, " x ".join("%g" % round(float(n), 2) for n in re.findall(r"[\d.]+", p["size"])[:2])]
        if p.get("bg"):
            bits.append("background " + colour(p["bg"]))
        if p.get("bgImage"):
            bits.append("background " + colour(p["bgImage"], tokens=False))
        if p.get("border"):
            bits.append("border " + colour(p["border"].split(" | ")[0][2:], role="border"))
        if p.get("radius"):
            bits.append("radius " + full(p["radius"]))
        if p.get("shadow"):
            bits.append("shadow " + colour(p["shadow"]))
        out.append(" ".join(bits))
    return "; ".join(out).replace("|", "/")


# --------------------------------------------------------------------------- page and group text

GROUP_INTRO = {
    "Sidebar": "The sidebar every page shares (`aside.LeftPanel`, 340 wide at 1440): a 52px header with search and hide, the destination rows (New chat, Images, Scheduled, Library, Plugins, Explore), then the Pinned, Projects and Recents sections and the account row. Rows are 36 tall and fully round; hover and the current row rest on the same translucent fill. Hiding it leaves the 52 wide rail.",
    "Top bar": "The 52px page header (`<header>`, fixed, z-index 30): the Chat / Work toggle centred on the home, Upgrade and the temporary-chat button at the end; in a thread Upgrade, Share and More.",
    "Home": "The new-chat page: one heading over the composer, three suggestion rows, and the Plus nudge card at the bottom.",
    "Composer": "The composer shared by the home and a thread: a 768 wide pill with the + button, the ProseMirror field, Think, Dictate and the voice button, which becomes Send once there is text.",
    "Thread": "A conversation: the user bubble in the accent colour, the assistant's markdown (paragraphs, headings, strong, inline code, code blocks, tables, links), the actions under a turn and the scroll-to-bottom button. Message text in the copies is same-length filler.",
    "Feedback": "What ChatGPT shows around an action, from a temporary chat (one prompt sent, nothing saved to the history): the pulsing dot and the Stop button while the answer streams, the toast after a failed Copy (the capture browser refuses clipboard writes, so the success state could not be shown), and the Save chat popover a temporary chat offers after its first answer.",
    "Menus": "The popovers: the chat row menu, the composer + menu (a popover of buttons, not a role=menu), the account menu, a notification channel's checkbox menu and the accent colour listbox. Menus are 90% surfaces with an 8px backdrop blur.",
    "Dialogs": "The delete confirmation (420 wide, a danger action and Cancel) and the global search dialog with its filter tabs and empty state.",
    "Library": "The file library: title, filter, grid and list view buttons, search, New, pill tabs, then a masonry grid of file cards with a hover checkbox. Also its error state and a partial-results banner.",
    "Images": "The Images page: Trending and Templates tabs over a grid of template cards (OpenAI's own sample images).",
    "Plugins": "The plugin store: Plugins / Skills tabs, a search field and plugin rows. The installed plugins were blanked in the copy.",
    "Settings": "The settings page (a full page since the redesign, not a dialog): a left nav, then panes of 60 to 64 tall rows with switches, select buttons, outline buttons and danger buttons.",
    "Pricing": "The Upgrade dialog: a full-screen sheet with a Personal / Business radio segment and plan cards.",
    "Signed out": "The public chatgpt.com a visitor without an account sees, read in a clean browser: Log in and Sign up for free in the header, a sign-in nudge card in the sidebar, and the Log in or sign up dialog with its provider buttons, email field and Continue. Continue with an incomplete address shows the field's error state. This page uses its own atomic CSS, not the app's `Button` modules.",
    "Phone": "The same app at 390 wide: the header, the two-row composer, the drawer, the user bubble and a code block.",
}

PAGE_DESC = [
    ("home", "Home. Captured at rest, with a tooltip, the + menu, a chat row's menu, the account menu, the delete confirmation, the search dialog (empty and with no results), a line typed in the composer, with the sidebar hidden, and a new temporary chat.", "/"),
    ("thread", "Two threads, their text replaced by same-length filler: one with code blocks (at the bottom, and at its user turn), one with a table and citations. Also a temporary chat with one prompt sent: while its answer streams, and after Copy on its code block (the error toast and the Save chat popover).", "/c/<id>"),
    ("library", "Library, grid view, Suggested tab; loading (the capture held the file list request open, so the grid shows its shimmer cards); the error state (the capture guard refused the file list request) and a search with a partial-results banner.", "/library"),
    ("images", "Images, Trending tab.", "/images"),
    ("plugins", "Plugins.", "/plugins"),
    ("settings", "Settings: General, Appearance (and its accent listbox), Keyboard, Data controls, Archived chats, Notifications (with a channel menu open).", "/settings/..."),
    ("pricing", "The Upgrade dialog over the home.", "/#pricing"),
    ("onboarding", "Signed out, in a clean browser with no account: the home, the Log in or sign up dialog, and the dialog after Continue with an incomplete address (the email error).", "/ (signed out)"),
]
MOBILE_DESC = [
    ("mobile-home", "Home at 390, and the drawer.", "/"),
    ("mobile-thread", "The code thread at 390, top and bottom.", "/c/<id>"),
]

# Which measured entries show each component of the checklist in docs/DESIGN-SYSTEM.md.
CHECKLIST = [
    ("Button", ["promo-button", "button-secondary", "button-danger", "button-outline", "library-new", "pricing-primary", "button-disabled", "onb-continue", "onb-login-header", "onb-provider"]),
    ("Icon button", ["header-icon-button", "sidebar-icon-button", "composer-plus", "voice-button", "send-button", "stop-button", "code-block-button"]),
    ("Link", ["md-link", "text-link", "archived-link", "header-upgrade"]),
    ("Text field", ["search-field", "library-search", "plugins-search", "archived-search", "color-field", "onb-email", "onb-email-error"]),
    ("Text area", ["composer"]),
    ("Select", ["select", "code-theme-select", "accent-menu"]),
    ("Checkbox", ["checkbox", "checkbox-menu-item"]),
    ("Radio", ["segmented-radio", "mode-segment"]),
    ("Switch", ["switch-on", "switch-off", "keyboard-switch"]),
    ("Tabs", ["library-tab", "search-tab", "images-tab", "plugins-tab"]),
    ("Menu", ["chat-menu", "menu-item", "menu-item-danger", "plus-menu", "user-menu"]),
    ("Tooltip", ["tooltip"]),
    ("Dialog", ["confirm-dialog", "search-dialog", "pricing-dialog", "dialog-backdrop", "onb-dialog"]),
    ("Toast", ["toast", "toast-close", "save-chat"]),
    ("Card", ["promo-card", "library-card", "library-loading", "pricing-card", "image-card", "onb-nudge"]),
    ("List row", ["chat-row", "nav-row", "search-result", "archived-row", "plugin-row", "plugin-row-link", "settings-row"]),
    ("Table", ["md-table", "md-th", "md-td"]),
    ("Avatar", ["avatar"]),
    ("Badge", ["badge"]),
]


L = []


def W(s=""):
    L.append(s)


shots = sorted(p.name for p in Path("screenshots").glob("*.png"))


def links(prefix):
    out = []
    for f in shots:
        m = re.fullmatch(re.escape(prefix) + r"-(dark|light)-(.+)\.png", f)
        if m and not (prefix == "home" and f.startswith("home-") and False):
            out.append(f"[{m.group(2)} ({m.group(1)})](screenshots/{f})")
        elif re.fullmatch(re.escape(prefix) + r"-(dark|light)\.png", f):
            out.append(f"[default ({f.split('-')[-1][:-4]})](screenshots/{f})")
    return ", ".join(out)


n_crops = len(list(Path("components/crops").glob("*.png")))
n_states = sum(len(c["states"]) for c in C.values())
icons = [r.split("\t") for r in open("icons/INDEX.tsv").read().strip().split("\n") if not r.startswith("#")][1:]

W("# ChatGPT components")
W()
W(f"The discovery list of every page and state captured, the checklist coverage, the shared values, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from chatgpt.com on {META['read']}, signed in to the owner's account (Free plan, dark theme, blue accent), as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Phone group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was created or deleted in the account. Apart from one prompt sent in a temporary chat (not saved to the history) for the streaming and feedback states, the only actions were hovering, keyboard focus, opening menus and dialogs and closing them, and typing into the composer and the search fields without sending.")
W()
W(f"The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) ({len(C)} components, {n_states} states). Page geometry is in [raw/layout.json](raw/layout.json).")
W()
W("How to read an entry:")
W()
W("- Values are written as tokens from [tokens.json](tokens.json): a colour is the token in that theme's set whose value is the same (`role.text.primary`, `surface.card`, `variant.primary.soft.bg-hover`), a padding, radius or control height the core token that holds it (`spacing.2`, `radius.2xl`, `size.control.lg`). Text is the typography style with the same size, line height and weight (`typography.text-sm`), that style at another weight, or a `fontSize` token with its line height and a `fontWeight` token, then its colour. A raw value is written only where no token holds it.")
W("- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example \"default (same: pressed)\". When the root paints nothing, \"Child layers\" names the first nodes inside it that do.")
W(f"- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) ({n_crops} files, named `{{component}}-{{state}}.png`, at 2x). Screenshots are in [screenshots/](screenshots).")
W()
W("## Discovery list")
W()
W("Screenshots are named `{page}-{theme}-{state}.png`, 1440 x 900 at 2x; `-full` shots are whole pages of the dark home, Library and Plugins; phone shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.")
W()
W("| Surface | URL | Screenshots |")
W("|---|---|---|")
for p, desc, url in PAGE_DESC + MOBILE_DESC:
    W(f"| {desc} | `{url}` | {links(p)} |")
W()

# --------------------------------------------------------------------------- checklist

W("## Checklist coverage")
W()
W("The 19 components of the checklist in [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md), with the entries below that show each one and the states measured across them.")
W()
W("| Component | Entries | States measured |")
W("|---|---|---|")
for name, keys in CHECKLIST:
    have = [k for k in keys if k in C]
    if not have:
        W(f"| {name} | not captured: ChatGPT shows a toast only after an action (copying, archiving, sharing), and the capture took no action | - |")
        continue
    states = sorted({re.sub(r"^light-?", "", s) or "default" for k in have for s, v in C[k]["states"].items() if "style" in v}, key=lambda x: ["default", "hover", "focus-visible", "pressed", "selected", "active", "checked", "open", "typed", "highlighted", "error"].index(x) if x in ["default", "hover", "focus-visible", "pressed", "selected", "active", "checked", "open", "typed", "highlighted", "error"] else 99)
    if any("disabled" in C[k]["title"].lower() for k in have):
        states.append("disabled")
    if any("loading" in C[k]["title"].lower() for k in have):
        states.append("loading")
    W(f"| {name} | {', '.join(f'[{k}](#{k})' for k in have)} | {', '.join(states)} |")
W()

# --------------------------------------------------------------------------- shared values

W("## Shared values")
W()
W("Values that apply across entries, tallied from the measurement file.")
W()
radii = collections.Counter()
trans = collections.Counter()
hover_dark = collections.Counter()
hover_light = collections.Counter()
focus = {"dark": collections.Counter(), "light": collections.Counter()}
focus_n = {"dark": 0, "light": 0}
for cid, c in C.items():
    for sname, s in c["states"].items():
        if "style" not in s:
            continue
        st = s["style"]
        r = full(st["borderTopLeftRadius"])
        if r != "0px" and s["rect"]["w"] > 4:
            radii[dtok(r, "radius", ("radius.",))] += 1
        if st["transitionDuration"] not in ("0s", ""):
            tf = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", st["transitionTimingFunction"])
            trans[f"{st['transitionDuration'].split(',')[0].strip()} {tf[0] if tf else st['transitionTimingFunction']}"] += 1
        if sname.endswith("focus-visible"):
            th = s["theme"]
            focus_n[th] += 1
            THEME[0] = th
            ring = re.search(r"(rgb\([^)]*\)) 0px 0px 0px ([1-9][\d.]*px)( inset)?", st["boxShadow"])
            after = next((p["outline"] for p in s.get("paint") or [] if p.get("outline") and p["node"].endswith("::after")), None)
            if ring:
                focus[th][f"a {ring.group(2)} box-shadow ring{' (inset)' if ring.group(3) else ''} in {colour(ring.group(1), role='border')}"] += 1
            elif st["outlineStyle"] == "solid" and float(st["outlineWidth"].replace("px", "")) > 0:
                focus[th][f"a {st['outlineWidth']} outline in {colour(st['outlineColor'], role='border')}, offset {st['outlineOffset']}"] += 1
            elif after:
                focus[th][f"a {after.split(' ')[0]} outline on ::after, offset {after.split('offset ')[-1]}"] += 1
            elif st["outlineStyle"] == "auto":
                focus[th]["the browser's own outline (auto)"] += 1
            else:
                focus[th]["no ring on the element"] += 1
for cid, c in C.items():
    for th, base, hov, ctr in (("dark", "default", "hover", hover_dark), ("light", "light", "light-hover", hover_light)):
        a, b = c["states"].get(base), c["states"].get(hov)
        if not a or not b or "style" not in a or "style" not in b:
            continue
        THEME[0] = th
        if a["style"]["backgroundColor"] != b["style"]["backgroundColor"]:
            ctr[f"{colour(a['style']['backgroundColor'])} to {colour(b['style']['backgroundColor'])}"] += 1
        elif a["style"]["color"] != b["style"]["color"]:
            ctr[f"text {colour(a['style']['color'], role='text')} to {colour(b['style']['color'], role='text')}"] += 1
        elif a["style"]["opacity"] != b["style"]["opacity"]:
            ctr[f"opacity {a['style']['opacity']} to {b['style']['opacity']}"] += 1
        elif pseudo(a.get("::before")) != pseudo(b.get("::before")):
            ctr[f"::before {pseudo(a.get('::before')) or 'transparent'} to {pseudo(b.get('::before')) or 'transparent'}"] += 1
        else:
            ctr["no change"] += 1
THEME[0] = "dark"
pressed_pairs = [(k, c["states"]["hover"], s) for k, c in C.items() for n, s in c["states"].items() if n == "pressed" and "style" in s and "style" in c["states"].get("hover", {})]
pressed_all = len(pressed_pairs)
pressed_diff = [k for k, h, s in pressed_pairs if props(h) != props(s)]
pressed_layers = collections.Counter(pseudo(s.get("::before")) for k, h, s in pressed_pairs if k in pressed_diff and pseudo(s.get("::before")) != pseudo(h.get("::before")))


def top(ctr, n):
    return ", ".join(f"{k} ({v})" for k, v in ctr.most_common(n))


W(f"**Radius.** {top(radii, 10)}.")
W()
W(f"**Hover.** Dark: {top(hover_dark, 6)}. Light: {top(hover_light, 6)}. Ghost buttons, menu items, rows and tabs all hover to `variant.primary.soft.bg-hover` (white at 10% in dark, black at 5% in light); solid neutral buttons drop to 80% opacity instead; the accent send and voice buttons do not change.")
W()
W(f"**Pressed.** {len(pressed_diff)} of {pressed_all} pressed readings (the mouse button held down, so `:active` applies) differ from hover. ChatGPT's `Button` paints its fill on `::before`, and `:active` swaps that layer to the variant's `-active` colour: {top(pressed_layers, 4)}, white at 16% where hover is 10%. The stylesheet also scales the layer by `--scale`, which no captured button sets, so nothing shrinks. The signed-out page's buttons change their own background instead. The rest (rows, links, tabs and the Tailwind-styled controls) set no `:active` style, so for them pressed is the hover state.")
W()
W(f"**Focus.** Of {focus_n['dark']} elements given a real keyboard focus in dark: {top(focus['dark'], 8)}. In light: {top(focus['light'], 8)}. The ring is `ring.default` (#3a83f7) at `size.focusRing.width` (2px) with no offset; rows draw it as an inset outline, ghost buttons on their ::after, links and segments fall back to the browser's outline.")
W()
W("**Disabled.** A disabled button keeps its variant's colours at 40% opacity (`component.button-disabled.opacity`): Restore defaults in Keyboard settings and Your current plan in the pricing dialog.")
W()
W(f"**Motion.** {top(trans, 6)}. Colour and opacity changes run at `duration.basic` (150 ms) on `easing.basic` or `easing.in-out`; the reduced-motion rules are listed under `core.duration.$extensions.reducedMotion` in [tokens.json](tokens.json).")
W()
W("**Layout.** The sidebar is 340 wide at 1440 (`--spacing-token-sidebar` clamps it between 240 and 520), the rail 52, the header 52 tall. The composer and thread share one 768 wide centred column. Settings panes are 768 wide. The Library is a masonry grid of 4 columns at 1440 (`core.layout.grid-columns-library`; `--masonry-columns` steps from 1 to 6 with the container width), Images a 5 column grid and the plugin store 2 columns. On a phone the sidebar is a 260 wide drawer over the page and the column is 358 wide at x 16.")
W()

# --------------------------------------------------------------------------- components

W("## Components")
W()
groups = collections.OrderedDict()
for cid, c in C.items():
    groups.setdefault(c["group"], []).append(cid)
for g, ids in groups.items():
    W(f"### {g}")
    W()
    if g in GROUP_INTRO:
        W(GROUP_INTRO[g])
        W()
    for cid in ids:
        c = C[cid]
        W(f"#### {c['title']}")
        W()
        W(f"<a id=\"{cid}\"></a>`{cid}`, on {', '.join(c.get('pages') or [c['page']])}. {c.get('desc', '') or ''}".rstrip())
        W()
        crops = []
        order = ("default", "hover", "focus-visible", "pressed", "light", "light-hover", "active", "selected", "checked", "open", "typed")
        for sname in [n for n in order if n in c["states"]] + sorted(n for n in c["states"] if n not in order):
            s = c["states"].get(sname)
            if s and s.get("crop") and Path(s["crop"]).exists():
                crops.append(f'<img src="{s["crop"]}" alt="{c["title"]}, {sname}" height="{min(120, max(24, round(s["rect"]["h"])))}"> ')
        if crops:
            W("".join(crops))
            W()
        rows = state_rows(c)
        if rows:
            W("| State | Values |")
            W("|---|---|")
            for name, d in rows:
                W(f"| {name} | {fmt(d)} |")
            W()
        cl, cll = child_layers(c), child_layers(c, "light")
        if cl:
            W(f"Child layers: {cl}" + (f". In light: {cll}" if cll and cll != cl else ""))
            W()

# --------------------------------------------------------------------------- icons

by_role = collections.Counter(r[1] for r in icons)
W("## Icon index")
W()
W(f"{len(icons)} icons were lifted from the sprite symbols inlined in the page copies into [icons/](icons), named by their sprite id. [icons/INDEX.tsv](icons/INDEX.tsv) indexes each by role, where it is drawn most ({', '.join(f'{k} {v}' for k, v in by_role.most_common())}), with every role it plays, its sprite id, viewBox, the sizes it was drawn at and the control it labels. ChatGPT draws them through `<use href=\"sprites-core-*.svg#name\">` at 20px (`size.icon.lg`), 16px (`size.icon.sm`) or 12px, filled in currentColor, paired with 14px labels in rows and menus and alone (with an aria-label) in 36px icon buttons. A few glyphs are CSS masks or inline SVG and are not in the folder. The icons are OpenAI's property, kept for reference only.")
W()
W("| Icon | Role | Sizes | Where it was used |")
W("|---|---|---|---|")
for r in icons:
    W(f"| `{r[0].replace('.svg', '')}` | {r[1]} | {r[5]} | {(r[8] if len(r) > 8 and r[8] else '-')[:60].replace('|', '/')} |")
W()

# --------------------------------------------------------------------------- gaps

W("## Gaps")
W()
W("- Toast: only the error toast was seen. The capture browser refuses clipboard writes, so Copy failed; the success state (the button's check mark) was not shown.")
W("- Loading: the Library's file shimmer (the capture held its request open) and a streaming answer (the pulsing dot and Stop) were captured as single frames; the animations themselves and the streaming text speed (`duration.animation-duration-streaming-text`, 700 ms) are from the CSS only. A button's own loader (`ButtonLoader`) was not seen.")
W("- Forms with a validation error and onboarding were read on the signed-out page, which is built with a different CSS system (atomic `x…` class names) from the signed-in app, so its values match the app's tokens only where the colours coincide. The account's own first-run flow is past.")
W("- Message text, chat, project and file titles, Library thumbnails and the installed plugins were replaced or blanked in the copies before they left the browser, so widths that depend on text are those of the filler.")
W("- Hover and focus on the 390 wide copies were not measured (a phone has neither).")
W("- The light theme was read by setting every `data-theme=\"dark\"` to light in the copies, not by changing the account's appearance. Only the Blue accent was captured; switching it is an account setting.")
W("- Not captured: voice mode, Work mode, Codex, Scheduled, a project page, the share dialog, the Account, Billing and Personalization panes, since each either spends quota, changes the account or shows account details. One prompt was sent, in a temporary chat, for the streaming and feedback states.")
W()

open("components.md", "w").write("\n".join(L) + "\n")
print(f"components.md: {len(C)} components, {n_states} states, {n_crops} crops, {len(L)} lines")
