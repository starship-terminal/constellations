# Homerun site tree

Mapped from the public homepage on 2026-11-21, before screenshots, in headless Chromium. `https://homerun.co/` redirects to `https://www.homerun.co/`. The marketing site is Webflow (`data-wf-site=58d684124f3644b01d649b26`). One light theme. No cookie banner mounted on the marketing pages in this run.

Nothing in this tree was submitted. Login, signup, Google, Microsoft, demo booking, newsletter, partner and contact forms were not filled.

## Homepage controls

| Control | Opens |
|---|---|
| Logo "Go to home page" | `/` |
| Organise your hiring | `/ats` |
| Manage your team | `/hr` |
| Pricing | `/pricing` |
| Customers (nav) | `/blog/customer-stories` |
| Partnership | `/partner-program` |
| Resources (dropdown, `aria-haspopup=menu`) | Menu, not a page. Items below. |
| Log in (dropdown) | Menu. Both items are login walls. Stop. |
| Book a demo | External HubSpot meeting page. Not opened as a form. |
| Start free trial | `/trial`, which redirects to the ATS register wall. Stop. |
| Try free for 15 days | `/trial`. Stop. |
| Feature rows ("Get an overview…", six ATS and six HR) | In-page disclosure. Copy only, no navigation. |
| Explore Homerun ATS | `/ats` |
| Explore Homerun HR | `/hr` |
| About our customers | `/customers` |
| View pricing | `/pricing` |
| Capterra / G2 / Instagram / LinkedIn / Twitter | External. Not captured. |
| Open Intercom Messenger | Third-party chat launcher. Not opened. |
| Footer newsletter email | Form on the page. Not filled, not submitted. |

### Resources menu

| Item | Opens |
|---|---|
| Blog | `/blog` |
| Product updates | `/blog/product-updates` |
| Guides | `/guides` |
| Careers | `https://jobs.homerun.co/` (public careers board) |
| Templates | `/templates` |
| Refer a friend | `/referral-program` |
| Integrations | `/integrations` |
| About us | `/about` |
| Help center | `https://help.homerun.co/en/` (public help home) |

### Log in menu (walls)

| Item | Opens | Stop |
|---|---|---|
| Organise your hiring | `https://app.homerun.co/login` | Email, password, Google, Microsoft. Not entered. |
| Manage your team | `https://app.homerun.hr/Account/Logon?ReturnUrl=%2F` | Login wall. Not entered. |

## Public pages captured as types

Shared chrome on marketing pages: the same nav, Resources menu, Log in menu, footer columns, newsletter field, Intercom launcher.

| Page | URL | What else it opens |
|---|---|---|
| Home | `/` | Feature disclosures, nav menus |
| ATS | `/ats` | Feature pages and integration pages |
| HR | `/hr` | Product story, same chrome |
| Pricing | `/pricing` | FAQ disclosures. Trial and demo links are walls or external. |
| Customers index | `/customers` and `/blog/customer-stories` | Story cards, category radios |
| Customers story | `/customer-stories/freshheads-and-homerun` | One published story |
| Partner program | `/partner-program` | Partner form present. Not filled. |
| Blog index | `/blog` | Article cards, pagination |
| Blog article | `/expertise-opinion/ai-and-candidate-fraud-a-recruiters-guide` | One published article |
| Product updates index | `/blog/product-updates` | Category radios |
| Product update | `/product-updates/updates-to-our-public-api` | One update |
| Guides index | `/guides` | Guide cards |
| Guide | `/guides/hiring-process` | One guide |
| Templates | `/templates` | Links to template collections |
| Template collection | `/job-description-templates` | Published templates |
| Referral | `/referral-program` | FAQ disclosures. Form not filled. |
| Integrations | `/integrations` | Category checkboxes (local filter), integration pages |
| Integration | `/integrations/slack` | One integration page |
| Features | `/product/features` | Feature list |
| Feature | `/product/applicant-tracking` | One feature page |
| About | `/about` | FAQ disclosures |
| Contact | `/contact` | Contact form present. Not filled. |
| GDPR | `/gdpr` | Guide page |
| Terms | `/terms-of-service` | Legal |
| Privacy | `/privacy-statement` | Legal |
| Careers board | `https://jobs.homerun.co/` | Public job list. Apply stops at the board. |
| Help home | `https://help.homerun.co/en/` | Search field present. Not submitted. |
| Newsletter page | `/artofwork/newsletter` | Email field. Not filled. |
| Missing page | `/this-page-does-not-exist` | Styled or server error, recorded as seen |

## Walls (URL recorded, branch stopped)

| URL | Asks for |
|---|---|
| `https://app.homerun.co/login` | Email, password, Google, Microsoft. Also links to register and forgot-password. |
| `https://app.homerun.co/register` | Account creation. Reached from "I don't have an account" and from `/trial`. |
| `https://app.homerun.co/forgot-password` | Password recovery. Not opened past the login page's link. |
| `https://app.homerun.hr/Account/Logon` | HR product login. |
| `https://www.homerun.co/trial` | Redirects into the ATS register wall. |
| HubSpot demo (`meetings.hubspot.com/...`) | Booking form. Not opened. |

## Not a separate interaction

Blog pagination, category radios and integration checkboxes stay on the same page. They filter published lists. They are captured where they appear. Article, story, guide and product-update bodies share one article template, so one of each is captured rather than every post.
