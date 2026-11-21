# Reclaim AI public site tree

Mapped from https://reclaim.ai/ on 2026-11-21, signed out, before screenshots. The marketing site is Webflow (`data-wf-site="67859049c02d67b2cfcceebf"`, last published 2026-10-28). The sitemap lists 547 URLs. This file records which control opens which page, menu, dialog, or wall. It is not a capture of every blog post or glossary entry.

Cookie banner (Osano) mounts on every marketing page. It was hidden for screenshots. Its buttons (Accept All, Reject Non-Essential, Save, Customize Cookies) were never clicked, because a consent click can POST.

## Header (desktop)

| Control | Opens |
|---|---|
| Logo | https://reclaim.ai/ |
| Product (hover `.nav_link_hover_back.product`) | Product menu. The Webflow toggle `.header-link.w-dropdown-toggle` is 0x0; the visible hover target is `.nav_link_hover_back`. |
| Solutions (hover `.nav_link_hover_back.teams`) | Solutions menu plus an Integrations column. The visible label is Solutions. An older Teams label is hidden in the DOM. |
| Resources (hover `.nav_link_hover_back.resources`) | Resources menu plus a Popular blog posts column. |
| Enterprise (has a caret) | https://reclaim.ai/enterprise. The caret was not opened as its own panel. |
| Pricing | https://reclaim.ai/pricing |
| Log In | https://app.reclaim.ai/login (login wall; stop) |
| Book a Demo | https://reclaim.ai/contact |
| Get Started | https://app.reclaim.ai/signup (signup wall; stop) |

## Product menu

Hover, not a click that navigates. Links:

| Label | URL |
|---|---|
| AI Focus Time | /features/focus-time |
| AI Habits | /features/habits |
| AI Tasks | /features/tasks |
| Team OOO Calendar | /features/out-of-office-calendar |
| AI Scheduling Links | /features/scheduling-links |
| AI Smart Meetings | /features/smart-meetings |
| AI Calendar Sync | /features/calendar-sync |
| AI Assistant | /features/ai-assistant |
| AI Buffer Time | /features/buffer-time |
| AI Time Tracking | /features/time-tracking |
| AI Planner | /features/planner |
| Workforce Analytics | /features/workforce-analytics |

The open panel also has Contact Sales (`/contact`) and Watch a demo (`/webinars-demos`). See [home-light-product-menu](screenshots/home-light-product-menu.png).

## Solutions menu (DOM class still says teams)

| Label | URL |
|---|---|
| Product | /teams/product |
| Sales | /teams/sales |
| Engineering | /teams/engineering |
| HR | /teams/hr |
| Marketing | /teams/marketing |
| Finance | /teams/finance |
| Executive Assistants | /teams/executive-assistants |

A second column, Integrations, lists Slack, Asana, ClickUp, Todoist, Jira, Linear, Google Tasks, Zoom, and Raycast, each linking `/integrations/<name>`. Contact Sales and Watch a demo sit under the team column. See [home-light-solutions-menu](screenshots/home-light-solutions-menu.png).

## Resources menu

| Label | URL |
|---|---|
| Blog | /blog |
| Help Docs | https://help.reclaim.ai/ (redirects to /en/) |
| Webinars & Demos | /webinars-demos |
| Customers | /customers |
| Glossary | /glossary |
| Pomodoro Timer | /pomodoro-timer |

A second column lists popular blog posts. Affiliate Program is in the footer, not this menu. See [home-light-resources-menu](screenshots/home-light-resources-menu.png).

## Phone header (390)

The hamburger (`.nav_open`, not the 0x0 `.w-nav-button`) opens the mobile nav. Inside it, Product, Solutions, and Resources are disclosure rows. Enterprise, Pricing, Log In, Book a Demo, and Get Started stay the same destinations as desktop. Log In and Get Started still stop at the app wall. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Home interactions

| Control | What it does |
|---|---|
| Audience tab menus (`.audience_content_menu.w-tab-menu`) | Switches the feature panel in three groups: focus/habits/tasks, assistant/links/meetings, sync/buffer. Local only. |
| FAQ questions (`button` in `.faq-item`) | Opens that answer. Local only. The open state was not captured: the shot named faq is the Resources menu, and that file was removed. |
| Get started free, Book a demo | Signup wall, or /contact |
| Feature cards | The feature URLs above |
| Team cards | The team URLs above |
| Integrations row | /integrations and /integrations/<name> |
| Customer quotes | /customers and /customers/<name> |
| Google Calendar add-on | External: workspace.google.com marketplace. Not followed. |
| 20% off / connect calendar | /connect-calendar, which immediately redirects to accounts.google.com. Stop. Do not type an email. |

## Pricing

| Control | What it does |
|---|---|
| Yearly - SAVE 20% / Monthly | Local billing toggle. Yearly showed $10 / $15 / $22. Monthly showed $12 / $18. |
| See all features | Expands the comparison. Show fewer features collapses it. |
| Info marks (`i` dropdowns) | Plan-feature notes. Local. |
| Get Started on a plan | Signup wall. Stop. |
| Apply now / Learn more on discounts | /pricing/education-discount, nonprofit, startup, switching-providers. |
| FAQ buttons | Open that answer. Local. |
| Contact sales | /contact |

## Contact, search, tools

| Page | Controls | Stop rule |
|---|---|---|
| /contact | Book-a-demo page. The HubSpot scheduler is an iframe. No form was filled or submitted. | Do not book. |
| /search | Blog search field (`input[name=query]`). Empty state is public. | Do not submit a query that would be personal. A published-word search is a local filter only if used. |
| /blog | Same search, plus a newsletter email field. | Do not fill or submit the email field. |
| /pomodoro-timer | Start, Reset, Pomodoro / Short Break / Long Break tabs, settings, task field, sound select. | Local timer. Do not type a personal task. |
| /meeting-cost-calculator | Salary, attendees, minutes, a select. | Local calculator. Do not type a personal salary. Public placeholders only. |
| /dsar, /o365-waitlist, /product-survey-additional-questions | Form pages. | Do not fill profile, survey, or waitlist fields. |

## App and auth walls (stop)

| URL | What is on screen | Action |
|---|---|---|
| https://app.reclaim.ai/login | "Log in to Reclaim.ai". Continue with Google, Microsoft, Dropbox, SSO. Sign up link. | Recorded. Not clicked. |
| https://app.reclaim.ai/signup | "Welcome to Reclaim". Continue with Google, Outlook, Dropbox. | Recorded. Not clicked. |
| https://reclaim.ai/connect-calendar | Redirects to Google sign-in ("Sign in to continue to Reclaim.ai"). | Stopped. Not typed. |

Signed-in calendar, planner, settings, onboarding, and billing checkout are behind those walls.

## Other public hosts linked from the footer

| Host | What it is | Capture |
|---|---|---|
| help.reclaim.ai | Help center. Search field and collection links. | Home only. Article tree is a docs site, not the product UI. |
| status.reclaim.ai | Status page | Linked. Not the product UI. |
| trust.reclaim.ai | Trust center | Linked. Not the product UI. |
| updates.reclaim.ai | Changelog | Linked. Not the product UI. |
| Social (YouTube, LinkedIn, X, Instagram, Facebook) | External | Not followed. |

## Sitemap sections not walked page by page

| Prefix | Count | Why |
|---|---|---|
| /blog | 288 | Same blog template. Index plus one post. |
| /glossary | 119 | Same glossary template. Index only. |
| /ai-agent-library | 47 | Index plus one agent page. |
| /compare | 19 | Index plus one comparison. |
| /integrations | 15 | Index plus one integration. |
| /customers | 7 | Index plus one story. |
| /features | 13 | Two feature pages, plus the menu targets recorded above. |
| /teams | 7 | One team page. |
| /initiatives | 5 | One initiative page. |
| /pricing | 5 | Pricing plus one discount page. |
| Legal | terms, privacy, cookie-policy, business-terms, dpa, subprocessors, security, responsible-disclosure, careers, about | One legal page (privacy) and about. Same marketing chrome. |

## Dark theme

No theme toggle was found on the marketing site or on the login wall. The package records light only.
