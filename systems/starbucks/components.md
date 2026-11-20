# Components

Values are token names. Measurements are from computed styles on the public pages, 2026-11-19.

## Button

Header account actions and every feature call to action are pills (`core.radius.pill`, 50px).

| State | Fill | Text | Border | Evidence |
|---|---|---|---|---|
| Primary (Join now) | `light.action.primary-bg` | `light.action.primary-text` | 1px solid black | [button-primary.png](components/crops/button-primary.png) |
| Primary hover | `light.action.primary-hover` | white | same as fill | measured, no separate crop |
| Secondary (Sign in) | transparent | `light.text.primary` | 1px `light.border.strong` | [button-secondary.png](components/crops/button-secondary.png) |
| Secondary hover | `light.action.secondary-hover` | unchanged | unchanged | measured |
| Accent (rewards Join now) | `light.action.accent-bg` | white | 1px same | [button-accent.png](components/crops/button-accent.png) |
| Outline on cream | transparent | `light.text.accent` | 1px accent | [button-outline-accent.png](components/crops/button-outline-accent.png) |
| On a green band | `light.action.on-green-bg` or transparent | white | 1px or 2px white | [button-on-green.png](components/crops/button-on-green.png) |
| Focus-visible | unchanged | unchanged | outline 2px `light.focus.ring`, offset 2px, plus a 5px white shadow | [button-focus-visible.png](components/crops/button-focus-visible.png) |

Label is `core.typography.button` (14px, weight 600) in the header and 16px / 600 on feature buttons. Height is 33px in the header and 35px on feature buttons. Padding is 7px 16px.

Pressed, disabled, and loading were not on the page.

## Icon button

The siren is a link to `/`, 52 by 52, colour `light.text.brand`, no radius, no border. Crop: [icon-button-logo.png](components/crops/icon-button-logo.png). Keyboard focus gives it a 2px radius and the same green outline as other links.

## Link

Footer links are 16px, weight 400, `core.color.black.58`, no underline in the computed style of the column links. The copyright line is `core.typography.legal`. Nav items are not underlined. They use `core.typography.nav`.

## Text field

The cafe locator search is `input[type=search]`, placeholder "Find a café", 19px SoDoSans, colour `light.text.primary`, background white, border 0, radius 0, height 35px, padding `0 48px 0 2px`. Crop: [text-field-search.png](components/crops/text-field-search.png). No query was typed, so focus and error are gaps.

The careers search fields (a different site) are 16px, 1px solid `rgb(0, 98, 65)`, radius 8px, padding 12px 16px, height 50px, Arial computed on the input.

## Radio

Pickup and Delivery on the locator are a two-part control. The checked segment is fill `light.action.accent-bg`, text white, weight 600, 16px. The unchecked segment is transparent with accent text. The native input itself measured transparent. No checkbox or switch was on the captured pages.

## Tabs

Rewards exposes `role=tab` for 25, 60, 100, 200 and 300 Stars. Selected and unselected both computed to `rgba(0, 0, 0, 0.87)`, 16px, weight 400, no border. A green mark sits beside the selected label as a separate element (`rgb(0, 117, 74)`). The selected treatment is not fully described by the tab's own computed style.

## Card

Rewards partner cards are 411 by 282, fill `light.background.card`, radius `core.radius.card` (32px), no shadow. The join band is 1264 by 355, radius 40px, fill `core.color.neutral.rewards-cream`. Gift utility cards are 627 by 223, radius 32px, fill `core.color.neutral.gift-card`.

Menu product tiles are about 247px wide, radius 0, shadow none, transparent fill. They are links with a photograph and a name, not cards.

## Header

100px tall at 1440, 72px at 390, transparent background, no shadow, relative position. Wordmark at the left. MENU, REWARDS, GIFT CARDS, STARBUCKS SHOP, then Find a café, Sign in, Join now. At 390 a menu button is present and was not opened.

## Cookie banner

TrustArc banner, title "This site uses cookies, but not the kind you eat", Agree button fill `rgb(0, 130, 72)`, white text, 14px, pill, 7px 16px. Dismissed with Agree before later shots. Not a product toast.

## 404

Heading "We can't find the page you're looking for." at 28px / 700 / `light.text.primary`. The same header and footer as the marketing site. [screenshots/not-found-light-default.png](screenshots/not-found-light-default.png).

## Gaps

- Sign-in and join forms. `/account/signin` returned 200 and rendered the footer shell with no inputs. Account creation was not opened, because it asks for personal data.
- Pressed, disabled, and loading buttons.
- Text field focus, error, and filled states. No text was typed.
- Checkbox, switch, select, text area, tooltip, dialog, toast, table, avatar, badge. Not on these pages.
- Phone navigation menu. The button is there. It was not opened.
- Dark theme. The product does not paint one on these pages.
- Reduced motion under emulation.
- About page. Headless Chromium got a Cloudflare challenge. Stopped.
- Ordering, gift checkout, and payment. Not entered.
