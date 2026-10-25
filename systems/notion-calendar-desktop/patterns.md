# Notion Calendar desktop: patterns

How Notion Calendar's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md). Dark is the owner's setting; light is Settings > General > Theme: Light mode, switched for the capture and switched back.

## App shell and navigation

The window is two columns. The sidebar (`role.surface`, `core.layout.sidebar` 240px, a hairline on its right) holds three icon buttons at the top (hide sidebar, command menu, create event), a mini month calendar with week numbers and today in red, the Scheduling row with its show-availability eye, the Meet with… field, then one list of calendars per account and per Notion workspace, each row a colour swatch and a name, and the help button at the bottom. The main area (`role.page`) is the calendar: a header with the month and year in 22px bold and the week number, the avatar, the view switcher (Week ⌄), Today, previous and next and the context panel toggle, then the grid. See [week-default](screenshots/dark/week-default.png) and [week-default light](screenshots/light/week-default.png); [sidebar-hidden](screenshots/dark/sidebar-hidden.png) gives the grid the whole window.

Views are Day, Week and Month, switched from the Week ⌄ menu or with single-letter shortcuts (D, W, M): [day-view](screenshots/dark/day-view.png), [month-view](screenshots/light/month-view.png). The week grid shows two time-zone columns (the owner's SF and SG), an all-day row, 48px hours (`core.size.hour`), weekends on a slightly different fill (`layout.fill-grid-wknd`) and a red now line with a time badge. The scheduling pane slides out beside the sidebar at 300px ([scheduling](screenshots/dark/scheduling.png)).

## Events: chips, popover and editor

An event is a chip in its calendar's colour, mixed toward the page, with a darker ribbon on its left edge, an 11px medium title and a 9px time; short events show the title only and overlapping ones stack side by side. Selecting one turns it solid with white text and opens the event popover: a 284px translucent floating panel (`role.overlay`, the wax blur) with the title, time and date, Propose new time, the time zone, the repeat rule, participants with their RSVP marks, the Yes / No / Maybe control, the meeting note action, the conferencing link, the calendar, busy and visibility, and reminders, in hairline-split sections. See [event-popover](screenshots/dark/event-popover.png) (two participants' addresses and the meeting code are painted out). Right-clicking a chip opens the event menu: a row of colour swatches, the RSVP rows with E-then-key shortcuts, email participants, join, block on calendar, cut, copy, duplicate and a red Delete ([event-context-menu](screenshots/light/event-context-menu.png)); right-clicking the empty grid offers Create event and Paste ([grid-context-menu](screenshots/dark/grid-context-menu.png)).

The new-event editor ([new-event](screenshots/dark/new-event.png)) is the same panel with an empty title ("Press 'space' for AI"), a 30-minute draft at the next half hour, and quiet rows for participants, conferencing, AI meeting notes, location, links and description, then the default calendar, busy, visibility and reminders. It was opened and closed untouched: closing a draft that has been typed into saves it.

## Menus, the command menu and shortcuts

Menus are dark in both themes (`surface.contr-elevated`, `shadow.elevation-middle`): [view-menu](screenshots/light/view-menu.png), its View settings submenu ([view-submenu](screenshots/dark/view-submenu.png)), Number of days ([days-submenu](screenshots/dark/days-submenu.png)), the profile menu ([profile-menu](screenshots/dark/profile-menu.png)) and Help ([help-menu](screenshots/dark/help-menu.png)). Every action has a single key or a two-key sequence, shown on the right of its row.

The command menu (Cmd+K) is a centred 680px translucent panel: a 17px input, rows grouped under Calendar, Navigation and View, the highlighted row on `state.hover`, and a footer of key hints ([command-menu](screenshots/dark/command-menu.png)). Typing filters the rows and adds a Search events row ([command-menu-typed](screenshots/dark/command-menu-typed.png)); no match leaves only that row ([command-menu-empty](screenshots/light/command-menu-empty.png)). The ? key opens every shortcut in the context panel with its own search ([shortcuts](screenshots/dark/shortcuts.png), [shortcuts-search](screenshots/light/shortcuts-search.png)).

## Forms and settings

Settings (Cmd+,) is a modal over a dim scrim: a navigation list (Account: General, Profile, Notifications, Menu bar, Conferencing; then each calendar account and each Notion workspace) and a scrolling pane of titled sections. Controls are small: 24 x 14px switches, 30px selects shaped like secondary buttons, native radios and checkboxes in the accent, 13px text and secondary descriptions. Settings apply on change; Profile alone shows Cancel and Update. See [settings-general](screenshots/dark/settings-general.png), [settings-general-scrolled](screenshots/light/settings-general-scrolled.png) (Time format, Time zones, Location, Theme), [settings-select-open](screenshots/dark/settings-select-open.png), [settings-profile](screenshots/dark/settings-profile.png), [settings-notifications](screenshots/dark/settings-notifications.png), [settings-menu-bar](screenshots/dark/settings-menu-bar.png), [settings-conferencing](screenshots/dark/settings-conferencing.png), [settings-calendar-account](screenshots/light/settings-calendar-account.png) and [settings-notion-workspace](screenshots/light/settings-notion-workspace.png). No validation error was reachable.

## Dialogs and confirmation

The settings modal is the one dialog captured: 12px radius, the elevated surface, `shadow.elevation-high`, a close button top right. No destructive confirmation was opened: every destructive action on these screens (Delete an event, Delete Notion Calendar account, Disconnect, Log out) acts on the owner's real data.

## Empty, loading and error states

The scheduling pane's empty state (no links yet) is a sentence and the two create buttons ([scheduling](screenshots/dark/scheduling.png)); the command menu's no-match state is [command-menu-empty](screenshots/dark/command-menu-empty.png). Today's column in [day-view](screenshots/dark/day-view.png) is an empty day. Loading and error states were not seen.

## Search and filtering

The command menu searches commands and events; the shortcuts panel filters its list as you type; Meet with… searches people (not captured: it lists contacts' addresses).

## Data display and feedback

The grid, the month view and the mini calendar are the app's data display. Feedback after an action is a toast (not raised during the capture) and the chip itself, which turns solid when selected ([event-popover](screenshots/dark/event-popover.png)). A tooltip names each icon button with its shortcut ([tooltip](screenshots/dark/tooltip.png)).
