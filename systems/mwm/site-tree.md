# MWM public site tree

Mapped on 2026-11-21 from https://www.mwm.ai/ with Playwright, before screenshots. The live host is `https://mwm.ai/` (the `www` host redirects). English is the captured language. The same shell repeats on every marketing page: a dark page (`html.dark-mode`, body background `rgb(0, 0, 0)`, theme-color `#0D0D0D`). No light theme switch was found.

Catalog rows (apps, tags, glossary terms, articles, rankings, guides) share one template each. The tree names the template and one example, not every row. Sitemap indexes under `https://mwm.ai/sitemaps/` list thousands of those rows.

## Shared chrome

| Control | Opens |
|---|---|
| Logo, "MWM home" | https://mwm.ai/ |
| Products (button, `aria-expanded`) | Mega menu. Columns: MWM AI, MWM Console, MWM Publishing, MWM Studio. See below. |
| Resources (button, `aria-expanded`) | Mega menu. Columns: directory, writing, company, featured apps. See below. |
| Pricing | https://mwm.ai/pricing |
| Open MWM Console | https://console.mwm.ai/ which redirects to https://console.mwm.ai/sign-in?next=home-redirect. Login wall. Stop. |
| Build your app | https://create.mwm.ai/ which redirects to https://create.mwm.ai/sign-in?next=home&next_path=/. Login wall. Stop. |
| Open navigation (`aria-controls="mwm-product-mobile-menu"`) | Phone drawer with the same header links, plus Products and Resources buttons. Close navigation dismisses it. |
| Footer summary Products | Same product links as the Products menu, collapsed until opened. |
| Footer summary Resources | Blog, Glossary, Guides. |
| Footer summary About | Company, Careers, IP Dispute. |
| Footer summary Our apps | External product sites: edjing.com, colorpop.ai, swipewipe.com, guitartunerpro.net, beatmakerpro.app. |
| Switch language (EN) | Menu of locale homes. English stays on `/`. Other locales are mirrors, not separate products. |
| Privacy Policy | https://mwm.ai/privacy-policy |
| Terms of Service | https://mwm.ai/terms-of-service |

Language menu targets: `/` English, `/es/` Español, `/pt/` Português, `/ko/` 한국어, `/it/` Italiano, `/de/` Deutsch, `/fr/` Français, `/ja/` 日本語. `/us/` redirects to `/`.

### Products menu

| Link | Opens |
|---|---|
| MWM AI | https://mwm.ai/mwm-ai |
| Meet the Squad | https://mwm.ai/mwm-ai#mwm-ai-agents |
| One chat | https://mwm.ai/mwm-ai#mwm-ai-pipeline |
| Apps Gallery | https://mwm.ai/mwm-ai#mwm-ai-gallery |
| Testimonials | https://mwm.ai/mwm-ai#mwm-ai-testimonials |
| FAQ | https://mwm.ai/mwm-ai#mwm-ai-faq |
| MWM Console | https://mwm.ai/mwm-console |
| One workspace | https://mwm.ai/mwm-console#mwm-console-overview |
| MWM Intelligence | https://mwm.ai/mwm-intelligence |
| From signal to decision | https://mwm.ai/mwm-console#mwm-console-signals |
| Testimonials | https://mwm.ai/mwm-console#mwm-console-testimonials |
| FAQ | https://mwm.ai/mwm-console#mwm-console-faq |
| MWM Publishing | https://mwm.ai/mwm-publishing |
| Your growth partner | https://mwm.ai/mwm-publishing#mwm-publishing-growth |
| One SDK | https://mwm.ai/mwm-publishing#mwm-publishing-sdk |
| From traction to global scale | https://mwm.ai/mwm-publishing#mwm-publishing-overview |
| Testimonials | https://mwm.ai/mwm-publishing#mwm-publishing-testimonials |
| FAQ | https://mwm.ai/mwm-publishing#mwm-publishing-faq |
| MWM Studio | https://mwm.ai/mwm-studio |
| View all apps | https://mwm.ai/mwm-studio/apps |
| Music apps | https://mwm.ai/mwm-studio#studio-section-music |
| Creativity apps | https://mwm.ai/mwm-studio#studio-section-creativity |
| Productivity apps | https://mwm.ai/mwm-studio#studio-section-productivity |

### Resources menu

| Link | Opens |
|---|---|
| Apps Directory | https://mwm.ai/apps/ |
| App Store Rankings | https://mwm.ai/rankings/countries |
| Explore Clusters | https://mwm.ai/tags |
| Blog | https://mwm.ai/articles |
| Glossary | https://mwm.ai/glossary |
| Guides | https://mwm.ai/guides |
| Company | https://mwm.ai/company |
| Careers | https://mwm.teamtailor.com/#jobs (leaves mwm.ai) |
| Terms of Service | https://mwm.ai/terms-of-service |
| Privacy Policy | https://mwm.ai/privacy-policy |
| IP Dispute | https://mwm.ai/legal/ip-dispute |
| Color Pop AI, Edjing Mix, Swipewipe | External product sites |

## Home, https://mwm.ai/

| Control | Opens |
|---|---|
| Prompt textarea, "Describe the mobile app you want to build..." | Local field. Not submitted. |
| Add attachment | File picker control. No file chosen. No dialog beyond the picker. |
| Agent (`aria-controls="mwm-agent-menu"`) | Option menu: Agent (selected), Plan, Debug, Ask. Selecting changes the composer label. Does not navigate. |
| iOS (`aria-controls="mwm-platform-menu"`) | Option menu: iOS (selected), Android. |
| Fable 5 (`aria-controls="mwm-model-menu"`) | Option menu: Fable 5 (selected), Opus 5, GPT 5.6 Sol, GPT 5.6 Terra, Gemini 3.1 Pro, Gemini 3.6 Flash. |
| Voice input | Control is present. Not used (would ask for a microphone). |
| Enter a prompt to continue | Disabled until a prompt is typed. Not pressed. Sending a prompt would start app creation. |
| Learn more about MWM AI | https://mwm.ai/mwm-ai |
| Learn more about MWM Console | https://mwm.ai/mwm-console |
| Learn more about MWM Publishing | https://mwm.ai/mwm-publishing |
| View more (studio) | https://mwm.ai/mwm-studio |
| View more (intelligence) | https://mwm.ai/mwm-intelligence |
| View more (company) | https://mwm.ai/company |

## Product and company pages

| Page | Extra controls |
|---|---|
| https://mwm.ai/pricing | Plan CTAs "Get MWM AI Pro" and "Get MWM AI Pro+" go to https://create.mwm.ai/ (login wall; stop). "Apply for Publishing" goes to `/mwm-publishing`. 15 FAQ buttons (`mwm-pricing-faq-answer-0` through `14`) expand answers in place. |
| https://mwm.ai/mwm-ai | Agent cards: Theo, Mira, Cody open a details panel. Aspen, Tess, Roy, Cora, Iris are "Coming Soon" and do not open a page. 9 FAQ buttons. In-page anchors from the Products menu. |
| https://mwm.ai/mwm-console | 11 FAQ buttons. Anchors from the Products menu. "Open MWM Console" is the login wall above. |
| https://mwm.ai/mwm-publishing | FAQ buttons. Anchors from the Products menu. |
| https://mwm.ai/mwm-intelligence | Marketing page. No extra controls beyond chrome and in-page links. |
| https://mwm.ai/mwm-studio | App cards open `/mwm-studio/apps/:slug`. "View all apps" opens the index. Section anchors for music, creativity, productivity. |
| https://mwm.ai/mwm-studio/apps | Index of studio apps. Each card opens `/mwm-studio/apps/:slug`. Example: `/mwm-studio/apps/edjing`. |
| https://mwm.ai/mwm-studio/apps/:slug | App page. Share button, Previous screenshot, Next screenshot. Example captured: edjing. |
| https://mwm.ai/company | Company page. "View more" and in-page links. |
| https://mwm.ai/company/story | Story page. Sources summary expands a source list. Linked from the company page, not the header. |

## Directory and writing

These indexes are public. Each row is the same template. Capture the index plus one example, not the catalog.

| Page | Controls and children |
|---|---|
| https://mwm.ai/articles | Index. Cards open three sections: `/articles/app-trends`, `/articles/app-updates`, `/articles/reports`. |
| https://mwm.ai/articles/app-trends | Search field, two selects, pagination (Previous, page numbers, Next). Cards open `/articles/app-trends/:slug`. |
| https://mwm.ai/articles/app-updates | Same search, selects, and pagination. Cards open `/articles/app-updates/:slug`. |
| https://mwm.ai/articles/reports | Search. Filter buttons: All, Worldwide, Europe, France, Category. Cards open `/articles/reports/:slug`. |
| Article `:slug` | Article. "On this page" summary. "+6 more" expands a tag list. Author link opens `/authors/:slug`. Related articles. Example: Herdr climbs to top five. |
| https://mwm.ai/guides | Cards open `/guides/:slug`. Example: `/guides/app-store-optimization`. |
| Guide `:slug` | Long article. "On this page" is a phone-width summary (0 size at 1440, visible at 390). In-page anchors. Glossary links. |
| https://mwm.ai/glossary | Search ("Search 222 terms"). Category buttons filter the list in place: All terms, ASO, Rankings, Monetization, Attribution, UA, Analytics. Terms open `/glossary/:slug`. |
| Glossary `:slug` | Definition. Related-term links. FAQ questions expand in place. Example: `/glossary/aso`. |
| https://mwm.ai/apps/ | Directory home. Cluster links to `/tags/:slug`, featured apps to `/apps/:slug/:storeId`, and iPhone Duo to `/apps/iphone-duo`. |
| https://mwm.ai/apps/:slug/:storeId | Public app profile. Not the studio app template. Example captured: `/apps/chatgpt/6448311069`. |
| https://mwm.ai/apps/iphone-duo | Filter buttons: All apps, Optimized, Compatible. Pagination. |
| https://mwm.ai/tags | Search. Pagination. Cards open `/tags/:slug`. |
| Tag `:slug` | Cluster page. Pagination. Example: `/tags/logic-and-brain-puzzles`. |
| https://mwm.ai/rankings/countries | Country and category links, about 262, to `/rankings/countries/:country/devices/:device/categories/:id`. |
| Ranking chart | Example: United States / iPhone / Social Networking. Buttons: United States, Social Networking, iPhone, iPad. FAQ questions expand in place. Changing country or category is a navigation, captured as the opened menu where it is a menu. |
| https://mwm.ai/authors | Author cards open `/authors/:slug`. |
| https://mwm.ai/authors/:slug | Author bio. Example: benjamin-duvivier. |
| https://mwm.ai/data-methodology | Index of method notes. |
| https://mwm.ai/data-methodology/:slug | Method page. Example: `/data-methodology/nass`. Siblings in the global sitemap: app-achievements, app-download-rankings, app-trust-index. |
| https://mwm.ai/aso-tool | FAQ summaries. CTA links to `/sign-up`, which is a 404 ("Page Not Found", Back to Home). Not a login wall. |

## Legal

| Page | Notes |
|---|---|
| https://mwm.ai/privacy-policy | Long text. Links to `/sdk-privacy-policy`. |
| https://mwm.ai/terms-of-service | Long text. Links to `/sdk-terms-of-service`. |
| https://mwm.ai/sdk-privacy-policy | SDK policy. |
| https://mwm.ai/sdk-terms-of-service | SDK terms. |
| https://mwm.ai/legal/ip-dispute | Form: name, email, URL, selects, textarea, checkbox, Submit Dispute. Not filled. Not submitted. |

## Stopped branches

| Control | URL reached | Why the branch stops |
|---|---|---|
| Open MWM Console | https://console.mwm.ai/sign-in?next=home-redirect | Email and password, or Google or Apple. Not entered. No screenshot kept. |
| Build your app, Get MWM AI Pro, Get MWM AI Pro+ | https://create.mwm.ai/sign-in?next=home&next_path=/ | Google, GitHub, or Apple. Not entered. No screenshot kept. |
| Careers | https://mwm.teamtailor.com/#jobs | Leaves mwm.ai. Jobs board, not the marketing system. |
| Featured app sites | edjing.com, colorpop.ai, swipewipe.com, guitartunerpro.net, beatmakerpro.app | Other products. |
| Prompt submit, attachment upload, voice input | Stay on the home composer | Would start creation, upload a file, or request a microphone. |
| IP dispute Submit | Stays on `/legal/ip-dispute` | Form not submitted. |
| Locale mirrors | `/es/`, `/pt/`, `/ko/`, `/it/`, `/de/`, `/fr/`, `/ja/` | Same pages in another language. English only. |
| Catalog rows beyond one example | apps, tags, glossary, articles, rankings, guides, studio apps | Same template. Indexes are captured. |

## Not a page

`https://mwm.ai/sign-up` returns 404. The ASO tool links there. There is no public account form on mwm.ai itself.
