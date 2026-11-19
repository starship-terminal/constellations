// Measures computed styles on Missive's public marketing pages and the
// signed-out mail screens. Writes raw/components-computed.json.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Hover is a real pointer. Focus-visible is Tab. Pressed is a forced
// :active pseudo-class, so no control fires. No form is submitted.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, REF, BASE, MAIL } from './lib.mjs';

const OUT = path.join(REF, 'raw', 'components-computed.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const FIELDS = [
  'backgroundColor', 'color', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'borderRadius', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'padding', 'boxShadow', 'outline', 'height', 'opacity', 'textDecorationLine',
];

function readStyle(spec) {
  const fields = [
    'backgroundColor', 'color', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
    'letterSpacing', 'borderRadius', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
    'padding', 'boxShadow', 'outline', 'height', 'opacity', 'textDecorationLine',
  ];
  const el = document.querySelector(spec.selector);
  if (!el) return null;
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const style = {};
  for (const f of fields) style[f] = cs[f];
  return {
    text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    style,
  };
}

async function states(page, spec) {
  const read = () => page.evaluate(readStyle, spec);
  const out = { selector: spec.selector, page: spec.page };
  out.default = await read();
  if (!out.default) return out;
  if (spec.hover !== false) {
    await page.locator(spec.selector).first().hover({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(180);
    out.hover = await read();
    await page.mouse.move(2, 2);
    await page.waitForTimeout(80);
  }
  if (spec.focus) {
    await page.locator(spec.selector).first().focus().catch(() => {});
    await page.waitForTimeout(120);
    out.focus = await read();
  }
  if (spec.press) {
    await page.locator(spec.selector).first().evaluate((el) => el.classList.add('__pressed')).catch(() => {});
    // Force :active through the DevTools protocol when available.
    const cdp = await page.context().newCDPSession(page).catch(() => null);
    if (cdp) {
      const node = await page.locator(spec.selector).first().elementHandle();
      if (node) {
        const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await node.evaluateHandle((el) => el))._objectId }).catch(() => ({}));
      }
    }
    out.pressed = null;
  }
  return out;
}

async function forceActive(page, selector) {
  const loc = page.locator(selector).first();
  const handle = await loc.elementHandle();
  if (!handle) return null;
  const cdp = await page.context().newCDPSession(page);
  const remote = await handle.evaluateHandle((el) => el);
  const objectId = remote._remoteObject?.objectId || remote._objectId;
  // Playwright's elementHandle has a private object id via CDP.
  const { object } = await cdp.send('Runtime.evaluate', {
    expression: 'document',
    returnByValue: false,
  }).catch(() => ({}));
  void object;
  try {
    await cdp.send('CSS.enable');
    await cdp.send('DOM.enable');
    const doc = await cdp.send('DOM.getDocument');
    const queried = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector });
    if (queried.nodeId) {
      await cdp.send('CSS.forcePseudoState', { nodeId: queried.nodeId, forcedPseudoClasses: ['active', 'focus'] });
      await page.waitForTimeout(80);
      const style = await page.evaluate(readStyle, { selector });
      await cdp.send('CSS.forcePseudoState', { nodeId: queried.nodeId, forcedPseudoClasses: [] }).catch(() => {});
      return style;
    }
  } catch {
    return null;
  }
  return null;
}

const marketing = [
  { key: 'nav-try', page: 'home', selector: 'a.button-base.w-button:not(.s-ghost)', hover: true, press: true },
  { key: 'nav-login', page: 'home', selector: 'a.button-base.s-ghost.w-button', hover: true },
  { key: 'hero-title', page: 'home', selector: 'h1.heading-6xl', hover: false },
  { key: 'hero-body', page: 'home', selector: 'p.text-2xl', hover: false },
  { key: 'watch-demo', page: 'home', selector: 'a.button-base.s-outline, a.button-base.s-secondary, a.s-outline', hover: true },
];

const mail = [
  { key: 'login-title', page: 'login', selector: 'h1, h2', hover: false },
  { key: 'login-google', page: 'login', selector: 'button', hover: true, press: true },
  { key: 'login-email', page: 'login', selector: 'input[type="email"]', hover: true, focus: true },
  { key: 'login-password', page: 'login', selector: 'input[type="password"]', hover: false, focus: true },
  { key: 'login-submit', page: 'login', selector: 'button[type="submit"]', hover: true, press: true },
  { key: 'login-forgot', page: 'login', selector: 'a[href*="forgot"], a', hover: true },
];

async function main() {
  const components = {};
  const { browser, context } = await launch({ width: 1440, height: 900 });
  const page = await context.newPage();
  await open(page, BASE + '/');
  // Resolve the secondary hero button by text, then pin a data attribute.
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'Watch demo');
    if (a) a.setAttribute('data-m', 'watch-demo');
    const login = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'Log in' && el.getBoundingClientRect().y < 80);
    if (login) login.setAttribute('data-m', 'nav-login');
    const demo = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'Book a demo' && el.getBoundingClientRect().y < 80);
    if (demo) demo.setAttribute('data-m', 'nav-demo');
    const trial = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'Try for free' && el.getBoundingClientRect().y < 80);
    if (trial) trial.setAttribute('data-m', 'nav-try');
  });
  const homeSpecs = [
    { key: 'nav-try', selector: '[data-m="nav-try"]' },
    { key: 'nav-login', selector: '[data-m="nav-login"]' },
    { key: 'nav-demo', selector: '[data-m="nav-demo"]' },
    { key: 'hero-title', selector: 'h1' },
    { key: 'hero-body', selector: 'h1 + p, p.text-2xl, p.text-color-b' },
    { key: 'watch-demo', selector: '[data-m="watch-demo"]' },
    { key: 'hero-try', selector: 'a.button-base.w-button' },
  ];
  for (const spec of homeSpecs) {
    const def = await page.evaluate(readStyle, spec);
    const entry = { page: 'https://missiveapp.com/', selector: spec.selector, states: { default: def } };
    if (def && spec.key !== 'hero-title' && spec.key !== 'hero-body') {
      await page.locator(spec.selector).first().hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(200);
      entry.states.hover = await page.evaluate(readStyle, spec);
      entry.states.pressed = await forceActive(page, spec.selector);
      await page.keyboard.press('Tab').catch(() => {});
    }
    components[spec.key] = entry;
    console.log(spec.key, def ? def.style.backgroundColor + ' ' + def.style.color + ' ' + def.style.fontSize : 'MISSING');
  }
  // focus-visible on nav try via keyboard
  await page.keyboard.press('Escape').catch(() => {});
  await page.locator('[data-m="nav-try"]').focus().catch(() => {});
  await page.waitForTimeout(150);
  components['nav-try'].states.focus = await page.evaluate(readStyle, { selector: '[data-m="nav-try"]' });

  await open(page, MAIL + '/#login');
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  await page.waitForTimeout(300);
  const mailSpecs = [
    { key: 'login-title', selector: 'h1' },
    { key: 'login-google', selector: 'button' },
    { key: 'login-email', selector: 'input[type="email"]' },
    { key: 'login-password', selector: 'input[type="password"]' },
    { key: 'login-submit', selector: 'button[type="submit"]' },
    { key: 'login-link', selector: 'a' },
  ];
  for (const spec of mailSpecs) {
    const def = await page.evaluate(readStyle, spec);
    const entry = { page: 'https://mail.missiveapp.com/#login', selector: spec.selector, states: { default: def } };
    if (def && !spec.key.includes('title')) {
      await page.locator(spec.selector).first().hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(180);
      entry.states.hover = await page.evaluate(readStyle, spec);
      entry.states.pressed = await forceActive(page, spec.selector);
    }
    if (spec.key === 'login-email') {
      await page.locator(spec.selector).focus();
      await page.waitForTimeout(150);
      entry.states.focus = await page.evaluate(readStyle, spec);
    }
    components[spec.key] = entry;
    console.log(spec.key, def ? def.text + ' | ' + def.style.backgroundColor + ' ' + def.style.borderRadius : 'MISSING');
  }

  // pricing switch and card
  await open(page, BASE + '/pricing');
  await page.evaluate(() => {
    const sw = document.querySelector('[role="switch"], input[type="checkbox"], button');
    const yearly = [...document.querySelectorAll('button, [role="switch"]')].find((el) => /billed yearly/i.test(el.getAttribute('aria-label') || el.innerText || '') || el.getAttribute('role') === 'switch');
    if (yearly) yearly.setAttribute('data-m', 'billing-switch');
    const card = [...document.querySelectorAll('div, article, section')].find((el) => {
      const t = (el.innerText || '').trim();
      return t.startsWith('Starter') && t.includes('$14') && t.length < 500;
    });
    if (card) card.setAttribute('data-m', 'plan-card');
  });
  for (const spec of [
    { key: 'billing-switch', selector: '[data-m="billing-switch"], [role="switch"]' },
    { key: 'plan-card', selector: '[data-m="plan-card"]' },
  ]) {
    const def = await page.evaluate(readStyle, spec);
    components[spec.key] = { page: 'https://missiveapp.com/pricing', selector: spec.selector, states: { default: def } };
    console.log(spec.key, def ? def.text.slice(0, 40) + ' | ' + def.style.backgroundColor + ' r=' + def.style.borderRadius : 'MISSING');
  }

  await browser.close();
  const doc = {
    source: 'Computed styles on missiveapp.com and mail.missiveapp.com, signed out, 2026-11-19, light, 1440. Hover is a real pointer. Pressed is CSS.forcePseudoState :active. No form submitted.',
    capturedAt: new Date().toISOString(),
    viewport: { width: 1440, height: 900 },
    components,
  };
  fs.writeFileSync(OUT, JSON.stringify(doc, null, 2) + '\n');
  console.log('wrote', OUT);
}

main().catch((e) => { console.error(e); process.exit(1); });
