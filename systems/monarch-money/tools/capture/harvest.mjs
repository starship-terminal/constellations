// Harvest Monarch Money public CSS custom properties, font faces and radii.
// Writes raw/css-vars.json. (It never wrote the raw/survey.json its header promised.)
// Never clicks Sign up, Sign in, OAuth, checkout, or a consent button.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, APP, open, hideConsent, RAW } from './public/lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
});
const page = await context.newPage();

async function readSheets() {
  return page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string'
      ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
      : v);
    const blocks = [];
    const fonts = [];
    const keyframes = [];
    let ruleCount = 0;
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const href = (sheet.href || 'inline').split('/').pop();
      const walk = (list, media) => {
        for (const r of list) {
          ruleCount++;
          // Any grouping rule (@media, @layer, @supports, @container) holds rules to walk; only
          // @media used to be, so tokens inside @layer or @supports were skipped silently.
          if (r.cssRules && !r.style && r.type !== CSSRule.KEYFRAMES_RULE) walk(r.cssRules, r.conditionText || media);
          else if (r.type === CSSRule.FONT_FACE_RULE) {
            fonts.push(noUrl(r.cssText).slice(0, 280));
          } else if (r.type === CSSRule.KEYFRAMES_RULE) {
            keyframes.push(r.name);
          } else if (r.style) {
            const props = {};
            for (let i = 0; i < r.style.length; i++) {
              const n = r.style[i];
              if (n.startsWith('--') && !n.startsWith('--osano') && !n.startsWith('--tw-')) {
                props[n] = noUrl(r.style.getPropertyValue(n).trim());
              }
            }
            if (Object.keys(props).length && /:root|html/.test(r.selectorText || '')) {
              blocks.push({
                href,
                selector: (r.selectorText || '').slice(0, 180),
                media: media || '',
                properties: props,
              });
            }
          }
        }
      };
      walk(rules, '');
    }
    const names = new Set();
    for (const b of blocks) for (const n of Object.keys(b.properties)) names.add(n);
    const cs = getComputedStyle(document.documentElement);
    const resolved = {};
    for (const n of names) {
      const v = cs.getPropertyValue(n).trim();
      if (v) resolved[n] = noUrl(v).slice(0, 400);
    }
    return {
      ruleCount,
      blocks,
      fonts: [...new Set(fonts)],
      keyframes: [...new Set(keyframes)],
      resolved,
      brand: document.documentElement.getAttribute('data-brand'),
      colorScheme: cs.colorScheme,
    };
  });
}

log('open home');
await open(page, BASE + '/', { wait: 2500 });
const home = await readSheets();
log('home vars', Object.keys(home.resolved).length, 'blocks', home.blocks.length, 'fonts', home.fonts.length);

log('open login');
await open(page, APP + '/login', { wait: 2500 });
const login = await readSheets();
log('login vars', Object.keys(login.resolved).length);

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'www.monarch.com and app.monarch.com/login, computed :root custom properties, headless Chromium, 1440x900, light. Osano hidden, never answered. No sign-up, no OAuth, no bank link.',
  viewport: { width: 1440, height: 900 },
  home,
  login: {
    resolved: login.resolved,
    blocks: login.blocks.filter((b) => !/osano/.test(b.selector)),
    fonts: login.fonts,
    brand: login.brand,
    colorScheme: login.colorScheme,
  },
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote css-vars.json');

await browser.close();
