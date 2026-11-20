// Measures onmarathon.com's public components in every state reachable
// without signing in, submitting a form, or filling a booking widget.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and one crop per component and state.
// Presses are local only: hover, keyboard focus, CDP :active, the phone
// menu, and the pricing Pay Monthly toggle. Sign In, Get Started and the
// SavvyCal embed are not activated.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { product: 'onmarathon.com', captured: '2026-11-21', components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

let page, cdp, current;

async function newPage(url, { mobile = false } = {}) {
  const b = page ? page.context().browser() : null;
  const browser = b || (await launch()).browser;
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = url;
  log('open', url, mobile ? 'mobile' : 'desktop');
  await open(page, BASE + url, { wait: 1600 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return browser;
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
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, loc, via, meta) {
  const c = (out.components[key] ??= { ...meta, states: {} });
  c.page = current;
  try {
    const target = loc.filter({ visible: true }).first();
    if (!(await target.count())) { c.states[state] = { error: 'not visible' }; log('  !', key, state, 'missing'); return; }
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, 6); }
    catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    c.states[state] = { ...s, crop: file, via };
    log('  ', key, state, s._box && Math.round(s._box.width) + 'x' + Math.round(s._box.height), s.color || s.backgroundColor);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 100));
  }
}

async function states(key, loc, meta, list = ['default', 'hover', 'focus-visible', 'pressed']) {
  for (const st of list) {
    await reset();
    const target = loc.filter({ visible: true }).first();
    if (!(await target.count())) { await record(key, st, loc, 'missing', meta); continue; }
    await target.scrollIntoViewIfNeeded().catch(() => {});
    let undo, via = 'at rest';
    if (st === 'hover') {
      await target.hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(350);
      via = 'mouse hover';
    } else if (st === 'focus-visible') {
      via = await kbFocus(target);
    } else if (st === 'pressed') {
      undo = await forcePseudo(target, ['active', 'hover']);
      via = 'CDP forcePseudoState :active:hover';
    } else if (st === 'selected') {
      via = 'billing toggle selected half';
    } else if (st === 'opened') {
      via = 'phone menu held open';
    }
    await record(key, st, loc, via, meta);
    if (undo) await undo();
  }
}

const browser = await (async () => {
  const launched = await launch();
  page = await launched.context.newPage();
  return launched.browser;
})();

// Desktop home
await newPage('/');
await states('banner', page.locator('a').filter({ hasText: 'Marathon archive' }).first(), {
  group: 'Shell', title: 'Archive banner', desc: 'The lime strip at the top of every public page. It links off-site and was not followed.',
});
await states('wordmark', page.getByRole('link', { name: 'Marathon', exact: true }).first(), {
  group: 'Shell', title: 'Wordmark', desc: 'Logo plus the word Marathon. Links to the homepage.',
});
await states('nav-link', page.getByRole('link', { name: 'For Agencies', exact: true }).first(), {
  group: 'Shell', title: 'Nav link', desc: 'A header text link. Product, For Agencies and Pricing share this treatment.',
});
await states('sign-in', page.getByRole('link', { name: 'Sign In', exact: true }).first(), {
  group: 'Shell', title: 'Sign in link', desc: 'Quiet header link. Following it redirects to the archive homepage with no login form. Measured, not followed.',
});
await states('button-primary', page.getByRole('link', { name: 'Get Started', exact: true }).first(), {
  group: 'Button', title: 'Primary button', desc: 'Black pill. Following it redirects to the archive homepage with no signup form. Measured, not followed.',
});
await states('heading', page.getByRole('heading', { level: 1 }).first(), {
  group: 'Type', title: 'Display heading', desc: 'The page h1.',
}, ['default']);
const footerLink = page.locator('footer a').filter({ hasText: 'Demo' }).first();
await states('footer-link', footerLink, {
  group: 'Footer', title: 'Footer link', desc: 'A text link in the footer columns.',
});
await page.close();

// Pricing
await newPage('/pricing');
await states('billing-selected', page.getByRole('button', { name: 'Pay Annually' }), {
  group: 'Pricing', title: 'Billing toggle, selected', desc: 'The selected half of the Pay Annually / Pay Monthly control. Default is Pay Annually.',
}, ['default', 'hover', 'focus-visible', 'pressed', 'selected']);
await states('billing-idle', page.getByRole('button', { name: 'Pay Monthly' }), {
  group: 'Pricing', title: 'Billing toggle, idle', desc: 'The unselected half. Clicking it is a local price change and was used only to capture the monthly screenshot.',
});
await states('badge', page.getByText('Popular', { exact: true }).first(), {
  group: 'Badge', title: 'Popular badge', desc: 'The small chip on the Pro plan card.',
}, ['default']);
await states('plan-card', page.locator('div').filter({ hasText: /^Free/ }).first(), {
  group: 'Card', title: 'Free plan card', desc: 'The white plan card. The Pro card uses the same radius on the lime fill.',
}, ['default']);
// Pro card: the lime one. Find by background.
const pro = page.locator('div').filter({ has: page.getByText('Popular', { exact: true }) }).last();
await states('plan-card-pro', pro, {
  group: 'Card', title: 'Pro plan card', desc: 'The lime plan card. Fill is the same colour as the archive banner.',
}, ['default']);
await page.close();

// 404
await newPage('/changelog');
await states('button-return', page.getByRole('link', { name: 'Return Home' }), {
  group: 'Button', title: 'Return home button', desc: 'The only control on the 404 page. Same black pill as Get Started.',
});
await page.close();

// Phone menu
await newPage('/', { mobile: true });
await states('menu-button', page.getByRole('button', { name: 'Open menu' }), {
  group: 'Mobile', title: 'Menu button', desc: 'The 40px round icon button that opens the phone nav. Hidden at 1440.',
});
await page.getByRole('button', { name: 'Open menu' }).click();
await page.waitForTimeout(500);
await states('menu-panel', page.locator('nav').filter({ hasText: 'Product' }).last(), {
  group: 'Mobile', title: 'Phone menu', desc: 'The opened phone nav: Product, For Agencies, Pricing, Sign In, Get Started.',
}, ['opened']);
await states('menu-close', page.getByRole('button', { name: 'Close menu' }), {
  group: 'Mobile', title: 'Close menu button', desc: 'The round close control that replaces Open menu while the phone nav is open.',
}, ['default', 'hover']);
await page.close();

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
