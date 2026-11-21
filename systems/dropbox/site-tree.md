# Dropbox public site tree

Mapped on 2026-11-22 from [https://www.dropbox.com/](https://www.dropbox.com/) in headless Chromium, signed out. Desktop shots are 1440 × 900 CSS pixels at 2× (PNG 2880 × 1800). Phone shots are 390 × 844 CSS pixels at 2× (PNG 780 × 1688). The homepage returned 200. The title was "Dropbox: Secure cloud storage, file sharing, and more". The desktop heading was "Store, share, and get more done with a smarter Dropbox". This is a live marketing site, not a parked domain.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Buy now, Try for free, Install, and Contact sales were not followed into checkout or a signed-in file browser. `login-extracted` stays `not-started`.

The homepage hero on desktop and the file-browser illustration on phone are marketing animations. The phone illustration shows sample folder names (Inspiration, cover_image, Fall shoot). Those names are in the public demo, not an account. Login and signup were photographed on their own URLs, with the email field empty.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header Products | hover | Two-column menu. Click also sets `aria-expanded`. Escape or moving the pointer away closes it. |
| Header Solutions | hover | Three-column menu: Teams, Use cases, Industries. |
| Header Get app | hover | Small menu: Desktop app, Mobile app. |
| Header globe, "Select a language" | click | Dialog, "Choose a language:". Close is the X. No language was chosen. |
| Phone hamburger | click | Full-screen drawer. Close is the X. Sign up and Log in stay in the bar. |
| Drawer Products, Solutions, Get app | click | Expands that section inside the drawer. Photographed collapsed. |
| Drawer "English (United States)" | click | Same language dialog. Not opened this pass on the phone. |
| Promo strip | click | Blog post on blog.dropbox.com. Not followed. |
| Cookie dialog | mounts on its own | "We use cookies…". Customize cookies, Decline, Accept All, and X were not clicked. |
| /plans Billed monthly / Billed yearly | click | Local radio. Default is yearly. Monthly was clicked and photographed. No purchase. |
| /plans Help me choose | click | Plan quiz dialog. Not opened this pass. |
| /plans Buy now, Try for free, or buy now | click | Checkout or register. Not followed. Stop. |

There is no site search in the header. The phone hero illustration contains a search field, Upload, Create, and folder rows. Those controls sit inside the illustration. They do not navigate.

## Header

Photographed: [public-home-desktop.png](screenshots/public-home-desktop.png), [public-menu-products-desktop.png](screenshots/public-menu-products-desktop.png), [public-menu-solutions-desktop.png](screenshots/public-menu-solutions-desktop.png), [public-menu-get-app-desktop.png](screenshots/public-menu-get-app-desktop.png), [public-language-desktop.png](screenshots/public-language-desktop.png).

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | [/](https://www.dropbox.com/) | home |
| Products | button, menu | panel below | photographed, destinations not clicked from the menu |
| Solutions | button, menu | panel below | photographed |
| Business | link | [/enterprise](https://www.dropbox.com/enterprise) | opened. On some inner pages the same slot reads Enterprise. |
| Pricing | link | [/plans](https://www.dropbox.com/plans) | opened |
| Globe, "Select a language" | button, dialog | language list | opened, none chosen |
| Contact sales | link | [/contact-sales](https://www.dropbox.com/contact-sales) | not opened. A sales form. Not filled. |
| Get app | button, menu | Desktop app, Mobile app | menu photographed; both destinations opened from the footer paths |
| Sign up | link | [/register](https://www.dropbox.com/register) | wall. Stop. |
| Log in | link | [/login](https://www.dropbox.com/login) | wall. Stop. |
| Get started | link | [/plans](https://www.dropbox.com/plans) | same pricing page |
| Promo, "Tigris joins Dropbox…" | link | [blog post](https://blog.dropbox.com/topics/company/dropbox-completes-acquisition-of-tigris-data) | not followed |

### Products menu

Opened by hover. Seven items.

| Label | Destination | This pass |
|---|---|---|
| Dropbox | [/dropbox](https://www.dropbox.com/dropbox) | opened |
| Replay | [/replay](https://www.dropbox.com/replay) | linked, not opened this pass |
| Sign | [/sign](https://www.dropbox.com/sign) | linked, not opened this pass |
| Reclaim.ai | [app.reclaim.ai/signup](https://app.reclaim.ai/signup) | wall. Not opened. |
| Dash | [dash.dropbox.com](https://dash.dropbox.com) | separate host. Not opened. |
| DocSend | [/docsend](https://www.dropbox.com/docsend) | linked, not opened this pass |
| Early access | [/early-access](https://www.dropbox.com/early-access) | opened |

### Solutions menu

| Column | Label | Destination |
|---|---|---|
| Teams | Sales | [/business/solutions/sales](https://www.dropbox.com/business/solutions/sales) |
| Teams | Marketing | [/business/solutions/marketing](https://www.dropbox.com/business/solutions/marketing) |
| Teams | HR | [/business/solutions/human-resources](https://www.dropbox.com/business/solutions/human-resources) |
| Teams | IT | [/business/solutions/it](https://www.dropbox.com/business/solutions/it) |
| Teams | Creatives | [/business/solutions/creatives](https://www.dropbox.com/business/solutions/creatives) |
| Use cases | Cloud storage | [/features/cloud-storage](https://www.dropbox.com/features/cloud-storage) |
| Use cases | AI integrations | [/app-integrations](https://www.dropbox.com/app-integrations) |
| Use cases | Send large files | [/features/share/send-large-files](https://www.dropbox.com/features/share/send-large-files) |
| Use cases | Video review | [/replay](https://www.dropbox.com/replay) |
| Use cases | Signing documents | [/features/productivity/electronic-signature](https://www.dropbox.com/features/productivity/electronic-signature) |
| Use cases | Sharing files | [/features/share](https://www.dropbox.com/features/share) |
| Industries | Construction | [/business/solutions/construction](https://www.dropbox.com/business/solutions/construction) |
| Industries | Technology | [/business/solutions/technology](https://www.dropbox.com/business/solutions/technology) |
| Industries | Manufacturing | [/business/solutions/manufacturing](https://www.dropbox.com/business/solutions/manufacturing) |
| Industries | Media | [/business/solutions/media](https://www.dropbox.com/business/solutions/media) |
| Industries | Professional services | [/business/solutions/professional-services](https://www.dropbox.com/business/solutions/professional-services) |
| Industries | Education | [/education](https://www.dropbox.com/education) |

The menu was photographed. Those destinations were not each opened this pass.

### Get app menu

| Label | Destination | This pass |
|---|---|---|
| Desktop app | [/desktop](https://www.dropbox.com/desktop) | opened. Install was not clicked. |
| Mobile app | [/mobile](https://www.dropbox.com/mobile) | opened. Store badges were not clicked. |

### Language dialog

Opens from the header globe. Photographed: [public-language-desktop.png](screenshots/public-language-desktop.png). No language was selected.

Bahasa Indonesia, Bahasa Malaysia, Dansk, Deutsch, English (United Kingdom), English (United States), Español (España), Español (Latinoamérica), Français (Canada), Français (France), Italiano, Nederlands, Norsk (bokmål), Polski, Português (Brasil), Русский, Svenska, Українська, ไทย, 中文 (简体), 中文 (繁體), 日本語, 한국어.

## Phone drawer

Photographed: [public-home-phone.png](screenshots/public-home-phone.png), [public-drawer-phone.png](screenshots/public-drawer-phone.png), [public-plans-phone.png](screenshots/public-plans-phone.png).

The hamburger is an icon button. Sign up and Log in stay in the bar and go to the same walls as desktop. The open drawer lists Products, Solutions, Business, Pricing, Contact sales, Get app, English (United States), and Get started. Products, Solutions, and Get app were left collapsed. Their destinations match the desktop menus; the DOM already holds those links while the sections are closed.

The phone homepage heading is a different variant from desktop: "One place to store, share, and collaborate".

## Cookie dialog

Photographed on the Get app menu shot [public-menu-get-app-desktop.png](screenshots/public-menu-get-app-desktop.png), the Solutions menu shot, the language dialog, and the login and signup walls. Decline, Accept All, Customize cookies, and the X were not clicked.

| Control | Kind | This pass |
|---|---|---|
| Privacy Policy | link | not followed |
| Privacy Policy FAQs | link | [help.dropbox.com cookie article](https://help.dropbox.com/accounts-billing/security/cookies) |
| Customize cookies | button | not clicked |
| Decline | button | not clicked |
| Accept All | button | not clicked |
| X | button | not clicked |

## Footer

Photographed: [public-footer-desktop.png](screenshots/public-footer-desktop.png). The same groups appear on the marketing pages. Destinations were read from the homepage footer. Child articles, template documents, and off-site hosts were not each opened.

| Group | Label | Destination |
|---|---|---|
| Dropbox | Desktop app | [/desktop](https://www.dropbox.com/desktop) |
| Dropbox | Mobile app | [/mobile](https://www.dropbox.com/mobile) |
| Dropbox | Integrations | [/app-integrations](https://www.dropbox.com/app-integrations) |
| Dropbox | Features | [/features](https://www.dropbox.com/features) |
| Dropbox | Solutions | [/business/solutions](https://www.dropbox.com/business/solutions) |
| Dropbox | Security | [/features/security](https://www.dropbox.com/features/security) |
| Dropbox | Early access | [/early-access](https://www.dropbox.com/early-access) |
| Dropbox | Templates | [/templates](https://www.dropbox.com/templates) |
| Dropbox | Free tools | [/tools](https://www.dropbox.com/tools) |
| Products | Plus | [/plus](https://www.dropbox.com/plus) |
| Products | Professional | [/pro](https://www.dropbox.com/pro) |
| Products | Business | [/business](https://www.dropbox.com/business) |
| Products | Enterprise | [/enterprise](https://www.dropbox.com/enterprise) |
| Products | DocSend | [www.docsend.com](https://www.docsend.com/) |
| Products | Dropbox Sign | [sign.dropbox.com](https://sign.dropbox.com/) |
| Products | Reclaim.ai | [app.reclaim.ai/signup](https://app.reclaim.ai/signup). Wall. Not opened. |
| Products | Dropbox Fax | [fax.dropbox.com](https://fax.dropbox.com/). Not opened. |
| Products | Plans | [/plans](https://www.dropbox.com/plans) |
| Features | Product updates | [/product-updates](https://www.dropbox.com/product-updates) |
| Features | Send large files | [/features/share/send-large-files](https://www.dropbox.com/features/share/send-large-files) |
| Features | Send long videos | [/features/share/send-long-videos](https://www.dropbox.com/features/share/send-long-videos) |
| Features | Cloud photo storage | [/features/cloud-storage/photos](https://www.dropbox.com/features/cloud-storage/photos) |
| Features | Secure file transfer | [/features/share/file-transfer](https://www.dropbox.com/features/share/file-transfer) |
| Features | Cloud backup | [/features/cloud-storage/file-backup](https://www.dropbox.com/features/cloud-storage/file-backup) |
| Features | Edit PDFs | [/features/productivity/pdf-editor](https://www.dropbox.com/features/productivity/pdf-editor) |
| Features | Electronic signatures | [/features/productivity/electronic-signature](https://www.dropbox.com/features/productivity/electronic-signature) |
| Features | Convert to PDF | [/features/productivity/convert-to-pdf](https://www.dropbox.com/features/productivity/convert-to-pdf) |
| Support | Help center | [help.dropbox.com](https://help.dropbox.com/) |
| Support | Contact us | [/contact](https://www.dropbox.com/contact) |
| Support | Privacy & terms | [/terms](https://www.dropbox.com/terms) |
| Support | Cookie policy | [help.dropbox.com cookies](https://help.dropbox.com/accounts-billing/security/cookies) |
| Support | Cookies & CCPA preferences | `#manage-cookies`. Not clicked. |
| Support | AI principles | [/ai-principles](https://www.dropbox.com/ai-principles) |
| Support | Sitemap | [experience.dropbox.com/sitemap](https://experience.dropbox.com/sitemap) |
| Resources | Learning resources | [learn.dropbox.com](https://learn.dropbox.com) |
| Resources | Blog | [blog.dropbox.com](https://blog.dropbox.com/) |
| Resources | Events | [events.dropbox.com](https://events.dropbox.com) |
| Resources | Customer stories | [/customers](https://www.dropbox.com/customers) |
| Resources | Resources library | [/resources](https://www.dropbox.com/resources) |
| Resources | Developers | [/developers](https://www.dropbox.com/developers) |
| Resources | Community forums | [www.dropboxforum.com](https://www.dropboxforum.com/) |
| Resources | Referrals | [/refer](https://www.dropbox.com/refer) |
| Resources | Reseller partners | [/business/partners](https://www.dropbox.com/business/partners) |
| Resources | Integration partners | [/app-integrations](https://www.dropbox.com/app-integrations) |
| Resources | Find a partner | [experience.dropbox.com/partner-locator](https://experience.dropbox.com/partner-locator) |
| Company | About us | [/about](https://www.dropbox.com/about) |
| Company | Jobs | [jobs.dropbox.com](https://jobs.dropbox.com) |
| Company | Investor relations | [dropbox.gcs-web.com](https://dropbox.gcs-web.com/) |
| Company | Corporate responsibility | [/corporate-responsibility](https://www.dropbox.com/corporate-responsibility) |
| Social | Twitter, Facebook, Youtube | brand profiles. Not opened. |

The footer language control is the same dialog as the header globe.

## Pages opened

| URL | Heading | Shot |
|---|---|---|
| [/](https://www.dropbox.com/) | Store, share, and get more done with a smarter Dropbox | [public-home-desktop.png](screenshots/public-home-desktop.png), [public-home-phone.png](screenshots/public-home-phone.png) |
| [/dropbox](https://www.dropbox.com/dropbox) | Don’t just store your files—put them to work | [public-product-desktop.png](screenshots/public-product-desktop.png) |
| [/plans](https://www.dropbox.com/plans) | Go from idea to done with Dropbox | [public-plans-desktop.png](screenshots/public-plans-desktop.png), [public-plans-monthly-desktop.png](screenshots/public-plans-monthly-desktop.png), [public-plans-phone.png](screenshots/public-plans-phone.png) |
| [/features](https://www.dropbox.com/features) | What is Dropbox? | [public-features-desktop.png](screenshots/public-features-desktop.png) |
| [/desktop](https://www.dropbox.com/desktop) | The Dropbox desktop app | [public-download-desktop.png](screenshots/public-download-desktop.png) |
| [/mobile](https://www.dropbox.com/mobile) | Keep work flowing—on the go | [public-mobile-desktop.png](screenshots/public-mobile-desktop.png) |
| [/enterprise](https://www.dropbox.com/enterprise) | Secure collaboration across your corporation | [public-enterprise-desktop.png](screenshots/public-enterprise-desktop.png) |
| [/early-access](https://www.dropbox.com/early-access) | Dropbox Early Access | [public-early-access-desktop.png](screenshots/public-early-access-desktop.png) |
| unknown path | Error (404) | [public-missing-desktop.png](screenshots/public-missing-desktop.png) |

Yearly prices on the photographed cards: Plus $9.99 / month, Standard $15 / user / month, Advanced $24 / user / month. Monthly: Plus $11.99, Standard $18, Advanced $30. Buy now and Try for free were not clicked.

The 404 page offers Home, Help center, Sign in, Get a free account, Dropbox Plus, and Dropbox Business. None of those links were clicked.

## Walls

Photographed empty and stopped. See [login-review.json](login-review.json).

| URL | What is on screen | Not used |
|---|---|---|
| [/login](https://www.dropbox.com/login) | "Log in or sign up for free". Continue with Google, Continue with Apple, Continue with Microsoft, empty email, Continue. | every button, the email field |
| [/register](https://www.dropbox.com/register) | "Get started with Dropbox". Same identity buttons and empty email. | every button, the email field |

The email field value length was 0 on both pages. A hidden autofill password input was also empty. Checkout, Reclaim signup, and Dash were not opened this pass.
