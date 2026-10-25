# Orca desktop: patterns

How Orca's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

The window is three columns over a status bar. A 280px left sidebar (`core.layout.sidebar`, on `worktreeSidebar.default`) holds, from the top: the app name with Toggle sidebar and back and forward arrows; a Search row; Tasks, Automations and Orca Mobile; then Projects, with icon buttons (activity, view options, add project, new workspace), each project as a folder row and each worktree as a card (a status dot, the name, a `primary` badge, the branch, and one line per agent with its status and age). Settings and Help sit at the bottom. The middle column is the workspace: a 31px tab strip (terminals, chats, browser tabs, files) with New tab and Command, and the active tab below. The 350px inspector on the right (`core.layout.right-sidebar`) has four icon tabs: Explorer, the agent session history, Source Control and Checks. A 24px status bar runs along the bottom with usage chips per provider, memory, terminals, ports and hosts. Hiding the sidebar gives the workspace the full width; the workspace board lays the worktrees out as columns by status.

Settings replaces the whole window: a sidebar with Back to app, a search field, the onboarding checklist and about thirty panes in groups (AI capabilities, Set up, Workflows, Interface, Remote hosts, Privacy and security, Advanced, Experimental), and an 832px column of bordered cards (`core.layout.settings-card`).

Screens: [workspace-terminal](screenshots/dark/workspace-terminal.png), [sidebar-hidden](screenshots/light/sidebar-hidden.png), [workspace-board](screenshots/dark/workspace-board.png), [right-sidebar-agents](screenshots/dark/right-sidebar-agents.png), [right-sidebar-source-control](screenshots/light/right-sidebar-source-control.png), [settings-general](screenshots/dark/settings-general.png).

## Starting and following an agent

New agents start from the New tab menu (a terminal, a browser tab, a markdown file, or any installed agent CLI) or from Orca's CLI. In a terminal tab the agent is its own TUI. In Orca's structured chat (opt-in, opened here per launch) the empty tab centres an icon tile, "Start a chat with Claude" and one muted line, with the composer docked at the bottom of a 736px column (`core.layout.chat-content`): a 14px-radius box on `chat.composer-surface` whose toolbar has attach, the permission mode (Full access in amber), the model and effort, dictation and a round ink send button that stays at 50% until there is text.

A sent prompt becomes a right-aligned bubble (`chat.user-surface`). While the agent works, a spinner and "Working..." sit under a "Working for 4s" line, tool calls appear as one line each (a terminal icon, the command, a check when done) with the agent's narration in mono, and the tab and the sidebar card show a status dot. When the turn ends it folds into "Worked for 11s", and the reply follows as plain text with bold headings (Done, Follow-ups), underlined file links and code blocks on `chat.code-surface`. The Explorer shows a created file at once, coloured as untracked.

Screens: [chat-empty](screenshots/dark/chat-empty.png), [chat-composer-typed](screenshots/light/chat-composer-typed.png), [run-started](screenshots/dark/run-started.png), [run-thinking](screenshots/dark/run-thinking.png), [run-tool-call](screenshots/dark/run-tool-call.png), [run-finished](screenshots/light/run-finished.png), [run-editing](screenshots/dark/run-editing.png), [run-file-done](screenshots/dark/run-file-done.png), [run-command-running](screenshots/light/run-command-running.png), [run-command-output](screenshots/dark/run-command-output.png), [conversation-expanded](screenshots/light/conversation-expanded.png), [terminal-output](screenshots/dark/terminal-output.png).

## Forms and settings

Settings apply on change; there is nothing to submit. A pane is a 24px semibold title and a muted description over a rule, then cards: an h3 section title, rows of a 14px medium label over a 12px muted description, and the control on the right (a switch, an outlined select, a segmented radio group, a stepper, a slider, or an input with a Browse button). Appearance nests collapsible cards with an icon tile. The dialogs that take input (Add Quick Command, Create worktree) put labels over fields, segmented choices in a row, and the default ink button bottom right with its shortcut. No validation error was reachable.

Screens: [settings-general](screenshots/light/settings-general.png), [settings-agents](screenshots/dark/settings-agents.png), [settings-appearance](screenshots/dark/settings-appearance.png), [settings-terminal](screenshots/light/settings-terminal.png), [quick-command-dialog](screenshots/dark/quick-command-dialog.png), [create-worktree-dialog](screenshots/light/create-worktree-dialog.png).

## Menus and selects

Every popup is shadcn's dropdown, restyled: a translucent fill with a backdrop blur (`component.menu.bg`), a 14% edge, an 11px radius and `shadow.menu`, 32px rows with a translucent highlight, shortcuts right-aligned in muted text, separators, and icons at the start of rows. The new-tab menu lists the agents with their logos; the permission menu is a radio list with descriptions (Ask for approval, Accept edits, Full access); the model picker opens with a search field. Selects open a listbox with a check on the chosen option.

Screens: [new-tab-menu](screenshots/dark/new-tab-menu.png), [permission-menu](screenshots/dark/permission-menu.png), [model-menu](screenshots/light/model-menu.png), [project-menu](screenshots/dark/project-menu.png), [workspace-context-menu](screenshots/light/workspace-context-menu.png), [help-menu](screenshots/dark/help-menu.png), [settings-select-open](screenshots/dark/settings-select-open.png).

## Dialogs and confirmation

Dialogs centre over a black overlay with a light blur. The confirmation is small (384px, `core.layout.confirm-dialog`): a semibold title, one sentence with the object in bold and a consequence on its own line, then an outline Cancel, focused when it opens, and the red Remove. The search palette (900px) is a dialog with a search field, a Filter button, sections of recent chats and terminals, and a row of key hints at the bottom.

Screens: [remove-confirmation](screenshots/dark/remove-confirmation.png), [search-palette](screenshots/light/search-palette.png), [search-palette-empty](screenshots/dark/search-palette-empty.png).

## Empty and loading states

Empty states are centred and quiet: an icon in a round tile, one title line and one muted line (the empty chat), or a single muted sentence (No files in this workspace, No automations across loaded hosts, No project sources selected). Loading is a small spinner beside "Working..." in the chat.

Screens: [chat-empty](screenshots/light/chat-empty.png), [tasks](screenshots/dark/tasks.png), [automations](screenshots/light/automations.png), [run-thinking](screenshots/light/run-thinking.png).

## Search and filtering

The sidebar's Search row opens the palette; Settings has its own search with a shortcut hint, which narrows the navigation to matching panes; the Explorer filters files by name or by contents; the activity view adds a Filter field above the agent cards; Tasks has a query field with filters.

Screens: [search-palette](screenshots/dark/search-palette.png), [settings-search](screenshots/light/settings-search.png), [activity](screenshots/dark/activity.png), [tasks](screenshots/light/tasks.png).

## Feedback and notices

Orca reports through status rather than toasts: a dot and an age on each agent in the sidebar and on its tab, usage chips in the status bar (with a popover of limits per provider), and the update card pinned bottom right with a full-width Update button.

Screens: [toast](screenshots/dark/toast.png), [usage-popover](screenshots/light/usage-popover.png), [run-finished](screenshots/dark/run-finished.png).

## Onboarding

The first-run flow had been completed on this machine, so onboarding shows as the checklist in Settings (Setup steps and Milestones, each step a numbered row that opens a panel with cards and one ink action), the Add a setup script callout at the bottom of the sidebar, and the Orca Mobile page, a full-bleed promo with a phone mock-up.

Screens: [settings-onboarding](screenshots/dark/settings-onboarding.png), [settings-onboarding-skills](screenshots/light/settings-onboarding-skills.png), [workspace-terminal](screenshots/dark/workspace-terminal.png), [orca-mobile](screenshots/light/orca-mobile.png).
