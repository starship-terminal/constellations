# Intercom public site tree

Mapped on 2026-11-21 from the live homepage at [https://www.intercom.com/](https://www.intercom.com/) before the extra screenshots. Desktop measured 1440×900. Phone is 390×844. The walk records which control opens which page, menu, dialog, or wall. Nothing was typed. No form was submitted. Google, SAML, and every identity provider were not clicked.

The homepage loaded (title "Intercom | A complete system for human and AI customer service", h1 "A complete system for AI and human customer service"). Body class is `theme-light`. `color-scheme` is `normal`. Theme color is `#050505`. There is no public dark theme switch. At 1440 the "Open navigation menu" button is in the DOM at 0×0. The desktop Product, Customers, and Resources buttons are 40px tall and start closed (`aria-expanded=false`).

## Home chrome

| Control | Opens |
|---|---|
| Wordmark | `/` |
| Product (button) | Mega-menu. Stays on `/`. See Product menu. Hover or click sets `aria-expanded=true`. Escape closes it. |
| Customers (button) | Mega-menu. Stays on `/`. See Customers menu. |
| Resources (button) | Mega-menu. Stays on `/`. See Resources menu. |
| Pricing | `/pricing` |
| Log in | Login wall. Opened and stopped. `https://app.intercom.com/admins/sign_in` (title "Intercom Login"). Work email, password, Google, and SAML were not used. |
| Contact sales | `/contact-sales` (first step only; not submitted) |
| View demo | `/view-demos` |
| Start free trial | Signup wall. Not opened. `https://www.intercom.com/signup?solution_id=29` |
| Fin AI Agent | Leaves the marketing host for `https://fin.ai/` |
| Close banner | Dismisses the Fin 4 promo strip. Local UI only. |
| Learn more (banner) | `https://fin.ai/fin4` |
| Hero Start free trial | Same signup wall. Not opened. |
| Hero View demo | `/view-demos` |
| PLAY (Introducing Fin 4) | Dialog on `/`. Playback was not started. |
| Intercom helpdesk (section tab) | In-page panel on `/`. Also links through to `/helpdesk`. |
| Fin AI Agent (section tab) | In-page panel on `/`. Also links to `https://fin.ai/`. |

Phone (390): the nav row collapses to the wordmark, Start free trial, Fin AI Agent, and a button labelled "Open navigation menu". That button opens a sheet. The sheet lists Product, Customers, Resources (each expands in place), Pricing, Log in, Contact sales, View demo, and Start free trial. Log in and Start free trial are the same walls. Log in was photographed on desktop only. Start free trial was not opened.

## Product menu

Opened on the homepage. The panel stays on `/`.

| Item | Opens |
|---|---|
| Intercom helpdesk | `/helpdesk` |
| Fin AI Agent | `https://fin.ai/` |
| Channels | `/helpdesk/omnichannel` |
| Integrations | `/integrations` |
| Safety & security | `/security` |
| Inbox | `/helpdesk/inbox` |
| Copilot | `/helpdesk/copilot` |
| Tickets | `/helpdesk/tickets` |
| Help Center | `/helpdesk/help-center` |
| Reporting | `/helpdesk/reporting` |
| Outbound | `/helpdesk/outbound` |
| Knowledge Hub | `/helpdesk/knowledge-hub` |

## Customers menu

Stays on `/` until a row is followed. Labels read from the homepage links.

| Item | Opens |
|---|---|
| Meet our customers | `/customers` |
| Technology | `/solutions/technology` |
| Ecommerce | `/solutions/ecommerce` |
| Fintech | `/solutions/fintech` |
| Gaming | `/solutions/gaming` |
| Startups | `/early-stage` |
| Small business | `/small-business` |
| Enterprise | `/enterprise` |

## Resources menu

| Item | Opens |
|---|---|
| Why choose Intercom? | `/why-choose-intercom` |
| Early Stage | `/early-stage` |
| Intercom blog | `/blog` |
| Webinars & events | `https://events.intercom.com/` |
| Academy | `https://academy.fin.ai/` |
| 2026 Transformation Report | `https://fin.ai/customer-transformation-report` |
| AI Agent Blueprint | `https://fin.ai/blueprint` |
| Help center | `/help/en/` |
| Product updates | `/changes/en` |
| Community | `https://community.intercom.com/` |
| About | `https://fin.ai/about` |
| Careers | `https://fin.ai/careers` |
| English | `/en` |
| Français | `/fr-fr` |
| Español (Latinoamérica) | `/es-la` |
| Deutsch | `/de-de` |
| Português (Brasil) | `/pt-br` |

## Login wall

Opened from Log in. Stopped on the form. Nothing typed. Google not clicked. SAML not clicked. Continue not pressed. Captcha not solved.

| Control | What it is |
|---|---|
| Join Intercom | `https://www.intercom.com/pricing`. Not followed this pass. |
| Your account region | Opens a menu: United States, Europe, Australia. No region was chosen. |
| Sign in with Google | Identity provider. Not clicked. |
| Your work email | Empty field. Placeholder only. |
| Your password | Empty field. |
| Keep me signed in | Checkbox. Not ticked. |
| Forgot your password? | `https://app.intercom.com/admins/password/new`. Not opened. |
| Continue | Submit. Not pressed. A reCAPTCHA sits above it. |
| Sign in with SAML SSO | `https://app.intercom.com/a/saml`. Not opened. |
| Your Privacy Choices | Consent control. Not accepted or rejected. |

## Product menu

Hover (desktop) or the Product button inside the phone sheet.

| Item | Opens |
|---|---|
| Intercom helpdesk | `/helpdesk` |
| Fin AI Agent | `https://fin.ai/` |
| Inbox | `/helpdesk/inbox` |
| Copilot | `/helpdesk/copilot` |
| Tickets | `/helpdesk/tickets` |
| Help Center | `/helpdesk/help-center` |
| Reporting | `/helpdesk/reporting` |
| Outbound | `/helpdesk/outbound` |
| Knowledge Hub | `/helpdesk/knowledge-hub` |
| Channels | `/helpdesk/omnichannel` |
| Integrations | `/integrations` |
| Safety & security | `/security` |

## Customers menu

| Item | Opens |
|---|---|
| Meet our customers | `/customers` |
| Technology | `/solutions/technology` |
| Ecommerce | `/solutions/ecommerce` |
| Fintech | `/solutions/fintech` |
| Gaming | `/solutions/gaming` |
| Startups | `/early-stage` |
| Small business | `/small-business` |
| Enterprise | `/enterprise` |

Customer story cards on `/customers` leave the host for `https://fin.ai/customers/<slug>` (Anthropic, Lightspeed, Gamma, and others). Those story pages loaded as public fin.ai pages. They are not the Intercom marketing shell.

## Resources menu

| Item | Opens |
|---|---|
| Why choose Intercom? | `/why-choose-intercom` |
| Early Stage | `/early-stage` |
| Intercom blog | `/blog` |
| Webinars & events | `https://events.intercom.com/` which redirects to `https://webinars.fin.ai/` |
| Academy | `https://academy.fin.ai/` |
| 2026 Transformation Report | `https://fin.ai/customer-transformation-report` |
| AI Agent Blueprint | `https://fin.ai/blueprint` |
| Help center | `/help/en/` |
| Product updates | `/changes/en` |
| Community | `https://community.intercom.com/` |
| About | `/about` redirects to `https://fin.ai/about` |
| Careers | `https://fin.ai/careers` |

## Footer

The footer is an accordion of link groups (Helpdesk features, Fin features, Pricing, Solutions, Learn, Evaluate, Support, Company, Programs, Intercom in action, Language). Groups that the nav already lists are not repeated here.

| Group | Extra destinations |
|---|---|
| Helpdesk features | `/live-chat`, `/app-store`, plus the Product menu routes |
| Fin features | `https://fin.ai/`, `/capabilities`, `/ai-engine` |
| Pricing | `/pricing`, `https://fin.ai/pricing` |
| Solutions | The Customers menu industry routes |
| Learn | `https://events.intercom.com/`, `/blog`, `https://academy.fin.ai`, YouTube, `https://fin.ai/blueprint`, `/learning-center`, `https://fin.ai/customer-transformation-report` |
| Evaluate | `/why-choose-intercom`, `https://trust.intercom.com/`, `https://fin.ai/roi-calculator`, `/customers` |
| Support | `/changes/en`, `/help/en/`, `https://developers.intercom.com/`, `https://community.intercom.com/`, `https://www.finstatus.com/` |
| Company | `/about` (redirects to fin.ai/about), `https://fin.ai/careers`, a press mailto (not opened, not written here) |
| Programs | `/solution-partner-program`, `/technology-partner-program`, `/early-stage` |
| Intercom in action | `/view-demos`, signup wall, `/contact-sales`, login wall |
| Language | `/en`, `/fr-fr`, `/es-la`, `/de-de`, `/pt-br` (locale routes; English is the captured locale) |
| Legal row | `/legal/terms-and-policies`, `/legal/privacy`, `https://trust.intercom.com/`. `/legal/terms` is a 404. |

## Pages that loaded

Public, signed out, HTTP 200 unless noted. Help articles and collections under `/help/en/` are a deep tree (the first crawl stopped at 36 pages, almost all of them help). One article and one collection stand in for that tree. The rest are the same help-center shell.

Marketing and product pages:

- `/` home
- `/pricing`, `/pricing/calculator`
- `/helpdesk`, `/helpdesk/inbox`, `/helpdesk/copilot`, `/helpdesk/tickets`, `/helpdesk/outbound`, `/helpdesk/omnichannel`, `/helpdesk/help-center`, `/helpdesk/reporting`, `/helpdesk/knowledge-hub`
- `/customers`
- `/integrations`, `/security`, `/app-store`, `/live-chat`
- `/view-demos`, `/contact-sales` (and `?journey=copilot`, same first step)
- `/why-choose-intercom`, `/enterprise`, `/early-stage`, `/small-business`
- `/solutions/technology`, `/solutions/ecommerce`, `/solutions/fintech`, `/solutions/gaming`
- `/blog`, `/learning-center`, `/changes/en`, `/help/en/`
- `/legal/privacy`, `/legal/terms-and-policies`
- `/solution-partner-program`, `/technology-partner-program`
- `/drlp/ai-agent` (a public Fin landing on the same host)

Sister hosts that loaded and are not this package's shell: `fin.ai`, `academy.fin.ai`, `webinars.fin.ai`, `community.intercom.com`, `developers.intercom.com`, `trust.intercom.com`.

## Interactions that stay on the page

| Control | Where | What it does |
|---|---|---|
| Product, Customers, Resources | Header, desktop | Opens that mega-menu. Escape closes it. |
| Open navigation menu | Header, phone | Opens the sheet. Product, Customers, Resources expand inside it. |
| Billing toggle | `/pricing` | Switches Billed annually and Billed monthly. Local state. |
| FAQ row | `/pricing` and home accordions | Expands one answer. |
| Company-size select | `/contact-sales` | Opens its listbox. No option was chosen. Next was not pressed. |
| Help search | `/help/en/` | Focuses the field. Nothing was typed or submitted. |
| Fin 4 video button | Home | Opens the video dialog. |
| Close banner | Home | Hides the promo strip. |
| Locale links | Footer | Would switch locale. English only was captured. |
| Cookie or consent banner | Any page | Hidden in the capture kit. Never accepted or rejected. |

## Walls (branch stopped)

| Control | URL | Why stopped |
|---|---|---|
| Log in, Sign in | `https://app.intercom.com/admins/sign_in` | Opened. Empty work email and password, Google, SAML, Continue, and a captcha. Nothing typed. No identity provider clicked. |
| Start free trial, Free trial, Apply now | `https://www.intercom.com/signup` and `/signup/email` (with `solution_id`) | Signup wall. |
| Settings, Billing, Teammates, Manage subscription, Outbound (in help articles) | `https://app.intercom.com/a/apps/_/...` | Signed-in product. Not opened. |

No form was submitted. No password, code, newsletter, or profile field was filled.

## What this pass did not capture

Unread token values stay Not captured. This pass did not re-read CSS.

- The sign-in wall was photographed empty. Google, SAML, Continue, and the captcha were not used. Signup was not opened.
- The contact-sales form past step one, and any submitted form.
- Locale routes other than English.
- Sister hosts (`fin.ai`, academy, webinars, community, developers, trust). They loaded. They are not this shell.
- The Fin 4 video after Play. The dialog opened. The player stayed on its loading frame.
- A dark theme. The public site does not paint one.
- Every help-center article. The tree is the same shell as `/help/en/`.
