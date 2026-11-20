# Patterns

Public pages only. The product app was not entered. Which control opens which page is in [site-tree.md](site-tree.md). A second pass on 2026-11-21 walked that tree at 1440×900 and 390×844 and stopped at https://runey.app/auth.

## Home

[home-light-default.png](screenshots/home-light-default.png) is the marketing home after the cookie card was dismissed, at 1440 by 900 CSS pixels, device pixel ratio 2. [home-light-cookie.png](screenshots/home-light-cookie.png) is the same page with the cookie card still open. [home-light-phone.png](screenshots/home-light-phone.png) is the home at 390 by 844.

The page sits on `light.surface.page`. A fixed bar holds the wordmark, Features, FAQ, Pricing, Updates, Log in and Start for free. The hero is one Poppins heading at `core.typography.hero`, a lede at `core.typography.lede` in `light.text.lede`, then a primary pill, a secondary pill and a ghost pill. Below that is a product screenshot, a scrolling row of feature photographs, three text columns, a feature chip row, pricing cards, quotes, an FAQ and a black footer.

The footer uses `light.surface.footer` with links in `light.text.footer`. It is the only large black region on the public page.

## Pricing on the home

Three cards share one body: Solo, Team and Agency. A pill track above them selects Monthly, Yearly or Lifetime. Yearly was selected when the page loaded. Each card ends in a primary pill labelled Start 14-day free trial. That pill links to `/auth`. It was not followed into a payment.

The 2026-11-21 pass also opened the Features menu, the feature tabs, Yearly and Lifetime pricing, the FAQ answer, the cookie Customize panel, and the phone menu. Those shots are named in [site-tree.md](site-tree.md) and sit beside the earlier home shots in [screenshots/](screenshots/). Feature pages, updates, help, contact, feedback, and the legal pages were captured the same day. `/pricing`, `/blog`, `/about`, `/privacy`, `/changelog`, `/features`, and `/legal` redirect to the auth wall and were not entered.

## Auth

[auth-light-signin.png](screenshots/auth-light-signin.png) is `/auth` on the sign-in view. [auth-light-signup.png](screenshots/auth-light-signup.png) is the same URL after Sign up was clicked. Nothing was typed and nothing was submitted.

The page keeps the marketing nav. The form sits in a white card on a pale frame. Sign in has Continue with Google, an email field, a password field and Sign In. Sign up adds a full name field and a short agreement line. Google was not followed. The form asks for a name as well as email, so it was not submitted.

## Coverage

| Checklist item | Status |
|---|---|
| Colour, type, spacing, radius, border, elevation | Captured on the public pages. See [tokens.json](tokens.json). |
| Motion | Partial. Computed 150ms standard easing on buttons and links. Reduced motion was not shown to stop the page. |
| Button | Default and hover. Pressed, disabled and loading not on the page. |
| Link | Nav and footer links, default. |
| Text field | Email, password and full name, empty. Focus measured on email. |
| Text area, select, checkbox, radio, switch | Not present on the public pages. |
| Tabs | Feature chips and the billing track. |
| Menu | Features button is present. The open menu was not captured. |
| Tooltip, toast, dialog | Not present, apart from the cookie card. |
| Card, list | Plan cards, quote cards, FAQ. |
| Table, avatar, badge | Not present as product controls. Photos in the feature row are marketing images. |
| Form with a validation error | Not captured. Nothing was submitted. |
| Empty, loading, error | Not captured. The public pages have no empty app state. |
| Destructive confirmation | Not present. |
| Search and filtering | Not present. |
| App shell | Not captured. Behind sign-in. |
| Light and dark | Light was painted. Dark is declared in CSS and was not applied. |
| Desktop and phone | 1440 and 390 screenshots. Computed styles were read at 1169. |
