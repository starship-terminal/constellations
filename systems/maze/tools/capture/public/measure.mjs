// Measure Maze public components. Nothing is submitted. Login and signup
// links are measured, never followed. CookieYes is hidden, never accepted.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, CROPS, RAW } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');
page.setDefaultTimeout(10000);

const out = { _meta: { product: 'maze', capturedAt: new Date().toISOString(), theme: 'light', width: 1440, dpr: 2 }, components: {} };

function save() { fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); }

async function styleOf(locator) {
  return locator.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      borderTopColor: cs.borderTopColor,
      borderTopWidth: cs.borderTopWidth,
      borderRadius: cs.borderRadius,
      padding: cs.padding,
      height: cs.height,
      boxShadow: cs.boxShadow,
      textDecoration: cs.textDecorationLine,
      box: { x: r.x, y: r.y, w: r.width, h: r.height },
    };
  });
}

async function crop(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  return name + '.png';
}

async function forcePseudo(locator, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await locator.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(200);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, locator, note) {
  const c = (out.components[key] ??= { states: {}, page: page.url().replace(/https:\/\/maze\.co/, '') });
  const style = await styleOf(locator);
  const file = await crop(locator, `${key}-${state}`);
  c.states[state] = { ...style, crop: file, note: note || '' };
  console.log(' ', key, state, style.fontSize, style.color, style.backgroundColor);
}

async function states(key, locator, { press = false } = {}) {
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.mouse.move(8, 8);
  await page.waitForTimeout(150);
  await record(key, 'default', locator, 'measured live, light, 1440');
  const undoH = await forcePseudo(locator, ['hover']);
  await record(key, 'hover', locator, 'CSS.forcePseudoState hover');
  await undoH();
  const undoF = await forcePseudo(locator, ['focus-visible']);
  await record(key, 'focus-visible', locator, 'CSS.forcePseudoState focus-visible');
  await undoF();
  if (press) {
    const undoP = await forcePseudo(locator, ['active']);
    await record(key, 'pressed', locator, 'CSS.forcePseudoState active');
    await undoP();
  }
}

async function go(urlPath) {
  await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1500);
  await hideConsent(page);
  await page.evaluate(() => {
    document.querySelectorAll('.cky-consent-container, #cookieyes-banner').forEach((el) => el.remove());
  });
}

console.log('home');
await go('/');
const demo = page.locator('header a', { hasText: 'Get a demo' }).first();
await states('button-primary', demo, { press: true });
const trial = page.locator('header a', { hasText: 'Try Maze for free' }).first();
await states('button-secondary', trial, { press: true });
const login = page.locator('header a', { hasText: 'Log in' }).first();
await states('link-login', login, { press: true });
const pricing = page.locator('header a', { hasText: 'PRICING' }).first();
await states('nav-link', pricing, { press: true });
const h1 = page.locator('h1').first();
await record('display', 'default', h1, 'homepage h1');
const heroCta = page.locator('main a, a').filter({ hasText: 'Get a demo' }).nth(1);
if (await heroCta.count()) await record('button-primary-hero', 'default', heroCta, 'hero Get a demo');

console.log('pricing');
await go('/pricing/');
const h1p = page.locator('h1').first();
await record('pricing-title', 'default', h1p, 'pricing h1');
const planBtn = page.getByRole('link', { name: /start for free|get started|try maze/i }).first();
if (await planBtn.count()) await states('plan-cta', planBtn, { press: true });
const cards = page.locator('main section, main article, main [class*="card"]').first();
if (await cards.count()) await record('plan-region', 'default', page.locator('main').first(), 'pricing main');

console.log('demo form');
await go('/demo/');
const field = page.locator('input[type="email"], input[name="email"]').first();
if (await field.count()) {
  await field.scrollIntoViewIfNeeded();
  await record('text-field', 'default', field, 'demo email, empty, not submitted');
  await field.focus();
  await page.waitForTimeout(200);
  await record('text-field', 'focus', field, 'focused, still empty, not submitted');
}
const area = page.locator('textarea').first();
if (await area.count()) await record('text-area', 'default', area, 'present, not filled');
const select = page.locator('select').first();
if (await select.count()) await record('select', 'default', select, 'present, not changed');

console.log('footer');
await go('/');
await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(600);
await hideConsent(page);
const footerLink = page.locator('footer a').filter({ hasText: /privacy/i }).first();
if (await footerLink.count()) await states('footer-link', footerLink, { press: true });
const footer = page.locator('footer').first();
if (await footer.count()) await record('footer', 'default', footer, 'homepage footer');

save();
console.log('wrote', OUT, 'components', Object.keys(out.components).length);
await browser.close();
