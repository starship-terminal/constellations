# Patterns

Public signed-out pages. Each screenshot is a headless Playwright capture at 1440x900 CSS, devicePixelRatio 1, except the phone shot.

## Marketing home

[screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png). Fixed 64px header: wordmark, Inspiration, Lab, Pricing, Open studio, Sign in. The hero sits over a scrolling wall of look thumbnails. Eyebrow "New: share a look, remix a link", h1 "Backgrounds nobody else has, in seconds", a short lede, then Open studio and Browse inspiration.

[screenshots/home-dark-phone.png](screenshots/home-dark-phone.png) is the same page at 390x844. The nav collapses to a menu button. The h1 drops to 30px.

## Pricing

[screenshots/pricing-dark-desktop.png](screenshots/pricing-dark-desktop.png). Eyebrow PRICING, h2 "Free to create. Pro to export without limits.", a Monthly / Yearly pill, then two cards. Free is $0 with Open studio. Pryzm Pro is $9 per month with Get Pryzm Pro. Get Pryzm Pro points at `/api/checkout` and was not opened.

## Gallery

[screenshots/gallery-dark-desktop.png](screenshots/gallery-dark-desktop.png). App shell: 256px sidebar (Studios, Library, Documentation, Sign in) and an inset canvas. Filter chips, then cards. All is selected. Cards carry a PRO badge, a title, a one-line description and small effect chips.

## Sign in

[screenshots/signin-dark-desktop.png](screenshots/signin-dark-desktop.png). A 896px panel, 14px radius, card fill, shadow `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)`. Left column is the form. Right column is a look. Continue with Google, an OR rule, email, password, Reset password, Continue. Sign up swaps the heading to "Sign up for Pryzm", adds a newsletter checkbox, and changes the submit label to Create account. Nothing was submitted.

## Lab

[screenshots/lab-dark-desktop.png](screenshots/lab-dark-desktop.png). Signed-out Lab: Layers list, a live preview, Props (Grain, Blending, Animation). Share and Export are outline buttons. Save is the primary button. None of those were clicked.

## Docs, about, blog

[screenshots/docs-dark-desktop.png](screenshots/docs-dark-desktop.png) uses the app shell with a docs nav and an "On this page" list. [screenshots/about-dark-desktop.png](screenshots/about-dark-desktop.png) is a narrow marketing column. [screenshots/blog-dark-desktop.png](screenshots/blog-dark-desktop.png) is a card grid under topic chips.

## Not captured

Checkout, Google sign-in, My work, hover and focus, form errors, empty and loading states, and a light theme.
