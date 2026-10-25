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
from prefer import skip  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-default", "button-outline", "button-destructive", "button-ghost", "button-secondary", "button-xs", "button-default-xs", "button-outline-icon", "command-button"],
     "shadcn/ui's button in five variants. Default is the ink fill (`base.primary`: near-black in light, near-white in dark) with `base.primary-foreground` text, for the one action that commits (Update, Sign in to Orca, Install skills, New Automation); outline (`base.background` fill, `base.input` edge, a light shadow) for everything else in Settings and dialogs; destructive is the red fill (`base.destructive`) and appears only as the confirm button of a removal; ghost has no fill until hover (`base.accent`); secondary is the `base.secondary` grey. Sizes default 36, sm 32, xs 24px, all with the 8px radius (`radius.md`). Hover takes the fill to 90%; there is no separate pressed style. Disabled is the same control at 50% opacity (the empty composer's send button)."),
    ("Icon button", ["icon-button", "new-tab", "right-tab", "attach-button", "dictation-button", "send-button", "sidebar-search"],
     "Ghost squares whose icon is `base.muted-foreground` and turns `base.foreground` on a `base.accent` wash under the pointer. The chat's send button is the one round, filled icon button (`base.primary`, at 50% while the composer is empty)."),
    ("Link", ["link"],
     "Links are the text colour with an underline, not a hue: in agent replies (hello.txt) and the update card's Release notes. `callout.note` blue is kept for notes and unread markers."),
    ("Text field", ["input", "settings-search", "find-field", "filter-field", "search-field", "palette-input"],
     "shadcn's input: 36px, `base.input` edge, 8px radius; focus turns the edge `base.ring` and adds a 3px ring of `base.ring` at 50%. Settings search carries a shortcut hint (Command F)."),
    ("Text area", ["composer", "composer-editor", "textarea"],
     "The chat composer is a 14px-radius box on `chat.composer-surface` with a `chat.composer-border` edge and a toolbar row (attach, permission mode, model, dictation, send). The Add Quick Command dialog has a plain textarea for the command."),
    ("Select", ["select", "listbox", "option", "option-selected", "permission-button", "model-button"],
     "shadcn's select: an outlined 36px trigger with a chevron; its listbox is a raised popover (`base.popover`) with a check on the selected option. The composer's permission and model pickers are ghost triggers that open menus."),
    ("Checkbox", ["checkbox"], "shadcn's checkbox, 16px with a 4px radius, in Settings > SSH Hosts. Most yes or no settings are switches instead."),
    ("Radio", ["radio", "radio-on"], "Single choice is a segmented radio group (`role=radiogroup`): Theme (System, Dark, Light) and Agent Permissions (Manual, Auto, Yolo). The selected segment gets a `base.accent` fill and medium weight; the others are `base.muted-foreground`. The capture only hovered, focused and pressed these; it never chose one."),
    ("Switch", ["switch-on", "switch-off"],
     "shadcn's switch: `base.primary` when on (ink), `base.input` when off, a `base.background` thumb. Hover changes nothing; focus adds the 3px ring."),
    ("Tabs", ["tab", "tab-active", "right-tab", "right-tab-active", "toggle-item", "toggle-item-on", "segmented-item", "segmented-active"],
     "Three kinds. Workspace tabs across the top (terminal, chat, browser), the active one marked by an underline; icon tabs in the right sidebar (Explorer, Agents, Source Control, Checks), also underlined; and segmented toggles (Names and Contents, Issues and PRs) where the selected item takes a filled chip."),
    ("Menu", ["menu", "menu-item", "menu-item-checked", "menu-item-destructive", "menu-separator", "menu-shortcut", "popover"],
     "shadcn's dropdown menu, restyled: a translucent fill (`component.menu.bg`, black at 72% in dark, white at 82% in light) with a backdrop blur, a 14% edge, an 11px radius and its own shadow (`shadow.menu`); 32px items with a 7px radius and a translucent highlight, shortcuts right-aligned in `base.muted-foreground`, separators of `base.border`. The destructive item (Remove Project) is red text. The new-tab menu lists every installed agent with its logo."),
    ("Context menu", ["context-menu", "context-item", "context-separator", "context-label"],
     "Right-clicking a workspace opens the same menu component with a section label (Workspace), submenus (Move to Status, Open in) and a red Remove at the bottom."),
    ("Tooltip", ["tooltip"], "A small inverted label (`base.foreground` fill, `base.background` text, 8px radius, 12px text) with an arrow, beside the trigger after a hover delay."),
    ("Dialog", ["dialog", "confirm-dialog", "overlay", "palette", "palette-row", "palette-filter", "palette-section-heading"],
     "shadcn's dialog, restyled: the popover colour at 96% (`role.overlay`), a 14% edge, a 10px radius and a deep shadow (`shadow.dialog`), over a black 55% overlay with a light blur. The removal confirmation is the small variant: title, one sentence with the project name in bold, Cancel (outline) and Remove (destructive). The search palette is a dialog with a search row, a Filter button, sections and keyboard hints."),
    ("Toast", ["toast"],
     "Orca's update notice is a card pinned bottom right (`role=complementary`, `base.card`, the floating shadow) with a title, close button, two lines and a full-width default button. Orca also mounts a Sonner toaster (its variables are in raw/css-vars.*.json); no action raised one."),
    ("Card", ["card", "card-title", "setup-card", "template-card", "activity-card", "card-header", "step-row", "step-row-selected"],
     "Settings groups are bordered, rounded cards on `base.card` with an h3 title; the Appearance pane nests collapsible cards with an icon tile. The onboarding callout (Add a setup script) and the Automations templates are smaller cards with a `base.border` edge."),
    ("List row", ["nav-row", "nav-row-selected", "workspace-row", "settings-nav", "settings-nav-selected", "back-to-app", "project-header", "field-label", "field-description"],
     "Sidebar rows have an 8px radius: `base.foreground` text with a muted icon and a `worktreeSidebar.accent` wash on hover and when selected. The workspace card (main, primary) is a taller row with a status dot, a badge, the branch and its agents. Settings rows put a 14px medium label over a 12px muted description, with the control on the right."),
    ("Table", [], "Not measured: Tasks shows a table header (ID, Title / Context, Assignees, Status, Updated) over an empty state, in [tasks](screenshots/dark/tasks.png) and [tasks light](screenshots/light/tasks.png); the header was not matched as a part, and no rows were reachable without connecting a task source."),
    ("Avatar", [], "Not present: Orca shows no people. Agent logos sit in rounded tiles in Settings > Agents and the onboarding checklist."),
    ("Badge", ["workspace-badge", "badge"], "Small outlined pills (primary on the main workspace, 11 detected) and plain uppercase labels (OPTIONAL, BETA; New in an ink pill)."),
    ("Toolbar", ["status-bar", "status-chip", "command-button"],
     "The window has no toolbar beyond the tab strip (tabs, New tab, Command) and a status bar of usage chips (per-provider limits, memory, terminals, ports, hosts) in 11px muted text."),
    ("Inspector", ["right-tab", "right-tab-active", "find-field", "toggle-item"],
     "The right sidebar (350px) is the inspector: Explorer with a file filter and a Names and Contents toggle, the agent session history, Source Control with untracked changes, and Checks."),
    ("Conversation", ["user-message", "assistant-message", "turn-status", "tool-call", "code-block", "context-usage"],
     "Not on the checklist; Orca's structured chat. The user's prompt is a right-aligned bubble (`chat.user-surface`, `chat.user-border`, 14px radius); the reply is plain text on the canvas; the turn collapses into a Worked for 11s line that expands to tool calls (a terminal icon, the command, a check) and the agent's narration in mono; code blocks sit on `chat.code-surface` with a 10px radius."),
    ("Terminal", ["terminal", "terminal-pane-title"],
     "The terminal pane is xterm drawn with the owner's terminal themes (Ghostty Default Style Dark, Builtin Tango Light) in 14px SF Mono; its colours come from the terminal theme, not the app's tokens."),
    ("Progress and sliders", ["slider", "slider-thumb", "collapsible"], "A shadcn slider in Settings > Terminal and collapsible sections."),
]
GAPS = [
    "Approval prompt: none appeared. The owner's Agent Permissions setting is Yolo and the chat's permission mode is Full access; the capture changed neither.",
    "Toast: only Orca's update card was on screen; no action raised a Sonner toast.",
    "Avatar: Orca shows no people; nothing to capture.",
    "Table: Tasks has no rows without a connected task source (GitHub, Linear, Jira); only the header and empty state were captured.",
    "A form validation error, an error state and a loading button were not reachable without changing settings.",
    "Chat appearance settings appear only when Settings > Experimental > Chat UI is on; it is off and was left off, so they were not captured. The structured chat itself was opened per launch with `orca agent launch --surface chat`.",
    "The onboarding flow's inline command terminal runs an install (Install skills); the capture opened the checklist steps but did not start it.",
    "Orca Account: not signed in, and the capture did not sign in; cloud features (artifact sharing, Orca Relay) show their signed-out state.",
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
CORE_NAMES = re.compile(r"^base\.(background|foreground|card|popover|primary|primary-foreground|secondary|muted|muted-foreground|accent|accent-foreground|border|input|ring|destructive)$")
PREFER = ["base", "role", "sidebar", "worktreeSidebar", "chat", "status", "callout", "color"]


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
BY_PROP = {"background-color": ["base.", "worktreeSidebar.", "chat.", "role."], "color": ["base.", "chat.", "role.text", "role."],
           "border-top-color": ["base.", "chat.", "role.border", "role."]}


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
        if d["state"] == state and part in d["parts"] and not skip(shot, part, state):
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


lines = ["# Orca desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Orca 1.4.237 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "at UI Zoom 100%. States: hover is a real pointer over the part, focus-visible real keyboard focus (Orca draws its own ring), "
         "pressed `:active` forced through the DevTools protocol with the pointer over the part.", ""]
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
