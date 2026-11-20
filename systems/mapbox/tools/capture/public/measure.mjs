// Measure Mapbox public controls and open the header menus.
// PLAYWRIGHT=... node tools/capture/public/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, chromium, UA, hideConsent } from './lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const RAW = path.join(REF, 'raw');
const SHOT = process.env.RAW || path.join(process.env.HOME, '.design-systems', 'mapbox', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOT, { recursive: true });

const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'minHeight', 'outline', 'outlineOffset', 'textDecorationLine', 'opacity',
  'gap', 'columnGap',
];

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await ctx.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await hideConsent(page);

async function readMarked(label) {
  return page.evaluate(({ label, PROPS }) => {
    const el = document.querySelector('[data-m-mark="1"]');
    if (!el) return { label, miss: true };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of PROPS) style[p] = cs[p];
    return {
      label,
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      style,
    };
  }, { label, PROPS });
}

async function mark(js) {
  await page.evaluate(() => document.querySelectorAll('[data-m-mark]').forEach((e) => e.removeAttribute('data-m-mark')));
  const ok = await page.evaluate(js);
  return ok;
}

const rows = [];
async function measure(label, marker) {
  const ok = await mark(marker);
  if (!ok) { rows.push({ label, miss: true }); console.log('miss', label); return; }
  rows.push(await readMarked(label));
  console.log('ok', label);
}

// Primary CTA: "Get started for free"
await measure('button-primary', () => {
  const el = [...document.querySelectorAll('a, button')].find((e) => /Get started for free/i.test(e.innerText || '') && e.getBoundingClientRect().width > 40 && e.getBoundingClientRect().top < 700);
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});
await page.locator('[data-m-mark="1"]').hover().catch(() => {});
await page.waitForTimeout(250);
rows.push({ ...(await readMarked('button-primary-hover')), label: 'button-primary-hover' });

await page.locator('[data-m-mark="1"]').focus().catch(() => {});
await page.waitForTimeout(150);
rows.push({ ...(await readMarked('button-primary-focus')), label: 'button-primary-focus' });

// Contact us secondary
await measure('button-secondary', () => {
  const el = [...document.querySelectorAll('a, button')].find((e) => /^Contact us$/i.test((e.innerText || '').trim()) && e.getBoundingClientRect().width > 40 && e.getBoundingClientRect().top > 80 && e.getBoundingClientRect().top < 700);
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Log in link
await measure('link-login', () => {
  const el = [...document.querySelectorAll('a')].find((e) => /^Log in$/i.test((e.innerText || '').trim()));
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Nav button
await measure('nav-products', () => {
  const el = [...document.querySelectorAll('button')].find((e) => /^Products$/.test((e.innerText || '').trim()) && e.getBoundingClientRect().top < 80);
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Header bar
await measure('header', () => {
  const el = document.querySelector('header') || document.querySelector('.navbar') || document.querySelector('nav');
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Footer
await measure('footer', () => {
  const el = document.querySelector('footer');
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Open Products menu and measure a menu link
const products = page.getByRole('button', { name: 'Products', exact: true }).first();
await products.click();
await page.waitForTimeout(500);
await screenshotWithMetadata(page, { path: `${SHOT}/home-light-menu-products.png` }, {
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: BASE + '/',
});
await measure('menu-link', () => {
  const el = [...document.querySelectorAll('a')].find((e) => /Mapbox GL JS/.test(e.innerText || '') && e.getBoundingClientRect().height > 10 && e.getBoundingClientRect().top > 40 && e.getBoundingClientRect().top < 500);
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});
await page.keyboard.press('Escape');
await page.waitForTimeout(200);

// Language menu
const lang = page.getByRole('button', { name: 'EN', exact: true }).first();
await lang.click().catch(() => {});
await page.waitForTimeout(400);
await screenshotWithMetadata(page, { path: `${SHOT}/home-light-language.png` }, {
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: BASE + '/',
});
await page.keyboard.press('Escape');

// Pricing page controls
await page.goto(BASE + '/pricing', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);
await measure('pricing-card', () => {
  const cards = [...document.querySelectorAll('a, div, section')].filter((e) => /Get started|Contact sales|Start/i.test(e.innerText || '') && e.getBoundingClientRect().height > 80 && e.getBoundingClientRect().height < 700 && e.getBoundingClientRect().width > 180 && e.getBoundingClientRect().width < 500);
  const el = cards.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0];
  if (!el) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});

// Contact page field, do not type or submit
await page.goto(BASE + '/contact', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);
await measure('text-field', () => {
  const el = document.querySelector('input[type="text"], input[type="email"], input:not([type]), textarea');
  if (!el) return false;
  const r = el.getBoundingClientRect();
  if (r.width < 40) return false;
  el.setAttribute('data-m-mark', '1');
  return true;
});
if (await page.locator('[data-m-mark="1"]').count()) {
  await page.locator('[data-m-mark="1"]').focus().catch(() => {});
  await page.waitForTimeout(200);
  rows.push({ ...(await readMarked('text-field-focus')), label: 'text-field-focus' });
  await screenshotWithMetadata(page, { path: `${SHOT}/contact-light-field-focus.png` }, {
    viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: BASE + '/contact',
  });
}

// Search for checkbox, radio, select, switch
const controls = await page.evaluate(() => ({
  checkbox: document.querySelectorAll('input[type="checkbox"]').length,
  radio: document.querySelectorAll('input[type="radio"]').length,
  select: document.querySelectorAll('select').length,
  textarea: document.querySelectorAll('textarea').length,
  switch: document.querySelectorAll('[role="switch"]').length,
  tabs: document.querySelectorAll('[role="tab"]').length,
}));
console.log('controls', controls);

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  viewport: { width: 1440, height: 900 },
  source: BASE,
  controls,
  rows,
}, null, 2));
console.log('rows', rows.length, 'misses', rows.filter((r) => r.miss).length);
await browser.close();
