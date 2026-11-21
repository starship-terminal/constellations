# Scale public site tree

Mapped from https://scale.com/ in headless Chromium before screenshots, on 2026-11-21. Desktop viewport 1440×900. The phone drawer was mapped the same way at 390×844. OneTrust's cookie banner (`#onetrust-consent-sdk`) covers the page on first load. It was hidden in CSS and never clicked, so no consent POST was sent.

This file is the control map. It is not a claim that every leaf was screenshotted. Capture status lives in [README.md](README.md).

## Header (desktop)

The bar is a fixed header. Four buttons open mega-menus (`aria-haspopup`, `aria-expanded`). Escape closes the open menu. "Log In" and "Get Started" are links, not menus.

| Control | Opens |
|---|---|
| Logo "Home" | https://scale.com/ |
| Products | Mega-menu, below |
| Solutions | Mega-menu, below |
| Research | Mega-menu, below |
| Resources | Mega-menu, below |
| Log In | https://dashboard.scale.com/login (login wall; this branch stops) |
| Get Started | https://scale.com/demo (lead form; not submitted) |

### Products menu

| Label | URL |
|---|---|
| Scale Data Engine | https://scale.com/data-engine |
| For Generative AI | https://scale.com/generative-ai-data-engine |
| For Physical AI | https://scale.com/physical-ai |
| For Government | https://scale.com/public-sector-data-engine |
| For Automotive | https://scale.com/automotive |
| RL Environments | https://scale.com/rlenvironments |
| Off The Shelf | https://scale.com/off-the-shelf-data |
| Experts | https://scale.com/experts |
| Scale GenAI Portfolio | https://scale.com/genai-portfolio |
| Scale Donovan | https://scale.com/donovan |
| For Model Developers | https://scale.com/evaluation/model-developers |
| For Public Sector | https://scale.com/evaluation/public-sector |
| For Enterprise | https://scale.com/evaluation/enterprise |

### Solutions menu

| Label | URL |
|---|---|
| Enterprise | https://scale.com/enterprise |
| US Public Sector | https://scale.com/public-sector |
| Global Public Sector | https://scale.com/global-public-sector |
| Insurance | https://scale.com/enterprise/insurance |
| Healthcare | https://scale.com/enterprise/healthcare |
| National Security | https://scale.com/public-sector/national-security |

### Research menu

These leave scale.com for the public labs host.

| Label | URL |
|---|---|
| Research Papers | https://labs.scale.com/papers |
| Frontier Leaderboards | https://labs.scale.com/leaderboard |
| Labs | https://labs.scale.com/ |
| Research Blog | https://labs.scale.com/blog |
| Research Careers | https://labs.scale.com/jobs |

### Resources menu

| Label | URL |
|---|---|
| About | https://scale.com/about |
| Security | https://scale.com/security |
| Guides | https://scale.com/guides |
| Careers | https://scale.com/careers |
| Contact us | https://scale.com/demo |
| Blog | https://scale.com/blog |
| Events | https://scale.com/events |
| Documentation | https://scale.com/docs |
| Partnerships | https://scale.com/partnership |
| Read the Agentic Planning eBook | https://go.scale.com/agentic-planning (external gated asset; not opened) |
| Arabic-First AI: Building From the Ground Up | https://scale.com/blog/arabic-first-ai |

## Header (phone, 390)

"Open menu" opens a drawer. The drawer repeats Products, Solutions, Research, Resources as expandable groups with the same destinations as the desktop menus, plus Log In and Get Started. Closing the drawer returns to the page underneath.

## Homepage interactions

https://scale.com/ is a long marketing page. Visible controls beyond the header:

| Control | What it does |
|---|---|
| Scroll to explore | Scrolls the hero |
| Previous slide / Next slide | Customer story carousel (CDAO, Meta, Mayo Clinic, Time, and others). Story cards link to published case pages such as https://scale.com/customers/time |
| Learn More | In-page or product links in later sections |
| Get Started (in page) | https://scale.com/demo |
| Cookie banner | OneTrust dialog. Hidden, not clicked. "Cookie Preferences" would open the OneTrust preference center (a dialog). Not opened, because the buttons POST or persist consent |

## Footer (every marketing page)

| Label | URL |
|---|---|
| Scale Data Engine | https://scale.com/data-engine |
| Scale GenAI Portfolio | https://scale.com/genai-platform (redirects to /genai-portfolio) |
| Scale Donovan | https://scale.com/donovan |
| Enterprise | https://scale.com/enterprise/agentic-solutions (redirects to /enterprise) |
| Insurance | https://scale.com/enterprise/insurance |
| Healthcare | https://scale.com/enterprise/healthcare |
| National Security | https://scale.com/public-sector/national-security |
| US Public Sector | https://scale.com/public-sector |
| Global Public Sector | https://scale.com/global-public-sector |
| About | https://scale.com/about |
| Careers | https://scale.com/careers |
| Security | https://scale.com/security |
| Terms | https://scale.com/legal/terms |
| Privacy | https://scale.com/legal/privacy |
| Modern Slavery Statement | https://scale.com/legal/modern-slavery-statement |
| Blog | https://scale.com/blog |
| Contact Us | https://scale.com/demo |
| Events | https://scale.com/events |
| Partnerships | https://scale.com/partnership |
| Data Partnerships | https://scale.com/data-partnership |
| Documentation | https://scale.com/docs |
| Brand Guidelines | https://brand.scale.com/ |
| Data Labeling | https://scale.com/guides/data-labeling-annotation-guide |
| ML Model Training | https://scale.com/guides/model-training-building |
| Diffusion Models | https://scale.com/guides/diffusion-models-guide |
| Guide To AI For ECommerce | https://scale.com/guides/ai-for-ecommerce |
| Computer Vision Applications | https://scale.com/guides/computer-vision |
| Large Language Models | https://scale.com/guides/large-language-models |
| LinkedIn | https://www.linkedin.com/company/scaleai (external) |
| X | https://x.com/scale_ai (external) |
| Terms of use | https://scale.com/legal/terms |
| Privacy policy | https://scale.com/legal/privacy |

## Page-level controls (reachable without a wall)

| Page | Control | Opens |
|---|---|---|
| /automotive | Tabs: 3D, Image, Mapping, Text, Audio | In-page modality panels |
| /automotive | Play video | Video overlay or inline player |
| /experts | Domain chips: Finance, Law & Policy, Healthcare, Software Engineering, Other Engineering, Research & Academia, Professional Services | In-page filter of expert domains |
| /experts | Testimonial tabs and Previous/Next | Testimonial carousel |
| /genai-portfolio | Previous step / Next step | Process stepper |
| /genai-portfolio | FAQ questions (vendor lock-in, IP, reliability, bad actors) | Accordion answers |
| /donovan | Tabs: Ingest Data, Agentic RAG, Agent Arsenal, Agent Interaction, Report Generation | In-page product panels |
| /enterprise/healthcare | Tabs: Order Guidance, Scheduling Intelligence, Custom Agents & Applications | In-page product panels |
| /public-sector/national-security | Problem cards and acquisition tabs (Buy Direct, OTA & CDAO, Partners, Cloud Marketplaces) | In-page panels |
| /data-partnership | Apply to partner / Refer a team | In-page tabs. Forms not submitted |
| /data-partnership | FAQ questions | Accordion answers |
| /blog | SEARCH... ⌘K | Search dialog. Not submitted |
| /blog | MORE | Category or filter menu |
| /blog | LOAD MORE | Next page of posts, same URL family |
| /events | Show more events | Expands the events list |
| /docs | Search... ⌘K | Docs search dialog |
| /docs | Ask Assistant ⌘I | Assistant panel with a question field. Not submitted |
| /docs | Change theme preference | Theme menu (the docs site publishes a theme switch; marketing pages do not) |
| /docs | Customer Dashboard | Login wall at dashboard.scale.com. Branch stops |
| /docs | On this page | In-page heading links |
| /off-the-shelf-data | Lead form (name, company, job title, work email, region, message) | Not submitted |
| /demo and /pricing | Lead form (name, company, job title, work email, region, company type, how you heard) | /pricing redirects to /demo. Not submitted |
| /careers | Job links | Individual https://scale.com/careers/<id> pages (168 in the careers sitemap). Apply buttons that open an account or application form are a wall; that branch stops |
| /guides | Guide cards | Individual guide pages under /guides/ |
| /blog | Post cards | Individual posts under /blog/ |
| /events | Event cards | Individual event pages under /events/ |

## Login wall (branch stops)

https://dashboard.scale.com/login loaded on 2026-11-21. Title: "Login to your Scale Account - Scale". Visible controls: email field, password field, "Log In", "Log in with Google", "Log in with Github", "Don't remember your password?". No password was typed. Google and GitHub were not clicked. No account was created. No code was entered.

Any control that navigates here (header Log In, docs Customer Dashboard, a careers apply flow that asks for an account) stops at this URL.

## Hosts outside the marketing shell

| Host | How it is reached | Treatment |
|---|---|---|
| labs.scale.com | Research menu | Public research site. Home, papers index, leaderboard, blog index, and jobs index are in the capture set. Individual papers (sitemap lists 168 lab URLs) are the same template and are not each screenshotted |
| brand.scale.com | Footer Brand Guidelines | Public brand site. Home only |
| go.scale.com | Resources eBook link | Gated download. Not opened |
| api-reference.scale.com | Docs sitemap (40 URLs) | API reference, linked from docs. Index captured if it loads without a wall |
| www.linkedin.com, x.com | Footer | External. Not captured |
| www.onetrust.com | Cookie policy link inside the banner | External. Not captured |

## Sitemap leaves not walked one by one

https://scale.com/sitemap.xml is an index. Child maps on 2026-11-21:

| Map | Count | Why not every URL |
|---|---|---|
| careers/sitemap.xml | 168 job posts | Same job-post template. Index plus one public post |
| blog/sitemap.xml | 59 posts | Same post template. Index plus one post linked from the homepage or resources menu |
| blog/category/sitemap.xml | 9 categories | Same listing template as /blog |
| labs.scale.com/sitemap.xml | 168 | Same paper or post template. Indexes only |
| legal/sitemap.xml | 23 | Terms, privacy, and cookie policy captured. Legacy and event terms are the same legal template |
| docs/sitemap.xml | 40 | Getting Started plus the docs shell. Customer Dashboard is the login wall |
| events, guides, customers, partnership, cms-pages | small sets | Index pages plus one example where the template differs |

Redirects observed: /pricing to /demo, /genai-platform to /genai-portfolio, /enterprise/agentic-solutions to /enterprise.
