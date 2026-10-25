# Raycast patterns

How Raycast's components combine into its two windows, with the captures that show each. Token paths are in [tokens.json](tokens.json); screenshots are in `screenshots/dark/` and `screenshots/light/` under the same names.

## App shell: the launcher

One floating window, 750 x 475 pt with 26 pt corners (`size.mainWindow`, `radius.window`), and no chrome: no title bar, no sidebar, no tabs. Three bands stack in it. The search field fills the 64 pt header. The result list fills the middle, its rows inset 8 pt from the window edge. The 44 pt footer holds the action bar: a round menu button on the left and a glass pill on the right naming what Return does and how to reach every other action. The window is translucent over the macOS window material (`--color-window-bg: var(--bg-40)` with a gradient), so it paints a neutral grey (`page`), and every fill on it is the foreground or selection colour at a low alpha.

Screens: [00-root](screenshots/dark/00-root.png), [00 light](screenshots/light/00-root.png).

## Search and results

Typing filters in place; there is no submit. Results come in labelled groups (Results, Suggestions, Commands, Files) with small secondary headers. The first match is selected (white or black at 10%), the pointer's row gets half that (5%), and the arrow keys move the selection. A special result can take over the top of the list, as the calculator card does for arithmetic. With no match the list offers the fallback commands instead of an empty state.

Screens: [01-root-calculator](screenshots/dark/01-root-calculator.png), [02-root-results](screenshots/dark/02-root-results.png), [03-root-selected](screenshots/dark/03-root-selected.png), [04-root-hover](screenshots/dark/04-root-hover.png), [05-root-commands](screenshots/dark/05-root-commands.png), [09-root-no-results](screenshots/dark/09-root-no-results.png).

## Actions

Every item has one primary action (Return) and more behind Command-K. The action panel floats over the bottom right of the window with the item's name as a header, one row per action with its key caps, separators between groups, and its own search field at the bottom that filters the actions. The footer's round button opens Raycast's own menu in the same panel shape.

Screens: [06-actions-menu](screenshots/dark/06-actions-menu.png), [07-actions-menu-typed](screenshots/dark/07-actions-menu-typed.png), [08-app-menu](screenshots/dark/08-app-menu.png).

## Commands with their own view

A command pushes its view into the same window: a back chevron joins the search field, the header gains the command's own controls (a category dropdown), and the footer names the command and its primary action. Emoji & Symbols shows a grid of square tiles under section headers with counts; the selected tile gets an inner ring.

Screens: [11-emoji-grid](screenshots/dark/11-emoji-grid.png), [12-emoji-grid-typed](screenshots/dark/12-emoji-grid-typed.png).

## Settings

A separate, ordinary window (800 x 864 pt) with traffic lights and back and forward buttons. The left sidebar holds a search field, the account, the app's own panes (General to About), then every extension with its icon and a Pro badge where it needs the paid plan. The right side stacks section titles over rounded cards (`surface`, 2.5% of the foreground over the window) whose 46 pt rows put a label and an optional description on the left and one control on the right: a switch, a dropdown, a pill button, a segmented control or a key-cap hotkey. An extension's pane opens with a large centred icon, title and description, then a table of its commands with Alias, Hotkey and an enable checkbox.

Screens: [20-settings-general](screenshots/dark/20-settings-general.png), [22-settings-launcher](screenshots/dark/22-settings-launcher.png) to [26-settings-about](screenshots/dark/26-settings-about.png), [28-settings-account](screenshots/dark/28-settings-account.png), [29-settings-extension-raycast](screenshots/dark/29-settings-extension-raycast.png).

## Searching settings and choosing a value

The sidebar's search field turns the sidebar into results grouped by pane, with the matched word highlighted. A dropdown opens a searchable list grouped by section (dark themes, light themes) with the current choice selected.

Screens: [30-settings-search-focused](screenshots/dark/30-settings-search-focused.png), [31-settings-search-typed](screenshots/dark/31-settings-search-typed.png), [32-settings-select-open](screenshots/dark/32-settings-select-open.png).

## Upselling

Paid features stay visible and labelled rather than hidden: a Pro badge in the sidebar and on root results, a pricing card on the Account page with plan tabs, and the AI pane listing what it would do behind a single Upgrade to Pro button.

Screens: [05-root-commands](screenshots/dark/05-root-commands.png), [27-settings-ai](screenshots/dark/27-settings-ai.png), [28-settings-account](screenshots/dark/28-settings-account.png).

## Not shown

Dialogs, toasts, the HUD, loading, form errors, onboarding, AI Chat and the Store were not captured; [components.md](components.md#gaps) says why for each.
