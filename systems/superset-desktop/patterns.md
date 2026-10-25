# Superset desktop: patterns

How Superset's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name (the folder-trust prompt, `run-approval`, only in dark); values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

One window in two columns. A 279px sidebar (`core.layout.sidebar`) on `ui.sidebar` holds, from the top: the sidebar toggle and back and forward buttons beside the traffic lights; New Workspace (a row on a 7% wash with a ⌘N hint on hover); Search, Workspaces, Automations, Tasks, Pull requests, Pages and Plugins; then two collapsible sections with 10px uppercase labels and icon buttons, SESSIONS and PROJECTS, where a project row (a lettered square and its name) holds its workspaces as indented rows; a setup card for the selected project; and a footer with the organisation menu, a monospace update pill and the Settings button. The main pane on `ui.background` shows the page. The toggle folds the sidebar to an icon rail.

Settings replaces the sidebar's content with Back, a title, a search field and 22 panes in four groups (Personal, Editor & workflow, Organization, System), and the page with a column of grouped rows.

Screens: [home-default](screenshots/dark/home-default.png), [sidebar-collapsed](screenshots/dark/sidebar-collapsed.png), [workspaces](screenshots/light/workspaces.png), [settings-general](screenshots/dark/settings-general.png).

## Starting a workspace and following an agent

The New Workspace page centres a pixel logo, a 30px heading (What should we build next?), three suggested prompts as ghost rows, and the composer: a 592px `ui.card` box with a 16px radius and a 1px ring, a 14px prompt, and a toolbar of a plus button, three chips (agent, model, effort), four ghost icon buttons and a round send button. Under it sit three small selects for where the workspace runs: the device, the project and the checkout (Worktree or Local).

Sending creates a workspace and opens it. A workspace is a tab strip (one tab per agent or terminal, a 6px `palette.amber-500` dot while the agent works), a bar of agent presets (Claude, Codex, OpenCode, Oh My Pi, Copilot, Mistral Vibe, Kimi Code, Grok, Superset CLI) that each open a new tab, and panes with a 28px header. Each agent is its CLI running in a terminal pane (xterm.js, JetBrains Mono, the theme's `terminal.*` palette): what streams is the CLI's own interface, so Superset's chrome only adds the running dot, the pane title the CLI sets, and the diff count on the workspace's sidebar row. The right panel lists the files the agent changed; clicking one opens its diff as a second pane.

Screens: [home-composer-typed](screenshots/dark/home-composer-typed.png), [run-approval](screenshots/dark/run-approval.png), [run-started](screenshots/dark/run-started.png), [run-thinking](screenshots/light/run-thinking.png), [run-tool-call](screenshots/dark/run-tool-call.png), [run-finished](screenshots/dark/run-finished.png), [run-editing](screenshots/light/run-editing.png), [run-file-changed](screenshots/dark/run-file-changed.png), [run-result](screenshots/light/run-result.png), [workspace-default](screenshots/dark/workspace-default.png), [workspace-diff](screenshots/light/workspace-diff.png), [workspace-files](screenshots/dark/workspace-files.png), [workspace-rich-input](screenshots/dark/workspace-rich-input.png).

## Forms and settings

Settings applies every change at once; there is nothing to submit. A pane is a 20px semibold title and a muted description over bordered groups of rows (10px radius); each row is a 14px label and a muted description with its control at the end: a switch, an outlined select, a text field, a button. Typography settings add a live preview. The one form that submits, Create a new project, stacks labelled fields (12px medium labels, 36px inputs, the location in monospace) with Cancel and an ink primary button that stays at half opacity until the name is filled.

Screens: [settings-general](screenshots/light/settings-general.png), [settings-appearance](screenshots/dark/settings-appearance.png), [settings-appearance-typography](screenshots/dark/settings-appearance-typography.png), [settings-agent-commands](screenshots/dark/settings-agent-commands.png), [settings-account](screenshots/light/settings-account.png), [create-project-dialog](screenshots/dark/create-project-dialog.png), [create-project-filled](screenshots/light/create-project-filled.png).

## Menus and selects

Every popup is shadcn's popover surface: `ui.popover`, a 1px `ui.border` edge, a 10px radius, shadow-md, 4px padding, 32px rows with a 6px radius that take `ui.accent` under the pointer, separators across the full width and shortcuts in muted, widely tracked text. Pickers with many items (project, branch, previous prompts) are command popovers with a search row. Right-clicking a project or workspace opens the same menu as a context menu, with Delete in `ui.destructive` at the bottom.

Screens: [agent-select](screenshots/dark/agent-select.png), [model-menu](screenshots/light/model-menu.png), [effort-menu](screenshots/dark/effort-menu.png), [plus-menu](screenshots/dark/plus-menu.png), [project-popover](screenshots/light/project-popover.png), [checkout-menu](screenshots/dark/checkout-menu.png), [org-menu](screenshots/dark/org-menu.png), [workspace-context-menu](screenshots/light/workspace-context-menu.png), [settings-theme-select](screenshots/dark/settings-theme-select.png).

## Dialogs and confirmation

Dialogs take the page colour, not the card colour, with a 1px edge, a 10px radius, 24px padding and shadow-lg over a black scrim at 50%. A destructive action is confirmed in an alert dialog whose title names the thing (Delete workspace "List files in this folder"?), a sentence on what happens and what stays, and Cancel beside a red Delete. Pro features open a wide upsell dialog with a feature list on the left and artwork on the right.

Screens: [delete-confirmation](screenshots/dark/delete-confirmation.png), [create-project-dialog](screenshots/light/create-project-dialog.png), [automations-pro](screenshots/dark/automations-pro.png), [tasks-pro](screenshots/light/tasks-pro.png).

## Empty, loading and error states

Empty pages centre an outline icon, a medium line and a muted sentence, with one outline button (Pages: No pages yet, Create with AI; Settings > API keys). The Workspaces board shows its four columns (Idle, Working, Needs attention, Needs review) with a coloured status icon and a count each. Errors are a toast (Create failed: Directory already exists) or a red message in place of the list (Pull requests, when the project has no GitHub remote). The agent's own waiting and thinking states are drawn by the CLI in the terminal.

Screens: [pages](screenshots/dark/pages.png), [settings-api-keys](screenshots/dark/settings-api-keys.png), [workspaces](screenshots/dark/workspaces.png), [create-project-error](screenshots/dark/create-project-error.png), [pull-requests](screenshots/light/pull-requests.png), [search-palette-empty](screenshots/dark/search-palette-empty.png).

## Search and filtering

Search opens a 720px command palette (a 48px input row, grouped 44px rows, shortcuts at the right). Settings filters its navigation as you type. The Workspaces board has a search field, a project select, Filter and Display buttons and a List or Board segmented control; Plugins and Pages have a search field and segmented filters.

Screens: [search-palette](screenshots/light/search-palette.png), [settings-search](screenshots/dark/settings-search.png), [workspaces](screenshots/dark/workspaces.png), [plugins](screenshots/dark/plugins.png).

## Data display

Settings > Usage shows quota bars per agent account, a leaderboard card and token charts; Organization lists members in a shadcn table (40px header, 48px rows); Plugins lists integrations as two-column rows with outline badges (MCP, SKILL) and Install buttons.

Screens: [settings-usage](screenshots/dark/settings-usage.png), [settings-organization](screenshots/light/settings-organization.png), [plugins](screenshots/light/plugins.png), [skills](screenshots/dark/skills.png).

## Feedback after an action

Superset reports in three places: a toast for app actions (an error, captured, and Project created., seen once), the running dot on the tab and the diff count on the workspace row while and after an agent works, and the right panel's list of changed files with a count on the Changes tab.

Screens: [create-project-error](screenshots/light/create-project-error.png), [run-file-changed](screenshots/dark/run-file-changed.png), [workspace-default](screenshots/light/workspace-default.png).
