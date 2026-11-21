// Measures Sharewillow's public components. No form submit, no auth, no typed
// email or phone. Sample field text is the word "sample" and is deleted.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, centre, RAW, chromium, UA } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = { _meta: { product: 'sharewillow', captured: '2026-11-21', route: 'public-web' }, components: {} };
const log = (...a) => console.log(...a);

let page, context, cdp;

async function newPage(url, { mobile = false } = {}) {
  if (context) await context.close().catch(() => {});
  const launched = await launch(mobile ? { mobile: true } : { width: 1440, height: 900 });
  context = launched.context;
  page = await context.newPage();
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await open(page, url, { wait: 2000 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function reset() {
  await page.mouse.move(8, 8).catch(() => {});
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(200);
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

async function measure(key, state, loc, via) {
  const c = out.components[key];
  try {
    const target = loc.first();
    await centre(target);
    const s = await styleOf(target);
    let file = null;
    try { file = await crop(page, target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    c.states[state] = { ...s, crop: file, via };
    log(' ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h), s.backgroundColor, s.color, s.fontSize);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180), via };
    log(' !', key, state, String(e.message || e).slice(0, 100));
  }
}

function comp(key, meta) {
  out.components[key] = { ...meta, states: {} };
}

async function states(key, loc, list, meta) {
  comp(key, meta);
  const target = loc;
  if (!(await target.count())) {
    out.components[key].missing = true;
    log(' ! missing', key);
    return;
  }
  for (const st of list) {
    let undo;
    try {
      await reset();
      const el = target.first();
      await centre(el);
      let via = 'at rest';
      if (st === 'hover') {
        await el.hover({ timeout: 4000 });
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        await el.focus();
        await page.keyboard.press('Shift+Tab');
        await page.keyboard.press('Tab');
        await page.waitForTimeout(200);
        via = 'keyboard focus';
      } else if (st === 'pressed') {
        undo = await forcePseudo(el, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await el.click({ timeout: 3000 });
        via = 'clicked into the field; nothing typed that is an address';
      }
      await measure(key, st, target, via);
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 160) };
      log(' !', key, st, String(e.message || e).slice(0, 80));
    }
    if (undo) await undo();
  }
}

const B = ['default', 'hover', 'focus-visible', 'pressed'];

await newPage(BASE + '/');
await states('button-primary', page.getByRole('link', { name: /Book a demo/ }).nth(1), B, {
  title: 'Primary button', group: 'Button', selector: 'link Book a demo (hero)',
});
await states('button-quiet', page.getByRole('link', { name: /See the app/ }).first(), B, {
  title: 'Quiet link button', group: 'Link', selector: 'link See the app',
});
await states('nav-link', page.getByRole('link', { name: 'Pricing', exact: true }).first(), ['default', 'hover'], {
  title: 'Header nav link', group: 'Link', selector: 'header Pricing',
});
await states('badge', page.getByText('COMING SOON', { exact: true }).first(), ['default'], {
  title: 'Coming soon badge', group: 'Badge', selector: 'COMING SOON',
});
await states('announcement', page.getByRole('link', { name: /raised/i }).first(), ['default', 'hover'], {
  title: 'Announcement bar', group: 'Banner', selector: 'top announcement link',
});
await page.getByRole('button', { name: 'Product', exact: true }).first().click();
await page.waitForTimeout(400);
await states('menu', page.locator('[role="menu"], [id]').filter({ hasText: 'Technician Mobile App' }).first(), ['opened'], {
  title: 'Product menu', group: 'Menu', selector: 'Product disclosure',
});

await newPage(BASE + '/pricing');
await states('card', page.locator('section, article, div').filter({ hasText: /per tech|month/i }).first(), ['default'], {
  title: 'Pricing block', group: 'Card', selector: 'pricing section',
});

await newPage(BASE + '/demo');
const field = page.locator('input:not([type="hidden"]):not([type="checkbox"]):not([type="email"]):not([type="tel"])').first();
await states('text-field', field, ['default', 'hover', 'focus-visible', 'focused'], {
  title: 'Demo form field', group: 'Text field', selector: 'first non-email input on /demo',
});

await newPage('https://app.sharewillow.com/login');
await states('login-card', page.locator('form, [class*="card"], main').first(), ['default'], {
  title: 'Login card', group: 'Dialog', selector: 'login form, unread past the wall',
});
await states('login-button', page.getByRole('button', { name: 'Login', exact: true }), ['default'], {
  title: 'Login submit', group: 'Button', selector: 'Login button, not clicked',
});

fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
log('wrote', OUT, 'components', Object.keys(out.components).length);
await context.close();
