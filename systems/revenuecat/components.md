# Components

Measured on 2026-11-19 from computed styles. Marketing controls are from
www.revenuecat.com at 1440 by 900. App controls are from the signed-out login
and signup pages at app.revenuecat.com, which rendered with `html.dark`.

Hover colours below are declared class rules (`hover:bg-secondary-blue-2`),
not a held hover. Focus on the marketing header was read after `focus()`.

## Button

Marketing primary. Header "Sign up". Background `#576ddb`, text `#ffffff`,
height 36px, padding 0 18px, font objectSans 14px / 500, radius pill
(computed `16777215px`). Declared hover background is `#3d52b8`.

Marketing large. Hero "Start for free". Same fill, height 48px, padding 0 28px,
font 16px / 500. At 390px the same control was 44px tall, padding 0 20px,
width 358px.

Marketing ghost. Header "Contact sales". Transparent fill, text `#3d52b8`,
1px border from `border-[#576cdb]/70`, height 36px, padding 0 18px, pill.
Declared hover border and text are `#3d52b8`.

App submit. "Log in" and "Sign up" were `disabled`. Background `#2d2f35`,
text `#75777e`, height 32px, padding 6px 8px, radius 8px, weight 600,
Inter Variable 14px. The enabled primary fill `#606dff` is a stylesheet
token (`--button-primary-bottom`), not a state that was on screen.

## Link

Header "Pricing": objectSans 14px / 400, `#1f1f47`, padding 0 12px, height
64px, radius 4px, colour transition 300ms.

"Log in": objectSans 14px / 500, `#3d3d5c`.

"Talk to sales": objectSans 16px / 500, `#3d52b8`, no background.

App "Sign up": Inter Variable 14px / 600, `#606dff`, padding 8px, radius 8px.

App footer links: Inter Variable 12px / 400, `#a2a4ab`.

## Text field

Marketing email. Placeholder "Your email address...". White fill, 1px
`#eaedf6` border, pill, height 64px, width 480px, padding 20px 176px 20px
28px, objectSans 16px, shadow `rgba(61, 75, 143, 0.15) 0px 6px 16px 0px`.

App email, name and password. Surface `#14161b`, 1px `#2d2f35` border,
radius 8px, height 32px, width 480px (password 434px beside a 24px show
button), padding 6px 14px, Inter Variable 14px, text `#f2f3f5`. Placeholder
"email@example.com".

## Text area

Not present on the pages that were open.

## Select

Signup has a combobox reading "Select One", 480 by 32, radius 8px. It was
not opened. Options were not read.

## Checkbox

Signup marketing opt-in is 16 by 20. Accent colour computed as `auto`.
Checked, hover and disabled were not captured.

## Radio

Not present.

## Switch

Not present on the signed-out pages.

## Tabs

Not present. Pricing has in-page jump links (Growth Tools, All features,
Testimonials, Certifications, FAQs), not a tab widget.

## Menu

At 390px the header Menu button is 40 by 40. The open panel is
`position: fixed; inset: 0`, white, z-index 40, padding-top 64px. Rows are
52px, objectSans 15px / 400, `#1f1f47`: Why RevenueCat?, Solutions,
Developers, Resources, Pricing. Desktop dropdown panels were not opened.

## Tooltip

Not present.

## Dialog

An iubenda cookie banner was on the marketing home. Accept and Reject were
both `#576cdb` (rgb(87, 108, 219)) fill, white text, height 38.4px, padding
8px 32px, radius 64px, weight 700, font `-apple-system`. It was dismissed
with Accept before the other reads. No product dialog was opened.

## Toast

Not present. The app showed an incident banner, not a toast: background
`#f0d81b`, text `#643c00`, radius 8px, padding 8px 12px, height 48px.
Title "Ongoing incident." at 14px / 700.

## Card

Home article: background `#f8f9fb`, 1px `#eaedf6` border, radius 16px,
384 by 426. Title helveticaNeue 18px / 500. Body 18px / 300, line-height
24.75px.

Pricing PRO card: white, 1px `#d6dbf5`, radius 16px, padding 40px, width
960px. Shadow `rgba(87, 108, 219, 0.06) 0 4px 20px, rgba(144, 138, 208, 0.05) 0 30px 60px, rgba(71, 92, 133, 0.03) 5px 5px 30px`.

## List row

Not present as an app list. The phone menu rows are under Menu.

## Table

Not present.

## Avatar

Not present. No account was signed in.

## Badge

Pricing eyebrow "PRO": helveticaNeue 14px / 500, line-height 17.5px, colour
`oklab(0.374539 0.012261 -0.0506019 / 0.8)`, canvas sRGB `#3d3d5bcc`.

## Focus

Marketing header Sign up and Contact sales, after `focus()`: box-shadow
`rgb(255, 255, 255) 0 0 0 2px, rgb(163, 199, 250) 0 0 0 4px`. The ring
token is `hsl(215 90% 81%)`.

App field: stylesheet rule `.Mui-focused .MuiOutlinedInput-notchedOutline`
sets a 2px border in `--mui-palette-primary-main`. Forcing the
`Mui-focused` class did not change the live computed border, so the held
focus colour is a gap.

## Gaps

- No marketing dark theme. `prefers-color-scheme` rules were not in the public stylesheets.
- App light sheet exists on `:root, .light` and was not the live page.
- Enabled app primary button, field error, checkbox checked, select options, desktop nav menus, hover-held states, and pressed states were not captured.
- Password field on login is absent until an email is continued. It was not continued.
- Signup was not submitted. It asks for a name and a password.
