# Components

Measured on the signed-out login and signup pages, and on the public home page, at 1440×900 on 2026-11-19. Values are token names where a token exists. Crops are 2x nearest-neighbour enlargements of the 1x captures, then quantized.

## Button

The product primary button is `button.next-button` on the login page.

| State | Crop | Values |
|---|---|---|
| Default | [button-primary-default.png](components/crops/button-primary-default.png) | Background `{light.accent}` (`#0073ea`). Text `{light.text.on-primary}`. Radius `{core.radius.small}` (4px). Padding 8px 16px. Height 48px. Type `{core.typography.button}`. |
| Hover | [button-primary-hover.png](components/crops/button-primary-hover.png) | Background `{light.accentHover}` (`#0060b9`). |
| Focus | [button-primary-focus.png](components/crops/button-primary-focus.png) | Same hover fill, plus a 3px ring `{light.component.button-focus-ring}` and a 1px inset of the hover blue. |

The secondary Google and Microsoft buttons are 40px tall, transparent, with a 1px `{light.border.ui}` border and 4px radius. Hover fills `rgba(103, 104, 121, 0.1)`, which is `{light.text.secondary}` at 10% and matches `--primary-background-hover-color`. Crop: [button-secondary-default.png](components/crops/button-secondary-default.png).

The marketing pill is a different control. `a.m_button-primary` on the home page is `{light.marketing.accent}` (`#6161ff`), white text, radius `{core.radius.pill}` (160px), padding 14px 32px, height 50px, Poppins 16px. Crop: [button-marketing-primary.png](components/crops/button-marketing-primary.png). Hover did not change its computed background.

Pressed, disabled and loading were not shown. Nothing was submitted.

## Text field

The login email field (`input.email-input`).

| State | Crop | Values |
|---|---|---|
| Default | [text-field-default.png](components/crops/text-field-default.png) | Background white. Text `{light.text.primary}`. Border 1px `{light.border.ui}`. Radius 4px. Padding 8px 4px 8px 12px. Height 40px. Width 360px. Figtree 16px/22px. |
| Focus | [text-field-focus.png](components/crops/text-field-focus.png) | Border becomes `{light.text.primary}` (`rgb(50, 51, 56)`). Transition `border-color 0.1s ease-in`. |

The filled state was measured and then cleared. The screenshot of the filled field was not kept.

## Link

Nav links (`a.nav_link-full`) are Poppins 14px weight 300, colour `{light.marketing.nav}` (`rgb(83, 87, 104)`), padding 8px 12px, radius 8px. Crop: [nav-default.png](components/crops/nav-default.png).

The login "Sign up" link uses `{light.text.link}` (`#1f76c2`).

## Signup form

The signup card stacks a Google button, an email field, and a blue Continue button of the same product primary style. Crop: [signup-form.png](components/crops/signup-form.png). Continue was not pressed.

## Pricing cards

Five plan cards (Free, Basic, Standard, Pro, Enterprise) with purple "Try for free" pills. Screenshot only. Crop: [pricing-cards.png](components/crops/pricing-cards.png). The seat select was not opened.

## Contact form

The sales form shows text fields, two selects, a phone field with a country code, a text area and a purple Submit pill. It asks for a phone number, so the flow stopped. Crop: [contact-form.png](components/crops/contact-form.png). Fields were not measured one by one and nothing was typed.

## Gaps

- The signed-in workspace (boards, items, automations, dashboards, settings) is behind login. Not captured.
- Login at 390px and signup at 390px show a desktop-or-app gate, not the form. See [screenshots/mobile-login-light-default.png](screenshots/mobile-login-light-default.png).
- Dark theme is declared on `.dark-app-theme` and was not painted.
- Validation, error, loading and success states were not produced. Nothing was submitted.
- Checkbox, radio, switch, tabs, tooltip, dialog, toast and menu panels were not present or did not open.
- Google and Microsoft sign-in were not followed.
- The contact form's phone field is a boundary. The flow stopped.
- Icons were not extracted. [icons/mark.svg](icons/mark.svg) is a reconstruction.
