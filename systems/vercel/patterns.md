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

## Signed-in dashboard

Walked on 2026-11-21 from an already signed-in Hobby scope. Start URL `https://vercel.com/dashboard`, landed on the scope overview. Measured CSS viewport 1440 x 900 at device pixel ratio 2, and 390 x 844 at device pixel ratio 2. Theme stayed `dark-theme`. The public token set was not rebuilt from this pass.

The desktop shell is a 256px sidebar of 36px rows, a header with the scope switcher, All Projects, the page title, Create New, and Agent, and a Find field. Overview is a usage card, an alerts empty card, a projects list, and recent previews. [overview-dark-desktop.png](screenshots/overview-dark-desktop.png).

Create New is a two-column menu: Project, Domain, Integration, Sandbox, Agent, Store, AI Gateway Key, Team Member. It was opened and closed. [create-menu-dark-desktop.png](screenshots/create-menu-dark-desktop.png).

Deployments is a filter row (Created, Author, Environment, Status and others) over a list of rows with project, message, Ready, Production or Preview, and a short id. Filters already on the page were not changed. [deployments-dark-desktop.png](screenshots/deployments-dark-desktop.png).

Domains is an empty state: a disabled search, Connect External, Transfer In, Buy, and "Add a domain". None of those were submitted. [domains-empty-dark-desktop.png](screenshots/domains-empty-dark-desktop.png).

Team Settings General is a settings sidebar plus stacked cards (Team Name, Team URL, Team Avatar, Preview Deployment Suffix) with a light Save button. Save was not clicked. A collaborator username in the sidebar was painted out. [settings-general-dark-desktop.png](screenshots/settings-general-dark-desktop.png).

At 390 the sidebar is gone. The header is the scope name, search, a filter, and a plus button. Recents, Usage and Alerts sit in a segmented control. A Find bar sits at the bottom. [overview-dark-phone.png](screenshots/overview-dark-phone.png). The scope switcher is a full-screen sheet with the current Hobby scope, an empty teams list, and Create Team. Create Team was not followed. [scope-switcher-dark-phone.png](screenshots/scope-switcher-dark-phone.png).

## Gaps

Signup submission, the theme switcher, and public-page dialogs were not captured. The 2026-11-19 public notes describe measured CSS, not images. The signed-in gaps are in [login-review.json](login-review.json).
