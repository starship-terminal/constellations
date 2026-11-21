# Frame.io public site tree

Walked on 2026-11-21 in headless Chromium, signed out. Start was `https://frame.io/` (HTTP 200, title "Frame.io | Home"). `https://www.frame.io/` redirects there. No Cloudflare, DataDome, or Akamai block rendered. No cookie banner appeared on first load of frame.io. Nothing was typed into a form. Nothing was submitted. No identity provider was clicked.

The marketing site paints one dark theme. There is no theme switch on frame.io. `accounts.frame.io/welcome` is a separate light page.

## Header

The desktop header (1440) sits under a purple announcement bar.

| Control | What it does |
|---|---|
| Announcement "Put your creative context to work with new AI-powered capabilities" | Link to `https://frame.io/ai`. Not followed this pass. |
| Announcement close ("Click to close") | Local dismiss. Not pressed. |
| Logo | `https://frame.io/` |
| Features | Click opens a full-width mega-menu (`role="dialog"`, label "Features navigation group"). Click again closes it. Shot: [home-dark-menu-features.png](screenshots/home-dark-menu-features.png). |
| Enterprise | Same pattern. Shot: [home-dark-menu-enterprise.png](screenshots/home-dark-menu-enterprise.png). |
| Resources | Same pattern. Shot: [home-dark-menu-resources.png](screenshots/home-dark-menu-resources.png). |
| Pricing | `https://frame.io/pricing` |
| Contact Us | `https://frame.io/contact` |
| Sign In | `https://app.frame.io/`, which redirects to the empty welcome wall. Stop. |
| Start Free Trial | `https://accounts.frame.io/welcome/?signup_as_v4_account=true`. Same empty email wall. Stop. |
| Adobe mark | `https://www.adobe.com/`. External. Not followed. |

Features mega-menu, eyebrow PRODUCT:

| Item | Opens |
|---|---|
| Workflow Management | `https://frame.io/features/workflow-management` |
| File Management | `https://frame.io/features/file-management` |
| Share & Present | `https://frame.io/features/present` |
| Review & Approvals | `https://frame.io/features/review-and-approval` |
| Camera to Cloud | `https://frame.io/features/c2c` |
| Integrations | `https://frame.io/integrations` |
| Mounted Storage | `https://frame.io/features/mounted-storage` |
| Frame.io Drive | `https://frame.io/drive` |

Enterprise mega-menu:

| Eyebrow | Item | Opens |
|---|---|---|
| INDUSTRIES | Overview | `https://frame.io/enterprise` |
| INDUSTRIES | Media and Entertainment | `https://frame.io/enterprise/media-and-entertainment` |
| INDUSTRIES | Agencies | `https://frame.io/enterprise/agencies` |
| INDUSTRIES | Brands | `https://frame.io/enterprise/brands` |
| USE CASES | Video | `https://frame.io/enterprise/video-workflows` |
| USE CASES | Photo | `https://frame.io/enterprise/photo-workflows` |
| USE CASES | Marketing Campaign | `https://frame.io/enterprise/campaign-workflows` |

Resources mega-menu, eyebrow INSIGHTS & SOLUTIONS:

| Item | Opens |
|---|---|
| Blog | `https://blog.frame.io/` |
| Customer Stories | `https://frame.io/customers` |
| Developer Resources | `https://next.developer.frame.io/platform/v4/welcome` |
| What's New | `https://frame.io/whats-new` |
| Support | `https://help.frame.io/en/` |
| Resource Hub | `https://frame.io/resources` |

## Phone header (390)

"Toggle mobile navigation" opens a full-screen drawer. Shot: [home-dark-mobile-drawer.png](screenshots/home-dark-mobile-drawer.png).

| Control | What it does |
|---|---|
| Logo | `https://frame.io/` |
| Sign In | `https://app.frame.io/` then the welcome wall. Stop. |
| Close (X) | Closes the drawer. |
| Features | Opens the same product list as the desktop mega-menu (Workflow Management through Frame.io Drive). A back control returns to the top list. |
| Enterprise | Opens Overview, Media and Entertainment, Agencies, Brands, Video, Photo, Marketing Campaign. |
| Resources | Opens Blog, Customer Stories, Developer Resources, What's New, Support, Resource Hub. |
| Pricing | `https://frame.io/pricing` |
| Contact Us | `https://frame.io/contact` |
| Start Free Trial | Welcome wall. Stop. |
| Take a Product Tour | `https://w.adobedemo.com/s/KuLoj7`. External demo. Not followed. |

## Home body

`https://frame.io/`. H1 "One platform for all your creative work."

| Control | What it does |
|---|---|
| Start Free Trial | Welcome wall. Stop. |
| Take a Product Tour | Adobe demo URL above. Not followed. |
| Unlock Faster Workflows | `https://frame.io/features/workflow-management` |
| Manage Files Effortlessly | `https://frame.io/features/file-management` |
| Enhance Your Reviews | `https://frame.io/features/review-and-approval` |
| Discover Better Sharing | `https://frame.io/features/present` |
| Explore Plans / Explore Pricing | `https://frame.io/pricing` |
| Sign Up Now | Welcome wall with `signup_as_v4_account=true`. Stop. |
| Go to previous slide / Go to next slide | Local carousel. Next was pressed. The visible section stayed "SHARING & PRESENTING" and advanced the feature cards (Curate effectively, Customize extensively, Control completely). |
| Feature cards on the home page | Local expanders (passphrases, expiration, workspaces, watermarking, and similar). Not a navigation. |
| Book a Meeting / Talk with Sales | Sales path. Not followed. |

## Footer

Columns, read from the live footer.

FEATURES: Workflow Management, File Management, Share & Present, Review & Approval (`/features/review-and-approval`), iOS & iPad (`/features/ios-ipad`), Camera to Cloud, Transfer (`/transfer`), Integrations, Security (`/security`).

RESOURCES: Blog, Customer Stories, Frame.io Live (`/live`), What's New, Support, Resource Hub, Developers (`https://developer.adobe.com/frameio/`), Status (`https://status.frame.io/`).

ENTERPRISE: Overview, Agencies, Brands, Media & Entertainment.

USE CASES: Video, Photo, Marketing Campaign.

COMPANY: Talk with Sales (sales path, not followed), Careers (`/careers` redirects to `https://careers.adobe.com/us/en`), Contact Us.

Bottom bar: Adobe (`https://www.adobe.com/`), Terms (`/terms`), Privacy (`/privacy`), Cookie preferences, Do not sell or share my personal information (`/privacy#my-personal-information`), language switch, Instagram, YouTube, Facebook, X. Social links were not followed.

Cookie preferences (`#manage-cookies`) does not open a banner. The click requested `https://frame.io/privacy` and stayed on the home page. No reject or accept control appeared. Nothing was accepted. The careers host showed its own Deny / Allow banner. Deny was not needed for the tree, and Allow was not pressed.

## Language switch

Footer button "English (US)", `aria-expanded` becomes true. Panel title "LANGUAGE / REGION". Shot: [home-dark-locale-open.png](screenshots/home-dark-locale-open.png). Escape closes it. No locale was followed.

| Label | Opens |
|---|---|
| Deutsch | `https://frame.io/de-de` |
| English (US) | `https://frame.io/` |
| Español | `https://frame.io/es-es` |
| Français | `https://frame.io/fr-fr` |
| Italiano | `https://frame.io/it-it` |
| 日本語 | `https://frame.io/ja-jp` |
| 한국어 | `https://frame.io/ko-kr` |
| Português (Brasil) | `https://frame.io/pt-br` |
| Русский | `https://frame.io/ru-ru` |
| 简体中文 | `https://frame.io/zh-cn` |

A hidden geo-redirect notice ("Close") sits off-screen on the en-US load. It was not pressed.

## Pricing

`https://frame.io/pricing`. H1 "Plans designed for how you work."

| Control | What it does |
|---|---|
| Monthly / Annually SAVE 13% | Radio pair. Monthly is selected on load ($0, $15, $25). Annually was selected this pass. Shot: [pricing-dark-annual.png](screenshots/pricing-dark-annual.png). Annual prices read $0, $156, $264 per year. The sales announcement bar on that shot was covered before the file entered the package. |
| Sign Up Now / Start Free Trial | Welcome wall, some with a promotions path (`/promotions/V8PY7DHP`, `/promotions/V8TM7DHP2`). Stop. |
| Book a meeting | Sales path. Not followed. |
| Compare plans accordions | Users, Storage, Projects & workspaces, Feedback & collaboration, Camera to cloud, Custom branding, Share for review, Asset playback, Enhanced content security, Admin & security, Apps & integrations, Support, Account services, Billing. Local expanders. |
| FAQ "How do monthly and annual pricing differ?" | Opens in place (`aria-expanded` true). Copy says the annual plan is a 13% discount and both plans renew until cancelled. Not a navigation. |

## Contact

`https://frame.io/contact`. H1 "Hello, how can we help you?" Schedule a Meeting is the only body control. Not followed.

`https://frame.io/contact/form` is an empty Name, Email, Message form with Submit. Photographed at rest in the earlier package. Not typed into this pass. Not submitted.

## Other marketing pages opened or confirmed (HTTP 200)

| URL | H1 | Extra controls |
|---|---|---|
| `/ai` | Your creative work has context. Now AI can put it to work. | None beyond chrome. |
| `/features/workflow-management` | Create your team’s perfect workflow. | None beyond chrome. |
| `/features/file-management` | Move, manage, and store files in one central secure place. | None beyond chrome. |
| `/features/present` | Share and present creative assets beautifully and securely. | Previous / next slide. |
| `/features/review-and-approval` | Deliver creative assets faster with reviews that drive clarity. | None beyond chrome. |
| `/features/c2c` | Lights. Camera. Cloud. | Watch the Video. Industry filters: Sports, Production, Photography, Brands, Agencies. Partner names (Accsoon, Atomos, Canon, and others) are local cards. |
| `/features/mounted-storage` | Work without waiting for files. | Download for macOS. Play. FAQ accordion. |
| `/features/ios-ipad` | Advanced review and approval. Now on the screen in your pocket. | None beyond chrome. |
| `/integrations` | All in on integrations. | Partner cards (Airtable, Asana, Slack, and others). No search field. |
| `/drive` | A better way to handle creative files. | Download for macOS. Play. FAQ accordion. |
| `/transfer` | Faster file transfers without fail. | None beyond chrome. |
| `/enterprise` | Securely scale your creative workflow. | Schedule a Meeting. Not followed. |
| `/security` | Full protection for your organization’s creative work. | None beyond chrome. |
| `/customers` | Collaborate and conquer. | Show More. Previous / next slide. |
| `/whats-new` | Your home for all of the freshest Frame.io news. | Show More. Previous / next slide. |
| `/resources` | Frame.io learning, tips, and support. | Schedule a Meeting. Topic chips (Metadata & Collections, Player and commenting, Workspaces, Sharing, and others). Story cards. |
| `/live` | Welcome to Frame.io Live! | Dated episode buttons. View all / View less. |
| `/case-studies/ford` | Captured in the earlier package as one story template. | Not re-walked this pass. |

## Blog

`https://blog.frame.io/` (HTTP 200, "Frame.io Insider"). Separate light header.

| Control | What it does |
|---|---|
| Search icon | Opens an empty search field (`input[type=search]`, name `s`, placeholder "Search..."). Value length 0. Not typed. Not submitted. |
| Category menus | Post-Production, Workflow, Behind the Scenes, Production, Business, Frame.io News. Each opens a category index under `/category/`. |
| Try Frame.io for Free! | Welcome wall. Stop. |

## Help

`https://help.frame.io/en/` (HTTP 200). Light knowledge base, separate from the marketing theme.

| Control | What it does |
|---|---|
| Language select (`#language-selector`) | Options: Português do Brasil, English (selected, value `/en/`), Français, Deutsch, Italiano, 日本語, 한국어, Pусский, 简体中文, Español. Not changed. |
| Search | Empty "Search for articles..." and a "Search docs" button. Not typed. Not submitted. |
| Sidebar | Expand Frame.io Explained opens article links in place. Other groups stay collapsed: Upload and Organize, Collaboration and Playback, Account Settings, Frame.io C2C, Frame.io Drive & Mounted Storage, Integrations and API, Enterprise, Security, Privacy, and Terms, Frame.io Legacy (V3). |
| Collection cards | Same groups, with article counts. |

## Login and signup walls

| Entry | Result |
|---|---|
| Header Sign In, `https://app.frame.io/` | HTTP 200 redirect to `https://accounts.frame.io/welcome` with an auth callback query. Empty email field (value length 0). Hidden empty password input in the DOM, not painted. Button "Let's go". No Google, Apple, Facebook, Microsoft, GitHub, or SSO control. Shots: [welcome-light-empty-desktop.png](screenshots/welcome-light-empty-desktop.png), [welcome-light-empty-phone.png](screenshots/welcome-light-empty-phone.png). Stop. |
| Start Free Trial / Sign Up Now | `https://accounts.frame.io/welcome/?signup_as_v4_account=true`. Same painted email wall. Password input exists in the DOM, value length 0, not visible. Not typed. Stop. |
| `https://next.frame.io/login` | HTTP 404. "Page not found" and "Return Home". Shot: [next-login-not-found.png](screenshots/next-login-not-found.png). |
| `https://accounts.frame.io/welcome` direct | Same empty email wall. HTTP 200. |

The signed-in app was not entered. No nav, settings, or create surface behind the wall was seen.
