// Measures reclaim.ai public components. Never submits a form, never clicks
// Google, Microsoft, Dropbox, SSO, Log In, or Get Started.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, RAW, chromium, UA, patch } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = { _meta: { product: 'reclaim.ai', readAt: new Date().toISOString().slice(0, 10) }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current;

async function newPage(url) {
  current = url;
  const browser = page ? page.context().browser() : null;
  if (page) await page.context().close().catch(() => {});
  const b = browser || await chromium.launch({ headless: true });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await open(page, url.startsWith('http') ? url : BASE + url, { wait: 2000 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important} .osano-cm-window{display:none!important}' });
  await closePromo(page);
  return b;
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

async function record(key, state, loc, meta, via) {
  const c = (out.components[key] ??= { states: {}, ...meta, page: current });
  Object.assign(c, meta);
  try {
    const target = loc.filter({ visible: true }).first();
    if (!(await target.count())) {
      c.states[state] = { error: 'not found' };
      log('  !', key, state, 'not found');
      return;
    }
    await centre(target);
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    c.states[state] = { ...s, crop: file, via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.style?.backgroundColor, s.style?.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 100));
  }
}

async function states(key, loc, meta) {
  await record(key, 'default', loc, meta, 'at rest');
  const t = loc.filter({ visible: true }).first();
  if (!(await t.count())) return;
  await t.hover({ timeout: 3000, force: true }).catch(() => {});
  await page.waitForTimeout(300);
  await record(key, 'hover', loc, meta, 'mouse hover');
  const undo = await forcePseudo(t, ['active', 'hover']);
  await record(key, 'pressed', loc, meta, 'CDP forcePseudoState :active:hover');
  await undo();
  await t.evaluate((el) => el.focus()).catch(() => {});
  await page.waitForTimeout(200);
  await record(key, 'focus-visible', loc, meta, 'element.focus()');
}

const browser = await chromium.launch({ headless: true });
page = await browser.newPage();
await page.close();

await newPage('/');
await states('nav-product', page.locator('.header-link.w-dropdown-toggle').filter({ hasText: /^Product$/ }), { group: 'Shell', title: 'Product menu trigger' });
await states('nav-link', page.locator('a.header-link, a').filter({ hasText: /^Pricing$/ }).first(), { group: 'Shell', title: 'Pricing nav link' });
await states('nav-login', page.locator('a').filter({ hasText: /^Log In$/ }).first(), { group: 'Shell', title: 'Log In link, not followed' });
await states('nav-cta', page.locator('a.w-button, a').filter({ hasText: /^Get Started$/ }).first(), { group: 'Shell', title: 'Get Started, not followed' });
await states('hero-cta', page.locator('a').filter({ hasText: /Get started free/i }).first(), { group: 'Home', title: 'Hero primary CTA' });
await states('hero-secondary', page.locator('a').filter({ hasText: /Book a demo/i }).first(), { group: 'Home', title: 'Hero secondary CTA' });
await states('faq', page.locator('.faq-q, button').filter({ hasText: /What is Reclaim/i }).first(), { group: 'Home', title: 'FAQ question' });
const faq = page.locator('.faq-q, button').filter({ hasText: /What is Reclaim/i }).first();
if (await faq.count()) {
  await faq.click({ force: true }).catch(() => {});
  await page.waitForTimeout(300);
  await record('faq-open', 'opened', faq, { group: 'Home', title: 'FAQ open' }, 'own toggle');
}
save();

await newPage('/pricing');
await states('billing-yearly', page.getByText('Yearly - SAVE 20%', { exact: false }).first(), { group: 'Pricing', title: 'Yearly billing control' });
await states('billing-monthly', page.getByText('Monthly', { exact: true }).first(), { group: 'Pricing', title: 'Monthly billing control' });
await page.getByText('Monthly', { exact: true }).first().click({ force: true }).catch(() => {});
await page.waitForTimeout(400);
await record('billing-monthly', 'selected', page.getByText('Monthly', { exact: true }).first(), { group: 'Pricing', title: 'Monthly selected' }, 'clicked Monthly');
await states('plan-cta', page.locator('a').filter({ hasText: /^Get Started$/ }).nth(1), { group: 'Pricing', title: 'Plan CTA, not followed' });
await states('see-features', page.getByText('See all features').first(), { group: 'Pricing', title: 'See all features' });
save();

await newPage('/blog');
await states('search-field', page.locator('input[name="query"], input[type="search"]').first(), { group: 'Blog', title: 'Blog search, empty' });
await states('blog-card', page.locator('a').filter({ hasText: /Read More/i }).first(), { group: 'Blog', title: 'Blog card link' });
save();

await newPage('/pomodoro-timer');
await states('timer-start', page.getByText('Start', { exact: true }).first(), { group: 'Timer', title: 'Pomodoro start' });
await states('timer-tab', page.getByText('Short Break', { exact: true }).first(), { group: 'Timer', title: 'Short break tab' });
save();

await newPage('https://app.reclaim.ai/login');
await record('login-wall', 'default', page.locator('body'), { group: 'Auth', title: 'Login wall, providers not clicked' }, 'at rest, no provider clicked');
save();

await page.context().browser().close();
log('done', Object.keys(out.components).length, 'components');
