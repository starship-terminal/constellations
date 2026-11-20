# Patterns

Signed-out pages only. Screenshots were not produced: the preview browser returned "The browser is not producing screenshot frames" twice. Layout numbers below are computed rectangles at innerWidth 1169.

## Marketing home

`https://www.paypal.com/` redirected to `/sg/home` (PayPal Open, business-first). `https://www.paypal.com/us/home` stayed on the US personal home.

The page is a stack of full-bleed plates. At this width the hero is a white `primary-plate` (about 806 to 904 px tall, padding-top 39.25px). Later plates are cyan (`accent-1`, US), navy (`accent-3`), black (`secondary-plate`), and grey (`tertiary-1`). Headlines sit in PayPal Pro at weight 900. Primary actions are black pills. Secondary actions are a translucent navy wash.

The US home header measured 50px tall and held Personal and Business links only. No Log in control was in that header. Login chrome is a separate URL.

A cookie banner was in the DOM (Yes, I accept / Close) with wrapper fill `rgb(240, 242, 249)`. It was not dismissed by this capture. Body carried `ccpaCookieBanner-acceptedAll` on the SG home.

## Signed-out login

`https://www.paypal.com/signin`. Title: Log in to your PayPal account.

A 460px card (`#content`) sits at x 355, y 120, padding 30px 46px 50px, 1px border `rgb(234, 236, 237)`, radius 12px. Heading is 24px pp-open-regular in `rgb(0, 20, 53)`. The email field, a blue Next button, a Passkey button, an "or" divider (visible in the text), and a Sign Up button stack inside the card. Footer languages: English, Français, Español, 中文. Footer links in the text: Contact Us, Privacy, Legal, Policy Updates, Worldwide.

Nothing was typed. Next was not clicked. Sign Up was not clicked.

## Signup wall

`https://www.paypal.com/us/webapps/mpp/account-selection`, reached by URL, not by submitting login. Heading eyebrow "Sign up for PayPal", headline "The secure way to pay and get paid" at 43.392px. Two cards, Personal and Business, padding 32px, radius 24px, on a tertiary plate. Each Get Started points at `https://www.paypal.com/welcome/signup`. That URL was not opened. No card, bank, phone, or identity field was on this page.

## Not captured

App shell after login, validation errors, empty and loading states, destructive confirmation, search, tables, onboarding, dark theme, and a 390px layout. The viewport was the preview pane at 1169 by 731.
