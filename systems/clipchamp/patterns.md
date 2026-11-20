# Clipchamp patterns

How the measured components compose clipchamp.com's public surfaces — the Microsoft React/Fluent-UI marketing site and the app.clipchamp.com sign-in boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared variable from [raw/css-vars.json](raw/css-vars.json).

## The nav bar

A 1440 x 62 white sticky bar (`header`, `position:sticky`), Segoe UI Variable ink `#232330`. Inside: the wordmark anchor (`logo`, 146.81 x 32 — the mark paints `#5a4cdb`), four dropdown triggers (`nav-item`, 108 x 44, `#545472` = `light.text.nav`), then the actions: the outline "Sign in" (`nav-signin`, 111 x 42, 1px `#433ac7` border on transparent) and the purple "Try for free" (`nav-cta`, 139 x 42, solid `#6453e4` = `light.accent` fill over a 1px same-colour border, `light.text.onAccent` label — the class is named GradientButton but paints solid). Both buttons run `radius 10px` — one step above the declared Fluent `--borderRadiusXLarge` 8px (`core.radius.xlarge`), a marketing-side step — pad `8px 30px`, and **scale 1.05 on hover** (139 → 145.95 wide) with a `0.2s ease` transition — the marketing site's signature micro-motion. Focus draws a 1px black border plus a 2px `#000000` outline offset 2px (`light.focus`).

Trigger hover opens a 248 x 810 panel (`nav-submenu`, padding `8px 24px` — hover-held; the trigger is `href="#"` with `aria-haspopup`). Link rows inside (`nav-submenu-link`, 232 x 38, `10px 16px`, `radius 12px`) paint a full `#6453e4` pill under white text on hover — the same 0.2s ease. The panel closes the moment intent moves off it, so focus/pressed on a submenu link are unreachable and were not measured.

## The hero

A solid purple band (`light.accent` family, the brand `Accent1` palette) over the white ground (`light.surface.page`, painted by `body`). "Online video editor" — `hero-title`, white, `hero-subtitle` in white @ 86.7% alpha. The CTA is the inverted style: `hero-cta` (163 x 42, `WhiteButton`) — white fill, 1px white border, `#6e006c` pink-50 text (hover `#b50ac1` pink-80), `radius 10px`, a `#1c1c28 @ 0.2` 16px/24px drop shadow that deepens to @ 0.4 on hover, and the same 1.05 hover scale. Focus on the dark band swaps the outline to `2px solid #ffffff offset 2px`.

## Buttons

One measured button language across the surface: height ~42px, `8px 30px` padding, `radius 10px`, `16px/24px 500` Segoe, `all 0.2s ease`, **1.05 scale on hover and pressed**. Three fills — solid purple (`nav-cta`/`cta-secondary`: `#6453e4` → `#4d43de` = `light.accentHover` on hover/pressed), outline (`nav-signin`: 1px `#433ac7` on transparent, hover/pressed `#4d43de` border), and white (`hero-cta`/`cta-white`/`pricing-cta`: white fill on the purple or dark bands, pink-50→pink-80 text). Mid-page CTAs (`cta-secondary`, 208 x 42) reuse the nav-cta style verbatim inside `ButtonContainer`s.

## Content blocks and the dark band

Sections alternate white and off-white (`light.surface.offWhite`, declared `--color-background-off-white #fbfbfc` — section ground only; cards read white). Copy blocks (`content-block`) run `#232330` = `light.text.primary`; feature sections on the index (`feature-section`, 1200 x 539) pair a `ContentTitle` heading (`feature-heading`) with inline entry links (`feature-link`, `#4d43de` = `light.text.link` → `#433ac7` = `light.text.linkHover` on hover, 1px `#101010` auto outline on focus). Inside the light theme sit dark bands (`core.sampled.surfaceDark` = `#313242` grey-20 as ground — the band's own element is transparent, the wrapper paints it; pixel-sampled evidence) carrying white text and the `cta-white` WhiteButton (163 x 42). Customer quotes use an asymmetric chat-bubble card (`quote`, 616 x 112, `#eaeafa` fill, `radius 2px 16px 16px`) — the one place the radius departs from the 10px button step.

## Pricing

The pricing page opens on a dark purple-gradient hero band (`pricing-hero`, 640 x 352 — the gradient is painted imagery, not a flat token) with a white `DarkHeroTitle` (`pricing-title`, 40px/48px 700) and its `pricing-cta` WhiteButton (211 x 40). Below, the Free/Premium comparison table (`plan-table`, 1280 x 625): a header row on `#eaeafa` (the table's child layers; `plan-head` is the 52 x 24 header icon, not a header cell, so the plan name and price cells were not measured), left feature-name column (`feature-row-head`, 672px), and value cells (`feature-cell`, muted `#64647c` = `light.text.muted` grey-40). `feature-tooltip` is one of those value cells read with its tooltip closed: the Fluent tooltip node inside it declares a `#302690` fill but measured 0 x 0, so no open tooltip was captured. The table carries no CTA — plan actions live in the hero and content buttons. The FAQ accordion (`faq-item`, `details`/`summary`, 696 x 56 → 696 x 208 opened) flips the title `#5d6276` → `#6453e4` purple when open — a local toggle, never a navigation.

## The sign-in card (boundary)

app.clipchamp.com/login is the app's own surface — a styled-components build, plain `Segoe UI` (not the marketing variable face), measured at rest and never submitted. A 792 x 900 white card (`signin-card`) centres a 32px/38.4px 600 title over provider rows (`signin-button`, 648 x 60, `radius 4px`, `16px` padding, 2px `#dfdfe8` border over a `#13131b @ 0.05` tint — hover `@ 0.1`, pressed `@ 0.2`, focus a 1px black border plus inset ring). **No credentials field is rendered until the email path is entered; the flow was never crossed.** Microsoft, Google and email options are measured; nothing was typed or sent.

## Footer and mobile

The 1440 x 1062 footer (`footer`) stacks link columns (`footer-link`, `#313242`, 1px `#101010` auto outline on focus), social icons (`footer-social`, 24 x 21, focus draws a `2px #6453e4` ring — the only purple focus on the surface) and a language `<select>` (`footer-lang`, 240 x 42, 1px `#2e248f` deep-indigo border, `radius 10px`) over the legal subfooter; footer headings run `#2e248f`. At 390 px the bar becomes a shadowed 390 x 72 white header (`m-header`, `#1c1c28 @ 0.15` twin shadows) with a 60 x 60 hamburger (`m-menu-button`). Its press opens a 390 x 844 white drawer (`m-menu-open`) over a `#211e4f @ 0.9` indigo scrim; rows inside (`m-menu-link`, 50 x 48, 16px/24px 500, `#1c1c1c @ 0.7`) and the same Sign-in/Try-for-free pair stretched to 310 x 42. The hero drops to `m-hero` 28px/35px 700 white.
