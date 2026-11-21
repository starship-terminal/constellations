# Cohere site tree

Public map of [cohere.com](https://cohere.com/), read in headless Chromium on 2026-11-21. Desktop is 1440 wide. Phone is 390 wide. A control is listed only when it was painted (ancestor opacity above zero). Nothing was typed, submitted, or downloaded. Login and OAuth branches were recorded and not entered.

The marketing site is one light theme. `theme-color` is `#ffffff`. There is no public theme switch on cohere.com. docs.cohere.com has a Theme menu (Light, Dark, System). The hero "North" panel (search, tabs, New agent, sort) is a marketing illustration, not a live app.

## How to read this

| Mark | Meaning |
|---|---|
| page | Navigation. The control opens that URL. |
| in-page | Stays on the same URL. Menu, drawer, accordion, tab, dialog, or carousel. |
| wall | Login, register, or OAuth. Recorded, not entered. |
| external | Leaves cohere.com. Listed, not used as a capture surface. |
| form | Fields are visible. Not filled, not submitted. |

## Home

URL: `https://cohere.com/`. Title: Cohere. H1: "Your AI. Your rules."

### Promo banner

Black bar above the header. Same bar on desktop and phone.

| Control | What it does |
|---|---|
| Learn more | page `https://cohere.com/blog/rerank-5` |
| Close banner (x, `aria-label="Close banner"`) | in-page. Dismisses the promo. Does not consent to cookies. |

### Desktop header (1440)

Hover opens a mega menu. The trigger is also a link, except Resources.

| Control | Trigger | Panel |
|---|---|---|
| Logo | page `https://cohere.com/` | |
| Products | hover opens the panel. Click is page `/products` | Platform: North `/north`, Compass `/compass`, Model Vault `/solutions/model-vault`. North Capabilities: Agents `/north/agents`, Automations `/north/automations`, Skills `/north/skills`, Libraries `/north/libraries`. Models: Command `/command`, Transcribe `/transcribe`, North Small Translate `/north-small-translate`, Parse `/parse` (NEW), Embed `/embed` (NEW), Rerank `/rerank` (NEW), Models Overview `/models-overview`. Product: Products Overview `/products`, Total Cost of AI Ownership `/total-cost-of-ai-ownership`, Pricing `/pricing`. Featured card: North 2 `/north`. |
| Solutions | hover opens the panel. Click is page `/solutions` | Deployment: Private Deployments `/private-deployments`, Security `/security`, See deployment options `/deployment-options`. Industries: Financial Services, Public Sector, Technology, Telecommunications, Energy and Utilities, Healthcare, Life Sciences, Manufacturing, each `/solutions/<slug>`. Featured card: Model Vault `/solutions/model-vault`. |
| Resources | hover only. `href` is `/` and does not navigate | Insights: Customer Stories `/customer-stories`. For Developers: Developers `/developers`, Models Overview `/models-overview`, Docs `https://docs.cohere.com/` (external), Discord `https://discord.com/invite/co-mmunity` (external), LLM University `/llmu`. Connect: Partners `/partners`, Events `/events`, Webinars `https://events.cohere.com/on-demand/` (external), Merch Store `https://shop.cohere.com/` (external). Featured card: Ada `/customer-stories/ada`. |
| Blog | hover opens the panel. Click is page `/blog` | Blog `/blog`, Read more `/blog`, and three article cards (AISLE and cubic, AISLE letter of intent, North 2). Cards change with the CMS. |
| Research | hover opens the panel. Click is page `/research` | Cohere Labs `/research`. Programs: Future(s) of Work `/research/futures-of-work`, Aya Models `/research/aya`, All Papers `/research/papers`, Open Science Community `/research/open-science`, Catalyst Grants `/research/grants`. Links: Blog `/blog/tag/research`, Hugging Face `https://huggingface.co/CohereLabs` (external), Events `https://luma.com/user/CohereLabs` (external). Featured card: a research post on `/blog/`. |
| Company | hover opens the panel. Click is page `/about` | About `/about`, Careers `/careers`, Newsroom `/newsroom`. |
| Sign in | wall `https://dashboard.cohere.com/welcome/login` | Not entered. |
| Request a demo | page `/contact-sales` | Form. Not filled. |

Moving the pointer off the bar closes the mega menu. There is no search control in this header.

### Phone header and drawer (390)

| Control | What it does |
|---|---|
| Logo | page `/` |
| Open navigation menu | in-page. Full-screen drawer. Label becomes Close navigation menu. |
| Close navigation menu | in-page. Returns to the page. |
| Products, Solutions, Resources, Blog, Research, Company | in-page. Each is a button that replaces the drawer with that section. Back returns to the section list. The links inside match the desktop panels above, including the featured cards. |
| Sign in | wall `https://dashboard.cohere.com/welcome/login`. In the drawer. Not entered. |
| Request a demo | page `/contact-sales`. In the drawer. |

### Cookie banner and settings

A cookie dialog mounts over the home hero. It was not accepted or rejected.

| Control | What it does |
|---|---|
| Cookie settings (in the banner) | in-page dialog "Opt-out Preferences". |
| Close (x) on that dialog | in-page. Closes it. |
| Accept only necessary cookies | checkbox. Not toggled. |
| Save My Preferences | form. Not submitted. |
| Cancel | in-page. Closes the dialog. |
| Privacy Policy (in the banner copy) | page `/privacy` |

Footer also shows Manage Cookies. Same dialog. Not submitted.

### Home body

The hero art is a picture of the North product. Search all available agents, New agent, Sort by, Starred, My agents, Shared with me, Company agents, and the agent cards do not navigate. They are not the signed-in app.

CTAs elsewhere on the page (Get started, Try North, and the green band) follow the same two destinations as the header: `/contact-sales` or the login wall. They were not used to create an account.

## Footer

Desktop paints the columns open. Phone collapses them into buttons with `aria-expanded`. Opening one shows its links and leaves the others collapsed. Request a demo in the footer is page `/contact-sales`.

| Column (phone button) | Links |
|---|---|
| Platforms | North `/north`, Compass `/compass`, Product Overview `/products` |
| Models | Command `/command`, Transcribe `/transcribe`, Embed `/embed`, Rerank `/rerank`, Aya `/research/aya`, Parse `/parse`, North Small Translate `/north-small-translate`, Models Overview `/models-overview`, Customization `/customization`, Pricing `/pricing` |
| Industries | Financial Services, Public Sector, Telecommunications, Technology, Energy and Utilities, Healthcare, Life Sciences, Manufacturing (each `/solutions/<slug>`), Solutions Overview `/solutions` |
| Deployment | Model Vault `/solutions/model-vault`, Private Deployments `/private-deployments`, Security `/security`, Deployment Options `/deployment-options` |
| Resources | Blog `/blog`, Customer Stories `/customer-stories`, Developers `/developers`, Documentation `https://docs.cohere.com/`, LLM University `/llmu`, Help Center `/help-center` |
| Connect | Research `/research`, Partners `/partners`, Events `/events`, Webinars `https://events.cohere.com/on-demand/` |
| Company | About `/about`, Careers `/careers`, Newsroom `/newsroom` |
| Legal | Legal Center `/legal`, Trust Center `https://trustcenter.cohere.com/` (external), Privacy Policy `/privacy`, Terms of Use `/terms-of-use` |
| Social | LinkedIn, X, Instagram, Discord, Reddit, YouTube (external). Email is a `mailto:` link. Not sent. |

An English language label is in the footer DOM. On this pass it was not a painted control at 1440 or 390, so its menu was not opened. Locale URLs exist in the sitemap (`/fr/`, `/de/`, `/ja/`, `/ko/`) and were not crawled.

## Login wall

Opened only to record it. Nothing typed. Google and GitHub were not clicked.

| URL | What is on it |
|---|---|
| `https://dashboard.cohere.com/welcome/login` | Title "Login \| Cohere". Email field, password field, Log in, Continue with Google, Continue with Github, Forgot Password (`/reset-password`), Sign up (`/welcome/register`), Terms of Use, Privacy Policy, a cookie Close. Branch stops here. |
| `https://dashboard.cohere.com/` | Same wall. Header DASHBOARD on docs.cohere.com points here. |
| `https://dashboard.cohere.com/playground/generate` | Docs header PLAYGROUND. Not entered. |
| `https://dashboard.cohere.com/login` | Docs header LOG IN. Not entered. |
| `https://dashboard.cohere.com/welcome/register` | Sign up from the login card. Not entered. |
| `https://dashboard.cohere.com/reset-password` | Forgot Password. Not entered. |

## Docs

`https://docs.cohere.com/` loaded signed out. Title "Cohere Documentation | Cohere". `html` class `light`.

| Control | What it does |
|---|---|
| Announcement Learn more | page `https://docs.cohere.com/docs/rerank` |
| Dismiss announcement | in-page. Closes the docs promo. |
| Logo "docs" | page `https://docs.cohere.com/` |
| v2 API (`aria-haspopup="menu"`) | in-page menu: v2 API `https://docs.cohere.com/`, v1 API `https://docs.cohere.com/v1` |
| DASHBOARD, PLAYGROUND, LOG IN | wall. See the login table. Not entered. |
| DOCS | page `https://docs.cohere.com/` |
| COMMUNITY | external Discord invite. Not opened. |
| Theme (`aria-haspopup="menu"`) | in-page menu: Light, Dark, System. Public. Not switched on this pass, so the dark docs theme is not captured. |
| Guides and concepts | page `https://docs.cohere.com/docs/welcome` |
| API Reference | page `https://docs.cohere.com/reference/about` |
| Release Notes | page `https://docs.cohere.com/v2/changelog` |
| LLMU | page `https://cohere.com/llmu` |
| Cookbooks | page `https://docs.cohere.com/page/cookbooks` |
| Search | in-page dialog. Filters Version, Content type, HTTP method. Ask AI row. Esc closes it. No query typed. |
| Ask AI | same search dialog. No question typed. |

The docs sidebar is a long page tree (guides, API, cookbooks). This pass records the header that opens it, not every article.

## Section pages

These opened from the home tree. In-page controls are the ones that were painted. Article, paper, story, and job URLs in the sitemap (hundreds under `/blog/` and `/research/papers/`) use the same templates and were not each opened.

| Path | H1 or title | Controls |
|---|---|---|
| `/products` | products overview | Links into the Products panel destinations. |
| `/solutions` | solutions overview | Links into the industry and deployment pages. |
| `/north` | North | Product page. CTAs go to `/contact-sales` or the login wall. |
| `/north/agents`, `/north/automations`, `/north/skills`, `/north/libraries` | North capability pages | Same shell. |
| `/compass`, `/command`, `/transcribe`, `/parse`, `/embed`, `/rerank`, `/north-small-translate` | model and product pages | Same shell. |
| `/models-overview` | Explore our models | in-page filters: All Models, Generative, Search, Aya. Click stays on the URL. |
| `/pricing` | Empower your team to put AI to work | Tabs: Workplace systems, Generative models, Advanced retrieval models, Coding models. Each click stays on `/pricing` and swaps the rate table. FAQ buttons expand in place (customization, Trial API key, Production API key, and further questions). |
| `/private-deployments`, `/security`, `/deployment-options` | deployment pages | Security has a numbered carousel (1, 2, 3) that advances in place. |
| `/solutions/financial-services` and the other industry slugs | industry pages | Same shell as Solutions. |
| `/customer-stories` | Enterprise AI case studies | Story cards link to `/customer-stories/<slug>` (Ada, and others in the sitemap). |
| `/customer-stories/ada` | one story | Featured from the Resources menu. |
| `/developers` | Shape the future of business with Cohere | Previous and Next move a carousel in place. |
| `/llmu` | LLM University | Eight module buttons (Large Language Models through Cohere on AWS). Click stays on `/llmu` and reveals that module's lessons. Lessons link to `/llmu/<slug>`. |
| `/blog` | Blog | Tag links: Enterprise AI, Research, AI for Developers, Product Launch, Company News (`/blog/tag/<slug>`). Open blog search opens a dialog with a "Search articles" field and topic chips (Enterprise AI, Company News, AI for Developers, Product Launch, Research). No query typed. Close (x) dismisses it. Previous and Next paginate. |
| `/newsroom` | Newsroom | Same search button and pager as the blog. |
| `/research` | Shaping the frontier of ML research | FAQ buttons expand in place. A numbered pager (1, 2, …) moves in place. |
| `/research/papers` | Research papers | Search field (not typed). Topic chips (Agents, AI Policy, Code, Data, Evaluation, and more) filter in place. |
| `/research/futures-of-work`, `/research/aya`, `/research/open-science`, `/research/grants` | research programs | Linked from the Research menu. |
| `/events` | events index (first visible event was AWS re:Invent) | Filters stay in place: BUSINESS, TECHNICAL, RESEARCH, ALL TYPES, IN-PERSON, ONLINE. |
| `/partners` | partners | Linked from Resources. |
| `/about` | about | Linked from Company. |
| `/careers` | Join the mission to scale intelligence | In-page buttons: Benefits, Culture and Growth, Working at Cohere. FAQ expands in place. Job links go to `/careers` postings. No application was started. `/careers/internships` is in the sitemap. |
| `/legal` | Cohere Legal Terms & Policies | Website Terms of Use `/terms-of-use`, Commercial SaaS Agreement `/saas-agreement`, Client License Agreement `/client-license-agreement`, Service Level Objective `/slo`, Azure AI EULA `/azure-ai-eula-for-cohere-models`, Channel Partner Marketplace Terms `/channel-partner-marketplace-tos`, Trust Center (external), Responsible Disclosure (external anchor), Security `/security`, Model Training Privacy Notice `/model-training-privacy-notice`, Enterprise Data Commitments `/enterprise-data-commitments`, Applicant Privacy Notice `/applicant-privacy`, Privacy Policy `/privacy`, Safety Modes and Usage Policy and Model docs on docs.cohere.com, one governance blog post, Secure AI Frontier Model Framework PDF (not downloaded), Modern Slavery Statement `/modern-slavery-statement`. |
| `/privacy`, `/terms-of-use` | legal documents | Long pages. No extra controls beyond the shell. |
| `/contact-sales` | Ready to put AI to work? | form. Fields seen and not filled: FirstName, LastName, Email, Title, Country (select), Phone, employee range (select), platform preference (select), products (select), use case (textarea), email opt-in (checkbox), Submit. |
| `/get-started` | get started | form. Selects for country, employee range, cloud, and product, plus Submit. Not filled. Previous and Next sit on the page. |
| `/help-center` | help center | Linked from the footer. The shell loaded. No ticket was filed. |
| `/customization`, `/total-cost-of-ai-ownership` | product explainers | Linked from the footer and the Products menu. |

## External, listed and not entered

| Control | URL |
|---|---|
| Docs | `https://docs.cohere.com/` (header recorded above) |
| Discord | `https://discord.com/invite/co-mmunity` |
| Webinars | `https://events.cohere.com/on-demand/` (loaded as a public title "On-Demand Events") |
| Merch Store | `https://shop.cohere.com/` |
| Hugging Face | `https://huggingface.co/CohereLabs` |
| Research events | `https://luma.com/user/CohereLabs` |
| Trust Center | `https://trustcenter.cohere.com/` |
| LinkedIn, X, Instagram, Reddit, YouTube | company profiles |

## Not present on the public marketing site

No public dark theme on cohere.com. No site search in the marketing header (search lives on `/blog`, `/newsroom`, `/research/papers`, and docs.cohere.com). No account menu while signed out. The North product, playground, billing, and API keys sit behind the login wall.
