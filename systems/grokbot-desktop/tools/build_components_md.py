#!/usr/bin/env python3
"""Write components.md from raw/components.<theme>.json, tokens.json and components/crops/.

    python3 tools/build_components_md.py

One entry per checklist component (docs/DESIGN-SYSTEM.md, desktop wording), listing the parts that
show it, the states captured in each theme with their crops, and the measured values written as the
token that holds them (the value after it). A value no token holds is written raw and counted.
PRODUCT (adapt): INVENTORY, NOTES and GAPS. Standard library only, deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "selected", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-primary-disabled", "button-secondary", "button-tonal", "button-danger", "button-invite", "update-pill"],
     "Pill buttons, 32px high. The primary is ink (`bg.primary`, the theme's text colour) with `text.on-primary` (Create in the New Bot dialog), and its disabled look is the same ink at 13% (`bg.primary-disabled`) until a name is typed. Secondary buttons (Cancel, Add account, Sign Out) sit on a 4% wash with a hairline; the Add buttons in Connect Apps are tonal; the destructive confirmation's Delete is red (`bg.danger-primary`). The sidebar's Update button is an accent-blue circle. Pressing scales a control to 98% (`press.scale`)."),
    ("Icon button", ["icon-button", "attach-button", "mic-button", "voice-button", "send-button", "dialog-close", "icon-button-close", "copy-link", "connect-apps"],
     "Circles: 36px in the sidebar header and footer (Search, New Bot, Connect apps) on a 4% wash, 28px in the composer. The voice-chat button is filled with the open Bot's colour; it becomes the send arrow once text is typed. Settings rows show a small link icon on hover (copy a link to the setting)."),
    ("Link", ["link", "pr-pill"], "Links in replies are underlined text in the reply's colour; a pull request is a pill with the GitHub mark (`pr-pill`). Both were measured while scrolled above the window, so neither has a crop."),
    ("Text field", ["text-field", "palette-input", "search-field", "inspector-name"],
     "The New Bot name field is a centred, 8px-radius field on the raised fill; the palette's and Connect Apps' search fields are borderless inside their dialogs; the inspector's Bot name is an inline field that looks like a title."),
    ("Text area", ["composer", "prompt-field"],
     "The composer is a full-width pill (`bg.elevated` fill, hairline, 999px radius) with an attach button, the prompt and the voice buttons. Typing swaps the voice-chat button for send; the placeholder names the open Bot, or asks for an answer while a question card is open."),
    ("Select", ["select", "listbox", "option", "option-selected"],
     "Settings selects are 28px triggers with a hairline and a chevron; their listbox is a raised popover with a check on the selected option. The Accent list adds every Bot's name, so the accent can follow one Bot."),
    ("Checkbox", [], "Not present in the reachable screens; switches take its place."),
    ("Radio", ["shape-option", "shape-option-selected", "color-swatch"],
     "Not present as radio buttons. Single choice in the New Bot dialog is a grid of Bot shapes and a row of colour swatches; the chosen one gets a ring."),
    ("Switch", ["switch-on", "switch-accent"],
     "32 x 20. On is the accent: blue in Settings, and the open Bot's colour in that Bot's inspector (Routines). Off was not visible in the reachable settings."),
    ("Tabs", ["tab", "tab-selected", "filter-pill", "filter-pill-selected"],
     "The inspector's Details, Library and Computer tabs are pill tabs: `text.secondary` at rest, a wash and `text.primary` when selected. Connect Apps' categories are filter pills; the selected one is ink-filled."),
    ("Menu", ["menu", "submenu", "menu-row", "menu-row-highlighted", "menu-submenu-trigger", "menu-banner", "menu-row-danger"],
     "Raised popovers (`bg.elevated`, 12px `menu.radius`, a hairline) with 30px rows (`menu.row-height`), a 6px row radius and a wash under the pointer. The account menu leads with an update banner on an accent tint; a submenu opens beside it (Weekly usage, Support)."),
    ("Context menu", ["context-menu", "menu-row-danger"], "A right-click on a Bot opens the same menu at the pointer: Unpin or Pin, Mark as Unread, Copy conversation ID, Hide from sidebar, and Delete in `text.danger-primary`."),
    ("Tooltip", ["tooltip"], "A small raised label with the shortcut beside the name, after a hover delay (`tooltip.*` metrics)."),
    ("Dialog", ["dialog", "confirm-dialog", "settings-dialog", "palette", "backdrop"],
     "Dialogs are raised (`bg.elevated`), 16 to 18px radius, over a black scrim (`bg.scrim`, 70%). Settings is the large dialog with its own navigation; the destructive confirmation is a small one with full-width Cancel and Delete; the search palette is the 14px-radius command palette."),
    ("Toast", [], "Not captured: no action taken during the capture raised one (copying a conversation ID would, and was not done, since it writes to the clipboard)."),
    ("Card", ["account-card", "settings-group", "question-card", "link-card", "inspector"],
     "Cards are raised fills with a 14 to 18px radius and no border: Settings groups rows into them, the account card holds the profile, a Bot's question is a card of lettered options in the transcript, and the inspector lists a Bot's pull request as a card."),
    ("List row", ["pinned-tile", "list-row", "list-row-selected", "section-header", "section-header-open", "settings-nav", "settings-nav-selected", "palette-row", "palette-row-selected", "settings-row"],
     "Pinned Bots are 90 x 92 tiles (avatar over name) with a 10px radius (`botItem.radius`); grouped Bots are rows with a preview line; group headers are 30px rows with a count that turns into a chevron under the pointer. Selection is a wash (`bg.secondary-hover`) with no colour."),
    ("Table", [], "Not present: lists are rows and cards."),
    ("Avatar", ["avatar", "bot-avatar"], "The account avatar is initials on a faint wash; Bots are drawn as coloured characters (one of fourteen shapes, eleven colours), with a group shown as a cluster."),
    ("Badge", ["pr-pill"], "Unread Bots carry a small accent dot; counts beside group names are plain `text.tertiary` numbers; a pull request is a pill."),
    ("Toolbar", ["chat-header"], "No toolbar: the conversation's title is a floating pill (the Bot's mark and name) that opens the inspector."),
    ("Inspector", ["inspector", "inspector-name", "tab", "tab-selected"], "The right-hand pane a Bot's title opens: its character, name, label, then Details (coding work, routines), Library (pages and files it made) and Computer (its screen). Opening it widens the window."),
    ("Conversation", ["user-message", "agent-message", "message-prose", "inline-code", "question-card", "time-separator", "row-timestamp", "system-event"],
     "Not on the checklist; the core of the product. The owner's messages are right-aligned bubbles filled with the open Bot's colour (`fill.<hue>-bubble-user`); the Bot's replies are left-aligned bubbles on a 4% wash (`transcript.bubble-agent-fill`), 18px radius, 22px line height. While a Bot works the transcript ends in its mark and a shimmering activity line (Thinking it through, Listing the directory files)."),
    ("Progress", ["progress"], "The weekly usage bar in Usage & Billing."),
]
GAPS = [
    "Toast: no action taken during the capture raised one.",
    "Approval prompt: none appeared. The owner's Settings > Computer > Execution on this computer is Always allow, so the test Bot listed, wrote and read files in the scratch folder without asking; nothing was changed to force one.",
    "Disabled was seen only on the New Bot dialog's Create button; loading buttons, a form validation error and an error state were not reachable.",
    "Checkbox, radio buttons and tables do not exist in the reachable screens.",
    "Onboarding: the account is signed in, so the app's first-run flow (sign-in, computer setup) was not shown. A new Bot's own first message, a question card with lettered options, is captured.",
    "About 20 settings views ship in the bundle; the five in the Settings dialog (General, Computer, Vault, Usage & Billing, Updates) were reachable. The rest belong to Bot settings, team and admin flows that were not opened.",
    "Focus-visible states were captured after a real Tab press: Grok Bot paints no focus ring until a Tab press sets `[data-sand-keyboard-nav]` on the root.",
    "Switch off: every switch in the reachable settings was on.",
]

def flat(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from flat(v, prefix + (k,))


CORE = dict(flat(TOK["core"]))
SETS = {t: dict(flat(TOK[t])) for t in ("light", "dark")}
CORE_NAMES = re.compile(r"^(text|bg|border|icon)\.(primary|secondary|tertiary|quaternary|on-primary|accent-primary(-hover)?|pane|chrome|sidebar|elevated|scrim|"
                        r"(primary|secondary|tertiary|quaternary)-translucent)$")
PREFER = ["role", "text", "bg", "border", "fill", "icon", "transcript", "prompt", "specular", "kit"]


def resolve(t, v):
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v):
        p = tuple(v[1:-1].split("."))
        v = (SETS[t].get(p) or CORE[p])["$value"]
    return v


def colour_index(t):
    idx = {}
    for p, tok in SETS[t].items():
        if tok["$type"] == "color" and p[0] in PREFER:
            idx.setdefault(resolve(t, tok["$value"]), []).append(p)
    for v in idx.values():
        v.sort(key=lambda p: (not CORE_NAMES.match(".".join(p)), PREFER.index(p[0]), len(".".join(p)), p))
    return {k: [".".join(x) for x in v] for k, v in idx.items()}


# The token group a value is looked up in first, by the property it was read from.
BY_PROP = {"background-color": ["bg.", "fill.", "transcript.", "role.accent", "role."], "color": ["text.", "role.text", "icon.", "role."],
           "border-top-color": ["border.", "role.border", "role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "spacing", "fontSize", "lineHeight", "letterSpacing"):
    for p, tok in CORE.items():
        if p[0] == group and isinstance(tok["$value"], str):
            DIDX.setdefault((group, tok["$value"]), ".".join(p))
stats = {"written": 0, "token": 0}


def as_token(t, prop, raw):
    stats["written"] += 1
    if prop in ("background-color", "color", "border-top-color") and is_color(raw):
        v = color(raw)
        if v == "rgba(0, 0, 0, 0)":
            stats["written"] -= 1
            return None
        if v in CIDX[t]:
            stats["token"] += 1
            return f"`{pick(CIDX[t][v], prop)}` {v}"
        return f"{v}"
    m = re.fullmatch(r"([\d.]+)px", raw)
    if m:
        v = "%gpx" % round(float(m.group(1)))
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if v == "9999px" and prop == "border-top-left-radius":
            stats["token"] += 1
            return "`radius.full`"
        if (group, v) in DIDX:
            stats["token"] += 1
            return f"`{DIDX[(group, v)]}` {v}"
        if prop == "font-weight":
            stats["written"] -= 1
            return None
        return v
    stats["written"] -= 1
    return None


PROPS = [("background-color", "fill"), ("color", "text"), ("border-top-color", "edge"), ("border-top-left-radius", "radius"),
         ("height", "height"), ("padding-left", "padding"), ("font-size", "size"), ("line-height", "line")]


def first(t, part, state):
    for shot, d in CAP[t].items():
        if d["state"] == state and part in d["parts"]:
            return shot, d["parts"][part]["style"]
    return None, None


def states_of(t, part):
    return sorted({d["state"] for d in CAP[t].values() if part in d["parts"]}, key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99)


def crop_links(part, state):
    out = []
    for suffix, label in (("", "dark"), ("-light", "light")):
        name = f"{part}-{state}{suffix}.png"
        if name in CROPS:
            out.append(f"[{label}](components/crops/{name})")
    return " ".join(out)


lines = ["# Grok Bot desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Grok Bot 0.75.5 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "before the window's 1.1 zoom (see the README). States: hover is a real pointer over the part, focus-visible real keyboard focus "
         "after a Tab press, pressed `:active` forced through the DevTools protocol (nothing was clicked).", ""]
lines.append("| Component | Parts | Captured |")
lines.append("|---|---|---|")
for name, parts, note in INVENTORY:
    present = [p for p in parts if states_of("dark", p) or states_of("light", p)]
    lines.append(f"| [{name}](#{name.lower().replace(' ', '-')}) | {len(present)} | {'yes' if present else 'not captured'} |")
lines.append("")
seen = set()
for name, parts, note in INVENTORY:
    lines += [f"## {name}", "", note, ""]
    rows = []
    for part in dict.fromkeys(parts):
        for state in sorted(set(states_of("dark", part)) | set(states_of("light", part)), key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99):
            vals = []
            for t in ("dark", "light"):
                shot, s = first(t, part, state)
                if not s:
                    continue
                cells = [f"{label} {v}" for prop, label in PROPS if not (prop == "border-top-color" and s.get("border-top-width") == "0px") and (v := as_token(t, prop, s.get(prop, "")))] if (part, state, t) not in seen else []
                seen.add((part, state, t))
                vals.append(f"{t}: " + "; ".join(cells) if cells else f"{t}: see crop")
            rows.append(f"| `{part}` | {state} | {crop_links(part, state) or 'no crop'} | {'<br>'.join(vals)} |")
    if rows:
        lines += ["| Part | State | Crops | Values |", "|---|---|---|---|"] + rows + [""]
lines += ["## Gaps", ""] + [f"- {g}" for g in GAPS] + [""]
lines.insert(4, f"{stats['token']} of {stats['written']} values written below are tokens ({round(100 * stats['token'] / max(1, stats['written']))}%); the rest no token holds and are written raw.")
lines.insert(5, "")
(PKG / "components.md").write_text("\n".join(lines))
print("components.md", len(INVENTORY), "components", stats)
