# Components

Measured on www.forhims.co.uk, signed out, on 2026-11-19. Crops are 256-colour PNGs. Colours in the tokens file are the values to copy. A crop shows shape and state.

## Button

Primary action. Black pill, white type, 48px tall, 48px radius, Care Sans 16px, padding 24px. Declared fill is `light.color.button.primary` (`#000000`). The computed background on the button node itself is transparent. The crop shows the painted pill.

| State | Crop |
|---|---|
| default | [hero-cta-default](components/crops/hero-cta-default.png) |
| hover | [hero-cta-hover](components/crops/hero-cta-hover.png) |

Login is a quieter pill in the nav: [login-button-default](components/crops/login-button-default.png), [login-button-hover](components/crops/login-button-hover.png).

The register drawer's Create account control is disabled until email, password and terms are set: [create-account-disabled](components/crops/create-account-disabled.png). The login submit is the same disabled grey (`#d5dade`, `light.color.button.disabled`): [login-submit-disabled](components/crops/login-submit-disabled.png).

## Icon button

The nav menu button, 56 by 36, icon only: [menu-button-default](components/crops/menu-button-default.png).

## Link

Nav links are Care Sans, near-black. Weight is the sample: [nav-link-default](components/crops/nav-link-default.png), [nav-link-hover](components/crops/nav-link-hover.png). Footer: [footer-link-default](components/crops/footer-link-default.png). A Sex menu item: [nav-menu-link-default](components/crops/nav-menu-link-default.png). Text buttons on the login card: [text-button-default](components/crops/text-button-default.png), [text-button-create](components/crops/text-button-create.png).

## Text field

White, 12px radius, about 60px tall, 16px Care Sans. Error copy is `#ce2f24` (`light.color.form.error`).

| State | Crop |
|---|---|
| default | [input-default](components/crops/input-default.png) |
| focus | [input-focus](components/crops/input-focus.png) |
| filled | [input-filled](components/crops/input-filled.png) |
| error | [input-error-default](components/crops/input-error-default.png) |

The filled crop is an empty field. It is not an account.

## Checkbox

Register drawer, terms. Default and focus. Not ticked in the measurement run: [checkbox-default](components/crops/checkbox-default.png), [checkbox-focus](components/crops/checkbox-focus.png).

## Menu and dialog

The hamburger opens a right drawer (Account, Explore): see [home-light-menu](screenshots/home-light-menu.png). Create an account opens a register drawer: [drawer-register](components/crops/drawer-register.png).

## Card

Category cards on the home hero. Warm surface, product photo, italic colour word: [category-card-default](components/crops/category-card-default.png), [category-card-hover](components/crops/category-card-hover.png).

## Wordmark and title

[logo-default](components/crops/logo-default.png). Hero title: [hero-title-default](components/crops/hero-title-default.png). Login heading: [login-title-default](components/crops/login-title-default.png).

## Gaps

Text area, select, radio, switch, tooltip, toast, avatar, badge, table, and list row were not on the captured surfaces. Focus-visible was read as focus on the email field and the terms checkbox. Pressed and loading were not held. The care-portal account menu click did not paint a drawer in the 1440 screenshot. Profile Edit, payment Edit, and support pills were not opened, because those paths ask for a phone number, a birthday, a card, or a medical question.
