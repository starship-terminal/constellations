# Zed patterns

How Zed's components combine into its screens, with the captures that show each. Token paths are in [tokens.json](tokens.json); screenshots are in `screenshots/dark/` and `screenshots/light/` under the same names.

## App shell

One window, three tiers of grey. The title bar and status bar (`role.chrome`, 34 and 30 pt) frame everything; panels, the tab bar and inactive tabs share the middle tier (`role.surface`); the editor is the darkest in One Dark and the lightest in One Light (`role.page`). A 1 pt `border` line separates each tier. The project panel docks left at 240 pt; the git panel, outline and agent panel dock right (the owner's settings); the terminal docks at the bottom. Status-bar icons toggle the docks, and the open dock's icon turns accent blue.

Screens: [01-editor-python](screenshots/dark/01-editor-python.png), [13-terminal-panel](screenshots/dark/13-terminal-panel.png), [14-git-panel](screenshots/dark/14-git-panel.png), [27-split-panes](screenshots/dark/27-split-panes.png), [43-agent-panel](screenshots/dark/43-agent-panel.png).

## Editing

The active tab takes the editor's fill and loses the line beneath it, so it reads as part of the buffer. A breadcrumb toolbar (44 pt) sits under the tabs. In the buffer, the git gutter marks added lines green and modified lines yellow, inline blame trails the cursor's line in `hint`, diagnostics underline in `error` and open a hover card, and the completion menu is a raised list with its documentation beside it. Multi-cursor selections and the other occurrences of a selected word use player 0's translucent selection colour.

Screens: [01](screenshots/dark/01-editor-python.png), [02](screenshots/dark/02-editor-markdown-tabs.png), [08](screenshots/dark/08-hover-diagnostic.png), [12](screenshots/dark/12-completions-menu.png), [28](screenshots/dark/28-multi-cursor-selection.png).

## Commands and pickers

The command palette, file finder, theme selector, outline and branch picker are one shape: a 610 pt raised box near the top of the window with a query field, a list whose selected row takes `element.selected` with a 4 pt margin, matched characters in the accent, key bindings right-aligned and muted, and a footer of actions. The theme selector previews a theme on the row under selection.

Screens: [03](screenshots/dark/03-file-finder.png) to [07](screenshots/dark/07-command-palette-selected.png), [24](screenshots/dark/24-theme-selector.png), [29](screenshots/dark/29-outline-symbols.png), [30](screenshots/dark/30-branch-picker.png).

## Menus and tooltips

Right-click menus (file, editor, tab) and the user menu are raised boxes with 6 pt corners, groups split by a 1 pt `border.variant` rule, disabled items in `text.disabled`, bindings on the right. Tooltips are raised too, with the binding beside the label; long file paths get one on hover.

Screens: [16](screenshots/dark/16-context-menu-file.png), [17](screenshots/dark/17-context-menu-editor.png), [18](screenshots/dark/18-context-menu-tab.png), [20](screenshots/dark/20-tooltip.png), [31](screenshots/dark/31-user-menu.png).

## Reviewing changes

The git panel lists tracked and untracked files with stage checkboxes, a branch line and a commit box. The project diff is a split multibuffer: deleted text on a red tint on the left, added text on a green tint on the right, word-level changes stronger. Project search and diagnostics use the same multibuffer of excerpts with file headers.

Screens: [09](screenshots/dark/09-diagnostics-panel.png), [11](screenshots/dark/11-project-search.png), [14](screenshots/dark/14-git-panel.png), [15](screenshots/dark/15-project-diff.png).

## Working with the agent

The agent panel opens on a new thread with a loading line, then a composer: the field in the buffer font, with mode (Manual, Accept edits, Plan, Auto, Bypass permissions), model, effort and profile selectors, a Fast mode switch and a send button. A sent prompt becomes a bordered box in the editor colour. While the agent works the send button turns into a red stop square and a spinner shows; tool calls appear as cards (a terminal card with its command and output, a file-write card with the new line on a green tint). Replies render as Markdown with headings, links and tables.

Screens: [43](screenshots/dark/43-agent-panel.png) to [57](screenshots/dark/57-agent-options-menu.png); the file-write card is in [55 light](screenshots/light/55-agent-edit-result.png).

## Forms and settings

Settings is its own window: a searchable sidebar of sections, and pages of rows with a label, a muted description and a control at the right (switch, select, stepper or an 'Edit in settings.json' button). A changed value shows a small reset icon beside its label. A warning banner on the warning fill sits at the top while the settings file needs migrating. Search filters the sidebar to matching sections and the page to matching rows.

Screens: [32](screenshots/dark/32-settings-general.png) to [40](screenshots/dark/40-settings-search-hover.png). No form validation error was seen.

## Destructive confirmation

Trash and Delete ask first, through the macOS system prompt (the owner's Use System Prompts is on), which dims the window; Cancel is the default. The prompt is AppKit's, so its colours are the system's, not the theme's.

Screen: [19-delete-confirm](screenshots/dark/19-delete-confirm.png).

## Empty, loading and onboarding

An empty workspace is a blank editor area with the shell around it ([00-launch](screenshots/dark/00-launch.png)). The agent panel shows 'Loading...' while its external agent starts ([43](screenshots/dark/43-agent-panel.png)). The onboarding page (zed: open onboarding) picks a theme, a base keymap and agents with segmented buttons and cards ([42](screenshots/dark/42-onboarding.png)). Extensions is a searchable list of cards with Install and Uninstall buttons ([41](screenshots/dark/41-extensions.png)).

## Feedback

No toast appeared. The pending update showed as a 'Restart to Update' button in the title bar, and git and diagnostics state shows in place (tree letters, gutter bars, the status-bar count).
