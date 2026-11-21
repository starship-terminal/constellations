# Enode public site tree

Walked signed out on 2026-11-21 from [https://enode.com](https://enode.com). That origin stays on [https://enode.com/](https://enode.com/) (HTTP 200, title "Enode: Orchestrating energy for the next grid"). Desktop viewport 1440 by 900. Phone viewport 390 by 844. The page paints light (`data-mode="light"` on `<html>`, `theme-color` `#f4f2f1`). No page-level theme switch. A Cookiebot script (`#cookieBanner-26533468`) is in the document and did not mount a banner. It was not answered.

Opened means the control was used and the result was read. Linked means the href was read and the destination was not followed past a wall. Sign-in and identity-provider walls stop the branch. Nothing was typed. No form was submitted.

## Header, desktop

The logo (`a[href="/"]`, accessible name "Enode, home") links to `/`. Enterprise links to `/enterprise`. Updates links to `/updates`. Company links to `/company`. Sign in links to `https://platform.enode.com`, which redirects to `https://platform.enode.com/login`. Wall. Not submitted. Talk to our team links to `/contact`.

Platform and Resources are hover dialogs. They keep the URL on `/`. Both mount `#nav-dropdown-panel` (`aria-haspopup="dialog"`). Keyboard Enter also opens them. A click on Resources closes the dialog. Photographed in [home-light-menu-platform.png](screenshots/home-light-menu-platform.png) and [home-light-menu-resources.png](screenshots/home-light-menu-resources.png).

### Platform

`aria-label="Platform menu"`. About 1120 by 290. Four product cards, then a 2 by 2 link grid.

| Control | Opens |
|---|---|
| Overview | `/platform/overview`. Subtitle: The energy orchestration platform for the next grid. |
| Asset connectivity | `/platform/assets`. Subtitle: Resilient connectivity for all major residential energy devices. |
| Home energy coordination | `/platform/homes`. Subtitle: An engine that coordinates EV charging and home energy systems. |
| Residential flexibility | `/platform/flexibility`. Subtitle: Thousands of homes, shaped and dispatched as one. |
| Partnerships | `/partnerships`. Subtitle: Bring your hardware to Enode. |
| Customers | `/customers`. Subtitle: What teams have built on Enode. |
| Careers | `/careers`. Badge: 5. Subtitle: Help shape the next grid. |
| Newsroom | `/newsroom`. Subtitle: Launches, milestones, and press. |

### Resources

`aria-label="Resources menu"`. About 512 by 152. The visible panel is the same four links as the Platform grid. The product cards are not in this panel.

| Control | Opens |
|---|---|
| Partnerships | `/partnerships`. Subtitle: Bring your hardware to Enode. |
| Customers | `/customers`. Subtitle: What teams have built on Enode. |
| Careers | `/careers`. Badge: 5. Subtitle: Help shape the next grid. |
| Newsroom | `/newsroom`. Subtitle: Launches, milestones, and press. |

## Header, phone (390)

The bar is the logo, Talk to our team (`/contact`), and a round button labelled "Open menu". Clicking it keeps the URL on `/` and opens a `section[role="dialog"]`. The close control is labelled "Close menu". Photographed in [mobile-home-light-drawer.png](screenshots/mobile-home-light-drawer.png).

The drawer lists a PLATFORM group, then the same top-level links as desktop.

| Control | Opens |
|---|---|
| Overview | `/platform/overview` |
| Asset connectivity | `/platform/assets` |
| Home energy coordination | `/platform/homes` |
| Residential flexibility | `/platform/flexibility` |
| Partnerships | `/partnerships` |
| Customers | `/customers` |
| Careers | `/careers` (badge 5) |
| Newsroom | `/newsroom` |
| Enterprise | `/enterprise` |
| Updates | `/updates` |
| Company | `/company` |
| Sign in | `https://platform.enode.com`. Wall. Not submitted. |

## Homepage body

URL stays `/` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png). The hero reads "Orchestrating energy for the next grid". The live metrics (producing, charging, balancing) are a public demonstration, not the signed-in product.

| Control | Result |
|---|---|
| Talk to our team (hero) | `/contact` |
| Explore our platform | `/platform/overview` |
| Home energy card | `/platform/homes` |
| Flexibility card | `/platform/flexibility` |
| Vattenfall story | `/customers/vattenfall` |
| Talk to our team (footer band) | `/contact` |

No homepage search. No locale switch. No theme switch.

## Footer

| Control | Opens |
|---|---|
| Logo | `/` |
| Platform overview | `/platform/overview` |
| Asset connectivity | `/platform/assets` |
| Home energy coordination | `/platform/homes` |
| Residential flexibility | `/platform/flexibility` |
| For enterprises | `/enterprise` |
| Customers | `/customers` |
| Partnerships | `/partnerships` |
| Updates | `/updates` |
| API reference | `https://platform.enode.com/api`. Redirects to `/login`. Wall. |
| Guides | `https://platform.enode.com/docs`. Redirects to `/login`. Wall. |
| Changelog | `https://platform.enode.com/changelog`. Linked. Same host as the login wall. |
| Dashboard | `https://platform.enode.com`. Wall. |
| Supported brands | `https://platform.enode.com/brands`. Linked. Same host as the login wall. |
| Status | `https://status.enode.com`. Public status page. |
| About us | `/company` |
| Careers | `/careers` |
| Newsroom | `/newsroom` |
| Privacy policy | `/privacy-policy` |

No social links on the homepage. No newsletter form on the homepage.

## Confirmed public pages

Visited signed out: `/`, `/platform/overview`, `/platform/homes`, `/platform/flexibility`, `/platform/assets`, `/enterprise`, `/customers`, `/customers/vattenfall`, `/company`, `/careers`, `/partnerships`, `/newsroom`, `/updates`, `/contact`, `/contact/partnerships`, `/privacy-policy`, and `https://status.enode.com/`.

`/contact` is a form (first name, last name, company, country, email, phone, inquiry radios, a message). `/contact/partnerships` is a second form (company email, device radios). Both were photographed at rest. Neither was filled or submitted.

## Walls

| Control | Stops at |
|---|---|
| Sign in | `https://platform.enode.com/login`. Email address, Sign in, Continue with SAML SSO, Contact us. Not submitted. SAML was not clicked. |
| Continue with SAML SSO | `https://platform.enode.com/sso`. Organization ID and Continue. Not submitted. Not an identity-provider button. |
| API reference, Guides | Redirect to `/login`. Wall. |
| Contact us (on the login card) | `https://enode.com/contact`. Public form. Not submitted. |

The login card offers no Google, Apple, or other identity provider. The dashboard chrome behind the card (Users, Assets, Homes, Settings) is a marketing illustration, not a signed-in app. No email, password, phone, organization id, or code was typed. No identity provider was clicked. No form was submitted.
