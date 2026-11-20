// Measures masterclass.com components on public signed-out pages.
// Nothing is typed, submitted, purchased or signed into. Consent is hidden.
//
//   PLAYWRIGHT=... node measure.mjs [group ...]
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, UA, UA_MOBILE, open, blockedByChallenge, hideConsent, styleOf, crop, quantize, CROPS, RAW } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= { product: 'MasterClass', route: 'public-web', signedOut: true };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  class: BASE + '/classes/revolutionize-your-workflows-with-ai',
  checkout: BASE + '/checkout',
  login: BASE + '/auth/login',
  categories: BASE + '/categories',
  gift: BASE + '/gift',
  business: BASE + '/for-business',
  quiz: BASE + '/find-my-classes',
};

let page, cdp;

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4);
  await page.waitForTimeout(200);
}

async function hover(loc) {
  const b = await loc.boundingBox();
  if (!b) return;
  await page.mouse.move(b.x + Math.min(b.width / 2, 80), b.y + Math.min(b.height / 2, 20));
  await page.waitForTimeout(500);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  await page.waitForTimeout(300);
}

// Forces :active:hover on the component node itself, found by a marker attribute, as the
// kit's forcePseudo does. The topmost node at the centre (a label span or an svg) would not
// carry the component's own :active rule.
async function pressOn(loc) {
  const marked = await loc.evaluate((el) => {
    document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force'));
    el.setAttribute('data-m-force', '1');
    return true;
  }).catch(() => false);
  if (!marked) return null;
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return null;
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
  await page.waitForTimeout(250);
  return nodeId;
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

const visible = (loc) => loc.filter({ visible: true });

const SPECS = {
  home: [
    { key: 'nav-header', title: 'Header bar', find: (p) => p.locator('header').first() },
    { key: 'nav-logo', title: 'Logo', find: (p) => p.locator('header a[aria-label*="logo" i], header a[href="/"]').first(), states: ['default', 'hover', 'focus-visible'] },
    { key: 'nav-browse', title: 'Browse button', find: (p) => p.locator('header button').filter({ hasText: /^Browse$/ }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'nav-cta', title: 'Get MasterClass', find: (p) => p.locator('header a.c-button--primary').filter({ hasText: /Get MasterClass/ }).locator('visible=true').first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'nav-login', title: 'Log In link', find: (p) => p.locator('header a[href="/auth/login"]').first(), states: ['default', 'hover', 'focus-visible'] },
    { key: 'nav-plans', title: 'View Plans link', find: (p) => p.locator('header a[href="/checkout"]').first(), states: ['default', 'hover'] },
    { key: 'hero-h1', title: 'Hero headline', find: (p) => p.locator('h1').filter({ visible: true }).first() },
    { key: 'hero-cta', title: 'Continue CTA', find: (p) => p.locator('a, button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'quiz-option', title: 'Quiz option', find: (p) => p.locator('button').filter({ hasText: /Learn about AI/ }).first(), states: ['default', 'hover', 'focus-visible'] },
    { key: 'class-card', title: 'Class card', find: (p) => p.locator('a[href^="/classes/"]').filter({ visible: true }).nth(2) },
    { key: 'category-chip', title: 'Category chip', find: (p) => p.locator('button').filter({ hasText: /^Trending$/ }).first(), states: ['default', 'hover'] },
    { key: 'footer', title: 'Footer', find: (p) => p.locator('footer').first() },
    { key: 'footer-link', title: 'Footer link', find: (p) => p.locator('footer a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  ],
  class: [
    { key: 'class-title', title: 'Class title', find: (p) => p.locator('h1').filter({ visible: true }).first() },
    { key: 'class-cta', title: 'Class primary CTA', find: (p) => p.locator('main a.c-button--primary, main a.c-button, a.c-button--primary').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'trailer-button', title: 'Watch Trailer', find: (p) => p.locator('button').filter({ hasText: /Watch Trailer|Trailer/i }).filter({ visible: true }).first(), states: ['default', 'hover'] },
    { key: 'lesson-row', title: 'Lesson row', find: (p) => p.locator('main li, [class*="lesson" i], [class*="chapter" i]').filter({ visible: true }).first() },
    { key: 'instructor', title: 'Instructor block', find: (p) => p.locator('main h2, main [class*="instructor" i]').filter({ visible: true }).first() },
  ],
  checkout: [
    { key: 'plan-card', title: 'Plan card', find: (p) => p.locator('button, [role="radio"], label, article, li').filter({ hasText: /Best Value|Premium|Standard/ }).filter({ visible: true }).first() },
    { key: 'plan-select', title: 'Select plan control', find: (p) => p.locator('button, [role="radio"], [role="button"]').filter({ hasText: /^Select$|^Selected$/ }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'checkout-continue', title: 'Checkout Continue', find: (p) => p.locator('button, a').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'faq-button', title: 'FAQ accordion', find: (p) => p.locator('button').filter({ hasText: /What is MasterClass|included in a MasterClass/i }).filter({ visible: true }).first(), states: ['default', 'hover'] },
    { key: 'price', title: 'Plan price', find: (p) => p.locator('text=/\\$\\d/').filter({ visible: true }).first() },
  ],
  login: [
    { key: 'login-google', title: 'Log In With Google', find: (p) => p.locator('button').filter({ hasText: /Google/ }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
    { key: 'login-email', title: 'Email field', find: (p) => p.locator('input').filter({ visible: true }).first(), states: ['default', 'focused'] },
    { key: 'login-password', title: 'Password field', find: (p) => p.locator('input').filter({ visible: true }).nth(1), states: ['default'] },
    { key: 'login-submit', title: 'Log In submit', find: (p) => p.locator('button').filter({ hasText: /^Log In$/ }).filter({ visible: true }).last(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
    { key: 'login-signup', title: 'Sign up link', find: (p) => p.locator('a, button').filter({ hasText: /Sign up/ }).filter({ visible: true }).first(), states: ['default', 'hover'] },
  ],
  categories: [
    { key: 'cat-h1', title: 'Categories headline', find: (p) => p.locator('h1').filter({ visible: true }).first() },
    { key: 'cat-card', title: 'Category card', find: (p) => p.locator('main a').filter({ visible: true }).nth(2), states: ['default', 'hover'] },
  ],
  gift: [
    { key: 'gift-h1', title: 'Gift headline', find: (p) => p.locator('h1').filter({ visible: true }).first() },
    { key: 'gift-cta', title: 'Gift CTA', find: (p) => p.locator('a.c-button--primary, button.c-button--primary, a.c-button').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  ],
  business: [
    { key: 'biz-h1', title: 'Business headline', find: (p) => p.locator('h1').filter({ visible: true }).first() },
    { key: 'biz-cta', title: 'Business CTA', find: (p) => p.locator('a, button').filter({ hasText: /demo|get started|contact|learn more/i }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  ],
  mobile: [
    { key: 'm-header', title: 'Mobile header', find: (p) => p.locator('header').first() },
    { key: 'm-menu', title: 'Menu button', find: (p) => p.locator('header button').filter({ hasText: /^Menu$/ }).first(), states: ['default'] },
    { key: 'm-cta', title: 'Mobile Get MasterClass', find: (p) => p.locator('header a.c-button--primary, a.c-button--primary').filter({ visible: true }).first(), states: ['default', 'hover'] },
    { key: 'm-h1', title: 'Mobile hero', find: (p) => p.locator('h1').filter({ visible: true }).first() },
  ],
};

const DRIVERS = {
  hover: { via: 'mouse hover', fn: hover },
  'focus-visible': { via: 'keyboard Tab after programmatic focus', fn: kbFocus },
  pressed: { via: 'CDP CSS.forcePseudoState active+hover, no real press', fn: async () => {} },
  focused: { via: 'element.focus(), nothing typed', fn: async (loc) => { await loc.evaluate((el) => el.focus()); await page.waitForTimeout(200); } },
  default: { via: 'resting', fn: async () => {} },
};

async function measureOne(spec) {
  const states = spec.states || ['default'];
  const rec = { title: spec.title, page: spec.page, states: {} };
  let loc;
  try { loc = spec.find(page); } catch (e) { rec.miss = String(e.message).slice(0, 160); out.components[spec.key] = rec; return; }
  const count = await loc.count().catch(() => 0);
  if (!count) { rec.miss = 'selector matched nothing'; out.components[spec.key] = rec; log('  miss', spec.key); return; }
  const el = loc.first();
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  for (const state of states) {
    await reset();
    await el.scrollIntoViewIfNeeded().catch(() => {});
    let nodeId = null;
    try {
      if (state === 'pressed') {
        nodeId = await pressOn(el);
        // No forced :active means no pressed reading: the catch records a failed state and no crop.
        if (nodeId == null) throw new Error('pressed could not be forced on the component');
      } else await DRIVERS[state].fn(el);
      const reading = await styleOf(el);
      reading.via = state === 'pressed' ? DRIVERS.pressed.via : DRIVERS[state].via;
      rec.states[state] = reading;
      const file = path.join(CROPS, `${spec.key}-${state}.png`);
      if (await crop(el, file)) quantize(file);
      log('  ', spec.key, state, reading.rect && reading.rect.w);
    } catch (e) {
      rec.states[state] = { miss: String(e.message).split('\n')[0].slice(0, 180), via: 'failed' };
      log('  fail', spec.key, state, e.message.split('\n')[0]);
    } finally {
      if (nodeId != null) await pressOff(nodeId);
    }
  }
  out.components[spec.key] = rec;
  save();
}

const want = new Set((process.argv[2] || '').split(',').filter(Boolean));
const browser = await chromium.launch({ headless: true });

async function runPage(pageKey, specs, mobile) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  // Automation is not hidden (no webdriver mask): a bot check is recorded as a boundary, not bypassed.
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  // DOM first: Chromium refuses CSS.enable until the DOM agent is on.
  await cdp.send('DOM.enable').catch(() => {});
  await cdp.send('CSS.enable').catch(() => {});
  const url = URLS[pageKey] || URLS.home;
  log('page', pageKey, url);
  await open(page, url, { wait: 3500 });
  if (await blockedByChallenge(page)) {
    // Keep every earlier reading for this page: nothing measured on a challenge is saved.
    log('  BLOCKED by a bot check; earlier readings kept', pageKey);
    (out._meta.blocked ??= {})[pageKey] = new Date().toISOString();
    await ctx.close();
    return;
  }
  for (const spec of specs) {
    spec.page = pageKey;
    await measureOne(spec);
  }
  await ctx.close();
}

for (const [group, specs] of Object.entries(SPECS)) {
  if (want.size && !want.has(group)) continue;
  await runPage(group === 'mobile' ? 'home' : group, specs, group === 'mobile');
}
out._meta.measuredAt = new Date().toISOString();
save();
log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
