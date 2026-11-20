// Measures Zellerfeld components on public pages. No form is submitted.
// Sign-in, Google, newsletter, onboarding and checkout are not entered.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { launchBrowser, UA, UA_MOBILE, BASE, hideCookies, dismissNotice, REF, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'Zellerfeld', captured: new Date().toISOString(), widths: '1440x900 and 390x844', theme: 'light only' }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const browser = await launchBrowser();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const mobileCtx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });

let page;
let cdp;

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, meta);
  return c;
}

async function styleOf(loc) {
  return loc.evaluate((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing,
      color: s.color,
      backgroundColor: s.backgroundColor,
      borderTopColor: s.borderTopColor,
      borderTopWidth: s.borderTopWidth,
      borderRadius: s.borderRadius,
      padding: s.padding,
      height: s.height,
      width: Math.round(r.width) + 'px',
      boxHeight: Math.round(r.height) + 'px',
      boxShadow: s.boxShadow === 'none' ? 'none' : s.boxShadow.slice(0, 180),
      textTransform: s.textTransform,
      outline: s.outline,
    };
  });
}

async function crop(key, state, loc) {
  const file = `${key}-${state}.png`;
  try {
    await loc.scrollIntoViewIfNeeded().catch(() => {});
    await page.waitForTimeout(200);
    await loc.screenshot({ path: path.join(CROPS, file) });
    return file;
  } catch (e) {
    log('  crop miss', key, state, String(e.message).split('\n')[0]);
    return null;
  }
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

async function states(key, loc, { hover = true, focus = true, press = true } = {}) {
  const c = out.components[key];
  const base = loc.first();
  c.states.default = { via: 'resting', style: await styleOf(base), crop: await crop(key, 'default', base) };
  if (hover) {
    const box = await base.boundingBox();
    if (box) {
      await page.mouse.move(box.x + Math.min(8, box.width / 2), box.y + Math.min(8, box.height / 2));
      await page.waitForTimeout(350);
      c.states.hover = { via: 'mouse hover', style: await styleOf(base), crop: await crop(key, 'hover', base) };
      await page.mouse.move(2, 2);
      await page.waitForTimeout(150);
    }
  }
  if (focus) {
    await base.focus().catch(() => {});
    await page.keyboard.press('Shift+Tab').catch(() => {});
    await page.keyboard.press('Tab').catch(() => {});
    await page.waitForTimeout(250);
    const ok = await base.evaluate((el) => document.activeElement === el || el.contains(document.activeElement)).catch(() => false);
    c.states['focus-visible'] = { via: ok ? 'keyboard Tab' : 'focus failed', style: ok ? await styleOf(base) : null, crop: ok ? await crop(key, 'focus-visible', base) : null };
    await page.evaluate(() => document.activeElement && document.activeElement.blur()).catch(() => {});
  }
  if (press) {
    const release = await forcePseudo(base, ['hover', 'active']);
    c.states.pressed = { via: 'CDP forcePseudoState hover+active (no click)', style: await styleOf(base), crop: await crop(key, 'pressed', base) };
    await release();
    await base.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  }
}

async function openPage(url, { mobile = false } = {}) {
  page = await (mobile ? mobileCtx : context).newPage();
  cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2800);
  await hideCookies(page);
  await dismissNotice(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return page;
}

async function run() {
  log('home');
  await openPage(BASE + '/');
  comp('nav-button', { page: 'home', role: 'icon button', note: 'Opens the navigation drawer' });
  await states('nav-button', page.locator('button[aria-label="Open navigation"]'));
  comp('wordmark', { page: 'home', role: 'link' });
  await states('wordmark', page.locator('header a[href="https://www.zellerfeld.com/"], a[aria-label="Zellerfeld"]').first(), { press: false });
  comp('create-link', { page: 'home', role: 'link', note: 'Leaves for studio.zellerfeld.com' });
  await states('create-link', page.getByRole('link', { name: /CREATE/i }).first());
  comp('sign-in-button', { page: 'home', role: 'button', note: 'Opens Clerk sign-in. Not clicked.' });
  await states('sign-in-button', page.getByRole('button', { name: /SIGN IN/i }).first());
  comp('search-field', { page: 'home', role: 'text field' });
  const search = page.locator('input[placeholder="What are you looking for?"]').first();
  await states('search-field', search, { press: false });
  await search.click();
  await page.waitForTimeout(300);
  out.components['search-field'].states.focused = { via: 'click, not submitted', style: await styleOf(search), crop: await crop('search-field', 'focused', search) };
  await search.fill('nike');
  await page.waitForTimeout(400);
  out.components['search-field'].states.filled = { via: 'typed nike, not submitted, then cleared', style: await styleOf(search), crop: await crop('search-field', 'filled', search) };
  await search.fill('');
  await page.keyboard.press('Escape');

  comp('cookie-accept', { page: 'home', role: 'button', note: 'Consent. Not clicked. Banner may already be hidden.' });
  const accept = page.locator('[data-cookie-banner] button').filter({ hasText: /ACCEPT/i }).first();
  if (await accept.count()) await states('cookie-accept', accept, { press: false });
  else out.components['cookie-accept'].states.default = { via: 'not captured: banner hidden before this measure so consent is never clicked', style: null, crop: null };

  await page.locator('button[aria-label="Open navigation"]').click();
  await page.waitForTimeout(700);
  comp('nav-drawer', { page: 'home', role: 'menu' });
  const drawer = page.locator('[role="dialog"][data-state="open"]').first();
  out.components['nav-drawer'].states.open = { via: 'Open navigation click', style: await styleOf(drawer), crop: await crop('nav-drawer', 'open', drawer) };
  comp('nav-link', { page: 'home', role: 'link' });
  await states('nav-link', drawer.getByRole('link', { name: 'Sneakers' }).first());
  await page.keyboard.press('Escape');
  await page.close();

  log('collection');
  await openPage(BASE + '/collections/sneakers');
  comp('sort-chip', { page: 'sneakers', role: 'button' });
  await states('sort-chip', page.getByRole('button', { name: /TRENDING/i }).first());
  comp('product-card', { page: 'sneakers', role: 'card' });
  const card = page.locator('main a[href*="/products/"]').filter({ visible: true }).first();
  await states('product-card', card, { press: false });
  await page.close();

  log('product');
  await openPage(BASE + '/products/pdf-bol-sneaker');
  comp('buy-button', { page: 'product', role: 'button', note: 'Opens Fit Profile. Measured at rest. Not used to proceed.' });
  await states('buy-button', page.getByRole('button', { name: /BUY NOW/i }).first());
  comp('wishlist-button', { page: 'product', role: 'icon button', note: 'Opens sign-in. Not clicked here.' });
  await states('wishlist-button', page.getByRole('button', { name: /wishlist/i }).first());
  comp('color-swatch', { page: 'product', role: 'link' });
  const swatch = page.locator('a').filter({ hasText: /^Black$/ }).first();
  if (await swatch.count()) await states('color-swatch', swatch);
  else out.components['color-swatch'].states.default = { via: 'not captured: colour link not found', style: null };
  comp('gallery-thumb', { page: 'product', role: 'button' });
  await states('gallery-thumb', page.getByRole('button', { name: 'Show image 2' }).first(), { press: false });
  await page.close();

  log('faq');
  await openPage(BASE + '/pages/faq');
  comp('accordion', { page: 'faq', role: 'disclosure' });
  const summary = page.locator('summary').first();
  out.components.accordion.states.default = { via: 'closed summary', style: await styleOf(summary), crop: await crop('accordion', 'default', summary) };
  await summary.click();
  await page.waitForTimeout(400);
  out.components.accordion.states.open = { via: 'summary click', style: await styleOf(summary), crop: await crop('accordion', 'open', summary) };
  await page.close();

  log('newsletter field, not submitted');
  await openPage(BASE + '/pages/newsletter');
  comp('newsletter-field', { page: 'newsletter', role: 'text field', note: 'Not filled. Not submitted.' });
  const email = page.locator('input[type="email"], input[placeholder*="email" i]').first();
  if (await email.count()) await states('newsletter-field', email, { press: false });
  else out.components['newsletter-field'].states.default = { via: 'not captured: field not found', style: null };
  comp('newsletter-submit', { page: 'newsletter', role: 'button', note: 'Not clicked.' });
  const submit = page.locator('button[type="submit"]').first();
  if (await submit.count()) await states('newsletter-submit', submit, { press: true });
  await page.close();

  log('footer');
  await openPage(BASE + '/pages/faq');
  comp('footer-link', { page: 'faq', role: 'link' });
  await states('footer-link', page.locator('footer a').filter({ hasText: 'FAQ' }).first());
  await page.close();

  log('mobile nav');
  await openPage(BASE + '/', { mobile: true });
  comp('mobile-nav-button', { page: 'home', role: 'icon button', width: 390, note: 'Bottom bar Menu. The desktop Open navigation button is hidden at 390.' });
  const menuBtn = page.getByRole('button', { name: 'Menu', exact: true }).filter({ visible: true }).first();
  await states('mobile-nav-button', menuBtn, { hover: false });
  await menuBtn.click();
  await page.waitForTimeout(700);
  comp('mobile-nav-drawer', { page: 'home', role: 'menu', width: 390 });
  const md = page.locator('[role="dialog"][data-state="open"]').first();
  out.components['mobile-nav-drawer'].states.open = { via: 'Open navigation', style: await styleOf(md), crop: await crop('mobile-nav-drawer', 'open', md) };
  await page.close();

  fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
  log('wrote', OUT, 'components', Object.keys(out.components).length);
  await browser.close();
}

run().catch(async (e) => {
  console.error(e);
  fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
  await browser.close();
  process.exit(1);
});
