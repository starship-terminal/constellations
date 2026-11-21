// Measures Sketch's public components in states reachable without signing in
// or submitting a form.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and one crop per state under
// components/crops/. Nothing is typed into an email or password field.
// Sign-in controls are measured, never followed. Apple, Google and SSO
// are not clicked.

import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = { _meta: {}, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current, browser;
const run = new Date().toISOString().slice(0, 10);

async function newPage(key, url, { mobile = false } = {}) {
  current = key;
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? 'mobile' : 'desktop', url);
  await open(page, BASE + url, { wait: 2000 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return ctx;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4);
  await page.waitForTimeout(150);
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
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(200);
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function measure(key, state, loc, via) {
  const c = out.components[key];
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    c.states[state] = { error: 'not visible' };
    log('  !', key, state, 'not visible');
    return;
  }
  try {
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, 8); } catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    c.states[state] = { ...s, crop: file, via };
    log('  ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h), s.style && s.style.backgroundColor, s.style && s.style.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message || e).slice(0, 120));
  }
}

async function S(key, loc, states, meta) {
  out.components[key] = {
    page: current,
    run,
    url: page.url().split('?')[0],
    title: meta.title,
    group: meta.group,
    desc: meta.desc || '',
    selector: meta.sel,
    states: {},
  };
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  for (const st of states) {
    let undo;
    let via = 'at rest';
    try {
      await reset();
      if (!meta.noScroll) await centre(target);
      if (st === 'hover') {
        await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await target.focus();
        await page.waitForTimeout(200);
        via = 'focus(), nothing typed';
      }
      await measure(key, st, loc, via);
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 180) };
      log('  !', key, st, String(e.message || e).slice(0, 100));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function brand() {
  const ctx = await newPage('home', '/');
  await S('page', q('body'), ['default'], { group: 'Foundations', title: 'Page', desc: 'The body surface and type.', sel: 'body' }, );
  await S('header', q('header.main-nav'), ['default'], { group: 'Shell', title: 'Header', desc: 'The marketing header at 1440.', sel: 'header.main-nav', noScroll: true });
  await S('logo', q('a.main-nav__logo__link').first(), ['default'], { group: 'Shell', title: 'Wordmark', sel: 'a.main-nav__logo__link', noScroll: true });
  await S('nav-link', q('header a.main-nav__link').filter({ hasText: 'Pricing' }).first(), B4, { group: 'Shell', title: 'Nav link', desc: 'Pricing, a direct header link.', sel: 'a.main-nav__link', noScroll: true });
  await S('nav-sign-in', q('header a[href*="/signin"]').filter({ hasText: 'Sign In' }).filter({ visible: true }).first(), B4, { group: 'Shell', title: 'Sign in link', desc: 'Measured, never followed.', sel: 'a[href*=signin]', noScroll: true });
  await S('button-primary', q('header a.button-new--primary').first(), B4, { group: 'Controls', title: 'Primary button', desc: 'Get started in the header. Measured, never followed.', sel: 'a.button-new--primary', noScroll: true });
  await S('hero-title', q('h1.hero__title, h1').first(), ['default'], { group: 'Type', title: 'Display title', sel: 'h1.hero__title' });
  await S('hero-cta', q('a.button-new--primary').filter({ hasText: /Get started for free/ }).first(), B4, { group: 'Controls', title: 'Hero primary button', sel: 'a.button-new--primary' });
  const sub = q('header li.main-nav__subnav').filter({ hasText: 'Product' }).first();
  if (await sub.count()) {
    await sub.hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(400);
  }
  await S('nav-menu', q('header .main-nav__subnav__dropdown').filter({ visible: true }).first(), ['default'], { group: 'Shell', title: 'Product menu', desc: 'The Product disclosure after hover.', sel: '.main-nav__subnav__dropdown', noScroll: true });
  await S('nav-menu-link', q('header a.main-nav__subnav__link').filter({ hasText: /^Design/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: 'Shell', title: 'Menu link', sel: 'a.main-nav__subnav__link', noScroll: true });
  await page.mouse.move(8, 800).catch(() => {});
  await S('promo', q('.promo__banner').first(), ['default'], { group: 'Patterns', title: 'Promo banner', sel: '.promo__banner' });
  await S('badge', q('.main-nav__item__badge, .main-nav__subnav__latest-update__badge').filter({ visible: true }).first(), ['default'], { group: 'Controls', title: 'Badge', desc: 'The NEW mark on Changelog, when the menu is open it may be hidden; the homepage promo or menu badge.', sel: '.badge' });
  const foot = q('footer').first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: 'Shell', title: 'Footer', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: 'Pricing' }).first(), B4, { group: 'Shell', title: 'Footer link', sel: 'footer a' });
  await S('newsletter-field', q('footer input[type="email"], form input[type="email"]').first(), ['default', 'focused'], { group: 'Forms', title: 'Newsletter email field', desc: 'Focused only. Nothing typed. Not submitted.', sel: 'input[type=email]' });
  await S('newsletter-submit', q('footer button, form button').filter({ hasText: /Sign up/ }).first(), B4, { group: 'Forms', title: 'Newsletter submit', desc: 'Measured. Not clicked, so the form is not submitted.', sel: 'newsletter submit' });
  save();
  await ctx.close();
}

async function pricing() {
  const ctx = await newPage('pricing', '/pricing/');
  await S('plan-card', q('.subscription-card').first(), ['default'], { group: 'Patterns', title: 'Plan card', sel: '.subscription-card' });
  await S('billing-yearly', q('.billing-toggle__option--yearly').first(), B4, { group: 'Controls', title: 'Billing toggle, yearly', desc: 'The selected yearly option.', sel: '.billing-toggle__option--yearly' });
  await S('billing-monthly', q('.billing-toggle__option--monthly').first(), B4, { group: 'Controls', title: 'Billing toggle, monthly', sel: '.billing-toggle__option--monthly' });
  await S('currency-select', q('select').first(), ['default', 'focus-visible'], { group: 'Forms', title: 'Currency select', sel: 'select' });
  await S('tooltip-trigger', q('.tooltip-trigger').first(), ['default', 'hover', 'focus-visible'], { group: 'Controls', title: 'Tooltip trigger', desc: 'Hover and focus only. The tooltip panel is a separate crop when it paints.', sel: '.tooltip-trigger' });
  const tip = q('.tooltip-trigger').first();
  await tip.hover().catch(() => {});
  await page.waitForTimeout(400);
  const panel = q('[role="tooltip"], .tooltip, .tooltip__content, [class*="tooltip__panel"]').filter({ visible: true }).first();
  if (await panel.count()) {
    await S('tooltip', panel, ['default'], { group: 'Controls', title: 'Tooltip', sel: '[role=tooltip]', noScroll: true });
  } else {
    out.components.tooltip = { page: 'pricing', run, missing: true, title: 'Tooltip', desc: 'Hover did not paint a tooltip panel this run.', states: {} };
    log('  ! missing tooltip panel');
  }
  await S('plan-cta', q('.subscription-card a, .subscription-card button').filter({ hasText: /Get started|Start|Try|Subscribe|Buy/i }).first(), B4, { group: 'Controls', title: 'Plan CTA', desc: 'Measured, never followed.', sel: '.subscription-card a' });
  save();
  await ctx.close();
}

async function signin() {
  const ctx = await newPage('signin', '/signin/');
  await S('signin-title', q('h1').first(), ['default'], { group: 'Auth wall', title: 'Sign-in title', sel: 'h1' });
  await S('sso-google', q('a, button').filter({ hasText: 'Continue with Google' }).first(), ['default', 'hover'], { group: 'Auth wall', title: 'Continue with Google', desc: 'Measured. Not clicked.', sel: 'google' });
  await S('sso-apple', q('a, button').filter({ hasText: 'Continue with Apple' }).first(), ['default'], { group: 'Auth wall', title: 'Continue with Apple', desc: 'Measured. Not clicked.', sel: 'apple' });
  await S('sso-sso', q('a, button').filter({ hasText: 'Continue with SSO' }).first(), ['default'], { group: 'Auth wall', title: 'Continue with SSO', desc: 'Measured. Not clicked.', sel: 'sso' });
  await S('email-field', q('input[type="email"]').first(), ['default', 'focused'], { group: 'Auth wall', title: 'Email field', desc: 'Focused only. Nothing typed.', sel: 'input[type=email]' });
  await S('password-field', q('input[type="password"]').first(), ['default', 'focused'], { group: 'Auth wall', title: 'Password field', desc: 'Focused only. Nothing typed. Not submitted.', sel: 'input[type=password]' });
  await S('signin-submit', q('button').filter({ hasText: /^Sign In$/ }).first(), ['default'], { group: 'Auth wall', title: 'Sign in button', desc: 'Disabled until fields are filled. Not clicked.', sel: 'button Sign In' });
  await S('create-account', q('a').filter({ hasText: 'Create an account' }).first(), ['default', 'hover'], { group: 'Auth wall', title: 'Create account link', desc: 'Measured. Not followed.', sel: 'a create account' });
  save();
  await ctx.close();
}

async function docs() {
  const ctx = await newPage('docs', '/docs/');
  await S('docs-title', q('h1').first(), ['default'], { group: 'Docs', title: 'Docs title', sel: 'h1' });
  const search = q('input[type="search"], input[placeholder*="Search" i]').first();
  if (await search.count()) await S('search-field', search, ['default', 'focused'], { group: 'Docs', title: 'Docs search', desc: 'Focused only. Nothing typed.', sel: 'input search' });
  else {
    out.components['search-field'] = { page: 'docs', run, missing: true, title: 'Docs search', states: {} };
    log('  ! missing search-field');
  }
  await S('docs-link', q('main a, article a').filter({ hasText: /\w{4,}/ }).first(), ['default', 'hover'], { group: 'Docs', title: 'Docs link', sel: 'main a' });
  save();
  await ctx.close();
}

async function mobile() {
  const ctx = await newPage('home', '/', { mobile: true });
  await S('m-header', q('header.main-nav').first(), ['default'], { group: 'Phone', title: 'Phone header', sel: 'header', noScroll: true });
  await S('m-menu-button', q('button.main-nav__toggle').first(), B4, { group: 'Phone', title: 'Menu button', sel: 'button.main-nav__toggle', noScroll: true });
  await q('button.main-nav__toggle').click({ force: true });
  await page.waitForTimeout(500);
  await S('m-menu', q('.mobile-nav').first(), ['default'], { group: 'Phone', title: 'Phone menu', desc: 'The drawer the Menu button opens.', sel: '.mobile-nav', noScroll: true });
  await S('m-nav-link', q('.mobile-nav a').filter({ hasText: 'Design' }).first(), ['default'], { group: 'Phone', title: 'Phone menu link', sel: '.mobile-nav a', noScroll: true });
  save();
  await ctx.close();
}

({ browser } = await launch());
try {
  await brand();
  await pricing();
  await signin();
  await docs();
  await mobile();
} finally {
  save();
  await browser.close().catch(() => {});
}
log('wrote', OUT, Object.keys(out.components).length, 'components');
