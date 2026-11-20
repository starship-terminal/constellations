# Components

Public Washington Post controls, measured on the signed-out site on 2026-11-21. Crops are 2x element screenshots. Values are token names from [tokens.json](tokens.json).

## Button

Save and subscribe. Blue pill (`core.radius.round`), Franklin, white label, 32px tall on the homepage header.

| State | Crop | Fill | Text |
|---|---|---|---|
| default | [button-subscribe-default](components/crops/button-subscribe-default.png) | `light.accent` | `light.onAccent` |
| hover | [button-subscribe-hover](components/crops/button-subscribe-hover.png) | `light.accentHover` when the paint changes | `light.onAccent` |
| focus-visible | [button-subscribe-focus-visible](components/crops/button-subscribe-focus-visible.png) | `light.accent` | focus colour `light.focus` |
| pressed | not captured | A press was not held. | |
| disabled | not present | No disabled subscribe control on the public header. | |

Sign in is a text button, not a filled one: [button-signin-default](components/crops/button-signin-default.png), hover and focus crops beside it. Text is `light.text`.

## Icon button

Search and browse sections, and News alerts. 36px square, no label text, ink `light.text`.

| State | Crop |
|---|---|
| default | [icon-button-search-default](components/crops/icon-button-search-default.png), [icon-button-alerts-default](components/crops/icon-button-alerts-default.png) |
| hover | [icon-button-search-hover](components/crops/icon-button-search-hover.png) |
| focus-visible | [icon-button-search-focus-visible](components/crops/icon-button-search-focus-visible.png) |
| pressed | not captured |

## Link

Section links in the header and drawer use Franklin at 16px, colour `light.text`. Hover crop: [link-section-hover](components/crops/link-section-hover.png). Footer links: [footer-link-default](components/crops/footer-link-default.png). Brand link blue is `light.link`.

## Text field

The drawer search field, label "Ask a question or search". Underline, no box. Typed "public" and not submitted.

| State | Crop |
|---|---|
| default | [text-field-default](components/crops/text-field-default.png) |
| filled | [text-field-filled](components/crops/text-field-filled.png) |
| error | not captured | No public form was submitted. |

The sign-in email field is on the login wall. It was not filled. See [signin-light-default](screenshots/signin-light-default.png).

## Text area, select, checkbox, radio, switch

Not present on the public pages that were opened. The sign-in wall may hold more inputs. That branch stopped at the wall.

## Tabs

Phone homepage has Top Stories, Latest, and For You. Desktop section fronts use a link row, not a tab widget. Phone Latest: [mobile-home-light-latest](screenshots/mobile-home-light-default.png) was recaptured as a tab state only when the shot exists. If that file is absent, the tab state is not captured.

## Menu

Sections drawer: [menu-sections-default](components/crops/menu-sections-default.png) and [home-light-sections](screenshots/home-light-sections.png). Child section lists open as a second dialog. Sports children are in the site tree.

## Tooltip, toast

Not present on the captured pages.

## Dialog

News alerts opens a dialog of published headlines plus a create-account link. The screenshot was not kept: one headline named a street sale. The Black Friday softwall is a second dialog. It was hidden for measurements. Cookie Settings was mapped in the footer and not submitted.

## Card

Story cards on section fronts. Politics card measured in [raw/components-computed.json](raw/components-computed.json) (`card`). No separate crop: the card is the story link, and article destinations were not screenshotted.

## List row

Section drawer rows and the news-alerts list. The drawer crop shows the rows.

## Table

Not present on the captured public pages.

## Avatar

Not present on the signed-out surface. Author photos live on article and people pages, which were left out of screenshots.

## Badge

Not measured as its own control. Subscriber labels, if they appear in a story grid, are in the section screenshots.

## Logo and type

[logo-default](components/crops/logo-default.png). Headline crop: [headline-default](components/crops/headline-default.png), Postoni, colour near `core.color.gray.40`.

## Gaps

- Pressed, disabled, loading, and error states of controls: not captured. No public control showed them, and no form was submitted.
- Dark theme: not present on the public site.
- Signed-in account chrome: not captured. Sign-in wall recorded and stopped.
- Article body, byline, and correction furniture: mapped, not screenshotted.
- Checkbox, radio, switch, text area, select, tooltip, toast, table, avatar: not present on the pages opened, or behind the wall.
