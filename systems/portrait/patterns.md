# Portrait patterns

Public marketing pages plus the signed-out sign-in dialog, then the editor shell after an email-only signup. Viewport 1169 by 731. No screenshots: the preview browser did not produce frames.

## Marketing shell

The homepage, /pages, /wallet, /pay, /blog, /points, and /hosting share one shell. Body background `#f7f7f7`, text `#353535`, Switzer 16px / 24px. The header is fixed, transparent, padding 32px 32px 0, height 80px. Inside it, a nav row is 48px tall with a wordmark, a "New / Introducing Portrait Wallet" pill link, and Log in plus Sign up.

Headings use Basier Circle at weight 500 in navy `#08304c`. The homepage h1 is the fluid display size, 71.49px at this width. Sections stack a heading, a short lede, and a pill button.

The footer is white, padding 32px 0, with quiet links at `#797979`.

## Sign-in

Log in opens a dialog on the current page. `/login` redirected back to `/`. The dialog offers Portrait Wallet, email, or another wallet. Email is a single field. Submit sends a code from privy.io. The code step is six cells. After the code, a terms step offers Accept or No thanks. Accepting creates the account. No card, phone, or government ID was asked.

## Editor

`/editor` is a dark canvas, `#141414`, white text. Publish sits top right as a rainbow-ringed pill. Account sits bottom left as a glass pill with a 28px avatar. The account menu lists Create your Portrait, Explore, Appearance, and Log out. Appearance lists Cancel, Light, Dark, and System. System was the selected row. Publish was not pressed.

## Points

`/points` shows a public dashboard shell with Points 0 and Referrals 0, a Dashboard tab, and a locked "Connect with X" task. The sign-up task was already satisfied in this session, so the empty numbers are the signed-in empty state.

## Gaps

Phone layout, a live dark marketing theme, a validation error, a toast, and a destructive confirm were not on these pages. The forced `data-mode="dark"` pass flipped the page to `#141414` and the body text to white. The h1 stayed navy. That pass is not a live theme capture.
