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
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-primary-inverse", "button-outline", "button-quiet", "button-accent", "button-update", "button-danger"],
     "Five looks. Accent-filled (`button-primary`: Create Project, Invite, and the Delete in the delete confirmation); ink-filled pill (`button-primary-inverse`: New Automation, Browse Marketplace); outline (`button-outline` in Settings: Open); quiet text (`button-quiet`: Cancel); the accent Update pill in the sidebar footer. Hover and pressed share one fill (`bg.accent-primary-hover` = `bg.accent-primary-pressed`). Disabled and loading were not seen."),
    ("Icon button", ["icon-button", "dialog-close", "voice-button", "send-button", "icon-picker"],
     "Ghost 24 x 24 squares with a 6px radius (`radius.base`); the icon is `text.secondary`-ish at 66% and turns `text.primary` on a `bg.tertiary` wash under the pointer. The voice and send buttons are ink circles."),
    ("Link", ["text-link", "text-button-accent", "link"],
     "Text links are `text.link` (blue). Inline actions such as Authenticate are accent-coloured text buttons; links inside agent replies are medium weight."),
    ("Text field", ["settings-search", "search-field", "search-field-outlined", "text-field", "palette-input", "select-search"],
     "Search fields sit on a 3% wash (`bg.input-surface`-like) with a 1px `stroke.secondary` edge that turns `stroke.primary` on focus; Customize's is a pill. The Models filter is an older VS Code input (`ide.input-*`)."),
    ("Text area", ["composer", "composer-editor"],
     "The composer: `seed.elevated` fill, 1px `stroke.secondary` edge, 20px radius, 15/24 prompt text. Typing changes nothing but the send button, which appears in place of the voice button."),
    ("Select", ["select-text", "select-outline", "model-button", "select-popover", "listbox", "option", "option-selected", "select-option"],
     "Two triggers: text-only (environment, branch; `text.secondary`, 6px radius) and outlined (Settings; 1px `stroke.secondary`). Popovers are raised (`seed.elevated`) with a search field on top and 30px rows."),
    ("Checkbox", ["menu-toggle-row"], "Not present as a box. A checkable menu item (`menuitemcheckbox`, the model menu's Fast row) draws a small switch instead."),
    ("Radio", ["option-selected", "tab-selected"], "Not present as radio buttons. Single choice is a select listbox with a check on the selected option, or a tab strip."),
    ("Switch", ["switch-on", "switch-off", "switch-disabled", "switch-sm", "switch-sm-off", "switch-sm-off"],
     "32 x 20 (`size.control.switch-*`), green when on (`data-variant=green`, `bg.success-primary`); 26 x 16 inside menus. Disabled keeps its state at reduced contrast (Reduce Transparency)."),
    ("Tabs", ["tab", "tab-selected", "tabs-list", "conversation-tab"],
     "Pill tabs: `text.secondary` at rest, `bg.tertiary` fill and `text.primary` when selected, 28px high. The palette's filter row and Automations' Mine/Team use the same component (`data-component=tabs-item`)."),
    ("Menu", ["menu", "context-menu", "submenu", "command-menu", "menu-row", "menu-toggle-row", "menu-submenu-trigger", "menu-section-title", "menu-separator", "menu-footer", "command-option", "menu-search"],
     "Raised popups (`seed.elevated`, 12 to 14px radius) with 26 to 30px rows, an 8px row radius, a `bg.tertiary` highlight, separators inset 14px, section titles in 12px `text.tertiary`, and submenus that open to the side."),
    ("Context menu", ["context-menu", "menu-row", "menu-separator"], "A right-click on an agent row opens the same menu component, positioned at the pointer."),
    ("Tooltip", ["tooltip"], "A raised label with the shortcut in `text.tertiary` beside the name (Search ⌘K), below the trigger after a hover delay."),
    ("Dialog", ["dialog", "confirm-dialog", "palette", "backdrop"],
     "Modal dialogs are raised (`seed.elevated`), 12px radius, a 1px `stroke.secondary` edge, over a black 40% scrim (`role.scrim`). The search palette is the translucent variant: 84% chrome with a 16px backdrop blur and the large shadow."),
    ("Toast", [], "Not captured. Cursor mounts a Sonner toaster (`[data-sonner-toaster]`, with its own light and dark variables in raw/css-vars.*.json), but no action taken during the capture raised a toast."),
    ("Card", ["template-card", "feature-banner", "field-group", "hover-card", "info-banner", "banner", "file-card"],
     "Cards are raised fills with a 12px radius and a 1px inset ring of `stroke.tertiary` instead of a border; Settings groups rows on a 6% wash (`bg.card`). The info banner is accent-tinted."),
    ("List row", ["sidebar-row", "sidebar-row-selected", "agent-row", "palette-row", "palette-row-selected", "list-row", "field-row", "explorer-row", "settings-nav", "settings-nav-selected"],
     "30px rows with an 8px radius; selection is a text change (`text.secondary` to `text.primary`) plus a `bg.tertiary` wash, and per-row actions (pin, archive) appear on hover."),
    ("Table", ["table", "table-header", "table-row"], "The Automations list: a raised, 12px-radius container with 41px header and 48px rows, a hairline between rows, and a 6% hover wash."),
    ("Avatar", ["avatar"], "28px circle with initials on a tinted fill, in the sidebar footer."),
    ("Badge", ["badge", "status-badge", "kbd"], "20px pills on `bg.tertiary` with `text.secondary` 12px text (Plugin, the sidebar's ⌘N); keyboard hints are plain `text.tertiary` glyphs."),
    ("Toolbar", ["ide-button", "titlebar", "status-bar"], "The Agents window has no toolbar beyond its 40px title bar (`layout.titlebar-height`) with icon buttons; the IDE window has a title bar, an activity bar and a 22px status bar."),
    ("Inspector", ["agent-pane", "apps-rail"], "The IDE's right-hand agent pane (422px) and, in a conversation, the Agents window's collapsed apps rail (Changes, Browser, Terminal, Files)."),
    ("Conversation", ["user-message", "assistant-message", "step-group-header", "turn-actions", "code-block", "inline-code"],
     "Not on the checklist; the core of the product. The user's prompt is a raised bubble (12px radius, a 10px backdrop blur); the agent's reply is plain text on the page; work collapses into one muted line (Worked for 13s); feedback icons sit under each turn."),
    ("Progress and sliders", ["progress", "slider", "number-field"], "Usage bars (8px, full radius), sliders and number steppers in Settings."),
]
GAPS = [
    "Toast: no action raised one (the toaster is mounted; its variables are in raw/css-vars.*.json).",
    "Approval prompt: the test command ran without one, because the owner's agent settings auto-run commands; nothing was changed to force it.",
    "Disabled and loading buttons, a form validation error and an error state were not seen in the reachable screens.",
    "Checkbox and radio buttons do not exist in the captured screens (switches, selects and tabs take their place).",
    "Onboarding: the account is set up; the only first-run surfaces are the empty-state callouts (Import your Claude Code conversations, Meet Grok Bot).",
    "Focus-visible states were captured with `data-focus-ring` set on the Agents window's root by the capture: without it Cursor draws no focus ring at all (see README).",
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
CORE_NAMES = re.compile(r"^(text|bg|stroke|icon)\.(primary|secondary|tertiary|quaternary|quinary|on-primary|link|elevated|chrome|sidebar|card|accent-primary(-hover|-pressed)?|focus-ring)$")
PREFER = ["role", "text", "bg", "stroke", "seed", "icon", "glass", "ide"]


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
BY_PROP = {"background-color": ["bg.", "role.accent", "role.", "seed."], "color": ["text.", "role.text", "icon.", "role."],
           "border-top-color": ["stroke.", "role.border", "role."]}


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


lines = ["# Cursor desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Cursor 3.27.6 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "before the window's 0.84 zoom (see the README). States: hover is a real pointer over the part, focus-visible real keyboard focus "
         "with the focus-ring switch the capture set, pressed `:active` forced through the DevTools protocol.", ""]
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
