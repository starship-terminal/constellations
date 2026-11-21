// Measure public IFTTT controls from computed styles. Writes raw/components-computed.json.
// Does not type into a password or email field, and does not submit a form.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(here, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const PROPS = [
  'color', 'backgroundColor', 'backgroundImage', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'textTransform', 'textDecorationLine', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'minHeight', 'width', 'display', 'opacity', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
];

function pick(style) {
  const o = {};
  for (const k of PROPS) o[k] = style[k];
  return o;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const cdp = await context.newCDPSession(page);

async function open(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1600);
}

async function measure(selector, note) {
  const handle = await page.locator(selector).first().elementHandle({ timeout: 8000 }).catch(() => null);
  if (!handle) return { selector, note, missing: true };
  const box = await handle.boundingBox();
  const style = await page.evaluate(([el, props]) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    o.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, [handle, PROPS]);
  return { selector, note, box, ...style };
}

async function states(selector, note) {
  const handle = await page.locator(selector).first().elementHandle({ timeout: 8000 }).catch(() => null);
  if (!handle) return { selector, note, missing: true };
  const read = () => page.evaluate(([el, props]) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    return o;
  }, [handle, PROPS]);
  const out = { selector, note, default: await read() };
  await handle.hover().catch(() => {});
  await page.waitForTimeout(250);
  out.hover = await read();
  try {
    await cdp.send('DOM.enable');
    const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined });
  } catch { /* hover-only is enough if CDP force fails */ }
  try {
    const objectId = handle._objectId || (await handle.evaluateHandle((el) => el))._remoteObject?.objectId;
  } catch { /* ignore */ }
  await page.evaluate((el) => el.focus(), handle).catch(() => {});
  await page.waitForTimeout(150);
  out.focus = await read();
  // Force :hover and :focus-visible through the style engine when the live pointer did not change paint.
  try {
    await cdp.send('CSS.enable');
    await cdp.send('CSS.forcePseudoState', { nodeId: (await cdp.send('DOM.getDocument')).root.nodeId, forcedPseudoClasses: [] }).catch(() => {});
  } catch { /* recorded live states stand */ }
  await page.mouse.move(0, 0);
  return out;
}

async function forceStates(selector, note, { press = false } = {}) {
  const loc = page.locator(selector).first();
  if (!await loc.count()) return { selector, note, missing: true };
  const node = await loc.elementHandle();
  const read = async () => page.evaluate(([el, props]) => {
    const s = getComputedStyle(el);
    const o = { text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60) };
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    o.box = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  }, [node, PROPS]);
  const out = { selector, note, default: await read() };
  await loc.hover().catch(() => {});
  await page.waitForTimeout(180);
  out.hover = await read();
  await page.evaluate((el) => { try { el.focus({ preventScroll: true }); } catch { /* not focusable */ } }, node).catch(() => {});
  await page.waitForTimeout(120);
  out.focus = await read();
  // Pressed only when asked, and only while the pointer is down. mouseup follows immediately.
  // Never used on a link or a submit control.
  if (press) {
    const box = await loc.boundingBox();
    if (box) {
      await page.mouse.move(box.x + Math.min(8, box.width / 2), box.y + box.height / 2);
      await page.mouse.down();
      await page.waitForTimeout(80);
      out.pressed = await read();
      await page.mouse.up();
    }
  }
  await page.mouse.move(2, 2);
  return out;
}

const readings = { capturedAt: new Date().toISOString(), pages: {} };

await open('https://ifttt.ai/');
readings.pages.home = {
  url: page.url(),
  viewport: await page.evaluate(() => ({ innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio })),
  body: await page.evaluate(() => {
    const b = getComputedStyle(document.body);
    const h = document.querySelector('header');
    const hs = h ? getComputedStyle(h) : null;
    return {
      color: b.color, backgroundColor: b.backgroundColor, fontFamily: b.fontFamily, fontSize: b.fontSize, lineHeight: b.lineHeight,
      headerHeight: h ? Math.round(h.getBoundingClientRect().height) : null,
      headerBg: hs?.backgroundColor, headerColor: hs?.color,
    };
  }),
  h1: await measure('h1', 'home display'),
  navLink: await forceStates('header a[href="https://ifttt.ai/explore"]', 'nav link'),
  primary: await forceStates('button.button-primary', 'hero start building'),
  tab: await forceStates('button.featured-tab', 'featured tab', { press: true }),
  card: await measure('a[href*="/applets/"]', 'applet card link'),
};

await open('https://ifttt.ai/plans');
readings.pages.plans = {
  url: page.url(),
  h1: await measure('h1', 'plans title'),
  switch: await forceStates('[role="switch"]', 'yearly switch', { press: true }),
  about: await forceStates('button[aria-expanded]', 'about credits'),
  summary: await measure('summary', 'faq summary'),
  cta: await forceStates('a[href*="/subscriptions/"]', 'plan get started'),
  price: await page.evaluate(() => {
    const el = [...document.querySelectorAll('h2, h3, p, span, div')].find((e) => /\$\d/.test(e.innerText || '') && e.children.length < 3);
    if (!el) return null;
    const s = getComputedStyle(el);
    return { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), color: s.color, fontSize: s.fontSize, fontWeight: s.fontWeight, fontFamily: s.fontFamily };
  }),
};

await open('https://ifttt.ai/login');
readings.pages.login = {
  url: page.url(),
  h1: await measure('h1', 'login title'),
  email: await measure('input[type="email"], input[name="user[email]"], input[name="login"]', 'email field, not typed'),
  password: await measure('input[type="password"]', 'password field, not typed'),
  submit: await measure('input[type="submit"], button[type="submit"]', 'login submit, not clicked'),
  google: await measure('[role="button"], a, button', 'first identity control, not clicked'),
};

await open('https://ifttt.ai/hue');
readings.pages.service = {
  url: page.url(),
  h1: await measure('h1', 'service title'),
  share: await forceStates('button[aria-label="share"]', 'share', { press: true }),
  copy: await forceStates('button.copy', 'copy', { press: true }),
  showMore: await forceStates('button.clamp-toggle', 'show more', { press: true }),
  back: await forceStates('a[href="/explore"]', 'back'),
};

await open('https://ifttt.ai/docs/api_reference');
readings.pages.docs = {
  url: page.url(),
  h1: await measure('h1', 'docs title'),
  code: await measure('pre, code', 'code sample'),
  menu: await measure('button', 'docs menu button'),
};

await open('https://ifttt.ai/mcp');
readings.pages.mcp = {
  url: page.url(),
  tab: await forceStates('[role="tab"]', 'mcp client tab', { press: true }),
  copy: await measure('button', 'first button on the page'),
};

// A second phone context for the hamburger.
const phone = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  locale: 'en-US',
});
const mp = await phone.newPage();
await mp.goto('https://ifttt.ai/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await mp.waitForTimeout(1200);
readings.pages.mobileHome = await mp.evaluate(() => {
  const btn = document.querySelector('button.closed');
  const s = btn ? getComputedStyle(btn) : null;
  const r = btn?.getBoundingClientRect();
  return {
    url: location.href,
    innerWidth: innerWidth,
    innerHeight: innerHeight,
    dpr: devicePixelRatio,
    menu: s ? {
      width: s.width, height: s.height, backgroundColor: s.backgroundColor, color: s.color,
      box: r ? { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } : null,
    } : null,
  };
});

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(readings, null, 2));
console.log('wrote components-computed.json', JSON.stringify({
  homeH1: readings.pages.home.h1?.fontSize,
  primary: readings.pages.home.primary?.default?.backgroundColor,
  loginField: readings.pages.login.email?.missing ? 'missing' : readings.pages.login.email?.height,
}, null, 2));
await browser.close();
