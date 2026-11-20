# Workflow public site tree

Mapped from https://www.workflow.design/ on 2026-11-21 in headless Chromium (Playwright), before screenshots. The marketing host redirects `workflow.design` to `www.workflow.design`. The product app lives on `app.workflow.design` and is a login wall. No form was submitted. No password, code, or account field was filled.

Sitemap: https://www.workflow.design/sitemap.xml (85 URLs, fetched the same day). Help articles are linked from `/help` and are not in that sitemap.

## Shell

Desktop header (1440): logo (`/`), Features (`/features`), About (`/about`), Pricing (`/pricing`), Log in (`https://app.workflow.design/`), Try now (`https://app.workflow.design/users/sign-up`). Case studies is in the markup with class `hidden-ui-elements` (`display: none`, href `#`). A second nav list (`.nav--items-mobile`) is `display: none` at 1440 and holds Careers, FAQs, Help center, Contact, Feature requests, Policies, LinkedIn, X/Twitter, and another Log in.

Phone header (390): logo, Toggle navigation (`.nav--menu`, opens `.nav--items-mobile`), and Try now. Sign in (`.nav--signin-mobilemenu`) is `display: none` even inside the open drawer.

Announcement nodes exist in the header but are not shown as a bar: `.downtime-banner` is `display: none`; the referral and affiliate banners contain the literal placeholder `[Name]` and point at sign-up. They were not opened.

Skip to content sits off-screen (`y: -884`) until keyboard focus.

Footer columns (same on every marketing page that uses this shell):

| Column | Control | Opens |
|---|---|---|
| Brand | logo | `/` |
| Company | About | `/about` |
| Company | Careers | `/backups-templates/careers` (404, styled page-not-found) |
| Company | Pricing | `/pricing` |
| Company | Features | `/features` |
| Company | LinkedIn | `https://www.linkedin.com/company/workflow-design` (left the site) |
| Company | X/Twitter | `https://x.com/workflowdesign_` (left the site) |
| Compare | Workflow vs MarkUp | `/compare/workflow-vs-markup` |
| Compare | Workflow vs ruttl | `/compare/workflow-vs-ruttl` |
| Compare | Workflow vs BugHerd | `/compare/workflow-vs-bugherd` |
| Compare | Workflow vs Pastel | `/compare/workflow-vs-pastel` |
| Compare | Workflow vs Loom | `/compare/workflow-vs-loom` |
| Support | FAQs | `/pricing#FAQs` |
| Support | Help center | `/help` |
| Support | Contact | `/contact` |
| Support | Feature requests | `https://workflowdesign.featurebase.app/` (left the site) |
| Support | Policies | `/policies` |
| Support | Privacy policy | `/policies#privacy-policy` |
| Support | I *Heart* Workflow | `/referral-program` |

## Auth walls (stop)

| Control | URL | What loaded |
|---|---|---|
| Log in (header) | `https://app.workflow.design/` | Redirects toward sign-in. Not walked past the wall. |
| Sign in (mobile markup, hidden at 1440) | `https://app.workflow.design/users/sign-in` | HTTP 200. Visible text: "Log in to Workflow", buttons "Log in with Google" and "Log in with email", links "Create account" and "Learn more". Google was not clicked. Email was not opened or filled. Known earlier probe that the form never loaded did not repeat on 2026-11-21: the chooser did load. |
| Try now, Get started, referral claim links | `https://app.workflow.design/users/sign-up` | Sign-up wall. Not filled. |
| Marketing login path guessed as `/login` | `https://www.workflow.design/login` | 404. Confirmed separately. |

A downtime banner in the DOM points at `https://status.workflow.design/`. The banner itself is `display: none`. Status was not treated as a product surface.

## Home `/`

| Control | Opens |
|---|---|
| Get started | sign-up wall (stop) |
| Tabs: Live websites, Figma, Images, Videos, Presentations | in-page panes `#w-tabs-0-data-w-pane-0` through `-4`. Videos also toggles a background video play control. |
| Pause page motion | in-page motion toggle (`#feedback-video-bar-play`), not a navigation |
| Watch demo | video overlay (`.video--overlay`). Close video dismisses it. |
| Tabs: Creatives, Reviewers, Teams | in-page testimonial panes (`#w-tabs-1-data-w-pane-*`). Off-screen until that section is in view; they are in the DOM. |
| Compare links in the body | the five `/compare/workflow-vs-*` pages |
| I *Heart* Workflow | `/referral-program` |

No cookie or consent dialog was present. No form on the home page.

## Primary pages

| Path | Title | Interactions |
|---|---|---|
| `/features` | Workflow – Features | Index of feature articles. Each card opens `/features/<slug>`. |
| `/about` | Workflow – About | Team links to `/team/midhat-hadi` and `/team/sophia-oneal`. |
| `/pricing` | Workflow – Pricing | Plan cards, FAQ anchors (`#FAQs`). Plan CTAs open the sign-up wall. Billing toggle, if present, is in-page and was recorded in the capture log. No checkout was started. |
| `/contact` | Workflow – Contact | Contact form present. Fields were not filled and the form was not submitted. |
| `/policies` | Workflow – Policies | In-page anchors for privacy and other policy sections. |
| `/help` | Workflow Help Center | Category links to `/help/<slug>`. |
| `/referral-program` | Referral Program | Program copy. Any "claim" or sign-up control stops at the auth wall. |
| `/backups-templates/careers` | Workflow — Page not found | Footer Careers target. Styled 404. |

## Compare (footer)

`/compare/workflow-vs-markup`, `workflow-vs-ruttl`, `workflow-vs-bugherd`, `workflow-vs-pastel`, `workflow-vs-loom`. Same shell. CTAs to Try now stop at sign-up.

## Feature articles (sitemap, 65 under `/features/`)

Reached from `/features` and from each other. Same marketing shell. Representative interactions (video overlay, in-page tabs) were opened on the index and on one article, not re-clicked on all 65. Full list is the sitemap section below.

## Stories, resources, team (sitemap, not in the header)

| Path | How it is reached |
|---|---|
| `/community-stories-new/adria-studio` | Sitemap. Not in the visible header (Case studies is `display: none`). |
| `/community-stories-new/mika-suetake` | Sitemap. |
| `/community-stories-new/nick-busman` | Sitemap. |
| `/community-stories-new/summonstudio` | Sitemap. |
| `/resources/best-alternatives-to-loom-for-client-review-client-walkthrough-videos` | Sitemap. |
| `/resources/best-budget-friendly-website-feedback-tools` | Sitemap. |
| `/resources/how-to-leave-loom` | Sitemap. |
| `/team/midhat-hadi` | About page. |
| `/team/sophia-oneal` | About page. |

## Help articles

Linked from `/help`. Captured as the help index plus one article from each visible category, not every article, when the index lists more than the shot list can hold. The crawl on 2026-11-21 confirmed these article paths exist (HTTP 200):

- `/help/getting-started-btdq1`
- `/help/why-we-made-workflow-z858t`
- `/help/getting-started-bp2m5`
- `/help/getting-notified-1o8td`
- `/help/sharing-work-nz2pu`
- `/help/what-reviewers-see-3ferr`
- `/help/feedback-3xhmb`
- `/help/versions-472qi`
- `/help/approval-299p5`
- `/help/how-to-view-videos-and-transcriptions-skfya`
- `/help/what-creative-formats-does-workflow-support-353dj`
- `/help/add-images-and-creative-assets-to-a-task-q0ec5`
- `/help/working-with-clients-xqvza`
- `/help/shared-spaces-37ufa`
- `/help/inviting-guests-to-a-project-1qncm`
- `/help/what-clients-and-guests-see-in-workflow-heevw`
- `/help/how-reminders-work-gr0rn`

Further help slugs found while capturing are listed in `raw/site-map.json`.

## Sitemap feature slugs

`/features`, plus:

a-beautiful-new-desktop-app, add-comments-to-videos, add-comments-to-websites, approval-button-a-signal-that-your-work-is-complete, attach-files-directly-to-on-asset-comments, automatic-screenshots-for-website-comments, bring-your-own-branding-to-workflow, browser-and-screen-size-information-for-live-website-comments, check-boxes, comments, custom-ai-checks, design-overlay-plugin, duplicate-projects-tasks-and-create-templates, experience-lightning-fast-collaboration-with-instant-interactions, faster-initial-load-time, faster-video-loading-with-mp4-conversion, feature-requests, figjam-integration, figma-plugin-v3, figma-sync, filter-comments-by-page-and-screen-size, filters-and-sorting, general-quality-of-life-improvements, get-feedback-from-anyone, guided-tours, hide-comments-from-previous-versions, hide-the-side-panel, introducing-project-info-pages, introducing-project-pages, introducing-task-priorities, introducing-text-documents, introducing-the-command-bar, introducing-the-inbox, lightning-fast-comments, lightning-fast-live-sites, lightning-fast-task-loading, live-websites-interact-and-comment, moving-comments, multiplayer-cursors, numbered-comments, pausing-comments, photoshop-plugin, predictive-command-bar, private-projects, project-folders, say-hello-to-our-free-starter-plan, search, search-for-projects, shareable-links, simplified-guest-management, sorting, speed, subscribe-to-projects, subscribe-to-tasks, subtasks, support-for-password-protected-squarespace-sites, tailored-onboarding, task-labels, ultra-responsive-canvas, ux-improvements, ux-quality-of-life-improvements, version-naming, workflow-ai, workflow-ai-improvements.

## Not present on the public site

No public app shell, inbox, project, task, comment composer, or settings. Those live behind the sign-in wall. No dark-theme toggle was found on the marketing pages. No cookie banner was found.
