// Measure public Glassnode components. No typing into auth, no submits.
//
//   PLAYWRIGHT=... node tools/capture/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CROPS = path.join(REF, 'components', 'crops');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'borderRadius', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'width', 'boxShadow', 'outline', 'textDecorationLine',
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function deny() {
  await page.evaluate(() => {
    const sr = document.querySelector('#usercentrics-root')?.shadowRoot;
    const deny = sr && [...sr.querySelectorAll('button')].find((b) => /^Deny$/i.test((b.innerText || '').trim()));
    if (deny) deny.click();
  });
}

async function read(locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  return handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 48) };
    for (const p of props) o[p] = s[p];
    o.box = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  }, PROPS);
}

async function crop(locator, name) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 800),
  };
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip });
}

async function force(locator, pseudo) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => ({ nodeId: null }));
  // Use DOM.getNodeForLocation via element box instead when describe fails.
  const box = await handle.boundingBox();
  if (!box) return;
  try {
    const node = await cdp.send('DOM.getNodeForLocation', { x: Math.round(box.x + box.width / 2), y: Math.round(box.y + box.height / 2) });
    await cdp.send('CSS.forcePseudoState', { nodeId: node.nodeId, forcedPseudoClasses: pseudo });
    return node.nodeId;
  } catch {
    return null;
  }
}

async function clearPseudo(nodeId) {
  if (!nodeId) return;
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
}

const components = {};
function put(name, state, reading) {
  components[name] ??= {};
  components[name][state] = reading;
}

async function states(name, locator) {
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const def = await read(locator);
  if (!def) { console.log('miss', name); return; }
  put(name, 'default', def);
  await crop(locator, name + '-default');
  const box = await locator.boundingBox();
  if (box) {
    await page.mouse.move(box.x + box.width / 2, box.y + Math.min(box.height / 2, 20));
    await page.waitForTimeout(350);
    put(name, 'hover', await read(locator));
    await crop(locator, name + '-hover');
    await page.mouse.move(2, 2);
    await page.waitForTimeout(150);
  }
  const nodeId = await force(locator, ['hover', 'active']);
  if (nodeId) {
    put(name, 'pressed', await read(locator));
    await crop(locator, name + '-pressed');
    await clearPseudo(nodeId);
  }
  await locator.focus().catch(() => {});
  await page.waitForTimeout(150);
  put(name, 'focus-visible', await read(locator));
  await crop(locator, name + '-focus-visible');
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  console.log('measured', name);
}

await page.goto('https://glassnode.com/', { waitUntil: 'load', timeout: 70000 });
await page.waitForTimeout(2000);
await deny();
await page.waitForTimeout(400);

await states('button-launch', page.getByRole('link', { name: 'Launch Studio' }).first());
await states('button-contact', page.getByRole('link', { name: /Contact us/ }).first());
await states('nav-link', page.getByRole('link', { name: 'About', exact: true }).first());
await states('menu-trigger', page.getByRole('button', { name: 'Products', exact: true }));

await page.getByRole('button', { name: 'Products', exact: true }).click();
await page.waitForTimeout(400);
await states('menu-item', page.getByRole('link', { name: 'Studio', exact: true }).first());
await page.keyboard.press('Escape');

const email = page.locator('input[placeholder="Enter your email"]').first();
await email.scrollIntoViewIfNeeded();
await states('text-field', email);
// focus only; do not type, do not submit
await email.focus();
await page.waitForTimeout(200);
put('text-field', 'focused-empty', await read(email));
await crop(email, 'text-field-focused-empty');

await page.goto('https://studio.glassnode.com/pricing', { waitUntil: 'load', timeout: 70000 });
await page.waitForTimeout(2500);
await states('button-primary', page.getByRole('button', { name: 'Sign up' }).first());
await states('button-login', page.getByRole('button', { name: 'Log in', exact: true }));
const searchBtn = page.getByRole('button', { name: 'search' });
if (await searchBtn.count()) await states('icon-button', searchBtn.first());
const searchInput = page.locator('input[placeholder="Search"]').first();
if (await searchInput.count()) {
  await states('search-field', searchInput);
}

await page.goto('https://studio.glassnode.com/', { waitUntil: 'load', timeout: 70000 });
await page.waitForTimeout(2500);
await states('nav-studio', page.getByRole('link', { name: 'Charts', exact: true }).first());
// period radio
const period = page.getByText('24h', { exact: true }).first();
if (await period.count()) await states('radio', period);

// card-like metric tile: first visible link in the main grid
const card = page.locator('a').filter({ hasText: /Market Cap|BTC/ }).first();
if (await card.count()) await states('card', card);

await page.goto('https://glassnode.com/products/data', { waitUntil: 'load', timeout: 70000 });
await page.waitForTimeout(2200);
await deny();
const metric = page.locator('input[placeholder="Search metrics"]').first();
if (await metric.count()) await states('search-metrics', metric);
const asset = page.locator('input[placeholder="Filter assets"]').first();
if (await asset.count()) await states('search-assets', asset);
const check = page.locator('input[type="checkbox"]').first();
if (await check.count()) {
  // do not check a lead-form consent box if it is the only checkbox; prefer a catalog filter
  const label = await check.evaluate((el) => (el.closest('label')?.innerText || el.getAttribute('aria-label') || '').slice(0, 60));
  if (!/newsletter|agree|consent|privacy/i.test(label)) await states('checkbox', check);
  else put('checkbox', 'not-captured', { reason: 'only checkboxes seen were lead-form consent; not clicked' });
}

// login wall measurements, empty, no typing
await page.goto('https://studio.glassnode.com/', { waitUntil: 'load', timeout: 70000 });
await page.waitForTimeout(2000);
await page.getByRole('button', { name: 'Log in', exact: true }).click();
await page.waitForURL(/auth\.glassnode\.com/, { timeout: 20000 }).catch(() => {});
await page.waitForTimeout(1500);
const user = page.locator('input[name="username"]').first();
const pass = page.locator('input[name="password"]').first();
if (await user.count()) await states('auth-email', user);
if (await pass.count()) await states('auth-password', pass);
const cont = page.getByRole('button', { name: 'Continue', exact: true });
if (await cont.count()) {
  // measure default/hover/focus only; do not click submit
  const def = await read(cont);
  put('auth-continue', 'default', def);
  await crop(cont, 'auth-continue-default');
  const box = await cont.boundingBox();
  if (box) {
    await page.mouse.move(box.x + box.width / 2, box.y + 8);
    await page.waitForTimeout(300);
    put('auth-continue', 'hover', await read(cont));
    await crop(cont, 'auth-continue-hover');
  }
}
const google = page.getByRole('button', { name: /Continue with Google/ });
if (await google.count()) {
  put('auth-google', 'default', await read(google));
  await crop(google, 'auth-google-default');
  // do not click
}

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'computed styles on glassnode.com, studio.glassnode.com and the empty auth.glassnode.com login wall, headless Chromium 1440x900, signed out, 2026-11-21. Hover is a real pointer. Pressed is CSS.forcePseudoState. Nothing was typed or submitted.',
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('components', Object.keys(components).length);
await browser.close();
