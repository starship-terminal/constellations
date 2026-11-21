# untitled public site tree

Mapped on 2026-11-22 from the live public site, signed out, in an incognito browser. Official domain confirmed as `https://untitled.stream` (title "[untitled]— a sacred place for your work-in-progress music", wordmark `[untitled]`, disc hero). This is the Untitled music product, not a parked page and not a captcha wall.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No email, password, code, phone, address, or recovery phrase was entered. Checkout was not clicked. Add to Cart was not clicked. `login-extracted` stays `not-started`.

The marketing homepage follows the browser colour scheme. `data-theme` was `dark` when the browser asked for dark, and the same routes painted a white page when the browser asked for light. Both are the public site. The signed-in app was not opened.

## Homepage header (`https://untitled.stream/`)

Desktop 1440. A dark or white bar, depending on the colour scheme. Left: the tagline "A sacred place for your work-in-progress music". Right: two bracketed links and one pill.

| Control | Opens |
|---|---|
| [shop] | `https://untitled.stream/shop` Public merch grid. Two products. |
| [membership] | `https://untitled.stream/pricing` Public pricing. |
| Enter App | `https://untitled.stream/login`, which redirects to `https://untitled.stream/welcome`. Empty gate. Branch stopped after the empty provider walls. |

The hero is a disc carousel. It is artwork, not a control. The names printed on the discs ("UNTITLED", "BROOKLYN, NEW YORK") are the product mark, not an account.

## Bottom pill bar (homepage)

Pinned over the hero. Social pills, one hiring pill, a Learn more control, and store pills.

| Control | Opens |
|---|---|
| [untitled broadcast network] | `https://www.instagram.com/untitledbroadcastnetwork/` Other host. Not photographed. |
| IG | `https://www.instagram.com/untitledinbrackets/` Other host. Not photographed. |
| X | `https://x.com/uuuntitleddd` Other host. Not photographed. |
| We're hiring | `https://jobs.untitled.stream/` Other host. Not photographed. |
| Learn more | In-page walkthrough. It swaps the disc hero for a product demo (desktop window and phone). Not a menu. Not a signed-in app. The demo shows public sample titles ("Zarkin", "untitled project", "67 west st (demos)"). |
| iOS | App Store listing `id6445854828`. Other host. Not photographed. |
| Android | Play Store `stream.untitled`. Other host. Not photographed. |
| MacOS | App Store listing `id6744922982`. Other host. Not photographed. |

## Homepage body and footer

Feature sections sit under the hero. One inline link.

| Control | Opens |
|---|---|
| Read more. | `https://untitled.stream/trust` Public Trust & Security page. |
| Terms | `https://untitled.stream/terms` Public terms. Last updated 23 January 2026. |
| Privacy | `https://untitled.stream/privacy` Public privacy page. |
| Cookie Settings | Reopens the consent dialog. Not opened this pass. |
| Cookie Policy | `https://untitled.stream/cookie-policy` Public. Not separately photographed. |
| Contact Us | `mailto:contact@untitled.stream` Not opened. |

## Consent dialog

First paint on a fresh browser shows a "We value privacy" card, bottom left. It is a dialog, not a page.

| Control | What it does |
|---|---|
| Customize | Opens cookie preferences. Not followed. |
| Reject all | Posts to `/settings/cookies`. Dismisses the card. Not used for the committed page shots. |
| Accept all | Posts consent. Not clicked. |
| Privacy Policy | `/privacy` |
| Cookie Notice | `/cookie-policy` |

## Shop

| Control | Opens |
|---|---|
| Back | Homepage. |
| [purple] tee | `https://untitled.stream/shop/purple-tee` Public product. $18.00. Size "Large T-shirt". Quantity stepper. Add to Cart was not clicked. |
| [white] babytee | `https://untitled.stream/shop/white-babytee` Same shape. Not photographed separately. |
| Cart | Drawer. Empty state: "[cart] Cart is empty", Total $0.00, Checkout. Checkout was not clicked. Closed with Escape. |

## Pricing (`https://untitled.stream/pricing`)

| Control | Opens |
|---|---|
| [untitled] | Homepage. |
| Enter app | Same welcome gate as Enter App. Not followed from this page. |
| Subscribe | `https://untitled.stream/login?next=%2Fmembership%2Fsignup%3Finterval%3Dyear` Account wall. Not followed. |
| Yearly / Monthly | In-page radio. Yearly is checked. Price shown: $49.99 / year on [membership]. Monthly was not switched for the committed shot. |

Plans on the page: [starter] (Free) and [membership]. No account required to read them.

## Trust (`https://untitled.stream/trust`)

Public article. Header is the wordmark and Enter App. Body links: Latacora (`https://www.latacora.com/`, other host, not photographed) and `mailto:security@untitled.stream` (not opened).

## Phone (390)

The phone homepage drops [shop] and [membership]. The Enter App pill becomes an App Store badge (`https://untitled.onelink.me/IUzL/upsell`). The disc hero stays. Footer links stack: We're hiring, then the social links, then Terms, Privacy, Cookie Settings, Cookie Policy, Contact Us. Pricing at 390 stacks the plan cards and puts Yearly / Monthly under the starter card.

## Auth walls

Photographed empty. Stopped there.

| Control | URL | What it asked |
|---|---|---|
| Enter App | `/login` redirects to `/welcome` | Create account, I have an account. No fields. |
| Create account | `/sign-up` | Sign up with Apple, Google, Email, device only. No fields. Providers not clicked. |
| I have an account | `/sign-in` | Sign in with QR Code, Apple, Google, Email, Phone, Recovery Phrase. No fields. Providers not clicked. |

The signed-in app was not entered.
