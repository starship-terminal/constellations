// Captures hume.ai's signed-out public surfaces into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// www.hume.ai paints one light theme and has no control — every www shot is
// `*-light-*`, the only theme the product has (verified: .dark class and a
// dark colour-scheme emulation leave the painted surface unchanged, zero
// dark rules in its sheets). dev.hume.ai is the one surface with a real
// theme control: the header Theme button's own Light / Dark / System menu
// repaints html.dark — the docs' `*-dark-*` shots are painted through it
// and Light is restored after. demo.hume.ai (the invitation gate) and
// app.hume.ai (/log-in) are light-only too.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots
// 1x. A page taller than one GPU texture is saved as name.partN.png tiles,
// which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary. Nothing is sent, bought,
// typed, searched or signed into: the only presses are local UI toggles —
// the docs Theme menu items, the home player transport (Play/Pause/Stop is
// a scripted sample-call player, pressed for the playing state and
// stopped after), the benchmark category tabs and the mobile "Open menu"
// drawer. The contact form, newsletter Subscribe and log-in form are
// captured at rest — never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, paintedTheme, themeSupported, chromium, UA, UA_MOBILE, BASE, DOCS, DEMO, APP } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// The www pages scroll the document; dev.hume.ai's article scrolls inside
// its own overflow pane. findScroller() picks the pane with the most
// scrollable content and falls back to the document. lazyScroll walks it
// so lazy sections paint before the shot.
async function findScroller(p) {
  for (let tries = 0; tries < 10; tries++) {
    const info = await p.evaluate(() => {
      let sc = null, best = 0;
      for (const el of document.querySelectorAll('div,main,section,article')) {
        const cs = getComputedStyle(el);
        if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > best) { best = el.scrollHeight; sc = el; }
      }
      if (sc) sc.setAttribute('data-fp-scroller', '1');
      return {
        h: sc ? sc.scrollHeight : Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        inner: !!sc,
        docH: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        vh: window.innerHeight,
      };
    });
    if (info.inner || info.docH > info.vh + 50 || tries === 9) return info;
    await wait(p, 800);
  }
}

async function lazyScroll(p) {
  const info = await findScroller(p);
  if (info.inner) {
    for (let y = 0; y < info.h; y += 700) { await p.evaluate((y) => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = y; }, y); await wait(p, 180); }
    await p.evaluate(() => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = 0; });
  } else {
    for (let y = 0; y < info.h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
    await p.evaluate(() => scrollTo(0, 0));
  }
  await wait(p, 900);
}

// For the full shot the article pane's ancestors are relaxed to natural
// height so the document itself becomes as tall as the article — a normal
// fullPage capture then paints every section, header still fixed at top.
// restoreShell() puts the shell back so later shots see the real layout.
async function expandScroller(p) {
  return p.evaluate(() => {
    const sc = document.querySelector('[data-fp-scroller]');
    if (!sc) return null;
    for (let el = sc; el && el !== document.documentElement; el = el.parentElement) {
      el.setAttribute('data-fp-expand', '1');
      // flex:none relaxes height but also drops the flex-basis width, letting
      // the pane grow wider than the viewport — pin the measured border-box
      // width so the full-page shot keeps the real layout.
      const w = el.getBoundingClientRect().width;
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
      el.style.setProperty('flex', 'none', 'important');
      el.style.setProperty('box-sizing', 'border-box', 'important');
      el.style.setProperty('width', `${w}px`, 'important');
    }
    for (const el of [document.body, document.documentElement]) {
      el.setAttribute('data-fp-expand', '1');
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
    }
    return true;
  });
}
async function restoreShell(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('[data-fp-expand]')) {
      for (const prop of ['height', 'max-height', 'min-height', 'overflow', 'flex', 'box-sizing', 'width']) el.style.removeProperty(prop);
      el.removeAttribute('data-fp-expand');
    }
    const sc = document.querySelector('[data-fp-scroller]');
    if (sc) { sc.removeAttribute('data-fp-scroller'); sc.scrollTop = 0; }
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full', maxChunks = 8) {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await expandScroller(p);
    await wait(p, 1200);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    // The bound is in CSS pixels: scale:'css' clips are CSS px and the
    // documented bound describes page coverage — dividing by dpr would
    // halve mobile coverage. A @2x tile's PNG is 28k device px tall; still
    // well inside what the stitcher handles.
    const chunk = 14000;
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and
    // record the boundary instead.
    const MAXH = maxChunks * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    const plan = { intendedHeight: hCap, pageHeight: H, chunk, parts: hCap <= chunk ? 0 : Math.ceil(hCap / chunk), scale: 'css' };
    const shootTiles = async (extra = {}) => {
      // Written at the start of every attempt (a retry after dropPartials()
      // has to leave one too) so quantize.py can prove the stitched set is
      // whole — a mid-loop failure must never publish a truncated sheet.
      fs.writeFileSync(`${f}.plan.json`, JSON.stringify(plan, null, 1) + '\n');
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, ...extra }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, ...extra }, this.requested);
    };
    const dropPartials = () => {
      // A tile loop that dies mid-run leaves parts 0..k of n — the stitcher
      // would publish a truncated sheet as a full page. Remove every tile so
      // quantize.py has nothing partial to stitch.
      for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.plan.json`)) fs.unlinkSync(`${RAW}/${old}`);
    };
    try {
      try {
        await shootTiles();
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        dropPartials();
        try {
          await shootTiles({ animations: 'disabled' });
        } catch (e2) {
          dropPartials();
          throw e2;
        }
      }
    } finally {
      await restoreShell(p).catch(() => {});
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Dark shots on the docs surface: the header's own Theme menu (Dark item),
// the painted surface verified by setTheme, shot, then Light restored.
async function darkPass(p, name, vw, vh, dpr, url, shots = ['default']) {
  if (!(await setTheme(p, 'dark'))) { log('  ! dark theme never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };
const BOTH_DARK = (name, url) => async (p, S, ctx) => { await BOTH(p, S); ctx.extra += await darkPass(p, name, 1440, 900, 1, url, ['default']); };

// www.hume.ai — every shot is `*-light-*`: the only theme the surface has.
const desktop = {
  home: { url: BASE + '/', wait: 8000, prefix: 'home-light', run: async (p, S) => {
    await S.view('default');
    // The home player's own transport: Play starts the scripted sample
    // call (a media control, not a submission), Stop ends it. Shot while
    // it runs when the controls mount.
    await step('playing', async () => {
      const play = p.locator('button[aria-label="Play"], button[aria-label="Pause"], button[aria-label="Stop"]').first();
      if (!(await play.count())) { log('  ! player transport not mounted'); return; }
      await play.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 600);
      await play.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 2500);
      await S.view('playing');
      const stop = p.locator('button[aria-label="Stop"]').first();
      if (await stop.count()) await stop.click({ timeout: 3000 }).catch(() => {});
      else await play.click({ timeout: 3000 }).catch(() => {});
      await wait(p, 500);
      await p.evaluate(() => scrollTo(0, 0));
    });
    // A benchmark-category tab's own activation, when it mounts on home.
    await step('benchmark-tab', async () => {
      const tab = p.locator('button, [role="tab"]').filter({ hasText: /reliability|voice naturalness/i }).first();
      if (!(await tab.count())) { log('  ! benchmark tabs not mounted'); return; }
      await tab.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 500);
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('benchmark-tab');
      await p.evaluate(() => scrollTo(0, 0));
    });
    await S.full();
  } },
  'emotion-science': { url: BASE + '/emotion-science', wait: 7000, prefix: 'emotion-science-light', run: BOTH },
  'decision-model': { url: BASE + '/products/decision-model-api', wait: 7000, prefix: 'decision-model-light', run: BOTH },
  'expression-apis': { url: BASE + '/products/expression-apis', wait: 7000, prefix: 'expression-apis-light', run: BOTH },
  'human-feedback': { url: BASE + '/products/human-feedback', wait: 7000, prefix: 'human-feedback-light', run: BOTH },
  'user-testing': { url: BASE + '/products/user-testing', wait: 7000, prefix: 'user-testing-light', run: BOTH },
  'speech-data': { url: BASE + '/products/speech-data', wait: 7000, prefix: 'speech-data-light', run: BOTH },
  prism: { url: BASE + '/products/prism', wait: 7000, prefix: 'prism-light', run: BOTH },
  voiceeq: { url: BASE + '/products/voiceeq-platform', wait: 7000, prefix: 'voiceeq-light', run: BOTH },
  'develop-models': { url: BASE + '/solutions/develop-voice-models', wait: 7000, prefix: 'develop-models-light', run: BOTH },
  'deploy-agents': { url: BASE + '/solutions/deploy-voice-agents', wait: 7000, prefix: 'deploy-agents-light', run: BOTH },
  benchmark: { url: BASE + '/benchmark', wait: 7000, prefix: 'benchmark-light', run: async (p, S) => {
    await S.view('default');
    await step('category-tab', async () => {
      const tab = p.locator('[role="tab"]').filter({ hasText: /reliability|overall|expressiveness/i }).first();
      if (!(await tab.count())) { log('  ! benchmark tabs not mounted'); return; }
      await tab.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 500);
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('category-tab');
    });
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 8000, prefix: 'blog-light', run: async (p, S) => {
    await S.view('default');
    await step('category-filter', async () => {
      const f = p.locator('button, a').filter({ hasText: /^Research$/i }).first();
      if (!(await f.count())) { log('  ! blog filters not mounted'); return; }
      await f.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('category-filter');
      const all = p.locator('button, a').filter({ hasText: /^All$/i }).first();
      if (await all.count()) await all.click({ timeout: 3000 }).catch(() => {});
    });
    await S.full();
  } },
  'blog-post': { url: BASE + '/blog/hume-audio-decision-benchmarks', wait: 7000, prefix: 'blog-post-light', run: BOTH },
  publications: { url: BASE + '/publications', wait: 7000, prefix: 'publications-light', run: BOTH },
  about: { url: BASE + '/about', wait: 7000, prefix: 'about-light', run: BOTH },
  careers: { url: BASE + '/careers', wait: 7000, prefix: 'careers-light', run: BOTH },
  'contact-form': { url: BASE + '/contact-form', wait: 7000, prefix: 'contact-form-light', run: async (p, S) => {
    await S.view('default');
    // The form focused: the first field is clicked into — never typed,
    // never submitted.
    await step('field-focused', async () => {
      const f = p.locator('input, select, textarea').filter({ visible: true }).first();
      if (!(await f.count())) { log('  ! no form field mounted'); return; }
      await f.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 600);
      await S.view('field-focused');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  'privacy-policy': { url: BASE + '/privacy-policy', wait: 6000, prefix: 'privacy-policy-light', run: BOTH },
  'terms-of-use': { url: BASE + '/terms-of-use', wait: 6000, prefix: 'terms-of-use-light', run: BOTH },
  explore: { url: BASE + '/explore/speech-prosody-model', wait: 9000, prefix: 'explore-light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  notfound: { url: BASE + '/this-page-does-not-exist', wait: 6000, prefix: 'notfound-light', run: async (p, S) => {
    // /products redirects to / — documented, not a 404 surface. A stray
    // path is probed for the real not-found page: the spec URL is the stray
    // path itself so the sidecars cite what was actually captured.
    await wait(p, 5000);
    await S.view('default');
    await S.full();
  } },
};

// dev.hume.ai — the docs. Light is the painted default; `dark` shots are
// the header Theme menu's own Dark press, verified and restored.
const docs = {
  'docs-overview': { url: DOCS + '/audio-decisions/docs/overview', wait: 8000, prefix: 'docs-overview-light', dark: 'docs-overview', run: BOTH_DARK('docs-overview', DOCS + '/audio-decisions/docs/overview') },
  'docs-quickstart': { url: DOCS + '/audio-decisions/docs/quickstart/python', wait: 7000, prefix: 'docs-quickstart-light', dark: 'docs-quickstart', run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await darkPass(p, 'docs-quickstart', 1440, 900, 1, DOCS + '/audio-decisions/docs/quickstart/python', ['default']);
  } },
  'docs-reference': { url: DOCS + '/audio-decisions/reference/decisions/create', wait: 7000, prefix: 'docs-reference-light', dark: 'docs-reference', run: async (p, S, ctx) => {
    await S.view('default');
    // The API playground's request editor is a form the docs render; it is
    // measured and shot at rest — Send is never pressed.
    await S.full('full', 4);
    ctx.extra += await darkPass(p, 'docs-reference', 1440, 900, 1, DOCS + '/audio-decisions/reference/decisions/create', ['default', 'full']);
  } },
  'docs-changelog': { url: DOCS + '/audio-decisions/changelog', wait: 7000, prefix: 'docs-changelog-light', dark: 'docs-changelog', run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await darkPass(p, 'docs-changelog', 1440, 900, 1, DOCS + '/audio-decisions/changelog', ['default']);
  } },
};

// demo.hume.ai — the invitation gate (the playground itself is a documented
// boundary). app.hume.ai/log-in — the public sign-in surface, never entered.
const gated = {
  'demo-gate': { url: DEMO + '/decision-model/file', wait: 8000, prefix: 'demo-gate-light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { url: APP + '/log-in', wait: 8000, prefix: 'login-light', run: async (p, S) => {
    await S.view('default');
    await step('field-focused', async () => {
      const f = p.locator('input[type="email"], input').filter({ visible: true }).first();
      if (!(await f.count())) { log('  ! log-in fields not mounted'); return; }
      await f.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 600);
      await S.view('field-focused');
      await p.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
    });
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, prefix: 'mobile-home-light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const menu = p.locator('button[aria-label="Open menu"]').first();
      if (!(await menu.count())) { log('  ! mobile menu button absent'); return; }
      await menu.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
      const close = p.locator('button').filter({ hasText: /close menu|close/i }).first();
      if (await close.count()) await close.click({ timeout: 2000 }).catch(() => {});
      await wait(p, 500);
    });
    await S.full();
  } },
  benchmark: { url: BASE + '/benchmark', wait: 7000, prefix: 'mobile-benchmark-light', run: BOTH },
  blog: { url: BASE + '/blog', wait: 8000, prefix: 'mobile-blog-light', run: BOTH },
  'contact-form': { url: BASE + '/contact-form', wait: 7000, prefix: 'mobile-contact-form-light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-overview': { url: DOCS + '/audio-decisions/docs/overview', wait: 8000, prefix: 'mobile-docs-overview-light', run: async (p, S, ctx) => {
    await S.view('default');
    await step('drawer', async () => {
      const menu = p.locator('button[aria-label="Open menu"]').first();
      if (!(await menu.count())) { log('  ! docs mobile menu absent'); return; }
      await menu.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full('full', 3);
    ctx.extra += await darkPass(p, 'mobile-docs-overview', 390, 844, 2, DOCS + '/audio-decisions/docs/overview', ['default']);
  } },
  'demo-gate': { url: DEMO + '/decision-model/file', wait: 8000, prefix: 'mobile-demo-gate-light', run: async (p, S) => { await S.view('default'); } },
  login: { url: APP + '/log-in', wait: 8000, prefix: 'mobile-login-light', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, dict: desktop })),
  ...Object.keys(docs).map((k) => ({ k, mob: false, dict: docs })),
  ...Object.keys(gated).map((k) => ({ k, mob: false, dict: gated })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, dict: mobile })),
];
for (const { k, mob, dict } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(k) && !pageArg.includes(name)) continue;
  const spec = dict[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, spec.prefix, vw, vh, dpr, spec.url);
  const runCtx = { extra: 0 };
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 8000);
    await spec.run(p, S, runCtx);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count + runCtx.extra;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
