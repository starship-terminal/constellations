# Grok Bot desktop: patterns

How Grok Bot's components combine on its main screens. Every screen exists in `screenshots/dark/` and `screenshots/light/` under the same name; values are tokens from [tokens.json](tokens.json), components are in [components.md](components.md).

## App shell and navigation

The window is two columns, three when the inspector is open. A 400px sidebar (`core.layout.sidebar`) on `bg.sidebar` holds, from the top: Search and New Bot as 36px circles; a grid of pinned Bots, each a 90 x 92 tile with the Bot's character over its name (a group shows its members' characters clustered); then groups as 30px rows (name, count) that open in place to list their Bots, each Bot a row with its character, name and the last message as a preview; and a footer with the account pill, Connect apps and the Update circle. The conversation fills the rest on `bg.pane`, with the open Bot's name as a floating pill at the top and the composer docked at the bottom. Selection is a wash, never a colour.

Screens: [home-default](screenshots/dark/home-default.png), [home-list-row](screenshots/light/home-list-row.png), [section-expanded](screenshots/dark/section-expanded.png), [inspector-details](screenshots/dark/inspector-details.png).

## A Bot's conversation and a run

One conversation per Bot. The owner's messages are right-aligned bubbles in the Bot's colour (`fill.<hue>-bubble-user`, white text); the Bot's are left-aligned bubbles on a 4% wash (`transcript.bubble-agent-fill`), both with an 18px radius and 22px lines; consecutive messages stack with a small gap, and time separators sit centred in `text.tertiary`. A new Bot opens with its own message and a question card: a raised card with a bold question and lettered options (A, B, C) the owner can pick or answer in the composer, whose placeholder changes to say so.

A sent prompt shows the Bot's character and a shimmering activity line at the end of the transcript (Thinking it through, Listing the directory files, Creating notes.txt, Drafting design token summary, Typing…). The Bot posts short progress messages and then its answer; inline code and code blocks sit on a faint wash in the system monospace. Hovering a message shows its actions (react, reply, more) beside it.

Screens: [conversation-top](screenshots/dark/conversation-top.png), [run-thinking](screenshots/dark/run-thinking.png), [run-tool-call](screenshots/dark/run-tool-call.png), [run-file-edit](screenshots/dark/run-file-edit.png), [run-file-created](screenshots/dark/run-file-created.png), [run-drafting](screenshots/dark/run-drafting.png), [run-typing](screenshots/light/run-typing.png), [run-answer](screenshots/light/run-answer.png), [conversation](screenshots/dark/conversation.png), [conversation-history](screenshots/dark/conversation-history.png).

## Composing

The composer is a 44px pill on `bg.elevated` with a 0.5px edge and a small shadow: an attach button (Attach files, Teach a task), the prompt, dictation, and the voice-chat button filled with the Bot's colour, which turns into the send arrow when there is text.

Screens: [home-composer-focus](screenshots/dark/home-composer-focus.png), [home-composer-typed](screenshots/light/home-composer-typed.png), [composer-menu](screenshots/dark/composer-menu.png).

## A new Bot

New Bot opens a 440px dialog: a large preview of the character, a centred name field, a grid of fourteen shapes and a row of eleven colours, and Cancel beside an ink Create that stays disabled until a name is typed.

Screens: [new-bot-dialog](screenshots/dark/new-bot-dialog.png), [new-bot-dialog-filled](screenshots/light/new-bot-dialog-filled.png).

## Menus and selects

Every popup is the same raised surface (`bg.elevated`, 12px `menu.radius`) with 30px rows, a 6px row radius and a wash under the pointer; submenus open beside their row. The account menu starts with an update banner on an accent tint. A right-click on a Bot opens the same menu at the pointer, ending in a red Delete. Settings selects open a listbox with a check on the chosen option.

Screens: [account-menu](screenshots/dark/account-menu.png), [account-submenu](screenshots/light/account-submenu.png), [support-submenu](screenshots/dark/support-submenu.png), [context-menu](screenshots/dark/context-menu.png), [settings-theme-select](screenshots/dark/settings-theme-select.png), [settings-accent-select](screenshots/light/settings-accent-select.png), [tooltip](screenshots/dark/tooltip.png).

## Dialogs and confirmation

Dialogs are raised with a 14px radius over a black scrim (`bg.scrim`, 70% in dark, 50% in light). The destructive confirmation is 320px: a bold title naming the Bot, one line of consequence, and two full-width pills, Cancel and a red Delete.

Screens: [delete-confirmation](screenshots/dark/delete-confirmation.png), [new-bot-dialog](screenshots/light/new-bot-dialog.png), [connect-apps](screenshots/dark/connect-apps.png).

## Settings

Settings is a 900px dialog with its own navigation (General, Computer, Vault, Usage & Billing, Updates, and Invite teammates at the bottom). A pane is a title over sections, each a small muted heading and a raised card of rows; a row is a label, sometimes a description in `text.secondary`, and the control at the end (a select, a switch, a button), and a link icon to copy a link to the setting appears on hover. Everything applies on change; nothing validates.

Screens: [settings-general](screenshots/dark/settings-general.png), [settings-general-scrolled](screenshots/light/settings-general-scrolled.png), [settings-computer](screenshots/dark/settings-computer.png), [settings-vault](screenshots/dark/settings-vault.png), [settings-usage](screenshots/light/settings-usage.png), [settings-updates](screenshots/dark/settings-updates.png), [settings-search-link](screenshots/dark/settings-search-link.png).

## Search, connecting apps, lists

Search opens a 560px palette: a borderless field over 49px rows of Bots and groups (character, name, the Bot's instructions as a preview, an unread dot), with an empty state when nothing matches. Connect Apps is an 800px dialog: a search field, Bot templates, category pills (the selected one ink-filled), then sections of apps in two columns, each with its logo, name, a line of description and a tonal Add.

Screens: [search-palette](screenshots/dark/search-palette.png), [search-palette-filtered](screenshots/light/search-palette-filtered.png), [search-palette-empty](screenshots/dark/search-palette-empty.png), [connect-apps](screenshots/light/connect-apps.png), [connect-apps-scrolled](screenshots/dark/connect-apps-scrolled.png).

## Empty and loading states

Empty states are one centred line in `text.tertiary` (the Library's "Pages, files, and apps this Bot makes show up here", the empty Vault). A Bot's computer that is not running shows "Computer is asleep" over a placeholder. The only loading states seen are the activity line in a conversation and the shimmer on its label.

Screens: [inspector-library](screenshots/dark/inspector-library.png), [inspector-computer](screenshots/light/inspector-computer.png), [settings-vault](screenshots/light/settings-vault.png), [run-thinking](screenshots/light/run-thinking.png).
