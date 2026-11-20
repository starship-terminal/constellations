// Measures LottieFiles public components without signing in or submitting.
//
//   PLAYWRIGHT=.../playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and crops under components/crops/.
// Log in, Sign up, Download submit, checkout and app.lottiefiles.com are never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, hideConsent, styleOf, crop, centre, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'lottiefiles', captured: new Date().toISOString(), route: 'public signed-out' }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  pricing: '/pricing',
  animations: '/free-animations',
  animation: '/free-animation/loading-animation-for-client-book-0DK063WUDW',
  marketplace: '/marketplace',
  notfound: '/this-page-does-not-exist-capture',
};

let page, cdp, current, context;
const run = new Date().toLocaleDateString('en-CA'); // the local date of the capture

async function newPage(key, { mobile = false } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait: 2800 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
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
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(300);
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
  Object.assign(c, { page: current, run, url: BASE + URLS[current] }, meta);
  c.states ??= {};
  return c;
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, opts.cropLoc || loc, `${key}-${state}`, opts.pad ?? 6); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.backgroundColor, s.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true }));
        await page.waitForTimeout(400);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
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
  home: 'Marketing home',
  pricing: 'Pricing',
  library: 'Animation library',
  animation: 'Public animation page',
  overlay: 'Menus',
};

async function home() {
  await newPage('home');
  const g = G.shell;
  await S('nav-signup', page.getByRole('button', { name: 'Sign up' }), ['default', 'hover', 'pressed'], {
    group: g, title: 'Sign up button', desc: 'Primary header control. Measured, never pressed. Sign-up sits behind this control.', sel: 'button:has-text("Sign up")',
  }, { noScroll: true });
  await S('nav-login', page.getByRole('button', { name: 'Log in' }), ['default', 'hover', 'focus-visible', 'pressed'], {
    group: g, title: 'Log in button', desc: 'Quiet header control. Measured, never pressed. The editor and dashboard sit behind sign-in.', sel: 'button:has-text("Log in")',
  }, { noScroll: true });
  await S('nav-products', page.getByRole('button', { name: 'Products' }), ['default', 'hover', 'focus-visible'], {
    group: g, title: 'Products menu button', desc: 'Opens the products menu on hover. The menu shot is a local toggle.', sel: 'button:has-text("Products")',
  }, { noScroll: true });
  await S('nav-pricing', page.getByRole('link', { name: 'Pricing' }).first(), B4, {
    group: g, title: 'Pricing link', sel: 'a[href*="/pricing"]',
  }, { noScroll: true });
  await S('search-button', page.getByRole('button', { name: 'Search animations' }), ['default', 'hover', 'focus-visible'], {
    group: g, title: 'Search animations control', desc: 'Header search trigger. The search field itself was not submitted.', sel: 'button:has-text("Search animations")',
  }, { noScroll: true });
  await S('hero-heading', page.locator('h1').first(), ['default'], {
    group: G.home, title: 'Home heading', sel: 'h1',
  }, { noScroll: true });
  await S('hero-cta', page.getByRole('link', { name: 'Get started for free' }).first(), B4, {
    group: G.home, title: 'Get started for free', desc: 'Primary marketing CTA. Links to app.lottiefiles.com. Measured, never followed.', sel: 'a:has-text("Get started for free")',
  });
  await S('feature-card', page.locator('button').filter({ hasText: 'Tiny file format' }).first(), ['default', 'hover'], {
    group: G.home, title: 'Feature card', sel: 'button:has-text("Tiny file format")',
  });
  await page.getByRole('button', { name: 'Products' }).first().hover();
  await page.waitForTimeout(600);
  const menu = page.locator('[role="menu"], [data-radix-popper-content-wrapper], [data-state="open"]').first();
  await S('products-menu', menu, ['default'], {
    group: G.overlay, title: 'Products menu', desc: 'Opened by hovering Products. Closed without following a destination.', sel: '[data-state="open"]',
  }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape');
  await page.close();
}

async function pricing() {
  await newPage('pricing');
  await S('pricing-heading', page.locator('h1').first(), ['default'], {
    group: G.pricing, title: 'Pricing heading', sel: 'h1',
  }, { noScroll: true });
  await S('plan-individual', page.getByRole('link', { name: 'Get Individual Plan' }).first(), ['default', 'hover', 'focus-visible'], {
    group: G.pricing, title: 'Get Individual Plan', desc: 'Links to app.lottiefiles.com/upgrade. Measured, never followed. Checkout was not opened.', sel: 'a:has-text("Get Individual Plan")',
  });
  await S('plan-team', page.getByRole('link', { name: 'Get Team Plan' }).first(), ['default', 'hover'], {
    group: G.pricing, title: 'Get Team Plan', desc: 'Links to the upgrade checkout. Measured, never followed.', sel: 'a:has-text("Get Team Plan")',
  });
  await S('plan-sales', page.getByRole('link', { name: 'Contact Sales' }).first(), ['default', 'hover'], {
    group: G.pricing, title: 'Contact Sales', desc: 'Leads to a sales form. Measured, never submitted.', sel: 'a:has-text("Contact Sales")',
  });
  await page.close();
}

async function animations() {
  await newPage('animations');
  await S('library-heading', page.locator('h1').first(), ['default'], {
    group: G.library, title: 'Library heading', sel: 'h1',
  }, { noScroll: true });
  const card = page.locator('a[href*="/free-animation/"]').first();
  await S('animation-card', card, ['default', 'hover'], {
    group: G.library, title: 'Animation card', desc: 'A published free-animation card on the public library.', sel: 'a[href*="/free-animation/"]',
  });
  await page.close();
}

async function animation() {
  await newPage('animation');
  await S('animation-heading', page.locator('h1').first(), ['default'], {
    group: G.animation, title: 'Animation title', sel: 'h1',
  }, { noScroll: true });
  await S('animation-download', page.getByRole('button', { name: 'Download' }).first(), ['default', 'hover', 'focus-visible'], {
    group: G.animation, title: 'Download button', desc: 'Opens a format menu. The download itself was not started. Some formats sit behind sign-in.', sel: 'button:has-text("Download")',
  }, { noScroll: true });
  await S('animation-save', page.getByRole('button', { name: 'Save animation' }).first(), ['default', 'hover'], {
    group: G.animation, title: 'Save animation', desc: 'Measured, never pressed. Saving sits behind sign-in.', sel: 'button:has-text("Save animation")',
  }, { noScroll: true });
  await S('animation-edit', page.getByRole('link', { name: 'Edit with AI' }).first(), ['default', 'hover'], {
    group: G.animation, title: 'Edit with AI', desc: 'Links to creator.lottiefiles.com. Measured, never followed. The editor sits behind sign-in.', sel: 'a:has-text("Edit with AI")',
  });
  await page.getByRole('button', { name: 'Download' }).first().click().catch(() => {});
  await page.waitForTimeout(500);
  const item = page.getByRole('button', { name: 'GIF' }).first();
  await S('download-format', item, ['default'], {
    group: G.overlay, title: 'Download format row', desc: 'A format row in the Download menu. Not activated.', sel: 'button:has-text("GIF")',
  }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape');
  await page.close();
}

async function marketplace() {
  await newPage('marketplace');
  await S('marketplace-cta', page.getByRole('link', { name: 'Unlock All Animations' }).first(), ['default', 'hover'], {
    group: G.library, title: 'Unlock All Animations', desc: 'Links to app.lottiefiles.com premium. Measured, never followed. Checkout was not opened.', sel: 'a:has-text("Unlock All Animations")',
  });
  await page.close();
}

async function notfound() {
  await newPage('notfound');
  await S('notfound-heading', page.locator('h1, h2').first(), ['default'], {
    group: G.home, title: 'Not found heading', sel: 'h1, h2',
  }, { noScroll: true });
  await page.close();
}

const { browser, context: ctx } = await launch({ width: 1440, height: 900, dpr: 2 });
context = ctx;
try {
  await home();
  await pricing();
  await animations();
  await animation();
  await marketplace();
  await notfound();
  save();
  log('wrote', OUT, Object.keys(out.components).length, 'components');
} finally {
  await browser.close();
}
