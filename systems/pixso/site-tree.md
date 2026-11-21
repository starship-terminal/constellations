# Pixso public site tree

Mapped from https://pixso.net/ on 2026-11-21 in headless Chromium at 1440×900, before screenshots. English is the captured locale. Footer language links (`/jp/`, `/kr/`, `/ru/`, `/es/`, `pixso.cn`) are recorded and not walked. Blog posts, tips posts, help articles, community files and plugin detail pages are the same templates as their indexes; one of each is captured, the rest are not.

Theme: one light theme. `html` has no `data-theme`. `color-scheme` is `normal`. Body background computed to `rgb(255, 255, 255)`. No theme switch was found.

Consent: no cookie banner mounted on the home page. Cookie policy is a footer page, not an overlay.

## Header (home, desktop)

| Control | Opens |
|---|---|
| Logo "Pixso" | `/` |
| Product (hover) | Menu, not a page. Items below. |
| AI design (hover) | Menu, not a page. Items below. |
| Import from Figma | `/pixso-vs-figma/` |
| Resources & learning (hover) | Menu, not a page. Items below. |
| Enterprise (hover) | Menu, not a page. Items below. |
| Pricing | `/pricing/` |
| Log in | `https://pixso.net/user/login/?redirect_uri=https://pixso.net/app/&from=1&product=pixso&ux_mode=redirect`. Wall. Branch stopped. Password was not submitted. |
| Get started | Same login URL. Wall. Branch stopped. |

`https://pixso.net/signin` returns 404. The live wall is `/user/login/`.

## Product menu

| Item | Opens |
|---|---|
| Pixso (workspace) | Login wall (`/user/login/?redirect_uri=…/app/`). Stopped. |
| UI design & collaboration | `/ui-design-collaboration/` |
| Prototyping | `/prototyping/` |
| Pixso whiteboard | `/pixso-whiteboard/` |
| Design system | `/design-system/` |
| Pixso AI | `/pixso-ai-generator/` |
| Pixso MCP | `/pixso-mcp/` |
| Paico AI builder | `https://paico.ai/` (external). Not captured. |
| UX design | `/ux-design-collaboration/` |
| Interface design | `/ui-design-collaboration/` |
| Web design | `/web-designing/` |
| Start designing for free | Login wall. Stopped. |
| Explore Pixso AI | `/pixso-ai-generator/` |
| Free plan | `/pricing/` |

## AI design menu

| Item | Opens |
|---|---|
| Pixso AI | `/pixso-ai-generator/` |
| AI design generator | `/ai-design-generator/` |
| AI UI generator | `/ai-ui-generator/` |
| AI website generator | `/ai-webpage-generator/` |
| AI app generator | `/ai-app-generator/` |
| Pixso MCP | `/pixso-mcp/` |
| Set up remote MCP | `/developer/en/mcp/remote-mcp.html` |
| Close navigation menu | Closes the menu. |

## Resources & learning menu

| Item | Opens |
|---|---|
| Design assets | `/community/home?classify=file` |
| Component libraries | `/community/home?classify=library` |
| Plugins | `/plugins/` |
| Help center | `/help/en/` |
| Design tips | `/tips/` |
| What's new | `/releases/` |
| Articles | `/articles/` |
| Developer docs | `/developer/en/` |

## Enterprise menu

| Item | Opens |
|---|---|
| Enterprise plan | `/pixso-enterprise/` |
| Private deployment | `/private-deployment/` |
| Contact us | `/contact-us/` (form present; not submitted, no fields typed) |
| Close navigation menu | Closes the menu. |
| Start designing for free | Login wall. Stopped. |

## Pricing

`/pricing/` has no month/year toggle in the header controls. Seat comparison and plan comparison are on the page. Enterprise in the header still opens the Enterprise menu. Plan CTAs that say Try for free or Get started go to the login wall. Stopped.

Related page, footer and sitemap only: `/pixso-lifetime-plan/`.

## Footer

| Control | Opens |
|---|---|
| Get started | Login wall. Stopped. |
| Language: `/`, `/jp/`, `/kr/`, `/ru/`, `/es/`, `https://pixso.cn/` | Locale homes. English `/` captured. Other locales not walked. |
| Social (Facebook, X, YouTube, Instagram, Pinterest, Discord, Telegram) | External. Not captured. |
| Product links | Same product pages as the Product menu, plus `/web-designing/`. |
| AI links | Same AI pages as the AI design menu. |
| Company: Contact us, About us, Reviews | `/contact-us/`, `/about/`, `/reviews/` |
| Legal: Privacy, Cookie, Refund, Terms, License, Subscription | `/private-policy/`, `/cookie-policy/`, `/refund-policy/`, `/terms-conditions/`, `/license-agreement/`, `/subscription-terms/` |
| Download Pixso | `/download/` |
| Help, Developer docs, Articles, Tips, What's new, Plugins | Same as Resources menu. |
| Comparisons: Figma, Adobe XD, Axure, Sketch, InVision | `/pixso-vs-figma/`, `/pixso-vs-adobe-xd/`, `/pixso-vs-axure/`, `/pixso-vs-sketch/`, `/pixso-vs-invision/` |

## Second shell (community, plugins, developer)

`/community/home`, `/plugins/`, and `/developer/en/` paint a different header from the marketing site. Body overflow is hidden. The page scrolls inside `#app`.

| Control | Opens |
|---|---|
| Products | Menu. Not opened (Sign up sits beside it; that branch was not followed). |
| Resources Community | Menu. Design assets and libraries are the classify links already mapped. |
| Pricing | `/pricing/` |
| Download | `/download/` |
| Business Service | Menu. Enterprise and private deployment pages already mapped. |
| Support | Menu. Help center already mapped. |
| English | Locale menu. English captured. Other locales not walked. |
| Sign up | Auth wall. Not clicked. |
| Search on community and plugins | Field visible. Not typed into. |
| Category chips (All, Icon, Text, Image, Works, Resources Library) | Filters on the same page. Not each captured. |
| Install | Would enter the editor or an auth step. Not clicked. |
| A resource card | `/community/file/<id>`. One file captured (Ant design). |
| A plugin row | `/plugins/?id=<id>`. Phosphor Icons was requested. The detail document stayed 900px tall. |

## Other public pages (sitemap, not in the header)

| Page | Notes |
|---|---|
| `/brainstorming/` | Product page. |
| `/ai-service-terms/` | Legal. |
| `/articles/page/2/` and later | Pager on `/articles/`. Page 1 captured. Later pages are the same list template. |
| `/tips/` posts | Same article template. Index captured. |
| `/help/en/guide/`, `/help/en/design/`, `/help/en/base/`, `/help/en/board/`, `/help/en/question/`, `/help/en/video/` | Help sections. Index plus one guide section captured. |
| `/help/en/` search field | Placeholder "Search features, questions, or tutorials". Not typed into. |
| `/developer/en/d2c/quick-start.html`, `/developer/en/plugin-api/guide/introduction.html` | Docs templates. One developer page captured. |
| `/community/file/…` | Published resource files. One file page captured. |
| `/plugins/?id=…` | Plugin detail. One detail captured. |
| `/plugins/` Sign Up | Auth control. Not clicked. |

## Phone (390×844)

Header shows the logo, Log in, Get started, and a button labelled "Open navigation menu". Log in and Get started are the same login wall. The menu button opens the same Product, AI design, Resources and Enterprise groups.

## Stopped branches

| Control | URL | Why |
|---|---|---|
| Log in, Get started, Start designing for free, Try for free, Try Pixso AI, Create with AI, Product "Pixso" workspace | `https://pixso.net/user/login/` (often with `redirect_uri` to `/app/`) | Email and password, or Google, NAVER, or SSO. Not typed. Not clicked. |
| `/signin` | 404 | Known missing wall. |
| `/app/`, `/editor/`, `/share/` | robots.txt Disallow | Signed-in app. Not opened. |
| Contact form | `/contact-us/` | Name, email, OS, browser, file link, file upload, message. Not filled. Not submitted. |
| Google, NAVER, SSO | on the login page | Not clicked. |
