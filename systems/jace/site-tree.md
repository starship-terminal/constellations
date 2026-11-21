# Jace AI site tree

Mapped from the homepage at `https://jace.ai/` on 2026-11-21, signed out, in headless Chromium at 1440 x 900. A control that leaves the public site for a login or signup wall was recorded and not followed. Google, Outlook, Microsoft and SSO were not clicked. No form was submitted. No email, name, password or code was typed.

The marketing header is a floating pill: the wordmark, Log In, and Get started. There is no product nav in that bar. Footer links repeat on every marketing page.

## Header

| Control | Opens | Followed |
|---|---|---|
| Wordmark "jace" | `https://jace.ai/` | yes |
| Log In | `https://app.jace.ai/signin` | opened once, then stopped |
| Get started | `https://app.jace.ai/signup` | opened once, then stopped |

## Hero

| Control | Opens | Followed |
|---|---|---|
| Get started for free | `https://app.jace.ai/signup` | recorded, not followed after the wall was seen |
| Gmail | `https://jace.ai/integrations/gmail` | yes |
| Outlook | `https://jace.ai/integrations/outlook` | yes |
| Draft e-mails | `https://app.jace.ai/signup` | recorded, not followed |
| Find an important file | `https://app.jace.ai/signup` | recorded, not followed |
| Organize inbox | `https://app.jace.ai/signup` | recorded, not followed |
| Sort by priority | `https://app.jace.ai/signup` | recorded, not followed |

The four chips look like in-page tabs. A click leaves the homepage for the signup wall. They were not used as a state switch.

The inbox mock under the chips is a public demo, not the signed-in app. Search, rows and labels in that mock are painted content. They are not controls that open a page.

## Further down the homepage

| Control | Opens | Followed |
|---|---|---|
| Get Started for Free (repeated section buttons) | `https://app.jace.ai/signup` | recorded, not followed |
| Go to testimonial 1-4, Previous testimonial, Next testimonial | stays on `/` | in-page carousel, not a route |
| Bill yearly, Bill monthly | stays on `/` | in-page price toggle |
| Try Pro, Start your free trial | `https://app.jace.ai/signup` | recorded, not followed |
| FAQ questions | stays on `/#faq` | accordion, in page |
| Book a personal demo | `https://cal.com/pawel-jace-ai/jace-personal-demo` | external, not followed |
| Get in touch | `https://jace.ai/contact/sales` | yes, form left empty and not submitted |

## Footer

| Control | Opens | Followed |
|---|---|---|
| Jace Home | `/` | yes |
| Pricing | `/pricing` | yes |
| Features | `/#features` | in-page anchor |
| FAQ | `/#faq` | in-page anchor |
| Company | `/about` | yes |
| Affiliate | `https://partners.dub.co/jace` | external, not followed |
| Learn | `/docs` which redirects to `/docs/guides-getting-started` | yes |
| Changelog | `/changelog` | yes |
| Blog | `/blog` | yes |
| Brand | `/brand` | yes |
| Discord, X, TikTok, Instagram, YouTube | external social URLs | not followed |
| LinkedIn | `https://ref.jace.ai/7wmCd1m` | referral redirect, not followed |
| Terms of service | `/terms` | yes |
| Privacy Policy | `/privacy` | yes |
| Impressum | `/impressum` | opened to confirm it is public, then the screenshot was left out: the page prints a street address and a phone number |
| Extension Privacy | `/extension-privacy` redirects to `https://zeta-labs.notion.site/extension-privacy` | external, not photographed |
| Security | `/#security` | in-page anchor |
| Contact us | a mailto link in the footer | not opened |

## Pages the homepage reaches

| Page | What a click there does |
|---|---|
| `/pricing` | Yearly and monthly toggles stay on the page. Plan buttons and "Get in touch" go to signup or `/contact/sales`. FAQ items expand in place. |
| `/about` | Company page. Header Log In and Get started are the same walls. |
| `/brand` | Brand usage notes. No component behaviour guide. |
| `/blog` | Index of public posts. Each card opens `/blog/<slug>`. One index shot stands for the list. Posts were not shot one by one. |
| `/changelog` | Public release notes. |
| `/docs/guides-getting-started` | Docs shell. Sidebar links open other `/docs/*` pages. "Settings → My account", "Settings → Rules" and "Settings → Integrations" point at `https://app.jace.ai/inbox#settings-*`. Those are the login wall. They were not opened. |
| `/docs/mcp-integrations` | Public docs page linked as Integrations from the homepage. |
| `/integrations/gmail`, `/integrations/outlook` | Public integration pages. |
| `/lawyers`, `/consultants` | Public persona pages. |
| `/contact/sales` | Empty sales form: name, work email, three selects, Send a request. Not filled, not submitted. |
| `/terms`, `/privacy` | Legal pages. |
| `/features` | Public 404. The footer Features link is an anchor, not this path. |

## Walls

| URL | What it asks | Stopped |
|---|---|---|
| `https://app.jace.ai/signin` | Continue with Google, Continue with Outlook, Launch the SSO portal. No email field, no password field, no code field. Sign up link returns to signup. | yes |
| `https://app.jace.ai/signup` | Continue, Support, Sign in. No email field. Continue was not clicked. | yes |
| `https://app.jace.ai/enterprise-sso` | Linked from sign-in as Launch the SSO portal. Not opened. | yes |
| `https://app.jace.ai/inbox` | Linked from docs as settings anchors. Not opened. | yes |
