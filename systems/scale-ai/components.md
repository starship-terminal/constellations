# Components

Measured on the public marketing site and the signed-out login, 2026-11-19.
Values are token names. The live browser did not paint screenshot frames, so
this file has no crops. See Gaps.

## Button, primary

Header Get Started and the demo Submit share a black face and white label.
Get Started is 105 by 40, radius `{core.radius.lg}`, type `{core.typography.nav}`
at 16px. Submit is 113 by 40, radius `{core.radius.md}`.

| Part | Token |
|---|---|
| Face | `{light.component.button-primary.background}` |
| Label | `{light.component.button-primary.text}` |
| Height | `{light.component.button-primary.height}` |

Hover and pressed were not forced. Disabled and loading were not on the page.

## Button, outline

Header Log In. Transparent face, 1px `{light.border.stroke}`, label
`{light.text.muted}`, 72 by 40, radius `{core.radius.lg}`. It links to
`https://dashboard.scale.com/login`.

## Button, secondary

Learn More. Face `{light.background.secondary}`, label `{light.text.primary}`,
radius `{core.radius.md}`, height 37px. Padding was not readable on the
visible instance (the measured box was 0 by 0 on a duplicate).

## Button, login submit

Dashboard Log In. Face `{light.background.ink}`, label `{light.text.on-ink}`,
weight 700, 352 by 46, radius `{core.radius.3xl}`, shadow
`{core.shadow.login-rest}`. The stylesheet raises the shadow to
`{core.shadow.login-hover}` on hover. Not clicked.

## Social login

"LOG IN WITH GOOGLE" and "LOG IN WITH GITHUB". Same size and shadow as the
login submit. The anchor's own background is transparent and its text is
`{light.text.link}`. The visible pill fill sits on a child the reading did
not isolate, so the pill face colour is a gap. Not entered. Both are
company SSO.

## Text field, marketing

Demo form. Face `{light.background.field}`, text `{light.text.field}`,
1px `{light.border.field}`, radius `{core.radius.lg}`, height 46px, padding
12px 16px, type 14px. Placeholders carry the label and a star: First name,
Last name, Company name, Job title, Work email. Selects match the same box.
Focus, after `focus()` on the email field: border `{light.border.focus}` and
`{core.shadow.field-focus}`. Error, disabled, and filled states were not shown.

## Text field, login

Email and password. Face `{light.background.field-login}`, text
`{light.text.field-login}`, no border, radius `{core.radius.lg}`, height 48px,
padding `0 24px 0 48px` (the left inset holds an icon that was not measured).
Placeholders: Email, Password. A stylesheet rule sets focus background to
`{light.background.field-login-focus}`. Not forced live. Nothing was typed.

## Link

Forgot-password link, `{light.text.link-strong}`, 14px, weight 500. Footer
product links, `{light.text.on-ink}`, `{core.typography.footer-link}`,
capitalize. Privacy Policy on the demo form, 14px, weight 500, color
`{light.text.field}`.

## Nav

Fixed header, 88px, inner bar `{light.background.nav}` from
`--nav-background: white`. Wordmark SVG 80 by 18. Nav items are buttons,
14px, black, 40px tall. Action cluster gap 12px.

## Card

Home story cards use radius 16px (`{core.radius.2xl}`). Several measured
about 373px tall. Their fills are photographic, so no flat surface token
was taken from them.

## Eyebrow

Mono, 11px, tracking 0.55px, uppercase. `{light.text.eyebrow}` on light
cards, white on dark cards.

## Cookie banner

Both hosts mount a cookie banner (Accept, Reject, Preferences). Those
controls belong to the consent vendor, not the product chrome, and were
not tokenised. Not dismissed in a way that submits a preference beyond
what the page already showed.

## Gaps

- No crops. The preview browser returned "The browser is not producing screenshot frames".
- No hover, pressed, disabled, loading, or error state was on screen.
- Checkbox, radio, switch, tabs, menu (the Products menu was not opened), tooltip, dialog, toast, table, avatar, and badge were not on these pages.
- Text area was not on the demo form. Select was present and shares the text-field box.
- Social-login pill face colour was not isolated from the transparent anchor.
- Login field leading icon was not measured.
- Dark theme was not on the page (`data-theme="light"`, `color-scheme: normal`).
