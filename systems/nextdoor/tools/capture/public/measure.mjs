// Measures Nextdoor's public components. Never types, never submits, never
// clicks Google, Facebook, Apple, Continue, Log in, or Sign up.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, patch, closePromo, styleOf, crop, centre } from './lib.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const REF = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(REF, 'components', 'crops'), { recursive: true });

const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'nextdoor', readAt: new Date().toISOString().slice(0, 10) }, components: {} };
const log = (...a) => console.log(...a);

const PAGES = {
  home: 'https://nextdoor.com/',
  about: 'https://about.nextdoor.com/',
  smallbiz: 'https://business.nextdoor.com/en-us/small-business',
  directories: 'https://nextdoor.com/directories/',
  help: 'https://help.nextdoor.com/s/topic-page?topicName=Neighbor&language=en_US',
};

let page, cdp, current;

async function openPage(url, { mobile = false } = {}) {
  const browser = page ? page.context().browser() : await chromium.launch({ headless: true });
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2200);
  await closePromo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return browser;
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

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  const ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function measure(key, state, loc, meta) {
  const c = (out.components[key] ??= { states: {}, page: current, ...meta });
  c.page = current;
  Object.assign(c, meta);
  try {
    const target = loc.first();
    if (!(await target.count())) {
      c.states[state] = { error: 'missing' };
      log('  missing', key, state);
      return;
    }
    await centre(target).catch(() => {});
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, 6); } catch (e) { s.cropError = String(e.message).slice(0, 120); }
    c.states[state] = { ...s, crop: file };
    log('  ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h), s.style && s.style.backgroundColor, s.style && s.style.color, s.style && s.style.fontSize);
  } catch (e) {
    c.states[state] = { error: String(e.message).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 100));
  }
}

async function states(key, loc, meta, { press = true, focus = true } = {}) {
  const target = loc.first();
  await measure(key, 'default', target, meta);
  if (!(await target.count())) return;
  try {
    await target.hover({ timeout: 4000 });
    await page.waitForTimeout(300);
    await measure(key, 'hover', target, meta);
  } catch (e) { log('  hover fail', key, String(e.message).slice(0, 80)); }
  if (focus) {
    const via = await kbFocus(target);
    await measure(key, 'focus-visible', target, meta);
    out.components[key].states['focus-visible'].via = via;
  }
  if (press) {
    const undo = await forcePseudo(target, ['active', 'hover']);
    await measure(key, 'pressed', target, meta);
    out.components[key].states.pressed.via = 'CDP forcePseudoState :active:hover';
    await undo();
  }
  await page.mouse.move(2, 2).catch(() => {});
}

const browser = await chromium.launch({ headless: true });
page = { context: () => ({ browser: () => browser }) };

async function go(key, url, mobile = false) {
  current = key + (mobile ? '-mobile' : '');
  if (page && page.close) await page.context().close().catch(() => {});
  await openPage(url, { mobile });
  log('open', current, page.url());
}

// Homepage
await go('home', PAGES.home);
await states('button-signup', page.getByRole('button', { name: 'Sign up', exact: true }), { group: 'button', title: 'Sign up', desc: 'Green pill in the homepage header. Not clicked.' });
await states('button-login', page.getByRole('button', { name: 'Log in', exact: true }), { group: 'button', title: 'Log in', desc: 'Quiet pill in the homepage header. Not clicked. It opens the login wall.' });
await states('button-continue', page.getByRole('button', { name: 'Continue', exact: true }), { group: 'button', title: 'Continue', desc: 'Green pill on the signup card. Not clicked. Submitting would create an account.' });
await states('button-oauth', page.getByRole('button', { name: /Continue with Google/ }), { group: 'button', title: 'Continue with Google', desc: 'OAuth button on the signup card. Not clicked.' });
await states('menu-trigger', page.getByRole('button', { name: 'Partners', exact: true }), { group: 'menu', title: 'Partners', desc: 'Header menu trigger.' }, { press: true });
await states('field-email', page.getByRole('textbox', { name: 'Email address' }), { group: 'text field', title: 'Email address', desc: 'Empty signup field. Not typed into.' }, { press: false, focus: true });
await states('link-invite', page.getByRole('link', { name: 'Have an invite code?' }), { group: 'link', title: 'Invite code', desc: 'Link on the signup card. Not followed. It opens the join wall.' });
await states('link-legal', page.getByRole('link', { name: 'Privacy Policy' }), { group: 'link', title: 'Privacy Policy', desc: 'Inline legal link on the signup card.' });

// Open the Partners menu and measure a menu row, then close it.
await page.getByRole('button', { name: 'Partners', exact: true }).click();
await page.waitForTimeout(500);
await states('menu-item', page.getByRole('link', { name: 'Publishers' }), { group: 'menu', title: 'Publishers', desc: 'Row in the Partners menu. Not followed in this measurement.' });
await page.keyboard.press('Escape');

// About header
await go('about', PAGES.about);
await states('button-login-about', page.getByRole('link', { name: 'Log in' }).or(page.getByRole('button', { name: 'Log in' })), { group: 'button', title: 'About Log in', desc: 'Dark pill on the about header. Not clicked.' });
await states('nav-link', page.getByRole('link', { name: 'Careers', exact: true }), { group: 'link', title: 'Careers', desc: 'About header link.' });
await states('heading-hero', page.getByRole('heading').first(), { group: 'type', title: 'About hero', desc: 'Hero heading on the about page.' }, { press: false, focus: false });

// Small business
await go('smallbiz', PAGES.smallbiz);
await states('button-claim', page.getByRole('link', { name: /Claim your free Business Page/ }).or(page.getByRole('button', { name: /Claim your free Business Page/ })), { group: 'button', title: 'Claim business page', desc: 'Dark pill on the small-business hero. Not clicked. It opens a signup wall.' });
await states('button-create-biz', page.getByRole('link', { name: 'Create Your Business Page' }).or(page.getByRole('button', { name: 'Create Your Business Page' })), { group: 'button', title: 'Create business page', desc: 'Green header pill. Not clicked. Signup wall.' });
await states('button-advertise', page.getByRole('link', { name: 'Advertise Now' }).or(page.getByRole('button', { name: 'Advertise Now' })), { group: 'button', title: 'Advertise now', desc: 'Quiet header pill. Not clicked. Ads signup wall.' });

// Directory
await go('directories', PAGES.directories);
await states('button-signup-dir', page.getByRole('link', { name: 'Sign up' }).or(page.getByRole('button', { name: 'Sign up' })), { group: 'button', title: 'Directory Sign up', desc: 'Dark pill on the directory header. Not clicked.' });
await states('link-category', page.getByRole('link', { name: 'Restaurant', exact: true }), { group: 'link', title: 'Category link', desc: 'Directory category link. Not followed. A category page can ask for a neighborhood.' });

// Help search field, not submitted
await go('help', PAGES.help);
const search = page.getByRole('searchbox').or(page.getByRole('textbox', { name: /search/i })).or(page.locator('input[placeholder="Search"], input[aria-label="Search"]'));
await states('field-search', search, { group: 'text field', title: 'Help search', desc: 'Help-center search. Not submitted.' }, { press: false });

// Phone homepage
await go('home-mobile', PAGES.home, true);
await states('button-signup-mobile', page.getByRole('button', { name: 'Sign up', exact: true }), { group: 'button', title: 'Mobile Sign up', desc: 'Green pill in the phone header. Not clicked.' });
await states('icon-button-menu', page.getByRole('button', { name: /menu/i }).or(page.locator('button').filter({ has: page.locator('svg') }).last()), { group: 'icon button', title: 'Mobile menu', desc: 'Hamburger on the phone header. Not opened, so the signup card stays the subject.' });

await page.context().close();
await browser.close();
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, 'components', Object.keys(out.components).length);
