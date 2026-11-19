# Patterns

Signed-out pages only. Screenshots were not produced: `preview_snapshot` returned "The browser is not producing screenshot frames" twice. Layout numbers are computed rectangles at innerWidth 1169.

## Marketing home

`https://squareup.com/` redirected to `https://squareup.com/us/en`. Title: Power your entire business.

Header is 72px. Sign up and Log in sit in the header in Cash Sans, white, on a transparent header over a hero whose h1 is also white (Square Sans Display VF, 64px, tracking -0.5px). The painted blue plate measured later on the page is `.HomePageKioskHero-background` at `rgb(0, 75, 255)`. Primary actions are blue pills. Alt actions are white pills with a blue label.

A cookie host `#onetrust-consent-sdk` was in the DOM and had no painted height on this page. It was not dismissed.

## Pricing

`https://squareup.com/us/en/pricing`. Plan cards (`.PwNextPricingPlanCards-card`) are white, radius 10px, padding 20px, 350 by 927 px, class `dropshadow`. Titles are Cash Sans 20px. A later heading uses Exact Block at 56px. Get started and Try free for 30 days are the same pill actions. Those signup URLs were not used as the entry to the wall. The wall was opened separately by URL and not filled.

## Signed-out login

`https://app.squareup.com/login?lang_code=en-us`. Title: Square: Sign in to Your Dashboard & Manage your Business. Not a Cloudflare challenge.

A split layout (`.layout-split-login--v3`) fills the viewport, white. The form column is 585px. Heading "Sign in" is 25px Square Sans Display VF, weight 700, colour `rgb(16, 16, 16)`. The email or phone field, a black Continue pill, an "or" divider (`rgb(240, 240, 240)`), and a grey passkey pill stack in the form. The right slot (`.product-tips-v3-animation-slot`) is `rgb(16, 16, 16)`, 505 by 483 px, with ticker text at white 15% opacity.

Nothing was typed. Continue was not clicked. Passkey was not clicked.

## Signup wall

`https://app.squareup.com/signup/en-US`, opened by URL. Heading "Create your free account" at 36px, weight 400, colour `rgb(16, 16, 16)`. Visible copy names Email, Password, an 8-character hint, an agreement to Terms, Privacy Policy, and E-Sign Consent, and Create account. reCAPTCHA Enterprise is named in the page text. No field was filled. Create account was not clicked. This is the wall.

## Not captured

App shell after login, validation errors, empty and loading states, destructive confirmation, search, tables, onboarding, dark theme, and a 390px layout. The viewport was the preview pane at 1169 by 731.
