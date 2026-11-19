# Patterns

How the signed-out surfaces are built. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Login wall

[login-light-default.png](screenshots/login-light-default.png) is a two-column page at 1440. The left pane is a promo: the glyph, a headline ("See everyday moments from your close friends.") with the spectrum on two words, and a stack of phone frames. The right pane is the form: a label, two fields, a disabled blue pill, a text link, a Facebook button, an outline Create new account pill, and the Meta mark. A hairline footer lists Meta, About, Blog, Jobs, Help, API, Privacy, Terms, Locations, and the language select.

The phone viewport drops the promo and the form. [mobile-login-light-default.png](screenshots/mobile-login-light-default.png) is a wordmark, a one-line headline, an Open Instagram pill, and a "Log in or sign up" link, with a terms bar and a tab bar that does not navigate.

Forcing `.__ig-dark-mode` darkens the promo pane and the footer and leaves the form light. [login-light-promo-dark.png](screenshots/login-light-promo-dark.png).

## Signup

Desktop [signup-light-default.png](screenshots/signup-light-default.png) is a single column on white: a back chevron, the Meta mark, a headline, email, password, birthday selects, name, username, legal copy, and a Submit that was not pressed. The phone path is a different screen. [mobile-signup-light-default.png](screenshots/mobile-signup-light-default.png) asks for a mobile number first and shows Sign up with email as a disabled wash. That boundary is why signup was not completed.

## Password reset

[password-reset-light-default.png](screenshots/password-reset-light-default.png) is the same column as signup, shorter: a headline, one field, a note about WhatsApp and SMS, and an enabled Continue pill. Continue was not pressed.

## Marketing

[about-light-default.png](screenshots/about-light-default.png) is a white page, a hamburger, a Log in link, the glyph, a three-line headline in Instagram Sans, and a pill whose border is the yellow-to-pink spectrum. [features-light-full.png](screenshots/features-light-full.png) continues that page. The spectrum colours are `core.color.spectrum`.

## Help

[help-light-default.png](screenshots/help-light-default.png) is a white app shell that does not require an account: a left rail of topics, a search field, and a list of blue links. Search was not submitted.

## Public directory and profile gate

[explore-light-default.png](screenshots/explore-light-default.png) is a country grid under a thin header with a small Log in pill and a Sign up link. [instagram-light-default.png](screenshots/instagram-light-default.png) is the public profile of `@instagram`, covered by the signup dialog. The grid behind it was not scraped.

## Privacy

[privacy-light-default.png](screenshots/privacy-light-default.png) is the Privacy Center: a left rail, a policy article, and disclosure rows. It is a document, not the app.
