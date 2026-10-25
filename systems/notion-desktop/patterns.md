# Notion desktop: patterns

How Notion's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md). All editing shown happened in the capture's own page, Design capture (scratch), and its sample database.

## App shell and navigation

The window is a 36px tab strip over the active tab's page. The strip is its own page in the app: the sidebar toggle, inbox and new-page buttons, back and forward, pinned tabs as icons, then titled tabs up to 200px, the active one in the page colour ([tabbar-default](screenshots/dark/tabbar-default.png)). Under it, the 270px sidebar (`role.surface`, the secondary background) starts with Search or ask, the Home, Chat and Meetings tabs, then Favorites, Private and Teamspaces sections of 30px page rows, Customize sidebar and the workspace switcher at the foot. The page sits on `role.page` with a 44px topbar: the breadcrumb, Edited time, Share, copy link, favourite and more. See [page-default](screenshots/dark/page-default.png) and [page-default light](screenshots/light/page-default.png).

Collapsing the sidebar leaves the page full width and moves its toggle into the tab strip ([sidebar-collapsed](screenshots/dark/sidebar-collapsed.png)). The sidebar's Chat tab swaps the page list for the account's AI chats ([sidebar-chat](screenshots/dark/sidebar-chat.png)). The workspace switcher lists accounts and workspaces, Settings and sign-out ([switcher-menu](screenshots/dark/switcher-menu.png)).

## Pages and blocks

A page is a 720px column (`core.layout.content`) with 96px margins: a 40px bold title, then blocks. Headings are 30, 24 and 20px at weight 600, body is 16px on a 24px line. Lists, to-dos and toggles share a 24px gutter for their marker; a quote has a 3px bar in the text colour; callouts and code blocks sit on soft fills with a 10px radius; inline code is mono at 85% on a translucent fill in red ([page-default](screenshots/light/page-default.png), [page-scrolled](screenshots/dark/page-scrolled.png), [toggle-open](screenshots/dark/toggle-open.png)).

Editing is in place. Hovering a block shows the + and drag handle in the left margin ([block-hover](screenshots/dark/block-hover.png)); clicking the handle opens the block menu ([block-menu](screenshots/light/block-menu.png)) with Turn into and Color submenus ([block-colour-menu](screenshots/dark/block-colour-menu.png)). An empty block shows its placeholder ([block-empty](screenshots/dark/block-empty.png)); typing / opens the slash menu, which filters as you type ([slash-menu](screenshots/dark/slash-menu.png), [slash-menu-filtered](screenshots/light/slash-menu-filtered.png)). Selecting a word raises the formatting toolbar ([text-selection-toolbar](screenshots/dark/text-selection-toolbar.png)); Escape selects the whole block in the blue selection tint ([block-selected](screenshots/light/block-selected.png)). While typing, the topbar and the tab strip fade out ([block-typed](screenshots/dark/block-typed.png)).

## Databases

A database page has view tabs (Default view, Board) and a toolbar of filter, sort, automation, search and settings icons beside the blue New button ([database-table](screenshots/dark/database-table.png)). The table has muted header cells with type icons, 1px rules, select values as coloured pills, checkboxes and dates, and a + New page row. Rows take a faint fill under the pointer ([database-row-hover](screenshots/light/database-row-hover.png)). The board groups cards by Status in columns tinted with each option's hue ([database-board](screenshots/dark/database-board.png)). Cells open their editors as popovers: the select menu ([database-select-menu](screenshots/dark/database-select-menu.png)), the date picker ([database-date-picker](screenshots/light/database-date-picker.png)) and a property's menu ([database-property-menu](screenshots/dark/database-property-menu.png)). A row opens as a side peek with its properties ([database-peek](screenshots/dark/database-peek.png)). The same table also sits inline at the foot of the scratch page.

## Forms and settings

Settings is a large window over the scrim: a searchable left column of panes (Account, Workspace, Features, Admin, Access and billing) and one column of titled sections, each row a label over a muted description with the control on the right: a switch, a ghost select or a button ([settings-preferences](screenshots/dark/settings-preferences.png)). Every pane but People is captured as `settings-<pane>`. Settings apply on change; there is no save button and no validation error was reachable. Search filters the panes ([settings-search](screenshots/light/settings-search.png)); selects open the standard menu ([settings-select-menu](screenshots/dark/settings-select-menu.png)).

## Menus and selects

One menu surface everywhere: `misc.popover-bg`, a 10px radius, a 1px ring and a soft drop shadow, 28px rows with an icon, a label and a right-aligned shortcut, small muted section headings and often a search field at the top. The page actions menu ([page-actions-menu](screenshots/dark/page-actions-menu.png)), a sidebar row's menu ([page-row-menu](screenshots/light/page-row-menu.png)) and Share ([share-menu](screenshots/dark/share-menu.png)) all use it. Destructive rows are red (Move to Trash, Delete property).

## Dialogs and confirmation

Confirmations are small centred cards over the dark scrim: one question, the red action and Cancel stacked full width ([delete-property-dialog](screenshots/dark/delete-property-dialog.png), [light](screenshots/light/delete-property-dialog.png)). It was cancelled. Settings uses the same scrim at full size.

## Empty, loading and error states

An empty block shows its placeholder; the empty search says No results with a link to search deleted pages ([search-palette-empty](screenshots/dark/search-palette-empty.png)). The Sidebar settings pane was caught loading ([settings-sidebar](screenshots/dark/settings-sidebar.png)). The AI panel shows the account's limit: You've run out of free AI responses, with Submit disabled ([ai-panel](screenshots/dark/ai-panel.png)).

## Search and filtering

Search or ask opens a wide palette: filters (Pages, Chats, Title only, Created by, In, + Filter), results grouped by date with breadcrumbs, and a preview of the highlighted page on the right ([search-palette](screenshots/dark/search-palette.png)). Menus filter as you type (the slash menu, the block menu's search).

## Notion AI

The AI button floats at the bottom right of every page; it opens a 360px panel docked to the right of the page with suggestions (Summarize this page, Translate, Analyze, Create a task tracker), the input with an attachment button, an approval mode and the model chip ([ai-panel](screenshots/light/ai-panel.png), [ai-panel-typed](screenshots/dark/ai-panel-typed.png), [ai-model-menu](screenshots/dark/ai-model-menu.png)). No response was captured: the account had no free responses left.

## Feedback

Copy link raises a toast at the bottom of the page with an action ([toast](screenshots/dark/toast.png)). Hover reveals controls rather than showing them at rest: a block's handle, a row's add and more buttons, the title's Add icon, Add cover and Add comment ([page-controls](screenshots/light/page-controls.png)). A tooltip names a button with its shortcut ([tooltip](screenshots/dark/tooltip.png)).
