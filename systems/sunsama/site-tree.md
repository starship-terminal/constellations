# Sunsama public site tree

Mapped from https://www.sunsama.com/ on 2026-11-21 in headless Chromium before any package screenshot. The homepage redirects to https://www.sunsama.com/ (200). Desktop nav is a flat Webflow bar. There is no hover flyout. Phone width (390) hides that bar and shows a menu button.

Consent (Termly) sits on every marketing page. Preferences opens a dialog. Accept posts consent. Neither is clicked. The banner is hidden in later captures so it does not cover the page.

## Primary nav (desktop, visible)

| Control | Opens |
|---|---|
| Logo ("home") | https://www.sunsama.com/ |
| Features | Same page, anchor `#features`. Does not open a menu. |
| Integrations | https://www.sunsama.com/integrations/asana (first integration page, not an index) |
| Pricing | https://www.sunsama.com/pricing |
| Love | https://www.sunsama.com/love |
| About | https://www.sunsama.com/about |
| Blog | https://www.sunsama.com/blog |
| Login | https://app.sunsama.com/login (login wall; branch stops) |
| Start for Free | https://www.sunsama.com/start/signup (signup wall; branch stops) |

## Phone menu

Control: `.menu-button-2` (`aria-label="menu"`, `aria-controls="w-nav-overlay-0"`). Hidden at 1440. At 390, click sets `aria-expanded="true"` and shows `.w-nav-overlay` with the same links: Features, Integrations, Pricing, Love, About, Blog, Login. Start for Free stays outside the overlay as the header CTA.

## Homepage interactions

| Control | Opens |
|---|---|
| "Works with Claude, ChatGPT and more" (`.ss-pill`, `aria-haspopup="dialog"`) | In-page `.ss-panel` dialog: assistant tabs Claude, ChatGPT, Cursor, Claude Code, Other. Close is `.ss-panel_close`. Copy buttons copy setup text. Connect links leave the site (claude.ai, chatgpt.com). "Start free trial" goes to `/start/signup`. |
| Assistant tabs inside the panel | Swap the step pane (`#ss-steps-claude`, `#ss-steps-chatgpt`, `#ss-steps-cursor`, `#ss-steps-claude-code`, `#ss-steps-other`). |
| Testimonial slider arrows (`.sliderarrow`) | Next or previous quote in `#w-slider-mask-0`. No new page. |
| "See how daily planning works" | https://www.sunsama.com/features/daily-planning |
| Integration logos in the body | Each product's `/integrations/<slug>` page, or `#` when the logo is not a page. |
| Newsletter form (`#wf-form-Newsletter-Form`, email + submit) | Would submit a subscription. Not filled. Not submitted. |
| Cookie Policy / Preferences | Termly dialog. Not opened. |
| Accept | Consent POST. Not clicked. |

## Login and signup walls (stop)

https://app.sunsama.com/login (200) shows email, password, "Log in with Google", "Log in with Outlook", "Log in with SSO", and "Log in with email". Password was not submitted. Google, Outlook, and SSO were not clicked. No email was typed.

https://www.sunsama.com/start/signup shows "Sign up", an email field, a Turnstile token, and "Already have an account? Log in" to the login URL. No email was typed. The form was not submitted. Google and Apple are not on this page.

`/start/signup?assistant=claude` and `/start/from-desktop` are the same signup wall. Not captured past the wall.

## Pages linked from the homepage or footer

| Control or link | Opens |
|---|---|
| iOS/iPadOS, Android | /mobile |
| macOS, Windows, Linux | /desktop |
| Each integration name | /integrations/<slug> (asana, clickup, github, gmail, google-calendar, google-tasks, jira, linear, microsoft-planner, microsoft-teams, microsoft-to-do, monday-com, notion, outlook, outlook-calendar, slack, todoist, toggl, trello, zapier) |
| Designers, Engineers, Product Managers, Marketers, Operations Leaders | /team/design, /team/engineering, /team/product, /team/marketing, /team/operations |
| Execs & Founders | /role/executives |
| Compare | /compare |
| Terms & Conditions | /terms |
| Privacy | /privacy |
| User Manual & Guides, Support | https://help.sunsama.com/ (external docs) |
| Vulnerability Disclosure Program | https://help.sunsama.com/docs/security/vulnerability-disclosure-program |
| Status | https://sunsamastatus.com/ |
| Social icons | x.com, facebook.com, instagram.com, linkedin.com (external) |
| Support mailto | mailto (not opened; the address is not copied into this package) |
| Join community | Slack invite (external; the invite URL is not copied into this package) |
| Named Best Scheduling Tool | nytimes.com Wirecutter (external) |

## Page-level interactions

| Page | Control | Opens |
|---|---|---|
| /pricing | Splide arrows and "Go to slide N" | Testimonial slides. No billing toggle. Prices are static copy ($17 billed yearly, $22 billed monthly). |
| /pricing | FAQ titles (`.about-philosophy_title`) | Already expanded text. Not a disclosure control. |
| /love | Two Splide carousels plus a Webflow social slider | Next or previous quote. No new page. |
| /about | Slider arrows (`.about_left-arrow`, `.about_right-arrow`) | Next or previous slide. |
| /compare | Eight tabs (`.compare_tab-link`), logos Akiflow, Motion, Reclaim, OmniFocus, Todoist, Trello, Asana, ClickUp | Swap the comparison pane. No new URL. |
| /features/daily-planning | "Plan my day" (`.ap-demo_go`) | In-page demo panel (`.ap-demo`). Stays on the page. Not a form submit. |
| /integrations/asana | "See how it works" (`.w-lightbox`) | Webflow lightbox. Same pattern on other integration pages. |
| /blog | Category links | /blog-categories/reports, articles, user-cases, integrations, features, user-manual-and-guides |
| /blog | Post cards | /blog/<slug> |
| /blog | Subscribe form | Email + Turnstile. Not filled. Not submitted. |
| /pro-tips | Category combobox (`.pt-select__button`, `aria-controls="pro-tips-category-list"`) | Listbox: All tips, Daily planning, Focus mode, Calendar & timeboxing, Objectives & planning, Recurring tasks, Multi-day tasks, Integrations, Shortcuts & capture, Navigation, Habits, AI. Selecting a row filters the public list. |
| /pro-tips | Search field (`type=search`, name `q`) | Would filter. Not typed. |
| /pro-tips | Tip cards | /pro-tips/<slug> |

## Sitemap pages not in the primary nav

Reached from the sitemap (https://www.sunsama.com/sitemap-0.xml, 671 URLs), not from a homepage control:

- Feature essays: /features/ai, /features/daily-highlights, /features/daily-planning-and-shutdown, /features/focus-mode, /features/guided-planning-and-reviews, /features/timeboxing
- Role and team-size: /role/individual-contributors, /role/managers, /team-size/individuals, /team-size/startups
- Alternatives: /alternative-to/asana, clickup, motion, ticktick, todoist
- Landing variants: /for-adhd, /be-productive, /daily-planning, /task-manager, /task-management-system, /task-manager-for-professionals, /workload-manager, /productivity-operating-system, /expense-sunsama, /share, /black-friday, /wirecutters-best-scheduling-tool-2025, /wirecutters-top-pick-for-ai-scheduling
- Blog index categories and authors: /blog-categories/*, /blog-authors/*
- Affiliate landers: /a/<slug> (260 URLs). Same marketing template. Not walked one by one.
- Conversion pixels: /conversion/plan-day-completed, /conversion/start-trial, /conversion/upgrade. Not product UI.
- /success/newsletter is a post-submit page. The form was not submitted, so this branch was not opened.

## Not in this capture

The signed-in app (tasks, calendar, focus mode, settings, onboarding) sits behind https://app.sunsama.com/login. The public site declares `--ss-*` app colour names, but they resolve empty on marketing pages. Dark theme is not a control on the public site (`color-scheme: normal`).
