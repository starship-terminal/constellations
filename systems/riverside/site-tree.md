# Riverside public site tree

Mapped from the live homepage at https://riverside.com/ on 2026-11-21, signed out, in headless Chromium at 1440×900, before any screenshot. The site is a Webflow marketing build (`w-nav`, `w-dropdown`, `wf-*` font classes). One light theme. Cookie UI is a dialog ("About cookies on this site") with Cookie settings and Allow all cookies. That dialog is hidden, never answered.

A control that opens a login or signup wall stops that branch. Known wall: https://riverside.com/login shows email and password, or SSO. Password was not submitted. No form was submitted.

## Header (desktop)

The bar is a Webflow nav. Logo goes home. Three dropdowns are `div.w-dropdown-toggle` (role button), not links. They open menus already in the DOM (`w-dropdown-list`), they do not navigate.

| Control | Opens |
|---|---|
| Logo (`a.c-updated-nav-logo`, href `/`) | https://riverside.com/ |
| Platform (`div.nav-dropdown-toggle--updated`) | Menu `w-dropdown-list-0` (products, features, apps). See below. |
| Meet the Agents (link inside the Platform menu) | https://riverside.com/agents |
| Solutions (`div.nav-dropdown-toggle--updated`) | Menu `w-dropdown-list-1` (use cases, for, industries). See below. |
| Resources (`div.nav-dropdown-toggle--updated`) | Menu `w-dropdown-list-2` (learn, community, support). See below. |
| For Business | https://riverside.com/business |
| Pricing | https://riverside.com/pricing |
| Contact Sales (`#contact_sales_button`) | In-page anchor, not a new page. The book-a-demo form is https://riverside.com/book-demo (email, name, phone, job, company). Not filled. Not submitted. |
| Login | https://riverside.com/dashboard. Wall: redirects into the studio sign-in. Branch stopped. |
| Start for Free | https://riverside.com/start redirects to https://riverside.com/register. Signup wall (account creation). Branch stopped. Not filled. |

### Platform menu

| Item | Opens |
|---|---|
| Recording | https://riverside.com/recording |
| Editing | https://riverside.com/video-editor |
| Live Streaming | https://riverside.com/livestream |
| Webinars | https://riverside.com/use-cases/webinars |
| Hosting | https://riverside.com/podcast-hosting |
| Newsletters | https://riverside.com/newsletter |
| Agents / Meet the Agents | https://riverside.com/agents |
| Magic Clips | https://riverside.com/magic-clips (tabs: Let AI generate your clips, Fine-tune or create from scratch) |
| AI Twin | https://riverside.com/ai-twin |
| Transcribing | https://riverside.com/transcription (file input; not uploaded) |
| Captions | https://riverside.com/captions |
| Magic Audio | https://riverside.com/magic-audio |
| AI Show Notes | https://riverside.com/show-notes |
| AI Translation | https://riverside.com/ai-translation |
| Social Scheduling | https://riverside.com/content-planner |
| Video Enhancement | https://riverside.com/video-enhancement |
| AI Tools / All AI Tools | https://riverside.com/ai |
| Mac App | https://riverside.com/mac-app |
| Mobile Apps | https://riverside.com/mobile |
| MCP | https://riverside.com/mcp |

### Solutions menu

| Item | Opens |
|---|---|
| Podcasts | https://riverside.com/use-cases/podcasting |
| Video testimonials | https://riverside.com/use-cases/video-testimonial-software |
| Webinars | https://riverside.com/use-cases/webinars |
| Video marketing | https://riverside.com/use-cases/video-marketing |
| In-person Recording | https://riverside.com/use-cases/in-person |
| Learning & Development | https://riverside.com/use-cases/learning-development |
| Async Recording | https://riverside.com/async-recording |
| Virtual conferences | https://riverside.com/use-cases/virtual-conferences (step tabs 1–4, local UI) |
| Internal communications | https://riverside.com/use-cases/internal-communications |
| Tutorial videos | https://riverside.com/use-cases/tutorial-videos |
| Podcasters | https://riverside.com/solutions/podcasters |
| Producers | https://riverside.com/solutions/producers |
| Marketers | https://riverside.com/solutions/marketers |
| Tech | https://riverside.com/industries/technology-recording-software |
| Finance | https://riverside.com/industries/financial-recording-software |

### Resources menu

| Item | Opens |
|---|---|
| Riverside University | https://riverside.com/university (search field; not submitted) |
| Blog | https://riverside.com/blog (email subscribe; not submitted) |
| What's New | https://riverside.com/university/product-updates |
| Free tools | https://riverside.com/tools |
| Webinars | https://riverside.com/webinars (email field; not submitted) |
| Masterclass | https://riverside.com/masterclass/master-the-art-of-podcasting |
| Case studies | https://riverside.com/case-studies |
| Creators Newsletter | https://riverside.com/creators-newsletter-registration (email; not submitted) |
| Community hub | https://riverside.com/community (name, email, message form; not submitted) |
| Recorded on Riverside | https://riverside.com/recorded-on-riverside (submission form; not submitted) |
| Help Center | https://support.riverside.com/hc/en-us (public Zendesk search; not submitted) |
| Contact support | `https://riverside.com/homepage#` (empty hash, stays on the page) |

## Header (phone)

At 390 the same links sit behind the Webflow hamburger (`.w-nav-button`). Opening it reveals Platform, Solutions, Resources, For Business, Pricing, Login, Start for Free. Login and Start for Free are the same walls as desktop. The menu is a local interaction, not a new page.

## Pricing page interactions

https://riverside.com/pricing heading "There's a plan for every story." A Monthly / Yearly toggle sits above four cards (Pro, Grow, Webinar, Business). Yearly is the default. Local UI only. No checkout was opened. Trial and Book a demo were not followed.

## FAQ

https://riverside.com/faq is a public accordion page. Opening a question is a local interaction.

## Language

Footer and repeated dropdowns labelled English open a two-item menu: English (https://riverside.com/homepage) and Deutsch (https://riverside.com/de). The German homepage loaded (h1 "Erstelle deine besten Inhalte."). The capture stays on the English surface. The German site is the same marketing system in another language, not a second theme.

## Homepage body and footer (not in the header menus)

These links are on the homepage body or footer. Each was loaded once to classify it. None was submitted.

| Control | Opens |
|---|---|
| About Us | https://riverside.com/about |
| Careers | https://careers.riverside.com/ (department radios and a text filter; not submitted) |
| Partners | https://riverside.com/partners |
| Affiliate Program | https://riverside.com/affiliate-program |
| Creator Partnerships | https://riverside.com/creator-partnerships |
| Why Riverside | https://riverside.com/why-riverside |
| FAQ | https://riverside.com/faq |
| AI Co-Creator | https://riverside.com/co-creator |
| Teleprompter | https://riverside.com/teleprompter |
| Overlays | https://riverside.com/overlays |
| Studio Branding | https://riverside.com/studio-branding |
| Virtual Events | https://riverside.com/use-cases/virtual-events |
| Live Show | https://riverside.com/use-cases/live-podcast-software (step tabs) |
| Split-Screen Video | https://riverside.com/use-cases/split-screen-video (step tabs) |
| Book a demo | https://riverside.com/book-demo (form; not submitted) |
| Terms | https://riverside.com/terms-conditions |
| Privacy | https://riverside.com/privacy-policy |
| Cookies | https://riverside.com/cookies |
| App Store | https://apps.apple.com/us/app/riverside-fm/id1554443872 (store listing, left) |
| Google Play | https://play.google.com/store/apps/details?id=riverside.fm (store listing, left) |
| Facebook, YouTube, X, LinkedIn | External social profiles. Left. |
| Instagram, TikTok | External profiles. Treated as walls (login chrome). Left. |

### Blog posts linked from the homepage

| Post | URL |
|---|---|
| How to Start a Podcast in 2026 | https://riverside.com/blog/how-to-start-a-podcast |
| How to Start a Podcast on YouTube | https://riverside.com/blog/how-to-start-a-podcast-on-youtube |
| How to Record a Podcast Remotely | https://riverside.com/blog/how-to-record-a-podcast-remotely |
| Video Podcast Software | https://riverside.com/blog/video-podcast-software |

Each has an email subscribe field. Not submitted. The blog index is the captured article pattern; individual posts are the same template.

### Free tools linked from the homepage footer

| Tool | URL | Interaction |
|---|---|---|
| Podcast Maker | https://riverside.com/tools/podcast-maker | File input. Not uploaded. |
| Podcast Recorder | https://riverside.com/tools/podcast-recorder | File input. Not uploaded. |
| Live Podcast | https://riverside.com/tools/live-podcast | File input. Not uploaded. |
| YouTube Video Maker | https://riverside.com/tools/youtube-video-maker | File input. Not uploaded. |
| Screen Recorder | https://riverside.com/recording/screen-recorder | Marketing page. |
| Video Compressor | https://riverside.com/video-compressor | Marketing page. |
| WAV To MP3 | https://riverside.com/wav-to-mp3 | Marketing page. |
| Podcast Name Generator | https://riverside.com/podcast-name-generator | Text field + submit. Not submitted. |
| YouTube Name Generator | https://riverside.com/youtube-name-generator | Text field + submit. Not submitted. |
| Mic Test | https://riverside.com/mic-test | Local mic UI. Not granted. |
| Webcam Test | https://riverside.com/webcam-test | Local camera UI. Not granted. |
| YouTube Transcript Generator | https://riverside.com/tools/youtube-transcript-generator | File input. Not uploaded. |
| Top Podcast Charts | https://riverside.com/top-podcasts | Public list. |
| Free Podcast Music | https://riverside.com/free-podcast-music | Public list. |
| Video Editing Glossary | https://riverside.com/video-editor/video-editing-glossary | Public glossary. |

## Walls (branch stopped)

| URL | What it showed | Action |
|---|---|---|
| https://riverside.com/login | Email and password, or SSO (Google, Apple). | Recorded. Password not submitted. SSO not clicked. |
| https://riverside.com/dashboard | Studio sign-in wall (Login in the header lands here). | Stopped. |
| https://riverside.com/start | Redirects to https://riverside.com/register (signup). | Not filled. Stopped. |

The signed-in studio, editor, recording room, billing checkout, and account settings are behind those walls. They are not in this package.

## Cookie dialog

Role `dialog`, label `ch2-dialog-title`. Buttons: Cookie settings, Allow all cookies. Hidden with CSS. Neither button was clicked, so no consent POST ran.
