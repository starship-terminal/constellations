# Components

Measured with `getComputedStyle` on 2026-11-19. Marketing at https://slack.com/intl/en-sg/ and https://slack.com/intl/en-sg/pricing. Sign-in chrome at https://slack.com/signin#/signin. No workspace was created. No email was submitted. Google, Microsoft, Apple, and company SSO were not followed.

## Button

Marketing primary `.c-button.v--primary` is `rgb(115, 3, 148)` with white text, 14px Salesforce-Sans, weight 700, letter-spacing 0.798px, uppercase, radius 4px. Header instance at 1169px: padding 12px 16px, 42 by 130. Hero instance: padding 19px 40px 20px, 57 by 178. Phone nav instance at 390px: padding 8px, 34 by 114.

Marketing secondary `.c-button.v--secondary` is transparent with colour `rgb(115, 3, 148)` and an inset 1px shadow of the same colour, radius 4px, padding 12px 16px. The footer secondary that was painted is white with a 1px solid `rgb(115, 3, 148)` border.

Sign-in submit `.p-get_started_aubergine_button` is `rgb(74, 21, 75)` with white Slack-Lato 18px weight 700, radius 12px, padding 0 16px 3px, 44 by 400.

Google, Microsoft, and Apple buttons are white, 2px solid `rgba(94, 93, 96, 0.45)`, radius 12px, 44 by 400, Slack-Lato 18px weight 700. They were not clicked.

Hover, pressed, disabled, and loading were not shown.

## Link

Header "Sign in" is `rgb(29, 29, 29)`, Salesforce-Sans 15px weight 700, padding 8px 0. It points at https://slack.com/signin.

Sign-in "Create an account" is `rgb(18, 100, 163)`, Slack-Lato 13px weight 700. It points at https://slack.com/get-started#/createnew. It was not followed.

Footer "Privacy & Terms" is `rgb(105, 105, 105)`, Slack-Lato 15px weight 400, letter-spacing -0.2px.

## Text field

The sign-in email field was already focused. Placeholder `name@work-email.com`. White fill, Slack-Lato 18px weight 400, colour `rgb(29, 28, 29)`, padding 12px, radius 12px, 44 by 400. Border is 1px solid transparent. Focus ring is `rgb(18, 100, 163) 0px 0px 0px 1px` plus a 5px ring at `color(srgb 0.0705882 0.392157 0.639216 / 0.3)`. The resting border was not measured. The field was not filled.

## Text area, select, checkbox, radio, switch

Not present on the pages opened. OneTrust cookie switches are in the DOM. Their painted controls were not measured. The cookie banner height was 0.

## Tabs, menu, tooltip, dialog, toast

The marketing nav keeps a Product panel in the DOM (`rgb(255, 255, 255)`, 546px tall). It was not opened as a visible menu, so hover and panel type were not recorded as a shown state. No tooltip, dialog, or toast was shown.

## Card

Pricing columns `.o-pricing-grid__column` are 268px wide, 1px solid `rgb(229, 229, 229)`. End columns use 12px radius on the outer corners. The featured column is 271px, 2px solid `rgb(163, 80, 175)`, radius 12px, shadow `rgba(24, 24, 24, 0.1) 0px 4px 16px 0px`.

## Badge

`.promo-pill-text` is `rgb(249, 240, 255)` with a 1px solid `rgb(209, 125, 254)` border, radius 20px, padding 3px 10px, Salesforce-Sans 10px weight 600, black text. Copy read: "50% OFF FOR THREE MONTHS*".

## List row, table, avatar

Pricing feature lists sit inside the columns. Individual row styles were not read. No table and no avatar on the pages opened.

## Shared values

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | `html` background on marketing |
| Text | `#1d1c1d` | sign-in body, `--dt_color-content-pry` |
| Muted | `#454447` | `--dt_color-content-sec` |
| Marketing accent | `#730394` | primary button background |
| Sign-in accent | `#4a154b` | `--dt_color-brand-core-aubergine` and submit |
| Aubergine section | `#481a54` | `.c-dark-ai-container` |
| Focus | `#1264a3` | sign-in link and field ring |
| Radius, marketing button | 4px | `.c-button` |
| Radius, sign-in control | 12px | email field and submit |

## Gaps

- Signup at https://slack.com/get-started#/createnew was not entered. The wall is the gap.
- Workspace URL, Google, Microsoft, Apple, and company SSO were not entered.
- No card, phone, or KYC field was shown or filled.
- Resting field border, button hover, focus-visible, pressed, disabled, and loading were not shown.
- Dark theme of the signed-in app was not captured. `.sk-client-theme--dark` exists in the sign-in stylesheet and was not applied.
- Screenshots and crops are missing. The preview browser returned "The browser is not producing screenshot frames".
