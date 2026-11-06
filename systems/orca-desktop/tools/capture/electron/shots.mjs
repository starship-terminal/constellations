// Take every shot in product.mjs's SHOTS in the theme on screen, live over CDP, and measure each
// shot's parts there and then. Generic: the product's windows, shots and theme switch come from
// product.mjs.
//
//   PORT=9401 node tools/capture/electron/shots.mjs <theme> [name ...]     take shots (all, or the named)
//   PORT=9401 node tools/capture/electron/shots.mjs --set-theme="<label>"  switch the app's theme, print the old one
//                                                                  (only where product.mjs exports setTheme)
//
// Writes $RAW/<theme>/<name>.png (full colour, the window's own pixels) and merges into
// $RAW/<theme>/captures.json: { <name>: { window, state, file, viewport, parts: { <part>: { box, style } } } }.
// box is in screenshot pixels; style is the computed style (cdp.mjs PROPS) in the shot's state.
// RAW defaults to ~/.design-systems/<slug>/raw-shots, outside the repository; <slug> is this package's folder.
import { existsSync, readFileSync, rmSync } from 'node:fs';
import { basename, resolve as pathResolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { connect, disconnect, shoot, viewport, force, box, computed, tag, untagAll, writeJson } from './cdp.mjs';
import * as P from './product.mjs';

// The package folder this script lives in (systems/<slug>/tools/capture/electron/), so a copy in another
// package never writes into the package it was copied from.
const SLUG = process.env.SLUG || basename(pathResolve(fileURLToPath(import.meta.url), '../../../..'));
const RAW = process.env.RAW || `${process.env.HOME}/.design-systems/${SLUG}/raw-shots`;
const args = process.argv.slice(2);
const setTheme = args.find(a => a.startsWith('--set-theme='))?.slice(12);

const sessions = {};
async function session(win) {
  if (!sessions[win]) sessions[win] = await connect(P.WINDOWS[win]);
  return sessions[win];
}
const resolve = (page, spec) => typeof spec === 'function' ? spec(page)
  : Array.isArray(spec) ? page.locator(spec[0]).filter({ visible: true }).nth(spec[1]) : page.locator(spec).filter({ visible: true }).first();

if (setTheme) {
  // Only for a product whose theme is its own setting (product.mjs exports setTheme); a product whose theme
  // follows prefers-color-scheme is captured with SCHEME=light|dark instead (cdp.mjs).
  if (!P.setTheme) { console.error(`${P.NAME} has no setTheme in product.mjs; run with SCHEME=light or SCHEME=dark`); process.exit(2); }
  const s = await session(Object.keys(P.WINDOWS)[0]);
  console.log('theme was', await P.setTheme(s, setTheme));
  await disconnect(s.browser); process.exit(0);
}

const [theme, ...only] = args;
if (!theme) { console.error('usage: shots.mjs <theme> [name ...] | --set-theme=<label>'); process.exit(2); }
const out = `${RAW}/${theme}/captures.json`;
const all = existsSync(out) ? JSON.parse(readFileSync(out, 'utf8')) : {};
// failures: what a shot could not capture. A part the shot lists as optional (shot.optionalParts) or
// a whole optional shot (shot.optional) is reported but does not fail the run.
const failures = [], fatal = [];
const fail = (shot, msg, part) => {
  failures.push(`${shot.name}: ${msg}`);
  if (!shot.optional && !(part && (shot.optionalParts || []).includes(part))) fatal.push(`${shot.name}: ${msg}`);
};

for (const shot of P.SHOTS.filter(s => !only.length || only.includes(s.name))) {
  const h = await session(shot.window);
  const { page, cdp } = h;
  const undo = [];
  const before = P.guard ? await P.guard(h, shot.window) : '';
  try {
    await P.reset(h, shot.window);
    await shot.reveal(h);
    // Resolve and tag parts first, so forcing a state cannot move the locator to another element.
    const sel = {};
    for (const [name, spec] of Object.entries(shot.parts || {})) {
      const loc = resolve(page, spec);
      if (!(await loc.count()) || !(await loc.isVisible().catch(() => false))) { fail(shot, `${name} not found`, name); continue; }
      sel[name] = await tag(loc, `${shot.name}--${name}`);
    }
    // A real pointer over one part (hover), or real keyboard focus on one part (focus-visible:
    // a key press first, so Chromium's heuristic counts the focus as keyboard focus).
    if (shot.hover && sel[shot.hover]) { await page.locator(sel[shot.hover]).hover(); await page.waitForTimeout(500); }
    if (shot.focus && sel[shot.focus]) {
      if (P.prepareState) { await P.prepareState(page, sel[shot.focus], ['focus-visible'], true); undo.push(() => P.prepareState(page, sel[shot.focus], ['focus-visible'], false).catch(() => {})); }
      await page.keyboard.press('Shift'); await page.locator(sel[shot.focus]).focus(); await page.waitForTimeout(300);
    }
    for (const [name, states] of Object.entries(shot.force || {})) if (sel[name]) {
      if (P.prepareState) { await P.prepareState(page, sel[name], states, true); undo.push(() => P.prepareState(page, sel[name], states, false).catch(() => {})); }
      undo.push(await force(cdp, sel[name], states));
    }
    await page.waitForTimeout(400);
    const file = await shoot(cdp, `${RAW}/${theme}/${shot.name}.png`);
    const parts = {};
    for (const [name, s] of Object.entries(sel)) {
      // The tag is lost if the app re-rendered the element; fall back to the part's own selector.
      let loc = page.locator(s);
      if (!(await loc.count())) loc = resolve(page, shot.parts[name]);
      try { parts[name] = { box: await box(loc), style: await computed(loc) }; }
      catch (e) { fail(shot, `${name} not measured: ${e.message.split('\n')[0]}`, name); }
    }
    all[shot.name] = { window: shot.window, state: shot.state || 'default', file: file.split('/').slice(-2).join('/'), viewport: await viewport(page), parts };
    console.log(shot.name, Object.keys(parts).length, 'parts');
  } catch (e) {
    // A failed shot drops any entry an earlier run left under its name, so no stale reading survives.
    delete all[shot.name];
    // ... and its image from an earlier run, so quantize.py cannot publish a picture with no reading behind it.
    rmSync(`${RAW}/${theme}/${shot.name}.png`, { force: true });
    fail(shot, e.message.split('\n')[0]);
    console.error('FAILED', shot.name, e.message.split('\n')[0]);
  } finally {
    for (const u of undo) await u();
    await untagAll(page).catch(() => {});
    if (shot.after) await shot.after(h).catch(() => {});
  }
  // Look, don't act: stop at once if the shot changed what the product's guard watches.
  const now = P.guard ? await P.guard(h, shot.window) : '';
  if (now !== before) {
    writeJson(out, all);
    console.error(`STOPPED after ${shot.name}: state changed\n  before: ${before}\n  after:  ${now}`);
    process.exit(1);
  }
}
writeJson(out, all);
if (failures.length) { console.log('\nnot captured:'); failures.forEach(f => console.log('  ' + f)); }
for (const s of Object.values(sessions)) await disconnect(s.browser);
if (fatal.length) { console.error(`\n${fatal.length} required part(s) or shot(s) not captured`); process.exit(1); }
