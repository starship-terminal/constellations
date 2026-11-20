# Meiro components

Measured on meiro.cc and app.meiro.cc on 2026-11-19, signed out, at 1440×900 (desktop shots at 1×, crops and the second app pass at 2×) and 390×844. Colours are the computed value, then the token whose value matches. A state row lists only what differed from default.

## Discovery

| Checklist | Present | Evidence |
|---|---|---|
| Button | yes | Header Get started, hero CTA, plan Start for free, app Continue with email |
| Icon button | yes | Mobile menu button, 48px rounded, on [mobile-home-dark-default](screenshots/mobile-home-dark-default.png). Its fill is a gradient image, not a flat token |
| Link | yes | Header Login, footer links, legal links on the sign-in card |
| Text field | yes | Email field on the sign-in card and the reset form |
| Text area | not present | No textarea on a signed-out page |
| Select | not present | Billing period is a segmented control, not a select |
| Checkbox | not present | Trial notes use decorative check marks, not inputs |
| Radio | not present | |
| Switch | not present | |
| Tabs | yes | Annual / 3-month / Monthly on pricing |
| Menu | partial | Features, Use cases and Resources are header menus. The open panel was covered by a hero image in the capture, so the open state has no crop |
| Tooltip | not present | |
| Dialog | not present | No modal on the captured pages |
| Toast | not present | |
| Card | yes | Sign-in card, review cards, pricing plan cards |
| List row | yes | Plan feature rows on pricing |
| Table | not present | |
| Avatar | not present | Review quotes have no avatar images in the measured header |
| Badge | yes | No AI, With AI, Most powerful, and the -40% / -20% billing badges |

## Button

Primary marketing button. Fill `accent` (#d5fe52), label `on-accent` (#0e0f0f), TT Hoves Medium 16/20, padding 16px 24px, radius `radius.nav` (18px), height 52px. The hero instance is 56px tall with an 18px label.

| State | What changed |
|---|---|
| default | [button-primary-default](components/crops/button-primary-default.png) |
| hover | Computed fill, radius and label did not change. [button-primary-hover](components/crops/button-primary-hover.png) |
| pressed | Computed fill did not change. The anchor's own `color` flipped to the browser active red; the visible label stayed ink. [button-primary-pressed](components/crops/button-primary-pressed.png) |
| focus-visible | Outline 1px auto `focus` (#005fcc), offset 1px. [button-primary-focus](components/crops/button-primary-focus.png) |
| disabled | Not captured. No disabled marketing button was shown |

Plan button, Start for free, is the same fill and radius at 332×52. [button-plan-default](components/crops/button-plan-default.png), [button-plan-hover](components/crops/button-plan-hover.png).

App email button. Fill `accent-deep` (#c0ef2a), label ink, SF Pro 15/20 weight 600, padding 15px 22px, radius 17px, height 50px, width 440px inside the card. Transition 300ms cubic-bezier(0.4, 0, 0.2, 1) on color and background. Forced hover did not change the fill. [button-email-default](components/crops/button-email-default.png), [button-email-hover](components/crops/button-email-hover.png), [button-email-focus](components/crops/button-email-focus.png).

App Google button. Fill `surface-raised` (#202222), label white, same size and radius. Hover fill `surface-hover` (#2c2e2e). [button-google-default](components/crops/button-google-default.png), [button-google-hover](components/crops/button-google-hover.png).

Reset password uses the marketing lime (#d5fe52) at the app radius (17px), 440×50, SF Pro 15/20.

## Link

Header Login is a transparent 88×52 control, radius 18px, padding 16px 24px. The visible label is white, TT Hoves Medium 16/20. Hover did not change the computed label color. [link-login-default](components/crops/link-login-default.png), [link-login-hover](components/crops/link-login-hover.png).

Legal links on the app are SF Pro 13/16, color #808484.

In-page links on privacy and terms are TT Hoves Regular 18/27, color `accent`.

## Text field

Email input on the sign-in card. Fill `surface-raised` (#202222), text white, placeholder #808484, SF Pro 15/20 weight 500, padding 16px 12px 16px 16px, radius 15px, height 50px, width 440px. Resting border is 1px solid transparent. Focus border is 1px solid `border` at about 0.84 alpha. [text-field-default](components/crops/text-field-default.png), [text-field-focus](components/crops/text-field-focus.png).

The reset form paints the same field with a resting 1px solid `border` (#3b3e3e).

Filled and error states were not captured. A one-character probe was typed and cleared, and that crop was not kept.

## Tabs

Billing control on pricing. The track is a dark pill. The selected segment (Annual, then Monthly after a click) is a lime pill, radius 90px, about 130×40, label ink, TT Hoves Medium 16/19.2. The discount badge inside it is ink on a near-black pill, radius 100px, label #f3f4f9 at 13px. Unselected labels are #f3f4f9. [pricing-dark-default](screenshots/pricing-dark-default.png), [pricing-dark-monthly](screenshots/pricing-dark-monthly.png).

The crop [tabs-billing-default](components/crops/tabs-billing-default.png) is only the Annual word, not the whole track.

## Card

Sign-in card. Fill `surface` (#171818), radius 30px, 520×370, padding 30px 40px 40px, no shadow, no border. [card-login-default](components/crops/card-login-default.png).

Review cards on the marketing home. Fill `surface`, radius 20px, 620×258, no shadow.

Plan cards. Width 332px. The Most powerful badge is a gradient pill, not a flat token.

## Badge

| Badge | Fill | Label |
|---|---|---|
| No AI, With AI | #202222, radius 12px | #f3f4f9, TT Hoves Medium 14/16.8 |
| Most powerful | gradient, not a flat token | #171818, TT Hoves Medium 14/16.8 |
| -40% | #0e0f0f, radius 100px, 48×26 | #f3f4f9, TT Hoves DemiBold 13/15.6 |
| -20% | pale pill | #171818, TT Hoves DemiBold 13/15.6 |

## List row

Plan features are TT Hoves Regular 15/21, white, with a lime check. The row has no measured separator.

## Icon button

The phone header replaces the nav with one 48px control, radius 48px, at the right of a 72px header. Its face is a pale gradient image. [mobile-home-dark-default](screenshots/mobile-home-dark-default.png).

## Gaps

- No light theme. Both sites paint dark, and neither offered a theme switch on a signed-out page.
- Marketing button hover and pressed did not change the computed fill. The change, if any, is in a Framer variant the forced pseudo-class did not reach.
- The open header menu was not measured. A click opened it under a hero image that intercepted the pointer.
- Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table and avatar were not on the signed-out pages.
- Disabled, loading and error states were not shown. The email form was not submitted, so validation never ran.
- The Gleap launcher (purple, 48px) is a third-party widget, recorded as `widget`, not as a Meiro control.
- Affiliate pages at affiliate.meiro.cc use a different TT Hoves stack and an orange link (#ff8562). Those values are not in the token set.
