# Leonardo.Ai public site tree

Mapped on 2026-11-21 from https://leonardo.ai/ in headless Chromium (Playwright), signed out, before screenshots. Official domain confirmed: leonardo.ai serves "Leonardo.Ai - Generative AI Platform for Images, Art & Video". Curl against the same host hits a Cloudflare challenge; Playwright loads the pages.

This tree is the controls on the main page and the pages they open. Deeper article indexes (news pagination, learn articles, webinar detail, legal extras) are listed as further public pages, not as a second click from home.

## Auth boundary

| Control | Opens | What happened | Stop |
|---|---|---|---|
| Log in (header) | https://app.leonardo.ai/ | 200. App shell renders ("YOURS TO CREATE") and still offers Sign up / Sign in. Signed-in product was not entered. | Recorded. No account created. |
| Start now, Create Free Account, Sign In, app nav items (Generate, Library, Agent, Upscaler, Blueprints, Flow State, Plans, API) | https://app.leonardo.ai/ or https://app.leonardo.ai/auth/login | Login page asks for email and password, or Canva, Apple, Google, or Microsoft. | Stopped. No email typed. No OAuth clicked. No form submitted. |
| https://leonardo.ai/login | same URL | 404. Title "Leonardo.ai". Body: "THIS PAGE IS NOT FOUND". | Known probe. Stopped. |
| Download app (footer) | https://apps.apple.com/us/app/leonardo-ai-image-generator/id1662773014 | Leaves leonardo.ai for the App Store. | Not captured as a Leonardo surface. |
| Google Play badge | https://play.google.com/store/apps/details?id=ai.leonardo.leonardo | Leaves leonardo.ai. | Not captured. |
| Help Center | https://intercom.help/leonardo-ai/en | Third-party help. | Not captured. |
| Social (Facebook, Instagram, Discord, X, YouTube, LinkedIn) | those hosts | Leave the product site. | Not captured. |

## Header

Desktop header, left to right. Menus open on hover. The same labels exist as a "Toggle menu" drawer at 390px.

| Control | Opens |
|---|---|
| Wordmark | https://leonardo.ai/ |
| Create (menu) | Panel, not a page. Items below. |
| Industry (menu) | Panel, not a page. Items below. |
| Business (menu) | Panel, not a page. Items below. |
| Learn (menu) | Panel, not a page. Items below. |
| Pricing | https://leonardo.ai/pricing |
| Contact | https://leonardo.ai/contact-us |
| Tutorial | https://leonardo.ai/news/how-to-use-leonardo-ai |
| Log in | Auth boundary above. |
| Toggle menu (phone) | Same four menus plus Pricing, Contact, Tutorial, Log in, stacked. |

### Create menu

| Item | Opens |
|---|---|
| AI Image Generator | https://leonardo.ai/ai-image-generator |
| Creative Ideation | https://leonardo.ai/fast-track-your-creativity-with-flow-state |
| Background Remover | https://leonardo.ai/transparent-png-generator |
| Train Your Own Model | https://leonardo.ai/element-training |
| AI Video Generator | https://leonardo.ai/ai-video-generator |
| Image Editor | https://leonardo.ai/ai-image-editor |
| Video Editor | https://leonardo.ai/ai-video-editor |
| Image Upscaler | https://leonardo.ai/universal-upscaler |
| GPT Image 2.6 | https://leonardo.ai/gpt-image-2-6 |
| Nano Banana 2.1 | https://leonardo.ai/nano-banana-2-1 |
| FLUX 3 Image | https://leonardo.ai/flux-3-image |
| Veo 3.1 | https://leonardo.ai/veo-3 |
| View all models | https://leonardo.ai/models |
| Get started | https://leonardo.ai/news/how-to-use-leonardo-ai |

### Industry menu

| Item | Opens |
|---|---|
| Marketing | https://leonardo.ai/ai-marketing-tools |
| Photography | https://leonardo.ai/ai-photography |
| Interior Design | https://leonardo.ai/interior-design |
| Graphic Design | https://leonardo.ai/ai-graphic-design |
| Art | https://leonardo.ai/ai-art-generator |
| Architecture | https://leonardo.ai/ai-architecture-generator |
| View all industries | https://leonardo.ai/ai-tools |
| Learn what's allowed | https://leonardo.ai/news/can-you-use-ai-generated-images-commercially |

### Business menu

| Item | Opens |
|---|---|
| Collaborate via Teams | https://leonardo.ai/team-plans |
| Integrate via API | https://leonardo.ai/api |
| Read the case study | https://leonardo.ai/news/coming-in-clutch-giving-ducati-riders-the-ai-reins-to-self-expression |

### Learn menu

| Item | Opens |
|---|---|
| Leonardo Learn | https://leonardo.ai/learn |
| News | https://leonardo.ai/news |
| Webinars | https://leonardo.ai/webinars |
| Learn more (prompt article) | https://leonardo.ai/news/ai-image-prompts |

## Home body

| Control | Opens |
|---|---|
| Start now (hero and each feature) | Auth boundary. Not followed into a session. |
| Developer API | https://leonardo.ai/api |
| Unmute / Previous video / Next video | In-page hero video. No navigation. |
| Go to slide 1–4 | In-page carousel. |
| Learn more: Create images without limits | https://leonardo.ai/ai-image-generator |
| Learn more: Bring visuals into motion | https://leonardo.ai/ai-video-generator |
| Learn more: Edit with precision | https://leonardo.ai/ai-image-editor |
| Learn more: Elevate quality at any size | https://leonardo.ai/universal-upscaler |
| Previous slide / Next slide | In-page carousels (artist stories, resources, industries). |
| Artist story cards | News articles (examples: Joyce Ng, Lucas Clément, Ivona Tau). |
| Resource cards | News and model pages already in the Create menu, plus https://leonardo.ai/news/ai-image-models/, https://leonardo.ai/news/mastering-prompts-for-veo-3, https://leonardo.ai/news/ai-art-styles, https://leonardo.ai/news/storyboard-ai, https://leonardo.ai/news/generative-ai-for-product-prototypes. |
| Case-study cards | https://leonardo.ai/news/gamepack-game-development-with-leonardo-ai, the Ducati article, https://leonardo.ai/news/from-static-assets-to-scalable-motion-how-springbok-used-ai-animation-as-a-creative-advantage. |

## Footer (same on marketing pages)

| Group | Opens |
|---|---|
| Product links | Image generator, Flow State, background remover, element training, video generator, upscaler, image editor, video editor, model pages already in Create. |
| Industry links | Marketing, graphic design, print on demand, photography, interior, architecture, art, banner, social post, storyboard, character. Print on demand, banner, social, storyboard and character are footer-only (not in the Industry menu). |
| Company | Pricing, Help Center (Intercom), Contact, Careers, Creator Program, Imagination Fund, Learn, Team plans, API, App Store, Play Store, download-app (redirects to the App Store). |
| Legal | Privacy, Terms, Cookie policy. |
| Social | External hosts above. |

## Interactions that stay on the page

| Page | Control | Result |
|---|---|---|
| Home | Create / Industry / Business / Learn | Dropdown or mega menu. |
| Home | Toggle menu at 390px | Full-screen nav drawer. |
| Home | Unmute, video arrows, slide dots | Hero media. |
| Home | Carousel arrows | Horizontal card rows. |
| Pricing | Plan tabs or billing controls, if present | Stay on /pricing. No checkout followed. |
| Contact | Two forms (short message; work enquiry with name, email, company, country, size) | Fields visible. Not filled. Not submitted. |
| Learn | Search field ("Search topic, tutorial, webinar, etc.") | Focus only. Not submitted. |
| Creator program | Application form (name, country, pronouns, email, portfolio, socials) | Visible. Not filled. Not submitted. |
| Models / tools / feature pages | Start now | Auth boundary. |

## Pages captured as the public system

Representative marketing templates, both widths (1440x900 and 390x844), light theme only (the site paints black; no theme toggle was found on the public pages):

- Home, including menus and the phone drawer.
- One feature page (AI Image Generator), one model page (GPT Image 2.6), one industry page (AI tools index).
- Pricing, API, team plans, contact (form visible, not submitted), learn (search focused, not submitted), news index, one news article (getting started), models index, careers, privacy.

## Further public pages, same templates, not shot one by one

Sitemap https://leonardo.ai/sitemap.xml lists about 192 marketing URLs (models, industries, guides, legal). News, learn and webinar indexes paginate. Those pages repeat the same header, footer and section pattern. They are recorded here so the tree is complete. They are not each a separate screenshot.

Examples reached while mapping, all 200, not used as extra shot targets: /ai-video-generator, /ai-image-editor, /universal-upscaler, /webinars, /transparent-png-generator, /element-training, /ai-video-editor, /flux-3-image, /veo-3, /nano-banana-2-1, /ai-marketing-tools, /ai-graphic-design, /ai-print-on-demand, /ai-photography, /interior-design, /ai-architecture-generator, /ai-art-generator, /ai-banner-generator, /ai-social-media-post-generator, /ai-storyboard-generator, /ai-character-generator, /leonardo-creator-program, /leonardo-imagination-fund, /cookie-policy, /terms-of-service.

## Not captured

- Signed-in app (generate, library, canvas, blueprints, settings, billing checkout).
- Auth providers (Canva, Apple, Google, Microsoft) and the email form.
- App Store and Play Store listings.
- Intercom help center.
- Newsletter, onboarding, birthday, plan and survey fields. None were filled. Creator-program and contact fields were left empty.
