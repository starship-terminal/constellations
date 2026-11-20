# Components

Values come from `getComputedStyle` in the T3 preview tab on 2026-11-19. Viewport was 1169 by 731, devicePixelRatio 2. The preview browser did not produce screenshot frames, so there are no crops. Token names point at [tokens.json](tokens.json).

## Button

Marketing primary. `GET STARTED` on [https://n8n.io/](https://n8n.io/) and `START FREE TRIAL` on [https://n8n.io/pricing/](https://n8n.io/pricing/).

| Property | Value | Token |
|---|---|---|
| Background | rgb(255, 188, 202) | `core.color.marketing.button-primary` |
| Text | rgb(33, 33, 33) | `core.color.marketing.text-on-primary` |
| Font | n8n Baumer Mono, 14px, weight 400, line-height 18px, letter-spacing 0.28px, uppercase | `core.typography.marketing-action` |
| Padding | 12px 16px | `core.spacing.marketing-sm`, `core.spacing.marketing-md` |
| Height | 42px | `core.spacing.marketing-button` |
| Radius | 9999px | `core.radius.marketing-full` |
| Border | 0 | |
| Shadow | none | |

Declared hover fill is `#ff91ac` (`core.color.marketing.button-primary-hover`). Hover was not held on a marketing button.

Marketing secondary. `TALK TO SALES`. Background rgb(217, 217, 217), text rgb(22, 22, 22), same size and radius. Token `core.color.marketing.button-secondary`.

Console primary. `Sign in` on [https://app.n8n.cloud/login](https://app.n8n.cloud/login) and `Continue` on [https://app.n8n.cloud/register](https://app.n8n.cloud/register).

| Property | Value | Token |
|---|---|---|
| Background | oklch(0.7807 0.136 5.02) | `core.color.console.brand` |
| Text | oklch(0 0 0) | |
| Font | Geist, 14px, weight 500, line-height 14px | `core.typography.console-button` |
| Padding | 0 16px | |
| Height | 36px | `core.spacing.console-button` |
| Radius | 9999px | `core.radius.console-button` |
| Shadow | brand 1px inset ring, plus oklch(0 0 0 / 0.25) 0 1px 2px -1px | |

`:hover` matched on Continue and the background did not change.

## Icon button

A 32 by 32 hamburger sits in the marketing header at 1169px. Its label was empty. No icon-button states were measured.

## Link

Announcement link `Learn more` on the homepage: n8n Baumer Uniwidth, 14px, weight 500, line-height 18px, color rgb(255, 145, 172), underline. Token `core.color.marketing.brand`.

Console link `Start a free trial`: Geist, 14px, weight 450, color oklch(0.8205 0.1071 4.98). Token `core.color.console.link`.

## Text field

Login instance field. Wrapper `.auth-field__control`: background oklch(0.2686 0 89.88), radius 4px, height 40px, inset ring oklch(1 0 89.88 / 0.15) 1px. Input padding 0 12px. Label `Instance name` is 12px, weight 500.

Register email field uses the same fill, radius and height. Its rest ring is stronger: oklch(1 0 89.88 / 0.7) 1px inset plus oklch(1 0 89.88 / 0.3) 2px.

Focus on the login field did not paint a new ring.

Error, register only. After typing `not-an-email` and clicking Continue, the field got `aria-invalid=true` and the inset ring became oklch(0.6378 0.2373 25.44). The alert text was `Value needs to be an email address`, 12px, weight 450, color oklch(0.7022 0.1892 22.23). The form was not submitted.

Empty submit on register showed the browser message `Please fill out this field.` No custom alert appeared.

## Text area

Not present on the pages that loaded.

## Select

Not present. Login asks for an instance name as a text field with a `.app.n8n.cloud` suffix, not a select.

## Checkbox

Not present on n8n's own pages. CookieScript, a third-party banner, had category switches. Those were declined and are not n8n controls.

## Radio

Not present.

## Switch

Not present on n8n's own pages. CookieScript painted a 38 by 20 track, rgb(7, 122, 199), radius 100px. That is the vendor widget.

## Tabs

Pricing billing control is a pill track, not a `role=tab` widget. Track background rgb(240, 240, 240), radius 9999px, padding 4px, height 52px. `Monthly` label is rgb(22, 22, 22). `Annually` label is rgb(250, 250, 250). Each option is 44px tall, padding 0 16px, radius 9999px, 16px weight 400. The selected indicator's own box was not separated from the label.

Persona pills on the homepage: selected `TOM, IT` is rgb(255, 188, 202) with rgb(22, 22, 22) text, 34px tall, padding 8px 16px, radius 9999px. Unselected pills are rgb(71, 71, 71) with rgb(250, 250, 250) text.

## Menu

Desktop nav links (Product, Use cases, Community, Enterprise, Pricing, Sign in) computed height 0 at 1169px. A hamburger was visible. Clicking it did not reveal labelled menu items. Menu open, hover and selected states were not captured.

## Tooltip

Not present.

## Dialog

Not present on n8n's pages after the cookie banner was declined. CookieScript's dialog is a vendor overlay and was not kept as an n8n component.

## Toast

Not present.

## Card

Stat card `.card.bg-surface-card-secondary`: background rgb(240, 240, 240), radius 24px, padding 16px 32px 16px 16px. Feature card `.card.bg-surface-card-primary`: background rgb(217, 217, 217), radius 24px, padding 32px. Pricing plan `.pricing-plan`: background rgb(240, 240, 240), radius 24px, padding 32px 16px, width 320px. No shadow on these cards.

## List row

Pricing feature lists are `ul.plan-features`, 16px, color rgb(22, 22, 22). Row height, marker and hover were not measured one row at a time.

## Table

Not present on the pages that loaded.

## Avatar

Not present. Signed-out pages show no account avatar.

## Badge

Not present as a named badge. The pricing save note `Annually (Save 17%)` sits in the billing label.

## Shared values

Marketing type is n8n Baumer Uniwidth. Marketing actions are n8n Baumer Mono, uppercase, 0.28px tracking. Console type is Geist. Marketing buttons are 42px pills. Console buttons are 36px pills. Marketing cards are 24px radius. Console fields are 4px radius.

## Gaps

- No screenshots or crops. `preview_snapshot` returned `The browser is not producing screenshot frames.`
- Desktop nav menu did not open, so menu items and the desktop link row were not measured.
- Phone width (390) was not measured. The only viewport was 1169 by 731.
- Marketing button hover, pressed, disabled and loading were not held.
- Console button hover did not change the fill. Pressed, disabled and loading were not held.
- Login field focus did not paint a new ring. A login validation error was not triggered, because no instance name was submitted.
- Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar and badge were not on the signed-out pages.
- The running workflow editor was not entered.
