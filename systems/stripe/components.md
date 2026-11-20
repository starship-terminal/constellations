# Stripe components

Public signed-out controls, measured on 2026-11-19. Values are token names. The crops are the real pixels.

## Button

Home primary (`a.hds-button--primary`, "Contact sales"): fill `light.accent` (`#533afd`), text `light.textOnAccent`, radius `core.radius.sm` (4px), height 40px, padding 11.5px 20px, label 14px / 400. Hover computed `rgb(72, 53, 221)`. The declared hover token is `light.accentHover` (`#4032c8`).

Home Sign in is `hds-button--secondary-on-quiet`: transparent fill, text `light.accent`, radius 4px, height 40px.

Pricing Contact sales (`.CtaButton.variant--Button`): fill `light.pricingAccent` (`#635bff`), radius `core.radius.pill` (16.5px), label 15px / 425, padding 3px 12px 6px 16px. A second Contact sales on the same page computed cyan `light.pricingCyan` (`#00d4ff`) with text `light.pricingText`.

Login Sign in: fill `light.dashboardAccent` (`#675dff`), radius 6px, height 44px, label 16px / 500, padding 8px 16px.

Crop: [components/crops/nav-default.png](components/crops/nav-default.png).

## Link

Nav triggers are 14px / 400, colour `light.text`. Footer links are 16px / 300, colour `rgb(80, 97, 122)`, which matches `light.muted`. Login "Forgot your password?" is 14px / 600, colour `light.pricingAccent`.

## Text field

Home newsletter slot: height 48px, radius 4px, border `1px solid rgba(212, 222, 233, 0.75)`, input colour `light.text`, placeholder "Enter work email". Focused with nothing typed: no outline, no shadow.

Contact sales email: height 48px, radius 4px, border `1px solid rgba(212, 222, 233, 0.75)`, background `rgba(255, 255, 255, 0.25)`, placeholder `jane@example.com`. Not typed.

Login email: height 44px, radius 6px, background white, ring `light.dashboardBorder`, padding 8px 12px, 16px / 300. Empty.

## Checkbox

Login "Remember me on this device" paints a 14px box, radius 4px, fill `light.dashboardAccent`. It was not clicked.

## Select

Register country shows "Singapore" in a 44px field. The menu was not opened.

## Card

Login card (`.db-RegisterAndLoginLayout-card`): width 540px, radius 12px, shadow `core.shadow.loginCard`. Register uses the same wall over a blurred dashboard image.

Crops: [components/crops/login-card-default.png](components/crops/login-card-default.png), [components/crops/register-card-default.png](components/crops/register-card-default.png).

## Gaps

- Text area, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar and badge were not on the signed-out pages that were opened, or were not opened.
- Hover, pressed, disabled, loading and error states were not captured, except the one primary hover reading above.
- Google, passkey and SSO start other sites and were not followed.
- The signed-in dashboard, KYC, card and bank flows were not entered.
