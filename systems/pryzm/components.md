# Pryzm components

Public pages of https://pryzm.design, captured 2026-11-21, signed out, dark theme only. Crops are element screenshots from the live page. Values are computed styles in [raw/components-computed.json](raw/components-computed.json), named against [tokens.json](tokens.json) where they match.

## Checklist

| Component | Status | Where |
|---|---|---|
| Button | Captured | Marketing Open studio link, studio Export, sign-in Continue. [button-primary-default.png](components/crops/button-primary-default.png), [button-export-default.png](components/crops/button-export-default.png), [button-submit-default.png](components/crops/button-submit-default.png) |
| Icon button | Captured | Studio Undo, 28px. [button-icon-default.png](components/crops/button-icon-default.png) |
| Link | Captured | Marketing nav Inspiration. [link-nav-default.png](components/crops/link-nav-default.png) |
| Text field | Captured | Sign-in email field, empty, not typed. [text-field-default.png](components/crops/text-field-default.png) |
| Text area | Not present | No public textarea on the pages that loaded. |
| Select | Captured as combobox | Lab blend mode, role combobox. [combobox-default.png](components/crops/combobox-default.png). Native `<select>` not present. |
| Checkbox | Not present | No public checkbox. |
| Radio | Not present | Pricing uses tabs, not radios. |
| Switch | Captured | Studio Grain enable switch. [switch-default.png](components/crops/switch-default.png) |
| Tabs | Captured | Pricing Monthly / Yearly. [tab-default.png](components/crops/tab-default.png) |
| Menu | Captured | Phone Menu dialog. [menu-default.png](components/crops/menu-default.png). Aspect menu and Add node are dialogs. |
| Tooltip | Not captured | Info marks exist in the studio. No tooltip was held open. |
| Dialog | Captured | Studio Export sheet. [dialog-default.png](components/crops/dialog-default.png). Share, aspect, add-node, remix paywall are in screenshots/. |
| Toast | Not present | Sonner colour hooks are in CSS. No toast was shown. |
| Card | Captured | Gallery look card. [card-default.png](components/crops/card-default.png) |
| List row | Not present | Layer rows are disclosure buttons, not a list component. |
| Table | Not present | |
| Avatar | Not present | Signed out. No account avatar. |
| Badge | Captured | PRO pill on a look page. [badge-default.png](components/crops/badge-default.png) |

## States

Hover and focus-visible were requested on the controls above. Computed background, colour and radius did not change on most of them. That is recorded as no measured change, not as a missing state file. Pressed, disabled, loading and error were not captured: no form was submitted, and no disabled control was on the public pages that were opened.

## Shared values

| Role | Token | Measured |
|---|---|---|
| Page | `dark.page` | `#000` |
| Surface | `dark.surface` | `#141414` |
| Text | `dark.text-primary` | `#fafafa` |
| Accent button | `dark.accent` | `#e5e5e5` on dark, near-black text |
| Radius, controls | `core.radius.md` | 8px |
| Radius, cards and dialogs | `core.radius.card` | 18px |
| Field height | `core.sizing.field` | 44px |
| Studio button height | `core.sizing.studio-button` | 32px |

## Gaps

- Focus ring: programmatic focus did not change outline or box-shadow on the measured controls. Not captured.
- Pressed, disabled, loading, error, tooltip, toast: not captured or not present, as the table says.
- The light token set is declared and not painted.
- Sign-in fields were not filled. Google was not clicked. Continue was not submitted.
