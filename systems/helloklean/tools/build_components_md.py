#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json and the crop folder."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CROPS = HERE / "components" / "crops"
data = {}
src = RAW / "components-computed.json"
if src.exists():
    data = json.loads(src.read_text())
comps = data.get("components", {})
crops = sorted(p.name for p in CROPS.glob("*.png")) if CROPS.exists() else []

lines = []
W = lines.append
W("# Components")
W("")
W("Measured from helloklean.com's public signed-out pages. A crop is the element as painted. A value is the computed style, not a colour read off the PNG.")
W("")
W("## Inventory")
W("")
W("| Component | Where | Size | Fill | Text | Radius | Crop |")
W("|---|---|---|---|---|---|---|")
for name, comp in comps.items():
    if comp.get("missing"):
        W(f"| {name} | {comp.get('reason', 'missing')} | | | | | |")
        continue
    d = (comp.get("states") or {}).get("default") or {}
    s = d.get("style") or {}
    r = d.get("rect") or {}
    crop = f"[crop](components/crops/{name}-default.png)" if (CROPS / f"{name}-default.png").exists() else ""
    W(f"| {name} | {comp.get('page', '')} | {r.get('w', '')} x {r.get('h', '')} | {s.get('backgroundColor', '')} | {s.get('color', '')} | {s.get('borderTopLeftRadius', '')} | {crop} |")
W("")
W("## States")
W("")
W("Hover and focus-visible were read where the element accepted them. Pressed states were not forced, so a script-applied active style is not in this file. Disabled, loading and error states do not render on the public pages that were measured.")
W("")
W("## Gaps")
W("")
W("Several selectors landed on the wrong painted control. Treat the crop as the evidence, not the component name.")
W("")
W("- `nav-cta` is the Shop All text link (56 x 18), not the header Shop Skin Filter pill.")
W("- `hero-cta` is the cart's Continue Shopping pill, measured on the cart page, not the home hero's Shop the sale pill.")
W("- `product-card` is the header Shop Skin Filter pill (150 x 34), not a shop-grid card. The grid is in [shop-light-default](screenshots/shop-light-default.png).")
W("- `add-to-cart` is the footer Subscribe pill, not the product Start now control.")
W("- `faq-row` is the hamburger glyph (22 x 14), not an FAQ question. The FAQ row is in [faq-light-default](screenshots/faq-light-default.png).")
W("- `variant` and `footer-link` missed. Colour swatches and supply cards are in [product-light-default](screenshots/product-light-default.png). Footer links are in [cart-light-default](screenshots/cart-light-default.png).")
W("- `text-field` is the contact Name field. The newsletter field is `newsletter-field`.")
W("- Checkbox, radio, switch, tooltip, toast and avatar were not measured as their own entries. The contact form shows a select, a checkbox and a textarea in [contact-light-default](screenshots/contact-light-default.png). Size pills and purchase radios are in [shampoo-light-default](screenshots/shampoo-light-default.png).")
W("- Account screens at account.helloklean.com were opened in the owner's browser and not saved: the preview host stopped producing frames.")
W("- Checkout, payment and address forms were not entered. Consent banners were hidden, never accepted or rejected.")
W("")
W(f"Crops on disk: {len(crops)}.")
W("")
(HERE / "components.md").write_text("\n".join(lines))
print("components.md", len(comps), "components", len(crops), "crops")
