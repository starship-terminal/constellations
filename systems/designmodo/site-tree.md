# Designmodo public site tree

Mapped on 2026-11-21 from [https://designmodo.com/](https://designmodo.com/), signed out, in headless Chromium. A control is recorded only when it was opened or its href was read. Login, signup, SSO and identity-provider branches stop at the wall. The builder canvas was not entered.

## Header

The desktop header is `header > nav.panel.top`. Phone width replaces the centre links with `span.menu-icon.sidebarTrigger` (aria-label "Open menu").

| Control | Opens |
|---|---|
| Logo (`a.logo`) | [https://designmodo.com/](https://designmodo.com/) |
| Apps (`a.dropdownTrigger[data-dropdown-id=apps]`) | Dropdown panel `div.dropdown[data-dropdown-id=apps]`. See Apps menu. |
| Articles (`a.dropdownTrigger[data-dropdown-id=articles]`) | Dropdown panel `div.dropdown[data-dropdown-id=articles]`. See Articles menu. |
| Log In (`a.menu-link` in the header) | [https://designmodo.com/my-account/sign-in/](https://designmodo.com/my-account/sign-in/). Wall. Form not filled. |
| Sign Up (`a.button.orange`) | [https://designmodo.com/my-account/sign-up/](https://designmodo.com/my-account/sign-up/). Wall. Form not filled. |
| Open menu (phone, `span.sidebarTrigger`) | `nav.sidebar[data-sidebar-id=mobile-menu]`. The forced-open shot is [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). It did not paint as a settled drawer (a blue band over the hero). Treat that shot as a failed open, not as the menu's design. |

## Apps menu

Opened from Apps. Shot: [home-light-apps-menu.png](screenshots/home-light-apps-menu.png).

| Row | Learn More | Open App |
|---|---|---|
| Postcards | [https://designmodo.com/postcards/](https://designmodo.com/postcards/) | [https://designmodo.com/postcards/app/](https://designmodo.com/postcards/app/). Stops at the Welcome back dialog. Canvas not entered. |
| Slides | [https://designmodo.com/slides/](https://designmodo.com/slides/) | [https://designmodo.com/slides/app/](https://designmodo.com/slides/app/). Builder. Not entered. |
| Startup | [https://designmodo.com/startup/](https://designmodo.com/startup/) | [https://designmodo.com/startup/app/](https://designmodo.com/startup/app/). Builder. Not entered. |

## Articles menu

Opened from Articles. Shot: [home-light-articles-menu.png](screenshots/home-light-articles-menu.png).

| Row | Opens |
|---|---|
| Website Design | [https://designmodo.com/website/website-design/](https://designmodo.com/website/website-design/) |
| Email Design | [https://designmodo.com/email/email-design/](https://designmodo.com/email/email-design/) |
| Website Examples | [https://designmodo.com/website/website-examples/](https://designmodo.com/website/website-examples/) |
| Email Marketing | [https://designmodo.com/email/email-marketing/](https://designmodo.com/email/email-marketing/) |
| Website Tools | [https://designmodo.com/website/website-tools/](https://designmodo.com/website/website-tools/) |
| Email Tools | [https://designmodo.com/email/email-tools/](https://designmodo.com/email/email-tools/) |
| Bootstrap | [https://designmodo.com/resources/bootstrap/](https://designmodo.com/resources/bootstrap/) |
| Resources | [https://designmodo.com/resources/](https://designmodo.com/resources/) |
| View All Articles | [https://designmodo.com/articles/](https://designmodo.com/articles/) |

## Account menu

`div#account.dropdown` sits in the header markup. Shot: [home-light-account-menu.png](screenshots/home-light-account-menu.png). It opened at the left of the viewport, not under the Log In control, so the position is the panel's own placement when the `show` class is added, not a click on a visible trigger.

| Row | Opens |
|---|---|
| Log In | [https://designmodo.com/my-account/sign-in/](https://designmodo.com/my-account/sign-in/). Wall. |
| Sign Up | [https://designmodo.com/my-account/sign-up/](https://designmodo.com/my-account/sign-up/). Wall. |
| Lost Password? | [https://designmodo.com/my-account/lost-password/](https://designmodo.com/my-account/lost-password/). Wall. Form not filled. |
| Chat with us | No href. Live chat. Not opened. |

## Cart

`div#cart.dropdown`. Shot: [home-light-cart.png](screenshots/home-light-cart.png). Signed out it reads "Your cart is empty". No checkout was opened.

## Home page body

[https://designmodo.com/](https://designmodo.com/). Shot: [home-light-default.png](screenshots/home-light-default.png).

| Control | Opens |
|---|---|
| Black Friday banner | [https://designmodo.com/black-friday/](https://designmodo.com/black-friday/) |
| Scratch card in the banner | [https://designmodo.com/black-friday/#scratch](https://designmodo.com/black-friday/#scratch). Not scratched. |
| Close banner (`button` aria-label "Close banner") | Dismisses the banner on this page. Not clicked, so the banner stays in the shots. |
| Postcards / Slides / Startup tabs | In-page product switch. Not a navigation. |
| Open App (Postcards) | [https://designmodo.com/postcards/app/](https://designmodo.com/postcards/app/). Wall. |
| See more (Postcards) | [https://designmodo.com/postcards/](https://designmodo.com/postcards/) |
| Open App (Slides) | [https://designmodo.com/slides/app/](https://designmodo.com/slides/app/). Builder. Not entered. |
| See more (Slides) | [https://designmodo.com/slides/](https://designmodo.com/slides/) |
| Open App (Startup) | [https://designmodo.com/startup/app/](https://designmodo.com/startup/app/). Builder. Not entered. |
| See more (Startup) | [https://designmodo.com/startup/](https://designmodo.com/startup/) |
| Plan price links (`?add-to-cart=`) | Cart add. Not clicked. |
| Go to Pricing (Postcards dropdown) | [https://designmodo.com/postcards/pricing/](https://designmodo.com/postcards/pricing/) |
| Go to Pricing (Slides dropdown) | [https://designmodo.com/slides/pricing/](https://designmodo.com/slides/pricing/) |
| Browse Email Templates | [https://designmodo.com/email-templates/](https://designmodo.com/email-templates/) |
| Browse Website Templates | [https://designmodo.com/website-templates/](https://designmodo.com/website-templates/) |
| Browse articles | [https://designmodo.com/articles/](https://designmodo.com/articles/) |
| Article cards | Individual posts, for example [https://designmodo.com/how-to-add-a-countdown-timer-to-email/](https://designmodo.com/how-to-add-a-countdown-timer-to-email/) |
| Search form (`form.searchForm`, action `/`, field `s`) | Site search. Not submitted. |

## Product marketing

| Page | How it is reached | Notes |
|---|---|---|
| [https://designmodo.com/postcards/](https://designmodo.com/postcards/) | See more, or Apps > Learn More | Own header: Why Postcards, Solutions, Use cases, Email templates, Pricing, Log In, Open editor. |
| [https://designmodo.com/postcards/pricing/](https://designmodo.com/postcards/pricing/) | Pricing, or Go to Pricing | Plan cards. Add-to-cart links not clicked. |
| [https://designmodo.com/slides/](https://designmodo.com/slides/) | See more | |
| [https://designmodo.com/slides/pricing/](https://designmodo.com/slides/pricing/) | Go to Pricing | |
| [https://designmodo.com/startup/](https://designmodo.com/startup/) | See more | |
| [https://designmodo.com/products/](https://designmodo.com/products/) | Body link "products developed by Designmodo" | |
| [https://designmodo.com/email-templates/](https://designmodo.com/email-templates/) | Browse Email Templates | Category index. Individual template edit URLs under `/postcards/app/template/` are the builder. Not entered. |
| [https://designmodo.com/website-templates/](https://designmodo.com/website-templates/) | Browse Website Templates | |
| [https://designmodo.com/black-friday/](https://designmodo.com/black-friday/) | Banner | Promo. Scratch card not used. |

Postcards feature pages linked from the Postcards header (Create with AI Suite, Import HTML Email, Email Client Preview, and the rest of that menu) are public marketing pages under `/postcards/`. They were read in the crawl. They share the Postcards marketing chrome. They are not a separate component system.

## Account walls

These pages ask for credentials. No field was filled. Google, SSO, Apple, Facebook, Microsoft and GitHub were not clicked.

| URL | What it asks |
|---|---|
| [https://designmodo.com/my-account/sign-in/](https://designmodo.com/my-account/sign-in/) | Email and password. Also Login with Google and Login with SSO. |
| [https://designmodo.com/my-account/sign-up/](https://designmodo.com/my-account/sign-up/) | Create-account form. Not filled. |
| [https://designmodo.com/my-account/lost-password/](https://designmodo.com/my-account/lost-password/) | Password reset. Not filled. |
| [https://designmodo.com/my-account/sso-sign-in/](https://designmodo.com/my-account/sso-sign-in/) | SSO. Branch stopped. |
| [https://designmodo.com/auth/google/](https://designmodo.com/auth/google/) | Google. Not clicked. |
| [https://designmodo.com/my-account/](https://designmodo.com/my-account/) | Redirects to the sign-in wall when signed out. |

## Postcards gallery

[https://designmodo.com/postcards/app/](https://designmodo.com/postcards/app/) redirects to `/postcards/app/folder/templates` and paints a Welcome back dialog over the template gallery. The dialog close control was clicked. That dismisses the dialog in the page. It does not log in. After the close, the gallery is still behind the same dialog: the close did not leave a usable signed-out gallery. Shots: [postcards-gallery-light-welcome.png](screenshots/postcards-gallery-light-welcome.png) and [postcards-gallery-light-default.png](screenshots/postcards-gallery-light-default.png). The canvas (`/postcards/app/template/.../edit`) was not entered.

Login, Signup, Continue with Google and Sign-in with SSO on that dialog are the same walls as the account pages. Not clicked.

## Other public pages

| Page | How it is reached |
|---|---|
| [https://designmodo.com/articles/](https://designmodo.com/articles/) | View All Articles, or Browse articles |
| [https://designmodo.com/about/](https://designmodo.com/about/) | Footer "About Us" |
| [https://designmodo.com/resources/](https://designmodo.com/resources/) | Articles menu |
| [https://help.designmodo.com/](https://help.designmodo.com/) | Footer "Help Center". Opens the help centre, a different host. |

## Not entered

| Control | Why |
|---|---|
| Contact Us, Newsletter, Privacy, Terms, Cookies, DPA | Public pages. They print a street address or a contact email, so they are not in `screenshots/`. |
| Search submit, contact submit, newsletter submit, login submit | Forms. Not submitted. |
| Cookie banner Accept all, Only necessary, Save choices | Consent record. The banner is hidden in captures, never answered. |
| Add to cart, checkout | Purchase. Not clicked. |
| Slides app, Startup app, Postcards template editor | Builder canvas. Account-only for editing. Not entered. |
| Chat with us | Live chat. Not opened. |
