// Capture an agent run: the states only a sent prompt shows (streaming, a tool call in progress, an
// approval prompt, the finished reply). Uses product.mjs's RUN; generic otherwise.
//
//   PORT=9401 node tools/capture/electron/run.mjs <theme>
//
// The owner approved test prompts on 2026-10-25, in a fresh chat on an empty scratch folder only.
// Each step sends one prompt, then screenshots the window every INTERVAL ms until the product's
// `done` says the run finished (or TIMEOUT), and records the parts RUN.parts finds on screen at each
// frame; once done, it waits SETTLE ms and takes one more frame, `<step>-done`. Frames go to $RAW/<theme>/run/; the step's `approve` decides whether an approval prompt may
// be accepted (only for actions inside the scratch folder).
import { rmSync } from 'node:fs';
import { basename, resolve as pathResolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { connect, disconnect, shoot, viewport, box, computed, writeJson } from './cdp.mjs';
import * as P from './product.mjs';

// The package folder this script lives in (systems/<slug>/tools/capture/electron/), so a copy in another
// package never writes into the package it was copied from.
const SLUG = process.env.SLUG || basename(pathResolve(fileURLToPath(import.meta.url), '../../../..'));
const RAW = process.env.RAW || `${process.env.HOME}/.design-systems/${SLUG}/raw-shots`;
const INTERVAL = +(process.env.INTERVAL || 1500), TIMEOUT = +(process.env.TIMEOUT || 120000), SETTLE = +(process.env.SETTLE || 1500);
const theme = process.argv[2];
// The theme names a folder that is emptied below, so it must be a plain theme name (`dark`, `light-more`),
// never a path such as `../..`.
if (!/^(dark|light)(-[a-z0-9]+)*$/.test(theme || '')) { console.error('usage: run.mjs <dark|light>[-<suffix>]'); process.exit(2); }
const out = `${RAW}/${theme}/run/frames.json`;
// A run starts from an empty folder, so no frame of an earlier, longer run survives into this one.
rmSync(`${RAW}/${theme}/run`, { recursive: true, force: true });
const all = {};
const h = await connect(P.WINDOWS[P.RUN.window]);
const { page, cdp } = h;

async function measure() {
  const parts = {};
  for (const [name, spec] of Object.entries(P.RUN.parts)) {
    const loc = (typeof spec === 'function' ? spec(page) : page.locator(spec).filter({ visible: true })).last();
    if (!(await loc.count().catch(() => 0))) continue;
    try { parts[name] = { box: await box(loc), style: await computed(loc) }; } catch {}
  }
  return parts;
}
// Every named component on screen (data-component, data-slot, role or aria-label; RUN.inventory
// overrides the selector), so parts can be chosen after the run.
const inventory = () => page.evaluate(sel => {
  const m = {};
  for (const e of document.querySelectorAll(sel)) {
    const r = e.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
    const k = e.getAttribute('data-component') || (e.getAttribute('data-slot') && `slot=${e.getAttribute('data-slot')}`)
      || (e.getAttribute('role') && `role=${e.getAttribute('role')}`) || `aria=${e.getAttribute('aria-label')}`;
    m[k] ||= { n: 0, box: [r.x, r.y, r.width, r.height].map(Math.round) }; m[k].n++;
  }
  return m;
}, P.RUN.inventory || '[data-component], [role]');

let failed = null;
try {
  await P.RUN.start(h);
  for (const step of P.RUN.steps) {
    await step.send(h);
    const t0 = Date.now();
    let done = false;
    for (let i = 0; Date.now() - t0 < TIMEOUT; i++) {
      const name = `${step.name}-${String(i).padStart(2, '0')}`;
      const file = await shoot(cdp, `${RAW}/${theme}/run/${name}.png`);
      const state = await P.RUN.state(h);
      all[name] = { step: step.name, t: Date.now() - t0, state, file: file.split('/').slice(-3).join('/'), viewport: await viewport(page), parts: await measure(), inventory: await inventory() };
      writeJson(out, all);
      console.log(name, state);
      if (state === 'approval') {
        if (!step.approve) { console.log('approval asked, not allowed for this step: rejecting'); await P.RUN.reject(h); }
        else if (!(await step.approve(h))) { console.log('approval asked for something outside the scratch folder: rejecting'); await P.RUN.reject(h); }
      }
      if (state === 'done' && i >= 2) {
        // One more frame once the window has settled: the frame that first reads done can still be painting
        // the last streamed words.
        await page.waitForTimeout(SETTLE);
        const last = `${step.name}-done`;
        const f = await shoot(cdp, `${RAW}/${theme}/run/${last}.png`);
        all[last] = { step: step.name, t: Date.now() - t0, state: await P.RUN.state(h), file: f.split('/').slice(-3).join('/'), viewport: await viewport(page), parts: await measure(), inventory: await inventory() };
        writeJson(out, all);
        console.log(last, all[last].state);
        done = true; break;
      }
      await page.waitForTimeout(INTERVAL);
    }
    // A step still running at TIMEOUT stops the run: the next prompt would land on a busy agent.
    if (!done) throw new Error(`${step.name} still running after ${TIMEOUT} ms`);
  }
} catch (e) {
  failed = e;
} finally {
  // Restore what start() changed even when a frame or a step failed; disconnect even when that fails.
  try { await P.RUN.finish(h); } catch (e) { failed ||= e; console.error('RESTORE FAILED', e.message); }
  await disconnect(h.browser);
}
if (failed) { console.error('RUN FAILED', failed.message); process.exit(1); }
