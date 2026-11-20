// Measures Krisp's public marketing components, in every state that can be
// reached without signing in, submitting a form, or answering a consent banner.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing assistant noise customers about security blog careers mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/.
//
// States:
//   hover          real mouse hover
//   focus-visible  keyboard focus (Shift+Tab, Tab)
//   pressed        CDP CSS.forcePseudoState [active, hover]; no click fires
//   opened         a resting state reached by the component's own toggle
// Sign in, Get Krisp, Book a demo, Try it Free, Start with Core and the
// contact-sales form are measured or link-observed, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  pricing: '/pricing/',
  assistant: '/ai-meeting-assistant/',
  noise: '/noise-cancellation/',
  customers: '/customers/',
  about: '/about-us/',
  security: '/security/',
  blog: '/blog/',
  careers: '/careers/',
  'not-found': '/download/',
};

let page, cdp, current, context, run;
const touched = new Set();

async function newPage(key, { mobile = false, wait = 3500 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait, promo: 'close' });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await loc.evaluate((el) => {
      const a = el.matches('a,button,input,select,textarea,[tabindex]') ? el : el.querySelector('a,button,[tabindex]');
      (a || el).focus();
    });
    ok = await loc.evaluate((el) => {
      const a = document.activeElement;
      return a === el || el.contains(a);
    });
    how = 'focus() on inner control';
  }
  await page.waitForTimeout(300);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) throw new Error('forcePseudo: node not found');
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(350);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  // The page the reading was taken on, as the browser reports it (the not-found key is a
  // route that 404s), not the URL the spec asked for.
  Object.assign(c, { page: current, run, url: safeUrl(page && !page.isClosed() ? page.url() : BASE + (URLS[current] || '')), ...meta });
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 160); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h));
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

const NEVER = /sign in|log in|get krisp|book a demo|try it free|start with|contact sales|submit|buy|checkout|subscribe/i;

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count().catch(() => 0))) { log('  ! missing', key); out.components[key].missing = true; return; }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ timeout: 4000, force: true }));
        await page.waitForTimeout(400);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'opened') {
        const text = await loc.evaluate((el) => (el.innerText || '').slice(0, 40));
        if (NEVER.test(text) && !opts.allowOpen) throw new Error('open refused: ' + text);
        await loc.click({ timeout: 4000 });
        await page.waitForTimeout(500);
        via = 'own toggle, no navigation';
      } else via = 'at rest';
      await measure(key, st, opts.measureLoc || loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 140));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const G = {
  shell: 'Shell and navigation',
  home: 'Home',
  pricing: 'Pricing',
  product: 'Product pages',
  content: 'Customers, about, security, blog, careers',
  mobile: 'Mobile (390 wide)',
};

async function shell() {
  await newPage('home');
  const g = G.shell;
  await S('header', q('header.new'), ['default'], { group: g, title: 'Header', desc: 'The 73px white bar: wordmark, product menus, Sign in, Book a demo, Get Krisp.', sel: 'header.new' }, { noScroll: true });
  await S('wordmark', q('header.new a[href="https://krisp.ai/"], header.new a[href="/"]').first(), ['default'], { group: g, title: 'Wordmark', desc: 'The krisp wordmark in the header.', sel: 'header a' }, { noScroll: true });
  await S('nav-link', q('header.new a').filter({ hasText: 'Pricing' }), B4, { group: g, title: 'Nav link', desc: 'A top-level destination. Hover and pressed measured; the link was not followed.', sel: 'header a' }, { noScroll: true });
  await S('nav-menu-trigger', q('header.new a, header.new button, header.new div').filter({ hasText: /^AI Meeting Assistant$/ }).first(), ['default', 'hover'], { group: g, title: 'Nav menu trigger', desc: 'Opens the product menu. The opened menu is captured separately.', sel: 'header' }, { noScroll: true });
  await S('sign-in', q('header .nav_action_link, header a[href*="login"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sign in link', desc: 'Text link to app.krisp.ai/login. Measured, never followed.', sel: '.nav_action_link' }, { noScroll: true });
  await S('book-demo', q('header .btn--dark').first(), B4, { group: g, title: 'Book a demo button', desc: 'Near-black pill in the header. The control is a div.button wrapping a link to /contact-sales/. Measured, never followed.', sel: '.btn--dark' }, { noScroll: true });
  await S('get-krisp', q('header .btn--primary').first(), B4, { group: g, title: 'Get Krisp button', desc: 'Indigo primary pill. Opens a download menu on the marketing site; the menu was opened for the opened state and the sign-up link was not followed.', sel: '.btn--primary' }, { noScroll: true });
  // Get Krisp is on the NEVER list: hovering opens its download menu without pressing the link.
  await page.locator('header .btn--primary').first().hover().catch(() => {});
  await page.waitForTimeout(500);
  await S('get-krisp-menu', q('header .btn--primary').first().locator('xpath=ancestor::*[contains(@class,"dropdown") or contains(@class,"menu")][1]').first(), ['opened'], { group: g, title: 'Get Krisp menu', desc: 'The download menu under Get Krisp, if the click revealed one.', sel: '.btn--dropdown' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('hero-title', q('h1').first(), ['default'], { group: G.home, title: 'Hero title', desc: 'Plus Jakarta Sans display heading.', sel: 'h1' });
  await S('hero-pill', q('.hero_pill, .pill_new').first(), ['default', 'hover'], { group: G.home, title: 'Hero announcement pill', desc: 'The "New" chip linking to a product page.', sel: '.hero_pill' });
  await S('hero-cta', q('#hero .btn--primary, .hero_container .btn--primary, main .btn--primary').first(), B4, { group: G.home, title: 'Hero Get Krisp button', desc: 'The primary CTA under the headline. Measured, never followed.', sel: '.btn--primary' });
  await S('footer', q('footer').first(), ['default'], { group: G.home, title: 'Footer', desc: 'Link columns, social marks, legal links including Cookie settings (not clicked).', sel: 'footer' });
  const faq = q('.faq_item, .faq-item, details, [class*="faq_"]').filter({ hasText: /./ }).first();
  await S('faq-item', faq, ['default', 'opened'], { group: G.home, title: 'FAQ row', desc: 'An accordion row on the home page, if one is present.', sel: '.faq' });
  await page.close();
}

async function pricing() {
  await newPage('pricing');
  const g = G.pricing;
  await S('billing-toggle', q('.switch_inner, .billing_toggle, .switcher_wrapper').first(), ['default'], { group: g, title: 'Billing toggle', desc: 'Monthly / Annually pill. Annually is the resting state and shows Save 50%.', sel: '.billing_toggle' });
  await S('plan-card', q('.plan_holder').first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing column: title, description, price, CTA.', sel: '.plan_holder' });
  await S('plan-card-highlight', q('.plan_holder.highlighted').first(), ['default', 'hover'], { group: g, title: 'Highlighted plan card', desc: 'The Most popular column.', sel: '.plan_holder.highlighted' });
  await S('plan-price', q('.price_wrapper .price.yearly, .price.yearly').first(), ['default'], { group: g, title: 'Plan price', desc: 'The yearly price shown at rest.', sel: '.price.yearly' });
  await S('plan-cta', q('.plan_holder .btn_wrapper, .pricing_app_btn').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Plan CTA', desc: 'Try it Free / Start with Core. Measured, never followed (it links to app.krisp.ai sign-up).', sel: '.pricing_app_btn' });
  await S('plan-badge', q('.plan_holder .badge, .most_popular, [class*="popular"]').first(), ['default'], { group: g, title: 'Most popular badge', desc: 'The badge on the highlighted plan, if it is its own element.', sel: '.popular' });
  await page.close();
}

async function product() {
  await newPage('assistant');
  await S('product-title', q('h1').first(), ['default'], { group: G.product, title: 'Product page title', sel: 'h1' });
  await S('product-cta', q('.btn--primary').first(), ['default', 'hover'], { group: G.product, title: 'Product page primary button', sel: '.btn--primary' }, { noScroll: true });
  await page.close();
  await newPage('noise');
  await S('feature-switch', q('.noise_cancellation_switch, .switch').first(), ['default'], { group: G.product, title: 'Demo switch', desc: 'The "With Krisp" demo switch on the noise-cancellation page. Not toggled if doing so starts audio.', sel: '.noise_cancellation_switch' });
  await page.close();
}

async function content() {
  for (const key of ['customers', 'about', 'security', 'blog', 'careers', 'not-found']) {
    await newPage(key);
    await S(key + '-title', q('h1').first(), ['default'], { group: G.content, title: key + ' title', sel: 'h1' });
    await page.close();
  }
}

let mobileBrowser;
async function mobile() {
  await context.close();
  ({ context, browser: mobileBrowser } = await launch({ mobile: true }));
  await newPage('home', { mobile: true });
  await S('mobile-header', q('header.new'), ['default'], { group: G.mobile, title: 'Mobile header', sel: 'header.new' }, { noScroll: true });
  const burger = q('header .burger, .burger').first();
  await S('mobile-menu-button', burger, ['default'], { group: G.mobile, title: 'Mobile menu button', sel: 'header button' }, { noScroll: true });
  await page.close();
}

const want = new Set((process.argv[2] || '').split(',').filter(Boolean));
const jobs = { shell, pricing, product, content, mobile };
run = new Date().toLocaleDateString('en-CA');   // the local run date
const launched = await launch({ width: 1440, height: 900 });
context = launched.context;
try {
  for (const [name, fn] of Object.entries(jobs)) {
    if (want.size && !want.has(name)) continue;
    await fn();
    save();
  }
  out._meta.capturedAt = new Date().toISOString();
  out._meta.viewport = { desktop: '1440x900', mobile: '390x844' };
  save();
  log('wrote', OUT, 'components', Object.keys(out.components).length);
} finally {
  await context.close().catch(() => {});
  await launched.browser.close().catch(() => {});
  if (mobileBrowser) await mobileBrowser.close().catch(() => {});
}
