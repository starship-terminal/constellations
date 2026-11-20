// Measures mapbox.com's public components without signing in, submitting or buying.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs [home|pricing|contact|docs|mobile]
//
// Writes raw/components-computed.json and one crop per component and state.
// The OneTrust banner is hidden, never answered. Sign-in, sign-up and form
// submit are never followed. Pressed is a CDP :active:hover force, not a real click
// on a navigation control.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/',
  pricing: BASE + '/pricing',
  contact: BASE + '/contact',
  docs: 'https://docs.mapbox.com/',
  gljs: 'https://docs.mapbox.com/mapbox-gl-js/guides/',
};
let page, cdp, current, view, run;
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const want = (k) => !pageArg.length || pageArg.includes(k);

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, view, run, url: URLS[current] }, meta);
  c.states ??= {};
  return c;
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
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
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    const prev = c.states[state];
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.style && s.style.backgroundColor);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, target, list, meta = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  const loc = target;
  const box = await loc.boundingBox().catch(() => null);
  if (!(await loc.count()) || !box || box.width < 2 || box.height < 2) {
    log('  ! missing', key);
    if (!Object.keys(out.components[key].states || {}).length) out.components[key].missing = true;
    return;
  }
  delete out.components[key].missing;
  for (const st of list) {
    let undo;
    try {
      await page.mouse.move(2, 2).catch(() => {});
      await centre(loc);
      let via = 'at rest';
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true, timeout: 3000 }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);  // as every other package forces it
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.waitForTimeout(250);
        via = 'focused the field; nothing submitted';
      } else if (st === 'opened') {
        await loc.click({ timeout: 3000 });
        await page.waitForTimeout(500);
        via = 'local toggle, not a navigation';
      }
      await measure(key, st, loc, { via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function newPage(key, { mobile = false, wait = 3500 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = page ? page.context().browser() : null;
  const browser = b || (await launch()).browser;
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', reducedMotion: 'reduce' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? 'mobile' : '');
  await open(page, URLS[key], { wait });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  await closePromo(page);
  return browser;
}

let browser;
run = new Date().toISOString().slice(0, 10);

if (want('home')) {
  browser = await newPage('home');
  await S('nav-signup', page.locator('nav a.button.is-nav').filter({ hasText: 'Sign up' }).first(), B4, {
    title: 'Nav sign-up pill', group: 'Button', desc: 'Blue pill in the desktop nav. The link was never followed.', sel: 'nav a.button.is-nav',
  });
  await S('nav-login', page.locator('nav a').filter({ hasText: /^Log in$/ }).first(), B4, {
    title: 'Nav log-in link', group: 'Link', desc: 'Text link beside the sign-up pill. Never followed.', sel: 'nav a Log in',
  });
  await S('nav-products', page.locator('nav button.nav_link-toggle').filter({ hasText: 'Products' }).first(), ['default', 'hover', 'focus-visible', 'opened'], {
    title: 'Products menu toggle', group: 'Menu', desc: 'Local nav toggle. Opened once, then closed. Not a link.', sel: 'button.nav_link-toggle',
  });
  await page.keyboard.press('Escape').catch(() => {});
  await S('hero-h1', page.locator('h1').first(), ['default'], {
    title: 'Home headline', group: 'Type', desc: 'Cera Pro display headline on the home hero.', sel: 'h1',
  });
  // Webflow paints the pill on .button_inner, not the transparent anchor.
  await S('cta-primary', page.locator('a.button_component').filter({ hasText: 'Get started for free' }).first().locator('.button_inner'), B4, {
    title: 'Get started for free', group: 'Button', desc: 'Hero CTA fill (.button_inner). The anchor was never followed. Pressed is a CDP :active:hover force.', sel: 'a.button_component .button_inner',
  });
  await S('cta-secondary', page.locator('a.button_component').filter({ hasText: /^Contact us$/ }).first().locator('.button_inner'), B4, {
    title: 'Contact us (hero)', group: 'Button', desc: 'Stroke pill beside the hero CTA. Never followed.', sel: 'a.button_component .button_inner stroke',
  });
  save();
  await page.context().close();
}

if (want('pricing')) {
  browser = await newPage('pricing');
  await S('pricing-h1', page.locator('h1').first(), ['default'], {
    title: 'Pricing headline', group: 'Type', desc: 'Pricing page h1.', sel: 'h1',
  });
  await S('pricing-tab', page.locator('a.pricing_subnav-link').filter({ hasText: /^Maps$/ }).first(), ['default', 'hover', 'focus-visible'], {
    title: 'Pricing product link', group: 'Tabs', desc: 'Maps link in the pricing subnav. Measured at rest, hover and focus. The link was not followed for a purchase.', sel: 'a.pricing_subnav-link',
  });
  const range = page.locator('input.product-sku_range-input').first();
  await S('pricing-slider', range, ['default', 'focused'], {
    title: 'Pricing usage slider', group: 'Slider', desc: 'Usage range on a public price calculator. Not submitted.', sel: 'input.product-sku_range-input',
  });
  await S('plan-card', page.locator('[class*="pricing_card"], [class*="product-card"], [class*="sku_card"]').first(), ['default'], {
    title: 'Pricing card', group: 'Card', desc: 'First visible pricing card, if the page paints one as its own box.', sel: 'pricing card',
  });
  save();
  await page.context().close();
}

if (want('contact')) {
  browser = await newPage('contact', { wait: 4500 });
  const field = page.locator('input.hsfc-TextInput, input[type="email"], input[type="text"]').filter({ visible: true }).first();
  await S('contact-input', field, ['default', 'focused'], {
    title: 'Contact field', group: 'Text field', desc: 'HubSpot field on the public contact page. Focused only. The form was not submitted.', sel: 'input.hsfc-TextInput',
  });
  // Request type is a HubSpot combobox, not a native select. Opened, not submitted.
  await S('contact-select', page.locator('input.hsfc-TextInput[role="combobox"]').first(), ['default', 'focused', 'opened'], {
    title: 'Contact request type', group: 'Select', desc: 'HubSpot combobox on the public contact page. Opened to show the list. No option was chosen and the form was not submitted.', sel: 'input.hsfc-TextInput[role=combobox]',
  });
  save();
  await page.context().close();
}

if (want('docs')) {
  browser = await newPage('docs');
  await S('docs-search', page.getByRole('button', { name: /Search/ }).first(), ['default', 'hover', 'focus-visible', 'opened'], {
    title: 'Docs search button', group: 'Search', desc: 'Opens the public docs search dialog. Nothing was typed into a signed-in console.', sel: 'button Search',
  });
  await page.keyboard.press('Escape').catch(() => {});
  await S('docs-signin', page.getByRole('link', { name: /^Sign in$/ }).first(), B4, {
    title: 'Docs sign-in link', group: 'Link', desc: 'Points at account.mapbox.com. Never followed.', sel: 'a Sign in',
  });
  await S('docs-signup', page.getByRole('link', { name: /^Sign up$/ }).first(), B4, {
    title: 'Docs sign-up link', group: 'Button', desc: 'Points at account.mapbox.com. Never followed.', sel: 'a Sign up',
  });
  await S('docs-card', page.locator('a[href*="mapbox-gl-js"]').filter({ visible: true }).first(), ['default', 'hover'], {
    title: 'Docs GL JS link', group: 'Card', desc: 'A visible GL JS link on the docs index. Not followed for this state shot.', sel: 'a[href*=mapbox-gl-js]',
  });
  save();
  await page.context().close();

  browser = await newPage('gljs');
  await S('docs-h1', page.locator('h1').first(), ['default'], {
    title: 'GL JS guides headline', group: 'Type', desc: 'Public docs heading.', sel: 'h1',
  });
  await S('docs-sidebar-link', page.locator('nav a, aside a').filter({ visible: true }).filter({ hasText: /.+/ }).first(), ['default', 'hover', 'focus-visible'], {
    title: 'Docs sidebar link', group: 'Link', desc: 'First visible text link in the docs nav.', sel: 'nav a',
  });
  const code = page.locator('pre, code').filter({ visible: true }).first();
  await S('docs-code', code, ['default'], {
    title: 'Docs code block', group: 'Code', desc: 'First visible code sample on the guides page.', sel: 'pre',
  });
  save();
  await page.context().close();
}

if (want('mobile')) {
  browser = await newPage('home', { mobile: true });
  const menu = page.locator('a.nav_menu-toggle').first();
  await S('m-menu-button', menu, ['default', 'pressed'], {
    title: 'Mobile menu button', group: 'Icon button', desc: 'Hamburger on the 390-wide nav. Local toggle.', sel: '.nav_mobile-menu-button',
  });
  await S('m-hero', page.locator('h1').first(), ['default'], {
    title: 'Mobile headline', group: 'Type', desc: 'Home h1 at 390.', sel: 'h1',
  });
  save();
  await page.context().close();
}

if (browser) await browser.close().catch(() => {});
log('wrote', OUT, 'components', Object.keys(out.components).length);
