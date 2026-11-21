// Read computed styles and WPDS custom properties from public Washington Post pages.
// Headed Chrome. Does not submit forms or follow the sign-in wall past the page itself.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(here, '../../..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const PAGES = [
  ['home', 'https://www.washingtonpost.com/'],
  ['politics', 'https://www.washingtonpost.com/politics/'],
  ['opinions', 'https://www.washingtonpost.com/opinions/'],
  ['games', 'https://www.washingtonpost.com/games/'],
  ['subscribe', 'https://subscribe.washingtonpost.com/acquisition/?p=s_v&s_l=ONSITE_FOOTER_DIGITAL'],
  ['signin', 'https://www.washingtonpost.com/subscribe/signin/?next_url=https%3A%2F%2Fwww.washingtonpost.com%2F&itid=nav_sign_in'],
  ['accessibility', 'https://www.washingtonpost.com/accessibility/'],
  ['search', 'https://www.washingtonpost.com/search'],
];

const SPECS = [
  ['button-subscribe', 'a[data-qa="subs-offer"], a[data-testid*="subs-offer"]'],
  ['button-signin', 'a[href*="/subscribe/signin"]'],
  ['icon-button-search', 'button[aria-label="Search and browse sections"]'],
  ['icon-button-alerts', 'button[aria-label="News alerts"]'],
  ['link-section', 'nav a, header a[href*="washingtonpost.com/politics"]'],
  ['text-field-search', '#query, input[name="query"], input[type="search"], input[type="email"]'],
  ['logo', 'a[aria-label*="Washington Post"], a[href*="itid=masthead"]'],
  ['headline', 'h1, h2'],
  ['body', 'p'],
  ['card', 'article, [data-testid*="card"]'],
  ['footer-link', 'footer a'],
  ['tab', '[role=tab], button'],
];

function pick(spec) {
  return `(() => {
    const sel = ${JSON.stringify(spec)};
    const nodes = [...document.querySelectorAll(sel)].filter((el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 8 && r.height > 8 && s.visibility !== 'hidden' && s.display !== 'none' && r.top < innerHeight && r.bottom > 0;
    });
    return nodes[0] || null;
  })()`;
}

async function readEl(page, el) {
  return page.evaluate((node) => {
    if (!node) return null;
    const s = getComputedStyle(node);
    const r = node.getBoundingClientRect();
    return {
      tag: node.tagName,
      text: (node.innerText || node.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      color: s.color,
      backgroundColor: s.backgroundColor,
      borderTopColor: s.borderTopColor,
      borderTopWidth: s.borderTopWidth,
      borderRadius: s.borderRadius,
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing,
      padding: s.padding,
      boxShadow: s.boxShadow,
      textDecoration: s.textDecorationLine,
      outline: s.outline,
      transition: s.transition,
    };
  }, el);
}

const browser = await chromium.launch({ channel: 'chrome', headless: false });
const components = {};
const vars = { pages: {}, root: {} };

for (const [id, url] of PAGES) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' });
  const page = await ctx.newPage();
  console.log('measure', id);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await page.waitForTimeout(2500);
    if (id === 'home') {
      await page.getByRole('button', { name: /Search and browse sections/i }).first().click().catch(() => {});
      await page.waitForTimeout(600);
    }
    const rootVars = await page.evaluate(() => {
      const names = new Set();
      for (const sheet of document.styleSheets) {
        let rules;
        try { rules = sheet.cssRules; } catch { continue; }
        const walk = (list) => {
          if (!list) return;
          for (const r of list) {
            if (r.style) {
              for (let i = 0; i < r.style.length; i++) {
                const k = r.style[i];
                if (k.startsWith('--')) names.add(k);
              }
            }
            if (r.cssRules) walk(r.cssRules);
          }
        };
        walk(rules);
      }
      const cs = getComputedStyle(document.documentElement);
      const out = {};
      for (const n of names) {
        if (!/wpds|color|font|space|radius|shadow|gray|blue/i.test(n)) continue;
        const v = cs.getPropertyValue(n).trim();
        if (v) out[n] = v.slice(0, 180);
      }
      return {
        colorScheme: cs.colorScheme,
        background: cs.backgroundColor,
        color: cs.color,
        fontFamily: cs.fontFamily,
        count: names.size,
        sample: out,
      };
    });
    vars.pages[id] = { url: url.split('?')[0], ...rootVars, varCount: Object.keys(rootVars.sample).length };
    if (id === 'home') vars.root = rootVars.sample;

    for (const [name, sel] of SPECS) {
      if (components[name]?.default) continue;
      const handle = await page.evaluateHandle(pick(sel));
      const el = handle.asElement();
      if (!el) { await handle.dispose(); continue; }
      const def = await readEl(page, el);
      const row = { page: id, selector: sel, default: def };
      try {
        await el.hover();
        await page.waitForTimeout(200);
        row.hover = await readEl(page, el);
      } catch {}
      try {
        await el.focus();
        await page.waitForTimeout(150);
        row.focus = await readEl(page, el);
      } catch {}
      components[name] = row;
      await handle.dispose();
      console.log('  ', name, def && def.fontSize, def && def.color);
    }
  } catch (e) {
    vars.pages[id] = { error: String(e.message || e).split('\n')[0] };
    console.log('  FAIL', id, vars.pages[id].error);
  }
  await ctx.close();
}
await browser.close();

const measuredAt = new Date().toISOString();
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({ measuredAt, source: 'computed custom properties on documentElement, headed Chrome, public pages', ...vars }, null, 2));
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({ measuredAt, viewport: { width: 1440, height: 900 }, components }, null, 2));
console.log('vars', Object.keys(vars.root).length, 'components', Object.keys(components).length);
