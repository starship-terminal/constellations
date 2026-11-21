# Hello Ivy public site tree

Mapped on 2026-11-21 from [https://www.helloivy.co/](https://www.helloivy.co/) with headless Playwright (Chromium), before any package screenshots. The marketing site is a Framer site (`www.helloivy.co`). The product lives on `app.helloivy.co` and stops at a login or signup wall. Nothing was submitted. No password was typed. Google was not clicked.

The sitemap at [https://www.helloivy.co/sitemap.xml](https://www.helloivy.co/sitemap.xml) lists 173 URLs: 1 home, 29 other marketing and docs index pages, 11 feature pages, 24 docs articles, 35 release notes, 84 blog posts. A crawl of the home page and its first-level links confirmed the same tree and then stopped inside the blog (80 pages visited, 101 blog URLs still queued). Blog posts and release notes share one template each. They are listed as families, not as 119 separate interaction maps.

`html` carries `toggle-theme="light"` on every page that loaded. No public control switched it to dark. The phone overlay paints the words "Change theme" next to a sun glyph, but that node is page content scrolled thousands of pixels down, not a control inside the overlay. Clicking the painted words did not change `toggle-theme` or the page background.

## Shell

The same header sits on every `www.helloivy.co` page. Desktop at 1440 shows the wordmark, three text links, a pill, and a menu icon. Phone at 390 shows the wordmark and the menu icon. A black "hi / Try it for free" pill is fixed to the bottom-right of marketing pages. It is a link, not a dialog.

| Control | Opens |
|---|---|
| Wordmark "hello ivy" | [https://www.helloivy.co/](https://www.helloivy.co/) |
| Features (header link and the duplicate header button) | [https://www.helloivy.co/features](https://www.helloivy.co/features). No dropdown. Hover does not open a menu. |
| Pricing | [https://www.helloivy.co/pricing](https://www.helloivy.co/pricing) |
| Log in | [https://app.helloivy.co/login](https://app.helloivy.co/login). Auth wall. Branch stops. |
| Get Started (header pill) | [https://complex.so/](https://complex.so/). A different product ("Simple task management"). Not Hello Ivy. |
| Menu icon (three lines, header right; `data-framer-name="Menu"`) | Full-screen overlay on the same URL. See Menu overlay. |
| Try it for free (fixed pill) | [https://complex.so/](https://complex.so/). Same off-site product. |

## Menu overlay

Opened by clicking the menu icon (desktop click at the icon, about 1336, 82; phone click about 294, 74). The page URL does not change. `html` gets `style="overflow: hidden"`. Close is the X in the top-right. The overlay is a list of links, not a dialog with its own route.

| Overlay control | Opens |
|---|---|
| 01 HOME | [https://www.helloivy.co/](https://www.helloivy.co/) |
| 02 FEATURES | [https://www.helloivy.co/features](https://www.helloivy.co/features) |
| 03 PRICING | [https://www.helloivy.co/pricing](https://www.helloivy.co/pricing) |
| 04 ABOUT | [https://www.helloivy.co/about](https://www.helloivy.co/about) |
| 05 BLOG | [https://www.helloivy.co/blog](https://www.helloivy.co/blog) |
| Get Started - Free Trial | [https://complex.so/](https://complex.so/) |
| LinkedIn glyph | [https://www.linkedin.com/company/hello-ivy](https://www.linkedin.com/company/hello-ivy) |
| X glyph | [https://twitter.com/hello_ivy_app](https://twitter.com/hello_ivy_app) |
| Facebook glyph (phone overlay only) | [https://www.facebook.com/clonify.io](https://www.facebook.com/clonify.io). A third-party page, not Hello Ivy. |
| X (close) | Closes the overlay. Stays on the current page. |

The overlay also paints a street address and an email. Those strings are not copied into this package. The address is the company's published footer line. The email is a contact address. Both stay out of the package text.

## Home

[https://www.helloivy.co/](https://www.helloivy.co/) is one long marketing page. No form. No dialog. Inline product videos play in the page (`framerusercontent.com` mp4), not in a modal. Clicking the "Meet Hello Ivy in 60 seconds" play mark did not open a dialog. It also did not start a visible modal player in the probe. The videos are public demos of the app, not the signed-in app.

| Control | Opens |
|---|---|
| "design projects" in the intro | [https://www.helloivy.co/project-management](https://www.helloivy.co/project-management) |
| Feed | [https://www.helloivy.co/features/feed](https://www.helloivy.co/features/feed) |
| external clients | [https://www.helloivy.co/features/client-portal](https://www.helloivy.co/features/client-portal) |
| drafting design briefs | [https://www.helloivy.co/features/docs](https://www.helloivy.co/features/docs) |
| task management | [https://www.helloivy.co/features/tasks](https://www.helloivy.co/features/tasks) |
| integrating feedback | [https://www.helloivy.co/features/feed](https://www.helloivy.co/features/feed) |
| annotation | [https://www.helloivy.co/features/annotate](https://www.helloivy.co/features/annotate) |
| approval phases | [https://www.helloivy.co/features/annotate](https://www.helloivy.co/features/annotate) |
| Projects card | [https://www.helloivy.co/project-management](https://www.helloivy.co/project-management) |
| Roadmap card | [https://www.helloivy.co/features/roadmap](https://www.helloivy.co/features/roadmap) |
| Feedback card | [https://www.helloivy.co/features/feed](https://www.helloivy.co/features/feed) |
| Tasks card | [https://www.helloivy.co/features/tasks](https://www.helloivy.co/features/tasks) |
| Calendar card | [https://www.helloivy.co/features/calendar](https://www.helloivy.co/features/calendar) |
| Documents card | [https://www.helloivy.co/features/docs](https://www.helloivy.co/features/docs) |
| Files card | [https://www.helloivy.co/features/files](https://www.helloivy.co/features/files) |
| Chat card | [https://www.helloivy.co/features/chat](https://www.helloivy.co/features/chat) |
| LOOKS GREAT GET STARTED | [https://complex.so/](https://complex.so/) |
| Footer feature links | The same feature pages, plus version control and client portal |
| Footer About | [https://www.helloivy.co/about](https://www.helloivy.co/about) |
| Footer Project Management | [https://www.helloivy.co/project-management](https://www.helloivy.co/project-management) |
| Footer Project Collaboration | [https://www.helloivy.co/project-collaboration-software](https://www.helloivy.co/project-collaboration-software) |
| Footer vs Basecamp, Notion, Asana, ClickUp, Monday, Trello | The matching `*-alternative` page |
| Footer Blog | [https://www.helloivy.co/blog](https://www.helloivy.co/blog) |
| Footer Documentation | [https://www.helloivy.co/docs](https://www.helloivy.co/docs) |
| Footer Release notes | [https://www.helloivy.co/release-notes](https://www.helloivy.co/release-notes) |
| Footer Media kit | An `app.helloivy.co` share URL. App host. Branch stops. Not opened. The path is omitted. |
| Footer Task Management | [https://complex.so/](https://complex.so/) |
| Footer Terms | [https://www.helloivy.co/terms](https://www.helloivy.co/terms) |
| Footer social glyphs | LinkedIn and X, as in the overlay |

## Feature pages

[https://www.helloivy.co/features](https://www.helloivy.co/features) is an index. Each card is a link to one feature page. No tabs, no filter, no dialog. The feature pages share one template (a long marketing article with the same header, footer, and off-site CTAs).

| Page | URL |
|---|---|
| Tasks | [https://www.helloivy.co/features/tasks](https://www.helloivy.co/features/tasks) |
| Docs | [https://www.helloivy.co/features/docs](https://www.helloivy.co/features/docs) |
| Feed | [https://www.helloivy.co/features/feed](https://www.helloivy.co/features/feed) |
| Roadmap | [https://www.helloivy.co/features/roadmap](https://www.helloivy.co/features/roadmap) |
| Calendar | [https://www.helloivy.co/features/calendar](https://www.helloivy.co/features/calendar) |
| Files | [https://www.helloivy.co/features/files](https://www.helloivy.co/features/files) |
| Chat | [https://www.helloivy.co/features/chat](https://www.helloivy.co/features/chat) |
| Embed | [https://www.helloivy.co/features/embed](https://www.helloivy.co/features/embed) |
| Client portal | [https://www.helloivy.co/features/client-portal](https://www.helloivy.co/features/client-portal) |
| Annotate | [https://www.helloivy.co/features/annotate](https://www.helloivy.co/features/annotate) |
| Version control | [https://www.helloivy.co/features/version-control](https://www.helloivy.co/features/version-control) |

## Pricing

[https://www.helloivy.co/pricing](https://www.helloivy.co/pricing) is a static plan page. No billing toggle, no FAQ accordion, no form.

| Control | Opens |
|---|---|
| Try for Free (two plan cards) | [https://app.helloivy.co/sign-up](https://app.helloivy.co/sign-up), which redirects to `https://app.helloivy.co/sign-up?teams`. Auth wall. Branch stops. |
| Let's Talk | `mailto:` with subject "Enterprise plan interest". Not opened. The address is not written here. |
| Unlimited plan request link | `mailto:` with subject "Unlimited Plan Request". Not opened. |

## About, solutions, comparisons

These are long marketing pages with the same shell. Comparison pages share one template. Solution pages found from in-page links (not all are in the sitemap) redirect or 200 as follows.

| Page | URL | Note |
|---|---|---|
| About | [https://www.helloivy.co/about](https://www.helloivy.co/about) | 200 |
| Project management | [https://www.helloivy.co/project-management](https://www.helloivy.co/project-management) | 200 |
| Project collaboration | [https://www.helloivy.co/project-collaboration-software](https://www.helloivy.co/project-collaboration-software) | 200 |
| Next-generation project management | [https://www.helloivy.co/next-generation-project-management](https://www.helloivy.co/next-generation-project-management) | 200, sitemap only |
| Alternatives | `/basecamp-alternative`, `/notion-alternative`, `/asana-alternative`, `/clickup-alternative`, `/monday-alternative`, `/trello-alternative`, `/jira-alternative`, `/teamwork-alternative` | Same template. Jira and Teamwork are sitemap-only, not in the home footer. |
| Waiting list, design, product, marketing, sales, startups, remote-teams, annotate-designs, task-management | same paths on `www.helloivy.co` | Linked from older blog posts. `/waiting-list` and `/design` redirect to home. Not separate products. |
| Terms | [https://www.helloivy.co/terms](https://www.helloivy.co/terms) | 200. Title "Terms & Privacy". No separate `/privacy` (404). |

## Blog

[https://www.helloivy.co/blog](https://www.helloivy.co/blog) is an index of article cards. Each card opens `/blog/<slug>`. The sitemap lists 84 posts. Posts share one article template (header, prose, footer). No comments form, no search box, no dialog. Representative post checked: [https://www.helloivy.co/blog/tips-tricks-for-using-hello-ivy](https://www.helloivy.co/blog/tips-tricks-for-using-hello-ivy).

## Docs

[https://www.helloivy.co/docs](https://www.helloivy.co/docs) is a public help index. Sidebar and body links open article pages. No search field was visible. No login wall.

Articles linked from the index and the sitemap:

`/docs/create-a-project`, `/docs/create-a-task`, `/docs/invite-your-team`, `/docs/team-collaboration-basics`, `/docs/tips-tricks`, `/docs/task-views`, `/docs/assign-a-task`, `/docs/task-attributes`, `/docs/filters-and-view`, `/docs/recurring-tasks`, `/docs/manage-teammates`, `/docs/project-overview`, `/docs/tasks`, `/docs/pages`, `/docs/conversations`, `/docs/embedded-views`, `/docs/today-tool`, `/docs/the-feed`, `/docs/timeline`, `/docs/chat`, `/docs/client-portal`, `/docs/task-management`, `/docs/what-s-new`, `/docs/support`.

## Release notes

[https://www.helloivy.co/release-notes](https://www.helloivy.co/release-notes) is a changelog index. Each row opens `/release-notes/<slug>`. The sitemap lists 35 notes. They share one article template. No dialog.

## Auth walls (branch stops)

These URLs were loaded only far enough to record the wall. No field was filled. No button that submits or starts OAuth was clicked.

| URL | What it asks |
|---|---|
| [https://app.helloivy.co/login](https://app.helloivy.co/login) | Email, password, Continue, Login with Google, Forgot password (`/reset-password`), Sign up. |
| [https://app.helloivy.co/sign-up](https://app.helloivy.co/sign-up) | Redirects to `/sign-up?teams`. Work email, Continue, Sign up with Google, Log in. |
| [https://app.helloivy.co/reset-password](https://app.helloivy.co/reset-password) | Linked from login as "Forgot password?". Not opened. Recovery flow. |
| Media kit share URL on `app.helloivy.co` | Footer link. Not opened. App host. |

`https://complex.so/` loads a different product's marketing page. It is recorded as an off-site CTA, not as a Hello Ivy surface, and is not captured as Hello Ivy UI.

## What is not on the public site

No cookie banner mounted (consent SDK requests were aborted, and no banner was in the DOM). No select, checkbox, radio, switch, tabs, tooltip, toast, or data table on the pages probed. No dark theme switch that changes the page. The signed-in app (projects, tasks, chat, settings) is behind the login wall.
