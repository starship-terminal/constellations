// Measure Reown public components. No form submits.
// PLAYWRIGHT=... node systems/reown/tools/capture/public/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'minHeight',
  'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'textDecorationLine', 'opacity', 'gap', 'columnGap',
];

async function styleOf(page, handle) {
  return handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    for (const p of props) o[p] = s[p];
    o.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    o.tag = el.tagName.toLowerCase();
    return o;
  }, PROPS);
}

async function crop(page, handle, name) {
  const box = await handle.boundingBox();
  if (!box || box.width < 4 || box.height < 4) return null;
  const pad = 8;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 4 || clip.height < 4) return null;
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  return name + '.png';
}

async function states(page, handle, name, readings) {
  const base = await styleOf(page, handle);
  readings.push({ name, state: 'default', ...base, crop: await crop(page, handle, name + '-default') });
  await handle.hover().catch(() => {});
  await page.waitForTimeout(250);
  const hover = await styleOf(page, handle);
  readings.push({ name, state: 'hover', ...hover, crop: await crop(page, handle, name + '-hover') });
  await handle.focus().catch(() => {});
  await page.waitForTimeout(200);
  const focus = await styleOf(page, handle);
  readings.push({ name, state: 'focus-visible', ...focus, crop: await crop(page, handle, name + '-focus-visible') });
  // pressed via CDP, not a real submit
  const pressed = await handle.evaluate((el, props) => {
    el.classList.add('is-active');
    const s = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = s[p];
    el.classList.remove('is-active');
    return o;
  }, PROPS).catch(() => null);
  if (pressed) readings.push({ name, state: 'pressed', via: 'class is-active (the site adds this on the header buttons; not a mousedown)', ...pressed });
  await page.mouse.move(2, 2);
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA });
const page = await context.newPage();
const readings = [];
const layout = [];

async function recordLayout(label) {
  const row = await page.evaluate(() => ({
    url: location.href.split('?')[0],
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    scrollHeight: document.documentElement.scrollHeight,
    header: (() => {
      const h = document.querySelector('header');
      if (!h) return null;
      const r = h.getBoundingClientRect();
      const s = getComputedStyle(h);
      return { h: Math.round(r.height), position: s.position, bg: s.backgroundColor, z: s.zIndex };
    })(),
    h1: (() => {
      const h = document.querySelector('h1');
      if (!h) return null;
      const s = getComputedStyle(h);
      return { font: s.fontFamily, size: s.fontSize, weight: s.fontWeight, leading: s.lineHeight, tracking: s.letterSpacing, color: s.color };
    })(),
  }));
  layout.push({ label, ...row });
}

await page.goto('https://reown.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
await recordLayout('home-1440');

const primary = page.locator('a.button--solid.theme--blue').filter({ hasText: 'Learn' }).first();
if (await primary.count()) await states(page, primary, 'button-primary', readings);

const secondary = page.locator('a.button--solid.theme--white').filter({ hasText: 'Log in' }).first();
if (await secondary.count()) await states(page, secondary, 'button-secondary', readings);

const outline = page.locator('a.button--outline').first();
if (await outline.count()) await states(page, outline, 'button-outline', readings);

const iconBtn = page.getByRole('button', { name: 'Navigation Toggle' });
if (await iconBtn.count()) await states(page, iconBtn, 'icon-button-nav', readings);

const link = page.locator('footer a').filter({ hasText: 'Privacy Policy' }).first();
if (await link.count()) {
  await link.scrollIntoViewIfNeeded();
  await states(page, link, 'link-footer', readings);
}

const h1 = page.locator('h1').first();
if (await h1.count()) {
  const s = await styleOf(page, h1);
  readings.push({ name: 'heading-display', state: 'default', ...s, crop: await crop(page, h1, 'heading-display-default') });
}

const card = page.locator('[class*="card"]').first();
if (await card.count()) {
  await card.scrollIntoViewIfNeeded().catch(() => {});
  const s = await styleOf(page, card);
  readings.push({ name: 'card', state: 'default', ...s, crop: await crop(page, card, 'card-default') });
}

// accordion on pricing
await page.goto('https://reown.com/pricing', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
await recordLayout('pricing-1440');
const acc = page.locator('button').filter({ hasText: /\?$/ }).first();
if (await acc.count()) {
  await acc.scrollIntoViewIfNeeded();
  await states(page, acc, 'accordion', readings);
  await acc.click();
  await page.waitForTimeout(400);
  const open = await styleOf(page, acc);
  readings.push({ name: 'accordion', state: 'selected', ...open, crop: await crop(page, acc, 'accordion-selected') });
}

// text field: newsletter is visible but we only focus, never type or submit
const mail = page.locator('input[placeholder="Mail"]').first();
if (await mail.count()) {
  await mail.scrollIntoViewIfNeeded();
  await states(page, mail, 'text-field', readings);
}

// docs
await page.goto('https://docs.reown.com/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1800);
await recordLayout('docs-1440');
const search = page.getByRole('button', { name: /Search/ }).first();
if (await search.count()) await states(page, search, 'docs-search-button', readings);
const docsLink = page.locator('aside a, nav a').filter({ hasText: 'Analytics' }).first();
if (await docsLink.count()) await states(page, docsLink, 'docs-nav-link', readings);
const docsH1 = page.locator('h1').first();
if (await docsH1.count()) {
  const s = await styleOf(page, docsH1);
  readings.push({ name: 'docs-heading', state: 'default', ...s, crop: await crop(page, docsH1, 'docs-heading-default') });
}

// demo
await page.goto('https://demo.reown.com/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1800);
await recordLayout('demo-1440');
const tab = page.getByRole('tab', { name: 'Auth' });
if (await tab.count()) await states(page, tab, 'demo-tab', readings);
const tab2 = page.getByRole('tab', { name: 'Design' });
if (await tab2.count()) {
  const s = await styleOf(page, tab2);
  readings.push({ name: 'demo-tab', state: 'default-unselected', ...s });
  await tab2.click();
  await page.waitForTimeout(400);
  const sel = await styleOf(page, tab2);
  readings.push({ name: 'demo-tab', state: 'selected', ...sel, crop: await crop(page, tab2, 'demo-tab-selected') });
}
const checkbox = page.locator('[role="checkbox"]').first();
if (await checkbox.count()) {
  await states(page, checkbox, 'demo-checkbox', readings);
  await checkbox.click().catch(() => {});
  await page.waitForTimeout(300);
  const sel = await styleOf(page, checkbox);
  readings.push({ name: 'demo-checkbox', state: 'selected', ...sel, crop: await crop(page, checkbox, 'demo-checkbox-selected') });
}

// mobile layout only
await page.setViewportSize({ width: 390, height: 844 });
await page.goto('https://reown.com/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
await recordLayout('home-390');

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({ capturedAt: new Date().toISOString(), readings }, null, 2));
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify({ capturedAt: new Date().toISOString(), layout }, null, 2));
console.log('readings', readings.length, 'layout', layout.length);
await browser.close();
