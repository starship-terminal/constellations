# Devin desktop: patterns

How Devin's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

A Devin window is one VS Code workbench with two views, switched from the menu at the top left (Agents view, IDE view). The Agents view is two columns. A 300px sidebar (`core.layout.sidebar`) on `bg.page` holds, from the top: the view switch with back and forward; the account (avatar, name, organisation) with Search and the inbox; New session, Automations, Wiki and a More row that opens a popover of the other pages (Review, Oncall, Security, Customize); then Sessions, a list of two-line rows grouped by parent session, with header actions (New, Properties, More); then, once local agents are on, a Recent group of local sessions; and Help and Settings at the foot. The page on the right uses the same `bg.page`, so the sidebar is set apart only by a hairline and its content; page headers are 44px. Collapsing the sidebar leaves an Expand sidebar button with its shortcut.

The IDE view is the workbench under Devin's theme: a 40px title bar with the view switch and the command center, a 300px side bar with a horizontal activity bar, the editor, a 300px agent pane on the right that holds a full Devin session, and a 22px status bar. Its colours are Devin's tokens (`ide.*`): the editor is `bg.page`, the bars are `bg.wash`.

Screens: [home-default](screenshots/dark/home-default.png), [view-menu](screenshots/dark/view-menu.png), [more-menu](screenshots/dark/more-menu.png), [sidebar-collapsed](screenshots/dark/sidebar-collapsed.png), [ide-shell](screenshots/dark/ide-shell.png), [ide-editor](screenshots/light/ide-editor.png).

## Starting and following an agent

The empty New session page centres the Devin wordmark, a Cloud / Local segmented control and one composer (688px, `bg.elevated`, a 20px radius, a `border.primary` hairline). Its toolbar: Attach or mention (+), Commands and skills (/), Configuration, the mode (Agent), then on the right the capability (Normal), dictation, voice call and a split send button whose chevron offers Start session in background and Start & send in Slack. Local swaps the toolbar for the local agent's: its permission mode (Bypass Permissions), the model (SWE-2 Max), and a footer of chips for the machine, the folder and the agent.

A sent prompt becomes a right-aligned `tint.tertiary` bubble (16px radius). Devin's work streams below it as a status line with the persona mark (Analyzing..., Pondering...), then folds into muted rows: Worked for a bit with the lines changed, Thoughts, Read hello.txt. The reply is plain 13px text with inline code; a status line closes the turn (Devin is awaiting instructions, with a coloured dot). While Devin works, the composer's placeholder becomes Guide Devin while it works, the send button becomes a stop button, and a bar above it counts the files changed with View changes and Mark as seen. The right pane offers Files, Browser, Changes, Progress and Terminal; a change opens Changes, a diff of full-width tinted rows.

Every turn of the local runs also printed Hook failed: ... vibe-island-bridge (exit 127), a hook from the owner's own setup that is missing on this machine; it shows how Devin renders a hook error in the transcript.

Screens: [home-local-trusted](screenshots/dark/home-local-trusted.png), [home-composer-typed](screenshots/dark/home-composer-typed.png), [send-menu](screenshots/dark/send-menu.png), [run-started](screenshots/dark/run-started.png), [run-working](screenshots/dark/run-working.png), [run-finished](screenshots/dark/run-finished.png), [run-editing](screenshots/light/run-editing.png), [run-file-changed](screenshots/dark/run-file-changed.png), [conversation-local](screenshots/dark/conversation-local.png).

## A cloud session and its pull request

A cloud session from history splits the page: the transcript on the left (Devin's name line with the time, replies with links in `text.link` and inline code on a `tint.secondary` chip, folded work rows, a waiting-for-approval row, the PR merged event) and a pane on the right with tabs (PR #1124, Changes). The PR pane carries a Merged pill (`bg.purple`, `text.purple`), the repository and branch, an outlined Comment button, text tabs (Changes, Description, Discussion, Commits, Checks, Bugs) and the diff, grouped into numbered review steps with a Viewed checkbox per file.

Screens: [conversation](screenshots/dark/conversation.png), [review](screenshots/dark/review.png).

## Forms and settings

Settings replaces the sidebar with its own navigation (Back to app, Search settings, Personal: Preferences, Keyboard shortcuts, Notifications, Connections, App settings; then the organisation) and the page with a 700px column. Nothing is submitted: every row applies on change. A pane is a 17px title over sections; each section is a heading and a card of rows (`bg.elevated`, a `border.secondary` hairline, a 10px radius); a row is a label, a description in `text.secondary` and the control at the end (an outlined select, a switch, a checkbox, a stepper, a text field, a button). App settings holds the workbench's own options and the local agent registry (Devin Local, Claude Agent, Codex, Cursor and others, each Enabled or Enable). No validation error was reachable.

Screens: [settings-preferences](screenshots/dark/settings-preferences.png), [settings-preferences-scrolled](screenshots/light/settings-preferences-scrolled.png), [settings-notifications](screenshots/dark/settings-notifications.png), [settings-connections](screenshots/dark/settings-connections.png), [settings-app](screenshots/dark/settings-app.png), [settings-app-agents](screenshots/dark/settings-app-agents.png), [settings-shortcuts](screenshots/light/settings-shortcuts.png).

## Menus and selects

Every popup is the same surface: `bg.elevated-wax` (the elevated fill at 94%), a `border.secondary` outline, a 10px radius and the large shadow. Rows are 30px with a 6px radius and a `tint.secondary` highlight; section titles are 12px medium in `text.secondary`; a submenu opens to the side (Actions in the attach menu); a checked row ends in a check; a toggle row ends in a small switch (Compact view). Selects in settings open a listbox of the same look; the composer's mode, capability and configuration triggers are plain text and open menus.

Screens: [attach-menu](screenshots/dark/attach-menu.png), [attach-submenu](screenshots/dark/attach-submenu.png), [mode-menu](screenshots/dark/mode-menu.png), [capability-menu](screenshots/light/capability-menu.png), [config-menu](screenshots/dark/config-menu.png), [commands-menu](screenshots/dark/commands-menu.png), [sessions-properties-menu](screenshots/dark/sessions-properties-menu.png), [session-context-menu](screenshots/dark/session-context-menu.png), [account-menu](screenshots/dark/account-menu.png), [help-menu](screenshots/dark/help-menu.png), [settings-theme-select](screenshots/dark/settings-theme-select.png).

## Dialogs and confirmation

Devin's own screens have no modal confirmation in the reachable paths: actions such as Archive act at once. The confirmation pattern comes from the workbench: Do you trust the authors of the files in this workspace?, a 480px dialog with a shield icon, two paragraphs, and Manage, Cancel and the accent Trust Workspace & Continue, the default button with its focus ring. Choosing Local or opening a terminal in an untrusted folder raises it; it was cancelled every time but once, when the capture trusted its own scratch folder (and removed the trust afterwards).

Screens: [trust-dialog](screenshots/dark/trust-dialog.png), [ide-terminal-trust-dialog](screenshots/light/ide-terminal-trust-dialog.png).

## Empty, loading and error states

The New session page is the empty state: the wordmark, the composer and a rotating tip as its placeholder. The palette's empty search shows no results. A run's loading states are the streaming status line and the stop button. Errors: the Restricted Mode banner (an orange pill under the composer: Local agents are off because this workspace is in Restricted Mode, with Trust workspace), the workbench's restricted-mode banner across the IDE, the error toast (The terminal process failed to launch...), and hook failures printed in the transcript.

Screens: [home-default](screenshots/dark/home-default.png), [home-local](screenshots/dark/home-local.png), [search-palette-empty](screenshots/dark/search-palette-empty.png), [run-started](screenshots/light/run-started.png), [toast](screenshots/dark/toast.png), [ide-shell](screenshots/light/ide-shell.png).

## Search and filtering

Search (⌘K) opens a 680px command palette with no scrim: an input row, Start session with a prompt and Search sessions, Recent, then Actions with their shortcuts, and a footer of key hints. Settings has a search field that narrows the navigation to matching sections. Lists filter with the segmented control (Automations' categories, the inbox's All / Unread) and a search field (Search wikis).

Screens: [search-palette](screenshots/dark/search-palette.png), [search-palette-empty](screenshots/light/search-palette-empty.png), [settings-search](screenshots/dark/settings-search.png), [automations](screenshots/dark/automations.png), [notifications](screenshots/dark/notifications.png), [wiki](screenshots/dark/wiki.png).

## Data display

Lists are cards and rows, not tables: automation templates in a three-column grid of 12px cards (an icon, a title, two lines of description, integration chips), wikis in a two-column grid of repository cards with an ink Generate button where none exists yet, PRs to review as rows with diff counts, the local agent registry as rows with a status.

Screens: [automations-scrolled](screenshots/dark/automations-scrolled.png), [wiki](screenshots/light/wiki.png), [review](screenshots/dark/review.png), [customize](screenshots/dark/customize.png), [settings-app-agents](screenshots/dark/settings-app-agents.png).

## Feedback and notifications

The inbox is a panel beside the sidebar: All / Unread, rows with an icon, a title, a description, the age and an unread dot, and an inline Review button on access requests. A finished turn ends in a status line and the files-changed bar; sessions in the sidebar carry an unread dot until opened. Tooltips are always dark, with the shortcut as key caps.

Screens: [notifications](screenshots/dark/notifications.png), [tooltip](screenshots/light/tooltip.png), [run-file-changed](screenshots/dark/run-file-changed.png).
