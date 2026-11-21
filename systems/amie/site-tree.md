# Amie public site tree

Mapped 2026-11-21 from https://amie.so/ in headless Chromium before screenshots. The seed was the home page plus every same-site link it exposes, then https://amie.so/sitemap.xml (65 URLs, last-modified 2026-11-18). Auth walls were recorded and not entered. No field was typed into. No form was submitted. No download was started. Google, Apple, Outlook, and "Continue with the app" were not clicked.

Theme: one painted light theme. `.dark` exists in CSS and only re-declares a few variables. No theme toggle on the public site.

## Global chrome

| Control | Opens | Stop |
|---|---|---|
| Logo (header) | https://amie.so/ | |
| Features (header button, desktop) | Radix popover, in place | Meeting Notes `#notes`, Chat `#chat`, Integrations `#integrations`, Pages `#pages`, AI Scheduling `#calendar-todos`, MCP Server `/mcp` |
| Pricing (header) | https://amie.so/pricing | |
| Login (header, desktop) | https://calendar.amie.so/login | Auth wall. Recorded, not entered |
| Get started (header, desktop) | https://calendar.amie.so/login | Auth wall |
| Get started (header, 390) | https://amie.so/subscribe | Email field present. Not typed |
| Download (hero button, home) | stays on https://amie.so/ | No menu opened on click |
| Footer column | See footer table | |
| GrowSurf widget | External affiliate window (`grow.surf`, `growsurf.com`) | Not opened. Not a product page |

Footer links, present on marketing pages:

| Label | URL |
|---|---|
| Blog | /blog |
| Our Story | /stories |
| Calendar | /calendar |
| Changelog | /changelog |
| Tools | /tools |
| Templates | /templates |
| Alternatives | /alternatives |
| Best Apps | /best |
| MCP Server | /mcp |
| Recording API | /recording-api |
| Routines | /routines |
| AI Response Generator | /tools/ai-response-generator |
| Contact us | /contact |
| Download | /download |
| Affiliates | /affiliate |
| Reviews | /reviews |
| Art | /art |
| Privacy Policy | /privacy |
| Terms of use | /terms |
| Imprint | /imprint |
| LinkedIn, Instagram, x.com | External. Not product pages |

Phone 390 header: logo, Pricing, Get started (`/subscribe`). Features is in the DOM at 0×0. No hamburger. Login is not in the phone header.

## Auth walls (recorded, branch stopped)

| URL | What it shows | Not clicked |
|---|---|---|
| https://calendar.amie.so/login | Title "Login \| Amie". Buttons: Continue with Google, Continue with Outlook, Have the Amie desktop app? Continue with the app. Links to /terms and /privacy. No email field. Known probe said "Login with browser"; the live label on 2026-11-21 is "Continue with the app" | Google, Outlook, Continue with the app |
| https://app.amie.so/login | HTTP 404, "This page doesn't exist" / DEPLOYMENT_NOT_FOUND (certificate warning ignored only to read the status) | |

Login and Get started on the desktop header, and Start free trial / Start 7 day free trial / plan Select on pricing, all point at `https://calendar.amie.so/login`. Those branches stop there.

## Home interactions

| Control | Result |
|---|---|
| Features | Popover listed above. Hash links scroll the home page. MCP Server goes to /mcp |
| Home FAQ buttons (7) | Radix accordion, in place. Same question set as pricing |
| Changelog pill | /changelog |
| Download (hero) | No navigation, no menu |
| Get started, Start free trial | Auth wall |

Hash targets on home, also linked from the Features popover: `#notes`, `#chat`, `#integrations`, `#pages`, `#calendar-todos`.

## Marketing and product pages

Each row is a public page. Shared chrome is the header and footer above. Extra controls are listed.

| Path | What it is | Extra controls |
|---|---|---|
| / | Home | Features popover, FAQ accordion, changelog pill, Download button |
| /pricing | Plans | Bill monthly / Bill yearly toggle. FAQ accordion (7). Trial and Select go to the login wall |
| /changelog | Changelog index | Long single page. No per-entry route in the sitemap |
| /blog | Blog index | Post links and /blog/page/2, /blog/page/3 |
| /blog/page/2, /blog/page/3 | Blog pagination | Page 3 links back to 2 and 3 only. End of the index |
| /stories | Story index | /stories/early-design, /stories/design |
| /calendar | Calendar marketing | Get started to login wall |
| /download | Download | "Download for macOS" starts a binary. Not clicked |
| /contact | Contact form | Name, email, message, Send message. Not typed, not submitted |
| /contact?sales | Request a demo | Same form family. Not submitted |
| /affiliate | Affiliate program | External GrowSurf links. Not opened |
| /reviews | Reviews | |
| /art | Art page ("Happy Saturday!") | |
| /privacy, /terms, /imprint, /additional-terms | Legal | |
| /subscribe | Email signup | Email field, Sign up, plus a second name/email form. Not typed, not submitted |
| /recap | Recap 2023 | In sitemap, not linked from home |
| /mcp | MCP marketing | Child setup guides |
| /recording-api | Recording API marketing | |
| /routines | Routines index | One child linked |
| /tools | Tools index | Three tools |
| /templates | Template index | Six templates. Copy buttons copy text. Not a form submit |
| /alternatives | Alternatives index | Four comparison pages |
| /best | Best-of index | Two guides |

## Feature pages

Linked from product sections and the sitemap. Not behind login.

| Path | H1 on 2026-11-21 |
|---|---|
| /features/notes | Record with Amie |
| /features/chat | (page title area reads Calendar & Todos on first paint; sitemap lists it as chat) |
| /features/collections | Collections |
| /features/calendar-todos | Chat |

## Content children

Blog posts in the sitemap (each is a long article, same chrome, no extra dialog):

- /blog/atomic-habits-summary
- /blog/best-ai-executive-assistant
- /blog/best-ai-note-taker
- /blog/best-transcription-software
- /blog/essential-ai-tools-for-remote-teams
- /blog/how-to-record-zoom-meetings
- /blog/how-to-take-meeting-notes
- /blog/how-to-transcribe-meetings
- /blog/intake-meetings
- /blog/note-taking-types
- /blog/remote-closing
- /blog/summary-report
- /blog/youtube-video-transcript

Stories: /stories/early-design, /stories/design.

Routines: /routines/andrew-huberman. The index exposed only this child.

Tools:

| Path | Extra controls | Stop |
|---|---|---|
| /tools/ai-response-generator | Mode buttons (New email, Reply), tone (Casual), Style, language (English), Generate. Email and feedback fields | Generate and Submit feedback not clicked. Fields not typed |
| /tools/ai-prompt-generator | Generator controls | Generate not clicked. Fields not typed |
| /tools/aesthetic-pomodoro-timer | Timer controls | Start not treated as a form submit; local timer only if captured |

Templates (copy-in-page, no signup wall): /templates/meeting-notes, /templates/meeting-agenda, /templates/one-on-one-meeting, /templates/time-blocking, /templates/weekly-planner, /templates/habit-tracker.

Alternatives: /alternatives/granola, /alternatives/otter, /alternatives/calendly, /alternatives/sunsama.

Best: /best/calendar-apps, /best/daily-planner-apps.

MCP setup guides: /mcp/claude-code, /mcp/claude-desktop, /mcp/chatgpt, /mcp/codex, /mcp/cursor, /mcp/google-calendar.

## Documentation

/documentation is a public index. It is in the sitemap and was not linked from the home footer. Its sidebar opens these pages:

- /documentation/getting-started/quick-start
- /documentation/getting-started/installation
- /documentation/attio-integration
- /documentation/email-integration
- /documentation/google-calendar-integration
- /documentation/google-meet-integration
- /documentation/salesforce-integration
- /documentation/scheduling-links
- /documentation/slack-integration
- /documentation/zoom-integration
- /documentation/account/billing
- /documentation/account/settings
- /documentation/desktop/menubar
- /documentation/features/ai-notes
- /documentation/features/ai-scheduling
- /documentation/features/pages
- /documentation/features/tasks

## Not captured on purpose

| Thing | Why |
|---|---|
| Signed-in calendar, inbox, notes, recording | Behind https://calendar.amie.so/login |
| Google, Outlook, Apple, Continue with the app | Auth providers. Not clicked |
| Contact, demo, subscribe, newsletter, tool feedback | Forms. Not typed, not submitted |
| macOS/Windows download binaries | `calendar.amie.so/api/download?...` starts a file download |
| External social, YouTube, GrowSurf | Not Amie product UI. The Watch demo dialog embeds a YouTube iframe; the iframe was not clicked |
| Full-page width on /recap, pomodoro, prompt generator | Those pages set a min-width, so the stitched `-full` PNG is wider than 1440 or 390. Viewport shots are the sized captures |
| Dark theme | No public control sets `.dark` |
| Phone hamburger menu | Not present. Features button is 0×0 at 390 |
