# Ulysses public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as `https://ulysses.app/` (wordmark "Ulysses", hero "The Ultimate Writing App for Mac, iPad and iPhone"). `https://ulysses.app/` redirects to `https://ulysses.app/en/`.

This is the first capture of the public marketing site. The package slug is `ulysses`. There is no `systems/ulysses-ios/` on this branch.

Nothing was typed. No form was submitted. No captcha was solved. Checkout was not entered. `login-extracted` stays `not-started`.

The marketing site paints one light theme. `color-scheme` on the root was `normal`. There is no theme control. The consumer app is sold through the App Store and Setapp. The only web account wall found is volume licensing at `license.ulysses.app`.

No cookie sheet was painted on the pages opened.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Marketing `/login`, `/signin`, `/signup`, `/register`, `/account` | The site's own 404, "This page is missing" | Not an account wall. |
| `account.ulysses.app`, `id.ulysses.app`, `auth.ulysses.app`, `my.ulysses.app` | No DNS | Not a product page. |
| Footer "Volume Licensing", and Pricing "Learn More" | `https://license.ulysses.app/` redirects to `https://license.ulysses.app/checkout` | Signup form for a volume-licensing purchase. Photographed empty. Continue to Checkout not clicked. Country select not opened. Terms checkbox not checked. |
| "log in here" on that page | `https://license.ulysses.app/users/sign_in` | "Log In". Empty Email. Empty Password. Log In not clicked. Forgot your password not opened. |
| "sign up" on the login wall | `/checkout` | Already photographed. Not followed again. |
| Contact form, newsletter form | Would submit | Fields left empty. Not submitted. |

The writing app itself has no public web login. Sign-in for the Mac, iPad, and iPhone app was not attempted.

## Homepage header (`https://ulysses.app/en/`)

Desktop, left to right: logo to `/en/`, Why Ulysses (`/en/`), Pricing (`/en/pricing/`), Stories (`https://stories.ulysses.app/`), Help (`https://help.ulysses.app/`). The bar is white. Why Ulysses is the current page and carries a yellow underline. There is no dropdown menu.

Stories and Help are other hosts. They were mapped and not photographed as product pages.

Phone (390): logo and a menu toggle labelled "Toggle navigation". The open drawer lists Why Ulysses, Pricing, Stories, and Help. The drawer was photographed closed and open. No row was followed.

## Footer

Photographed on the 404. The bar is near-black (`#262626`) with yellow links.

- Company: People (`/people/`), Jobs (`/jobs/`), Press (`/press/`), Privacy (`/privacy-policy/web/`), Imprint (`/imprint/`).
- Explore: Newsletter (`/newsletter/`), New Features (`/en/releases/`), Beta (`/en/beta/`), Affiliate Program (`/en/affiliate/`).
- Help & Licensing: Help & Support (`https://help.ulysses.app/`), Community (`https://cafe.ulysses.app/`), Styles & Themes (`https://styles.ulysses.app/`), Students (`/en/students/`), Volume Licensing (`https://license.ulysses.app/`), Contact Us (`/contact/`).
- Language: English, and 简 (`/zh/`).
- Subscribe to Newsletter (`/newsletter/`).
- Twitter, Mastodon, Weibo. Those are other hosts and were not opened.
- © 2026 Ulysses GmbH & Co. KG.

The volume-licensing host uses a different footer: Company, Updates (Blog at `https://blog.ulysses.app/`), Help & Licensing, plus Facebook, LinkedIn, and vKontakte. That footer was photographed on the login wall and not walked.

Community (`cafe.ulysses.app`) returned a human-verification page to a plain fetch. It was not opened in the browser and the captcha was not solved.

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Home | `https://ulysses.app/en/` | Desktop and phone, drawer open and closed |
| Pricing | `https://ulysses.app/en/pricing/` | Desktop. $39.99 per year, or $5.99 per month. App Store and Setapp badges. Volume licensing "Learn More" not followed from this page. |
| Students | `https://ulysses.app/en/students/` | Desktop |
| New Features | `https://ulysses.app/en/releases/` | Desktop |
| People | `https://ulysses.app/people/` | Desktop |
| Jobs | `https://ulysses.app/jobs/` | Desktop |
| Press | `https://ulysses.app/press/` | Desktop |
| Privacy | `https://ulysses.app/privacy-policy/web/` | Desktop |
| Imprint | `https://ulysses.app/imprint/` | Desktop |
| Newsletter | `https://ulysses.app/newsletter/` | Desktop, form empty, not submitted |
| Beta | `https://ulysses.app/en/beta/` | Desktop |
| Affiliate | `https://ulysses.app/en/affiliate/` | Desktop |
| Contact | `https://ulysses.app/contact/` | Desktop, form empty, not submitted |
| 404 | `https://ulysses.app/this-page-is-missing/` | Desktop. "This page is missing". Back to Homepage not clicked. |
| Login | `https://license.ulysses.app/users/sign_in` | Empty wall |
| Signup | `https://license.ulysses.app/checkout` | Empty first screen. Checkout not entered. |

Chinese (`/zh/`) was mapped from the footer and not photographed.
