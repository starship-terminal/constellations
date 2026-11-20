// Reads the product's motion into raw/motion.json: durations, easing curves, which properties transition,
// animation and @keyframes names, motion custom properties, and what prefers-reduced-motion: reduce
// changes. Serves both web routes (docs/decisions/0001-motion-tokens.md, docs/CAPTURE.md#motion).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/motion-probe.mjs
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/motion-probe.mjs --urls <url>[,<url>...]
//
// Signed-in route: every copy under SNAPS is opened the way layout.mjs opens it. Public route: each URL is
// opened in a plain headless context. Each page is read twice in the same session, on the same elements:
// once with page.emulateMedia({ reducedMotion: 'no-preference' }), once with 'reduce'. The page's own
// matchMedia answer is recorded for both, so a pass that did not take is visible. Nothing is clicked,
// typed or submitted; computed transitions are read at rest, and the stylesheets' own rules (hover and
// state rules included) are read from the CSSOM.
//
// The output is raw readings, not tokens: build_tokens.py turns them into the motion group
// (tools/kit/build/motion.py). Elements with the same motion share one group, so the file stays small.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { MOTION_PROPS, MOTION_VAR_NAME, MOTION_VAR_VALUE, motionOf, groupRecords, summarise, mergeSummaries, declaredOf, readMotionInPage, readSheetsInPage } from './motion.mjs';
import { safeUrl } from './safe-url.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');              // systems/<slug>, from tools/capture
const OUT = process.env.OUT_JSON || path.join(REF, 'raw', 'motion.json');
const SNAPS = process.env.SNAPS ? path.resolve(process.env.SNAPS) : null;
const urlsArg = process.argv.indexOf('--urls');
const URLS = urlsArg > 0 ? (process.argv[urlsArg + 1] || '').split(',').filter(Boolean) : [];
if (!SNAPS && !URLS.length) { console.error('SNAPS=<dir of page copies>, or --urls <url>[,<url>...], is required'); process.exit(2); }
const CAP = Number(process.env.MOTION_CAP) || 6000;   // moving elements kept per pass
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

// PRODUCT (adapt): anything a public page needs before it shows its real UI (a promo dialog, a cookie
// banner), pressed the way public.mjs presses it. Never press anything that sends or submits.
// headspace.com mounts the OneTrust consent bar (#onetrust-banner-sdk) over the
// viewport bottom; it is hidden, never answered — the same REMOVE-ONLY hide
// public.mjs's closePromo does.
async function prepare(page) {
  await page.waitForTimeout(3000);
  await page.evaluate(() => {
    document.querySelectorAll('div[id*="onetrust" i], div[class*="onetrust" i], iframe[title*="privacy" i]').forEach((x) => x.style.setProperty('display', 'none', 'important'));
  });
}

// One page, both passes. Returns the record for raw/motion.json.
async function readPage(page, label, url) {
  const arg = { props: MOTION_PROPS, cap: CAP, pseudos: ['::before', '::after'] };
  await page.evaluate(() => { delete window.__motion; });
  await page.emulateMedia({ reducedMotion: 'no-preference' });
  await page.waitForTimeout(400);
  const normal = await page.evaluate(readMotionInPage, arg);
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.waitForTimeout(400);                       // a transition or animation restyles on the next frame
  const reduced = await page.evaluate(readMotionInPage, arg);
  await page.emulateMedia({ reducedMotion: 'no-preference' });
  const sheets = await page.evaluate(readSheetsInPage, { varName: MOTION_VAR_NAME, varValue: MOTION_VAR_VALUE, cap: 400 });

  const after = new Map(reduced.records.map((r) => [r.id, r]));
  const records = normal.records.map((r) => ({ node: r.node, base: motionOf(r.style), reduced: motionOf(after.get(r.id)?.style || {}) }));
  // an element that moves only under reduce (it was not moving in the normal pass)
  const known = new Set(normal.records.map((r) => r.id));
  for (const r of reduced.records) if (!known.has(r.id)) records.push({ node: r.node, base: motionOf({}), reduced: motionOf(r.style) });
  const groups = groupRecords(records);
  const page_ = {
    url: url && safeUrl(url),
    matchMedia: { normal: normal.matches, reduce: reduced.matches },
    scanned: normal.scanned,
    // moving elements left out because the cap was reached; they are in neither pass, so none is read as stopped
    capped: normal.dropped + reduced.dropped > 0 ? { cap: CAP, droppedNormal: normal.dropped, droppedReduced: reduced.dropped } : false,
    unreadableSheets: sheets.unreadable,
    sheetsTruncated: sheets.truncated,
    summary: summarise(groups),
    groups,
    keyframes: sheets.keyframes,
    reducedMotionRules: sheets.reducedRules,
    declared: sheets.declared.map(declaredOf).filter((d) => d.transitions.length || d.animations.length || d.scrollBehavior || d.viaVar),
    customProperties: sheets.customProperties,
  };
  if (page_.capped) log('  ! more than', CAP, 'moving elements on', label, '; the rest were not read');
  if (Object.values(sheets.truncated).some(Boolean)) log('  ! a stylesheet list was cut at 400 entries on', label, JSON.stringify(sheets.truncated));
  if (!page_.matchMedia.reduce || page_.matchMedia.normal) log('  ! the emulation did not take on', label, JSON.stringify(page_.matchMedia));
  log(label, `${normal.records.length} moving, ${groups.length} groups, reduce: ${page_.summary.behaviour}`);
  return page_;
}

const browser = await chromium.launch();
const pages = {};
try {
  if (SNAPS) {
    // The signed-in route's own opener (lib.mjs reads SNAPS when it loads, so import it after the check).
    const lib = await import('./signed-in/lib.mjs');
    const labels = fs.readdirSync(SNAPS).filter((f) => f.endsWith('.json')).map((f) => f.slice(0, -5)).filter((l) => fs.existsSync(path.join(SNAPS, `${l}.html`))).sort();
    for (const label of labels) {
      const meta = lib.metaOf(label);
      const ctx = await lib.newContext(browser, meta);
      try {
        const page = await lib.openSnap(ctx, label);
        pages[`${label}@${meta.w}`] = await readPage(page, label, meta.url);   // a copy's label is unique in SNAPS
      } catch (e) { log('failed', label, String(e.message).split('\n')[0]); }
      await ctx.close();
    }
  } else {
    for (const [i, url] of URLS.entries()) {
      const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' });
      const page = await ctx.newPage();
      try {
        await page.goto(url, { waitUntil: 'load', timeout: 90000 });
        await prepare(page);
        // keyed by run position: two URLs can share one sanitised form (/view?tab=one and ?tab=two); the record keeps it
        pages[`page-${i + 1}`] = await readPage(page, `page-${i + 1}`, url);
      } catch (e) { log('failed', safeUrl(url), String(e.message).split('\n')[0]); }
      await ctx.close();
    }
  }
} finally {
  await browser.close();
}

// Nothing captured is a failed run, not a finding that nothing moves: keep the earlier raw/motion.json.
if (!Object.keys(pages).length) { console.error('no page was captured; raw/motion.json was not written'); process.exit(1); }

const out = {
  _meta: {
    readAt: new Date().toLocaleDateString('en-CA'),     // the local date of the run
    probe: "page.emulateMedia({ reducedMotion }): 'no-preference' then 'reduce', same elements, same page",
    source: SNAPS ? 'static signed-in page copies (stylesheets inlined), rendered headless' : 'public pages, headless Chromium, read at rest',
    notes: 'Computed transitions and animations are read at rest; rules in :hover and other state selectors appear under `declared`. Outcome per element: removed (every transition and animation ends at or under 1 ms), reduced, kept, partial.',
  },
  summary: mergeSummaries(Object.values(pages).map((p) => p.summary)),
  pages,
};
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('raw/motion.json', Object.keys(pages).length, 'pages;', 'reduced motion:', out.summary.behaviour);
