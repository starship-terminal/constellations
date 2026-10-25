# OpenCode desktop: patterns

How OpenCode's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

The window is a title bar on `bg.deep` and one rounded panel on `bg.base` inset 8px below it. The title bar holds the Home button, a row of session tabs (each a 214px tab with the project's letter avatar and the session title; the open one raised on `bg.layer-01`) and a new-tab button. There is no sidebar: Home (⌘B, a toggle) replaces the panel with two columns, the projects on the left (28px rows, the selected one on `bg.layer-03`, then Settings and Help) and the sessions on the right under a 720px search field, grouped by Today and Older. Selecting a project filters the sessions to it; selecting it again shows every project.

Screens: [home-default](screenshots/dark/home-default.png), [home-all-projects](screenshots/light/home-all-projects.png), [home-project-empty](screenshots/dark/home-project-empty.png), [tab-popover](screenshots/dark/tab-popover.png), [tab-context-menu](screenshots/light/tab-context-menu.png).

## A session and a run

A session is a single 696px column (`layout.transcript`) under a 28px header (project, title, More options, then the context button with its ring, Toggle review and Session details), with the composer docked at the bottom. The owner's prompt is a right-aligned bubble with `text.accent` text on a faint blue; the agent's reply sits on the page in 14/22.4 Inter (`typography.body`), with inline code and code blocks in IBM Plex Mono and file names as accent links. Tool calls collapse into one muted line, Used 1 Shell or Used 1 Write, that expands to the command and its output; shell output is shown as a bordered block.

A sent prompt turns Send into a Stop square, changes the placeholder to Add follow-up, and shows Working under the prompt; a command that takes a while adds Move to background beside it. The reply streams into place; when it finishes, the turn ends in a Copy button and the agent, model and time (1. Build · MiniMax-M3 · 8:21 AM), and the tab's avatar returns from a spinner to the project letter.

Screens: [run-working](screenshots/dark/run-working.png), [run-tool-running](screenshots/dark/run-tool-running.png), [run-streaming](screenshots/dark/run-streaming.png), [run-file-written](screenshots/light/run-file-written.png), [run-command-running](screenshots/light/run-command-running.png), [run-command-output](screenshots/dark/run-command-output.png), [run-finished](screenshots/dark/run-finished.png), [conversation](screenshots/dark/conversation.png), [conversation-top](screenshots/light/conversation-top.png), [tool-expanded](screenshots/dark/tool-expanded.png), [message-actions](screenshots/dark/message-actions.png).

## Composing

The composer is a 10px-radius card (`component.composer`) with the floating `shadow.raised`: the prompt, then a row of Add images and files, the model button (provider icon, model name), the variant button (Default) and Send, an ink square that stays grey until there is text. A new session shows the same composer centred under the opencode wordmark, with the project picker and a No Git pill below it. Typing / lists commands and @ lists context, in a menu that opens above the composer.

Screens: [new-session](screenshots/dark/new-session.png), [composer-focus](screenshots/dark/composer-focus.png), [composer-typed](screenshots/light/composer-typed.png), [slash-commands](screenshots/dark/slash-commands.png), [mention-empty](screenshots/dark/mention-empty.png), [model-menu](screenshots/dark/model-menu.png), [variant-menu](screenshots/light/variant-menu.png).

## Panes

Toggle review opens a pane on the right with Review and Context tabs. Review lists tracked changes (in a folder without Git it says No tracked changes and offers Create Git repository); Context lists the session's provider, model, context limit, token counts, cost and dates as a two-column grid, then the raw messages as rows. The terminal (⌃\`) opens beside the conversation as its own pane with terminal tabs. Session details is a popover of the project's repository state and its extensions (MCP, Plugins, Skills, LSP).

Screens: [review-pane](screenshots/dark/review-pane.png), [context-pane](screenshots/light/context-pane.png), [terminal](screenshots/dark/terminal.png), [session-details](screenshots/dark/session-details.png).

## Menus and selects

Every menu is the same floating surface (`bg.layer-01`, 6px radius, `shadow.floating`) with 28px rows that wash under the pointer. The model menu adds a search field, provider group labels and Free tags, and ends in Manage models; the project, session and tab menus are short lists, with disabled rows faint. Settings selects open the same menu as a listbox with a check on the chosen value.

Screens: [project-menu](screenshots/dark/project-menu.png), [session-menu](screenshots/light/session-menu.png), [settings-select-open](screenshots/dark/settings-select-open.png), [tooltip](screenshots/dark/tooltip.png).

## Dialogs and confirmation

Dialogs centre over a black scrim (`overlay.scrim`). Deleting a session asks in a 480px card: Delete session, the session's name in a sentence, and Cancel beside Delete session, whose only warning is its red text. The command palette (⌘K) is a 640px dialog with a search field, commands with their shortcuts, and recent sessions across every project.

Screens: [delete-confirmation](screenshots/dark/delete-confirmation.png), [command-palette](screenshots/dark/command-palette.png), [command-palette-filtered](screenshots/light/command-palette-filtered.png), [command-palette-empty](screenshots/dark/command-palette-empty.png).

## Settings

Settings replaces the panel: Back to app, a search field and a vertical list of twelve panes on the left (Preferences, Appearance, Notifications, Shortcuts, Pairing; Projects, Worktrees, Providers, Models, Extensions, Server; About), and the pane on the right as a title, a sentence and groups of rows on `bg.layer-01` with a hairline ring. Each row is a 13px label over a muted description, with its control on the right: a borderless select, a switch, a text field or a button. Settings apply on change; there is no Save. A project's own settings (name, icon, colour, worktree script) open from its menu in the same layout.

Screens: [settings-preferences](screenshots/dark/settings-preferences.png), [settings-appearance](screenshots/light/settings-appearance.png), [settings-notifications](screenshots/dark/settings-notifications.png), [settings-shortcuts](screenshots/dark/settings-shortcuts.png), [settings-pairing](screenshots/dark/settings-pairing.png), [settings-projects](screenshots/dark/settings-projects.png), [settings-worktrees](screenshots/dark/settings-worktrees.png), [settings-providers](screenshots/dark/settings-providers.png), [settings-models](screenshots/dark/settings-models.png), [settings-extensions](screenshots/dark/settings-extensions.png), [settings-server](screenshots/dark/settings-server.png), [settings-about](screenshots/dark/settings-about.png), [settings-search-filled](screenshots/light/settings-search-filled.png), [project-settings](screenshots/dark/project-settings.png).

## Search and filtering

Home's search filters sessions as you type and lists matches in a dropdown under the field (No sessions found for … when nothing matches). Settings' search narrows the panes, the Models pane filters its provider list, and the palette searches files, commands and sessions.

Screens: [home-search-filled](screenshots/dark/home-search-filled.png), [home-search-empty](screenshots/light/home-search-empty.png), [settings-search-filled](screenshots/dark/settings-search-filled.png), [command-palette-filtered](screenshots/dark/command-palette-filtered.png).

## Empty and loading states

A project with no sessions shows Nothing here yet, Create a session to get started and a New session button, centred where the list would be. The palette shows No results found, the @ menu No matching items. Loading is the Working line in a run and the spinner that replaces a tab's avatar; the app's startup splash was not captured.

Screens: [home-project-empty](screenshots/light/home-project-empty.png), [command-palette-empty](screenshots/light/command-palette-empty.png), [mention-empty](screenshots/light/mention-empty.png), [run-working](screenshots/light/run-working.png).
