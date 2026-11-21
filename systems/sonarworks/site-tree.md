# Sonarworks public site tree

Mapped 2026-11-21 from the live public site before screenshots. Source: `https://www.sonarworks.com/` in headless Chromium (Playwright), plus `https://www.sonarworks.com/sitemap.xml` (209 `<loc>` entries). CookieScript and GetSiteControl overlays were removed in the DOM for mapping. No consent button was clicked. No form was submitted. No email, password, or code was typed.

Official product: Sonarworks, speaker and headphone calibration software. Confirmed domain `www.sonarworks.com` (HTTP 200, title "Sonarworks - Industry-Leading Tools for Audio Creators"). Related public hosts: `store.sonarworks.com` (Shopify store, HTTP 200), `support.sonarworks.com` (Zendesk, HTTP 403 Cloudflare challenge from this host).

No theme switch exists on the public site. The marketing surface is light only (`bg-base-100` on `body`). Dark is not a reachable public state.

## Shell

| Control | Where | Opens |
|---|---|---|
| Wordmark "Sonarworks" | `#primary-navigation` | `/` |
| Reviews | `#top-navigation` (desktop, `lg` and up) and footer | `/reviews` |
| Blog | `#top-navigation` and footer | `/blog` |
| Help & Support | `#top-navigation` | `https://support.sonarworks.com/hc/en-us` (Cloudflare challenge from this host; stop) |
| Company | `#top-navigation` `[data-menu="company-top-navigation"]` hover | Menu `#company-top-navigation` (mouseenter sets `display:block`; mouseleave hides after a timeout). Not a page. |
| Company menu: About us | that menu | `/company` |
| Company menu: Careers | that menu | `/company/careers` |
| Company menu: For media | that menu | `/company/media-kit` |
| Company menu: Become a partner | that menu | `/licensing` |
| Company menu: Contact us | that menu | `/company/contacts` (contact form; do not submit) |
| Log in | `#top-navigation` | `/account/login` (auth wall; stop) |
| Menu | `#menu-open-button` `href="#mobile-navigation"` (shown below `lg`) | Hash target `#mobile-navigation` (`:target` makes it visible). Not a new page. Close is `#menu-close-button` `href="#"`. |
| Cart | `#cart-nav-link` | `https://store.sonarworks.com/cart` |

Primary tabs are anchors with `data-navigation`. `blueprint.js` listens for `mouseenter` on `#primary-navigation [data-navigation]` and reveals the matching bar inside `#secondary-navigation` (class `sub-navigation`, opacity transition 300ms). The tab itself is also a page link.

| Primary tab | Hover reveals | Tab click goes to |
|---|---|---|
| SoundID Reference | `#soundid-reference-navigation` | `/soundid-reference` |
| SoundID VM PRO | `#soundid-vm-pro-navigation` | `/soundid-vm-pro` |
| SoundID VoiceAI | `#soundid-produce-navigation` | `/soundid-produce/voiceai` |
| SoundID (Personalization app) | `#soundid-navigation` | `/soundid` |
| Store | `#store-navigation` | `https://store.sonarworks.com/` |

### SoundID Reference bar (`#soundid-reference-navigation`)

| Control | Opens |
|---|---|
| Multichannel | `/soundid-reference/multichannel` |
| Virtual Monitoring | `/soundid-vm-pro/virtual-monitoring` |
| Pricing | `/soundid-reference/pricing` which **redirects to** `/black-friday` (observed 2026-11-21) |
| SoundID Tools | `/soundid-reference/tools/dolby-atmos-personalization` |
| Integrations | `/soundid-reference/integrations` |
| eBooks | `/soundid-reference/ebooks` |
| Download | `/download-center#SoundIDReference` |
| Upgrades | `/soundid-reference/upgrades` |
| Get Free Trial | `/soundid-reference/download/mac` (download page, not a form) |

### SoundID VM PRO bar

| Control | Opens |
|---|---|
| Virtual Monitoring PRO | `/soundid-vm-pro` |
| Virtual Monitoring | `/soundid-vm-pro/virtual-monitoring` |
| Reviews | `/soundid-vm-pro#reviews` (same page, anchor) |
| Pricing | `/soundid-vm-pro#pricing` |
| Download | `/download-center#SoundIDReference` |
| FAQ | `/soundid-vm-pro#faq` |
| Shop Now | `/soundid-vm-pro#pricing` |

### SoundID VoiceAI bar

| Control | Opens |
|---|---|
| Pricing | `/soundid-produce/voiceai#pricing` |
| Voice Packs | `/soundid-produce/voiceai#voice-packs` |
| Use Cases | `/soundid-produce/voiceai#use-cases` |
| How It Works? | `/soundid-produce/voiceai#how-it-works` |
| Demo All Presets | `/soundid-produce/voiceai/preset-catalog` |
| Affiliate | `/affiliate-program` |
| FAQ | `/soundid-produce/voiceai#faq` |
| Download | `/download-center#SoundIDVoiceAI` |
| 7-day Free Trial | `/soundid-produce/voiceai/download/mac` |

### SoundID personalization bar

| Control | Opens |
|---|---|
| Overview | `/soundid` |
| Enabled Devices | `/soundid/enabled-devices` |
| Try Out on Android | `/soundid/android` |
| Supported Headphones | `/soundid/supported-headphones` |
| Get on App Store | Apple App Store listing for the SoundID app (external; not captured) |
| Get on Google Play | Google Play listing for the SoundID app (external; not captured) |

### Store bar

| Control | Opens |
|---|---|
| Store Home | `https://store.sonarworks.com/` |
| SoundID Reference | `/soundid-reference/pricing` then redirect `/black-friday` |
| Virtual Monitoring | `/soundid-reference/virtual-monitoring#pricing` |
| ORIA Mini | `/soundid-reference/integrations/audient-oria-mini#pricing` |
| Software Upgrades | `/soundid-reference/upgrades` |
| Headphones | `https://store.sonarworks.com/collections/individually-calibrated-headphones` |

## Mobile menu (`#mobile-navigation`)

Opened by Menu (`#menu-open-button`). Same destinations as the desktop bars, plus logo, cart, Log in, and the company/support/blog/reviews links. Product groups are disclosure rows (the "↓" labels in the menu). Close returns to `#`.

## Footer (every marketing page)

| Control | Opens |
|---|---|
| About Us | `/company` |
| Careers | `/company/careers` |
| For Media | `/company/media-kit` |
| Contact Us | `/company/contacts` |
| Affiliate Program | `/affiliate-program` |
| Return your purchase | `/withdrawal` |
| Privacy Policy | `/legal/privacy` |
| Cookies Policy | `/legal/cookies-policy` |
| Legal | `/legal` |
| Download Center | `/download-center` |
| For Partners | `/soundid-reference/brand-assets` |

## Dialogs and overlays

| Control | What it is | Action taken |
|---|---|---|
| CookieScript `#cookiescript_injected` | Dialog: "Yep, we use cookies". Actions: "Got it", "Cookie policy" (`/legal/cookies-policy`). | Hidden in the DOM. Never clicked. |
| GetSiteControl widgets `#getsitecontrol-652564`, `#getsitecontrol-652571` | Third-party promo widgets. They intercept pointer events on the primary nav. | Removed from the DOM for capture. Not submitted. |
| Product page `<details>` | `/soundid-reference` has 11 `<details>` (FAQ / feature disclosures). | Open locally; no submit. |
| Carousel arrows "←" / "→" | On product pages. | Local interaction only. |

## Forms (never submitted)

| Page | Fields | Stop |
|---|---|---|
| `/account/login` | Email, password. Buttons: Continue with Facebook, Continue with Google, Continue with Apple, Log in. Link: Sign up → `/account/signup`. | Auth wall. Record URL and stop. Do not type. Do not click Facebook, Google, or Apple. |
| `/account/signup` | Linked from login. Not opened past the wall. | Auth wall. |
| `/company/contacts` | Hidden `to`, email `from`, `title`, `content`, reCAPTCHA. Buttons: Cancel, Send the message. | Do not type an email. Do not submit. Do not solve the captcha. |
| `/blog` | Customer.io newsletter, email placeholder. Button: Subscribe. | Do not type an email. Do not submit. |
| `/soundid-reference` (and similar product pages) | "Get download link" and footer Subscribe (Customer.io, email field). | Do not type an email. Do not submit. |
| `/download-center` | Microphone profile id text field, post to `/download-center/microphone-profiles`. Buttons: Download, Download profile. | Do not submit the profile form. Download links that are plain anchors may be opened as pages. |
| `/soundid-reference/education/application` and `/education/bulk-order` | Application / order forms (sitemap). | Do not fill. |
| Buy now buttons on `/black-friday` | Commerce. | Do not click through to checkout. |

## Reachable public pages (capture set)

Nav and footer pages, both widths (desktop 1440×900, phone 390×844), light only:

- `/` home
- `/soundid-reference` plus secondary bar pages that are distinct URLs: multichannel, virtual monitoring (both `/soundid-vm-pro/virtual-monitoring` and `/soundid-reference/virtual-monitoring`), integrations, integrations/audient-oria-mini, tools/dolby-atmos-personalization, ebooks, upgrades, download/mac, brand-assets
- `/soundid-vm-pro`
- `/soundid-produce/voiceai`, `/soundid-produce/voiceai/preset-catalog`, `/soundid-produce/voiceai/download/mac`
- `/soundid`, `/soundid/enabled-devices`, `/soundid/android`, `/soundid/supported-headphones`
- `/black-friday` (the live pricing destination)
- `/download-center`
- `/reviews`, `/blog`
- `/company`, `/company/careers`, `/company/media-kit`, `/company/contacts` (form visible, not filled)
- `/licensing`, `/affiliate-program`, `/withdrawal`
- `/legal`, `/legal/privacy`, `/legal/cookies-policy`
- Store home, cart, and the headphones collection on `store.sonarworks.com` (public Shopify; no checkout submit)

In-page anchors (`#pricing`, `#faq`, `#reviews`, `#voice-packs`, `#use-cases`, `#how-it-works`, `#overview`, `#SoundIDReference`, `#SoundIDVoiceAI`) are states of the page they sit on, not separate pages.

## Sitemap beyond the nav (209 URLs)

The sitemap lists many more public URLs that the main-page controls do not open directly: blog posts under `/soundid-reference/blog/`, ebook landing pages, integration partner pages, headphone and device detail pages, legal manuals, EU-funding pages (Latvian), education, resellers, artist quotes, and redirects such as `/reference`, `/privacy`, `/careers`, `/contacts`. Those are recorded here. The capture covers the nav and footer tree plus one example of a list page (blog, reviews, integrations, ebooks, enabled devices) rather than every article. A page that 404s or challenges is a gap, not invented.

## Walls and out of scope

| URL or control | Why it stops |
|---|---|
| `/account/login` | Email, password, Facebook, Google, Apple. |
| `/account/signup` | Account creation. |
| Facebook / Google / Apple buttons | Named social login. Never clicked. |
| `/company/contacts` send, newsletter subscribe, download-link email, education application | Forms. Never submitted. No email typed. |
| Buy now / cart checkout | Purchase. Cart page may be screenshotted empty. Checkout is not followed. |
| `support.sonarworks.com` | Cloudflare "Just a moment" (HTTP 403) from this host. |
| App Store and Google Play | External store listings. |
| Signed-in account (licenses, devices, trials, token balance) | Behind login. Not captured. |
| Dark theme | No control. Not present. |
