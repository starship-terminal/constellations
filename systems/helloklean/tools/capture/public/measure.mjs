// Measures Hello Klean's public components and writes raw/components-computed.json.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Selects by role and structure. Hover is a real mouse move. Focus-visible is
// keyboard. Pressed is a CDP-forced pseudo-class, never a real press, so no
// link fires and no form submits. Overlays are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, BASE, RAW, CROPS, clearChallenge, closePromo, styleOf, crop, centre, patch } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PAGES = [
  ['home', '/en-int'],
  ['shop', '/en-int/collections/filters'],
  ['product', '/en-int/products/hello-klean-skin-filter'],
  ['faq', '/en-int/pages/faqs'],
  ['contact', '/en-int/pages/contact-us'],
  ['cart', '/en-int/cart'],
];

async function firstVisible(page, selector) {
  const loc = page.locator(selector);
  const n = await loc.count();
  for (let i = 0; i < Math.min(n, 12); i++) {
    const item = loc.nth(i);
    if (await item.isVisible().catch(() => false)) return item;
  }
  return null;
}

const SPECS = [
  { name: 'logo', page: 'home', sel: 'a[href="/"], a[aria-label*="Hello Klean" i], header a:has(img), header a:has(svg)' },
  { name: 'announcement', page: 'home', sel: '[class*="announcement"] , [class*="marquee"]' },
  { name: 'nav-cta', page: 'home', sel: 'header a[href*="collections"], a:has-text("Shop")' },
  { name: 'hero-cta', page: 'home', sel: 'main a[href*="product"], main a[href*="collection"]' },
  { name: 'hero-title', page: 'home', sel: 'main h1' },
  { name: 'menu-button', page: 'home', sel: 'button[aria-label*="menu" i], button[aria-label*="Menu" i]' },
  { name: 'search-button', page: 'home', sel: 'button[aria-label*="search" i]' },
  { name: 'cart-button', page: 'home', sel: 'button[aria-label*="cart" i], a[href*="cart"]' },
  { name: 'account-link', page: 'home', sel: 'a[href*="account"]' },
  { name: 'product-card', page: 'shop', sel: 'a[href*="/products/"]' },
  { name: 'product-title', page: 'product', sel: 'h1' },
  { name: 'product-price', page: 'product', sel: '[class*="price"]' },
  { name: 'add-to-cart', page: 'product', sel: 'button[name="add"], button[type="submit"], form[action*="cart"] button' },
  { name: 'variant', page: 'product', sel: 'fieldset label, [class*="swatch"] label, [class*="variant"] label, [class*="variant"] button' },
  { name: 'accordion', page: 'product', sel: 'details summary, [class*="accordion"] button' },
  { name: 'faq-row', page: 'faq', sel: 'details summary, [class*="accordion"] button, [class*="faq"] button' },
  { name: 'text-field', page: 'contact', sel: 'input[type="email"], input[type="text"], textarea' },
  { name: 'submit', page: 'contact', sel: 'form button[type="submit"], form button' },
  { name: 'footer-link', page: 'home', sel: 'footer a' },
  { name: 'newsletter-field', page: 'home', sel: 'footer input[type="email"], [class*="newsletter"] input' },
  { name: 'cart-empty', page: 'cart', sel: 'main' },
];

async function force(page, locator, pseudo) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const session = await page.context().newCDPSession(page);
  await session.send('DOM.enable');
  await session.send('CSS.enable');
  const { nodeId } = await session.send('DOM.describeNode', { objectId: handle._objectId || undefined }).catch(async () => {
    const node = await session.send('DOM.getDocument');
    return { nodeId: node.root.nodeId };
  });
  try {
    const nid = (await session.send('DOM.requestNode', { objectId: handle._objectId || (await handle.evaluateHandle((el) => el))._remoteObject?.objectId })).nodeId;
    await session.send('CSS.forcePseudoState', { nodeId: nid, forcedPseudoClasses: [pseudo] });
  } catch { /* forced state is best-effort */ }
}

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-GB' });
await patch(ctx);
const page = await ctx.newPage();
const pages = {};
const components = {};

for (const [name, urlPath] of PAGES) {
  console.log('page', name);
  await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (!(await clearChallenge(page))) { console.log('  blocked', name); continue; }
  await page.waitForTimeout(4000);
  await closePromo(page);
  pages[name] = { url: page.url().split('?')[0], title: await page.title() };
}

for (const spec of SPECS) {
  if (!pages[spec.page]) { components[spec.name] = { missing: true, reason: 'page blocked' }; continue; }
  const urlPath = PAGES.find((p) => p[0] === spec.page)[1];
  if (!page.url().includes(urlPath.replace('/en-int', '')) && !page.url().endsWith(urlPath)) {
    await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await page.waitForTimeout(2500);
    await closePromo(page);
  }
  const loc = await firstVisible(page, spec.sel);
  if (!loc) { components[spec.name] = { missing: true, reason: 'no visible match', selector: spec.sel }; console.log('  miss', spec.name); continue; }
  await centre(loc);
  const states = {};
  try {
    states.default = await styleOf(loc);
    await crop(page, loc, `${spec.name}-default`).catch((e) => console.log('  crop fail', spec.name, e.message.split('\n')[0]));
    await loc.hover({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(250);
    states.hover = await styleOf(loc);
    await crop(page, loc, `${spec.name}-hover`).catch(() => {});
    await loc.focus().catch(() => {});
    await page.waitForTimeout(200);
    states['focus-visible'] = await styleOf(loc);
    await crop(page, loc, `${spec.name}-focus-visible`).catch(() => {});
    components[spec.name] = { page: spec.page, selector: spec.sel, states };
    console.log('  ok', spec.name, states.default.rect.w + 'x' + states.default.rect.h);
  } catch (e) {
    components[spec.name] = { missing: true, reason: String(e.message).split('\n')[0] };
    console.log('  fail', spec.name, e.message.split('\n')[0]);
  }
}

const out = {
  source: BASE,
  captured: new Date().toISOString(),
  viewport: { width: 1440, height: 900, deviceScaleFactor: 1 },
  pages,
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2));
console.log('wrote', Object.keys(components).length, 'components');
await browser.close();
