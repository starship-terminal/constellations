# Fourmula.ai public site tree

Captured 2026-11-21 from the live site in headless Chromium. Desktop shots are 1440x900. Phone shots are 390x844 CSS, saved at 2x (780x1688). The cookie banner was photographed, then hidden. It was not accepted.

`signed_in` is false. The walk stopped at the auth wall.

## Pages that paint

| URL | Status | What it is | Shot |
|---|---|---|---|
| https://fourmula.ai/ | 200 | Marketing home. One Webflow page. Last published note in the 404 HTML: Thu Aug 13 2026. | [home-light-default.png](screenshots/home-light-default.png), [home-dark-default.png](screenshots/home-dark-default.png), [home-light-full.png](screenshots/home-light-full.png) |
| https://fourmula.ai/privacy-policy | 200 | Privacy and cookies policy. H1: FOURMULA AI PRIVACY & COOKIES POLICY. | [privacy-light-default.png](screenshots/privacy-light-default.png) |
| https://fourmula.ai/terms-of-service | 200 | Terms of use. H1: TERMS OF USE. | [terms-light-default.png](screenshots/terms-light-default.png) |
| https://fourmula.ai/login | 404 | Styled error page. H1: Our fourmula is broken. | [notfound-light-default.png](screenshots/notfound-light-default.png) |
| https://app.fourmula.ai/auth | 200 | Empty sign-in wall. Email, password, Google. Not submitted. | [auth-dark-signin.png](screenshots/auth-dark-signin.png) |
| https://app.fourmula.ai/start | 200 | Public start page. Copy says no login. Create asset was not followed. | [start-dark-default.png](screenshots/start-dark-default.png) |
| https://app.fourmula.ai/ | 200 | Redirects to https://app.fourmula.ai/start | same as start |

These marketing paths also 404 to the same styled error page: `/cookie-policy`, `/start`, `/auth`, `/pricing`, `/blog`, `/about`, `/faq`, `/contact`. `/sitemap.xml` is 404. `/robots.txt` is 200 and empty of page URLs in the body that was read.

## Home page sections

The home page is one document. Header links scroll to these ids.

| Id | Section |
|---|---|
| `#hero` | Headline, orbit of sample shots, upload drop zone |
| `#what-is-fourmula` | What you can do |
| `#pdp` | PDP feature |
| `#products` | Product shots feature |
| `#video` | Video feature |
| `#list` | Feature list and how-it-works |
| (no id) | FAQ accordion |
| (no id) | Footer |

Hash clicks from the menu, measured on desktop: `#pdp` scrolled to 359, `#products` to 789, `#video` to 1180, `#list` to 1616, `#what-is-fourmula` to 1236.

## Header

The header sits on every marketing page. On the 404 the menu control is replaced by a Home link back to `/`. The theme icon, account icon, and Get started stay.

| Control | Opens |
|---|---|
| Logo (`/`) | https://fourmula.ai/ |
| Menu (`.header__menu`) | In-page panel. Second click closes it. Shot: [home-light-menu.png](screenshots/home-light-menu.png), phone [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Theme icon (`.header__theme`) | Toggles `body.dark`. The class present is the light page. Removing it paints the dark page. Shot: [home-dark-default.png](screenshots/home-dark-default.png) |
| Progress label (`0%`) | No navigation. It is a scroll progress readout. |
| Account icon | https://app.fourmula.ai/auth in a new tab. Auth wall. |
| Get started | https://app.fourmula.ai/start in a new tab. Public start page. |

## Menu panel

| Label | Href | Result |
|---|---|---|
| PDP's | `#pdp` | Scrolls to the PDP section on the home page |
| Products | `#products` | Scrolls to the products section |
| Videos | `#video` | Scrolls to the video section |
| Our features | `#list` | Scrolls to the feature list |
| Privacy Policy | `/privacy-policy` | Privacy page |
| Terms of Service | `/terms-of-service` | Terms page |
| Cookie Policy | `#` | No page. The click did not open a preference dialog in the walk. The cookie banner is a separate overlay. |
| Instagram | https://www.instagram.com/fourmula.ai | External, new tab. Not opened. The live href also carries a share parameter. That parameter is omitted here. |
| Linkedin | `#` | Dead hash. No destination. |
| Youtube | `#` | Dead hash. No destination. |
| Get started (inside the panel) | https://app.fourmula.ai/start | Public start page, new tab |
| Account icon (inside the panel) | https://app.fourmula.ai/auth | Auth wall, new tab |

The footer repeats a smaller set: logo to `/`, PDP's to `#pdp`, Videos to `#video`, Products to `#products`, Our features to `#list`, Privacy, Terms, Cookie Policy (`#`), Instagram (external), Facebook (`#`), Youtube (`#`). Footer copy names the company and a registration line. That line is public marketing text.

## In-page controls

| Control | Opens |
|---|---|
| SCROLL DOWN | `#what-is-fourmula` |
| Upload or drop your assets (`#dropZone`, `input[type=file][accept=image/*]`) | A file picker. No file was chosen. |
| Orbit chips (PDPs, UGC, Lifestyle shots, Ads, Stories, Street style) | In-page labels on the hero. They were not separate routes. |
| Get started, repeated in the how-it-works steps | https://app.fourmula.ai/start |
| Feature card wordmarks | https://app.fourmula.ai/start |
| FAQ row (`.faq__item-title`) | Opens that row's answer in place. Shot: [home-light-faq.png](screenshots/home-light-faq.png) |
| Awwwards badge | https://www.awwwards.com/sites/fourmula-ai, new tab. Not opened. |

FAQ answers, read from the DOM:

1. What can AI FOURMULA create for my brand? Product images, fashion shots, lifestyle scenes and short videos for PDPs, social, ads and email.
2. What do I need to start? Just a store link or a product photo. We use it to generate on-brand visuals automatically.
3. Will the visuals match our brand look? Yes. We learn from your existing images and keep colours, lighting and style consistent.
4. Do I own the assets you generate? Yes. All approved outputs are yours to use across any channel.
5. How fast do I get results? Usually in seconds or a few minutes, depending on how many assets you request.
6. Does this replace my creative team? No. It speeds up production so your team can focus on ideas, not manual reshoots and cropping.

## Search

The public marketing site has no search field, search button, or search dialog. None was photographed.

## Cookie banner

It paints after the preloader, bottom right. Controls: close, Accept all, Settings, and a privacy policy hash inside the copy. None of those were clicked. The banner was hidden with CSS after the cookie shots: [home-light-cookie.png](screenshots/home-light-cookie.png), [mobile-home-light-cookie.png](screenshots/mobile-home-light-cookie.png).

## Auth wall

https://app.fourmula.ai/auth. Empty. Not submitted. Google was not clicked. No email or password was typed. See [login-review.json](login-review.json).

| Control | What it did when opened only far enough to read |
|---|---|
| Open main menu | A menu with Shopify integration and Website. Shot: [auth-dark-menu.png](screenshots/auth-dark-menu.png). Website was not followed. |
| Create asset | On the start page this goes to a generator. That branch was not followed from the wall. |
| Sign in (header) | Stays on the sign-in dialog |
| Back | Stays on the wall |
| Continue with Google | Not clicked |
| Email address | Empty field. Not filled. |
| Password | Empty field. Not filled. |
| Toggle password visibility | Not clicked |
| Forgot password? | Shows a validation line, "Please enter a valid email address", because the email field was empty. No reset was requested. Shot: [auth-dark-forgot.png](screenshots/auth-dark-forgot.png) |
| Sign in (submit) | Not clicked |
| Sign up | Swaps the dialog to Create account: email, password, Continue with Google, Sign up. Not submitted. Shot: [auth-dark-signup.png](screenshots/auth-dark-signup.png) |

## Not captured

The signed-in app was not captured. Generator, Shopify connect, onboarding, plans, and profile were not opened. Unread token values are Not captured.
