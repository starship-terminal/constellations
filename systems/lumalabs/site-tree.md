# Luma AI public site tree

Mapped from [https://lumalabs.ai/](https://lumalabs.ai/) on 2026-11-21 in headless Chromium at 1440×900, before screenshots. Same-origin links were followed. A control that opened a login, signup, or third-party wall was recorded and that branch stopped. No form was submitted. No password, email code, Google, or Apple control was used.

The marketing site is Next.js (`__variable_*` on `html`). It paints a white page (`rgb(255, 255, 255)`) and black text. `color-scheme` is `normal`. No theme toggle and no `data-theme` were found on the pages below. `/photon` is an older dark product page and is not linked from the current home footer.

## Home controls

| Control | What it opens |
|---|---|
| Banner "It's here! Luma is now in Claude and ChatGPT" | `/mcp` |
| Logo | `/` |
| PRODUCT | `/app` (link, no menu) |
| PRICING | `/pricing` |
| API | `/api` |
| ENTERPRISE | `/enterprise` |
| MCP | `/mcp` |
| NEWS | `/news` |
| JOIN US | `/careers` |
| Sign In | `https://app.lumalabs.ai/` which redirects to `https://auth.lumalabs.ai/sign-up` (signup wall). Stop. |
| Instagram, YouTube, X, TikTok, LinkedIn icons | Off-site profiles. Not captured. |
| Prompt textarea (`name=prompt`) | Local field. Chips fill it. Submit is not used. |
| Submit prompt | Would send the prompt into the signed-in app. Not pressed. |
| Product Hero Shots | Fills the prompt. Stays on `/`. |
| Paid Social Variants | Fills the prompt. Stays on `/`. |
| Cut a Teaser | Fills the prompt. Stays on `/`. |
| Try for free, Try Free | `https://app.lumalabs.ai/` signup wall. Stop. |
| Learn more (Ray 3.2 band) | `/ray3-2` which redirects to `/ray` |
| Learn more (product band) | `/app` |
| Learn more (research band) | `/news/luma-open-physical-ai-lab` |
| Discover Ray3.2 | `/ray3-2` then `/ray` |
| Discover Uni-1 | `/uni-1` |
| Research paper titles | `/news/tvm`, `/news/ray3-eval`, `/news/inductive-moment-matching` |
| All news | `/news` |
| Recent news titles | `/news/luma-skills`, `/news/introducing-ray-3-2`, `/news/uni-1-1-api`, `/news/luma-innovative-dreams` |
| Careers (team band) | `/careers` |
| Learning Center (team band) | `/learning-center` |
| Toggle mobile navigation menu | Visible at 390. Opens the same nav links in a sheet. |
| Footer Product, Pricing, Ray, UNI-1, API, AI Video Generator, AI Video Generator from Image | `/app`, `/pricing`, `/ray`, `/uni-1`, `/api`, `/create/ai-video-generator`, `/create/ai-video-generator-from-image` |
| Footer About Luma, Enterprise, Join Us, Case Studies, Creative Partner Program, Education Program, Learning Center | `/about`, `/enterprise`, `/careers`, `/case-studies`, `/creative-partner-program`, `/education/educator`, `/learning-center` |
| Footer Media kit | `https://drive.google.com/drive/folders/1FmFNI1dmo0i6mZALAgWsnf2rT7OKRFwG` (Google Drive sign-in wall). Stop. |
| Footer Terms, Privacy, Cookie Policy, Subprocessors | `/legal/terms-of-service`, `/legal/privacy-policy`, `/legal/cookie-policy`, `/legal/subprocessors` |

Hovering PRODUCT, PRICING, API, ENTERPRISE, MCP, NEWS, and JOIN US opened no menu.

## Sitemap pages not linked from the home footer

These are in `https://lumalabs.ai/sitemap.xml` (27 locs) and loaded as public pages.

| Path | What it is |
|---|---|
| `/agents-guide` | Public guide. |
| `/changelog` | Public changelog. |
| `/contact-sales` | Public form. Not submitted. |
| `/dreamlab/featured` | Public gallery. |
| `/education/student` | Public education page. |
| `/llm-info` | Public model notes. |
| `/series-b` | Public announcement. |
| `/the-state-of-ai-2026-annual-trend-report` | Public report page. |
| `/whitepaper` | Public page with a waitlist anchor (`#form`). Form not submitted. |
| `/uni-1/showcase` | Public showcase. |
| `/photon` | Older dark Photon page. Its nav points at a previous site (`/join`, `/dream-machine/api`, `/ray2`, `/genie`, `/interactive-scenes`). Those older routes were not in the current sitemap and were not followed past recording the links. |

## Page controls

Discovered on the loaded pages. A form field is listed so the branch is mapped. None of these forms were filled or submitted.

| Page | Control | Opens |
|---|---|---|
| `/app` | Monthly, Yearly | Local billing toggle on the same page. |
| `/app` | FAQ questions (`aria-expanded=false`) | Accordion panels on the same page. |
| `/app` | Try for free, use-case cards | `https://app.lumalabs.ai/` signup wall. Stop. |
| `/app` | Contact Sales | `/enterprise` |
| `/app` | Explore all features | `/learning-center` |
| `/pricing` | Monthly, Yearly | Local billing toggle. |
| `/pricing` | Plan CTAs | Signup wall. Stop. |
| `/api` | Ray3.2, Uni-1.1 | Local model tabs. |
| `/api` | FAQ questions | Accordion panels. |
| `/api` | Dashboard link | `/api/dashboard`. Probed at capture time. If it is an account wall, stop. |
| `/enterprise` | Industry, company size, region selects | Local listboxes. Not chosen. |
| `/enterprise` | Name, email, company, message, referral, Submit | Sales form. Not filled. Not submitted. |
| `/enterprise` | Case study cards | `/case-studies/aperture`, `/case-studies/boundless` |
| `/mcp` | Claude, ChatGPT | Local connector tabs. |
| `/mcp` | Numbered steps | Accordion. "Connect and sign in" stays on the page as instructions. Not followed into an account. |
| `/news` | Article titles | `/news/<slug>`. The index lists hundreds. Home-linked articles and the sitemap article are the captured set. The rest use the same article template. |
| `/careers` | Title, Description | Local sort. |
| `/careers` | All departments, All locations, department chips | Local filters. |
| `/careers` | Search job titles | Local filter field. Not filled. |
| `/careers` | Role rows | Role detail if it stays on lumalabs.ai. An application form is not submitted. |
| `/learning-center` | Search articles | Local field. Not filled. |
| `/learning-center` | Article cards | `/learning-center/articles/<slug>`. Index plus one article. Remaining articles are the same template. |
| `/learning-center` | FAQ questions | Accordion panels. |
| `/ray` | FAQ questions | Accordion panels. |
| `/uni-1` | Go to slide 1–8 | Local carousel. |
| `/uni-1` | Introduction, Showcase, Intelligent, Directable, Cultured, Evaluations, Pricing, API, FAQ | In-page sections. |
| `/uni-1` | Showcase link | `/uni-1/showcase` |
| `/uni-1` | Tech specs link | `/uni-1/tech-specs` |
| `/uni-1` | Sales form fields and Submit | Not filled. Not submitted. |
| `/case-studies` | All Stories, Agency, Film & Commercials | Local filters. |
| `/case-studies` | Search stories | Local field. Not filled. |
| `/case-studies` | Story cards | `/case-studies/aperture`, `/case-studies/boundless`, `/case-studies/one-day`, `/case-studies/service-plan`, `/case-studies/uncharted` |
| `/create/ai-video-generator` | FAQ questions | Accordion panels. |
| `/create/ai-video-generator` | Related generator links | More `/create/…` and `/reframe/…` marketing pages. Same template. One sibling captured. |
| `/contact-sales` | Same sales form as enterprise | Not filled. Not submitted. |
| `/whitepaper` | Join the waitlist (`#form`) | Form with name, email, company, role, and a phone field. Not filled. Not submitted. |
| `/creative-partner-program` | Application fields, Select one, Submit | Not filled. Not submitted. |
| `/education/educator` | Educator application, including a phone field | Not filled. Not submitted. |
| `/education/student` | Student page controls | Public page. Any apply form is not submitted. |
| `/photon` | Previous, Next, Scroll to page 1–5 | Local carousel. |
| `/photon` | Join us, API, Start Building | Older routes (`/join`, `/dream-machine/api`, `/dream-machine/api/keys`). Keys URL is an account wall. Stop. |
| `/photon` | Ray2, Genie, Capture, pricing, careers | Older site paths. Not in the current sitemap. Recorded. Not used as the current product. |

## Sitemap (27 locs)

`/`, `/about`, `/agents-guide`, `/api`, `/app`, `/careers`, `/case-studies`, `/changelog`, `/contact-sales`, `/creative-partner-program`, `/dreamlab/featured`, `/education/educator`, `/education/student`, `/enterprise`, `/learning-center`, `/llm-info`, `/mcp`, `/news`, `/news/packed-multimodal-attention`, `/pricing`, `/ray`, `/series-b`, `/the-state-of-ai-2026-annual-trend-report`, `/uni-1`, `/uni-1/showcase`, `/whitepaper`, `/photon`.

## Page controls

| Page | Control | Opens |
|---|---|---|
| `/app` | Monthly, Yearly | Local billing toggle. |
| `/app` | FAQ questions (`aria-expanded=false`) | Accordion panels on the same page. |
| `/app` | Try for free, use-case cards | `https://app.lumalabs.ai/` signup wall. Stop. |
| `/app` | Contact Sales | `/enterprise` |
| `/app` | Explore all features | `/learning-center` |
| `/pricing` | Plan CTAs | Signup wall (`app.lumalabs.ai` or auth). Stop. |
| `/api` | Code and model tabs | Local tab panels. |
| `/enterprise` | Contact / demo links | `/contact-sales` where linked. Forms not submitted. |
| `/mcp` | Connector links | Public MCP page sections. App store links that need an account are walls. |
| `/news` | Article titles, filters if present | Individual `/news/<slug>` pages. Index only plus the articles linked from home. |
| `/careers` | Role links | `/join?role=…` style role pages when they stay on lumalabs.ai. Application forms not submitted. |
| `/ray`, `/uni-1` | Model tabs, showcase links | Local panels and `/uni-1/showcase`. |
| `/learning-center` | Article cards | Public learning articles. |
| `/create/*` | Generator CTAs | Signup wall. Stop. |
| `/case-studies` | Study cards | Individual public case studies linked on the index. |
| `/creative-partner-program`, `/education/*` | Apply or enroll | Recorded. Forms not submitted. |
| `/contact-sales`, `/whitepaper#form` | Form fields | Visible public fields. Not filled, not submitted. |
| `/photon` | Previous, Next, Scroll to page N | Local carousel. |
| `/photon` | Join us, API, Start Building | Older routes and an API keys URL. Keys URL is an account wall. Stop. |

## Auth wall (known probe)

Sign In and Try for free go to `https://app.lumalabs.ai/`, which redirects to `https://auth.lumalabs.ai/sign-up` with a session query. The page title was "Sign up". Visible controls: first name, last name, email, Continue, Continue with Google, Continue with Apple, and a Sign in link to `https://auth.lumalabs.ai/`. Nothing was typed. Continue was not pressed. Google and Apple were not clicked. The password field, passkey, and email-code step were not reached, because reaching them would mean submitting the email form.

## Not followed

- Social profiles (Instagram, YouTube, X, TikTok, LinkedIn, Discord).
- Google Drive media kit.
- `auth.lumalabs.ai` past the signup URL.
- Any form submit, newsletter field, or account field.
