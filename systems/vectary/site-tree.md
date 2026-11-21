# Vectary public site tree

Mapped from https://www.vectary.com/ on 2026-11-21 in headless Chromium, signed out. The marketing host is www.vectary.com. Login and signup stay on that host. This file records the shared chrome, the homepage controls, and one page of each public template the chrome opens. A control that opens a login or signup wall is recorded and that branch stops.

Cookie overlays were hidden, not answered. No email, name, password, or code was typed. Google, Apple, GitHub, and Slack were not clicked. No form was submitted.

## Header

Present on every marketing page. At 1440 the labels sit in the bar. At 390 they move into a menu button. Product, Solutions, Business, and Resources are hover menus on desktop and tap menus on the phone. Pricing is a link.

| Control | Opens |
|---|---|
| Vectary mark | https://www.vectary.com/ |
| Product | Menu, stays on the page. See Product. |
| Solutions | Menu, stays on the page. See Solutions. |
| Business | Menu, stays on the page. See Business. |
| Resources | Menu, stays on the page. See Resources. |
| Pricing | https://www.vectary.com/pricing/ |
| Login | https://www.vectary.com/login/ . Empty identity wall. Branch stops. See [login-review.json](login-review.json). |
| Sign up | https://www.vectary.com/signup/ . Empty identity wall. Branch stops. |
| Open Vectary (signed-out nav, present in the DOM, not painted in the 1440 bar) | https://www.vectary.com/dashboard/ redirects to https://www.vectary.com/login/ . Branch stops. |
| Menu button (390) | Overlay with Product, Solutions, Business, Resources, and Pricing. Login and Sign up stay in the bar. Close returns to the page. |

## Product

Opened from the header control. The panel stays on the page. White fill, 16px radius.

| Label | Opens |
|---|---|
| Studio | https://www.vectary.com/studio-3d/ |
| Canvas | https://www.vectary.com/canvas/ |
| Workspaces | https://www.vectary.com/workspaces/ |

## Solutions

Opened from the header control. The panel stays on the page.

| Label | Opens |
|---|---|
| 3D Design | https://www.vectary.com/3d-design-tool/ |
| CAD importing | https://www.vectary.com/import-cad-file/ |
| Integrations | https://www.vectary.com/integrations/ |
| Configurators | https://www.vectary.com/3d-configurator-maker/ |
| 3D manuals | https://www.vectary.com/3d-manuals/ |
| Sharing & embedding | https://www.vectary.com/3d-file-sharing-and-embedding/ |
| Augmented Reality | https://www.vectary.com/augmented-reality/ |
| API | https://www.vectary.com/api/ |

## Business

Opened from the header control. The panel stays on the page.

| Label | Opens |
|---|---|
| Team solutions | https://www.vectary.com/business/ |
| Use cases | https://www.vectary.com/use-cases/ |
| Customer support | https://www.vectary.com/customer-success/ |
| Security | https://www.vectary.com/security/ |
| Contact sales | https://www.vectary.com/business-contact/ |

## Resources

Opened from the header control. The panel stays on the page.

| Label | Opens |
|---|---|
| Blog | https://www.vectary.com/3d-modeling-blog/ |
| Case studies | https://www.vectary.com/success-stories/ |
| Help center | https://help.vectary.com/ |
| Discord | https://discord.com/invite/kbfe4SxzMg . External. Not followed. |
| Examples | https://www.vectary.com/examples/ |

A hidden Explore dropdown also sits in the nav markup (Augmented Reality, and a 3D configurators item whose href is the homepage hash). It is marked `u__hide` and was not painted.

## Homepage controls

| Control | Opens |
|---|---|
| Yellow bar, Canvas | https://www.vectary.com/canvas/ |
| Create account | https://www.vectary.com/signup/ . Branch stops. |
| Let's talk | https://www.vectary.com/business-contact/ |
| Learn more about Canvas | https://www.vectary.com/canvas/ |
| Learn more about Studio | https://www.vectary.com/studio-3d/ |

No message was typed. The embedded 3D player failed in headless Chromium and showed "Player error". Reload Player and Send Error Log were not clicked.

## Footer

Shared on marketing pages. Dark fill.

| Column | Control | Opens |
|---|---|---|
| Company | Contact us | https://www.vectary.com/contact/ |
| Company | Pricing | https://www.vectary.com/pricing/ |
| Company | Security | https://www.vectary.com/security/ |
| Legal | Terms of Service | https://www.vectary.com/terms-of-service/ |
| Legal | Privacy Policy | https://www.vectary.com/privacy-policy/ |
| Legal | Acceptable Use Policy | https://www.vectary.com/aup/ |
| Legal | Cookie Policy | https://www.vectary.com/cookie-policy/ |
| Product | CAD importing, Configurators, 3D manuals, Sharing & embedding, Integrations, Augmented Reality, API | The same public pages as Solutions. |
| Business | Team solutions, Workspaces, Use cases, Contact sales | The same public pages as Business, plus Workspaces. |
| Industries | Automotive, Cycling, Electronics, Manufacturing, Furniture, Fashion, Consumer products, Agencies, Events | https://www.vectary.com/automotive/ and the matching industry pages. Not opened this pass. |
| Learn | Blog, Case studies, Help center, Discord, Examples | Same as Resources. |
| Learn | Tutorials | https://community.vectary.com/c/tutorials . Not followed. |
| Language | English, and de, es, fr, ja, pt, zh | Locale home pages. The menu was not opened. |
| Social | YouTube, LinkedIn, Instagram, X, Facebook | External profiles. Not followed. |

## Page templates

Each row is one template the chrome opens. Industry pages, blog posts, and example cards use the same chrome.

| Template | URL | Controls beyond the chrome |
|---|---|---|
| Home | https://www.vectary.com/ | See Homepage controls. |
| Canvas | https://www.vectary.com/canvas/ | Start creating stops at signup. BETA pill. |
| Studio | https://www.vectary.com/studio-3d/ | Create account stops at signup. Let's talk stays public. |
| Pricing | https://www.vectary.com/pricing/ | Free "Get started for free" stops at signup. Starter and Team "Get started" point at `/dashboard/?buy=`. Not followed. Business "Contact sales" is https://www.vectary.com/business-contact/ . |
| Examples | https://www.vectary.com/examples/ | Learn more stays on a public example page. Not followed past the card. |
| Contact | https://www.vectary.com/contact/ | A public form (first name, last name, email, topic, message). Not filled. Not submitted. |
| Security | https://www.vectary.com/security/ | See the ISO 27001 certificate. Not followed. |
| Help | https://help.vectary.com/ | Separate host. Not opened. |

## Auth walls

| Control | Landed URL | Stop |
|---|---|---|
| Login, Open Vectary | https://www.vectary.com/login/ | Empty wall. Google, Apple, GitHub, and Slack are offered and were not clicked. Use email was opened only far enough to see the empty fields. |
| Use email, from login | https://www.vectary.com/login-email/ | Empty email and password. Log in was not clicked. Forgot password was not opened. Log in with SSO was not opened. |
| Sign up, Create account, Get started for free | https://www.vectary.com/signup/ | Empty wall. The same four identity providers. None clicked. |
| Use email, from signup | https://www.vectary.com/signup/ | Empty name, work email, password, occupation select, and two checkboxes. Sign up was not clicked. The select was not opened. The checkboxes were not checked. |
