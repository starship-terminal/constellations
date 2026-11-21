// Measures public lottiefiles.com controls. Nothing is submitted.
// PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';
import { UA, BASE, hideConsent } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(REF, 'raw');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PROPS = [
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'color',
  'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderRadius', 'boxShadow',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width',
  'outline', 'textDecorationLine', 'opacity',
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
await context.route(/accounts\.google\.com|gsi\/client/, (r) => r.abort());
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const out = { readAt: new Date().toISOString().slice(0, 10), source: 'computed styles on lottiefiles.com public pages, 1440x900, dpr 2 crops', components: {} };

async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { tag: el.tagName, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of props) o[p] = cs[p];
    return o;
  }, PROPS);
}

async function crop(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  await locator.page().screenshot({ path: path.join(CROPS, name + '.png'), clip });
}

async function force(locator, classes) {
  const handle = await locator.elementHandle();
  if (!handle) return async () => {};
  const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => ({ nodeId: 0 }));
  // Use the documented query path.
  const node = await cdp.send('DOM.getDocument');
  return async () => {};
}

async function record(name, state, locator, via) {
  const n = await locator.count();
  if (!n) { out.components[name] ??= {}; out.components[name][state] = { missing: true, via }; return; }
  const loc = locator.first();
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const style = await styleOf(loc);
  style.via = via;
  style.url = new URL(page.url()).pathname;
  out.components[name] ??= {};
  out.components[name][state] = style;
  await crop(loc, `${name}-${state}`);
  console.log(' ', name, state, style.backgroundColor, style.color, style.fontSize, style.borderRadius);
}

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);
await page.getByRole('button', { name: 'Dismiss' }).first().click().catch(() => {});
await page.waitForTimeout(300);

await record('button-primary', 'default', page.getByRole('link', { name: 'Get started for free' }).first(), 'home hero');
await page.getByRole('link', { name: 'Get started for free' }).first().hover();
await page.waitForTimeout(250);
await record('button-primary', 'hover', page.getByRole('link', { name: 'Get started for free' }).first(), 'pointer hover');
await page.getByRole('link', { name: 'Get started for free' }).first().focus();
await page.waitForTimeout(200);
await record('button-primary', 'focus-visible', page.getByRole('link', { name: 'Get started for free' }).first(), 'focus()');

await record('button-secondary', 'default', page.getByRole('link', { name: 'Get in touch' }).first(), 'home hero');
await page.getByRole('link', { name: 'Get in touch' }).first().hover();
await page.waitForTimeout(200);
await record('button-secondary', 'hover', page.getByRole('link', { name: 'Get in touch' }).first(), 'pointer hover');

await record('button-signup', 'default', page.getByRole('button', { name: 'Sign up', exact: true }).first(), 'header');
await page.getByRole('button', { name: 'Sign up', exact: true }).first().hover();
await page.waitForTimeout(200);
await record('button-signup', 'hover', page.getByRole('button', { name: 'Sign up', exact: true }).first(), 'pointer hover');

await record('button-login', 'default', page.getByRole('button', { name: 'Log in', exact: true }).first(), 'header');
await record('nav-link', 'default', page.getByRole('link', { name: 'Pricing', exact: true }).first(), 'header');
await page.getByRole('link', { name: 'Pricing', exact: true }).first().hover();
await page.waitForTimeout(200);
await record('nav-link', 'hover', page.getByRole('link', { name: 'Pricing', exact: true }).first(), 'pointer hover');

await record('heading', 'default', page.getByRole('heading', { level: 1 }).first(), 'home h1');
await record('search-button', 'default', page.getByRole('button', { name: /Search animations/ }).first(), 'header search');

// menu
await page.getByRole('button', { name: 'Products', exact: true }).click();
await page.waitForTimeout(500);
await record('menu', 'opened', page.locator('[data-state="open"]').last(), 'products menu');
await page.keyboard.press('Escape');

// search dialog
await page.getByRole('button', { name: /Search animations/ }).first().click();
await page.waitForTimeout(400);
const input = page.locator('input[placeholder="Search for animations..."]').first();
await record('text-field', 'default', input, 'search dialog');
await input.focus();
await page.waitForTimeout(150);
await record('text-field', 'focus-visible', input, 'focus search');
await input.fill('loader');
await page.waitForTimeout(200);
await record('text-field', 'filled', input, 'typed loader, not submitted');
await page.keyboard.press('Escape');

await page.goto(BASE + '/pricing', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);
await record('badge', 'default', page.getByText('Individual', { exact: true }).first(), 'pricing plan name');
const price = page.locator('text=/\\$\\d+/').first();
if (await price.count()) await record('price', 'default', price, 'pricing');

await page.goto(BASE + '/free-animation/loader-cat-dWUie0iIVk', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);
const dl = page.getByRole('button', { name: 'Download', exact: true }).first();
if (await dl.count()) {
  await record('button-download', 'default', dl, 'animation page');
  await dl.hover();
  await page.waitForTimeout(200);
  await record('button-download', 'hover', dl, 'pointer hover');
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
