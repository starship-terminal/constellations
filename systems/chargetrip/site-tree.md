# Chargetrip public site tree

Walked signed out on 2026-11-21 from [https://chargetrip.com](https://chargetrip.com). That origin redirects to [https://www.chargetrip.com/](https://www.chargetrip.com/) (HTTP 200, title "Chargetrip EV routing | Routing revenue"). Desktop viewport 1440 by 900. Phone viewport 390 by 844. The page paints light (`color-scheme: normal`, page ground `rgb(239, 237, 229)`). No page-level theme switch. A fixed "Cookie Settings" card mounts on the marketing routes. It was hidden for screenshots, never accepted or rejected.

Opened means the control was used and the result was read or photographed. Linked means the href was read and the destination was not opened in this pass. Sign-in, sign-up, and identity-provider walls stop the branch.

## Header, desktop

The logo (`a[href="./"]`) links to `/`. Contact sales links to `/contact/sales`. Sign in links to `https://account.chargetrip.com`, which redirects to `https://account.chargetrip.io/` (HTTP 200). Wall. Not submitted. The photographed card is [signin-light-default.png](screenshots/signin-light-default.png).

Products, Use cases, Developers, Pricing, and Company are hover panels. They keep the URL on `/`. The panel root is `[data-framer-name="Desktop - Products"]`. Only the hovered group's `pointer-events` turns on. Photographed in [home-light-menu.png](screenshots/home-light-menu.png) (Products).

### Products

| Control | Opens |
|---|---|
| No-code | `/no-code`. Subtitle: Get ready-made solutions. |
| API | `/api`. Subtitle: Build your own custom solutions. |
| Integration Partners | `/use-case-legacy/integration-partners`. Subtitle: Resell Chargetrip EV routing. |

### Use cases

| Control | Opens |
|---|---|
| CPO | `/cpo`. Subtitle: Grow your utilization. |
| eMSP | `/emsp`. Subtitle: Grow your margins. |
| Leasing | `/leasing`. Subtitle: Lease more EVs and monetize charging. |
| Rental | `/rental`. Subtitle: Increase your EV fleet's utilization. |
| OEM | `/oems`. Subtitle: Transparent and accurate range marketing. |
| Fleet Management | `/fleets`. Subtitle: Plan charge stops for fleets. |
| Consulting | `/consulting`. Subtitle: Business intelligence for fleet electrification. |
| Retailers | `/retailers`. Subtitle: Grow retail sales with EV charging. |
| Looking for a different use-case? | `https://meetings-eu1.hubspot.com/admoni/use-case-menu`. Booking. Not submitted. |

### Developers

| Control | Opens |
|---|---|
| Playground | `https://playground.chargetrip.com`. Subtitle: Try the API test environment. Credential wall. Stopped. |
| Documentation | `https://developers.chargetrip.com`. Subtitle: How to build with Chargetrip. Public docs shell. |

### Pricing

| Control | Opens |
|---|---|
| No-Code Pricing | `/pricing/nocode`. Subtitle: Save on dev time. |
| API Pricing | `/pricing/api`. Subtitle: Get started for free. |

### Company

| Control | Opens |
|---|---|
| About | `/about`. Subtitle: What we do. |
| Careers | `/careers`. Subtitle: Join the team. |
| Newsroom | `/newsroom`. Subtitle: News and knowledge base. |
| Mission | `/mission`. Subtitle: Why we do it. |

## Header, phone (390)

The bar is the logo and a 40 by 40 `[data-framer-name="Button Icon"]` at the right (`cursor: pointer`, no text). Clicking it keeps the URL on `/` and opens `[data-framer-name="Mobile - Closed"]` (the open drawer, despite the name). Photographed in [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).

The drawer lists Sign in (`https://account.chargetrip.com`, wall), then the same groups as desktop: No-code, API, Integration Partners, CPO, eMSP, Leasing, Rental, OEM, Fleet Management, Consulting, Retailers, Playground, Documentation, No-Code Pricing, API Pricing, About, Careers, plus the rest of the Company group below the fold. Contact sales was not in the drawer. Close is the same icon once open.

## Homepage body

URL stays `/` unless noted. Prior capture: [home-light-default.png](screenshots/home-light-default.png).

| Control | Result |
|---|---|
| Book a demo (hero) | `https://meetings-eu1.hubspot.com/admoni/home-page-hero` with `utm_source=demo-request`. Booking. Not submitted. |
| Plan a route | `https://go.chargetrip.com`. Public planner. |
| Explore EV routing | `/products/routing` |
| CPO, Rental, eMSP, Leasing | In-page industry tabs. Same paths as the Use cases menu. |
| Retailers, OEMs, Consulting | Same use-case paths, further down the page. |
| Watch on-demand | Button with no href. Not a navigation. Not used. |
| Book a demo (footer band) | `https://meetings-eu1.hubspot.com/admoni/footer`. Booking. Not submitted. |
| Start building | `https://developers.chargetrip.com` |

The route-planner mock (vehicle settings, Send to phone, Refresh, Share, Route breakdown) is a demonstration on the marketing page. Send to phone, Refresh, and Share were not used. No homepage search. No locale switch. No theme switch.

## Footer

| Control | Opens |
|---|---|
| No-code | `/no-code` |
| API | `/api` |
| eMSP & CPO | `/emsp` |
| Commercial fleets | `/fleets` |
| Rental & Leasing | `/renting-and-leasing` |
| Retailers | `/retailers` |
| OEMs | `/oems` |
| Documentation | `https://developers.chargetrip.com/` |
| Setup guides | `https://developers.chargetrip.com/basics/api-basics/getting-started` |
| Sign up | `https://account.chargetrip.io/sign-in`. Wall. Not submitted. |
| Stable | `https://status.chargetrip.com/` |
| About | `/about` |
| Mission | `/mission` |
| Newsroom | `/newsroom` |
| Contact | `/contact` |
| LinkedIn | `https://www.linkedin.com/company/chargetrip/` |
| Join us | `/careers#open-positions` |
| Sign up (newsletter) | Button with no href. Not submitted. |
| B Corp mark | `https://www.bcorporation.net/en-us/find-a-b-corp/company/chargetrip/` |
| Terms | `/legal/terms-and-conditions` |
| Privacy | `/legal/privacy-policy` |
| Cookies | `/legal/cookies` |
| Security | `/legal/security` |
| Manage Cookies | Opens the Cookie Settings card. Not answered. |

## Confirmed public pages

Visited signed out in the prior capture (2026-11-12) and still linked from this homepage: `/`, `/products/routing`, `/api`, `/no-code`, `/cpo`, `/pricing/api`, `/pricing/nocode`, `/about`, `/newsroom`, `/contact`, `/contact/sales`, `/legal/terms-and-conditions`, `https://developers.chargetrip.com/`.

This pass also photographs `/go` via `https://go.chargetrip.com` when it stays public, and stops at the account and playground walls.

## Walls

| Control | Stops at |
|---|---|
| Sign in | `https://account.chargetrip.com`, which redirects to `https://account.chargetrip.io/`. Empty email field, Continue, Create account. Not submitted. |
| Sign up | `https://account.chargetrip.io/sign-in` (footer) and the sign-up link named on the playground dialog. Not opened past the wall. |
| Playground | `https://playground.chargetrip.com` |
| Book a demo, Schedule a call | HubSpot meetings. Not submitted. |

No email, password, phone, or code was typed. No identity provider was clicked. No form was submitted.
