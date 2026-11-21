// Measures Super.so's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home templates pricing usecase blog feature mobile login.
// Writes raw/components-computed.json and one crop per component and state.
//
// States: hover (real pointer), focus-visible (keyboard), pressed (CDP
// forcePseudoState, so no link or submit fires), focused and filled on the
// template search field. The fill word is "portfolio" and is deleted.
// Sign in, Get started, Google, Apple and passkey are measured, never clicked.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, centre, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(RAW, '..', 'components', 'crops'), { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  templates: '/templates',
  pricing: '/pricing-annual',
  usecase: '/use-cases/website',
  blog: '/blog',
  feature: '/features/ai-chat',
  login: 'https://app.super.so/login',
};

let page, cdp, current, context, run;
const touched = new Set();

async function newPage(key, { mobile = false, wait = 1600 } = {}) {
  current = key;
  if (page) await page.close().catch(() => {});
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  const url = URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key];
  await open(page, url, { wait });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2).catch(() => {});
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
    how = 'focus()';
  }
  await page.waitForTimeout(250);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(300);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  const url = URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current];
  Object.assign(c, { page: current, run, url }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      const cropFile = path.join(RAW, '..', 'components', 'crops', `${key}-${state}.png`);
      const ok = await crop(opts.cropLoc || loc, cropFile);
      if (ok) file = `components/crops/${key}-${state}.png`;
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.style.color, s.style.backgroundColor, s.style.fontSize);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (opts.open) { await reset(); await opts.open().catch((e) => log('  open failed', key, e.message.split('\n')[0])); }
  const loc = target.first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) {
        await loc.scrollIntoViewIfNeeded().catch(() => {});
        await page.waitForTimeout(150);
      }
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(opts.focusLoc || loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(opts.pressLoc || loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).click({ timeout: 4000 });
        await page.waitForTimeout(250);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).first();
        await f.click({ timeout: 4000 });
        await f.fill('portfolio');
        await page.waitForTimeout(300);
        undo = async () => { await f.fill(''); };
        via = 'typed "portfolio", then cleared; nothing submitted';
      } else if (st === 'opened') {
        via = 'opened in place';
      } else via = 'at rest';
      await measure(key, st, loc, { ...opts, via });
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
  templates: 'Templates',
  pricing: 'Pricing',
  usecase: 'Use case',
  blog: 'Blog',
  feature: 'Feature page',
  auth: 'Login wall (not submitted)',
  mobile: 'Phone (390)',
};

async function home() {
  await newPage('home');
  const g = G.shell;
  await S('navbar', q('.super-navbar').first(), ['default'], { group: g, title: 'Navbar', desc: 'The sticky bar: logo, destination links, Sign in, and the yellow Get started free button.', sel: '.super-navbar' }, { noScroll: true });
  await S('nav-link', q('a.super-navbar__item').first(), B4, { group: g, title: 'Nav link', desc: 'A destination in the bar. Measured, never followed.', sel: 'a.super-navbar__item' }, { noScroll: true });
  await S('nav-menu', q('.super-navbar__list').filter({ hasText: 'Use cases' }).first(), ['default', 'opened'], { group: g, title: 'Nav menu trigger', desc: 'Use cases. Opening sets aria-expanded and shows the dropdown. No item was followed.', sel: '.super-navbar__list' }, {
    noScroll: true,
    open: async () => {},
    before: undefined,
  });
  // reopen for the opened state only
  await page.locator('[aria-expanded]').filter({ hasText: 'Use cases' }).first().click();
  await page.waitForTimeout(400);
  await S('nav-dropdown', q('.super-navbar__item-list .notion-dropdown__menu, .super-navbar .notion-dropdown__menu').first(), ['opened'], { group: g, title: 'Use cases dropdown', desc: 'The panel the Use cases control opens. Items are links to /use-cases/*. None were followed.', sel: '.super-navbar .notion-dropdown__menu' }, { noScroll: true, noReset: true });
  await S('nav-dropdown-item', q('a[href="/use-cases/website"]').first(), ['default', 'hover'], { group: g, title: 'Dropdown item', desc: 'One row in the Use cases panel. Hovered, never followed.', sel: 'a[href="/use-cases/website"]' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape');
  await S('nav-signin', q('a').filter({ hasText: /^Sign in$/ }).first(), B4, { group: g, title: 'Sign in link', desc: 'Opens the login wall. Measured, never followed.', sel: 'a Sign in' }, { noScroll: true });
  await S('nav-cta', q('.super-navbar__cta').first(), B4, { group: g, title: 'Get started free', desc: 'The yellow navbar button. Opens the signup wall. Measured, never followed.', sel: '.super-navbar__cta' }, { noScroll: true });
  await S('logo', q('.super-navbar__logo').first(), ['default'], { group: g, title: 'Logo', sel: '.super-navbar__logo' }, { noScroll: true });
  await S('hero-title', q('h1.notion-heading').first(), ['default'], { group: G.home, title: 'Hero title', desc: 'The painted page title. The document h1.notion-header__title is 0x0 and is not the visible heading.', sel: 'h1.notion-heading' }, { noScroll: true });
  await S('hero-cta', q('a').filter({ hasText: 'Get started for free' }).first(), B4, { group: G.home, title: 'Hero CTA', desc: 'The yellow page button. Opens the signup wall. Measured, never followed.', sel: 'a Get started for free' });
  await S('announcement', page.locator('a').filter({ hasText: 'Now with MCP' }).first(), ['default'], { group: G.home, title: 'Announcement link', desc: 'The yellow announcement under the navbar. Its links go to feature pages. Measured, never followed.', sel: 'a Now with MCP' }, { noScroll: true });
  await S('load-more', q('.notion-collection-load-more').first(), B4, { group: G.home, title: 'Load more', desc: 'Reveals more cards on the same page. Measured in resting and forced states. The screenshot runner clicks it once.', sel: '.notion-collection-load-more' });
  await S('footer', q('footer, .super-footer').first(), ['default'], { group: g, title: 'Footer', sel: 'footer' });
  await S('footer-link', q('.super-footer__link, footer a').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Footer link', sel: 'footer a' });
  await page.close();
  page = null;
}

async function templates() {
  await newPage('templates');
  const g = G.templates;
  await S('page-title', q('h1').first(), ['default'], { group: g, title: 'Page title', sel: 'h1' });
  await S('filter-button', q('button').filter({ hasText: 'any site' }).first(), B4, { group: g, title: 'Filter button', desc: 'The "any site" control in the templates sentence. Opens an in-page menu. Stays on /templates.', sel: 'button any site' });
  await page.getByRole('button', { name: 'any site' }).first().click().catch(() => {});
  await page.waitForTimeout(400);
  await S('filter-menu', q('button').filter({ hasText: 'any site' }).locator('xpath=following::*').locator('a').first(), ['default'], { group: g, title: 'Filter menu item', desc: 'A category in the any-site menu. href is #. Not a navigation.', sel: 'templates filter menu' }, { noReset: true });
  await page.keyboard.press('Escape');
  const input = q('input').first();
  await S('search-field', input, ['default', 'hover', 'focused', 'filled', 'focus-visible'], { group: g, title: 'Template search', desc: 'The search field on /templates. Filled with "portfolio" and cleared. Not submitted.', sel: 'input' }, { fieldLoc: input });
  await S('template-card', q('a').filter({ hasText: 'Free' }).first(), ['default', 'hover'], { group: g, title: 'Template card', desc: 'A template tile. Hovered, never followed (cards open customer sites).', sel: 'template card' });
  await S('category-row', q('[data-tab="Website"]').first(), ['default', 'hover'], { group: g, title: 'Category row', desc: 'A sidebar filter. href is #. Selecting it filters the grid on the same page.', sel: '[data-tab=Website]' });
  await page.close();
  page = null;
}

async function pricing() {
  await newPage('pricing');
  await S('pricing-title', q('h1.notion-heading').first(), ['default'], { group: G.pricing, title: 'Pricing title', sel: 'h1.notion-heading' });
  await S('pricing-cta', q('a').filter({ hasText: /Get started|Start|free/i }).first(), ['default', 'hover', 'focus-visible'], { group: G.pricing, title: 'Pricing CTA', desc: 'A plan button. Measured, never followed into signup.', sel: 'pricing CTA' });
  await page.close();
  page = null;
}

async function usecase() {
  await newPage('usecase');
  await S('usecase-title', q('h1.notion-heading').first(), ['default'], { group: G.usecase, title: 'Use-case title', sel: 'h1.notion-heading' });
  await S('usecase-cta', q('a').filter({ hasText: 'Start with this website' }).first(), B4, { group: G.usecase, title: 'Start with this website', desc: 'Opens the signup wall. Measured, never followed.', sel: 'Start with this website' });
  await S('demo-chip', page.getByText('Mono', { exact: true }).first(), ['default', 'hover'], { group: G.usecase, title: 'Demo colour chip', desc: 'Recolours the embedded demo on the same URL.', sel: 'Mono' });
  await page.close();
  page = null;
}

async function blog() {
  await newPage('blog');
  await S('blog-title', q('h1').first(), ['default'], { group: G.blog, title: 'Blog title', sel: 'h1' });
  await S('blog-card', q('a').filter({ hasText: /./ }).nth(8), ['default', 'hover'], { group: G.blog, title: 'Blog card', desc: 'A post card. Hovered, never followed.', sel: 'blog card' });
  await page.close();
  page = null;
}

async function feature() {
  await newPage('feature');
  await S('feature-title', q('h1.notion-heading').first(), ['default'], { group: G.feature, title: 'Feature title', sel: 'h1.notion-heading' });
  await S('body-text', q('p').first(), ['default'], { group: G.feature, title: 'Body text', sel: 'p' });
  await page.close();
  page = null;
}

async function login() {
  await newPage('login', { wait: 2000 });
  const g = G.auth;
  await S('login-email', q('input[type="email"]').first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'On the login wall. Focused only. No address was typed.', sel: 'input[type=email]' }, { fieldLoc: q('input[type="email"]') });
  await S('login-password', q('input[type="password"]').first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'On the login wall. Focused only. No password was typed.', sel: 'input[type=password]' }, { fieldLoc: q('input[type="password"]') });
  await S('login-submit', q('button').filter({ hasText: /^Log in$/ }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Log in button', desc: 'Measured. Never clicked.', sel: 'button Log in' });
  await S('login-google', q('button').filter({ hasText: 'Google' }).first(), ['default'], { group: g, title: 'Sign in with Google', desc: 'Visible. Not clicked.', sel: 'button Google' });
  await S('login-apple', q('button').filter({ hasText: 'Apple' }).first(), ['default'], { group: g, title: 'Sign in with Apple', desc: 'Visible. Not clicked.', sel: 'button Apple' });
  await S('login-passkey', q('button').filter({ hasText: 'passkey' }).first(), ['default'], { group: g, title: 'Sign in with a passkey', desc: 'Visible. Not clicked.', sel: 'button passkey' });
  await page.close();
  page = null;
}

async function mobile() {
  const b = context.browser();
  const mctx = await b.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
    locale: 'en-US',
  });
  await mctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const prev = context;
  context = mctx;
  await newPage('home', { mobile: true });
  await S('m-menu-button', q('.super-navbar__menu-open').first(), ['default'], { group: G.mobile, title: 'Menu button', desc: 'The hamburger. Opens the drawer. Not a link.', sel: '.super-navbar__menu-open' }, { noScroll: true });
  await page.locator('.super-navbar__menu-open').click({ force: true });
  await page.waitForTimeout(500);
  await S('m-drawer', q('.super-navbar__menu').first(), ['opened'], { group: G.mobile, title: 'Phone drawer', desc: 'The full-screen menu. Use cases and Features expand in place. Sign in is the login wall and was not followed.', sel: '.super-navbar__menu' }, { noScroll: true, noReset: true });
  await S('m-drawer-item', q('.super-navbar__menu a').filter({ hasText: 'Showcase' }).first(), ['default'], { group: G.mobile, title: 'Drawer item', sel: '.super-navbar__menu a' }, { noScroll: true, noReset: true });
  await page.close();
  page = null;
  await mctx.close();
  context = prev;
}

const want = new Set((process.argv[2] || 'home,templates,pricing,usecase,blog,feature,login,mobile').split(',').filter(Boolean));
const launched = await launch();
context = launched.context;
run = new Date().toISOString().slice(0, 10);
out._meta.run = run;
out._meta.source = 'https://super.so public pages, signed out, headless Chromium';
try {
  if (want.has('home')) await home();
  if (want.has('templates')) await templates();
  if (want.has('pricing')) await pricing();
  if (want.has('usecase')) await usecase();
  if (want.has('blog')) await blog();
  if (want.has('feature')) await feature();
  if (want.has('login')) await login();
  if (want.has('mobile')) await mobile();
} finally {
  save();
  await launched.browser.close();
}
log('measured', touched.size, 'components');
