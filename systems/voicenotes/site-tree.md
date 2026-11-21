# Voicenotes public site tree

Mapped on 21 November 2026 from `https://voicenotes.com/` in headless Chromium, signed out. Desktop viewport measured 1440 by 900 at devicePixelRatio 1. Phone viewport measured 390 by 844 at devicePixelRatio 2.

A control that opens a login or signup wall was recorded and not followed further. No email, name, password or code was typed. Google, Microsoft, Apple, Twitter and SSO were not clicked. No form was submitted.

## Header, desktop

| Control | Opens |
|---|---|
| Wordmark | `https://voicenotes.com/` |
| Download | Menu on the same page: Desktop, iOS, Android. See [home-light-download-open](screenshots/home-light-download-open.png). |
| Download, Desktop | Nested items in the same menu. Not followed (app-store and download hosts). |
| Download, iOS | App Store listing for Voicenotes. External. Not followed. |
| Download, Android | Play Store listing. External. Not followed. |
| Enterprise | `https://voicenotes.com/enterprise` |
| Pricing | `https://voicenotes.com/pricing` |
| Resources | Menu on the same page. See [home-light-resources-open](screenshots/home-light-resources-open.png). |
| Resources, Integrations | `https://help.voicenotes.com/en/collections/12277349-integrations`. External help center. Not followed. |
| Resources, Help Center | `https://help.voicenotes.com/en/`. External. Not followed. |
| Resources, Blog | `https://voicenotes.com/blog/` |
| Resources, What's new | `https://voicenotes.com/whats-new/` |
| Log in | Login modal on `https://voicenotes.com/`. Stopped. See [login-review.json](login-review.json). |
| Book a demo | `https://voicenotes.com/enterprise` |
| Start for free | `https://voicenotes.com/signup`. Signup wall. Stopped. |

## Home, below the header

| Control | Opens |
|---|---|
| Hero Book a demo | `https://voicenotes.com/enterprise` |
| Hero Start for free | `https://voicenotes.com/signup`. Signup wall. Stopped. |
| Hero demo Cancel and Record | Painted inside the marketing illustration. Not the signed-in app. Record was not pressed. |
| Footer Start for free | Signup wall. Not followed. |
| Footer product links | macOS and Windows installers on `dl.voicenotes.com`, iOS and watchOS on the App Store, Android and Wear OS on the Play Store, Chrome Web Store. External. Not followed. |
| Footer Brand assets | `https://voicenotes.com/brand-assets` |
| Footer Reviews | `https://voicenotes.com/reviews` |
| Footer Blog | `https://voicenotes.com/blog/` |
| Footer Terms of Service, Help center, FAQ, Privacy Policy | `help.voicenotes.com`. External. Not followed. |
| Footer Trust Center, Subprocessors | `trust.voicenotes.com`. External. Not followed. |
| Footer Status | `status.voicenotes.com`. External. Not followed. |
| Footer Contact support | A mailto link. Not opened. The address is not recorded here. |
| Footer Submit feedback, Report an issue | Typeform URLs. External forms. Not opened. |
| Footer socials | Reddit, X, YouTube, Instagram, LinkedIn. External. Not followed. |
| Ask about Voicenotes | ChatGPT, Claude, Gemini, Grok, Perplexity. External. Not followed. |

## Pricing

`https://voicenotes.com/pricing`. Same header as home.

| Control | Opens |
|---|---|
| Monthly / Annual | Local billing pill. Stays on `/pricing`. Annual is the painted default in [pricing-light-default](screenshots/pricing-light-default.png). |
| Get started | Signup wall. Not followed. |
| Talk to sales | Same destination as Book a demo: `/enterprise`. Not submitted. |
| Compare search | A search field in the compare table. See [pricing-light-compare](screenshots/pricing-light-compare.png). Nothing was typed. |
| FAQ questions | Buttons on the same page. A click did not expand an answer in this pass, so the open state is not captured. |

## Enterprise

`https://voicenotes.com/enterprise`. Header as home. The page embeds a Typeform (`typeform.com/meetvoicenotes`) that asks for a business email. The field was photographed empty and not filled. Next was not clicked.

## Reviews

`https://voicenotes.com/reviews`. A smaller header: wordmark, Log in, Sign up.

| Control | Opens |
|---|---|
| Log in | `javascript:void(null)` on this template. Treated as a login wall. Not followed past the label. |
| Sign up | Same. Treated as a signup wall. Not followed. |
| Wall of love / Use cases | Local tabs. Both photographed. |
| A review card | External post on x.com. Not followed. |

## Blog and What's new

`https://voicenotes.com/blog/` and `https://voicenotes.com/whats-new/` share a second header: wordmark, Pricing, Log in, and a filled pill (Try Voicenotes on the blog, Download for Mac on What's new).

| Control | Opens |
|---|---|
| Pricing | `https://voicenotes.com/pricing` |
| Log in | `https://voicenotes.com/login`. Login wall. Stopped. |
| Try Voicenotes | `https://voicenotes.com/signup`. Signup wall. Stopped. |
| A post card | A published post, for example `/blog/uncategorized/are-ai-meeting-notetakers-safe-for-confidential-business-meetings/`. Photographed. |
| Load more | On the blog index. Not pressed. |
| Share | On a post. Not pressed. |
| Download for Mac | Installer host. Not followed. |

## Brand assets

`https://voicenotes.com/brand-assets`. Logo tiles with PNG, SVG and JPEG download chips. The chips were not clicked. Logo files were not copied into the package.

## Phone

At 390 the header is the wordmark and an Open menu control. The menu lists Download, Enterprise, Pricing, Resources, Login, Book a demo and Start for free. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png). Login and Start for free were not followed. Download and Resources rows were not expanded.

## Stopped

| URL | Why |
|---|---|
| `https://voicenotes.com/` login modal | Login wall. Photographed. Not submitted. |
| `https://voicenotes.com/login` | Login wall. Photographed. Not submitted. |
| `https://voicenotes.com/signup` | Signup wall. Photographed. Not submitted. |
| `https://voicenotes.com/app` | Prior probe redirected to login. Not reopened this pass. |
| Identity providers | Google, Microsoft, Apple, Twitter, SSO. Not clicked. |
| Signed-in app, onboarding, checkout | Behind the walls above. Not captured. |
