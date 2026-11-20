// One-off selector probe for measure.mjs: prints the visible candidates for
// each component slot on the pages that file measures.
import { BASE, launch, open, closePromo, openFirstProduct } from './lib.mjs';

const { context, browser } = await launch();
const page = await context.newPage();
page.setDefaultTimeout(8000);

const dump = async (label, loc) => {
  const els = await loc.all();
  console.log(`--- ${label} (${els.length})`);
  for (const el of els.slice(0, 8)) {
    const i = await el.evaluate((n) => ({
      tag: n.tagName.toLowerCase(), cls: n.className.toString().slice(0, 90),
      id: n.id || '', text: (n.innerText || n.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
      vis: !!(n.offsetWidth && n.offsetHeight),
    })).catch(() => null);
    if (i) console.log('   ', JSON.stringify(i));
  }
};

// ---- home ----
await open(page, BASE + '/', { wait: 8000 });
await dump('promo bar', page.locator('[class*="announcement" i], [class*="promo-bar" i], [class*="top-bar" i], header [class*="marquee" i]').filter({ visible: true }));
await dump('header', page.locator('header, .shopify-section-group-header-group > *').filter({ visible: true }));
await dump('nav buttons', page.locator('header a, header button').filter({ visible: true }));
await dump('hero CTAs', page.locator('a.btn, a.btn-primary, .btn-primary').filter({ visible: true }));
await dump('sections h2', page.locator('h1, h2').filter({ visible: true }));
await dump('cards', page.locator('[class*="card" i]').filter({ visible: true }));
await dump('footer', page.locator('footer').filter({ visible: true }));
await dump('chat chip', page.locator('[class*="chat" i], [id*="chat" i], [class*="ai-" i]').filter({ visible: true }));
await dump('geo dialog', page.locator('[id*="geofencing"]').filter({ visible: true }));
// search overlay
await page.getByRole('button', { name: /search/i }).filter({ visible: true }).first().click().catch(() => {});
await page.waitForTimeout(2000);
await dump('search overlay', page.locator('[role="dialog"], [class*="search" i]').filter({ visible: true }));
await page.keyboard.press('Escape');
await page.waitForTimeout(800);

// ---- collection ----
await open(page, BASE + '/collections/mens', { wait: 6000 });
await dump('filter controls', page.locator('button, [role="button"]').filter({ hasText: /filter|sort/i }).filter({ visible: true }));
await page.evaluate(() => scrollTo(0, 1200));
await page.waitForTimeout(2500);
await dump('product cards', page.locator('a[href*="/products/"]').filter({ visible: true }));
await dump('card parts', page.locator('a[href*="/products/"] [class*="price" i], a[href*="/products/"] img, a[href*="/products/"] h3, [class*="badge" i]').filter({ visible: true }));

// ---- product ----
await open(page, BASE + '/products/mens-tree-runner-nz-medium-grey', { wait: 8000 });
await closePromo(page);
await dump('pdp title/price', page.locator('h1, [class*="price" i]').filter({ visible: true }));
await dump('swatches', page.locator('[class*="swatch" i], fieldset label, [class*="color" i] input, a[href*="/products/"][class*="color" i]').filter({ visible: true }));
await dump('size tabs', page.locator('[role="tab"], button, a').filter({ hasText: /men'?s sizes|women'?s sizes/i }).filter({ visible: true }));
await dump('size buttons', page.locator('button.btn-size').filter({ visible: true }));
await dump('atc', page.getByRole('button', { name: /add to cart|add to bag/i }).filter({ visible: true }));
await dump('accordion', page.locator('button[aria-expanded], details, summary, [class*="accordion" i]').filter({ visible: true }));
await dump('fit guide', page.locator('a, button').filter({ hasText: /fit guide/i }).filter({ visible: true }));
await dump('perks', page.locator('[class*="shipping" i], [class*="perk" i], [class*="guarantee" i], [class*="benefit" i]').filter({ visible: true }));
// size chip picked -> drawer contents through the header cart button. Add to
// Cart is never pressed (state change: recorded as a boundary).
const chip = page.locator('button.btn-size:not(.disabled)').filter({ visible: true }).first();
if (await chip.count()) await chip.click().catch(() => {});
await closePromo(page);
const cartBtn = page.locator('button[aria-label*="cart" i], a[aria-label*="cart" i]').filter({ visible: true }).first();
if (await cartBtn.count()) { await cartBtn.click().catch(() => {}); await page.waitForTimeout(3000); }
await dump('cart drawer', page.locator('[class*="cart" i], [role="dialog"]').filter({ visible: true }));
await dump('qty stepper', page.locator('button').filter({ hasText: /^[+\-−]$/ }).filter({ visible: true }));
await dump('express buttons', page.locator('[class*="express" i], [class*="wallet" i], [data-shopify] , .shopify-payment-button').filter({ visible: true }));
await page.close();

await browser.close();
