// One-off: the /app/* scene gradient is a full-viewport painted layer that no
// other measured component covers. /app/sleep has been PerimeterX-blocked for
// a long stretch; the same SceneGradient paints on /app/meditate and
// /app/music, so this probe tries all three and writes the first real
// styleOf() record it gets into components-computed.json as `scene`.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, closePromo, isChallengeText, styleOf, RAW, UA_DESKTOP } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser } = await launch();
let context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
await patch(context);

const ROUTES = ['/app/meditate', '/app/music', '/app/sleep'];
const SEL = '[class*="SceneGradient" i], [class*="Scene" i]';
const deadline = Date.now() + 45 * 60 * 1000;

outer:
while (Date.now() < deadline) {
  for (const route of ROUTES) {
    const p = await context.newPage();
    try {
      await p.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(11000);
      const s = await p.evaluate(() => ({ title: document.title, body: (document.body && document.body.innerText) || '' })).catch(() => null);
      if (!s || isChallengeText(s) || s.body.trim().length < 40) {
        log('blocked', route, '- fresh context after 5 min quiet');
        await p.close().catch(() => {});
        await context.close().catch(() => {});
        await new Promise((r) => setTimeout(r, 300000));
        context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
        await patch(context);
        continue;
      }
      await closePromo(p).catch(() => {});
      const loc = p.locator(SEL).filter({ visible: true }).first();
      if (!(await loc.count())) { log('no scene node on', route); await p.close(); continue; }
      const rec = await styleOf(loc);
      rec.via = 'at rest';
      const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
      out.components ??= {};
      out.components.scene = {
        page: route === '/app/sleep' ? 'sleep' : route === '/app/meditate' ? 'meditate' : 'music',
        run: '2026-11-16',
        url: BASE + route,
        title: 'Scene canvas',
        group: 'App shell (dark)',
        desc: 'The full-viewport scene gradient the app shell paints behind everything (measured on ' + route + '; the same SceneGradient layer paints on all /app/* routes).',
        selector: 'scene gradient',
        states: { default: rec },
      };
      fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
      log('scene recorded from', route, JSON.stringify(rec.style.backgroundImage));
      break outer;
    } finally {
      await p.close().catch(() => {});
    }
  }
}
await browser.close().catch(() => {});
