# Unsplash components

Public signed-out surface, measured 2026-11-21 in headed Chromium at 1440 x 900. Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json).

## Search field

The header search is a gray pill (`light.surface`, radius larger than the 8px button token; the pill radius was not isolated as its own custom property). The input itself paints transparent. Placeholder copy: "Search photos and illustrations". Focus opens a suggestion list. Nothing was typed or submitted.

| State | Crop | Notes |
|---|---|---|
| default | [search-field-default](components/crops/search-field-default.png) | 14px, `light.text` |
| hover | [search-field-hover](components/crops/search-field-hover.png) | no fill change on the input |
| focus-visible | [search-field-focus-visible](components/crops/search-field-focus-visible.png) | focus ring not captured as a distinct outline on the input |
| pressed | [search-field-pressed](components/crops/search-field-pressed.png) | CDP `:active`. No submit |

## Primary button

Login submit. Fill `light.button` (`#111111`), text `light.button-text`, radius `core.radius.button` (8px), height `core.space.control-medium` (44px). Hover fill `light.button-hover` (`#222222`).

| State | Crop |
|---|---|
| default | [login-submit-default](components/crops/login-submit-default.png) |
| hover | [login-submit-hover](components/crops/login-submit-hover.png) |
| focus-visible | [login-submit-focus-visible](components/crops/login-submit-focus-visible.png) |
| pressed | [login-submit-pressed](components/crops/login-submit-pressed.png) |

## Quiet button

"Submit an image" in the header. White fill, gray text (`#767676`, `light.muted`), 8px radius, 32px height (`core.space.control-small`), 1px shadow `rgba(0, 0, 0, 0.08) 0 1px 1px`. Clicking it opens the login wall. The click was not used for the state shots. Pressed is CDP.

| State | Crop |
|---|---|
| default | [submit-button-default](components/crops/submit-button-default.png) |
| hover | [submit-button-hover](components/crops/submit-button-hover.png) |
| focus-visible | [submit-button-focus-visible](components/crops/submit-button-focus-visible.png) |
| pressed | [submit-button-pressed](components/crops/submit-button-pressed.png) |

## Icon button

The header Menu control is 40 x 40, 8px radius. Hover fills `light.surface` (`#eeeeee`, `--color-gray-200`).

| State | Crop |
|---|---|
| default | [menu-button-default](components/crops/menu-button-default.png) |
| hover | [menu-button-hover](components/crops/menu-button-hover.png) |
| focus-visible | [menu-button-focus-visible](components/crops/menu-button-focus-visible.png) |
| pressed | [menu-button-pressed](components/crops/menu-button-pressed.png) |

## Link

Header "Log in" is 14px / 500, `light.muted` at rest, `light.text` on hover.

| State | Crop |
|---|---|
| default | [login-link-default](components/crops/login-link-default.png) |
| hover | [login-link-hover](components/crops/login-link-hover.png) |
| focus-visible | [login-link-focus-visible](components/crops/login-link-focus-visible.png) |
| pressed | [login-link-pressed](components/crops/login-link-pressed.png) |

Menu links use the same gray-to-black shift. See [menu-link-default](components/crops/menu-link-default.png).

## Text field

Login email and password, empty. Not typed. White fill, 8px radius, 40px tall, 472px wide on the 1440 capture.

| Field | Crop |
|---|---|
| email | [email-field-default](components/crops/email-field-default.png) |
| password | [password-field-default](components/crops/password-field-default.png) |

## Tabs

Topic chips under the search. Resting text `light.muted`. Selected topic uses a 2px black underline (Featured on the home shot). Hover darkens the label to `light.text`.

| State | Crop |
|---|---|
| default | [topic-chip-default](components/crops/topic-chip-default.png) |
| hover | [topic-chip-hover](components/crops/topic-chip-hover.png) |

## Menu

The Menu button opens a white dialog with Company, Product, and Community columns. Captured in [home-light-menu](screenshots/home-light-menu.png).

## Dialog

Visual search opens a dialog (drop a file, paste a link, try an example). No file was uploaded. See [home-light-visual-search](screenshots/home-light-visual-search.png).

## Card

Photo and collection tiles on the home grid. The crop of the first photo link hit a caption line, not the image. The layout is in [home-light-default](screenshots/home-light-default.png).

## Shared values

| Role | Token |
|---|---|
| Page | `light.page` #ffffff |
| Text | `light.text` #111111 |
| Muted | `light.muted` #767676 |
| Search surface | `light.surface` #f5f5f5 |
| Primary button | `light.button` / `light.button-hover` |
| Radius | `core.radius.button` 8px |
| Body | 15px / 24px, `ui-sans-serif, system-ui, sans-serif` |

## Gaps

- Text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge: not present on the public pages that were opened, or not isolated.
- Disabled, loading, and error states: not shown. No form was submitted, so validation never appeared.
- Dark theme: declared on `.dark` in CSS, never applied. Not exported as a theme.
- Search pill radius and photo corner radius: visible, not a dedicated custom property. Not captured as their own tokens.
- Icon artwork: not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)).
