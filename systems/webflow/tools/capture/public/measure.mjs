// Measures webflow.com public components. No form submit, no login, no Google click.
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, chromium, UA, UA_MOBILE, styleOf, crop, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const browser = await chromium.launch({ headless: true });
const out = {
  _meta: {
    product: 'Webflow',
    url: BASE,
    capturedAt: new Date().toISOString(),
    note: 'Public marketing site. Login and signup are walls. No form submitted.',
  },
  components: {},
};

async function openPage(pathName, { mobile = false, theme = 'light' } = {}) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript((theme) => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    if (theme === 'dark') {
      try { localStorage.setItem('darkMode', 'true'); } catch { /* ignore */ }
    }
  }, theme);
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await page.goto(BASE + pathName, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1600);
  if (theme === 'dark') {
    await page.evaluate(() => document.documentElement.classList.add('u-mode-dark'));
    await page.waitForTimeout(300);
  }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return { page, ctx, cdp };
}

async function record(page, cdp, key, locator, state, via) {
  const loc = locator.first();
  if (!(await loc.count())) { log('  miss', key, state); return; }
  const vis = await loc.isVisible().catch(() => false);
  if (!vis) { log('  hidden', key, state); return; }
  let style;
  try { style = await styleOf(loc); } catch (e) { log('  style fail', key, e.message.split('\n')[0]); return; }
  let cropFile = null;
  try { cropFile = await crop(page, loc, `${key}-${state}`); } catch (e) { log('  crop fail', key, e.message.split('\n')[0]); }
  out.components[key] ??= { states: {} };
  out.components[key].states[state] = { via: via || 'visible', style, crop: cropFile };
  log('  ok', key, state, style.rect && `${Math.round(style.rect.w)}x${Math.round(style.rect.h)}`);
}

async function pseudo(cdp, locator, pseudoName) {
  const el = locator.first();
  if (!(await el.count())) return;
  await cdp.send('CSS.enable');
  const node = await el.evaluateHandle((n) => n);
  // Playwright CDP forcePseudoState via DOM.describeNode is awkward; use CSS.forcePseudoState on the remote object.
  try {
    const { nodeId } = await cdp.send('DOM.describeNode', { objectId: node._objectId || (await node.evaluate(() => 1), undefined) }).catch(() => ({}));
  } catch { /* fall through */ }
  await el.evaluate((n, name) => {
    n.setAttribute('data-m-pseudo', name);
  }, pseudoName);
  // Prefer the protocol when the element has a backend id.
  try {
    const backend = await cdp.send('DOM.getDocument', { depth: 0 });
    const q = await cdp.send('DOM.querySelector', { nodeId: backend.root.nodeId, selector: '[data-m-pseudo="' + pseudoName + '"]' });
    if (q.nodeId) await cdp.send('CSS.forcePseudoState', { nodeId: q.nodeId, forcedPseudoClasses: [pseudoName] });
  } catch (e) {
    log('  pseudo', pseudoName, String(e.message).split('\n')[0].slice(0, 80));
  }
}

async function homeDesktop(theme) {
  const { page, ctx, cdp } = await openPage('/', { theme });
  const suffix = theme === 'dark' ? '-dark' : '';
  await record(page, cdp, 'nav-bar' + suffix, page.locator('.nav.w-nav, header.nav').first(), 'default', 'header');
  await record(page, cdp, 'nav-link' + suffix, page.locator('.nav a[href="/pricing"], .w-nav a').filter({ hasText: /^Pricing$/ }).first(), 'default', 'pricing link');
  const pricing = page.locator('header a, .nav a').filter({ hasText: /^Pricing$/ }).first();
  if (await pricing.count()) {
    await pricing.hover();
    await page.waitForTimeout(200);
    await record(page, cdp, 'nav-link' + suffix, pricing, 'hover', 'pointer hover');
    await pricing.focus();
    await page.waitForTimeout(200);
    await record(page, cdp, 'nav-link' + suffix, pricing, 'focus-visible', 'focus()');
  }
  const cta = page.locator('a').filter({ hasText: /^Get started$/ }).first();
  if (await cta.count() && await cta.isVisible().catch(() => false)) {
    await record(page, cdp, 'button-primary' + suffix, cta, 'default', 'Get started link, not followed');
    await cta.hover().catch(() => {});
    await page.waitForTimeout(200);
    await record(page, cdp, 'button-primary' + suffix, cta, 'hover', 'pointer hover, not followed');
    await cta.focus().catch(() => {});
    await page.waitForTimeout(150);
    await record(page, cdp, 'button-primary' + suffix, cta, 'focus-visible', 'focus(), not followed');
  } else {
    log('  miss button-primary visible');
  }
  const platform = page.locator('[aria-controls="dropdown_content_0"]').first();
  await record(page, cdp, 'nav-menu-button' + suffix, platform, 'default', 'Platform button');
  if (await platform.count()) {
    await platform.click();
    await page.waitForTimeout(400);
    await record(page, cdp, 'menu' + suffix, page.locator('#dropdown_content_0').first(), 'open', 'Platform expanded');
    await record(page, cdp, 'menu-link' + suffix, page.locator('#dropdown_content_0 a').filter({ hasText: /^Design$/ }).first(), 'default', 'Design link inside menu');
    await page.keyboard.press('Escape');
  }
  const hero = page.locator('h1').first();
  await record(page, cdp, 'hero-title' + suffix, hero, 'default', 'h1');
  const body = page.locator('main p, .hero p, p').filter({ hasText: /website/i }).first();
  await record(page, cdp, 'body-text' + suffix, body, 'default', 'paragraph');
  const card = page.locator('.marquee-card, [class*="card"]').first();
  await record(page, cdp, 'card' + suffix, card, 'default', 'first card');
  const badge = page.locator('a, span').filter({ hasText: /^NEW$/ }).first();
  await record(page, cdp, 'badge' + suffix, badge, 'default', 'NEW label');
  await ctx.close();
}

async function pricingDesktop(theme) {
  const { page, ctx, cdp } = await openPage('/pricing', { theme });
  const suffix = theme === 'dark' ? '-dark' : '';
  const toggle = page.locator('input[name="toggle"]').first();
  await record(page, cdp, 'switch' + suffix, toggle, 'default', 'billing toggle, not submitted');
  const select = page.locator('select').first();
  await record(page, cdp, 'select' + suffix, select, 'default', 'plan select, not submitted');
  const plan = page.locator('a, button').filter({ hasText: /Start for free/i }).first();
  await record(page, cdp, 'plan-cta' + suffix, plan, 'default', 'plan CTA, not followed');
  await ctx.close();
}

async function salesDesktop(theme) {
  const { page, ctx, cdp } = await openPage('/enterprise/contact-sales', { theme });
  const suffix = theme === 'dark' ? '-dark' : '';
  const email = page.locator('input[type="email"], input[name="Email"]').first();
  await record(page, cdp, 'text-field' + suffix, email, 'default', 'email field, not filled, not submitted');
  if (await email.count()) {
    await email.focus();
    await page.waitForTimeout(200);
    await record(page, cdp, 'text-field' + suffix, email, 'focus', 'focused, empty, not submitted');
  }
  const area = page.locator('textarea').first();
  await record(page, cdp, 'text-area' + suffix, area, 'default', 'textarea if present, not filled');
  const submit = page.locator('button[type="submit"], input[type="submit"]').first();
  await record(page, cdp, 'submit-button' + suffix, submit, 'default', 'submit control, not clicked');
  await ctx.close();
}

async function loginWall() {
  const { page, ctx, cdp } = await openPage('/login');
  const email = page.locator('input[name="email"]').first();
  await record(page, cdp, 'login-email', email, 'default', 'login wall, not typed');
  const pass = page.locator('input[name="password"]').first();
  await record(page, cdp, 'login-password', pass, 'default', 'password field, not typed');
  const cont = page.getByRole('button', { name: /^Continue$/ }).first();
  await record(page, cdp, 'login-continue', cont, 'default', 'Continue, not clicked');
  await ctx.close();
}

async function phone() {
  const { page, ctx, cdp } = await openPage('/', { mobile: true });
  const btn = page.locator('.w-nav-button').first();
  await record(page, cdp, 'icon-button', btn, 'default', 'phone menu button');
  if (await btn.count()) {
    await btn.click();
    await page.waitForTimeout(500);
    await record(page, cdp, 'icon-button', btn, 'pressed', 'menu opened');
    const overlay = page.locator('.w-nav-overlay, #w-nav-overlay-0').first();
    await record(page, cdp, 'phone-menu', overlay, 'open', 'phone nav overlay');
  }
  await ctx.close();
}

log('measure home light');
await homeDesktop('light');
log('measure home dark');
await homeDesktop('dark');
log('measure pricing');
await pricingDesktop('light');
await pricingDesktop('dark');
log('measure sales form');
await salesDesktop('light');
log('measure login wall');
await loginWall();
log('measure phone');
await phone();
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, 'components', Object.keys(out.components).length);
await browser.close();
