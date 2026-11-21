# Runway public site tree

Mapped on 2026-11-21 from the main page before any screenshots. Playwright, headless Chromium, signed out. `https://runwayml.com/` returns 200 and lands on `https://runway.com/`. No form was submitted. No password, code, Google, or Apple control was used.

The marketing site is light only (`html` class `bg-white`, `color-scheme: normal`, no `data-theme`). Dark mode is not a public toggle.

## Header

Desktop (1440). The wordmark goes to `/`. These controls sit in the header:

| Control | Opens | Kind |
|---|---|---|
| Runway home | `https://runway.com/` | page |
| Creative (hover, `aria-expanded`) | Mega menu. Click follows the link to `/product` | menu, then page |
| Dev (hover) | Mega menu. Click follows the link to `https://dev.runwayml.com/` | menu, then page |
| Robotics (hover) | Mega menu. Click follows the link to `/product/robotics` | menu, then page |
| Research (hover) | Mega menu. Click follows the link to `/research` | menu, then page |
| Resources (hover) | Mega menu. Click follows the link to `/resources` | menu, then page |
| Enterprise (hover) | Mega menu. Click follows the link to `/enterprise` | menu, then page |
| Pricing | `/pricing` | page |
| Enterprise Sales | `/enterprise-contact` | page (form, not submitted) |
| Login | `https://app.runwayml.com/login` then `https://auth.runwayml.com/interaction/…` | login wall. Stop. |
| Try Runway | `https://app.runwayml.com/` | app wall. Stop. |
| ENGLISH (`aria-label` Change language) | Menu: English, 日本語, 한국어, Français, Português (BR). Not switched. | menu |
| Dismiss banner | Hides the top promo strip ("Enterprises get up to 2 months…") | interaction |
| Cookie Settings / Your privacy choices | OneTrust preferences. Hidden, never clicked (a consent button can POST). | dialog, not opened |

Phone (390). A **Menu** button (`aria-label` Menu, `aria-expanded` false) opens a sheet with Login, Try Runway, Enterprise Sales, Pricing, Get Started, and the same product links. Login and Try Runway are the same walls.

## Creative menu (hover)

| Item | Opens |
|---|---|
| Overview | `/product` |
| Agent | `/product/agent` |
| Runway Ads | `/product/ads` |
| App Studio | `/app-studio` |
| Pricing | `/pricing` |
| iOS app | App Store (off site) |
| Android app | Play Store (off site) |
| ChatGPT plugin | `/mcp/chatgpt` |
| MCP | `/mcp` |
| Plugins | `/plugins` |
| Text to video | `/product/ai-video-generator` |
| Text to image | `/product/ai-image-generator` |
| Image to video | `/product/ai-video-generator` |
| Expand images | `/product/ai-photo-editor` |
| Edit with natural language | `/product/aleph-2` |
| Product reshoot | `/apps/reshoot-product` |
| Convert to HDR | `/product/ruby` |
| Localize content | `/product/use-cases` |
| Upscale video | `/apps/upscale-video` |
| Create slides | `/product` |
| Try today | `https://app.runwayml.com/` wall |

## Dev menu (hover)

| Item | Opens |
|---|---|
| Explore | `https://dev.runwayml.com/` |
| Models | `https://dev.runwayml.com/models` |
| Model licensing | `/model-licensing` |
| Pricing | `/pricing?tab=dev` |
| Model Router | `https://docs.dev.runwayml.com/model-routers/` |
| Workflows | `/workflows` |
| Recipes | `https://dev.runwayml.com/recipes/product_ad` |
| Characters | `/product/characters` |
| Documentation | `https://docs.dev.runwayml.com/` |
| Get an API key | `https://dev.runwayml.com/` |

## Robotics menu (hover)

| Item | Opens |
|---|---|
| Praxis-1 | `/product/praxis` |
| Overview | `/product/praxis` |
| Announcement | `/news/company-news/praxis-1-is-now-available` |
| Technical blog | `/research/praxis-1-video-pretraining-to-robot-control` |
| Contact our robotics team | `/product/robotics/contact` (form, not submitted) |

## Research menu (hover)

| Item | Opens |
|---|---|
| Research News | `/news/research` |
| Publications | `/research/publications` |
| RNA Sessions | `/research/rna-sessions` |
| Optimization | `/optimization` |
| Gen-4.5 | `/research/introducing-runway-gen-4.5` |
| Aleph 2.0 | `/product/aleph-2` |
| Ruby | `/product/ruby` |
| Act-Two | `/research/introducing-act-one` |
| Solaris | `/news/research/introducing-solaris` |
| Characters | `/product/characters` |
| Robotics | `/product/robotics` |
| World Simulation | `/research/introducing-gwm-worlds-2` |

## Resources menu (hover)

| Item | Opens |
|---|---|
| Academy | `https://academy.runwayml.com/` |
| Help Center | `https://help.runwayml.com/hc/en-us` |
| Ways to Use Runway | `https://academy.runwayml.com/ways-to-use-runway` |
| News | `/news` |
| Changelog | `/changelog` |
| AI Festival | `https://aif.runwayml.com/` |
| AI Summit | `https://summit.runwayml.com/` |
| About Us | `/about` |
| Careers | `/careers` |
| Safety | `/safety` |
| Verify Content Credentials | `/safety/verify` |

## Enterprise menu (hover)

| Item | Opens |
|---|---|
| Runway Creative | `/product` |
| Runway Ads | `/product/ads` |
| App Studio | `/product/app-studio` |
| Runway Dev | `https://dev.runwayml.com/` |
| Runway MCP | `/mcp` |
| Media and entertainment | `/solutions/industry/media-entertainment` |
| Marketing and advertising | `/solutions/industry/marketing-advertising` |
| Product and design | `/solutions/industry/product-design` |
| Gaming and interactive | `/solutions/industry/gaming-interactive` |
| Professional services | `/solutions/industry/professional-services` |
| Ideation and concepting | `/solutions/use-cases/ideation-concepting` |
| Content creation | `/solutions/use-cases/content-creation` |
| Enhancement and editing | `/solutions/use-cases/enhancement-editing` |
| Marketing and distribution | `/solutions/use-cases/marketing-distribution` |
| Security and Admin | `/data-security` |
| Model licensing | `/model-licensing` |
| Services and support | `https://academy.runwayml.com/` |
| Customer stories | `/news/customers` |
| News and partnerships | `/news` |
| Contact sales | `/enterprise-contact` |

## Home page interactions (no navigation)

| Control | What it does |
|---|---|
| Runway Creative / Runway Dev / Runway Robotics | Section tabs on the home page. Stay on `/`. |
| How Runway is Used, Create with Agent, Build your own Workflows, Enterprise-grade, The World's Best Models | In-page section jumps or tabs. Stay on `/`. |
| See terms | `/code-terms/enterprise-bonus-terms` |
| Contact sales | `/enterprise-contact` |

## Pricing interactions

`/pricing` has Individual, Team & Enterprise, and API audience tabs, plus Monthly and Yearly billing toggles. Get Started and similar CTAs go to `app.runwayml.com` (wall). No checkout was opened.

## Login and app wall

Reached by Login, Try Runway, Get Started, and in-product generate links.

| URL | What it shows | Action |
|---|---|---|
| `https://app.runwayml.com/login` | Redirects to auth | Stop |
| `https://auth.runwayml.com/interaction/…` | Sign In. Fields: Username or Email, Password. Buttons: Log in, Continue with Google, Continue with Apple. Link: Sign up. | Stop. Password not typed. Google and Apple not clicked. No account created. |
| `https://app.runwayml.com/` | App entry | Stop |
| `https://app.runwayml.com/generate`, `/characters`, `/video-tools/ai-tools/agent`, `/ai-tools/generate` | Same app wall | Stop |

`https://auth.runwayml.com/` with no path redirected back to `https://runway.com/` (200). The signed-in product (editor, projects, billing, onboarding) is behind this wall.

## Forms (not submitted)

| Page | Fields | Submit control |
|---|---|---|
| `/enterprise-contact` | first name, last name, business email, company, a select, job title, phone, a select, product checkboxes, a textarea | Submit. Not clicked. Fields not filled. |
| `/product/robotics/contact` | name, email, company, subject, message, a checkbox | Send Message. Not clicked. |
| `/rewards` | Application form (name, contact, profile). | Not filled. |
| `/educators` | Education discount request. | Not filled. |

## Public pages that loaded (200)

Marketing (`runway.com`): `/`, `/product`, `/product/agent`, `/product/ads`, `/product/app-studio` (menu), `/plugins`, `/mcp`, `/mcp/chatgpt`, `/product/ai-video-generator` (menu), `/product/ai-image-generator` (menu), `/product/ai-photo-editor` (menu), `/product/aleph-2`, `/product/ruby`, `/product/characters`, `/product/use-cases` (menu), `/apps/reshoot-product` (menu), `/apps/upscale-video` (menu), `/product/robotics`, `/product/praxis`, `/product/robotics/contact`, `/product/builders`, `/research`, `/research/publications`, `/research/rna-sessions` (menu), `/optimization` (menu), `/research/introducing-runway-gen-4.5`, `/research/introducing-act-one`, `/research/introducing-gwm-worlds-2`, `/research/introducing-runway-gwm-1`, `/research/introducing-general-world-models`, `/research/praxis-1-video-pretraining-to-robot-control` (menu), `/resources`, `/enterprise`, `/pricing`, `/enterprise-contact`, `/use-cases`, `/team-plan`, `/workflows`, `/model-licensing` (menu), `/data-security`, `/solutions/industry/*` and `/solutions/use-cases/*` (menu), `/educators`, `/news`, `/news/customers`, `/news/research`, `/news/company-news/runway-ads`, `/news/company-news/praxis-1-is-now-available` (menu), `/news/company-news/runway-for-adobe`, `/news/introducing-aleph-2-and-edit-studio`, `/news/introducing-runway-agent`, `/changelog`, `/about`, `/careers`, `/safety`, `/safety/verify`, `/safety/usage-policy`, `/brand-guidelines`, `/studios`, `/creative-partners-program`, `/rewards`, `/gen48`, `/terms-of-use`, `/privacy-policy`, `/code-terms/enterprise-bonus-terms`. Footer also names `/coc`, which redirected to `/safety/usage-policy`.

Other public hosts that loaded:

| Host | What it is |
|---|---|
| `dev.runwayml.com` | Developer marketing: `/`, `/models`, `/recipes/product_ad` |
| `docs.dev.runwayml.com` | API docs: `/`, `/model-routers/` |
| `academy.runwayml.com` | Academy home, `/meetups`, `/ways-to-use-runway` (menu) |
| `help.runwayml.com/hc/en-us` | Help Center |
| `aif.runwayml.com` | AI Festival |
| `summit.runwayml.com` | AI Summit |
| `status.runwayml.com` | Status page |
| `diffuse.runway.com` | Talent Network (`talent.runwayml.com` redirected here) |

Off-site, not captured: App Store, Play Store, Hugging Face, GitHub, arXiv, X, Instagram, YouTube, Discord, OneLink app banner.

## Capture set

Screenshots cover the public shell and the pages a visitor reaches from the header, the six hover menus, the footer, and the home section tabs, at 1440x900 and 390x844. Article indexes are captured; every article in `/news` and `/resources` is not. Signed-in product states are the wall above.
