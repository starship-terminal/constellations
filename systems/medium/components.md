# Components

Values are computed styles from the T3 preview browser on 2026-11-19. Crops are reconstructions of those boxes. See [What to distrust](README.md#what-to-distrust).

## Button

Primary pill. Get started on the home header.

| State | Background | Text | Border | Radius | Padding | Size |
|---|---|---|---|---|---|---|
| Light default | #191919 | #ffffff | 1px solid #191919 | 1386px | 8px 16px | 14px / 20px, height 38px |
| Light hover | #080808 | #ffffff | 1px solid #242424 | 1386px | 8px 16px | same |
| Dark default | #ffffff | #121212 | 1px solid #ffffff | 1386px | 8px 16px | 14px / 20px, height 38px |
| Dark hover | #f2f2f2 | #121212 | 1px solid #d2d2d2 | 1386px | 8px 16px | same |
| Focus, dark | same face | same | same | same | same | outline rgb(153, 200, 255) auto 1px |

Font is sohne. Transition is `background-color 0.3s linear, color 0.3s linear`.

Start reading is the same face at 20px / 28px, padding 8px 20px, height 46px, radius 1980px.

Secondary pill. Sign in on membership: transparent face, 1px solid #242424, text #242424, radius 1386px, height 38px. View plans matches that at 16px, radius 1584px, height 42px.

OAuth row. Sign in with Google and the sibling rows: #ffffff face, 1px solid #242424, text #242424, radius 1584px, padding 8px, 300 x 42, sohne 16px. Not pressed.

Continue. #191919 face, white text, radius 1386px, 90 x 38. Not pressed.

Select on /plans. Same primary face, width 262px at 1440 and 276px at 390. Not pressed.

Disabled, loading, and error were not on these pages.

## Link

Nav links (Our story, Membership, Write, Sign in): sohne 14px / 20px, weight 400, colour #242424 in light. No underline at rest. Footer links: medium-content-sans-serif-font 16px, colour #242424, y=856 at 1440.

## Text field

Email field on `/m/signin` after "Sign in with email", focused, empty.

| Part | Value |
|---|---|
| Wrapper | #f2f2f2, radius 4px, padding 8px 12px, 360 x 38, border 1px solid transparent |
| Input | sohne 14px, placeholder "Enter your email address" |
| Focus | still #f2f2f2, outline none. No extra ring was computed |
| Label | "Your email", sohne 14px, #242424 |

Continue was not pressed, so no error state exists in this package.

## Badge

Welcome Offer on /plans: background #ffc017, text #242424, radius 8px, padding 4px 8px, height 28px. The inner span is sohne 14px.

## Billing control

Two labels, not a switch. Pay monthly: transparent, 1px solid #242424, radius 4px 0 0 4px, padding 12px 24px 10px, 139 x 72. Pay annually: background #f9f9f9, 1px solid #e5e5e5, radius 0 4px 4px 0, 141 x 72. Neither was toggled.

## Story title and body

Blog story h1: sohne 42px, weight 700, line-height 52px, letter-spacing -0.462px, colour #242424, width 680px.

Kicker: sohne 22px / 28px, weight 400, colour #6b6b6b.

Body: source-serif-pro 20px / 32px, letter-spacing -0.06px, colour #242424, width 680px.

Caption: sohne 14px / 20px, colour #6b6b6b, max-width 728px.

## Display

Home h2: gt-super 120px / 100px, letter-spacing -6.6px, colour #000000 in light, width 720px, x=124.

Phone home h2, dark: gt-super 80px / 72px, letter-spacing -4.4px, colour #ffffff, x=24, width 253px.

Membership h2: gt-super 85px / 88px, letter-spacing -4.675px.

Plans h1: gt-super 48px, letter-spacing -1.92px. At 390 dark it is 32px, colour #ffffff.

Sign-in title: gt-super 28px, colour #000000.

## Wordmark

SVG at viewBox `0 0 719 160`, drawn at 112 x 25. Authored path fill is `#242424`. The winning rule `.bv path` sets `fill: var(--color-fg-neutral-primary)`, which computed to `#e5e5e5` in dark. [icons/wordmark.svg](icons/wordmark.svg) uses `currentColor`.

## Help search

help.medium.com, a separate theme. The ask-box is #171717 in dark (oklch 0.2052), radius 20px, 704 x 62, border `1px solid oklch(0.58 0 0)`. The input is 702 x 60, padding `1px 20px 1px 52px`, Sohne 18px. Not submitted.

## Gaps

| Component | Why it is missing |
|---|---|
| Text area | No public composer. Write redirects toward sign-in and was not followed |
| Select | No native select on the captured pages |
| Checkbox, radio, switch | Remember-me input computed to 0 x 0. Billing is two labels |
| Tabs, menu, tooltip, dialog, toast | Not opened. Reach flags exist on `:root` |
| Avatar | Not measured on these signed-out pages |
| Table | No data table |
| Error, disabled, loading | Continue and Select were not pressed |
| Signed-in shell | Behind `/m/signin` |
| Checkout | Select was not pressed. No card, phone, or KYC |
