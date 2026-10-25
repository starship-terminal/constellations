# Codex desktop: patterns

How Codex's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name (the folder trust dialog in dark only); values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md). The themes are the owner's: Absolutely in dark, Catppuccin in light.

## App shell and navigation

The window is three columns on the window colour. A 52px navigation rail (`core.size.control.rail-button` buttons) holds the destinations (Home, Space, Scheduled, Plugins, Explore, Code Review), the Update available button and the profile. Beside it the sidebar (`role.surface`, the owner's 290px including the rail) starts with the mode switch (Codex or ChatGPT), the activity bell and search, then New chat, the Projects list with each project's chats indented under it, and Recents. The main pane (`role.page`) is the new-chat page, a chat, a destination page or Settings. A right panel of browser-style tabs (a start page, Files, Terminal) opens beside a chat. See [home-default](screenshots/dark/home-default.png), [sidebar-collapsed](screenshots/dark/sidebar-collapsed.png) and [tabs-new](screenshots/light/tabs-new.png).

Sidebar rows are 30px with a pill highlight; the selected project or chat takes the soft ink fill (`bg.primary-soft-hover` in dark). Section titles are muted text, not bold.

## Starting and following an agent

The new-chat page centres a mark and the question "What should we work on in design-capture?" (`core.typography.display`) over the composer. The composer (`component.composer`, 22px radius, the elevated surface) has the prompt, then a footer of pill chips: add, the permission mode (Full access in the warning colour), hooks, the model and effort, dictate and the round voice button, which becomes send when text is typed ([home-composer-typed](screenshots/dark/home-composer-typed.png)) and stop while the agent runs. Above it, the utility bar holds the project and Work in chips.

A run, from [run-started](screenshots/dark/run-started.png) to [run-file-created](screenshots/dark/run-file-created.png): the prompt appears as a right-aligned bubble, the chat appears under its project in the sidebar with a spinner, a muted Thinking line shimmers, then "Working for 8s" heads the turn with the agent's narration and a tool row in progress (Listing files, Running printf ...), and the turn folds into "Worked for 9s" above the reply. The Outputs card floats top right. Finished chats get an accent dot in the sidebar until read. [conversation-expanded](screenshots/light/conversation-expanded.png) shows a folded turn opened.

## Forms and settings

Settings replace the sidebar with a navigation list (search, Personal, Teams, Integrations, Coding) and centre one 768px column of titled sections. Each section is a card (`component.settings-card`, 20px radius, the panel fill with a hairline) of rows: a label over a muted description, the control on the right (switch, select, button, path). See [settings-general](screenshots/dark/settings-general.png); every pane is captured as `settings-<pane>`. Settings apply on change; there is no save button and no validation error was reachable.

Appearance is where the theme engine shows: Mode as three thumbnails, then Theme (a code theme preset), Accent, Background, Foreground and Font, each a seed of the theme ([settings-appearance](screenshots/light/settings-appearance.png)).

## Menus and selects

Menus share one surface: the elevated fill at 90 to 96%, a hairline ring, a soft shadow, a 20px radius and 15px row highlights ([profile-menu](screenshots/dark/profile-menu.png), [chat-actions-menu](screenshots/light/chat-actions-menu.png)). Submenus open beside the row ([profile-submenu](screenshots/dark/profile-submenu.png)). Selects in settings open the same menu; the default file open destination lists the editors and terminals Codex can open a file in ([settings-open-in-menu](screenshots/dark/settings-open-in-menu.png)). The composer's add menu is a wider panel above the composer ([add-menu](screenshots/dark/add-menu.png)); the model picker is a small popover with an effort slider ([model-menu](screenshots/dark/model-menu.png)); the project chip opens a searchable list ([project-popover](screenshots/dark/project-popover.png)).

## Dialogs and confirmation

Dialogs float without a tinted scrim: a 1px backdrop blur and a deep shadow lift them ([create-project-dialog](screenshots/dark/create-project-dialog.png)). Destructive confirmations are short: a title naming the thing, one sentence on what is kept, Cancel as a ghost button and the action in red on a red tint ([remove-project-dialog](screenshots/light/remove-project-dialog.png), [delete-archived-dialog](screenshots/dark/delete-archived-dialog.png)). Both were cancelled. The folder trust prompt stacks a narrower dialog with full-width buttons over Create project ([trust-dialog](screenshots/dark/trust-dialog.png)).

## Empty, loading and error states

The empty new chat ([home-default](screenshots/dark/home-default.png)), an empty search ([search-palette-empty](screenshots/dark/search-palette-empty.png)), Scheduled with no tasks ([scheduled](screenshots/dark/scheduled.png)), Code Review before a pull request is chosen ([code-review](screenshots/dark/code-review.png)), Passwords with none saved. Loading is the shimmering Thinking line and the sidebar spinner during a run. The one error surface seen is the Configuration warning card for ignored settings ([settings-agent](screenshots/dark/settings-agent.png)), a red-tinted card with a warning icon.

## Search and filtering

The search palette (Command K) lists recent chats with their project and number shortcuts, then quick actions ([search-palette](screenshots/dark/search-palette.png)). Settings, keyboard shortcuts, archived chats and Plugins each have a search field; archived chats add All chats and All projects filters ([settings-archived](screenshots/dark/settings-archived.png)).

## Data display

Lists are rows in cards: archived chats grouped by project with Unarchive buttons, keyboard shortcuts with key caps ([settings-shortcuts](screenshots/dark/settings-shortcuts.png)), Plugins as a two-column list with segmented tabs ([plugins](screenshots/dark/plugins.png)), the profile pane's token activity chart ([settings-profile](screenshots/dark/settings-profile.png)), usage limits as progress text ([settings-usage](screenshots/dark/settings-usage.png)).

## Feedback

Feedback is quiet: the accent dot on a finished chat, the activity bell, the Update available button, the context usage ring in the composer. No toast was raised during the capture.
