# Mapbox components

Public marketing site, signed out, measured 2026-11-21. Crops are the real controls where a shot was cut. Values are token names from [tokens.json](../tokens.json).

## Button

Primary pill. The painted face is `.button_inner` (hero) or `a.button.is-nav` (header Sign up). Background `{light.accent.default}` `#007afc`, text `{light.text.on-accent}`, radius `100px`, hero height `52px`. Hover background `{light.accent.hover}` `#3195ff`.

| State | Evidence |
|---|---|
| default | measured `.button_inner` background `#007afc` |
| hover | measured `.button_inner:hover` background `#3195ff` |
| focus-visible | header Sign up reports `outline: rgb(1, 96, 204) auto 1px`; not a custom focus ring |
| pressed | Not captured. CDP press was not held on the pill. |
| disabled | not present on the captured public pages |

Stroke button (`a.button.stroke`): transparent face, text `#1c1f24`, 1px border `#bbc2ce`, radius `100px`.

## Link

Header Log in is 15px / 500 / `#0e1012`, no underline at rest. Body links use the same ink. Accent links (`#007afc`) appear on pricing chips such as "Mapbox Support".

## Text field

Contact page HubSpot field. Height 44px, radius 8px, border `#e3e6e8`. Focus border `#007afc`. Nothing was typed. Nothing was submitted.

## Text area

Not present on the contact page this pass (no textarea in the DOM).

## Select

The contact "How can we help you?" control is an `input[role=combobox]`, not a native select. Opening it was not required to read the field. Native `select` count was 0.

## Checkbox, radio, switch

Not present in the marketing UI. OneTrust mounts hidden checkbox switches for cookie categories. Those were not opened and not clicked.

## Tabs

Not present as `role=tab`. The home hero uses slide buttons (Slide 1–5, Go to slide).

## Menu

Products, Solutions, Developers, Company, and Resources are header buttons that open mega menus. A menu link measures 6px radius, 8px 12px padding. See [home-light-menu-products.png](../screenshots/home-light-menu-products.png) when that shot is in the package.

Language control EN opens English and 日本語.

## Tooltip, toast, dialog

Not present on the captured public pages. The cookie banner is a OneTrust overlay. It was hidden, never accepted, and is not treated as a product dialog.

## Card

Pricing uses stacked plan blocks (Pay-as-you-go and later tiers). A tight card box was not isolated; the page screenshot is the evidence.

## List row, table, avatar, badge

List rows appear in the footer link columns and the showcase index. No data table. No avatar. "NEW" and "HIRING" tags sit in the menus; their fill was not isolated as a crop.

## Icon button

No standalone icon button in the header at desktop. Mobile uses a menu control. That state is in the phone screenshots.

## Gaps

- Signed-in console, Studio, and account settings: login wall at https://account.mapbox.com/auth/signin/
- Pressed, disabled, loading, and error states of buttons: not shown on the public pages
- Dark theme: not present
- Motion durations and easings: not declared as custom properties on `:root`. Not captured.
- Elevation shadows: `--_color-mode---box-shadow--box-shadow` is a colour (`#5f7e9b33`), not a shadow layer. Not captured as an elevation scale.
