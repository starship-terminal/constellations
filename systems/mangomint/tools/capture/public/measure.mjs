// Measures Mangomint public components. Nothing is submitted, signed into, or booked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, BOOK, launch, open, styleOf, crop, centre, RAW, hidePromo } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings and replace only what this run reads, so a page that fails
// keeps the earlier readings of its components instead of dropping them.
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
// _meta.captured keeps the earlier date until a component is read again, and each component
// carries its own read date, so a partial run never makes retained readings look fresh.
const today = new Date().toLocaleDateString('en-CA');
const out = {
  _meta: { ...(prev._meta || {}), product: 'Mangomint', route: 'public-web', theme: 'light' },
  components: prev.components || {},
};
if (!out._meta.captured) out._meta.captured = today;
const done = new Set();
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

let page, context, browser, cdp, current;

async function newPage(url, wait = 2200) {
  if (page) await page.close().catch(() => {});
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = url;
  log('open', url);
  await open(page, url, { wait });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await hidePromo(page);
}

async function reset() {
  await page.mouse.move(8, 8).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(120);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  const ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  await page.waitForTimeout(180);
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
  await page.waitForTimeout(200);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force'))).catch(() => {});
  };
}

async function record(key, state, loc, meta, via) {
  // A component this run reaches is rewritten from scratch; one it never reaches keeps its reading.
  if (!done.has(key)) { out.components[key] = { states: {}, ...meta, url: current, read: today }; done.add(key); out._meta.captured = today; }
  const c = out.components[key];
  try {
    await centre(loc);
    const s = await styleOf(loc);
    let file;
    try { file = await crop(page, loc, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
    c.states[state] = { ...s, crop: file, via };
    log(' ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h));
  } catch (e) {
    c.states[state] = { error: String(e.message).slice(0, 180), via };
    log(' !', key, state, String(e.message).slice(0, 120));
  }
}

async function states(key, loc, list, meta) {
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    log(' ! missing', key);
    out.components[key] = { missing: true, ...meta, url: current, read: today, states: {} };
    done.add(key);
    out._meta.captured = today;
    return;
  }
  for (const st of list) {
    try {
      await reset();
      let undo, via = 'at rest';
      if (st === 'hover') { await target.hover({ timeout: 4000 }).catch(() => {}); via = 'mouse hover'; await page.waitForTimeout(240); }
      else if (st === 'focus-visible') {
        via = await kbFocus(target);
        if (via === 'focus failed') {
          // Keyboard focus never reached the element, so a reading now would be the element at rest
          // saved as its focus. Record the miss instead, as the kit does.
          if (!done.has(key)) { out.components[key] = { states: {}, ...meta, url: current, read: today }; done.add(key); out._meta.captured = today; }
          out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via };
          log('  -', key, st, 'skipped: focus failed');
          continue;
        }
      }
      else if (st === 'pressed') { undo = await forcePseudo(target, ['active', 'hover']); via = 'CDP forcePseudoState :active:hover'; }
      else if (st === 'focused') { await target.focus().catch(() => target.click({ timeout: 4000 })); via = 'focused the field; nothing typed, nothing submitted'; await page.waitForTimeout(180); }
      else if (st === 'filled') {
        await target.click({ timeout: 4000 });
        await target.fill('capture@example.com');
        via = 'typed a throwaway address; not submitted';
        await page.waitForTimeout(150);
      }
      await record(key, st, target, meta, via);
      if (undo) await undo();
      if (st === 'filled') await target.fill('').catch(() => {});
    } catch (e) {
      // One state that throws (a hover or click timing out) is recorded and the rest still run.
      if (!done.has(key)) { out.components[key] = { states: {}, ...meta, url: current, read: today }; done.add(key); out._meta.captured = today; }
      out.components[key].states[st] = { error: String(e.message).slice(0, 180) };
      log(' !', key, st, String(e.message).slice(0, 120));
    }
  }
  await reset();
}

const B = ['default', 'hover', 'focus-visible', 'pressed'];

// Each page runs on its own: a page that throws is logged, and the readings so far are saved after
// every page, so one missing selector no longer loses the whole run.
const failed = [];
async function step(url, fn) {
  try { await fn(); } catch (e) { failed.push(url); log(' ! page failed', url, String(e.message).slice(0, 120)); }
  save();
}

({ browser, context } = await launch({ width: 1440, height: 900 }));

await step(BASE + '/', async () => {
  await newPage(BASE + '/');
  await states('nav-login', page.getByRole('link', { name: 'Log in', exact: true }).first(), B, { title: 'Log in link', group: 'Navigation' });
  await states('nav-demo', page.getByRole('link', { name: 'Book a demo', exact: true }).first(), B, { title: 'Book a demo outline button', group: 'Button' });
  await states('nav-trial', page.locator('header a, [class*="navbar"] a').filter({ hasText: /^Try it now$/ }).first(), B, { title: 'Try it now filled button', group: 'Button' });
  const businesses = page.locator('button[class*="desktopNavbarDropdown"]').filter({ hasText: 'Businesses' }).first();
  await states('nav-businesses', businesses, B, { title: 'Businesses menu button', group: 'Navigation' });
  await businesses.click();
  await page.waitForTimeout(400);
  await states('menu-item', page.getByRole('link', { name: 'Hair Salons' }).first(), ['default', 'hover'], { title: 'Businesses menu item', group: 'Menu' });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(200);
  await states('video-tour', page.getByRole('button', { name: /WATCH A VIDEO TOUR/i }).first(), ['default', 'hover'], { title: 'Watch a video tour', group: 'Button' });
});

await step(BASE + '/pricing/', async () => {
  await newPage(BASE + '/pricing/');
  await states('price-digit', page.locator('[class*="pricing"]').filter({ hasText: '/mo' }).first(), ['default'], { title: 'Price calculator', group: 'Pricing' });
  const faq = page.locator('[class*="faqs-module--questionButton"]').filter({ hasText: 'Who counts as a user' }).first();
  await states('faq', faq, ['default', 'hover'], { title: 'Pricing FAQ question', group: 'Disclosure' });
  await faq.click().catch(() => {});
  await page.waitForTimeout(300);
  await record('faq', 'open', faq, { title: 'Pricing FAQ question', group: 'Disclosure' }, 'clicked locally; nothing submitted');
});

await step(BASE + '/demo/', async () => {
  await newPage(BASE + '/demo/');
  await states('demo-chip', page.getByText('Haircuts & styling', { exact: true }).first(), ['default', 'hover'], { title: 'Demo service chip', group: 'Chip' });
  await states('demo-continue', page.getByRole('button', { name: 'Continue', exact: true }), B, { title: 'Demo Continue', group: 'Button' });
});

await step(BASE + '/trial/', async () => {
  await newPage(BASE + '/trial/');
  await states('trial-chip', page.getByText('Haircuts & styling', { exact: true }).first(), ['default'], { title: 'Trial service chip', group: 'Chip' });
});

await step(APP + '/login', async () => {
  await newPage(APP + '/login', 2800);
  await states('login-email', page.locator('#login-page-email'), ['default', 'focused', 'filled'], { title: 'Login email field', group: 'Text field' });
  await states('login-password', page.locator('#login-page-password'), ['default', 'focused'], { title: 'Login password field', group: 'Text field' });
  await states('login-toggle', page.getByRole('button', { name: 'Toggle password visibility' }), B, { title: 'Password visibility toggle', group: 'Icon button' });
  await states('login-submit', page.getByRole('button', { name: 'Log In', exact: true }), B, { title: 'Log In button', group: 'Button' });
  await states('login-forgot', page.getByRole('link', { name: 'Forgot password?' }), ['default', 'hover', 'focus-visible'], { title: 'Forgot password link', group: 'Link' });
});

await step(APP + '/forgot-password', async () => {
  await newPage(APP + '/forgot-password', 2200);
  await states('forgot-email', page.locator('input').first(), ['default', 'focused'], { title: 'Reset email field', group: 'Text field' });
  await states('forgot-continue', page.getByRole('button', { name: 'Continue', exact: true }), B, { title: 'Reset Continue', group: 'Button' });
});

await step(BOOK, async () => {
  await newPage(BOOK, 3500);
  const rebook = page.getByRole('button', { name: /Rebook a past service/i });
  await states('book-rebook', rebook, B, { title: 'Rebook a past service', group: 'Link' });
});

await step(BASE + '/learn/', async () => {
  await newPage(BASE + '/learn/');
  await states('learn-search', page.locator('#learning-center-search'), ['default', 'focused'], { title: 'Learning Center search', group: 'Text field' });
});

save();
log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
if (failed.length) { console.error('pages failed:', failed.join(', ')); process.exitCode = 1; }
