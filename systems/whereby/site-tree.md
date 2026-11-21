# Whereby public site tree

Mapped on 2026-11-21 from the live public site, signed out. Official domain confirmed as `https://whereby.com/` (wordmark "Whereby", hero "Secure video calls. Zero hassle"). Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No room was joined. No signed-in app was opened.

The marketing pages paint a light surface. The home hero is blush. Pricing sits on grey. There is no public theme toggle.

origin/main already had `systems/whereby/`. This is a refresh of that slug. catalog.json was left alone. login-extracted stays not-started.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Header "Log in" | `https://whereby.com/user/login` | "Log in". Empty work email, placeholder "name@email.com". Google and Apple buttons. Submit not clicked. Identity buttons not clicked. Nothing typed. |
| Header "Sign up", "Get started", "Try for free" | `https://whereby.com/information/select-product` | Public product choice: Meetings or Embedded. Not a form. |
| Select product, then a product | Would continue toward signup | Not followed into an account form from the cards. |
| Direct signup URL | `https://whereby.com/user/signup` | "Get Started". Empty email, placeholder "Email". Empty name, placeholder "Full Name". Google and Apple. A reCAPTCHA "I'm not a robot" checkbox. Continue is disabled until the form is filled. Nothing typed. Identity buttons not clicked. Captcha not solved. Continue not clicked. |
| Login "Sign up for free" | `https://whereby.com/information/select-product` | Not followed from the login card. |
| Login "Try for free" | `https://whereby.com/user/signup` | The signup wall above. |

The login wall asks for a work email so it can send a login code. That field was left empty.

## Homepage header (`https://whereby.com/`)

Desktop, left to right: logo to `/`, Products, Pricing, Developers, Resources. Right side: Log in, Sign up. Each of the four labels opens a white dropdown on hover. No item inside a dropdown was followed into a signed-in path.

| Control | Opens |
|---|---|
| Products | "Choose the right Whereby for you". Whereby Meetings (`/information/meetings`), Whereby Embedded (`/information/embedded`), Features (`/information/features`), What's new (`https://whereby.launchnotes.io/`), Telehealth (`/information/embedded/healthcare`), eLearning (`/information/embedded/elearning`). |
| Pricing | Whereby Meetings (`/information/meetings/pricing`), Whereby Embedded (`/information/embedded/pricing`), Contact Embedded sales (`/information/contact-sales?ref=nav`), Compare products (`/information/meetings-vs-embedded`). |
| Developers | Developer docs, REST API reference, Embedded FAQs, and Tutorials on `docs.whereby.com` or YouTube. SDK links: iOS, Android, Web, React Native on GitHub or the docs. Developer Community is a Discord invite. Those external docs and the Discord invite were not captured as product pages. |
| Resources | Blog (`/blog/`), Customer stories (`/blog/customer-stories/`), Guides & Reports (`/information/guides-reports`), Partnerships (`/information/partnerships`), Support Center (`https://whereby.frontkb.com/en`), Contact Support (`mailto:support@whereby.com`), Status (`https://wherebystatus.com/`). |
| Log in | Login wall. |
| Sign up | Product select. |

Phone (390): logo and a hamburger. The hamburger opens a full-screen drawer: Products, Pricing, Developers, Resources, each with a chevron, then Login and Try for free. The drawer was photographed. No row was expanded or followed.

## Footer

On the homepage, after the closing band. Light grey fill, black type. Columns:

- About: About us, Our vision, Partnerships, Press, Careers (`careers.whereby.com`).
- Product: Embedded, Meetings, What's New, Status, Developer docs.
- Pricing: For Embedded, For Meetings.
- Connect: Blog, LinkedIn, Dev Community, Github, Instagram.
- Support: Support Center, Privacy Policy, Terms of Service, Cookie Policy, Cookie Settings, GDPR Statement, Security, Sitemap.
- Comparisons: Whereby vs Twilio, Whereby vs Zoom SDK, Whereby vs Jitsi, European Alternative.

The login app has a second footer: About, Video Conferencing, Social, Support, and Get in touch (`mailto:support@whereby.com`). That mail link was not opened.

A cookie card sits over the first view: "This website uses cookies", Cookie Policy, Cookie settings, and Accept all cookies. It was hidden with CSS for the page shots. Accept was not clicked. Cookie settings was not opened.

## Pages opened

| Page | What it is |
|---|---|
| `https://whereby.com/` | Marketing home. Blush hero. Product cards. |
| `https://whereby.com/information/pricing` | Pricing index. "Explore pricing for Whereby". Meetings and Embedded cards. |
| `https://whereby.com/information/meetings/pricing` | Meetings pricing. Free, Pro, Business. Monthly / Annual switch. |
| `https://whereby.com/information/embedded/pricing` | Embedded pricing. |
| `https://whereby.com/information/meetings` | Meetings product page. |
| `https://whereby.com/information/embedded` | Embedded product page. |
| `https://whereby.com/information/features` | Features. |
| `https://whereby.com/information/about-us/` | About. |
| `https://whereby.com/information/security/` | Security. |
| `https://whereby.com/information/tos/privacy-policy/` | Privacy policy. |
| `https://whereby.com/information/select-product` | Product choice before signup. |
| `https://whereby.com/information/this-page-does-not-exist-capture-2026/` | 404. "Not found". Take me home. HTTP 404. |
| `https://whereby.com/user/login` | Login wall. Empty. |
| `https://whereby.com/user/signup` | Signup wall. Empty. Continue disabled. Captcha not solved. |

Contact Embedded sales was listed in the Pricing menu and not opened, so a sales form was not submitted.

## Phone

390 x 844. Homepage and Meetings pricing. The homepage menu button opens the drawer above. Pricing stacks the plan cards.
