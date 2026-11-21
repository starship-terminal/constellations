# Editor X public site tree

Mapped on 2026-11-21 from [https://www.editorx.com/](https://www.editorx.com/) in headless Chromium, signed out. Catalog name: Editor X. Domain: editorx.com. The product now serves Wix Studio.

Nothing in this map was submitted. Login and signup walls are recorded in [login-review.json](login-review.json). The signed-in Studio editor is out of scope.

## Redirect

| Request | Status | Lands on |
|---|---|---|
| `https://www.editorx.com/` | 301 | `https://www.wix.com/studio` |
| `https://www.editorx.com/login` | 301 | `https://www.wix.com/studio` (marketing home, not a login form) |
| `https://www.editorx.com/pricing` | 200, no redirect | Same URL. The page paints "Couldn't load Premium plans due to a technical issue". |

Deep editorx.com paths that still 301 keep their tail on `wix.com/studio` when that path exists. Pages that have no editorx.com path left (design, plans, templates) are linked from the Studio header as `www.wix.com/studio/...`.

Shots: [home after redirect, desktop](screenshots/interactions/home-light-redirect-desktop.png), [phone](screenshots/interactions/home-light-redirect-phone.png), [pricing error](screenshots/interactions/pricing-error-desktop.png).

## How a control was recorded

A control is a button, link, menu, or in-page control that was visible on a page this pass opened. "Opens" is the URL after navigation, or the panel the control revealed, without following a login wall.

Widths: desktop 1440 x 900 at 1x, phone 390 x 844 at 2x. Measured `innerWidth` matched those viewports.

Cookie dialog: not mounted on the home load. The hide pass matched no OneTrust, iubenda, or fixed cookie overlay, and clicked nothing. No consent was accepted.

## Header

Present on `https://www.wix.com/studio` after the redirect. Desktop shows the wordmark, three menus, Pricing, a language globe, Log In, and Start Creating. Phone replaces the menus with an "open navigation" button. Start Creating stays in the bar.

| Control | Kind | Opens | Followed |
|---|---|---|---|
| Wix Studio wordmark | link | `https://www.wix.com/studio` | yes |
| Product | button, desktop menu | Dropdown. Click and hover in this pass left the panel at 0px height, so the open desktop panel was not photographed. The same items are in the DOM and open on the phone drawer. | phone only |
| Resources | button, desktop menu | Same as Product. | phone only |
| Enterprise | button, desktop menu | Same as Product. | phone only |
| Pricing | link | `https://www.wix.com/studio/plans` | yes |
| language selector, english selected | button | Language list. Desktop click did not paint a visible list in the screenshot. Phone drawer did. | phone |
| Log In | link | `https://users.wix.com/signin?loginDialogContext=login` | stopped at the empty wall |
| Start Creating | link | `https://users.wix.com/signin?loginDialogContext=signup` | stopped at the empty signup wall |
| open navigation | button, phone | Navigation drawer | yes |
| close navigation | button, inside the drawer | Closes the drawer | yes |

Phone drawer, closed sections: [nav-drawer-phone.png](screenshots/interactions/nav-drawer-phone.png).

### Product menu

Opened by the Product row in the phone drawer. Desktop button is the same control; its panel did not paint.

| Item | Opens |
|---|---|
| Design | `https://www.wix.com/studio/design` |
| Business solutions | `https://www.wix.com/studio/business-solutions` |
| CMS | `https://www.wix.com/studio/cms` |
| Development | `https://www.wix.com/studio/developers` |
| Ecommerce | `https://www.wix.com/studio/ecommerce` |
| SEO | `https://www.wix.com/studio/marketing/seo` |
| AI features | `https://www.wix.com/studio/ai` |
| Management tools | `https://www.wix.com/studio/management-tools` |
| Marketing integrations | `https://www.wix.com/studio/marketing/integrations` |
| View other solutions | `https://www.wix.com/` (Wix home, outside the Studio tree) |

Shot: [nav-product-phone.png](screenshots/interactions/nav-product-phone.png).

### Resources menu

| Item | Opens |
|---|---|
| Community | `https://www.wix.com/studio/community` |
| Inspiration | `https://www.wix.com/studio/inspiration` |
| SEO Hub | `https://www.wix.com/seo/learn` (outside `/studio`) |
| Partner Program | `https://www.wix.com/studio/partner-program` |
| Templates | `https://www.wix.com/studio/templates` |
| Developer docs | `https://dev.wix.com/docs` (outside the marketing tree; not walked) |
| Marketing Resources | `https://www.wix.com/studio/marketing/resources` |
| Blog | `https://www.wix.com/studio/blog` |
| Help Center | `https://support.wix.com/en/wix-studio` (support host; not walked) |

Shot: [nav-resources-phone.png](screenshots/interactions/nav-resources-phone.png).

### Enterprise menu

| Item | Opens |
|---|---|
| Learn about Wix Enterprise | `https://www.wix.com/studio/enterprise` |
| Company Websites | `https://www.wix.com/studio/enterprise/company-websites` |
| Partner Network Websites | `https://www.wix.com/studio/enterprise/partner-websites` |
| Customer Websites | `https://www.wix.com/studio/enterprise/customer-websites` |
| Performance | `https://www.wix.com/studio/infrastructure/reliability-performance` |
| Security | `https://www.wix.com/studio/infrastructure/security` |
| Top Enterprise Features | `https://www.wix.com/studio/features` |
| Talk to Sales | `https://www.wix.com/studio/enterprise/contact-sales` (public page; form not submitted) |

Shot: [nav-enterprise-phone.png](screenshots/interactions/nav-enterprise-phone.png).

### Language

The globe button's accessible name is "language selector, english selected". On the phone drawer, the English row opens:

| Item | Opens | Followed |
|---|---|---|
| Deutsch | `https://users.wix.com/wix-users/auth/setLanguage?language=de` then `https://de.wix.com/studio` | no |
| Español | same host, `language=es`, then `https://es.wix.com/studio` | no |
| Français | `language=fr`, then `https://fr.wix.com/studio` | no |
| 日本語 | `language=ja`, then `https://ja.wix.com/studio` | no |
| Português | `language=pt`, then `https://pt.wix.com/studio` | no |

Those links set a language cookie through the users host. They were not followed. Shot: [language-phone.png](screenshots/interactions/language-phone.png).

## Footer

The home page ends in a near-black footer. "Back to top" is a button that scrolls to the top. Social marks leave the Studio tree. Shot: [footer-desktop.png](screenshots/interactions/footer-desktop.png).

| Column | Control | Opens |
|---|---|---|
| Product | Design | `/studio/design` |
| Product | Development | `/studio/developers` |
| Product | Enterprise | `/studio/enterprise` |
| Product | Figma to Wix Studio | `/studio/figmatowixstudio` |
| Product | AI Features | `/studio/ai` |
| Product | Visual Sitemap | `/studio/visual-sitemap` |
| Product | Business Solutions | `/studio/business-solutions` |
| Product | Ecommerce | `/studio/ecommerce` |
| Product | CMS | `/studio/cms` |
| Product | Management Tools | `/studio/management-tools` |
| Product | SEO | `/studio/marketing/seo` |
| Product | Marketing Integrations | `/studio/marketing/integrations` |
| Product | Security | `/studio/infrastructure/security` |
| Product | Reliability & Performance | `/studio/infrastructure/reliability-performance` |
| Product | Top Features | `/studio/features` |
| Resources | Community | `/studio/community` |
| Resources | Forum | `https://forum.wixstudio.com/` (not walked) |
| Resources | Inspiration | `/studio/inspiration` |
| Resources | Marketing Resources | `/studio/marketing/resources` |
| Resources | Blog | `/studio/blog` |
| Resources | Partner Program | `/studio/partner-program` |
| Resources | Help Center | `https://support.wix.com/en/wix-studio` |
| Resources | Pricing | `/studio/plans` |
| Resources | Brand Guidelines | `/studio/about/brand-guidelines` |
| More from Wix | Website Builder, Website Design, Website Templates, Ecommerce Website, Appointment Scheduling, Portfolio Website, Blog Website, Domain Registration | `www.wix.com` paths outside `/studio` |
| Company | About Wix, Contact Us, Press & Media, Accessibility Statement, Site Map | `www.wix.com/about` or press, outside `/studio` |
| Company | About Wix Studio | `/studio/about-us` |
| Company | Careers | `https://careers.wix.com/` |
| Legal | Terms of Use | `https://www.wix.com/about/terms-of-use` |
| Legal | Privacy Policy | `https://www.wix.com/about/privacy` |
| Social | YouTube, X, Instagram, Facebook, TikTok | those hosts, not walked |

## Login and signup walls

| Control | Opens | Stop |
|---|---|---|
| Log In, header and drawer | `https://users.wix.com/signin` | Empty email field. Not typed. Not submitted. Identity providers not clicked. |
| Start Creating, header, drawer, and in-page "Start creating" | `https://users.wix.com/signin` with `loginDialogContext=signup`, which redirects to `https://users.wix.com/signin/signup/password` | Empty email field. No password field was visible. Not typed. Not submitted. |
| `https://www.editorx.com/login` | `https://www.wix.com/studio` | No wall. Recorded as a redirect. |

Shots: [login desktop](screenshots/interactions/login-wall-desktop.png), [login phone](screenshots/interactions/login-wall-phone.png), [signup desktop](screenshots/interactions/signup-wall-desktop.png).

## Pages reached

The crawl started at `https://www.editorx.com/` and followed in-tree links on `www.wix.com/studio` up to 80 page loads. 67 pathnames were distinct. A further queue of inspiration case studies and academy lessons was left unwalked after that cap. Each of those is the same template as the case studies and lessons already opened. Login links on every page were counted and not followed (118 of them pointed at `users.wix.com/signin`).

### Studio marketing

| Path | Heading | In-page controls |
|---|---|---|
| `/studio` | Design with impact Deliver at scale | Header menus above. In-page "Start creating" opens the signup wall. "Get more inspo" opens `/studio/inspiration`. Expand buttons reveal more copy on the page. Play-video buttons start public demos. |
| `/studio/design` | Pure web design, max productivity | In-page tabs: Sound, Lighting, Security. |
| `/studio/business-solutions` | Full-stack business solutions for any industry | Tabs: eCommerce, Bookings, Events, Restaurants, Hotels, App Builder, Multilingual, Blog, Members Area, Payments, CRM, Pricing Plans. |
| `/studio/business-solutions/home` | Full-stack business solutions for any client | Tabs: eCommerce, Bookings, Events, Restaurants, CMS, Blog, Multilingual, Payments, Pricing Plans, Members Area, CRM. |
| `/studio/cms` | A powerful CMS to build content-rich sites, smarter | Header and footer only. |
| `/studio/developers` | For devs who build websites | Links into the developer subpages. |
| `/studio/developers/web-development` | WEBSITE DEVELOPMENT | Header and footer. |
| `/studio/developers/build-wix-apps` | Open your apps to millions | Header and footer. |
| `/studio/developers/mcp-server` | The Wix MCP Server | Tabs: eCommerce, Bookings, Payments, Events, Pricing Plans, Blog, CMS, CRM, Restaurants. |
| `/studio/ecommerce` | Build exceptional stores | Link to book a demo. |
| `/studio/ecommerce/bookademo` | Book a demo with our ecomm experts | Form present. Not filled. Not submitted. |
| `/studio/marketing/seo` | SEO by design | Tabs: SEO pros and agencies, Content marketers. |
| `/studio/ai` | AI that transforms how teams work | Header and footer. |
| `/studio/management-tools` | Power your agency's productivity | Header and footer. |
| `/studio/marketing/integrations` | Native integrations that do the heavy lifting | Header and footer. |
| `/studio/marketing/resources` | Resources for marketers | Header and footer. |
| `/studio/features` | Smart, flexible tools for agencies & enterprises | Also opened with `?category=enterprise` from the Enterprise menu. |
| `/studio/plans` | Choose the right Studio plan for each project | Plan cards. Start Creating on a card opens the signup wall. No billing toggle was clicked. Shot: [plans-desktop.png](screenshots/interactions/plans-desktop.png). |
| `/studio/templates` | All Responsive Templates | Search field "Search templates...". Focused, not submitted. Category chips: Landing Page, Portfolio, Marketing, Ecommerce, Wireframes, Minimal. Browse menus: Main, Type, Industry, Features, Style. Shots: [filters](screenshots/interactions/templates-filters-desktop.png), [search focus](screenshots/interactions/templates-search-focus-desktop.png). |
| `/studio/inspiration` | Turn inspiration into creative fuel | Filters: Type, Feature, Style. Sort: Recent, Popular. "Showcase your site" opens the submit page. "Start creating" opens the signup wall. Shot: [inspiration-desktop.png](screenshots/interactions/inspiration-desktop.png). |
| `/studio/inspiration/submit-form` | Inspire the industry with your creation | Form present. Not filled. Not submitted. |
| `/studio/figmatowixstudio` | Bring your website designs to life | Header and footer. |
| `/studio/visual-sitemap` | VISUAL SITEMAP AND WIREFRAME GENERATOR | Header and footer. |
| `/studio/for-agencies` | The website building platform for agencies | Header and footer. |
| `/studio/partner-program` | PARTNER PROGRAM | Header and footer. |
| `/studio/about-us` | The website building platform for agencies and freelancers | Header and footer. |
| `/studio/about/brand-guidelines` | Wix Studio brand guidelines | Header and footer. |
| `/headless` | Every business solution your AI project needs | Linked from the developers page. Outside `/studio`, still on www.wix.com. |

### Enterprise

| Path | Heading | In-page controls |
|---|---|---|
| `/studio/enterprise` | The enterprise web platform | Links to the three website types and contact sales. |
| `/studio/enterprise/company-websites` | Get enterprise web scale without the big tradeoffs | Header and footer. |
| `/studio/enterprise/partner-websites` | Own the web experience | Header and footer. |
| `/studio/enterprise/customer-websites` | Grow beyond your core business | Header and footer. |
| `/studio/enterprise/contact-sales` | Talk to our enterprise team | Form present. Not filled. Not submitted. |
| `/studio/infrastructure/reliability-performance` | Fast. Resilient. Infinitely scalable. | Header and footer. |
| `/studio/infrastructure/security` | Focus on your projects. Security is on us. | Header and footer. |

### Community, academy, blog

| Path | Heading | In-page controls |
|---|---|---|
| `/studio/community` | Wix Studio Community | Links to league, code of conduct, events. |
| `/studio/community/studio-league` | Scouted. Certified. Lead the field. | Search field. Not submitted. |
| `/studio/community/code-of-conduct` | (no h1 read) | Header and footer. |
| `/studio/community/leaders-old` | Lead today, transform tomorrow | Header and footer. |
| `/studio/community/leaders-apply/eventsleader` | Apply to be an Events Leader | Form present. Not filled. Not submitted. |
| `/studio/academy` | Learn the Wix Studio way | Search button. Not submitted. |
| `/studio/academy/library` | Library | Search field. Not submitted. |
| `/studio/academy/certifications` | WIX STUDIO CERTIFICATIONS | Search field. Not submitted. |
| `/studio/academy/event` | Find your next event | Opened with `filter=online` and `filter=inPerson`. Search field. Not submitted. |
| `/studio/academy/courses/wix-studio-essentials-course` | Wix Studio Essentials | Tabs: About, In this lesson, Transcript. Search field. Not submitted. |
| `/studio/academy/webinars/discover-the-wix-studio-editor` | Discover the Wix Studio Editor | Search field. Not submitted. |
| `/studio/academy/webinars/how-to-build-dynamic-content-with-wix-studio` | How to build dynamic content with Wix Studio | Search field. Not submitted. |
| `/studio/academy/webinars/customize-product-pages-for-conversion-driven-design` | Customize product pages for conversion-driven design | Search field. Not submitted. |
| `/studio/academy/webinars/designing-and-optimizing-the-category-page-with-wix-studio` | Designing and optimizing the category page with Wix Studio | Search field. Not submitted. |
| `/studio/academy/webinars/extend-ecommerce-functionalities-with-wix-studio's-open-platform-apis-and-spis` | Extend eCommerce functionalities | Search field. Not submitted. |
| `/studio/blog` | The blog for creative professionals | "Open search box" button. The click in this pass did not paint an open field. Shot of the closed state: [blog-search-closed-desktop.png](screenshots/interactions/blog-search-closed-desktop.png). Subscribe was not clicked. |
| `/studio/blog/category/development` | The blog for creative professionals | Same search control. |

### Inspiration case studies opened

Each is a public case-study page. External "visit site" links leave the tree and were not walked. Start creating on these pages opens the signup wall.

`/studio/inspiration/site/interactive-studio`, `a-cosmic-scroll-journey`, `visual-identity`, `praagya`, `anzo.studio™`, `bolt-—-designs`, `eliran-vahdi`, `the-museum-of-adventures`, `sunday-best`, `thjnk`, `vanyadoing`, `lilian-cannam-kindergarten`, `chain-labs`. Design-inspiration variants: `/studio/design/inspiration/space`, `/studio/design/inspiration/blendmode` (tabs: I BACK-TO-BACK MEETING, II ENDLESS REVISIONS, III NOTIFICATIONS FLOOD, IV PURSUIT OF PERFECTION).

## Not captured

| Control | Why |
|---|---|
| Desktop Product, Resources, and Enterprise panels | Click, hover, and a forced click left the panel at 0px height. Contents were read from the same anchors the phone drawer opens, and photographed there. |
| Desktop language list | The globe click did not paint a visible list. The phone drawer did. |
| Blog search field | The Open search box click did not paint an input. |
| Cookie dialog | Did not mount. Not accepted. |
| Identity providers | Seen on the walls. Not clicked. |
| Forms | Contact sales, book a demo, events-leader apply, inspiration submit, newsletter. Opened when public. Not filled. Not submitted. |
| Remaining inspiration case studies and academy lessons | Same templates as the ones opened. Crawl stopped at 80 page loads, with 20 URLs still queued. |
| Signed-in Studio editor | Out of scope. Every path into it is a login or signup wall. |
