# Conductor desktop: patterns

How Conductor's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name unless it says otherwise; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

The window is one web view at 1400 x 800 pt with the macOS window buttons drawn over its top-left corner, so the sidebar's first row leaves 66px for them (`core.layout.traffic-lights-clearance`). Three columns: a 256px sidebar (`core.layout.sidebar`, on `sidebar.background`), the workspace in the middle, and a resizable right panel. The sidebar holds, from the top: Toggle sidebar and back and forward arrows; the account button (the owner's photo, emoji and machine name); Home, Create and Search, each with its shortcut on hover; then My workspaces, with each repository as a semibold row with a letter tile, a workspace count and a + button, and each workspace as a row with a branch icon and a green diff count. The plan badge (FREE), Help and Settings sit at the bottom.

The workspace has a header (repository and branch breadcrumb, a ... popover for the target branch, an Open in split button and the right-panel toggle), a row of chat tabs with + for a new chat, and the chat. The right panel splits in two: All files, Changes and Checks over a file tree or the change list, and Setup, Run and Terminal below, each with an empty state until a script exists. Home replaces the workspace with a list of every workspace (search, filters, Display, Create) and folds the workspaces out of the sidebar.

Screens: [workspace](screenshots/dark/workspace.png), [conversation](screenshots/light/conversation.png), [home](screenshots/dark/home.png), [home-empty](screenshots/dark/home-empty.png) (dark only, before any project), [account-menu](screenshots/dark/account-menu.png), [help-menu](screenshots/light/help-menu.png), [settings-general](screenshots/dark/settings-general.png).

## Starting and following an agent

A new workspace opens on an empty chat with a card (You're in a new copy of conductor called dalat), three lines about the branch and the copied files, four dashed suggestion chips, and the composer at the bottom: a 12px-radius box on `base.muted` with the placeholder, a ⌘L to focus pill, and a toolbar of the model and effort (GPT-5.6 Sol High), + for attachments, plan mode and linked issues, and the send button, ink at 50% until there is text. A second chat in the same workspace opens on New chat in /folder-files-list with the earlier chats offered as transcripts.

A sent prompt becomes a right-aligned block on `base.highlight` (`component.user-message.bg`, a warm rose tint), and the tab and the right panel's header read Working.... While the agent runs, a small spinner and a running timer sit under the prompt, the send button becomes a stop square, and tool calls appear one per line (an icon, List files or Write 1 lines, and a mono argument chip). When the turn ends its tool calls fold into one line (2 tool calls, 1 message), the reply follows as plain 14px text with 20px semibold headings (Done, Follow-ups), tan file links and outlined inline code, and a footer gives the duration, time, copy, more and a diff chip (hello.txt +1 -0). Conductor renamed the workspace and its branch from the first prompt (Dalat became Folder files list, on c-wenlong/folder-files-list), the sidebar row gains +1, Changes gains a count and a Review button appears.

Screens: [run-list-streaming](screenshots/light/run-list-streaming.png), [run-list-working](screenshots/light/run-list-working.png), [run-list-finished](screenshots/light/run-list-finished.png), [run-write-thinking](screenshots/dark/run-write-thinking.png), [run-write-tool-calls](screenshots/dark/run-write-tool-calls.png), [run-write-finished](screenshots/dark/run-write-finished.png), [conversation-top](screenshots/dark/conversation-top.png), [conversation-expanded](screenshots/light/conversation-expanded.png), [composer-typed](screenshots/dark/composer-typed.png).

## Reviewing changes

The diff chip, the Changes tab and the palette's Show changes all open a diff tab (Latest turn) in the centre: a toolbar with the file chip, copy, Unified and Split toggles, more, and a Viewed checkbox, over the diff in Geist Mono 13px with added lines on a green wash and a green gutter. The right panel switches to Changes with a Latest turn filter chip. Files open from the palette's File picker in a file tab with a source and preview toggle; markdown previews render with a 30px h1.

Screens: [diff-view](screenshots/dark/diff-view.png), [diff-view-split](screenshots/light/diff-view-split.png), [diff-states](screenshots/dark/diff-states.png), [file-view](screenshots/light/file-view.png), [changes-empty](screenshots/dark/changes-empty.png), [checks](screenshots/light/checks.png).

## Forms and settings

Settings replaces the sidebar with Back, a search field (⌘F) and grouped panes (Personal, Agents & environment, Repositories with one entry per repository and its own Git, Environment, Scripts, Actions and Misc, More), and the content with a 24px medium title over rows: a 14px medium title, a 14px muted description, and the control on the right (a switch, an outlined select, a button, a text field), separated by hairline rules. Settings apply on change; there is no Save. The one form that submits is the offer to create a GitHub repository for a folder with no remote: labels over a select and a text field, helper text, Cancel and the ink primary. A name that already exists turns the helper line red (This repository already exists.) and disables the primary button; there is no field outline in red.

Screens: [settings-general](screenshots/light/settings-general.png), [settings-appearance](screenshots/dark/settings-appearance.png), [settings-account](screenshots/dark/settings-account.png), [settings-agents](screenshots/light/settings-agents.png), [settings-models](screenshots/dark/settings-models.png), [settings-git](screenshots/dark/settings-git.png), [settings-repo-misc](screenshots/dark/settings-repo-misc.png), [repo-dialog](screenshots/dark/repo-dialog.png), [repo-dialog-error](screenshots/light/repo-dialog-error.png).

## Menus, selects and the palette

Every popup is a Base UI menu on `base.popover` with a ring for an edge, an 8px radius and Tailwind's medium shadow: 32px rows, a faint highlight, shortcuts right-aligned in muted text, submenus with a chevron. The model picker adds a search field, drag handles and a Fast switch; the workspace menu carries single-key shortcuts and a status submenu of coloured dots; Open in lists Finder and nine editors and terminals with numbered shortcuts. Selects open a listbox with a check on the chosen option. The command palette (⌘K, Search) is a 672px dialog with scope pills, grouped results (Recent workspaces, Workspace actions, Actions, Settings) and keycap shortcuts.

Screens: [model-menu](screenshots/dark/model-menu.png), [model-effort-submenu](screenshots/light/model-effort-submenu.png), [composer-add-menu](screenshots/dark/composer-add-menu.png), [add-project-menu](screenshots/light/add-project-menu.png), [workspace-context-menu](screenshots/dark/workspace-context-menu.png), [workspace-status-submenu](screenshots/light/workspace-status-submenu.png), [open-in-menu](screenshots/dark/open-in-menu.png), [target-branch-popover](screenshots/dark/target-branch-popover.png), [settings-select-open](screenshots/dark/settings-select-open.png), [search-palette](screenshots/dark/search-palette.png), [keyboard-shortcuts](screenshots/light/keyboard-shortcuts.png), [tooltip](screenshots/dark/tooltip.png).

## Dialogs and destructive actions

Dialogs centre a 512px box with a 12px radius over black at 50% with a slight blur. Removing a repository asks first (Remove conductor? All your workspaces will be permanently deleted.) with Cancel and a red Remove; the trigger in the settings page is red text. Archiving a workspace has no confirmation.

Screens: [remove-confirm](screenshots/dark/remove-confirm.png), [remove-confirm-states](screenshots/light/remove-confirm-states.png).

## Empty, loading and error states

Empty states are muted, centred text in a dashed or plain bordered box with one secondary button (Run tests or a development server..., Add run script; Add setup script with Ask agent and Add manually; No variables set). The palette and settings search show No results found. Loading is a spinner and a running timer in the chat and Working... in the panel header; the run panel's lottie loaders were not captured. Errors are quiet: Couldn't load PR info with a warning icon in the panel header, and Workspace not found (light only) with Try again.

Screens: [setup-tab](screenshots/dark/setup-tab.png), [settings-environment](screenshots/light/settings-environment.png), [search-palette-empty](screenshots/dark/search-palette-empty.png), [settings-search-empty](screenshots/light/settings-search-empty.png), [run-write-thinking](screenshots/light/run-write-thinking.png), [workspace-not-found](screenshots/light/workspace-not-found.png).

## Feedback after an action

The workspace row's diff count, the Changes count and the Review button appear as soon as an agent writes a file; the chat footer adds the diff chip. Conductor's own notice is a Sonner toast pinned bottom right (New update available, See changes, Restart).

Screens: [update-toast](screenshots/dark/update-toast.png), [conversation](screenshots/dark/conversation.png).

## Search and filtering

Search is the palette (⌘K), with scope pills and typed filtering; Home has its own search field and filter selects (Hiding archived, Last active, Display); Settings has a search field that lists matching settings under the field.

Screens: [search-palette-typed](screenshots/light/search-palette-typed.png), [home](screenshots/light/home.png), [settings-search-typed](screenshots/dark/settings-search-typed.png).

## Onboarding

Not captured: the account had finished onboarding. The empty Home before any project (the CONDUCTOR wordmark over Open project, Open GitHub project and Quick start cards) is in [home-empty](screenshots/dark/home-empty.png).
