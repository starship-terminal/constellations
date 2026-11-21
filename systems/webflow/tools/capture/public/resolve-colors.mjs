// Resolves semantic colour vars to computed sRGB on a real page, light and dark.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE } from './lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const browser = await chromium.launch({ headless: true });
const out = {};
for (const theme of ['light', 'dark']) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript((theme) => {
    if (theme === 'dark') try { localStorage.setItem('darkMode', 'true'); } catch { /* ignore */ }
  }, theme);
  const page = await ctx.newPage();
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1200);
  if (theme === 'dark') await page.evaluate(() => document.documentElement.classList.add('u-mode-dark'));
  out[theme] = await page.evaluate(() => {
    const cs = getComputedStyle(document.documentElement);
    const names = [];
    for (const s of document.styleSheets) {
      let rules; try { rules = [...s.cssRules]; } catch { continue; }
      const walk = (list) => { for (const r of list) { if (r.style) for (const p of r.style) if (p.startsWith('--')) names.push(p); if (r.cssRules) walk([...r.cssRules]); } };
      walk(rules);
    }
    const unique = [...new Set(names)];
    const probe = document.createElement('div');
    document.body.appendChild(probe);
    const computed = {};
    for (const n of unique) {
      const raw = cs.getPropertyValue(n).trim();
      if (!raw) continue;
      if (/color|background|text|border|accent|blue|white|black|gray|green|red|pink|purple|orange|yellow/i.test(n) && !/font|size|weight|spacing|margin|padding|radius|height|width/i.test(n)) {
        probe.style.color = 'transparent';
        probe.style.color = `var(${n})`;
        computed[n] = { raw: raw.slice(0, 180), computed: getComputedStyle(probe).color };
      }
    }
    const body = getComputedStyle(document.body);
    const link = document.querySelector('a');
    const btn = document.querySelector('a.button, a.btn, .button, .w-button, a[class*="button"]');
    return {
      computed,
      paint: {
        bodyBg: body.backgroundColor,
        bodyColor: body.color,
        scheme: getComputedStyle(document.documentElement).colorScheme,
        className: document.documentElement.className,
        linkColor: link ? getComputedStyle(link).color : null,
        buttonBg: btn ? getComputedStyle(btn).backgroundColor : null,
        buttonColor: btn ? getComputedStyle(btn).color : null,
        buttonRadius: btn ? getComputedStyle(btn).borderRadius : null,
        buttonHeight: btn ? Math.round(btn.getBoundingClientRect().height) : null,
      },
    };
  });
  await ctx.close();
}
fs.writeFileSync(path.join(REF, 'raw', 'computed-colors.json'), JSON.stringify(out, null, 1) + '\n');
console.log('light', Object.keys(out.light.computed).length, 'dark', Object.keys(out.dark.computed).length);
console.log(out.light.paint, out.dark.paint);
await browser.close();
