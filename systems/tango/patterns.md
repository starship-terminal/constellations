# Patterns

Public signed-out Tango, 2026-11-19, CSS viewport 1169 by 731. No screenshots: preview frames failed.

## Marketing shell

https://www.tango.ai/ uses a fixed transparent header, 80px (`--navbar--height` is 4rem). The logo is an inline SVG in orange `#f9650f`. Nav links are Apercu Pro 16px, `#383838`. "Login" is a text button. "See a demo" is a purple outline pill. "Get started for free" is a purple fill pill. The page background is `#fafafa`. Body text is `#383838`. There is no dark theme: `prefers-color-scheme` was dark and the page stayed light.

The hero `h1` is Gelica, 63.4px / 400 / 69.8px, colour black, with a background clip of `linear-gradient(109deg, #ffa3c6 0%, #ff7c2f 40%, #fdd543 100%)`. In this browser `-webkit-text-fill-color` stayed `rgb(0, 0, 0)`, so the painted headline reads as black. The lede is Apercu Pro 21.2px / 27.6px, `#383838`.

## Pricing

https://www.tango.ai/pricing opens with a Gelica h1 at 41px. Three cards sit in a row: Free $0, Pro $22, Enterprise "Custom pricing". Cards are 340px wide, 24px padding, 16px radius. Annual pricing is the selected orange pill. A "See Team plan" switch sits on the Pro card, unchecked. A compare table lists Free, Pro and Enterprise. No plan was purchased. "Upgrade to Pro" was not followed.

## Enterprise

https://www.tango.ai/enterprise uses the same header. A 52px purple banner says "NEW Tango MCP is now live!" The h1 is Gelica 59px, white, with the same gradient clip. "Talk to sales" is an orange pill, `#ff8c49`, black text. The sales form was not opened.

## Auth

https://app.tango.us/sign-in is the signed-out login for the AI product. The host is app.tango.us. tango.us was not captured as a separate site. The column is 468px. The panel is `#faf9fa`, 404 by 667, radius 32px. The heading is Gelica 32px, `#251f2d`, "Sign in to Tango". The lede is Apercu 15px, `#524d59`. "Continue with Google" was not followed. The email field was set to kaichen@agentmail.to. A password field and "Reset password" appeared. The password was not typed. The form was not submitted.

https://app.tango.us/sign-up asks for a work email, then continues to https://app.tango.us/sign-up/email, which adds first name, last name, password, and "At least 8 characters". A hidden `cf-turnstile-response` input is in the form. The visible challenge was not shown and was not solved. The form was not submitted. Google was not followed. No card, phone, or company SSO was requested on these pages.

## What was not entered

The signed-in app, a password, a name, Google, a sales form, a card, and the Turnstile challenge were not entered. The password field appearing after an email is a signed-out step. It is not a completed login.
