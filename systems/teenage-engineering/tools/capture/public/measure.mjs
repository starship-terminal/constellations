// Measure teenage.engineering controls on public pages. Nothing is submitted.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and components/crops/{name}-{state}.png.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, BASE, PROPS, REF, CROPS, RAW } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

function styleOf(el, props) {
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const o = {
    text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
  };
  for (const p of props) o[p] = cs[p];
  return o;
}

async function shot(page, loc, name) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) {
    log('  no box', name);
    return null;
  }
  const pad = 8;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({ path: file, clip });
  return file;
}

async function read(page, loc) {
  return loc.evaluate(styleOf, PROPS);
}

async function forcePressed(page, loc) {
  const cdp = await page.context().newCDPSession(page);
  try {
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    const handle = await loc.elementHandle();
    if (!handle) return false;
    const described = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((e) => e))._objectId });
    const nodeId = described.node.backendNodeId;
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(80);
    return async () => {
      await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
      await cdp.detach().catch(() => {});
    };
  } catch (e) {
    await cdp.detach().catch(() => {});
    throw e;
  }
}

async function states(page, loc, id, { field = false } = {}) {
  const out = {};
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  out.default = await read(page, loc);
  await shot(page, loc, `${id}-default`);
  await loc.hover().catch(() => {});
  await page.waitForTimeout(350);
  out.hover = await read(page, loc);
  await shot(page, loc, `${id}-hover`);
  const vp = page.viewportSize();
  await page.mouse.move((vp?.width || 1440) - 2, 2);
  await page.waitForTimeout(150);
  try {
    await loc.focus();
    await page.keyboard.press('Shift+Tab');
    await page.keyboard.press('Tab');
    await page.waitForTimeout(200);
    out['focus-visible'] = await read(page, loc);
    await shot(page, loc, `${id}-focus-visible`);
  } catch (e) {
    out['focus-visible'] = { error: String(e.message).split('\n')[0] };
  }
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur());
  try {
    const release = await forcePressed(page, loc);
    out.pressed = await read(page, loc);
    await shot(page, loc, `${id}-pressed`);
    if (release) await release();
  } catch (e) {
    out.pressed = { error: String(e.message).split('\n')[0] };
  }
  if (field) {
    await loc.click().catch(() => {});
    await page.waitForTimeout(150);
    out.focused = await read(page, loc);
    await shot(page, loc, `${id}-focused`);
    // type a non-personal sample, then clear. Never submit.
    await loc.fill('sample');
    await page.waitForTimeout(150);
    out.filled = await read(page, loc);
    await shot(page, loc, `${id}-filled`);
    await loc.fill('');
    await page.keyboard.press('Escape').catch(() => {});
  }
  return out;
}

const pages = {};
const components = {};

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
const page = await context.newPage();

async function go(url) {
  log('open', url);
  await open(page, BASE + url, { wait: 1600 });
  pages[url] = { title: await page.title(), viewport: await page.evaluate(() => ({ w: innerWidth, h: innerHeight, dpr: devicePixelRatio })) };
}

const specs = [
  { id: 'logo', url: '/', sel: () => page.locator('a[href="/"]').first() },
  { id: 'nav-link', url: '/', sel: () => page.getByRole('link', { name: 'store', exact: true }).first() },
  { id: 'search-button', url: '/', sel: () => page.locator('button', { hasText: /^search$/ }).first() },
  { id: 'checkout-link', url: '/', sel: () => page.getByRole('link', { name: 'checkout', exact: true }).first() },
  { id: 'footer-link', url: '/', sel: () => page.getByRole('link', { name: 'retailers', exact: true }).first() },
  { id: 'product-tile', url: '/products', sel: () => page.locator('a[href^="/products/"]').nth(12) },
  { id: 'store-tile', url: '/store', sel: () => page.locator('a[href^="/store/bc-1"], a[href^="/store/ep-133"]').first() },
  { id: 'add-to-cart', url: '/store/ep-133', sel: () => page.locator('button', { hasText: 'add to cart' }).first() },
  { id: 'sold-out', url: '/store/op-1', sel: () => page.locator('button', { hasText: /sold out|no longer available|not available/ }).first() },
  { id: 'newsletter-field', url: '/newsletter', sel: () => page.locator('input[name="email"]'), field: true },
  { id: 'newsletter-check', url: '/newsletter', sel: () => page.locator('input[name="termsAndConditions"]') },
  { id: 'subscribe', url: '/newsletter', sel: () => page.locator('button', { hasText: 'subscribe' }).first() },
  { id: 'region-select', url: '/', sel: () => page.locator('select[name="country"]').first() },
  { id: 'notfound-title', url: '/login', sel: () => page.locator('h1, h2').first() },
];

let current = '';
for (const spec of specs) {
  try {
    if (current !== spec.url) {
      await go(spec.url);
      current = spec.url;
    }
    const loc = spec.sel();
    if (!(await loc.count())) {
      components[spec.id] = { missing: true, url: spec.url };
      log('  missing', spec.id);
      continue;
    }
    log('  measure', spec.id);
    components[spec.id] = { url: spec.url, states: await states(page, loc, spec.id, { field: spec.field }) };
    fs.writeFileSync(OUT, JSON.stringify({ pages, components }, null, 1) + '\n');
  } catch (e) {
    components[spec.id] = { error: String(e.message).split('\n')[0], url: spec.url };
    log('  FAILED', spec.id, e.message.split('\n')[0]);
    fs.writeFileSync(OUT, JSON.stringify({ pages, components }, null, 1) + '\n');
  }
}

// search field after opening search
try {
  await go('/');
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => /^search$/i.test((el.innerText || '').trim()) && el.getBoundingClientRect().width > 8);
    if (b) b.click();
  });
  await page.waitForTimeout(500);
  const loc = page.locator('input[name="search"]');
  components['search-field'] = { url: '/', states: await states(page, loc, 'search-field', { field: true }) };
  await page.keyboard.press('Escape');
} catch (e) {
  components['search-field'] = { error: String(e.message).split('\n')[0] };
}

// phone menu
const mobile = await (await launch({ mobile: true })).context;
const mp = await mobile.newPage();
try {
  await open(mp, BASE + '/', { wait: 1400 });
  const menu = mp.locator('button', { hasText: /^menu$/ }).first();
  if (await menu.count()) {
    components['menu-button'] = { url: '/', width: 390, states: await states(mp, menu, 'menu-button') };
    await menu.click();
    await mp.waitForTimeout(600);
    const item = mp.getByRole('link', { name: 'store', exact: true }).first();
    components['menu-item'] = { url: '/', width: 390, states: { default: await read(mp, item) } };
    await shot(mp, item, 'menu-item-default');
    const drawer = mp.locator('nav, [class*="menu"], [role="dialog"]').first();
    if (await drawer.count()) await shot(mp, drawer, 'menu-drawer-default');
  }
} catch (e) {
  components['menu-button'] = { error: String(e.message).split('\n')[0] };
}
await mobile.close();

fs.writeFileSync(OUT, JSON.stringify({
  readAt: new Date().toISOString().slice(0, 10),
  source: 'computed styles on live teenage.engineering, signed out, 1440x900 at 2x except menu-button at 390',
  pages,
  components,
}, null, 1) + '\n');
await browser.close();
log('wrote', OUT, Object.keys(components).length, 'components');
