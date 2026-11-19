# Vercel patterns

Public pages measured on 2026-11-19. CSS viewport 1169 by 731. Theme class `dark-theme`, `color-scheme: dark`, page background `rgb(0, 0, 0)`.

## Marketing home

https://vercel.com/ title "Agentic Infrastructure - Vercel". Body text `rgb(237, 237, 237)`, GeistSans 16px / 24px weight 400. The `h1` is 64px / 64px weight 400, letter-spacing `-3.84px`, same text colour. Header actions are "Get a Demo", "Log In", and "Sign Up". The hero pair is "Deploy now" (light pill, 40px) and "Talk to sales" (dark pill, 40px). Content width token `--geist-page-width` is 1200px. Page margin token `--geist-page-margin` is 24px.

## Pricing

https://vercel.com/pricing title "Vercel Pricing: Hobby, Pro, and Enterprise plans". The `h1` is 64px / 64px, weight 450, letter-spacing `-3.84px`. Section titles are 24px / 32px, weight 450, letter-spacing `-0.96px`. Supporting copy is `rgb(161, 161, 161)` at 16px / 24px. Visible plans are Hobby `$0`, Pro `$20` with a "Popular" label, and Enterprise "Custom". Actions stay on the page. Trials and sales were not started.

## Signed-out login

https://vercel.com/login title "Login – Vercel". The `h1` is "Log in to Vercel", 32px / 40px weight 600, letter-spacing `-0.96px`. The form is 320px wide with `gap-4`. It asks for an email, then "Continue with Email". Other options on the same page: Google, GitHub, ChatGPT, SAML SSO, Passkey, and "Show other options". A "Sign Up" link points at https://vercel.com/signup. None of those were followed. The form was not submitted.

## Docs

https://vercel.com/docs title "Vercel Documentation". `html` also has `uncontained tailwind dark-theme`. The `h1` is "Ship anything with Vercel", 48px / 56px weight 600, letter-spacing `-2.88px`. A sidebar measures 264px wide. "Search Docs" is a 264 by 36 button. The search dialog was not opened.

## Geist

https://vercel.com/geist/introduction is the public design system: "Geist Design System", 40px / 48px weight 600, letter-spacing `-2.4px`. https://vercel.com/geist/colors describes 10 scales and two backgrounds. The page stayed on `dark-theme`. A "Theme Switcher" link points at https://vercel.com/geist/theme-switcher and was not opened, so light was not measured. https://vercel.com/design is a team page on `rgb(10, 10, 10)` with `color-scheme: normal` and class `dark`. Its `h1` is 52px / 72px weight 600.

## Gaps

Signed-in dashboard, signup submission, theme switcher, dialogs, and phone width were not captured. Screenshot frames failed, so these notes describe measured CSS, not images.
