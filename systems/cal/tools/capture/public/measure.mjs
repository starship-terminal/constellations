// Measures Cal.com public components without signing in or submitting forms.
// Writes raw/components-computed.json and crops under components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, contextFor, hideBanners, isAuth, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { source: 'https://cal.com public, signed out, 2026-11-21', widths: { desktop: 1440, phone: 390 } }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const PROPS = [
  'display', 'position', 'width', 'height', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'gap', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'backgroundColor', 'color', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'textDecorationLine', 'opacity',
];

async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = cs[p];
    const r = el.getBoundingClientRect();
    o._rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  }, PROPS);
}

async function crop(page, loc, name) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 900),
  };
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  return name + '.png';
}

function put(key, state, style, extra = {}) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, extra);
  c.states[state] = { style, ...extra.stateMeta };
}

async function forcePseudo(cdp, page, loc, classes) {
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(200);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await loc.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  };
}

const browser = await chromium.launch({ headless: true });
const ctx = await contextFor(browser);
const page = await ctx.newPage();
const cdp = await ctx.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function open(url) {
  const res = await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1800);
  await hideBanners(page);
  if (isAuth(page.url())) throw new Error('auth wall ' + page.url());
  return res?.status();
}

log('home');
await open('/');

const navCta = page.locator('nav a, header a').filter({ hasText: /^Get started$/ }).first();
const signIn = page.locator('nav a, header a').filter({ hasText: /^Sign in$/ }).first();
const navLink = page.locator('nav a').filter({ hasText: /^Pricing$/ }).first();
const products = page.locator('nav button').filter({ hasText: /^Products$/ }).first();

async function states(key, loc, { click = false } = {}) {
  if (!(await loc.count())) { log('  missing', key); return; }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  const def = await styleOf(loc);
  const cropDefault = await crop(page, loc, key + '-default');
  put(key, 'default', def, { crop: cropDefault });
  await loc.hover();
  await page.waitForTimeout(250);
  put(key, 'hover', await styleOf(loc), { crop: await crop(page, loc, key + '-hover') });
  await page.mouse.move(8, 800);
  const release = await forcePseudo(cdp, page, loc, ['focus-visible']);
  put(key, 'focus-visible', await styleOf(loc), { crop: await crop(page, loc, key + '-focus-visible') });
  await release();
  const releaseP = await forcePseudo(cdp, page, loc, ['active']);
  put(key, 'pressed', await styleOf(loc), { crop: await crop(page, loc, key + '-pressed') });
  await releaseP();
  log('  measured', key);
}

await states('nav-cta', navCta);
await states('nav-signin', signIn);
await states('nav-link', navLink);
await states('nav-trigger', products);

await products.click({ force: true });
await page.waitForTimeout(600);
const menuLink = page.locator('a[href="/scheduling"]').first();
if (await menuLink.count()) {
  await states('menu-link', menuLink);
  const dialog = page.locator('[role="dialog"]').filter({ has: page.locator('a[href="/scheduling"]') }).first();
  if (await dialog.count()) {
    put('mega-menu', 'open', await styleOf(dialog), { crop: await crop(page, dialog, 'mega-menu-open'), page: 'home' });
  }
}
await page.keyboard.press('Escape');

const h1 = page.locator('h1').first();
if (await h1.count()) put('display', 'default', await styleOf(h1), { crop: await crop(page, h1, 'display-default') });
const bodyP = page.locator('main p').first();
if (await bodyP.count()) put('body-copy', 'default', await styleOf(bodyP));

log('pricing');
await open('/pricing');
const planBtn = page.getByRole('link', { name: /get started|start|choose|subscribe/i }).first();
await states('plan-cta', planBtn);
const price = page.locator('text=/\\$\\d+/').first();
if (await price.count()) put('plan-price', 'default', await styleOf(price), { crop: await crop(page, price, 'plan-price-default') });

log('login wall look only');
await page.goto('https://app.cal.com/auth/login', { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
await page.waitForTimeout(2000);
if (isAuth(page.url())) {
  const email = page.locator('input[type="email"], input[name="email"]').first();
  const pass = page.locator('input[type="password"]').first();
  const card = page.locator('form').first();
  if (await email.count()) {
    put('login-email', 'default', await styleOf(email), { crop: await crop(page, email, 'login-email-default'), note: 'look only; nothing typed' });
    await email.focus();
    await page.waitForTimeout(200);
    put('login-email', 'focus', await styleOf(email), { crop: await crop(page, email, 'login-email-focus') });
  }
  if (await pass.count()) put('login-password', 'default', await styleOf(pass), { crop: await crop(page, pass, 'login-password-default') });
  if (await card.count()) put('login-card', 'default', await styleOf(card), { crop: await crop(page, card, 'login-card-default') });
  const google = page.getByRole('button', { name: /google/i }).first();
  const link = page.getByRole('link', { name: /google/i }).first();
  const g = (await google.count()) ? google : link;
  if (await g.count()) put('oauth-google', 'default', await styleOf(g), { crop: await crop(page, g, 'oauth-google-default'), note: 'not clicked' });
}

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, 'components', Object.keys(out.components).length);
await browser.close();
