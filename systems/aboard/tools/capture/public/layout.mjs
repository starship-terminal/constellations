// Probe aboard.com's page layout at four widths and write raw/layout.json:
// per page@width the viewport, document height, the h1's box and font, fixed
// layers, elements with a max-width, CSS-grid containers and the main content
// column. Read-only; the CookieYes strip is hidden, never consented.
import fs from 'fs';
import { fileURLToPath } from 'node:url';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = fileURLToPath(new URL('../../../raw/layout.json', import.meta.url));
const PAGES = {
  home: '/', 'how-we-work': '/how-we-work/', 'case-studies': '/case-studies/',
  foundry: '/foundry/', newsletter: '/newsletter/', podcast: '/podcast/',
  about: '/about/', faq: '/faq/',
  events: '/events/', media: '/media/', careers: '/careers/',
  security: '/security/', perspectives: '/perspectives/',
  whitepaper: '/resources/how-to-utilize-ai-agents-to-actually-deliver-results/',
  essay: '/welcome-to-the-age-of-receipts/',
};
const WIDTHS = [1440, 390];
const HIDE = '.cky-consent-container, .cky-modal { display: none !important; }';
(async () => {
  const b = await chromium.launch();
  const out = {};
  for (const [key, path] of Object.entries(PAGES)) {
    for (const vw of WIDTHS) {
      const ctx = await b.newContext({ viewport: { width: vw, height: 900 } });
      const p = await ctx.newPage();
      await p.goto('https://aboard.com' + path, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await p.waitForTimeout(1500);
      // A Cloudflare challenge page refuses addStyleTag. Hide the consent
      // strip in the DOM instead, and skip a page that never became the site.
      const ready = await p.evaluate((hide) => {
        const t = document.body?.innerText || '';
        if (/just a moment|verify you are human|performing security verification/i.test(t) || t.trim().length < 40) return false;
        for (const el of document.querySelectorAll(hide)) el.style.setProperty('display', 'none', 'important');
        return true;
      }, '.cky-consent-container, .cky-modal, #ckyPreferenceCenter').catch(() => false);
      if (!ready) { console.log('SKIP challenge', key, vw); await ctx.close(); continue; }
      await p.waitForTimeout(800);
      const r = await p.evaluate(() => {
        const box = el => { const b = el.getBoundingClientRect(); return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height) }; };
        const sel = el => { const c = (el.className || '').toString().trim().split(/\s+/).slice(0, 3).join('.'); return `${el.tagName.toLowerCase()}${c ? '.' + c : ''}`; };
        const h1 = document.querySelector('h1, [class*="hero"] [class*="title"], .main-content h2');
        const fixed = [...document.querySelectorAll('body *')].filter(el => { const s = getComputedStyle(el); return (s.position === 'fixed' || s.position === 'sticky') && el.getBoundingClientRect().width > 200; }).slice(0, 8)
          .map(el => ({ el: sel(el), pos: getComputedStyle(el).position, top: getComputedStyle(el).top, z: getComputedStyle(el).zIndex, ...box(el) }));
        const maxWidths = [...document.querySelectorAll('body *')].filter(el => { const mw = getComputedStyle(el).maxWidth; return mw !== 'none' && parseFloat(mw) < 1500 && el.getBoundingClientRect().width > 300; }).slice(0, 10)
          .map(el => ({ el: sel(el), max: getComputedStyle(el).maxWidth, padL: getComputedStyle(el).paddingLeft, padR: getComputedStyle(el).paddingRight, ...box(el) }));
        const grids = [...document.querySelectorAll('body *')].filter(el => { const s = getComputedStyle(el); return s.display.includes('grid') && s.gridTemplateColumns.split(' ').length > 1 && el.getBoundingClientRect().width > 300; }).slice(0, 8)
          .map(el => ({ el: sel(el), cols: getComputedStyle(el).gridTemplateColumns, colGap: getComputedStyle(el).columnGap, rowGap: getComputedStyle(el).rowGap, ...box(el) }));
        const main = document.querySelector('main') || document.querySelector('[role="main"], .main-content, #main-content')
          || [...document.body.children].filter(el => !['SCRIPT', 'STYLE', 'LINK', 'HEADER', 'A'].includes(el.tagName) && el.getBoundingClientRect().height > 400)[0];
        return {
          vw: innerWidth, docH: document.documentElement.scrollHeight,
          h1: h1 ? { text: h1.innerText.trim().slice(0, 80), font: getComputedStyle(h1).font, ...box(h1) } : null,
          fixed, maxWidths, grids,
          main: main ? { el: sel(main), ...box(main) } : { el: null, x: 0, y: 0, w: 0, h: 0 }
        };
      });
      out[`${key}@${vw}`] = r;
      await ctx.close();
      console.log(key, vw, 'docH', r.docH);
    }
  }
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1));
  console.log('layout.json:', Object.keys(out).length, 'entries');
  await b.close();
})();
