# Components

Public signed-out surfaces of Rox, measured 2026-11-19. Crops are 2x slices of the viewport screenshots. Token names point at [tokens.json](tokens.json).

## Button

The marketing site paints square buttons. Computed `border-radius` on the nav Start now, the pricing Start for free, and the contact Get in touch is `0px`.

| State | Crop | Values |
|---|---|---|
| Nav primary, on the home photograph | [button-primary-nav.png](components/crops/button-primary-nav.png) | Background `core.color.paper` (#fafafa). Label Geist 14px weight 500, colour `core.color.ink`. Padding 8px 13px. Height 30px. Inset shadow `core.shadow.nav-primary`. |
| Hero primary | [button-primary-hero.png](components/crops/button-primary-hero.png) | White face, label `core.color.ink`, Geist 18px weight 400, letter-spacing -0.18px. The anchor itself computed as transparent; the white face is the visible control. Height 49px. |
| Hero secondary | [button-secondary-hero.png](components/crops/button-secondary-hero.png) | Background rgba(0, 0, 0, 0.18). Label rgb(250, 250, 250), Geist 18px weight 400. Padding 12px 14px 13px. Height 49px. |
| Plan primary | [button-primary-pricing.png](components/crops/button-primary-pricing.png) | Background `core.color.action-dark` rgb(64, 63, 62). Label rgb(250, 250, 250), Geist 16px weight 500. Padding 12px 24px 13px. Height 41px. |
| Contact submit | [button-primary-contact.png](components/crops/button-primary-contact.png) | Background `core.color.ink` rgb(12, 10, 9). Label rgb(250, 250, 250), Geist 16px weight 500. Height 52px. Width 560px. |

A second plan button on the pricing page computed to rgb(130, 130, 130). That is the dimmed column, recorded as `core.color.action-muted`. Hover, focus-visible, pressed and disabled were not captured.

## Link

Nav links on the home hero are Geist 14px weight 500, colour rgba(250, 250, 250, 0.8), line-height 14px. Footer links include Privacy Policy and Security. Their rest colour on a light page was not measured separately.

## Text field

[text-field-default.png](components/crops/text-field-default.png) is the contact form email field. The wrapper is `core.color.field` (#f4f4f3), radius 4px, padding 16px, height 49px. The input itself is transparent. Placeholder colour is stone-400, rgb(166, 160, 155). Type is Geist 14px. [text-field-half.png](components/crops/text-field-half.png) is the half-width first-name field, same chrome.

Focus and error were not shown. The form was not submitted.

## Text area

[textarea-default.png](components/crops/textarea-default.png). Same field chrome as the text field. The control is 100px tall with 16px padding. Placeholder "Write your message".

## Select

[select-default.png](components/crops/select-default.png). Native select, Geist 14px, colour rgb(28, 25, 23), padding 16px, height 49px. Options seen: Select an option, LinkedIn, X, Collegue or Friend, Google, Other. The closed state is the only one captured.

## Card

[card-plan.png](components/crops/card-plan.png) is the Individual plan card on /pricing. White surface, 1px stone border, price in Season Mix 42px weight 420, colour rgb(28, 25, 23). The charcoal button sits inside the card.

## Auth0 controls

The signed-out login at roxai.us.auth0.com was measured and not screenshotted. The preview browser was not producing frames, and a login page is not a public marketing page, so headless Playwright was not launched against it.

Email input: 52px tall, 318px wide, radius 10px, 1px solid rgb(166, 166, 166), background #ffffff, text #0d0d0d, padding 0 16px. Continue: black fill, white label, radius 10px, 52px tall. Google and Microsoft buttons: background #fafaf9, border 1px #e7e5e4, label rgb(133, 133, 133), radius 10px. Card: 400px wide, radius 14px, border 1px #e7e5e4, shadow 0 12px 40px rgba(0, 0, 0, 0.12), background #fafaf9, on page #efedea.

## Not on these pages

Checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, avatar, badge, table, icon button. See [raw/gaps.md](raw/gaps.md).

## Gaps

Hover, focus-visible, pressed, disabled, loading and error states were not displayed. Auth0 publishes `--base-focus-color: #a6a6a6`, `--base-hover-color: #dbdbdb` and `--error-color: #E38268` as custom properties. Those were not observed on a control in that state. The signed-in product was not entered.
