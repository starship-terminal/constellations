# Cursor desktop: patterns

How Cursor's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

The Agents window is two columns. A 261px sidebar (`core.layout.sidebar`) on `seed.sidebar` holds, from the top: the traffic lights with Hide Sidebar, Search and back and forward icon buttons in a 40px bar (`layout.sidebar-top-bar-height`); New Chat, Automations and Customize; then groups with small muted headings (Projects, Pinned, Repositories) whose rows show an icon or status dot, a title that fades at the end and a relative time; and a footer with the avatar, the account name, the accent Update pill and the Settings icon button. The main panel on `seed.chrome` has a 40px title bar with the IDE button and an actions menu, and the page below. Hiding the sidebar leaves only the top bar's icons. Settings replaces the sidebar's content with its own navigation (Back, a search field and 12 panes) and the page with a 680px column of grouped rows.

The IDE window is the VS Code workbench under Cursor's theme: a 35px title bar with the Agents Window pill, a 300px side bar with a horizontal activity bar, the editor, a 422px agent pane on the right and a 22px status bar.

Screens: [home-default](screenshots/dark/home-default.png), [sidebar-hidden](screenshots/dark/sidebar-hidden.png), [settings-general](screenshots/dark/settings-general.png), [ide-shell](screenshots/dark/ide-shell.png), [ide-editor](screenshots/light/ide-editor.png).

## Starting and following an agent

The empty New Chat page centres one composer (608px, `seed.elevated`, 20px radius, a 12% hairline) under two text selects (environment and branch) and above pills for suggested modes. The composer's toolbar has a plus button (agents, context, tools), the model select, dictation and an ink voice button, which becomes the send button once there is text.

A sent prompt opens the conversation in a tab. The prompt becomes a raised bubble at the top of a 764px column; the agent's work streams below it as one muted status line (Planning next moves, Thinking, Exploring 1 search, ran 1 command) that folds into "Worked for 13s" when done, followed by the reply as plain text, file and code references in `text.link`, and a row of feedback icons with the time. A file the agent changed adds a card (1 Files Changed, Review). Command output is a code block on `seed.pane`. A follow-up composer stays docked at the bottom with the environment under it, and the right edge shows the apps rail (Changes, Browser, Terminal, Files).

Screens: [home-composer-typed](screenshots/dark/home-composer-typed.png), [run-started](screenshots/dark/run-started.png), [run-thinking](screenshots/dark/run-thinking.png), [run-exploring](screenshots/dark/run-exploring.png), [run-finished](screenshots/dark/run-finished.png), [run-editing](screenshots/light/run-editing.png), [run-file-changed](screenshots/dark/run-file-changed.png), [run-command-running](screenshots/dark/run-command-running.png), [run-command-output](screenshots/light/run-command-output.png), [conversation](screenshots/dark/conversation.png).

## Forms and settings

Settings has no forms to submit: every row applies on change. A pane is a page title (17/21, medium) over sections, each a small muted heading and a group of rows on a 6% wash with a 12px radius; a row is a label, a description in `text.secondary` and the control at the end (a switch, an outlined select, a number stepper, a slider, a text field). The only multi-field dialog captured, Create Project, follows the same shape: label left, control right, one accent button at the bottom right. No validation error was reachable.

Screens: [settings-general](screenshots/light/settings-general.png), [settings-appearance](screenshots/dark/settings-appearance.png), [settings-source-control](screenshots/dark/settings-source-control.png), [settings-models](screenshots/dark/settings-models.png), [create-project-dialog](screenshots/dark/create-project-dialog.png).

## Menus and selects

Every popup is the same raised surface (`seed.elevated`, 12 to 14px radius) with 26 to 30px rows, an 8px row radius and a `bg.tertiary` highlight that follows the pointer or the arrow keys. Long lists start with a search row; sections have 12px muted titles; submenus open to the side; a checkable row ends in a small switch; shortcuts sit right in `text.tertiary`. Selects open the same component, anchored to their trigger.

Screens: [model-menu](screenshots/dark/model-menu.png), [model-submenu](screenshots/dark/model-submenu.png), [plus-menu](screenshots/dark/plus-menu.png), [environment-select](screenshots/light/environment-select.png), [chat-actions-menu](screenshots/dark/chat-actions-menu.png), [sidebar-context-menu](screenshots/dark/sidebar-context-menu.png), [settings-theme-select](screenshots/dark/settings-theme-select.png).

## Dialogs and destructive confirmation

Modal dialogs sit centred over a black 40% scrim (`role.scrim`). The delete confirmation is a 450px dialog: a title, one sentence naming the item and saying it cannot be undone, then Cancel as a quiet text button and Delete as the accent button with an Enter hint. Nothing in it is red. The search palette is the translucent dialog: 640px, 84% chrome with a 16px backdrop blur.

Screens: [delete-confirmation](screenshots/dark/delete-confirmation.png), [create-project-dialog](screenshots/light/create-project-dialog.png), [search-palette](screenshots/dark/search-palette.png).

## Empty, loading and error states

The New Chat page is the main empty state: the composer alone, with an onboarding callout at the bottom (Import your Claude Code conversations). A search with no results leaves the palette's filter tabs and an empty list. Loading is the agent's status line (Planning next moves, Thinking) rather than a spinner or skeleton. No error state was seen.

Screens: [home-default](screenshots/light/home-default.png), [search-palette-empty](screenshots/dark/search-palette-empty.png), [run-thinking](screenshots/light/run-thinking.png).

## Feedback after an action

Feedback stays in place: the status line turns into "Worked for Ns", the changed file appears as a card in the conversation, and each turn gets feedback buttons. A tooltip names an icon button and its shortcut after a hover delay. No toast was raised during the capture.

Screens: [run-file-changed](screenshots/light/run-file-changed.png), [tooltip](screenshots/dark/tooltip.png).

## Search and filtering

Search (⌘K) is a palette with a search field, pill filter tabs (All, Projects, Agents, Files, Actions, Settings), sections and rows with shortcuts. Settings has its own search field that filters the panes as you type. Customize filters plugins with a pill search field, a type select and pill toggles.

Screens: [search-palette](screenshots/light/search-palette.png), [settings-search](screenshots/dark/settings-search.png), [customize](screenshots/dark/customize.png).

## Data display

Automations shows its list as a raised table: a header row of muted labels, 48px rows separated by hairlines, a status with an icon (Active, Inactive), tool chips and a row menu, with Mine and Team tabs and a search field above, and template cards (an icon, a title, two lines, a Use button) below. Customize lists plugins as rows with an icon, a name, a badge (Plugin, User), a muted status line and an accent text action.

Screens: [automations](screenshots/dark/automations.png), [automations-scrolled](screenshots/light/automations-scrolled.png), [customize](screenshots/light/customize.png).

## Onboarding

The account was already set up, so no first-run flow was reachable. The product introduces features with inline callouts instead: the Claude Code import strip on the New Chat page, the Meet Grok Bot banner on Customize, and the moved-to-Customize notice in Settings, each dismissible.

Screens: [customize](screenshots/dark/customize.png), [settings-general](screenshots/dark/settings-general.png).
