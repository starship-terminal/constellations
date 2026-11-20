# Gaps

Values that were not on a page this capture reached. They are not in tokens.json.

- Dark theme. www.rox.com has no theme switch. The home hero is a photograph, not a dark theme.
- Hover, focus-visible, pressed, disabled, loading, error. Computed styles were read at rest. The preview browser stopped producing screenshot frames, so hover was not photographed. Auth0 publishes `--base-focus-color: #a6a6a6`, `--base-hover-color: #dbdbdb`, `--error-color: #E38268` and `--success-color: #94AD7D`. Those are stylesheet variables, not a state this capture displayed. The contact form was not submitted, so its error state was not shown.
- Signed-in app. Start now and Login both go to Auth0, then offer Google and Microsoft. That is company SSO. No email was submitted. The product behind login (tables, agent runs, settings, empty and loading states) was not reached.
- Payment. Pricing lists $100 and $255 and sends the visitor to Contact sales or Start for free. No card form was shown. Nothing was purchased.
- Phone and name on the contact form. The form asks for a phone number, first name, last name and company. It was not filled in.
- Checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, avatar, badge, table. Not present on the signed-out pages that were measured. The home page has a Gartner card and a logo row. Those are marketing, not those components.
- Season Mix and Geist font files. Both are loaded by Framer as trial or placeholder faces. The files are not in this package.
- Hover colour of the nav. The nav sits on a video. Its text colour was measured as rgba(250, 250, 250, 0.8) on the home hero. On the pricing and contact pages the same nav reads as dark type on the stone page. A second nav token was not split out, because the light-page nav colour was not measured as its own computed style after the screenshot pass.
