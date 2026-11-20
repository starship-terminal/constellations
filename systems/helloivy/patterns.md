# Hello Ivy patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Three surfaces carry two unrelated design layers: **www.helloivy.co** (the Framer marketing build — its whole theme is five hashed `--token-*` variables re-pointed per theme), **app.helloivy.co** (the Vue product — its own semantic `--*-color` layer delivered as an inline theme block, seen signed-out only at /login and the public share route), and the hosted **/docs** platform (a third surface, General Sans, sharing neither layer).

## The marketing shell

Every www.helloivy.co page boots `html[toggle-theme=light]` on the cream ground (`--token-8cbad9a1…` → `light.color.ground` **#faf6f0**). A **116px top strip** (`nav-bar`, a `div[data-framer-name]` element — Framer paints no semantic `header`) carries the wordmark, the nav links (`nav-link`, Inter 16/19.2 600 in `color.ink`), the **"Start for free" pill CTA** (`nav-cta`, 154×56px, 15px 30px padding, 9999px radius, `color.ink` fill on `color.inverseSurface` text, 0.8 opacity on hover, a `#0000ee`-blue border accent in light / `#9e9eff` in dark), and the **"Menu" control** (`nav-menu-box`) whose own press opens Framer's full-screen overlay — numbered entries like "01 HOME" and "FEATURES". The overlay ignores Escape; it takes its own close control, and captures were reloaded to a clean state afterwards. The **footer** (`footer`) holds the resource columns (`footer-link`) and the real **"Change theme" control** (`theme-control`, Inter 14/21 500): its own press repaints `html[toggle-theme=dark]` — ground #16161a, ink #edecda — persisted in `localStorage.currentToggleState`. That verified repaint is the `dark` token set.

## The editorial layer

Below the strip, the marketing pages speak in **Unbounded display**: the hero heading (`hero-heading`, 82/90 w500 desktop, `m-hero-heading` 32/38 at 390px), the `hero-copy` lead (Inter 27/41), the mid-page `section-heading` (Unbounded 62/68), all in `color.ink` on `color.ground`. Feature tiles (`feature-card` headings Unbounded 34/41) and blog `post-card`s recast the grammar. `/pricing` adds the **plan columns** (`plan-card`) with their own pill CTAs (`plan-cta`) and a **FAQ accordion** (`faq-question`, Inter-Medium 16/25.6) whose question rows open answers by their own press — captured `pricing-light-faq-open`.

## The product layer (app.helloivy.co)

A different system. The public share route paints the product shell a signed-out reader can reach: a **header strip** (`share-header`, ~69px) over the document **canvas** (`share-doc`, ~795px wide, Inter 16/25.6 body — `--canvas` #fff ground, `--canvas-color` #323235 ink), with a settings popover (`share-settings`) opened through its own control — captured `app-share-light-settings-menu`. The shell dimensions are declared on `section.main_section`'s inline theme: `--sidebar-width` **242px**, `--header-height` **66px**, `--main-header-height` **65px**. The semantic palette — recorded as `core.app.color.*` — is a warm-grey ramp: `--app-color` **#37352f** ink, `--canvas` white, `--sidebar` **#F5F6F4**, `--hover` **#F3F5F7**, `--book` **#F5F6FA**, `--selection` **#F3F5F7**, `--text-selection` **#e4f2ff**, the `--comment` **#fdffe4** pin tint, the `--project` chip greys and the `--scrollBar*` ramp — around the **#3F40F2** indigo (`--main-color`, `--link-color`, `--checkbox`; the `app.color.brand` token). The surface paints light only; no dark exists to capture.

**/login at rest** is the auth boundary itself: a centred **500px card** (`login-card`, Inter ~23/28 600 heading) holding the fields (`login-input-email`, 500×48.5px, 12px 20px padding, 10px radius on #fcfcfc, `--radius.field`), the **Continue** button (`login-continue`, 500×53.25px, #222 fill → near-black on hover, Inter 17/21 500), the Google SSO row and the sign-up/forgot links. Fields were measured, the email field was given a real focus for its state, and nothing was typed or submitted.

## The docs platform

/docs is a hosted documentation surface: a **200px left nav rail** (`docs-nav`, `docs-link`, General Sans 14/20 600) beside guide articles — a separate platform that shares neither the Framer tokens nor the app palette. Light-only; no theme control was observed, so dark was correctly never captured there.

## Mobile (390px)

The marketing shell compresses to a compact strip (`m-nav-bar`, still 116px tall at 358px wide) whose `m-menu-box` control opens the drawer by its own tap; the hero drops to `m-hero-heading` (Unbounded 32/38). The app login card keeps its 500px grammar inside the small viewport.

## Motion and focus

`raw/motion.json` is the honest record: the probe found four moving elements on one sampled page, none on two others, and **prefers-reduced-motion: reduce changed nothing** on the sampled movers — recorded as behaviour `ignores`, not suppressed. Transitions read on components are short UI fades (the app's ~0.2–0.3s ease-ins and the v-calendar widget's `--vc-slide-duration` 150ms, kept in `core.motion` as the vendor's own declarations). Focus: `login-input-email` takes a real keyboard focus (border re-points); marketing controls were measured under `focus-visible` where the element held it.
