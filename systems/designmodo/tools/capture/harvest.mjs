// Reads Designmodo custom properties, computed component styles, brand colour
// evidence and colour-use counts from public pages. Writes systems/designmodo/raw/.
// Does not submit forms or enter a builder canvas.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PAGES = [
  ['home', 'https://designmodo.com/'],
  ['postcards', 'https://designmodo.com/postcards/'],
  ['pricing', 'https://designmodo.com/postcards/pricing/'],
  ['email-templates', 'https://designmodo.com/email-templates/'],
  ['sign-in', 'https://designmodo.com/my-account/sign-in/'],
  ['articles', 'https://designmodo.com/articles/'],
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch {}
});

await page.goto(PAGES[0][1], { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(2500);

const brand = await page.evaluate(() => ({
  themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({
    content: m.content, media: m.getAttribute('media'),
  })),
  maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  manifest: document.querySelector('link[rel="manifest"]')?.href || null,
  title: document.title,
}));
log('brand', JSON.stringify(brand));

const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));

const sheetList = [...bodies.entries()].map(([url, css]) => [url, css]);
for (const pair of inline) sheetList.push(pair);
log('sheets', sheetList.length, 'bytes', sheetList.reduce((n, s) => n + s[1].length, 0));

const parsed = await page.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.cssText.split('{')[0].trim().slice(0, 180);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, selector: r.selectorText, context: ctx, props });
    }
  };
  for (const [name, css] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(css);
      walk(sheet.cssRules, [], name.split('/').pop().slice(0, 80));
    } catch (e) {
      rules.push({ file: name, error: String(e).slice(0, 160) });
    }
  }
  return { rules, fonts };
}, sheetList);

const vars = {};
for (const r of parsed.rules) {
  if (!r.props) continue;
  for (const [k, v] of Object.entries(r.props)) {
    (vars[k] ||= []).push({ value: v, selector: r.selector, file: r.file, context: r.context });
  }
}
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  brand,
  varCount: Object.keys(vars).length,
  ruleCount: parsed.rules.length,
  fonts: parsed.fonts,
  vars,
}, null, 1));
log('css vars', Object.keys(vars).length, 'font-face', parsed.fonts.length);

const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'borderRadius', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'minHeight', 'boxShadow', 'outline', 'textTransform', 'display',
];

function styleOf(el) {
  return null;
}

const readings = { capturedAt: new Date().toISOString(), pages: {} };

for (const [id, url] of PAGES) {
  log('measure', id);
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForFunction(() => {
    const h1 = document.querySelector('h1');
    const r = h1 && h1.getBoundingClientRect();
    return r && r.height > 8 && document.documentElement.scrollHeight > 400;
  }, { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(800);
  const measured = await page.evaluate((PROPS) => {
    const pick = (el) => {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return { miss: true, w: Math.round(r.width), h: Math.round(r.height), cls: String(el.className).slice(0, 80) };
      const o = {
        tag: el.tagName.toLowerCase(),
        cls: String(el.className).slice(0, 100),
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      };
      for (const p of PROPS) o[p] = cs[p];
      return o;
    };
    const q = (sel) => pick(document.querySelector(sel));
    const byText = (sel, re) => {
      const el = [...document.querySelectorAll(sel)].find((e) => re.test((e.innerText || '').trim()) && e.getBoundingClientRect().width > 8);
      return pick(el);
    };
    return {
      url: location.href.split('?')[0],
      title: document.title,
      body: pick(document.body),
      h1: pick(document.querySelector('h1')),
      h2: pick(document.querySelector('h2')),
      p: pick(document.querySelector('p')),
      header: q('header, nav.panel'),
      logo: q('a.logo, .logo'),
      navLink: q('a.menu-link'),
      signUp: byText('a.button, a, button', /^sign up$/i),
      logIn: byText('a, button', /^log in$/i),
      primaryButton: byText('a.button, button, a', /open app|get started|login ->|see pricing|start/i),
      greenButton: q('a.button.green, .button.green, a.green'),
      orangeButton: q('a.button.orange, .button.orange, a.orange'),
      field: q('input[type="email"], input.searchField, input[type="text"], input[type="search"]'),
      footer: q('footer'),
      footerLink: q('footer a'),
      card: q('.card, article, .post, .pricing-card, [class*="card"]'),
      link: q('a.p, main a, .content a'),
      theme: {
        colorScheme: getComputedStyle(document.documentElement).colorScheme,
        bg: getComputedStyle(document.body).backgroundColor,
      },
    };
  }, PROPS);
  readings.pages[id] = measured;
}

// hover and focus on home primary and sign-up, without submitting
await page.goto('https://designmodo.com/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1500);
const states = await page.evaluate(async (PROPS) => {
  const read = (el) => {
    const cs = getComputedStyle(el);
    const o = { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), cls: String(el.className).slice(0, 80) };
    for (const p of PROPS) o[p] = cs[p];
    return o;
  };
  const signup = [...document.querySelectorAll('a')].find((a) => /^sign up$/i.test((a.innerText || '').trim()));
  const open = [...document.querySelectorAll('a')].find((a) => /open app/i.test(a.innerText || ''));
  const out = {};
  if (signup) {
    out.signupDefault = read(signup);
    signup.focus();
    out.signupFocus = read(signup);
  }
  if (open) out.openAppDefault = read(open);
  return out;
}, PROPS);
if (states.openAppDefault) {
  const loc = page.locator('a', { hasText: 'Open App' }).first();
  await loc.hover().catch(() => {});
  await page.waitForTimeout(300);
  states.openAppHover = await loc.evaluate((el, PROPS) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const p of PROPS) o[p] = cs[p];
    return o;
  }, PROPS).catch(() => null);
}
readings.states = states;

// colour use counts on home
await page.goto('https://designmodo.com/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1200);
const counts = await page.evaluate(() => {
  const colors = {};
  const radii = {};
  const sizes = {};
  const els = [...document.querySelectorAll('body *')].slice(0, 2500);
  for (const el of els) {
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    const cs = getComputedStyle(el);
    const c = cs.color;
    const bg = cs.backgroundColor;
    if (c && c !== 'rgba(0, 0, 0, 0)') colors[c] = (colors[c] || 0) + 1;
    if (bg && bg !== 'rgba(0, 0, 0, 0)') colors['bg ' + bg] = (colors['bg ' + bg] || 0) + 1;
    if (cs.borderRadius && cs.borderRadius !== '0px') radii[cs.borderRadius] = (radii[cs.borderRadius] || 0) + 1;
    if (cs.fontSize) sizes[cs.fontSize] = (sizes[cs.fontSize] || 0) + 1;
  }
  const top = (o) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, 30);
  return { colors: top(colors), radii: top(radii), sizes: top(sizes) };
});
readings.counts = { home: counts };

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(readings, null, 1));
log('wrote readings');
await browser.close();
