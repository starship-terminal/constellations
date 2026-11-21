// Measures SavvyCal public components. Nothing is submitted.
// Password fields are not typed. OAuth buttons are not clicked.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, RAW, chromium, UA, UA_MOBILE } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.resolve(RAW, '..', 'components', 'crops'), { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'savvycal', captured: '2026-11-21', source: 'computed style, public pages' }, components: {} };
const log = (...a) => console.log(...a);

async function states(page, cdp, key, loc, list, meta) {
  const c = out.components[key] = { ...meta, page: meta.page, states: {} };
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count().catch(() => 0))) {
    c.missing = true;
    log('  ! missing', key);
    return;
  }
  async function read(state, via) {
    try {
      const s = await styleOf(target);
      let file;
      try { file = await crop(page, target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 120); }
      c.states[state] = { ...s, crop: file, via };
      log('  ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h));
    } catch (e) {
      c.states[state] = { error: String(e.message).slice(0, 180), via };
      log('  !', key, state, String(e.message).slice(0, 100));
    }
  }
  async function force(classes) {
    await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
    await target.evaluate((el) => el.setAttribute('data-m-force', '1'));
    const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
    const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
    if (!nodeId) return async () => {};
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
    await page.waitForTimeout(250);
    return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
  }
  for (const st of list) {
    if (st === 'default') await read('default', 'rest');
    else if (st === 'hover') {
      const box = await target.boundingBox();
      if (box) await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
      await page.waitForTimeout(300);
      await read('hover', 'mouse');
      await page.mouse.move(2, 2);
    } else if (st === 'focus-visible') {
      await target.evaluate((el) => el.focus());
      await page.keyboard.press('Shift+Tab');
      await page.keyboard.press('Tab');
      await page.waitForTimeout(200);
      const ok = await target.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
      await read('focus-visible', ok ? 'keyboard' : 'focus failed');
      await page.evaluate(() => document.activeElement && document.activeElement.blur());
    } else if (st === 'pressed') {
      const undo = await force(['active', 'hover']);
      await read('pressed', 'CDP active+hover');
      await undo();
    } else if (st === 'focused') {
      await target.click({ timeout: 3000 }).catch(() => {});
      await page.waitForTimeout(200);
      await read('focused', 'click, not submitted');
    }
  }
}

async function session(mobile, fn) {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  try { await fn(page, cdp); }
  finally { await ctx.close(); await browser.close(); }
}

const interactive = ['default', 'hover', 'focus-visible', 'pressed'];

await session(false, async (page, cdp) => {
  log('home');
  await open(page, BASE + '/');
  await states(page, cdp, 'nav-link', page.getByRole('link', { name: 'Features', exact: true }).first(), interactive, { title: 'Nav link', group: 'link', page: 'home' });
  await states(page, cdp, 'nav-login', page.getByRole('link', { name: 'Log in', exact: true }).first(), interactive, { title: 'Log in', group: 'link', page: 'home' });
  await states(page, cdp, 'nav-signup', page.getByRole('link', { name: 'Sign up', exact: true }).first(), interactive, { title: 'Sign up', group: 'button', page: 'home' });
  await states(page, cdp, 'hero-cta', page.getByRole('link', { name: 'Try SavvyCal risk-free' }).first(), interactive, { title: 'Hero CTA', group: 'button', page: 'home' });
  await states(page, cdp, 'hero-secondary', page.getByRole('link', { name: 'See plans & pricing' }).first(), interactive, { title: 'Secondary CTA', group: 'link', page: 'home' });
  await states(page, cdp, 'logo', page.getByRole('link', { name: 'SavvyCal home' }).first(), ['default'], { title: 'Logo', group: 'link', page: 'home' });
  await states(page, cdp, 'faq-summary', page.locator('summary').first(), interactive, { title: 'FAQ summary', group: 'accordion', page: 'home' });
  await page.locator('summary').first().click();
  await page.waitForTimeout(300);
  await states(page, cdp, 'faq-open', page.locator('details[open]').first(), ['default'], { title: 'FAQ open', group: 'accordion', page: 'home' });
  await states(page, cdp, 'footer-link', page.locator('footer a').filter({ hasText: 'Privacy' }).first(), interactive, { title: 'Footer link', group: 'link', page: 'home' });
  await states(page, cdp, 'hero-title', page.locator('h1').first(), ['default'], { title: 'Display heading', group: 'type', page: 'home' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

await session(false, async (page, cdp) => {
  log('pricing');
  await open(page, BASE + '/pricing');
  await states(page, cdp, 'billing-annual', page.getByRole('button', { name: /Annual/ }).first(), interactive, { title: 'Annual billing', group: 'tabs', page: 'pricing' });
  await states(page, cdp, 'billing-monthly', page.getByRole('button', { name: 'Monthly', exact: true }).first(), interactive, { title: 'Monthly billing', group: 'tabs', page: 'pricing' });
  await page.getByRole('button', { name: 'Monthly', exact: true }).click();
  await page.waitForTimeout(300);
  await states(page, cdp, 'billing-monthly-selected', page.getByRole('button', { name: 'Monthly', exact: true }).first(), ['default'], { title: 'Monthly selected', group: 'tabs', page: 'pricing' });
  const plan = page.locator('a').filter({ hasText: /Get started|Start/ }).first();
  await states(page, cdp, 'plan-cta', plan, interactive, { title: 'Plan CTA', group: 'button', page: 'pricing' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

await session(false, async (page, cdp) => {
  log('integrations');
  await open(page, BASE + '/integrations-directory');
  await states(page, cdp, 'search', page.getByPlaceholder('Search integrations'), ['default', 'focused'], { title: 'Search field', group: 'text field', page: 'integrations' });
  await states(page, cdp, 'filter-pill', page.getByRole('button', { name: 'Calendar', exact: true }), interactive, { title: 'Filter pill', group: 'tabs', page: 'integrations' });
  await page.getByRole('button', { name: 'Calendar', exact: true }).click();
  await page.waitForTimeout(250);
  await states(page, cdp, 'filter-pill-selected', page.getByRole('button', { name: 'Calendar', exact: true }), ['default'], { title: 'Filter pill selected', group: 'tabs', page: 'integrations' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

await session(false, async (page, cdp) => {
  log('login wall');
  await open(page, BASE + '/login');
  await states(page, cdp, 'login-email', page.locator('input[type="email"]').first(), ['default', 'focused'], { title: 'Email field', group: 'text field', page: 'login' });
  await states(page, cdp, 'login-password', page.locator('input[type="password"]').first(), ['default', 'focused'], { title: 'Password field', group: 'text field', page: 'login' });
  await states(page, cdp, 'login-submit', page.getByRole('button', { name: 'Sign In', exact: true }), interactive, { title: 'Sign in submit', group: 'button', page: 'login' });
  await states(page, cdp, 'oauth-google', page.getByRole('button', { name: 'Sign in with Google' }), ['default', 'hover', 'focus-visible'], { title: 'Google sign-in', group: 'button', page: 'login' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

await session(false, async (page, cdp) => {
  log('demo');
  await open(page, BASE + '/demo', { wait: 2200 });
  await states(page, cdp, 'demo-next', page.getByRole('button', { name: 'Go to the Next Month' }), interactive, { title: 'Next month', group: 'icon button', page: 'demo' });
  await states(page, cdp, 'demo-day', page.locator('button').filter({ hasText: /^1[5-9]$/ }).first(), ['default'], { title: 'Day cell', group: 'button', page: 'demo' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

await session(true, async (page, cdp) => {
  log('mobile menu');
  await open(page, BASE + '/');
  await states(page, cdp, 'menu-button', page.getByRole('button', { name: 'Open main menu' }), interactive, { title: 'Open menu', group: 'icon button', page: 'mobile-home' });
  await page.getByRole('button', { name: 'Open main menu' }).click();
  await page.waitForTimeout(500);
  await states(page, cdp, 'menu-link', page.getByRole('link', { name: 'Pricing', exact: true }).last(), ['default'], { title: 'Menu link', group: 'link', page: 'mobile-home' });
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
});

log('wrote', OUT, Object.keys(out.components).length);
