// Measures Parallel's public controls. Writes raw/components-computed.json
// and crops. Does not submit forms or click LinkedIn, Google, or Apple.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE, closePromo, PROPS, crop } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const pages = [
  { key: 'home', route: '/' },
  { key: 'employers', route: '/employers' },
  { key: 'search', route: '/app/candidate/search' },
  { key: 'job', route: '/app/candidate/job/6aff911a9a678d5f427fedc8' },
  { key: 'pricing', route: '/pricing' },
  { key: 'blog', route: '/blog' },
  { key: 'ai-training', route: '/ai-training' },
  { key: 'work-form', route: '/work-form' },
  { key: 'login-wall', route: '/login' },
];

const browser = await chromium.launch();
const out = { readAt: new Date().toISOString().slice(0, 10), source: BASE, pages: {} };

async function readPage(ctx, spec) {
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await page.goto(BASE + spec.route, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(2500);
  await closePromo(page);
  const data = await page.evaluate((props) => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 8 && r.height > 8 && r.top < innerHeight && r.bottom > 0 && cs.visibility !== 'hidden' && cs.display !== 'none';
    };
    function style(el) {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const o = { text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 50), rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
      for (const k of props) o[k] = cs[k];
      return o;
    }
    const buttons = [...document.querySelectorAll('button, a')].filter(vis).slice(0, 18).map(style);
    const inputs = [...document.querySelectorAll('input, textarea')].filter(vis).slice(0, 4).map(style);
    const headings = [...document.querySelectorAll('h1, h2')].filter(vis).slice(0, 4).map(style);
    const body = getComputedStyle(document.body);
    return {
      title: document.title,
      url: location.pathname,
      page: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize },
      buttons, inputs, headings,
    };
  }, PROPS);

  // Focus the first visible button and record focus-visible.
  const focus = await page.evaluate(() => {
    const el = [...document.querySelectorAll('button, a')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 20 && r.height > 16 && r.top > 0 && r.top < 200;
    });
    if (!el) return null;
    el.setAttribute('data-m-focus', '1');
    el.focus();
    return true;
  });
  let focusStyle = null;
  if (focus) {
    await page.keyboard.press('Shift');
    await page.waitForTimeout(200);
    const loc = page.locator('[data-m-focus="1"]');
    const node = await cdp.send('DOM.getDocument', { depth: 0 });
    const q = await cdp.send('DOM.querySelector', { nodeId: node.root.nodeId, selector: '[data-m-focus="1"]' });
    if (q.nodeId) {
      await cdp.send('CSS.forcePseudoState', { nodeId: q.nodeId, forcedPseudoClasses: ['focus-visible'] });
      await page.waitForTimeout(200);
      focusStyle = await loc.evaluate((el, props) => {
        const cs = getComputedStyle(el);
        const o = { text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40) };
        for (const k of ['outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'boxShadow', 'backgroundColor', 'color', 'borderTopColor', 'borderTopWidth']) o[k] = cs[k];
        return o;
      }, PROPS);
      await cdp.send('CSS.forcePseudoState', { nodeId: q.nodeId, forcedPseudoClasses: ['hover'] }).catch(() => {});
      await page.waitForTimeout(150);
      const hover = await loc.evaluate((el) => {
        const cs = getComputedStyle(el);
        return { backgroundColor: cs.backgroundColor, color: cs.color, boxShadow: cs.boxShadow, outline: cs.outline };
      });
      focusStyle.hover = hover;
      try { await crop(page, loc, spec.key + '-focus'); } catch (e) { focusStyle.cropError = String(e.message).slice(0, 80); }
    }
  }
  data.focus = focusStyle;
  await page.close();
  return data;
}

for (const spec of pages) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  try {
    out.pages[spec.key] = await readPage(ctx, spec);
    log('measured', spec.key, out.pages[spec.key].title.slice(0, 40));
  } catch (e) {
    log('FAIL', spec.key, e.message.split('\n')[0]);
    out.pages[spec.key] = { error: e.message.split('\n')[0] };
  }
  await ctx.close();
}
await browser.close();
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote components-computed.json');
