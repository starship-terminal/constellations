// Measures Limitless public components. Nothing is submitted or signed into.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, HELP, launch, open, styleOf, crop, centre, RAW, hideConsent } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Merge into the committed file: a run that stops early keeps the readings it
// did not reach. Each page block saves when it closes.
// _meta.captured keeps the earlier date until this run reads a state, so a rerun
// that fails throughout never redates old readings; _meta.lastAttempt is this
// run's date. Each component and state carries its own `read` date, so a reading
// kept from an earlier run keeps the date it was taken.
const TODAY = new Date().toLocaleDateString('en-CA');
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
const prevDate = prev._meta && prev._meta.captured;
// Backfill the earlier date onto every saved component and state that predates
// per-reading dates, before this run updates any of them.
for (const c of Object.values(prev.components || {})) {
  if (!c || !prevDate) continue;
  if (!c.read) c.read = prevDate;
  for (const st of Object.values(c.states || {})) if (st && typeof st === 'object' && !st.read) st.read = prevDate;
}
const out = { _meta: { product: 'Limitless', captured: prevDate || TODAY, lastAttempt: TODAY, route: 'public-web', theme: 'light' }, components: prev.components || {} };
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

let page, context, browser, cdp, current;

async function newPage(url) {
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = url;
  log('open', url);
  await open(page, url, { wait: 2200 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await hideConsent(page);
}

async function reset() {
  await page.mouse.move(8, 8).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(150);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  const ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  await page.waitForTimeout(200);
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  // Clear markers left by earlier calls: DOM.querySelector returns the first in document order.
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, loc, meta, via) {
  const c = (out.components[key] ??= { states: {}, ...meta, url: current });
  c.states ??= {};
  try {
    await centre(loc);
    const s = await styleOf(loc);
    let file;
    try { file = await crop(page, loc, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
    c.states[state] = { ...s, crop: file, via, read: TODAY };
    // Found and measured now: no longer missing (nor missed on a rerun), and dated today.
    delete c.missing;
    delete c.recaptureMissed;
    c.read = TODAY;
    out._meta.captured = TODAY;
    log(' ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h));
  } catch (e) {
    // A failed re-read keeps an earlier good reading (and its date) and notes the failure.
    const msg = String(e.message).slice(0, 180);
    const old = c.states[state];
    c.states[state] = old && !old.error ? { ...old, recaptureError: msg, recaptureRun: TODAY } : { error: msg, via, read: TODAY };
    log(' !', key, state, String(e.message).slice(0, 100));
  }
}

async function states(key, loc, list, meta) {
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    log(' ! missing', key);
    // An earlier reading is kept and flagged; only a component never read is marked missing.
    const old = out.components[key];
    if (old && old.states && Object.keys(old.states).length && !old.missing) old.recaptureMissed = TODAY;
    else out.components[key] = { missing: true, read: TODAY, ...meta, url: current, states: {} };
    return;
  }
  for (const st of list) {
    await reset();
    let undo, via = 'at rest';
    try {
    if (st === 'hover') { await target.hover({ timeout: 4000 }).catch(() => {}); via = 'mouse hover'; await page.waitForTimeout(280); }
    else if (st === 'focus-visible') via = await kbFocus(target);
    else if (st === 'pressed') { undo = await forcePseudo(target, ['active', 'hover']); via = 'CDP forcePseudoState :active:hover'; }
    else if (st === 'focused') { await target.click({ timeout: 4000 }); via = 'clicked into the field; nothing submitted'; await page.waitForTimeout(200); }
    await record(key, st, target, meta, via);
    } catch (e) {
      // One state that throws (a click that times out) is recorded and the rest still run.
      const c = (out.components[key] ??= { states: {}, ...meta, url: current });
      const msg = String(e.message).slice(0, 180);
      const old = c.states[st];
      c.states[st] = old && !old.error ? { ...old, recaptureError: msg, recaptureRun: TODAY } : { error: msg, via, read: TODAY };
      log(' !', key, st, String(e.message).slice(0, 100));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const B = ['default', 'hover', 'focus-visible', 'pressed'];

({ browser, context } = await launch({ width: 1440, height: 900 }));

await newPage(BASE + '/');
await states('nav-link', page.getByRole('link', { name: 'Privacy', exact: true }).first(), B, { title: 'Nav link', group: 'Navigation' });
await states('nav-solutions', page.getByRole('button', { name: 'Solutions' }), B, { title: 'Solutions menu button', group: 'Navigation' });
await states('wordmark', page.getByRole('link', { name: 'Limitless', exact: true }).first(), ['default', 'hover'], { title: 'Wordmark', group: 'Navigation' });
// open solutions, measure a menu item, close without navigating
await page.getByRole('button', { name: 'Solutions' }).click().catch((e) => log(' ! solutions menu did not open', String(e.message).slice(0, 80)));
await page.waitForTimeout(400);
await states('menu-item', page.getByRole('link', { name: 'Voice Recorder' }), ['default', 'hover'], { title: 'Solutions menu item', group: 'Menu' });
await page.keyboard.press('Escape');
await page.waitForTimeout(200);
const signIn = page.locator('a[href="https://app.limitless.ai"]').filter({ hasText: 'Sign In' }).first();
await states('signin-link', signIn, B, { title: 'Sign in link', group: 'Navigation' });
await states('hero-title', page.locator('h1').first(), ['default'], { title: 'Hero title', group: 'Type' });
const prose = page.locator('main p, article p, h1 + p, .prose p').first();
await states('body-copy', prose, ['default'], { title: 'Body copy', group: 'Type' });
await page.close();
save();

await newPage(BASE + '/for/voice-recorder');
const cta = page.locator('a, button').filter({ hasText: /Get the app|Download|Buy|Shop|Order|App Store|Get started/i }).first();
await states('cta', cta, B, { title: 'Primary call to action', group: 'Button' });
await states('feature-card', page.locator('main h2').first(), ['default'], { title: 'Section heading', group: 'Type' });
await page.close();
save();

await newPage(BASE + '/developers');
await states('code-block', page.locator('pre, code').first(), ['default'], { title: 'Code block', group: 'Docs' });
await states('copy-button', page.getByRole('button', { name: 'Copy' }).first(), B, { title: 'Copy button', group: 'Button' });
await states('anchor-link', page.getByRole('link', { name: 'Endpoints' }).first(), ['default', 'hover'], { title: 'In-page anchor', group: 'Link' });
await page.close();
save();

await newPage(BASE + '/privacy');
const faq = page.locator('main button, main summary').first();
await states('faq', faq, ['default', 'hover'], { title: 'FAQ disclosure', group: 'Disclosure' });
if (await faq.count()) {
  await faq.click().catch(() => {});
  await page.waitForTimeout(300);
  await states('faq-open', faq, ['default'], { title: 'FAQ disclosure opened', group: 'Disclosure' });
}
await page.close();
save();

await newPage(BASE + '/support');
await states('support-textarea', page.locator('textarea').first(), ['default', 'focused'], { title: 'Support message field', group: 'Field' });
await states('help-link', page.getByRole('link', { name: /Help Center/ }).first(), ['default', 'hover'], { title: 'Help Center link', group: 'Link' });
await page.close();
save();

await newPage(BASE + '/careers');
await states('roles-link', page.getByRole('link', { name: /View open roles/ }).first(), B, { title: 'Open roles link', group: 'Link' });
await page.close();
save();

await newPage(APP + '/');
await states('google-button', page.getByRole('button', { name: /Continue with Google/ }), B, { title: 'Continue with Google', group: 'Auth boundary' });
await states('email-field', page.locator('#email'), ['default', 'focused'], { title: 'Email field', group: 'Auth boundary' });
await page.close();
save();

await newPage(HELP + '/en/');
await states('search-field', page.locator('#search-input'), ['default', 'focused'], { title: 'Help search field', group: 'Search' });
await states('collection-card', page.locator('a[href*="/collections/"]').first(), ['default', 'hover'], { title: 'Help collection card', group: 'Card' });
await page.close();
save();

await newPage(BASE + '/');
// footer link
await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(400);
await hideConsent(page);
await states('footer-link', page.getByRole('link', { name: 'Terms', exact: true }).last(), ['default', 'hover'], { title: 'Footer link', group: 'Navigation' });
await page.close();
save();

await context.close();
await browser.close();
save();
const n = Object.keys(out.components).length;
const statesN = Object.values(out.components).reduce((a, c) => a + Object.keys(c.states || {}).length, 0);
console.log('wrote', n, 'components', statesN, 'states');
