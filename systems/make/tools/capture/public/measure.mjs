// Measures Make public components. Nothing is submitted or signed into.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, centre, RAW, hideConsent } from './lib.mjs';
import { startRun, touch, readOk, readFailed } from './dates.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings and replace only what this run reads, so a page that fails
// part way keeps the earlier readings of every later component instead of dropping them.
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
// Dates follow dates.mjs: _meta.read and each component's `read` move only when a state is
// actually read, kept readings take the earlier date, and _meta.lastAttempt records this run.
const today = new Date().toLocaleDateString('en-CA');
const out = startRun(prev, today);
Object.assign(out._meta, { product: 'Make', route: 'public-web', theme: 'light' });
const done = new Set();
const earlier = new Map();   // key -> the states the committed file held, for a failed reread
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

let page, context, browser, cdp, current;

async function newPage(url) {
  if (page) await page.close().catch(() => {});
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
  await page.waitForTimeout(120);
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
  // Clear markers an earlier call left, or DOM.querySelector finds that element first and forces it.
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(220);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force'))).catch(() => {});
  };
}

async function record(key, state, loc, meta, via) {
  // A component this run reaches is rewritten from its new readings; one it never reaches keeps its
  // reading and date. Dates move only on a successful read (dates.mjs).
  if (!done.has(key)) { touch(out, earlier, key, { ...meta, url: current }); done.add(key); }
  const c = out.components[key];
  try {
    await centre(loc);
    const s = await styleOf(loc);
    let file;
    try { file = await crop(page, loc, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
    readOk(out, c, state, { ...s, crop: file, via }, today);
    log(' ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style && s.style.backgroundColor, s.style && s.style.color, s.style && s.style.fontSize);
  } catch (e) {
    readFailed(c, earlier.get(key), state, { error: String(e.message).slice(0, 180), via }, today);
    log(' !', key, state, String(e.message).slice(0, 120));
  }
}

async function states(key, loc, list, meta) {
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) { log(' ! missing', key); out.components[key] = { missing: true, ...meta, url: current, read: today, states: {} }; done.add(key); return; }  // absence seen today; no state read, so _meta.read stays
  for (const st of list) {
    await reset();
    let undo, via = 'at rest';
    if (st === 'hover') { await target.hover({ timeout: 4000 }).catch(() => {}); via = 'mouse hover'; await page.waitForTimeout(280); }
    else if (st === 'focus-visible') {
      via = await kbFocus(target);
      if (via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead, as the kit does.
        if (!done.has(key)) { touch(out, earlier, key, { ...meta, url: current }); done.add(key); }
        readFailed(out.components[key], earlier.get(key), st, { skipped: 'focus failed: keyboard focus did not reach the element', via }, today);
        log('  -', key, st, 'skipped: focus failed');
        continue;
      }
    }
    else if (st === 'pressed') { undo = await forcePseudo(target, ['active', 'hover']); via = 'CDP forcePseudoState :active:hover'; }
    else if (st === 'focused') { await target.click({ timeout: 4000 }); via = 'clicked into the field; nothing submitted'; await page.waitForTimeout(200); }
    await record(key, st, target, meta, via);
    if (undo) await undo();
  }
  await reset();
}

const B = ['default', 'hover', 'focus-visible', 'pressed'];

({ browser, context } = await launch({ width: 1440, height: 900 }));
try {
  await newPage(BASE + '/');
  await states('cta-primary', page.getByRole('link', { name: 'Try it free' }).first(), B, { title: 'Primary action', group: 'Button' });
  await states('cta-secondary', page.getByRole('link', { name: 'Talk to sales' }).first(), B, { title: 'Secondary action', group: 'Button' });
  await states('text-link', page.getByRole('link', { name: /Explore everything Make can do/ }).first(), ['default', 'hover', 'focus-visible'], { title: 'Text link', group: 'Link' });
  await states('display', page.locator('h1').first(), ['default'], { title: 'Display heading', group: 'Type' });

  await newPage(BASE + '/templates');
  await states('search-field', page.locator('input[placeholder*="Search templates"]').first(), ['default', 'hover', 'focus-visible', 'focused'], { title: 'Template search', group: 'Text field' });
  await states('template-card', page.locator('a[href*="/templates/"]').filter({ hasText: /./ }).first(), ['default', 'hover'], { title: 'Template card', group: 'Card' });
  await states('nav-get-started', page.getByRole('link', { name: 'Get started free' }).first(), B, { title: 'Nav primary action', group: 'Button' });
  await states('checkbox', page.locator('input[name="category"]').first(), ['default'], { title: 'Category checkbox', group: 'Checkbox' });

  await newPage(BASE + '/pricing');
  await states('faq-summary', page.locator('h3').filter({ hasText: 'What are credits?' }).first(), ['default', 'hover'], { title: 'FAQ summary', group: 'Disclosure' });
  await states('pricing-heading', page.locator('h1').first(), ['default'], { title: 'Pricing heading', group: 'Type' });

  await newPage(BASE + '/login');
  await states('email-field', page.locator('input[name="email"]').first(), ['default', 'focus-visible', 'focused'], { title: 'Sign-in email field', group: 'Text field' });
  await states('password-field', page.locator('input[name="password"]').first(), ['default'], { title: 'Sign-in password field', group: 'Text field' });
  await states('signin-submit', page.getByRole('button', { name: /^Sign in$/ }).first(), ['default'], { title: 'Sign-in button (not pressed)', group: 'Button' });
  await states('google-continue', page.getByRole('button', { name: /Continue with Google/ }).first(), ['default'], { title: 'Google continue (not pressed)', group: 'Button' });
} finally {
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
  await browser.close();
}
log('wrote', OUT, Object.keys(out.components).length, 'components');
