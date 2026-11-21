# Grow with Google site tree

Mapped 2026-11-21 from a headless Chromium visit, signed out, no cookies accepted. `https://grow.google/` returns 200 and redirects to `https://grow.google/intl/ALL_sg/` (Singapore, title "Grow Your Skills When Preparing for a New Job - Grow with Google APAC"). The English Singapore home is `https://grow.google/intl/en_sg/` and renders the same page. `https://grow.google/intl/en/` is a 404: "Error: Not Found. The requested URL /intl/en/ was not found on this server."

There is no account sign-in on either shell. No password field, OAuth button, or robot check appeared. US marketing pages post newsletter and partner forms to `services.google.com`; those forms were not filled.

Two shells share the domain:

| Shell | Where | What opens it |
|---|---|---|
| APAC Glue (`glue-body`, class `page`) | `/intl/en_sg/…` and `/intl/ALL_sg/…` | Geo redirect from `/`, and the APAC header nav |
| US Brightspot marketing | `/certificates`, `/ai`, `/stories`, `/sitemap`, and the other paths below | Footer and in-page links that leave `/intl/`, plus the US header mega-nav |

## APAC home controls

Page: `https://grow.google/intl/en_sg/`. Header landmark, then main, then footer.

| Control | Kind | Opens |
|---|---|---|
| Jump to Content | link `#page-content` | Same page, main |
| Google wordmark | link `/` | Redirects back to `/intl/ALL_sg/` |
| Home | nav link | `/intl/en_sg/` |
| Majulah AI | nav link | `/intl/en_sg/majulah-ai/` |
| Skills Ignition SG | nav link | `/intl/en_sg/skillsignitionsg/` |
| Stories | nav link | `/intl/en_sg/stories/` |
| Use Tools | nav link | `/intl/en_sg/use-tools/` |
| Learn Skills | nav link | `/intl/en_sg/learn-skills/` |
| Gemini Report | nav link | `/intl/en_sg/gemini-report/` |
| Redeem Google AI Pro | nav link | `/intl/en_sg/redeem-google-ai-pro/` |
| About Grow with Google | button | In-page section (no navigation) |
| Go to the previous page / next page | carousel buttons | Featured cards on the same page |
| Play/Pause | button | Featured carousel motion |
| Start you checkup now | link | Leaves the site: `https://myaccount.google.com/security-checkup` (not followed) |
| Learn more (traineeship) | link | `/intl/en_sg/skillsignitionsg/` |
| Learn more (Majulah AI) | link | `/intl/en_sg/majulah-ai/` |
| Learn more (stories anchor) | link | `/intl/en_sg/stories/#new-skills-new-careers` |
| Learn more (AI Professional) | link | `/intl/en_sg/ai-professional/` |
| View all tools | link | `/intl/en_sg/use-tools/` |
| View all courses | link | `/intl/en_sg/learn-skills/` |
| Cookies management controls | button | Cookie preference dialog |
| Privacy / Terms | footer links | `policies.google.com` (not followed) |

Stories page adds three tab buttons ("Selected tab 1 of 3", "2 of 3", "3 of 3") that swap the story panel on the same URL.

## APAC pages reached

All returned 200. Header nav is the same on each.

| Path | Title |
|---|---|
| `/intl/ALL_sg/` and `/intl/en_sg/` | Home |
| `/intl/en_sg/majulah-ai/` | Singapore \| Majulah AI |
| `/intl/en_sg/skillsignitionsg/` | Skills Ignition SG |
| `/intl/en_sg/stories/` | Empowering Singaporeans today, for tomorrow |
| `/intl/en_sg/aira-challenge/` | AI Ready ASEAN Youth Challenge |
| `/intl/en_sg/use-tools/` | Digital tools to reach your goals |
| `/intl/en_sg/learn-skills/` | Get the required skills for the changing landscape |
| `/intl/en_sg/gemini-report/` | The Gemini Report \| Southeast Asia 2026 \| Singapore |
| `/intl/en_sg/redeem-google-ai-pro/` | Redeem Google AI Pro |
| `/intl/en_sg/ai-professional/` | Singapore \| Google AI Professional Certificate |
| `/intl/en_sg/healthcare-professionals/` | Google AI Healthcare Training |
| `/intl/en_sg/ai-essentials/` | Singapore \| Google AI Essentials |
| `/intl/en_sg/ai-challenge/` | Skills Ignition AI Challenge 2026 |

`/intl/en_sg/learn-skills/` and `/intl/en_sg/skillsignitionsg/` also link out to the US certificate paths (`/certificates/data-analytics/` and siblings). Those links leave the APAC shell.

## US shell controls

Page: `https://grow.google/certificates`. Header buttons named Career Certificates, AI Training, For Partners, and Stories & Resources. Each has a desktop trigger with `aria-haspopup=true` that opens a mega-menu, plus a duplicate link of the same name. Mobile uses the same labels inside the collapsed header.

| Control | Opens |
|---|---|
| Career Certificates (popup) | Menu of `/certificates` and each `/certificates/<slug>/` |
| AI Training (popup) | Menu of `/ai`, `/ai-essentials`, `/ai-professional`, `/ai-for-educators`, `/ai-for-small-businesses`, `/job-search-with-ai` |
| For Partners (popup) | Menu of `/employers`, `/certificates-academic-institutions`, `/government`, `/partners`, `/coaches` |
| Stories & Resources (popup) | Menu of `/stories`, `/grow-your-career`, `/news-insights`, `/our-mission`, `/expanding-opportunity` |
| Sitemap link | `/sitemap` (51 same-site paths) |

## US pages reached

All returned 200. The certificate family shares one template; one product page stands for the rest.

| Path | Role |
|---|---|
| `/certificates` | Certificate index |
| `/certificates/data-analytics/` | One certificate product page (siblings: cybersecurity, digital-marketing-ecommerce, it-support, project-management, ux-design, advanced-data-analytics, business-intelligence, it-automation-python) |
| `/ai` | AI training index |
| `/ai-essentials`, `/ai-professional`, `/ai-for-educators`, `/ai-for-small-businesses`, `/job-search-with-ai`, `/agile-essentials`, `/people-management-essentials` | Course landings, same shell |
| `/students`, `/healthcare-professionals`, `/career-dreamer` | Audience landings |
| `/employers`, `/partners`, `/coaches`, `/government`, `/certificates-academic-institutions` | Partner landings |
| `/stories` | Story index |
| `/grow-your-career` | Article index |
| `/grow-your-career/articles/what-is-vibe-coding/` | One article (sitemap lists 14 more of the same template) |
| `/news-insights`, `/our-mission`, `/expanding-opportunity`, `/expanding-opportunity/military-community/` | Editorial landings |
| `/applied-digital-skills` | Programme landing |
| `/sitemap` | Link index |
| `/government-form` | Salesforce lead form. Not filled (captcha field present, empty). |
| `/partnerapply` | Partner signup form. Not filled (captcha field present, empty). |

## Not followed

- `myaccount.google.com` security checkup (account surface).
- `policies.google.com` privacy and terms.
- `accounts.google.com` did not appear.
- Coursera, YouTube and other off-site course CTAs were recorded as external and not opened.
- Article siblings beyond one sample, and certificate siblings beyond data-analytics, share the templates above. The sitemap lists them; they were not each screenshotted.
