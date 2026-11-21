# Dropbox public site tree

Mapped on 2026-11-21 from [https://www.dropbox.com/](https://www.dropbox.com/) in headless Chromium, signed out. Desktop shots are 1440 x 900 at 1x. Phone shots are 390 x 844 at 2x (PNG 780 x 1688). The crawl opened 70 public pages (depth 0 to 2) and recorded 1,128 control destinations. 557 further same-host links were still queued when the crawl stopped at 70 pages. Those leftovers are named below as linked, not opened.

Nothing was typed. Nothing was submitted. Identity-provider buttons were not clicked. Login, register, checkout, and the Reclaim signup were recorded as walls and the branch stopped there.

Cookie dialogs were hidden with CSS after one photograph. Decline and Accept All were not clicked. The footer control "Cookies & CCPA preferences" points at `#manage-cookies` and was not clicked.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header Products | hover, or click | Mega-menu panel. A second click closes it. |
| Header Solutions | hover, or click | Mega-menu panel. |
| Header Get app | click | Small menu: Desktop app, Mobile app. |
| Header globe, "Select a language" | click | Dialog, "Choose a language:". Close is the X. |
| Phone hamburger | click | Full-screen drawer. Close is the X. |
| Drawer Products, Solutions, Get app | click | Expands that section inside the drawer. |
| Drawer "English (United States)" | click | Same language dialog, stacked as a list. |
| /plans "Billed monthly" / "Billed yearly" | click | Local radio. Default is yearly. |
| /plans "Show only differences" | click | Local switch on the comparison table. |
| /plans "Help me choose" | click | Dialog, "Find your plan in seconds". Close is the X. The three choices were not clicked. |
| /features Share, Sync, Storage, Security, Collaborate, Productivity | click | In-page tab. The hero illustration did not change in this capture. |
| Cookie dialog | mounts on its own | "We use cookies…". Controls: Customize cookies, Decline, Accept All, X. None clicked. Hidden with CSS. |
| Google One Tap, "Sign in to Dropbox with Google" | mounts on its own | Bottom sheet. Not clicked. Hidden with CSS on later shots. |

There is no site search box in the header. The home hero illustration shows a product demo with a search field, Folder / Type / Last modified / People / Sort menus, and an "Ask Dash" button. Those controls sit inside the illustration. They do not navigate.

## Header

Photographed: [home-menu-products.png](screenshots/home-menu-products.png), [home-menu-solutions.png](screenshots/home-menu-solutions.png), [home-menu-get-app.png](screenshots/home-menu-get-app.png), [home-light-language.png](screenshots/home-light-language.png).

| Control | Kind | Destination |
|---|---|---|
| Logo | link | [/](https://www.dropbox.com/) |
| Products | button, menu | panel below |
| Solutions | button, menu | panel below |
| Business | link | [/enterprise](https://www.dropbox.com/enterprise) |
| Pricing | link | [/plans](https://www.dropbox.com/plans) |
| Globe, "Select a language" | button, dialog | language list below. Does not navigate until a language is chosen. None chosen. |
| Contact sales | link | [/contact-sales](https://www.dropbox.com/contact-sales) |
| Get app | button, menu | Desktop app → [/desktop](https://www.dropbox.com/desktop). Mobile app → [/mobile](https://www.dropbox.com/mobile) |
| Sign up | link | [/register](https://www.dropbox.com/register). Wall. Stop. |
| Log in | link | [/login](https://www.dropbox.com/login). Wall. Stop. |
| Get started | link | [/plans](https://www.dropbox.com/plans) |
| Skip to main content | link | `#main-content` |
| Promo strip, "Tigris joins Dropbox…" | link | [blog.dropbox.com acquisition post](https://blog.dropbox.com/topics/company/dropbox-completes-acquisition-of-tigris-data) |

### Products menu

| Label | Destination | This pass |
|---|---|---|
| Dropbox | [/dropbox](https://www.dropbox.com/dropbox) | linked, not opened this pass (opened on 2026-11-13) |
| Replay | [/replay](https://www.dropbox.com/replay) | linked, not opened this pass |
| Sign | [/sign](https://www.dropbox.com/sign) | linked, not opened this pass |
| Reclaim.ai | [app.reclaim.ai/signup](https://app.reclaim.ai/signup) | wall. Footer link was opened and stopped. Header link was not clicked. |
| Dash | [dash.dropbox.com](https://dash.dropbox.com) | separate host. Not opened. |
| DocSend | [/docsend](https://www.dropbox.com/docsend) | linked, not opened this pass |
| Early access | [/early-access](https://www.dropbox.com/early-access) | opened from the footer |

### Solutions menu

Teams: Sales [/business/solutions/sales](https://www.dropbox.com/business/solutions/sales), Marketing [/business/solutions/marketing](https://www.dropbox.com/business/solutions/marketing), HR [/business/solutions/human-resources](https://www.dropbox.com/business/solutions/human-resources), IT [/business/solutions/it](https://www.dropbox.com/business/solutions/it), Creatives [/business/solutions/creatives](https://www.dropbox.com/business/solutions/creatives). Linked from the menu. Not opened this pass (the crawl budget opened other solution pages first).

Use cases: Cloud storage [/features/cloud-storage](https://www.dropbox.com/features/cloud-storage), AI integrations [/app-integrations](https://www.dropbox.com/app-integrations), Send large files [/features/share/send-large-files](https://www.dropbox.com/features/share/send-large-files), Video review [/replay](https://www.dropbox.com/replay), Signing documents [/features/productivity/electronic-signature](https://www.dropbox.com/features/productivity/electronic-signature), Sharing files [/features/share](https://www.dropbox.com/features/share). The first three and the signature page were opened. Video review and Sharing files were linked.

Industries: Construction, Technology, Manufacturing, Media, Professional services, all under [/business/solutions/](https://www.dropbox.com/business/solutions), plus Education [/education](https://www.dropbox.com/education). Those six industry and education pages were opened from home "Learn more" links.

### Language dialog

Opens from the header globe and from the same control in the footer and on the auth cards. Photographed desktop [home-light-language.png](screenshots/home-light-language.png) and phone [mobile-home-light-drawer-language.png](screenshots/mobile-home-light-drawer-language.png). No language was selected.

Bahasa Indonesia, Bahasa Malaysia, Dansk, Deutsch, English (United Kingdom), English (United States), Español (España), Español (Latinoamérica), Français (Canada), Français (France), Italiano, Nederlands, Norsk (bokmål), Polski, Português (Brasil), Русский, Svenska, Українська, ไทย, 中文 (简体), 中文 (繁體), 日本語, 한국어.

## Phone drawer

Photographed: [mobile-home-light-drawer.png](screenshots/mobile-home-light-drawer.png), [mobile-home-light-drawer-products.png](screenshots/mobile-home-light-drawer-products.png), [mobile-home-light-drawer-language.png](screenshots/mobile-home-light-drawer-language.png), [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) (drawer with the cookie dialog still up), [mobile-plans-light-default.png](screenshots/mobile-plans-light-default.png).

The hamburger is an icon button with no text label (`dwg-nav__hamburger-button`). Sign up and Log in stay in the bar and go to the same walls as desktop. The drawer lists Products, Solutions, Business, Pricing, Contact sales, Get app, English (United States), and Get started. Products expands to the same seven product links as the desktop menu. Solutions and Get app expand to the same destinations as the desktop menus. The phone language shot also shows a Google One Tap sheet, "Sign in to Dropbox with Google". That sheet was not clicked.

## Cookie dialog

Photographed on desktop inside [home-light-language.png](screenshots/home-light-language.png) and on phone in [mobile-home-light-cookie.png](screenshots/mobile-home-light-cookie.png).

| Control | Kind | This pass |
|---|---|---|
| Privacy Policy | link | [/privacy](https://www.dropbox.com/privacy), linked, not opened |
| Privacy Policy FAQs | link | [help.dropbox.com cookie article](https://help.dropbox.com/accounts-billing/security/cookies) |
| Customize cookies | button | not clicked |
| Decline | button | not clicked |
| Accept All | button | not clicked |
| X | button | not clicked |

Later shots hide the dialog with CSS (`display: none` on the cookie box). That writes no consent.

## Footer

The same footer is on the marketing pages and on the auth cards. Groups and where each link goes:

Products: Desktop app [/desktop](https://www.dropbox.com/desktop), Mobile app [/mobile](https://www.dropbox.com/mobile), Integrations [/app-integrations](https://www.dropbox.com/app-integrations), Features [/features](https://www.dropbox.com/features), Solutions [/business/solutions](https://www.dropbox.com/business/solutions), Security [/features/security](https://www.dropbox.com/features/security), Early access [/early-access](https://www.dropbox.com/early-access), Templates [/templates](https://www.dropbox.com/templates), Free tools [/tools](https://www.dropbox.com/tools). All opened.

Plans: Plus [/plus](https://www.dropbox.com/plus), Professional [/pro](https://www.dropbox.com/pro) (lands on [/overview/professionals](https://www.dropbox.com/overview/professionals)), Business [/business](https://www.dropbox.com/business), Enterprise [/enterprise](https://www.dropbox.com/enterprise), DocSend [www.docsend.com](https://www.docsend.com/), Dropbox Sign [sign.dropbox.com](https://sign.dropbox.com/), Reclaim.ai [app.reclaim.ai/signup](https://app.reclaim.ai/signup) (wall, stopped), Dropbox Fax [fax.dropbox.com](https://fax.dropbox.com/) (not opened), Plans [/plans](https://www.dropbox.com/plans).

Features: Product updates [/product-updates](https://www.dropbox.com/product-updates), Send large files, Send long videos, Cloud photo storage, Secure file transfer, Cloud backup, Edit PDFs, Electronic signatures, Convert to PDF. All opened.

Support: Help center [help.dropbox.com](https://help.dropbox.com/), Contact us [/contact](https://www.dropbox.com/contact), Privacy & terms [/terms](https://www.dropbox.com/terms), Cookie policy [help.dropbox.com cookies](https://help.dropbox.com/accounts-billing/security/cookies), Cookies & CCPA preferences `#manage-cookies` (not clicked), AI principles [/ai-principles](https://www.dropbox.com/ai-principles), Sitemap [experience.dropbox.com/sitemap](https://experience.dropbox.com/sitemap) (the fetch returned an empty body; not opened in the browser).

Resources: Learning resources [learn.dropbox.com](https://learn.dropbox.com), Blog [blog.dropbox.com](https://blog.dropbox.com/), Events [events.dropbox.com](https://events.dropbox.com), Customer stories [/customers](https://www.dropbox.com/customers), Resources library [/resources](https://www.dropbox.com/resources), Developers [/developers](https://www.dropbox.com/developers), Community forums [www.dropboxforum.com](https://www.dropboxforum.com/). Customer stories, resources, and developers were opened. The other four hosts were not.

Partners: Referrals [/refer](https://www.dropbox.com/refer), Reseller partners [/business/partners](https://www.dropbox.com/business/partners), Integration partners [/app-integrations](https://www.dropbox.com/app-integrations), Find a partner [experience.dropbox.com/partner-locator](https://experience.dropbox.com/partner-locator) (not opened).

Company: About us [/about](https://www.dropbox.com/about), Jobs [jobs.dropbox.com](https://jobs.dropbox.com) (not opened), Investor relations [dropbox.gcs-web.com](https://dropbox.gcs-web.com/) (not opened), Corporate responsibility [/corporate-responsibility](https://www.dropbox.com/corporate-responsibility).

Social: Twitter [twitter.com/Dropbox](https://twitter.com/Dropbox), Facebook [facebook.com/Dropbox](https://www.facebook.com/Dropbox/), YouTube [youtube.com/user/dropbox](https://www.youtube.com/user/dropbox). Not opened. These are the brand profiles, not a sign-in.

The footer language button is the same dialog as the header globe.

## Home page controls

Hero "Try Dropbox free" and the promo "Get started" go to [/plans](https://www.dropbox.com/plans). "Enable animation" is a checkbox on the hero illustration. It was not toggled.

Integration row: See all integrations → [/app-integrations](https://www.dropbox.com/app-integrations). ChatGPT, Gemini, SpaceXAI, Muse, Microsoft Copilot each have a product page under [/app-integrations/](https://www.dropbox.com/app-integrations) (opened) and a "Connect now" or "Learn more" that leaves the site (chatgpt.com, claude.com, gemini.google.com, cursor.com, help.dropbox.com). Those off-site connect links were not followed.

Feature cards "Learn more" opened cloud storage, send large files, security, and the industry pages listed above. "Watch testimonial" and "Watch webinar" are buttons with no href. They were not clicked, so the player they open is not captured.

Resources: one article was opened ([/resources/send-video-without-losing-quality](https://www.dropbox.com/resources/send-video-without-losing-quality)). "View more resources" opened [/resources](https://www.dropbox.com/resources), which lists hundreds of article links. Those article links were recorded and not each opened.

## Pages opened

Each row is a page the crawl loaded. "Via" is the control that put it in the queue.

| URL | Heading | Via |
|---|---|---|
| [/](https://www.dropbox.com/) | Freedom to work your way (A/B; other loads say "Store, share, and get more done") | start |
| [/enterprise](https://www.dropbox.com/enterprise) | Secure collaboration across your corporation | header Business |
| [/plans](https://www.dropbox.com/plans) | pricing | header Pricing |
| [/contact-sales](https://www.dropbox.com/contact-sales) | Contact our sales team | header Contact sales |
| [/register](https://www.dropbox.com/register) | Get started with Dropbox | header Sign up. Wall. |
| [/login](https://www.dropbox.com/login) | Log in or sign up for free | header Log in. Wall. |
| [/app-integrations](https://www.dropbox.com/app-integrations) | Dropbox Partners | See all integrations |
| [/app-integrations/open-ai](https://www.dropbox.com/app-integrations/open-ai) | ChatGPT | ChatGPT card |
| [/app-integrations/gemini](https://www.dropbox.com/app-integrations/gemini) | Gemini | Gemini card |
| [/app-integrations/spacex-ai](https://www.dropbox.com/app-integrations/spacex-ai) | Cursor / Grok Bot plugin | SpaceXAI card |
| [/app-integrations/meta-muse](https://www.dropbox.com/app-integrations/meta-muse) | Muse | Muse card |
| [/app-integrations/microsoft-copilot](https://www.dropbox.com/app-integrations/microsoft-copilot) | Microsoft Copilot | Copilot card |
| [/features/cloud-storage](https://www.dropbox.com/features/cloud-storage) | Secure cloud storage | Learn more |
| [/features/share/send-large-files](https://www.dropbox.com/features/share/send-large-files) | Securely send large files | Learn more |
| [/features/security](https://www.dropbox.com/features/security) | security | Learn more |
| [/business/solutions/construction](https://www.dropbox.com/business/solutions/construction) | construction | Learn more |
| [/business/solutions/media](https://www.dropbox.com/business/solutions/media) | media | Learn more |
| [/business/solutions/technology](https://www.dropbox.com/business/solutions/technology) | technology | Learn more |
| [/business/solutions/professional-services](https://www.dropbox.com/business/solutions/professional-services) | professional services | Learn more |
| [/business/solutions/manufacturing](https://www.dropbox.com/business/solutions/manufacturing) | manufacturing | Learn more |
| [/education](https://www.dropbox.com/education) | campus | Learn more |
| [/resources](https://www.dropbox.com/resources) | Dropbox resources | View more resources |
| [/resources/send-video-without-losing-quality](https://www.dropbox.com/resources/send-video-without-losing-quality) | send videos | Read article |
| [/desktop](https://www.dropbox.com/desktop) | desktop app | footer |
| [/mobile](https://www.dropbox.com/mobile) | mobile app | footer |
| [/features](https://www.dropbox.com/features) | What is Dropbox? | footer |
| [/business/solutions](https://www.dropbox.com/business/solutions) | Business solutions | footer |
| [/early-access](https://www.dropbox.com/early-access) | Early Access | footer |
| [/templates](https://www.dropbox.com/templates) | Formswift templates | footer |
| [/tools](https://www.dropbox.com/tools) | free tools | footer |
| [/plus](https://www.dropbox.com/plus) | Plus | footer |
| [/overview/professionals](https://www.dropbox.com/overview/professionals) | Professionals | footer Professional |
| [/business](https://www.dropbox.com/business) | business | footer |
| [app.reclaim.ai/signup](https://app.reclaim.ai/signup) | Welcome to Reclaim | footer Reclaim.ai. Wall. |
| [/product-updates](https://www.dropbox.com/product-updates) | What's new | footer |
| [/features/share/send-long-videos](https://www.dropbox.com/features/share/send-long-videos) | long videos | footer |
| [/features/cloud-storage/photos](https://www.dropbox.com/features/cloud-storage/photos) | photo storage | footer |
| [/features/share/file-transfer](https://www.dropbox.com/features/share/file-transfer) | file transfer | footer |
| [/features/cloud-storage/file-backup](https://www.dropbox.com/features/cloud-storage/file-backup) | cloud backup | footer |
| [/features/productivity/pdf-editor](https://www.dropbox.com/features/productivity/pdf-editor) | PDF editor | footer |
| [/features/productivity/electronic-signature](https://www.dropbox.com/features/productivity/electronic-signature) | electronic signatures | footer |
| [/features/productivity/convert-to-pdf](https://www.dropbox.com/features/productivity/convert-to-pdf) | convert to PDF | footer |
| [/contact](https://www.dropbox.com/contact) | Contact Dropbox | footer |
| [/terms](https://www.dropbox.com/terms) | Terms of Service | footer |
| [/ai-principles](https://www.dropbox.com/ai-principles) | AI Principles | footer |
| [/customers](https://www.dropbox.com/customers) | Customer stories | footer |
| [/developers](https://www.dropbox.com/developers) | developers | footer |
| [/refer](https://www.dropbox.com/refer) | referral program | footer |
| [/business/partners](https://www.dropbox.com/business/partners) | Partner Program | footer |
| [/about](https://www.dropbox.com/about) | mission | footer |
| [/corporate-responsibility](https://www.dropbox.com/corporate-responsibility) | corporate responsibility | footer |
| [/enterprise/data-governance](https://www.dropbox.com/enterprise/data-governance) | Data Governance | Explore data governance |
| [/apps](https://www.dropbox.com/apps) | App Center | Explore our App Center |
| [/apps/google_suite](https://www.dropbox.com/apps/google_suite) | GSuite | Connect now |
| [/apps/autocad](https://www.dropbox.com/apps/autocad) | AutoCAD | Connect now |
| [/apps/canva](https://www.dropbox.com/apps/canva) | Canva | Connect now |
| [/app-integrations/microsoft](https://www.dropbox.com/app-integrations/microsoft) | Microsoft | Learn more |
| [/app-integrations/adobe](https://www.dropbox.com/app-integrations/adobe) | Adobe | Learn more |
| [/app-integrations/hubspot](https://www.dropbox.com/app-integrations/hubspot) | HubSpot | Learn more |
| [/app-integrations/aws](https://www.dropbox.com/app-integrations/aws) | AWS | Learn more |
| [/apps/collections/creativity_and_design](https://www.dropbox.com/apps/collections/creativity_and_design) | Creativity & design | collection link |
| [/apps/collections/marketing_and_sales](https://www.dropbox.com/apps/collections/marketing_and_sales) | Marketing & sales | collection link |
| [/apps/collections/project_management](https://www.dropbox.com/apps/collections/project_management) | Project management | collection link |
| [/checkout?key=fss_plus](https://www.dropbox.com/checkout?key=fss_plus) | Buy Dropbox Plus | Plus "Buy now". Auth wall over the form. Stop. |
| [/features/sync](https://www.dropbox.com/features/sync) | file syncing | in-page link |
| [/features/share](https://www.dropbox.com/features/share) | file sharing | in-page link |
| [/features/cloud-storage/remote-wipe](https://www.dropbox.com/features/cloud-storage/remote-wipe) | remote wipe | in-page link |
| [/features/cloud-storage/cloud-security](https://www.dropbox.com/features/cloud-storage/cloud-security) | cloud security | in-page link |

Product pages opened on 2026-11-13 and linked again this pass, not reopened: [/dropbox](https://www.dropbox.com/dropbox), [/replay](https://www.dropbox.com/replay), [/sign](https://www.dropbox.com/sign), [/docsend](https://www.dropbox.com/docsend).

## In-page controls

### /plans

Photographed: [plans-light-help-choose.png](screenshots/plans-light-help-choose.png), [plans-light-toggled.png](screenshots/plans-light-toggled.png). The yearly radio is the default. "Show only differences" is a switch. Clicking it turned the switch on. "Help me choose" opens a dialog with three choices: Just me, My growing business or startup, My established company. Those choices were not clicked. "Buy now" on Plus goes to [/checkout?key=fss_plus](https://www.dropbox.com/checkout?key=fss_plus). "Try for free" goes to [/plans](https://www.dropbox.com/plans) or the register wall depending on the card. "or buy now" is a text link toward checkout. Checkout was opened once and stopped at the auth overlay. Purchase was not clicked.

### /features

Photographed: [features-light-tab-share.png](screenshots/features-light-tab-share.png), [features-light-tab-sync.png](screenshots/features-light-tab-sync.png), [features-light-tab-security.png](screenshots/features-light-tab-security.png), [features-light-tab-collaborate.png](screenshots/features-light-tab-collaborate.png). The tab row is Features, Share, Sync, Storage, Security, Collaborate, Productivity. Share, Sync, Security, and Collaborate were clicked. Storage and Productivity were not. The hero copy and illustration did not change between those clicks, so the tab state is the selected label, not a new page. "Compare plans" goes to [/plans](https://www.dropbox.com/plans). "Play video" was not clicked.

### /contact-sales

A sales form: First Name, Last Name, Work Email, Phone Number, Company Name, Country, Company Size, Potential Users, help topic, product of interest, Message, and Contact Sales. The form was not filled and not submitted. The page also prints a sales phone number. That page was not photographed into the package, so the number is not stored here. "Looking for immediate support?" links to an FAQ. Not followed.

### /checkout

Photographed: [checkout-light-wall.png](screenshots/checkout-light-wall.png). The page behind the overlay shows Choose space (Plus, Professional), Billed yearly / Billed monthly, card brands, and Purchase. An overlay, "Get Dropbox Plus / Log in or sign up", covers it with Continue with Google, Continue with Apple, Continue with Microsoft, an empty email field, and Continue. None of those were used. The branch stopped.

### /templates, /tools, /apps, /resources, /developers

These pages are directories. Templates lists document templates (1099-NEC, bill of sale, and others) as links under [/templates/](https://www.dropbox.com/templates). Tools lists free tools. Apps lists integrations and collections. Resources lists articles. Developers links out to [docs.dropboxapi.com](https://docs.dropboxapi.com/). The directory pages were opened. Their child articles, template documents, and API docs were recorded as links and not each opened.

## Walls

Photographed and stopped. See [login-review.json](login-review.json).

| URL | What is on screen | Not used |
|---|---|---|
| [/login](https://www.dropbox.com/login) | "Log in or sign up for free". Desktop: Continue with Apple, Continue with Microsoft, empty email, Continue. Phone also shows Continue with Google. | every button, the email field |
| [/register](https://www.dropbox.com/register) | "Get started with Dropbox". Same identity buttons and empty email. | every button, the email field |
| [/checkout?key=fss_plus](https://www.dropbox.com/checkout?key=fss_plus) | Auth overlay over the Plus checkout | Google, Apple, Microsoft, Continue, Purchase |
| [app.reclaim.ai/signup](https://app.reclaim.ai/signup) | "Welcome to Reclaim" | not filled |

A known earlier probe found that submitting an email on [/login](https://www.dropbox.com/login) continues into a name-and-password signup. That step was not repeated. The email was not typed again.

## Linked and not opened

The crawl stopped with 557 same-host URLs still queued. The large groups are:

- [/resources/](https://www.dropbox.com/resources) articles (the resources index alone accounts for most of the remainder)
- [/templates/](https://www.dropbox.com/templates) individual templates
- [/apps/](https://www.dropbox.com/apps) individual apps beyond GSuite, AutoCAD, and Canva
- Solutions menu team pages: sales, marketing, HR, IT, creatives
- Product landings already in the 2026-11-13 package: [/dropbox](https://www.dropbox.com/dropbox), [/replay](https://www.dropbox.com/replay), [/sign](https://www.dropbox.com/sign), [/docsend](https://www.dropbox.com/docsend)
- [/privacy](https://www.dropbox.com/privacy), [/waitlist](https://www.dropbox.com/waitlist), [/transfer](https://www.dropbox.com/transfer)

Other hosts linked from the public pages and not opened: help.dropbox.com, blog.dropbox.com, learn.dropbox.com, events.dropbox.com, experience.dropbox.com, jobs.dropbox.com, dash.dropbox.com, sign.dropbox.com, fax.dropbox.com, www.docsend.com, docs.dropboxapi.com, trust.dropbox.com, dropbox.gcs-web.com, www.dropboxforum.com, and the store badges (App Store, Google Play).

Signed-in product surfaces (the file dashboard, Paper, Dash, Replay and Sign workspaces, account, billing) were not reached. They sit behind the auth walls.
