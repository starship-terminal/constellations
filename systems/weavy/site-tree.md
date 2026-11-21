# Weavy public site tree

Mapped 2026-11-21 from the live site before screenshots, with headless Playwright. `https://www.weavy.ai/` returns 200 and redirects to `https://weave.figma.com/`. The product is branded Figma Weave. The marketing site is a Webflow site (`data-wf-domain=weave.figma.com`, stylesheet `weavy-ai.webflow.shared.*.css`). One theme is painted: white page, dark ink. The changelog says the signed-in editor gained a light mode on 2026-11-02. That switch sits in the app, which this capture does not enter.

Sitemap (`https://weave.figma.com/sitemap.xml`, lastmod 2026-11-15 to 2026-11-18) lists seven URLs. No other marketing routes were linked from the homepage.

Nothing below submits a form, types a password, or clicks Figma, Google, Microsoft, or Apple sign-in.

## Shared chrome (every weave.figma.com page)

| Control | Opens |
|---|---|
| Top banner "Explore Max" | `/pricing` (query `utm_source=Website&utm_medium=top_bar_banner&utm_campaign=max_plan`) |
| Banner "Terms apply." | `https://help.weavy.ai/en/articles/17636512-seedance-2-5-max-plan-launch-promotion` (knowledge-center article; second visit in the same session was Cloudflare-blocked) |
| Logo | `/` |
| Nav "COLLECTIVE" | `/collective` |
| Nav "ENTERPRISE" | `/enterprise` |
| Nav "PRICING" | `/pricing` |
| Nav "REQUEST A DEMO" | `https://www.figma.com/contact/weave/` (Figma contact page, off the product site) |
| Nav "SIGN IN" | `https://app.weavy.ai/signin` (login wall; stop) |
| Nav "Start Now" | same sign-in URL |
| Footer "ABOUT" | `/about-us` |
| Footer "CAREERS" | `https://www.figma.com/careers/` (Figma, off-site) |
| Footer "TRUST" | `https://content.weavy.ai/` which redirects to `https://content.weave.figma.com/` |
| Footer "TERMS" | `https://content.weavy.ai/terms-of-service` which redirects to `https://content.weave.figma.com/terms-of-service` |
| Footer "PRIVACY" | `https://content.weavy.ai/privacy-policy` which redirects to `https://www.figma.com/legal/privacy/` (Figma legal, off-site) |
| Footer "COLLECTIVE" | `/collective` |
| Footer "AFFILIATES" | `/affiliate` |
| Footer "KNOWLEDGE CENTER" | `https://help.weavy.ai/en/` |
| Footer "CHANGE LOG" | `/change-log` |
| Footer socials (LinkedIn, Instagram, X, Discord, YouTube) | external profiles; not product UI |

Desktop nav is a flat link row (`.navbar_main`). There is no desktop hamburger and no nav dropdown. Phone hides Collective, Enterprise, and Request a demo (`hide-mobile-landscape`); Pricing, Sign in, Start Now, and the logo stay.

## Home `/`

| Control | Opens |
|---|---|
| Hero and footer "Start Now" / "START NOW" | `https://app.weavy.ai/signin` (login wall; stop) |
| Tools carousel previous / next (`Go to last slide`, `Next slide`, controls `tools-slider-track`) | moves the tools slider on the same page |
| Workflows carousel previous / next (controls `splide01-track`) | moves the Splide carousel on the same page |
| Each workflow card "Try" | `https://app.weavy.ai/recipe/<id>` or `/flow/<id>` (app; login wall; stop). Eight public cards: ControlNet, Camera Angle Control, Relight 2.0 human, Figma Weave Logo, Relight Product, Wan Lora Rotate, Multiple Models, Wan LoRa Inflate |

## Pricing `/pricing`

| Control | Opens |
|---|---|
| Audience tab "Individuals" | hash `#pricing-individuals` (same page) |
| Audience tab "Teams" | hash `#pricing-teams` (same page) |
| Billing switch (`role=switch`, label "Bill annually") | toggles Monthly / Annual prices on the same page. Annual is the default and shows "Save 30%". Monthly prices read $0 / $24 / $45 / $100 for the individual plans |
| Plan "Start free" | `https://app.weavy.ai/signin` (login wall; stop) |
| Plan "Get this plan" (Starter, Professional, Max, Team) | `https://app.weavy.ai/pricing` (app checkout; login wall; stop) |
| Enterprise "Contact sales" | `https://form.typeform.com/to/VmiA3c6t` (external form; not submitted) |
| FAQ questions (eight, `.faq_question` / `.faq_accordion`) | expand the answer on the same page. Answers are already in the DOM |
| FAQ "here" / "comprehensive model list" | `https://content.weave.figma.com/models-pricing` |
| FAQ "pricing page" | `/pricing` |
| FAQ mailto | a support mailto on the pricing FAQ. The address is not stored in this package |

## Collective `/collective`

| Control | Opens |
|---|---|
| "Apply now" | `https://weavyai.notion.site/20f355cab8da81568073e9a4ab1c910f` (external Notion form; not submitted) |
| In-page `#` anchors | same page |

## Enterprise `/enterprise`

| Control | Opens |
|---|---|
| "Contact Sales" | `https://www.figma.com/contact/weave/` (Figma contact; off-site) |

## About `/about-us`

Shared chrome only. No extra dialogs or tabs.

## Affiliate `/affiliate`

| Control | Opens |
|---|---|
| "Apply now" / "Apply Now" | `https://weavyai.notion.site/207355cab8da805d9dcdc00ab14f3443` (external Notion form; not submitted) |
| "Terms and Conditions here" | `https://content.weavy.ai/` (trust center) |

## Change log `/change-log`

| Control | Opens |
|---|---|
| Dropdown "All users" (`.changelog_dropdown-toggle`) | a menu of audience filters (links are `.changelog_dropdown-link`; hidden tag chips include Enterprise) |
| Dropdown "All update types" | a menu of update-type filters (hidden tag chips include Bug fix) |
| "Clear filters" (`.changelog_clear`, hidden until a filter is on) | resets both dropdowns on the same page |
| Update cards | not links. The list is the page |

## Trust center `https://content.weavy.ai/`

Redirects to `https://content.weave.figma.com/`. Notion-hosted.

| Control | Opens |
|---|---|
| "Terms of Service" | a Notion page (`www.notion.so/Weavy-Figma-Weave-Terms-of-Service-…`) |
| "Privacy" | `https://www.figma.com/legal/privacy/` |
| "Policy" | a Notion page |
| "Share site to socials" / "More actions" | Notion site chrome, `aria-expanded=false` |

## Terms `https://content.weavy.ai/terms-of-service`

Redirects to `https://content.weave.figma.com/terms-of-service`. Long legal page. Links out to `www.figma.com/aup`, the DPA, and a verified-models Notion page. No form.

## Models pricing `https://content.weave.figma.com/models-pricing`

Public Notion page, title "Models Pricing List". Linked from the pricing FAQ. One link back to `https://weavy.ai/pricing`.

## Knowledge center `https://help.weavy.ai/en/`

Intercom help center. Search field is present (`input[name=q]`, placeholder "Search for articles..."). It is not submitted.

| Control | Opens |
|---|---|
| "Weave's Editor" | `/en/collections/15341378-weave-s-editor` |
| "My Dashboard" | `/en/collections/15341586-my-dashboard` |
| "Account management" | `/en/collections/15341987-account-management` |
| "Nodes and Models Documentations" | `/en/collections/15247921-nodes-and-models-documentations` |
| "Frequently Asked Questions" | `/en/collections/15249535-frequently-asked-questions` |

A second navigation in the same browser session to a collection URL returned Cloudflare "Sorry, you have been blocked" (Attention Required). The home of the knowledge center loaded. Collections are recorded as a boundary when the block repeats.

## Login wall (stop)

`https://app.weavy.ai/signin` is the destination of Sign in, Start Now, Start free, and Get this plan. The task names it as offering Figma, Google, and Microsoft. Those controls are not clicked. Recipe and flow "Try" links (`/recipe/<id>`, `/flow/<id>`) and `https://app.weavy.ai/pricing` are the same app host and the same stop.

A headless probe of `/signin` did not reach the sign-in form. Cloudflare returned "Sorry, you have been blocked" (Ray ID `a5db5863afd1d43a`). An earlier probe in the same run returned title "Figma Weave" and an empty body, which is the same wall: the app did not paint a public page. The branch stops at the URL.

## Not on this site

No public theme toggle. No public toast, select, checkbox, radio, or text-area form. The only public switch is the pricing billing toggle. The only public text field is the knowledge-center search box, which is not submitted. No account, profile, newsletter, survey, or onboarding field is filled.
