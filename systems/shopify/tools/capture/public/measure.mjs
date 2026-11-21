// Measures Shopify public marketing controls. Nothing is submitted.
// PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(HERE, '..', '..', '..');
const CROPS = path.join(REF, 'components', 'crops');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const PROPS = [
  'color', 'backgroundColor', 'backgroundImage', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'textTransform', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'width', 'height', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'opacity', 'textDecorationLine',
];

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const out = { _meta: { product: 'Shopify', captured: '2026-11-21', url: 'https://www.shopify.com/?country=us&lang=en', theme: 'light', width: 1440 }, components: {} };

function styleOf(cs) {
  const o = {};
  for (const k of PROPS) o[k] = cs[k];
  return o;
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, locale: 'en-US', userAgent: UA });
const page = await ctx.newPage();
const cdp = await ctx.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function goto(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  await page.waitForTimeout(2200);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function mark(sel, tag) {
  const ok = await page.evaluate(([sel, tag]) => {
    document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
    const el = document.querySelector(sel);
    if (!el) return false;
    el.setAttribute('data-m-mark', tag);
    return true;
  }, [sel, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : null;
}

async function read(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = cs[k];
    const r = el.getBoundingClientRect();
    o._rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    return o;
  }, PROPS);
}

async function crop(loc, name) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) {
    log('  no box', name);
    return;
  }
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip });
  log('  crop', name);
}

async function forcePseudo(loc, classes) {
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function states(key, loc, { hover = true, focus = true, pressed = true } = {}) {
  out.components[key] = out.components[key] || {};
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  out.components[key].default = await read(loc);
  await crop(loc, key + '-default');
  if (hover) {
    await loc.hover().catch(() => {});
    await page.waitForTimeout(350);
    out.components[key].hover = await read(loc);
    await crop(loc, key + '-hover');
    await page.mouse.move(2, 2);
  }
  if (focus) {
    await loc.evaluate((el) => el.focus());
    await page.keyboard.press('Shift+Tab').catch(() => {});
    await page.keyboard.press('Tab').catch(() => {});
    await page.waitForTimeout(250);
    out.components[key]['focus-visible'] = await read(loc);
    await crop(loc, key + '-focus-visible');
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
  }
  if (pressed) {
    const release = await forcePseudo(loc, ['hover', 'active']);
    out.components[key].pressed = await read(loc);
    await crop(loc, key + '-pressed');
    await release();
    await loc.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  }
}

await goto('https://www.shopify.com/?country=us&lang=en');

// Primary CTA in the header (not the signup host: we only style the link)
const start = await mark('header a[href*="admin.shopify.com/signup"]', 'start');
if (start) await states('button-primary', start);

const login = await mark('header a[href*="/login"]', 'login');
if (login) await states('link-login', login);

const pricing = await mark('header a[href="/pricing"]', 'pricing');
if (pricing) await states('nav-link', pricing);

const logo = await mark('header a[href="/"]', 'logo');
if (logo) {
  out.components['logo'] = { default: await read(logo) };
  await crop(logo, 'logo-default');
}

// Why Shopify menu open, then a menu link
const why = page.locator('label[for="bk-nav-Why Shopify"]').first();
const box = await why.boundingBox();
if (box) {
  await page.mouse.move(box.x + 30, box.y + 20);
  await page.waitForTimeout(700);
  const item = page.locator('#bk-nav-level1-items > li').first().locator('a[href="/start"]').first();
  if (await item.count()) {
    out.components['menu-link'] = { default: await read(item) };
    await crop(item, 'menu-link-default');
    await item.hover();
    await page.waitForTimeout(300);
    out.components['menu-link'].hover = await read(item);
    await crop(item, 'menu-link-hover');
  }
  out.components['menu'] = { open: { note: 'Why Shopify mega menu open by hover on label[for="bk-nav-Why Shopify"]' } };
  await page.screenshot({ path: path.join(CROPS, 'menu-open.png'), clip: { x: 0, y: 0, width: 1440, height: 420 } });
}
await page.mouse.move(8, 860);
await page.waitForTimeout(300);

// Region button
const region = page.locator('button[aria-controls="language-selector-popover"]').first();
if (await region.count()) {
  await region.scrollIntoViewIfNeeded();
  await states('region-button', region, { pressed: true });
  await region.click();
  await page.waitForTimeout(600);
  const dlg = page.locator('#language-selector-popover');
  if (await dlg.count()) {
    out.components['dialog'] = { open: await read(dlg) };
    const dbox = await dlg.boundingBox();
    if (dbox) await page.screenshot({ path: path.join(CROPS, 'dialog-open.png'), clip: { x: Math.max(0, dbox.x), y: Math.max(0, dbox.y), width: Math.min(dbox.width, 1440), height: Math.min(dbox.height, 700) } });
    const close = dlg.locator('button').first();
    if (await close.count()) {
      out.components['icon-button'] = { default: await read(close) };
      await crop(close, 'icon-button-default');
      await close.hover().catch(() => {});
      out.components['icon-button'].hover = await read(close);
      await crop(close, 'icon-button-hover');
    }
    await page.keyboard.press('Escape');
  }
}

// Pricing page: switch, card, faq, plan button
await goto('https://www.shopify.com/pricing?country=us&lang=en');
const sw = page.getByRole('switch').first();
if (await sw.count()) {
  await sw.scrollIntoViewIfNeeded();
  await states('switch', sw, { pressed: false });
  const before = await read(sw);
  await sw.click();
  await page.waitForTimeout(400);
  out.components['switch'].selected = await read(sw);
  await crop(sw, 'switch-selected');
  out.components['switch'].defaultNote = before;
  await sw.click().catch(() => {});
}

const planBtn = page.locator('a, button').filter({ hasText: /^Start for free$/ }).first();
if (await planBtn.count()) {
  await planBtn.scrollIntoViewIfNeeded();
  await states('button-plan', planBtn);
}

const summary = page.locator('summary').first();
if (await summary.count()) {
  await summary.scrollIntoViewIfNeeded();
  await states('accordion', summary, { pressed: false });
  await summary.click();
  await page.waitForTimeout(400);
  out.components['accordion'].open = await read(summary);
  await crop(summary, 'accordion-open');
}

// A plan card: first heading-like price block
const card = page.locator('section, article, div').filter({ hasText: /Basic|Grow|Advanced|Plus/ }).first();
if (await card.count()) {
  const c = await card.boundingBox();
  if (c && c.height > 40 && c.height < 800) {
    out.components['card'] = { default: await read(card) };
    await crop(card, 'card-default');
  }
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2));
log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
