// Measures jitter.video components on public pages. Nothing is submitted,
// signed into, or purchased. Login/signup buttons are measured at rest only.
//
//   PLAYWRIGHT=... node measure.mjs [page ...]
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= { product: 'jitter', captured: '2026-11-18', route: 'public-web' };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  product: '/product/',
  pricing: '/pricing/',
  templates: '/templates/',
  customers: '/customers/',
  login: '/login/',
  contact: '/contact-sales/',
  changelog: '/changelog/',
  notfound: '/this-page-is-not-real/',
};

const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
let page, cdp, current;

async function newPage(key, { mobile = false, wait = 3500 } = {}) {
  current = key;
  const launched = await launch({ mobile, width: 1440, height: 900 });
  page = await launched.context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await launched.context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page._browser = launched.browser;
  log('open', key, mobile ? 'mobile' : 'desktop');
  if (!(await open(page, BASE + URLS[key], { wait }))) throw new Error(`BLOCKED ${key}: the page never loaded, nothing measured`);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}
async function done() {
  await page._browser.close();
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4);
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(250);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, `${s.rect.w}x${s.rect.h}`, s.face?.backgroundColor || s.style.backgroundColor);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  out.components[key] = {
    page: current, url: new URL(URLS[current], BASE).href,
    title: meta.title, group: meta.group, desc: meta.desc,
    states: { ...(prev && prev.states || {}) },
  };
  const loc = target;
  if (!(await loc.count().catch(() => 0))) {
    out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  const el = loc.first();
  for (const st of list) {
    let undo;
    let via = 'at rest';
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(el);
      if (st === 'hover') {
        await el.hover({ timeout: 4000 }).catch(() => el.hover({ force: true }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(el);
      } else if (st === 'pressed') {
        undo = await forcePseudo(el, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await el.click({ timeout: 3000 }).catch(() => el.evaluate((n) => n.focus()));
        via = 'clicked into the field; nothing submitted';
      } else if (st === 'opened') {
        if (opts.open) await opts.open();
        via = opts.via || 'opened locally';
      }
      await measure(key, st, el, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
  save();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function home() {
  await newPage('home');
  const g = 'Shell';
  await S('header', q('header').first(), ['default'], { group: g, title: 'Site header', desc: 'Fixed marketing header: logo, Product and Customers menus, Templates, Pricing, Log in, Sign up.' }, { noScroll: true });
  await S('nav-signup', q('header a[href="/join/"]').first(), B4, { group: g, title: 'Sign up button', desc: 'Black pill in the header. The fill paints on span.button-inner. The link is not followed.' }, { noScroll: true });
  await S('nav-login', q('header a[href="/login/"]').first(), B4, { group: g, title: 'Log in link', desc: 'Header log-in link. Not followed.' }, { noScroll: true });
  await S('hero-cta', q('a[href="/join/"]').filter({ hasText: 'Try Jitter for free' }).first(), B4, { group: 'Home', title: 'Hero CTA', desc: 'Violet pill "Try Jitter for free". Fill is on button-inner. Link not followed.' });
  await S('stories-link', q('a').filter({ hasText: 'Read customer stories' }).first(), B4, { group: 'Home', title: 'Yellow text button', desc: 'Yellow pill linking to customer stories. Not followed during measurement.' });
  const product = q('header a[href="/product/"]').first();
  await page.evaluate(() => window.scrollTo(0, 0));
  await product.hover({ force: true }).catch(() => {});
  await page.waitForTimeout(700);
  await S('nav-submenu', q('[class*="_submenuOpen_"]').first(), ['opened'], { group: g, title: 'Product submenu', desc: 'Hover-opened product panel. Not navigated.' }, { noScroll: true, noReset: true, open: async () => { await product.hover({ force: true }); await page.waitForTimeout(300); } });
  await S('footer', q('footer').first(), ['default'], { group: g, title: 'Footer', desc: 'Site footer with product, company and legal links, plus the newsletter field.' });
  await S('newsletter', q('footer input[type="email"], input[name="email"]').last(), ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Footer email field. Focused, never filled, never submitted.' });
  await done();
}

async function pricing() {
  await newPage('pricing');
  const g = 'Pricing';
  await S('plan-toggle', q('[class*="_planToggler"], [role="radiogroup"]').first(), ['default'], { group: g, title: 'Billing toggle', desc: 'Pay monthly / Pay annually segmented control. Annual was clicked in the screenshot pass; this reading is the control at rest.' });
  await S('plan-free', q('button').filter({ hasText: 'Get started' }).nth(0), ['default', 'hover'], { group: g, title: 'Free plan CTA', desc: 'First Get started button on the plan grid. Not clicked: it starts signup.' });
  await S('plan-pro', q('[class*="_yellow_"]').filter({ hasText: 'Get started' }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Pro plan CTA', desc: 'Yellow Get started pill. Not followed.' });
  await S('faq', q('[class*="_accordionItem_"]').first(), ['default'], { group: g, title: 'FAQ row', desc: 'First pricing accordion row at rest.' });
  const heading = q('[class*="_accordionItemHeading_"]').first();
  if (await heading.count()) {
    await heading.click({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(400);
    await S('faq-open', q('[class*="_accordionItem_"]').first(), ['opened'], { group: g, title: 'FAQ row open', desc: 'Same row after its heading was clicked. Local toggle, no submission.' }, { noReset: true });
  }
  await done();
}

async function templates() {
  await newPage('templates');
  const g = 'Templates';
  await S('search', q('input[type="search"]').first(), ['default', 'focused'], { group: g, title: 'Template search', desc: 'Search templates field. Focused, not typed, not submitted.' });
  await S('template-card', q('a[href*="/templates/"]').nth(3), ['default', 'hover'], { group: g, title: 'Template category link', desc: 'A public template category link. The editor behind /file/ was not opened.' });
  await done();
}

async function login() {
  await newPage('login', { wait: 4000 });
  const g = 'Sign-in boundary';
  await S('login-card', q('main, [class*="auth"], form, body').first(), ['default'], { group: g, title: 'Login card', desc: 'Public login card at rest. No button is clicked.' }, { noScroll: true, crop: false });
  await S('login-google', q('button').filter({ hasText: 'Continue with Google' }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Continue with Google', desc: 'OAuth button measured at rest and hover. Never clicked.' }, { noScroll: true });
  await S('login-sso', q('button').filter({ hasText: 'Continue with SSO' }).first(), ['default', 'hover'], { group: g, title: 'Continue with SSO', desc: 'SSO button. Never clicked.' }, { noScroll: true });
  await S('login-email', q('button').filter({ hasText: 'Continue with email' }).first(), ['default', 'hover'], { group: g, title: 'Continue with email', desc: 'Email continue button. Never clicked, so the password step was never reached.' }, { noScroll: true });
  await S('login-field', q('input[type="email"]').first(), ['default', 'focused'], { group: g, title: 'Work email field', desc: 'Email field on the login card. Focused empty. Nothing typed, nothing submitted.' }, { noScroll: true });
  await done();
}

async function contact() {
  await newPage('contact');
  const g = 'Contact sales boundary';
  await S('contact-name', q('input[name="name"]').first(), ['default', 'focused'], { group: g, title: 'Name field', desc: 'Contact sales name field. Focused empty. Not filled, not submitted.' });
  await S('contact-email', q('form input[type="email"]').first(), ['default'], { group: g, title: 'Work email field', desc: 'Contact form email. Not filled.' });
  await S('contact-body', q('textarea[name="body"]').first(), ['default', 'focused'], { group: g, title: 'Message field', desc: 'Contact sales textarea. Focused empty. Not submitted.' });
  await S('contact-send', q('button').filter({ hasText: 'Send message' }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Send message', desc: 'Submit button measured, never clicked.' });
  await done();
}

async function product() {
  await newPage('product');
  await S('product-cta', q('a[href="/join/"]').filter({ hasText: /Try it for free|Get started/ }).first(), ['default', 'hover', 'focus-visible'], { group: 'Product', title: 'Product CTA', desc: 'Primary signup link on the product page. Not followed.' });
  await done();
}

async function mobileHome() {
  await newPage('home', { mobile: true });
  await S('m-header', q('header').first(), ['default'], { group: 'Mobile', title: 'Phone header', desc: '390-wide header with the Open menu control.' }, { noScroll: true });
  await S('m-menu-button', q('button[aria-label="Open menu"], button').filter({ hasText: /Open menu|Menu/ }).first(), ['default'], { group: 'Mobile', title: 'Open menu', desc: 'Hamburger. Clicked only to open the local drawer.' }, { noScroll: true });
  const btn = q('button[aria-label="Open menu"]').first();
  if (await btn.count()) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(700);
    await S('m-menu', q('[role="dialog"], nav, [class*="_mobile"]').first(), ['opened'], { group: 'Mobile', title: 'Phone menu', desc: 'Drawer after Open menu. No destination followed.' }, { noScroll: true, noReset: true });
  }
  await done();
}

const jobs = { home, pricing, templates, login, contact, product, 'mobile-home': mobileHome };
const keys = pageArg.length ? pageArg : Object.keys(jobs);
for (const k of keys) {
  if (!jobs[k]) { log('unknown', k); continue; }
  try { await jobs[k](); }
  catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); try { await page?._browser?.close(); } catch { /* closed */ } }
}
save();
log('wrote', OUT);
