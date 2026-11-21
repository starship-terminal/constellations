# Elementor public site tree

Mapped on 2026-11-21 from the signed-out site, in headless Chromium, starting at [https://elementor.com/](https://elementor.com/). Desktop shots are 1440 x 900. Phone shots are a 390 CSS viewport at 2x (780 x 1688 PNG). Cookiebot did not paint a dialog on these loads. No consent button was pressed. Login, signup, checkout, identity providers, and every form submit were not followed.

Shots live in [screenshots/tree/](screenshots/tree/).

## How the chrome works

The marketing header is one Elementor menu (`nav.e-n-menu`) on every English marketing page. Products is the only item that opens a panel. Agency, Enterprise, Pricing, and App Builder are links. Log in and Get started leave the public site.

| Control | Kind | Opens | Shot |
|---|---|---|---|
| Logo | link | [https://elementor.com/](https://elementor.com/) | [home default](screenshots/tree/home-light-default.png) |
| Products | button, `.e-n-menu-title` | Mega menu panel, same page | [desktop products](screenshots/tree/home-light-menu-products.png), [phone products](screenshots/tree/mobile-home-light-products.png) |
| Agency | link | [https://elementor.com/solutions/agency/](https://elementor.com/solutions/agency/) | visited |
| Enterprise | link | [https://elementor.com/solutions/enterprise/](https://elementor.com/solutions/enterprise/) (same document as `/solutions/enterprises/`) | visited |
| Pricing | link | [https://elementor.com/pricing/](https://elementor.com/pricing/) | [pricing](screenshots/tree/pricing-light-default.png) |
| App Builder | link | [https://sticklight.com/elementor/](https://sticklight.com/elementor/) with Elementor campaign query | external, not opened |
| En | link, `href="#"` | Weglot list is in the DOM (`English`, `Deutsch`, `Español`, `Français`, `Italiano`, `Português`, `Nederlands`) but the desktop dropdown measured 0 x 0 after the click | not a visible desktop open; [phone language](screenshots/tree/mobile-home-light-language.png) |
| Log in | link | [https://my.elementor.com/login/](https://my.elementor.com/login/) | wall, branch stopped. [desktop](screenshots/tree/login-wall-light-default.png), [phone](screenshots/tree/mobile-login-wall-light-default.png) |
| Get started | link | [https://my.elementor.com/signup/](https://my.elementor.com/signup/) | recorded, not followed |
| Phone menu button | button, `button.e-n-menu-toggle` | Full-screen drawer | [phone menu](screenshots/tree/mobile-home-light-menu.png) |
| Phone close | button in the drawer | Closes the drawer | same shot, X at the top |

On `/pricing/` the header CTA label is "See plans" and still points at the signup wall. It was not followed.

### Products menu destinations

The panel is a grid, not a navigation to a new route until a row is chosen. Each row is a link.

| Row | Opens |
|---|---|
| Black Friday sale card | [https://elementor.com/pages/bfcm-2026-tof/](https://elementor.com/pages/bfcm-2026-tof/) |
| Get Elementor One | [https://elementor.com/one/](https://elementor.com/one/) |
| Build with AI Editor | [https://elementor.com/products/website-builder/](https://elementor.com/products/website-builder/) |
| Generate pages with AI | [https://elementor.com/ai-page-builder/](https://elementor.com/ai-page-builder/) |
| Build with Elementor MCP | [https://elementor.com/mcp/](https://elementor.com/mcp/) |
| Launch an online store | [https://elementor.com/ecommerce-builder/](https://elementor.com/ecommerce-builder/) |
| Optimize images | [https://elementor.com/products/image-optimizer/](https://elementor.com/products/image-optimizer/) |
| Improve accessibility | [https://elementor.com/products/ally-web-accessibility/](https://elementor.com/products/ally-web-accessibility/) |
| Boost performance | [https://elementor.com/speed-performance/](https://elementor.com/speed-performance/) |
| Manage cookie consent | [https://elementor.com/products/cookie-consent/](https://elementor.com/products/cookie-consent/) |
| Host your website | [https://elementor.com/hosting/](https://elementor.com/hosting/) |
| Register a domain | [https://elementor.com/domains/](https://elementor.com/domains/) |
| Ensure email delivery | [https://elementor.com/products/site-mailer/](https://elementor.com/products/site-mailer/) |
| Manage connected sites | [https://elementor.com/products/manage/](https://elementor.com/products/manage/) |
| Agent Ready Scanner | [https://elementor.com/checker/](https://elementor.com/checker/) |
| Angie | [https://elementor.com/products/angie-ai-for-wordpress/](https://elementor.com/products/angie-ai-for-wordpress/) |

### Language list

Desktop `En` is an anchor with `href="#"`. The list items are real links and were visited as pages:

| Label | Opens |
|---|---|
| English | stays on the current English URL |
| Deutsch | [https://elementor.com/de/](https://elementor.com/de/) |
| Español | [https://elementor.com/es/](https://elementor.com/es/) |
| Français | [https://elementor.com/fr/](https://elementor.com/fr/) |
| Italiano | [https://elementor.com/it/](https://elementor.com/it/) |
| Português | [https://elementor.com/pt-br/](https://elementor.com/pt-br/) |
| Nederlands | [https://elementor.com/nl/](https://elementor.com/nl/) |

The German home repeats the same menu against German paths (`/de/one/`, `/de/preise/`, `/de/products/website-builder/`, and the rest of that cluster). Those German product pages were visited. The other languages were visited at their home URL only.

### Promo dialog

Home auto-opens a Black Friday lightbox (`#elementor-popup-modal-8318268`). Close is `.js-close-popup`. "See discounts" is a link to the sale page. The CTA was not clicked. Shot: [promo dialog](screenshots/tree/home-light-promo-dialog.png). Later page shots hide this dialog with CSS so the page underneath can be read. Hiding is not an accept or a dismiss POST.

### Cookie dialog

Cookiebot's script is on the page (`#Cookiebot`, hidden iframes). No visible consent dialog painted on these loads, so no allow or deny control was available to record. None was pressed.

### Search

The marketing header has no search field. Search lives on two other headers:

| Surface | Control | What it does | Shot |
|---|---|---|---|
| [https://elementor.com/help/](https://elementor.com/help/) | text field "Search for whatever you want to learn..." plus "Get answer" | Submitting would query the knowledge hub. The field was not filled and Get answer was not pressed. | [desktop help](screenshots/tree/help-light-hub.png), [phone help](screenshots/tree/mobile-help-light-default.png) |
| [https://elementor.com/blog/](https://elementor.com/blog/) | "Search ..." field in the blog header | Focused, not submitted. | [blog search](screenshots/tree/blog-light-search.png) |

## Footer

The footer is a dark island (`.dark-mode`) on marketing pages. Shot: [desktop footer](screenshots/tree/home-light-footer.png), [phone footer](screenshots/tree/mobile-home-light-footer.png).

| Control | Opens | Followed |
|---|---|---|
| Get started | signup wall on my.elementor.com | no |
| What's your email? and Subscribe | newsletter form | not filled, not submitted |
| WordPress, GitHub, Instagram, Facebook, X, YouTube, TikTok, LinkedIn icons | those public profiles | recorded as external, not opened |
| Website Builder | `/products/website-builder/` | yes |
| Hello Themes | `/hello-theme/` | yes |
| Elementor AI | `/ai-page-builder/` | yes |
| WooCommerce Builder | `/features/woocommerce-builder/` | yes |
| Image Optimizer | `/products/image-optimizer/` | yes |
| Ally | `/products/ally-web-accessibility/` | yes |
| Performance | `/speed-performance/` | yes |
| Hosting for WordPress | `/hosting/` | yes |
| Domains | `/domains/` | yes |
| Site Mailer | `/products/site-mailer/` | yes |
| Angie | `/products/angie-ai-for-wordpress/` | yes |
| Cookiez | `/products/cookie-consent/` | yes |
| Agencies | `/solutions/agency/` | yes |
| Enterprise | `/solutions/enterprise/` | yes |
| Blog | `/blog/` | yes |
| Roadmap | `/roadmap/` | yes |
| Developers Website | [https://developers.elementor.com/](https://developers.elementor.com/) | yes |
| Glossary | `/resources/glossary/` | yes |
| Free Elementor Download | `/free-download/` | yes |
| WordPress Download | `/wordpress/` | yes |
| Utilities Center | `/utilities-center/` | yes |
| Prompt Library | [http://prompts.elementor.com/](http://prompts.elementor.com/) | recorded, not opened as its own capture |
| About Us | `/about/` | yes |
| Contact Us | `/contact/` | yes |
| Careers | [https://elementor.careers/explore/](https://elementor.careers/explore/) | external, not opened |
| FAQs | `/faq/` | yes |
| Affiliate Program | `/affiliates/` | yes |
| Trust Center | `/trust/` | yes |
| Legal Center | `/legal-center/` | yes |
| Media | `/logos/` | yes |
| Help Center | `/help/` | yes |
| Priority Support | `/priority-support/` | yes |
| Terms & Conditions | `/terms/` | yes |
| Privacy Policy | `/terms/privacy/` | yes |

## In-page controls

### Pricing

| Control | Opens | Shot |
|---|---|---|
| `.multi-year-select__trigger` "1-year plans" | Menu: 1-year, 2-year, 3-year. A choice changes the displayed price. It does not start checkout. | [desktop](screenshots/tree/pricing-light-term-open.png), [phone](screenshots/tree/mobile-pricing-light-term.png) |
| `button.plan-toggle` Advanced / Expert and One / One Agency | Swaps the card in that column. Local only. | [Expert selected](screenshots/tree/pricing-light-plan-expert.png) |
| "57 Editor Pro widgets" and the sibling counts (`a.widget-popup`) | Widget List dialog with Free / Essential / Pro tabs | [widget list](screenshots/tree/pricing-light-widgets.png) |
| More information | Disclosure under a feature row. The click ran. The open row was below the 900px fold in the shot, so the open state is recorded from the DOM, not from a visible crop. | not a useful open-state photo |
| Buy now | `my.elementor.com/store/checkout` with a plan id | recorded, not followed |
| FAQ rows on the pricing page | Same accordion as `/faq/` | see FAQ |

### FAQ

`/faq/` renders the first row "What is Elementor?" already expanded (`aria-expanded="true"`). The title is `.dsm-faq--title` with `role="button"`. A click toggles that row. Other rows start closed. Shot of the already-open first row: [desktop](screenshots/tree/faq-light-open.png), [phone](screenshots/tree/mobile-faq-light-open.png).

### Contact

Four cards. Two open a form dialog and were not submitted.

| Card | Opens |
|---|---|
| General Inquiries | chat entry, not a page navigation in the harvest |
| Sales | chat entry |
| Legal department | popup form (`data-action-link` popup open). Fields: name, email, subject, message, privacy checkbox, Submit. Shot: [dialog](screenshots/tree/contact-light-popup.png) |
| Partnerships | a second popup form, same pattern, not submitted |

Submit was not pressed. No field was filled on this pass.

### Help center

`/help/` uses its own header: Knowledge hub, Topics, Video gallery, Pricing. The search field and Get answer were not submitted. Visible category links from the hub:

| Label | Opens |
|---|---|
| Getting Started | `/help/build-with-the-editor/getting-started-editor/` |
| Layouts | `/help/build-with-the-editor/layouts/` |
| Widgets | `/help/build-with-the-editor/widgets/` |
| Marketing Tools | `/help/build-with-the-editor/marketing-tools/` |
| Editor Version 4 | `/help/build-with-the-editor/v4-editor/` |
| Hosting | `/help/hosting/` |
| Connect Domains | `/help/connect-domains/` |
| Elementor One | `/help/manage-subscription/elementor-one/` |
| Read article (eight cards) | individual `/help/<slug>/` articles |

One article was opened as a sample of that branch: [https://elementor.com/help/connect-your-domain-to-a-website/](https://elementor.com/help/connect-your-domain-to-a-website/). The rest of the article tree is the same template and was not walked page by page.

### Blog

The blog header is a different template: logo, Categories, Search, language globe, Login, Get Started. Categories click highlighted the label and did not open a visible panel in the 1440 shot, so that open state is not claimed. Search focus is [blog-light-search.png](screenshots/tree/blog-light-search.png). Article cards link to `/blog/<slug>/`. Twenty-four article URLs were in the first page harvest. They were not each opened. Login and Get Started on this header are the same walls and were not followed.

### Checker

`/checker/` has a Scan button and four in-page tabs (Get found, Get represented right, Get the agent to convert, See it and fix it) plus an FAQ accordion. Scan would submit a URL to a checker. It was not pressed, and no URL was typed.

### Developers

Footer "Developers Website" opens [https://developers.elementor.com/](https://developers.elementor.com/). Its header is separate from the marketing pill.

| Control | Opens | Shot |
|---|---|---|
| Getting Started | menu: Getting Started, Your First Addon, Building Addons | [menu](screenshots/tree/docs-light-menu-getting-started.png) |
| Internals | menu: The Editor, Editor Controls, Data Structure, Managers, Scripts & Styles, Hooks, Deprecations, CLI | [menu](screenshots/tree/docs-light-menu-internals.png) |
| Components | menu: Widgets, Controls, Dynamic Tags, Form Actions, Form Fields, Theme Conditions, Theme Locations, Context Menu, Finder | [menu](screenshots/tree/docs-light-menu-components.png) |
| Blog | developers blog | link, not opened past the home |
| Get Started, Start Coding | in-page docs links | [home](screenshots/tree/docs-light-home.png) |

No search field was on the developers home.

## Pages visited

Sixty-seven unique final URLs returned a public document. The Yoast page sitemap lists 39 URLs. Two of those were not opened: `/affiliates/signup/` (signup wall, recorded and stopped) and `/features/` (the crawler followed a redirect of that URL back to the home document). The legal sitemap lists 48 URLs. Terms and Privacy were opened. The other legal pages are the same long-form template linked from the legal center and were not each opened.

| URL | Title |
|---|---|
| https://elementor.com | Website builder: Create a Website Now / Elementor |
| https://elementor.com/about | Learn all about Elementor |
| https://elementor.com/domains | Buy a Domain Name / Register domain names with Elementor |
| https://elementor.com/affiliates | Earn commission: join our Affiliate Program / Elementor |
| https://elementor.com/logos | Elementor logo guidelines and branding |
| https://elementor.com/bug-bounty-programs | Elementor’s bug bounty programs / Elementor |
| https://elementor.com/hello-theme | Hello: The best & fastest theme for WordPress / Elementor |
| https://elementor.com/priority-support | WordPress & Elementor support: Priority Support |
| https://elementor.com/products/website-builder/v4-faq | Version 4 FAQs |
| https://elementor.com/ecommerce-builder | Builder for WooCommerce: Design a store that sells |
| https://elementor.com/wordpress | Download WordPress - Latest Version (Free) |
| https://elementor.com/hosting | Hosting for WordPress: ultra fast, cloud, managed & secure |
| https://elementor.com/pro/changelog | The Elementor Pro Changelog- Version Updates / Elementor.com |
| https://elementor.com/faq | Elementor Frequently Asked Questions / Elementor |
| https://elementor.com/products/cookie-consent | Cookie Consent for WordPress / Elementor |
| https://elementor.com/solutions/enterprises | Website builder for enterprises / Elementor |
| https://elementor.com/trust | Elementor Trust Center |
| https://elementor.com/products/angie-ai-for-wordpress | Angie: AI for WordPress creation & management / Elementor |
| https://elementor.com/products/image-optimizer | Image Optimizer: PNG, JPG & GIFs, convert to WebP & AVIF |
| https://elementor.com/products/ally-web-accessibility | Ally: Web accessibility plugin for WordPress / Elementor |
| https://elementor.com/mcp | MCP / Elementor |
| https://elementor.com/ai-page-builder | AI tools for WordPress website creation / Elementor |
| https://elementor.com/products/website-builder | Editor: AI Website Builder for WordPress: 22M+ sites / Elementor |
| https://elementor.com/products/site-mailer | Site Mailer: SMTP replacement, email deliverability & logs |
| https://elementor.com/showoff | Showoff / Elementor |
| https://elementor.com/features/popup-builder | Popup Builder for WordPress / No-code popups that convert |
| https://elementor.com/checker | Free Agent Ready Checker / Elementor |
| https://elementor.com/one | One / Elementor |
| https://elementor.com/solutions/agency | Website builder for agencies / Elementor |
| https://elementor.com/contact | Contact the Elementor Team for Any Question / Elementor.com |
| https://elementor.com/free-download | Free Download / Elementor |
| https://elementor.com/hello-theme/download-success | Hello Theme Submission / Elementor |
| https://elementor.com/utilities-center | Utilities center / Elementor |
| https://elementor.com/legal-center | Legal center / Elementor |
| https://elementor.com/speed-performance | Speed Performance / Elementor |
| https://elementor.com/pricing | Elementor Website Builder Pricing Plans / Choose Your Plan |
| https://elementor.com/pro | Elementor Pro Plans: Find The Right Plan For You |
| https://elementor.com/help | Elementor Knowledge Hub |
| https://elementor.com/blog | The Elementor Blog |
| https://elementor.com/roadmap | Elementor roadmap |
| https://elementor.com/pages/bfcm-2026-tof | Black Friday 2026 / Elementor |
| https://elementor.com/products/manage | Manage multiple WordPress sites from one dashboard |
| https://elementor.com/de | Website-Builder: Jetzt erstellen Website erstellen / Elementor |
| https://elementor.com/es | Website builder: Crea un sitio web ahora / Elementor |
| https://elementor.com/fr | Créateur de sites web : Créez un site web dès maintenant / Elementor |
| https://elementor.com/it | Website builder: crea subito un sito web / Elementor |
| https://elementor.com/pt-br | Construtor de sites: Crie um site agora / Elementor |
| https://elementor.com/nl | Websitebouwer: Creëer nu een website / Elementor |
| https://elementor.com/help/connect-your-domain-to-a-website | Connect your domain to a website / Elementor |
| https://elementor.com/terms | Terms / Elementor |
| https://elementor.com/terms/privacy | Privacy Policy / Elementor |
| https://elementor.com/resources/glossary | Web Creators Glossary: Defintions of Web Design & WordPress Terms |
| https://elementor.com/de/one | One / Elementor |
| https://elementor.com/de/products/website-builder | Editor: AI Website Builder for WordPress: 22M+ sites / Elementor |
| https://elementor.com/de/ecommerce-builder | Builder für WooCommerce: Gestalte einen Shop, der verkauft |
| https://elementor.com/de/products/image-optimizer | Image Optimizer: PNG, JPG und GIFs in WebP und AVIF umwandeln |
| https://elementor.com/de/products/ally-barrierefreiheit | Ally: Plugin für Barrierefreiheit im Web für WordPress / Elementor |
| https://elementor.com/de/speed-performance | Geschwindigkeits-Performance / Elementor |
| https://elementor.com/de/products/cookie-consent | Cookie Consent for WordPress / Elementor |
| https://elementor.com/de/hosting | Hosting für WordPress: superschnell, Cloud, verwaltet und sicher |
| https://elementor.com/de/domains | Domain-Namen kaufen / Domain-Namen bei Elementor registrieren |
| https://elementor.com/de/products/site-mailer | Site Mailer: SMTP-Ersatz, E-Mail-Zustellbarkeit und Protokolle |
| https://elementor.com/de/products/manage | Verwalte mehrere WordPress-Seiten über ein einziges Dashboard |
| https://elementor.com/de/products/angie-ki-fuer-wordpress | Angie: KI für die Erstellung und Verwaltung von WordPress-Seiten / Ele |
| https://elementor.com/de/solutions/agency | Website-Builder für Agenturen / Elementor |
| https://elementor.com/de/preise | Elementor Website Builder Preispläne / Wähle deinen Plan |
| https://elementor.com/de/solutions/enterprises | Website-Builder für Unternehmen / Elementor |

Unique final URLs: 67


## Walls, recorded and not followed

| Control | URL | Why the branch stopped |
|---|---|---|
| Log in | [https://my.elementor.com/login/](https://my.elementor.com/login/) | Sign-in wall. Photographed, nothing typed. |
| Get started, Create an Account | [https://my.elementor.com/signup/](https://my.elementor.com/signup/) | Signup wall. Not opened. |
| Buy now, Try it for free, Start free | `my.elementor.com/store/checkout` | Checkout. Not opened. |
| Join program | `/affiliates/signup/` | Signup path. Not opened. |
| Continue with Google, Continue with passkey, Continue with SSO, More options | on the login wall | Identity-provider and passkey controls. Not clicked. |
| Subscribe, contact Submit, help Get answer, checker Scan | on the public pages | Forms. Not submitted. |

Details of the login wall are in [login-review.json](login-review.json).
