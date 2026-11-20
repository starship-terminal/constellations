# Components

Measured on withjulienne.com, signed out, on 2026-11-18. Values are token names. The reading behind each one is in [raw/components-computed.json](raw/components-computed.json).

## Button

The home hero's "See more recipes" is a 64px solid at `light.color.brand` with `light.color.onBrand` text and `core.radius.control` (20px). The recipe "Cook" pill is 44px, `light.color.cook`, `core.radius.pill`.

![See more recipes](components/crops/see-more-default.png)

![Cook](components/crops/cook-button-default.png)

The signup "Create account" button is the same 56px / 20px shape, painted `light.color.disabledFill` with `light.color.disabledInk` until the form is valid. It was never pressed.

![Create account at rest](components/crops/auth-create-default.png)

## Icon button

The header theme toggle is a 44px glass pill (`light.color.glass`, `core.radius.pill`). The recipe Save control is an icon button on the card. Saving was never pressed.

![Theme toggle](components/crops/theme-toggle-default.png)

![Save](components/crops/save-button-default.png)

## Link

Nav links are 14px `light.color.nav`. The auth Terms link is `light.color.link` (`#3c1518`). Footer links sit on `light.color.footer`.

![Nav](components/crops/nav-link-default.png)

![Footer](components/crops/footer-default.png)

## Text field

The search field is transparent type inside the glass pill. The auth email and password fields are 56px, `light.color.field`, 1px `light.color.fieldBorder`, `core.radius.control`. Nothing was typed.

![Search](components/crops/search-field-default.png)

![Email](components/crops/auth-email-default.png)

## Text area

Not present on the signed-out surfaces.

## Select

Not present. Discover filters are buttons, not a select.

## Checkbox

The signup form includes an agreement checkbox beside the Terms link. It was not toggled. No separate crop isolates it from the form.

![Auth form](components/crops/auth-form-default.png)

## Radio

Not present.

## Switch

Not present. Theme is a button, not a switch.

## Tabs

Not present. Discover's meal filters are a chip row.

## Menu

The marketing pages (`/team`, `/roadmap`, `/shop`) use a Menu button. On the 390px team capture the menu opens over the page. The desktop marketing header does not use the app header.

![Team menu, phone](screenshots/mobile-team-light-menu.png)

## Tooltip

Not present.

## Dialog

Log in opens an auth form over the home page. It was read at rest and closed. Create account, Google, Apple and the Turnstile widget were never used.

![Login form at rest](components/crops/login-dialog-default.png)

## Toast

Not present.

## Card

Recipe cards are a photo, a 12px title and a `light.color.muted` time line. The collection page reuses the same card.

![Recipe card](components/crops/recipe-card-default.png)

## List row

Ingredients on the recipe page are a name and an amount, 12px medium. There is no separate list-row component beyond that row.

## Table

Not present.

## Avatar

Not present on the signed-out pages. Recipe bylines are text (`@withlotsoflovemary` on the captured recipe).

## Badge

Not present as a component. Time and sale prices are caption text.

## Shared values

| Role | Token |
|---|---|
| Page | `light.color.page` / `dark.color.page` |
| Text | `light.color.ink` / `dark.color.ink` |
| Muted | `light.color.muted` |
| Brand | `light.color.brand` |
| Glass | `light.color.glass` / `dark.color.glass` |
| Display | `core.font.family.display` at `core.font.size.display` |
| Control radius | `core.radius.control` (20px) and `core.radius.pill` |

## Gaps

- Save, Cook and Buy were not pressed. Save and Cook need an account. Buy leaves the site.
- The cookbook at `/cookbook` is the signed-out empty state "Come back soon." The signed-in cookbook was not entered.
- Search was not submitted. `/search?ingredients=apple` is a published browse link.
- Focus rings did not paint on the header Log in button under hover, mousedown or focus. The search field's glass shell also did not gain an outline.
- Checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge are not on the public surfaces.
- Hover and pressed on Log in did not change the computed fill. The visible change, where one exists, is opacity on the discover chips (`transition-opacity`).
