# Resume.io components

Measured on the signed-out site on 2026-11-19. Values are token names. The T3 preview browser returned "The browser is not producing screenshot frames", so there are no element crops. Whole-page shots are in [screenshots/](screenshots/).

## Button

Primary action. "Create my resume" and "Build Resume".

| State | Fill | Text | Source |
|---|---|---|---|
| Default | `light.component.button-bg` (`#1a91f0`) | `light.component.button-text` | computed `a.button.auth-button` |
| Hover | `light.background.action-hover` (`#1170cd`) | white | stylesheet `.button:hover`, not hovered live |
| Pressed | `light.background.action-pressed` (`#10529b`) | white | stylesheet `.button:active`; cookie Accept was already this colour |
| Disabled | `light.background.disabled` | `light.text.disabled` | stylesheet `.button[disabled]`. No disabled control was on screen |
| Outline | transparent, inset `light.border.stroke` | `light.component.button-outline-text` | computed `a.button.button--outline` ("My Account") |
| Secondary | `light.background.secondary` | `light.text.link` | computed `button.upload__resume-button` |
| Ghost | transparent, 1px `light.border.strong` | link blue | stylesheet `.button.button--ghost`; the free-plan "Build Resume" |

Radius `core.radius.button` (4px). Padding 14px 24px. Type 18px / 600 / 22px. Height observed 52px on the nav button and 48px on the hero and sign-in Continue.

## Link

Nav "Sign in" and "View all" use `light.text.link`. Footer links on the dark band are `light.text.on-footer`. No underline on the measured links.

## Text field

Sign-in email step, `input[name=email]`, and stylesheet `.field__input`.

- Fill `light.component.field-bg`, text `light.text.primary`, radius `core.radius.field` (3px).
- Padding 13px 16px 11px on the marketing rule, 12px 16px on the sign-in field. Height 48px. Size 19px / 24px.
- Focus paints a 2px bottom border in `light.border.focus`. The field was focused. Nothing was typed. Continue was not pressed.
- Placeholder colour on the marketing rule is `rgb(130, 139, 162)` (`light.text.secondary`).

Text area: stylesheet `.field__textarea` sets `min-height: 150px` and `resize: none`. No text area was on the measured pages.

## Checkbox and switch

From the landing stylesheet, not toggled.

- Checkbox box is 24px, radius 4px, border `light.border.stroke`. Checked fill and border are action blue. The tick is a 5px by 10px rotated border.
- Toggle (`.checkbox--toggle`) is 30px by 18px, radius 9px, off fill `light.background.disabled`, knob 14px white.

The cookie settings form holds checkboxes. That dialog was in the DOM and was not opened.

## Tabs

Template filter pills on [templates](screenshots/templates-light-default.png). `.templates-filter__tab-static`: height 38px, padding 8px 16px, radius `core.radius.pill` (36px), fill `light.background.sunken`, text `light.text.primary`, 16px / 400. A blue selector bar sits under the row. Tabs were not clicked.

## Card

Pricing cards on [pricing](screenshots/pricing-light-default.png). `.pricing__card-inner`: white, radius `core.radius.card` (6px), padding 40px 32px, no computed shadow. Price is 38px / 600 / 40px. Caption is `light.text.secondary`.

Template cards (`.templates-card`) are 350px wide at innerWidth 1169, radius 0 on the anchor. The page thumbnail itself carries the document art. No separate card shadow was computed.

## Dialog

Stylesheet `.modal__content`: white, width 544px, radius 6px, shadow starting `rgba(0, 0, 0, 0.08) 0px 0px 1px` (the rule dump cut the second shadow). Overlay is `z-index: 106`, fixed, inset 0. The cookie settings modal was present and not opened. The country modal was not opened.

## Navigation

`.nav__bar` is white, 80px tall, padding 0 32px, at innerWidth 1169. Links are 19px / 400, text primary. "Sign in" is link blue. At 390px the same header collapses to a logo and a hamburger. The hamburger was not opened.

## Footer

`footer.footer` fill `light.background.footer` (`#0f141e`), text white. Column titles are `light.text.muted`, 14px / 600 / 20px. This is a painted band, not a dark theme.

## Sign-in chooser

On `/app/auth/sign-in`, not screenshotted (preview frames failed, and headless was not used on the login page).

| Control | Fill | Size |
|---|---|---|
| Facebook | `rgb(19, 113, 240)` | 200 by 48, radius 4px, white 18px / 600 |
| Google | `rgb(219, 68, 55)` | same |
| LinkedIn | `rgb(40, 103, 178)` | same |
| Email | white, 1px `light.border.stroke` | same, text primary |

Title "Sign in" is TT Talent 47px / 600 / 48px. Subtitle "Enter your email" is 19px, `light.text.secondary`. Back is an outline button. Continue is the primary button at 48px height, weight 500. Social links and Continue were not followed.

## Gaps

- No crops. The preview browser could not produce screenshot frames.
- Hover, focus-visible, and pressed were not captured as states, except the email field focus underline and the cookie Accept button already sitting on the pressed blue.
- Disabled, loading, error, toast, tooltip, menu, table, avatar, and badge were not on the measured pages.
- The cookie settings dialog, country switch, FAQ accordion, and mobile menu were not opened.
- No dark theme exists in the measured CSS. Dark colours are the footer band and the declared `--dark-shadow-*` tokens.
