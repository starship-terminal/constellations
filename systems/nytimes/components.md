# Components

Signed-in New York Times account and masthead chrome, light theme, 2026-11-21. Crops are 2x cuts from the page screenshots. Hover, focus-visible and pressed were not driven. The phone account-nav close control shows a preview-tool focus ring; that crop is omitted.

Values name tokens from [tokens.json](tokens.json). A value with no token is the computed reading from [raw/component-tokens.json](raw/component-tokens.json).

## Button, emphasis

![Connect](components/crops/button-emphasis-default.png)

| | default |
|---|---|
| Face | `light.component.button-emphasis-bg` (`core.color.emphasis`, #121212) |
| Label | `light.component.button-emphasis-text` (`core.color.emphasis-fg`, #f8f8f8) |
| Radius | `core.radius.search` (3px, same corner as the dialog) |
| Where | Apple and Work or School Connect on [account settings](screenshots/account-settings-light.png) |

Not captured: hover, focus-visible, pressed, disabled. Connect was not clicked.

## Button, outline

![Disconnect](components/crops/button-outline-default.png)

| | default |
|---|---|
| Face | `light.component.button-bg` |
| Label | `light.component.button-text` |
| Border | `light.component.button-border` (`core.color.rule`, #121212), 1px |
| Where | Google Disconnect on account settings |

Not captured: hover, focus-visible, pressed. Disconnect was not clicked.

## Button, search submit

![Go](components/crops/search-go-enabled.png)

| | enabled, after typing |
|---|---|
| Face | `light.component.search-go-bg` (`core.color.go`, #567b95) |
| Border | `core.color.go-border` (#326891) |
| Label | 10px, weight 700, white |
| Radius | `core.radius.search` (3px) |
| Where | Masthead on [search typed](screenshots/search-typed-light.png) |

The control stays disabled until the field has text. Search was not submitted.

## Text field

![Search](components/crops/search-field-filled.png)

| | filled |
|---|---|
| Face | `core.color.paper` |
| Text | #333333, 14px, weight 400 |
| Border | `core.color.stroke` (#959595) when empty; #121212 when the field is open |
| Radius | `core.radius.search` (3px) |
| Where | Masthead search |

Empty, hover, focus-visible and error were not cropped. The empty open field is in [search-empty-light](screenshots/search-empty-light.png).

## Link

![Update](components/crops/link-update-default.png)

![Learn More](components/crops/link-inline-default.png)

| | row action | inline |
|---|---|---|
| Label | `light.component.link-text`, 16px / 20.8px, weight 500, underlined | `core.color.link` (#346eb7), underlined |
| Where | Update, Create, Manage on [account phone](screenshots/account-phone.png) | Learn More on [saved](screenshots/saved-empty-light.png) |

Create and Manage use the same row treatment: [Create](components/crops/link-create-default.png), [Manage](components/crops/link-manage-default.png). None of these links were followed into an editor.

## Account nav

![Selected](components/crops/account-nav-selected.png)

![Rest](components/crops/account-nav-default.png)

| | selected | rest |
|---|---|---|
| Label | Franklin 18/27, weight 700, `core.color.ink` | weight 500, `core.color.muted` |
| Mark | 2px rule on the left | none |
| Where | Email and settings on [account settings](screenshots/account-settings-light.png) | Account, same page |

Phone selected state: [account-nav-phone-selected](components/crops/account-nav-phone-selected.png), from [account-nav-phone](screenshots/account-nav-phone.png).

## Page heading

![Email and settings](components/crops/heading-page-default.png)

Franklin, about 32px, weight 600, `core.color.ink`. The account greeting uses the same stack at 32/38.4.

## Section drawer

![Drawer](components/crops/section-drawer-default.png)

| | open |
|---|---|
| Width | 240px CSS (`raw` geometry) |
| Item | Franklin 18/23, weight 600, `core.color.ink` |
| Scrim | `core.color.scrim` (#12121299) |
| Where | [section-nav-light](screenshots/section-nav-light.png) |

The open search field sits under the drawer. That clip is in the screenshot.

## Masthead

![Wordmark](components/crops/masthead-wordmark-default.png)

![Subscribe](components/crops/subscribe-nav-default.png)

![Account](components/crops/account-menu-default.png)

![Menu](components/crops/section-menu-default.png)

![Search](components/crops/search-button-default.png)

The wordmark is the product blackletter, not a UI face. Subscribe is a filled blue pill (`core.color.editorial` family, #326891). Account is Franklin with a chevron. Menu and search are icon buttons. Subscribe was not clicked.

## Empty state

![Empty reading list](components/crops/empty-state-default.png)

Heading in Franklin, weight 700, `core.color.ink`. Body in `core.color.body`. The bookmark glyph is part of the sentence. Seen on [saved-empty-light](screenshots/saved-empty-light.png).

## Avatar

![Profile icon](components/crops/avatar-default.png)

Default grey person mark on a light circle. No photo was set. Update was not clicked.

## Help

![Help](components/crops/help-link-default.png)

Question mark plus Franklin label, `core.color.muted`. Help Center was not opened.

## Shared values

| Token | Value | Use |
|---|---|---|
| `core.color.ink` | #121212 | headings, selected nav, rules |
| `core.color.body` | #363636 | body copy on account |
| `core.color.muted` | #727272 | rest nav, help |
| `core.color.paper` | #ffffff | page |
| `core.color.surface` | #f8f8f8 | emphasis label, secondary fill |
| `core.color.hairline` | #dfdfdf | row rules |
| `core.color.link` | #346eb7 | inline links |
| `core.font.franklin` | nyt-franklin, helvetica, arial, sans-serif | chrome |
| `core.spacing.2` | 1rem | the step the account rows sit on |
| `core.radius.dialog` | 3px | dialogs and search |

## Gaps

- No hover, focus-visible, pressed, disabled, loading or error crops.
- No text area, select, checkbox, radio, switch, tabs, tooltip, toast, table or badge.
- Dialog radius and shadow are tokenised from computed custom properties. No dialog was opened, because the ones offered were subscribe, gift, password and delete.
- Icon SVGs in [icons/](icons) are traces of the chrome marks, not the shipped SVG files.
- Dark theme was not on this account.
