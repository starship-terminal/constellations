// One-shot DOM recon for kitchen.co. Writes ~/.design-systems/kitchen/recon.json.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium, UA, BASE, hideConsent } from './lib.mjs';

const OUT = path.join(os.homedir(), '.design-systems', 'kitchen', 'recon.json');
const pages = (process.argv[2] || 'home,pricing,login,get-started,blog,features').split(',');
const URLS = {
  home: '/', features: '/features', pricing: '/pricing', buy: '/buy', reviews: '/reviews',
  tutorials: '/tutorials', integrations: '/integrations', 'how-it-works': '/how-it-works',
  about: '/about', blog: '/blog', login: '/login', 'get-started': '/get-started',
  'get-demo': '/get-demo',
};

const browser = await chromium.launch();
const out = {};
for (const key of pages) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  const url = BASE + (URLS[key] || key);
  console.log('open', url);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(1800);
    await hideConsent(page);
    out[key] = await page.evaluate(() => {
      const vis = (el) => {
        const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el);
        return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0;
      };
      const brief = (el) => {
        const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el);
        return {
          tag: el.tagName.toLowerCase(),
          cls: [...el.classList].slice(0, 5).join('.'),
          text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 70),
          w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y),
          bg: cs.backgroundColor, color: cs.color, fs: cs.fontSize, fw: cs.fontWeight,
          ff: cs.fontFamily.split(',')[0], radius: cs.borderTopLeftRadius, pad: cs.padding,
          border: cs.borderTopWidth + ' ' + cs.borderTopStyle + ' ' + cs.borderTopColor,
          shadow: cs.boxShadow === 'none' ? '' : cs.boxShadow.slice(0, 80),
          href: el.getAttribute('href') || '',
          type: el.getAttribute('type') || '',
          name: el.getAttribute('name') || '',
        };
      };
      const pick = (sel, n = 8) => [...document.querySelectorAll(sel)].filter(vis).slice(0, n).map(brief);
      const sheets = [...document.styleSheets].map((s) => {
        let rules = 0, err = '';
        try { rules = s.cssRules ? s.cssRules.length : 0; } catch (e) { err = String(e).slice(0, 80); }
        return { href: s.href, rules, err };
      });
      const props = [];
      for (const s of document.styleSheets) {
        let rules;
        try { rules = [...s.cssRules]; } catch { continue; }
        const walk = (list) => {
          for (const r of list) {
            if (r.cssRules && !r.style) walk([...r.cssRules]);
            if (!r.style) continue;
            for (let i = 0; i < r.style.length; i++) {
              const k = r.style[i];
              if (k && k.startsWith('--')) props.push([r.selectorText, k, r.style.getPropertyValue(k).trim()]);
            }
          }
        };
        walk(rules);
      }
      return {
        title: document.title,
        url: location.href,
        inner: [innerWidth, innerHeight],
        scrollH: document.documentElement.scrollHeight,
        body: brief(document.body),
        h1: pick('h1', 2),
        buttons: pick('a.btn, button, .btn', 12),
        inputs: pick('input, textarea, select', 12),
        nav: pick('header a, .nav a, .header__actions a', 16),
        cards: pick('.card, .pricing__item, .plan, .feature, article, .tile, .box', 6),
        footer: pick('footer, .footer', 1),
        dialogs: pick('[role=dialog], .modal, .popup', 4),
        sheets,
        customProps: props.slice(0, 40),
        fonts: [...document.fonts].slice(0, 20).map((f) => f.family + ' ' + f.weight + ' ' + f.status),
      };
    });
    console.log(' ', key, out[key].title, 'scroll', out[key].scrollH, 'btns', out[key].buttons.length, 'inputs', out[key].inputs.length);
  } catch (e) {
    console.log(' FAIL', key, e.message.split('\n')[0]);
    out[key] = { error: e.message.split('\n')[0] };
  }
  await ctx.close();
}
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(out, null, 1));
console.log('wrote', OUT);
await browser.close();
