// Tests for motion.mjs (the pure half, no browser) and, when Playwright is installed, motion-probe.mjs
// against a local fixture page. Run with `node --test tools/kit/capture/test_motion.mjs`; make test runs it
// through tools/test_kit_motion.py.
import assert from 'node:assert/strict';
import { execFile, execFileSync } from 'node:child_process';
import { promisify } from 'node:util';
import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import {
  NEGLIGIBLE_MS, animationsOf, classifyMotionValue, declaredOf, diffMotion, easingBezier, groupRecords, hasMotion,
  isMotionVar, mergeSummaries, motionOf, noUrl, normEasing, parseTime, splitList, summarise, transitionsOf,
} from './motion.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));

test('splitList splits at top-level commas only', () => {
  assert.deepEqual(splitList('opacity, transform'), ['opacity', 'transform']);
  assert.deepEqual(splitList('cubic-bezier(0.4, 0, 0.2, 1), ease'), ['cubic-bezier(0.4, 0, 0.2, 1)', 'ease']);
  assert.deepEqual(splitList('linear(0, 0.5 40%, 1), steps(4, end)'), ['linear(0, 0.5 40%, 1)', 'steps(4, end)']);
  assert.deepEqual(splitList(''), []);
  assert.deepEqual(splitList(undefined), []);
});

test('parseTime reads s and ms, and refuses anything else', () => {
  assert.equal(parseTime('0.2s'), 200);
  assert.equal(parseTime('150ms'), 150);
  assert.equal(parseTime('.5S'), 500);
  assert.equal(parseTime('0s'), 0);
  assert.equal(parseTime('0.01ms'), 0.01);
  assert.equal(parseTime('1e-2s'), 10);
  for (const bad of ['var(--d)', 'calc(1s + 2s)', '200', '', null, 'fast']) assert.equal(parseTime(bad), null, String(bad));
});

test('normEasing gives one spelling per easing', () => {
  assert.equal(normEasing('  EASE-OUT '), 'ease-out');
  assert.equal(normEasing('cubic-bezier(0.40, 0, .2, 1.0)'), 'cubic-bezier(0.4, 0, 0.2, 1)');
  assert.equal(normEasing('cubic-bezier(0.4,0,0.2,1)'), 'cubic-bezier(0.4, 0, 0.2, 1)');
  assert.equal(normEasing('cubic-bezier(0.1234567, 0, 0, 1)'), 'cubic-bezier(0.1235, 0, 0, 1)');
  assert.equal(normEasing('steps(4)'), 'steps(4, end)');
  assert.equal(normEasing('steps(4, jump-start)'), 'steps(4, start)');
  assert.equal(normEasing('step-end'), 'steps(1, end)');
  assert.equal(normEasing('linear(0,  0.25 20%,1)'), 'linear(0, 0.25 20%, 1)');
  assert.equal(normEasing(''), '');
});

test('easingBezier expands keywords and bezier, and leaves steps and linear() alone', () => {
  assert.deepEqual(easingBezier('ease-out'), [0, 0, 0.58, 1]);
  assert.deepEqual(easingBezier('cubic-bezier(0.4, 0, 0.2, 1)'), [0.4, 0, 0.2, 1]);
  assert.equal(easingBezier('steps(4, end)'), null);
  assert.equal(easingBezier('linear(0, 1)'), null);
});

test('classifyMotionValue and isMotionVar sort custom properties', () => {
  assert.equal(classifyMotionValue('200ms'), 'duration');
  assert.equal(classifyMotionValue('cubic-bezier(0.2, 0, 0, 1)'), 'easing');
  assert.equal(classifyMotionValue('ease-in-out'), 'easing');
  assert.equal(classifyMotionValue('12px'), 'other');
  assert.equal(isMotionVar('--dur-fast', 'var(--x)'), true);
  assert.equal(isMotionVar('--ease-out', 'x'), true);
  assert.equal(isMotionVar('--cds-motion-scale', '1'), true);
  assert.equal(isMotionVar('--custom', '120ms'), true);
  assert.equal(isMotionVar('--color-bg', '#fff'), false);
  assert.equal(isMotionVar('--duration-label', 'Duration'), true);
  assert.equal(isMotionVar('--durable-colour', '#000'), false);
});

test('transitionsOf zips the lists, repeating the short ones, and drops no-ops', () => {
  const t = transitionsOf({ transitionProperty: 'opacity, transform, color', transitionDuration: '0.2s, 150ms', transitionTimingFunction: 'ease', transitionDelay: '0s, 50ms, 0s' });
  assert.deepEqual(t, [
    { property: 'opacity', durationMs: 200, delayMs: 0, easing: 'ease' },
    { property: 'transform', durationMs: 150, delayMs: 50, easing: 'ease' },
    { property: 'color', durationMs: 200, delayMs: 0, easing: 'ease' },
  ]);
  assert.deepEqual(transitionsOf({ transitionProperty: 'all', transitionDuration: '0s', transitionTimingFunction: 'ease', transitionDelay: '0s' }), []);
  assert.deepEqual(transitionsOf({ transitionProperty: 'none', transitionDuration: '1s' }), []);
  const raw = transitionsOf({ transitionProperty: 'opacity', transitionDuration: 'var(--d)' });
  assert.equal(raw[0].durationRaw, 'var(--d)');
});

test('animationsOf reads one record per name and skips none', () => {
  const a = animationsOf({ animationName: 'spin, none, fade', animationDuration: '1s', animationTimingFunction: 'linear, ease', animationDelay: '0s', animationIterationCount: 'infinite, 1', animationDirection: 'normal', animationFillMode: 'none, both', animationPlayState: 'running' });
  assert.deepEqual(a.map((x) => [x.name, x.durationMs, x.easing, x.iterationCount]), [['spin', 1000, 'linear', 'infinite'], ['fade', 1000, 'linear', 'infinite']]);
  assert.deepEqual(animationsOf({ animationName: 'none' }), []);
});

test('motionOf and hasMotion', () => {
  assert.equal(hasMotion(motionOf({})), false);
  assert.equal(hasMotion(motionOf({ scrollBehavior: 'smooth' })), true);
  assert.equal(hasMotion(motionOf({ scrollBehavior: 'auto' })), false);
});

const base = motionOf({
  transitionProperty: 'opacity, transform', transitionDuration: '200ms', transitionTimingFunction: 'ease-out', transitionDelay: '0s',
  animationName: 'spin', animationDuration: '1s', animationTimingFunction: 'linear', animationDelay: '0s', animationIterationCount: 'infinite',
});

test('diffMotion: removed, shortened, kept and changed', () => {
  const none = motionOf({});
  assert.equal(diffMotion(base, none).outcome, 'removed');
  // the usual reset: 0.01ms is no motion
  const reset = motionOf({ transitionProperty: 'opacity, transform', transitionDuration: '0.01ms', transitionTimingFunction: 'ease-out', animationName: 'spin', animationDuration: '0.01ms', animationTimingFunction: 'linear', animationIterationCount: '1' });
  assert.ok(0.01 <= NEGLIGIBLE_MS);
  assert.equal(diffMotion(base, reset).outcome, 'removed');
  const shorter = motionOf({ transitionProperty: 'opacity, transform', transitionDuration: '50ms', transitionTimingFunction: 'ease-out', animationName: 'none' });
  const d = diffMotion(base, shorter);
  assert.equal(d.outcome, 'reduced');
  assert.deepEqual(d.items.map((i) => [i.key, i.outcome]), [['opacity', 'shortened'], ['transform', 'shortened'], ['spin', 'removed']]);
  assert.equal(diffMotion(base, base).outcome, 'kept');
  assert.equal(diffMotion(base, structuredClone(base)).items.find((i) => i.key === 'spin').loops, true);
  const eased = structuredClone(base); eased.transitions[0].easing = 'linear';
  assert.equal(diffMotion(base, eased).items[0].outcome, 'changed');
});

test('diffMotion: partial, none and added', () => {
  const partial = structuredClone(base); partial.animations = [];
  assert.equal(diffMotion(base, partial).outcome, 'partial');
  assert.equal(diffMotion(motionOf({}), motionOf({})).outcome, 'none');
  const added = diffMotion(motionOf({}), motionOf({ transitionProperty: 'opacity', transitionDuration: '1s' }));
  assert.equal(added.outcome, 'added');
  assert.equal(added.items[0].outcome, 'added');
  assert.equal(diffMotion({ transitions: [], animations: [], scrollBehavior: 'smooth' }, motionOf({})).outcome, 'removed');
});

test('groupRecords folds equal motion into one group, in a stable order', () => {
  const recs = [
    { node: 'button.btn', base, reduced: motionOf({}) },
    { node: 'a.link', base, reduced: motionOf({}) },
    { node: 'div.card', base: motionOf({ transitionProperty: 'opacity', transitionDuration: '1s' }), reduced: motionOf({ transitionProperty: 'opacity', transitionDuration: '1s' }) },
    { node: 'p.still', base: motionOf({}), reduced: motionOf({}) },
  ];
  const g = groupRecords(recs);
  assert.deepEqual(g.map((x) => [x.count, x.outcome, x.nodes]), [[2, 'removed', ['button.btn', 'a.link']], [1, 'kept', ['div.card']]]);
  assert.deepEqual(groupRecords([...recs].reverse()).map((x) => x.count), [2, 1]);
});

test('summarise and mergeSummaries name the page behaviour', () => {
  const kept = groupRecords([{ node: 'a', base, reduced: base }]);
  assert.equal(summarise(kept).behaviour, 'ignores');
  assert.deepEqual(summarise(kept).loops, ['spin']);
  const gone = groupRecords([{ node: 'a', base, reduced: motionOf({}) }]);
  assert.equal(summarise(gone).behaviour, 'honours');
  assert.equal(summarise([]).behaviour, 'no-motion');
  assert.equal(summarise([...kept, ...gone]).behaviour, 'partial');
  assert.equal(mergeSummaries([summarise(kept), summarise(gone)]).behaviour, 'partial');
  assert.equal(mergeSummaries([summarise(gone), summarise(gone)]).behaviour, 'honours');
  assert.equal(mergeSummaries([]).behaviour, 'no-motion');
});

test('declaredOf records only what the rule authors', () => {
  const d = declaredOf({ selector: '.btn:hover', context: ['@media (hover: hover)'], transitionProperty: 'color', transitionDuration: '0.3s', transitionTimingFunction: 'ease-in' });
  assert.deepEqual(d.transitions, [{ property: 'color', durationMs: 300, easing: 'ease-in' }]);
  assert.equal(d.viaVar, undefined);
  assert.equal(declaredOf({ selector: '.x', context: [], transitionProperty: 'opacity', transitionDuration: 'var(--d)' }).viaVar, true);
});

test('declaredOf keeps every entry of a state rule that sets only durations, and invents no easing', () => {
  const d = declaredOf({ selector: '.btn:hover', context: [], transitionDuration: '.4s, .6s' });
  assert.deepEqual(d.transitions, [{ property: '(base #0)', durationMs: 400 }, { property: '(base #1)', durationMs: 600 }]);
  assert.equal(declaredOf({ selector: '.x', context: [], animationDelay: '1s' }).animations[0].name, '(base #0)');
  assert.deepEqual(declaredOf({ selector: '.x', context: [], color: 'red' }).transitions, []);
});

test('declaredOf keeps a state-only scroll-behavior: smooth', () => {
  assert.equal(declaredOf({ selector: 'html:focus-within', context: [], scrollBehavior: 'smooth' }).scrollBehavior, 'smooth');
  assert.equal(declaredOf({ selector: 'html', context: [], scrollBehavior: 'auto' }).scrollBehavior, undefined);
});

test('more motion under reduce is never a reduction', () => {
  const slow = motionOf({ transitionProperty: 'opacity', transitionDuration: '200ms' });
  const slower = motionOf({ transitionProperty: 'opacity', transitionDuration: '2000ms' });
  const d = diffMotion(slow, slower);
  assert.equal(d.items[0].outcome, 'increased');
  assert.equal(d.outcome, 'increased');
  assert.equal(summarise(groupRecords([{ node: 'a', base: slow, reduced: slower }])).behaviour, 'partial');
  // a replacement infinite animation: the old one is gone, the new one loops
  const spin = motionOf({ animationName: 'spin', animationDuration: '1s', animationIterationCount: 'infinite' });
  const pulse = motionOf({ animationName: 'pulse', animationDuration: '1s', animationIterationCount: 'infinite' });
  const swap = diffMotion(spin, pulse);
  assert.deepEqual(swap.items.map((i) => [i.key, i.outcome, !!i.loops]), [['spin', 'removed', false], ['pulse', 'added', true]]);
  assert.equal(swap.outcome, 'partial');
  assert.deepEqual(summarise(groupRecords([{ node: 'a', base: spin, reduced: pulse }])).loops, ['pulse']);
  // smooth scrolling that only appears under reduce
  const smooth = diffMotion(slow, { ...slow, scrollBehavior: 'smooth' });
  assert.ok(smooth.items.some((i) => i.kind === 'scroll' && i.outcome === 'added'));
  assert.equal(smooth.outcome, 'increased');
});

test('an animation paused under reduce is stopped, not kept or looping', () => {
  const run = motionOf({ animationName: 'spin', animationDuration: '1s', animationIterationCount: 'infinite', animationPlayState: 'running' });
  const paused = motionOf({ animationName: 'spin', animationDuration: '1s', animationIterationCount: 'infinite', animationPlayState: 'paused' });
  assert.equal(animationsOf({ animationName: 'spin', animationPlayState: 'paused' })[0].playState, 'paused');
  const d = diffMotion(run, paused);
  assert.equal(d.outcome, 'removed');
  assert.equal(d.items[0].loops, undefined);
  assert.equal(summarise(groupRecords([{ node: 'a', base: run, reduced: paused }])).behaviour, 'honours');
  assert.notEqual(diffMotion(run, run).outcome, 'removed');
});

test('noUrl keeps authored tokens and cuts a url()', () => {
  assert.equal(noUrl('url("https://x.test/a.png?fakesig=s3cret")'), 'url(…)');
  assert.equal(noUrl("fade URL( 'https://x.test/b?t=1' )"), 'fade url(…)');
  assert.equal(noUrl('url(data:image/png;base64,AAAA)'), 'url(data:image/png;base64,AAAA)');
  assert.equal(noUrl('200ms'), '200ms');
});

// ---- the probe, against a fixture page (needs Playwright; skipped without it)
const PW = process.env.PLAYWRIGHT || path.join(os.homedir(), '.design-systems/pw/node_modules/playwright/index.mjs');
const FIXTURE = `<!doctype html><meta charset=utf-8><title>fixture</title><style>
:root { --dur-fast: 120ms; --ease-out: cubic-bezier(0.2, 0, 0, 1); --hero: url("https://cdn.test/h.png?fakesig=SECRET"); --gap: 8px; }
@keyframes spin { from { transform: rotate(0) } to { transform: rotate(360deg) } }
@keyframes fade { from { opacity: 0 } to { opacity: 1 } }
.btn { transition: background-color var(--dur-fast) var(--ease-out), transform .2s ease-in-out; }
.btn:hover { transition-duration: .4s; }
.spinner { animation: spin 1s linear infinite; }
.toast { animation: fade 300ms ease; }
.polite { transition: opacity 200ms; }
.glow::before { content: ""; display: block; transition: opacity 500ms linear; }
@media (prefers-reduced-motion: reduce) { .spinner { animation: none; } .toast { animation-duration: 0.01ms !important; } .btn { transition: none; } .glow::before { transition-duration: 1ms; } }
</style><button class=btn>ok</button><div class=spinner></div><div class=toast></div><div class=polite></div><div class=glow></div>`;

test('motion-probe reads a fixture page in both passes', { skip: !fs.existsSync(PW) && 'the capture Playwright is not installed' }, () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'motion-'));
  const page = path.join(dir, 'page.html');
  fs.writeFileSync(page, FIXTURE);
  const out = path.join(dir, 'motion.json');
  execFileSync(process.execPath, [path.join(here, 'motion-probe.mjs'), '--urls', 'file://' + page], { env: { ...process.env, PLAYWRIGHT: PW, OUT_JSON: out }, timeout: 120000, stdio: 'pipe' });
  const raw = JSON.parse(fs.readFileSync(out, 'utf8'));
  const [p] = Object.values(raw.pages);
  assert.deepEqual(p.matchMedia, { normal: false, reduce: true });
  assert.equal(p.summary.behaviour, 'partial');
  assert.equal(p.summary.kept, 1, 'only .polite ignores reduce');
  assert.equal(p.summary.removed, 4, 'button, spinner, toast, glow::before');
  const byNode = Object.fromEntries(p.groups.flatMap((g) => g.nodes.map((n) => [n, g])));
  assert.deepEqual(byNode['button.btn'].base.transitions.map((t) => [t.property, t.durationMs, t.easing]), [['background-color', 120, 'cubic-bezier(0.2, 0, 0, 1)'], ['transform', 200, 'ease-in-out']]);
  assert.equal(byNode['div.spinner'].base.animations[0].iterationCount, 'infinite');
  assert.equal(byNode['div.spinner'].outcome, 'removed');
  assert.equal(byNode['div.polite'].outcome, 'kept');
  assert.ok(byNode['div.glow::before'], 'a pseudo-element is its own record');
  assert.deepEqual(p.keyframes.map((k) => [k.name, k.properties]).sort(), [['fade', ['opacity']], ['spin', ['transform']]]);
  assert.equal(p.reducedMotionRules.length, 4);
  assert.ok(p.reducedMotionRules.some((r) => r.declarations['animation-duration'] === '0.01ms !important'));
  assert.ok(p.declared.some((d) => d.selector === '.btn:hover' && d.transitions[0].durationMs === 400), 'a :hover rule is read from the sheet');
  const vars = Object.fromEntries(p.customProperties.map((v) => [v.name, v.resolved]));
  assert.deepEqual(vars, { '--dur-fast': '120ms', '--ease-out': 'cubic-bezier(0.2, 0, 0, 1)' });
  assert.ok(!JSON.stringify(raw).includes('SECRET'));
  assert.equal(raw.summary.behaviour, 'partial');
});

// ---- the probe over http: imports, sheet media, SVG, signed selectors, page keys, failure, paths
const PAGE2 = `<!doctype html><meta charset=utf-8><title>f2</title>
<style>@import url("/imp.css");</style>
<style media="(prefers-reduced-motion: reduce)">.on-reduce { animation: none; }</style>
<style>
.dot { animation: blink 1s ease infinite; }
@keyframes blink { 50% { opacity: .2 } }
@media (prefers-reduced-motion: no-preference) { .btn:hover { transition: transform 700ms ease-out; } }
@media (prefers-reduced-motion: reduce) { img[src="https://cdn.test/a.png?fakesig=SECRET2"], .dot { animation: none; } }
</style>
<svg width=20 height=20><circle class=dot cx=10 cy=10 r=5 /></svg><div class=imp></div>`;
const IMP = '@keyframes imp { from { opacity: 0 } to { opacity: 1 } } .imp { animation: imp 1s linear infinite; } @media (prefers-reduced-motion: reduce) { .imp { animation: none; } }';

function serve(routes) {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const r = routes[req.url.split('?')[0]];
      if (!r) { res.writeHead(404); return res.end(); }
      res.writeHead(200, { 'content-type': r[0] }); res.end(r[1]);
    });
    srv.listen(0, '127.0.0.1', () => resolve(srv));
  });
}
const probe = (args, env = {}) => execFileSync(process.execPath, [path.join(here, 'motion-probe.mjs'), ...args], { env: { ...process.env, PLAYWRIGHT: PW, ...env }, timeout: 120000, stdio: 'pipe' });
const skipPw = !fs.existsSync(PW) && 'the capture Playwright is not installed';

test('motion-probe follows @import, reads sheet media and SVG, keeps pages apart and strips signed selectors', { skip: skipPw }, async () => {
  const srv = await serve({ '/p.html': ['text/html', PAGE2], '/imp.css': ['text/css', IMP] });
  try {
    const base = `http://127.0.0.1:${srv.address().port}/p.html`;
    const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'motion-')), 'motion.json');
    // two URLs that sanitise to the same form must stay two pages
    // (async: the server lives in this process, so a blocking spawn would never be answered)
    await promisify(execFile)(process.execPath, [path.join(here, 'motion-probe.mjs'), '--urls', `${base}?tab=one,${base}?tab=two`], { env: { ...process.env, PLAYWRIGHT: PW, OUT_JSON: out }, timeout: 120000 });
    const raw = JSON.parse(fs.readFileSync(out, 'utf8'));
    assert.deepEqual(Object.keys(raw.pages), ['page-1', 'page-2']);
    const p = raw.pages['page-1'];
    assert.ok(p.keyframes.some((k) => k.name === 'imp'), 'an @import is walked');
    assert.ok(p.reducedMotionRules.some((r) => r.selector === '.imp'), 'a rule inside an imported sheet is read');
    assert.ok(p.reducedMotionRules.some((r) => r.selector === '.on-reduce' && /prefers-reduced-motion/.test(r.media)), "a sheet's own media condition is kept");
    assert.ok(p.reducedMotionRules.some((r) => /no-preference/.test(r.media)), 'no-preference rules are kept');
    assert.ok(p.declared.some((d) => d.context.some((c) => /no-preference/.test(c)) && d.transitions[0].durationMs === 700));
    const nodes = p.groups.flatMap((g) => g.nodes);
    assert.ok(nodes.some((n) => n.startsWith('circle')), 'an svg descendant is read');
    assert.equal(p.summary.behaviour, 'honours');
    assert.ok(!JSON.stringify(raw).includes('SECRET2'), 'a signed URL in a selector is cut');
    assert.ok(p.reducedMotionRules.some((r) => r.selector.includes('<url>') && r.selector.includes('.dot')));
    assert.equal(p.sheetsTruncated.reducedRules, false);
  } finally { srv.close(); }
});

test('motion-probe flags a cap and a cut list, and reads no stopped element out of them', { skip: skipPw }, () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'motion-'));
  fs.writeFileSync(path.join(dir, 'page.html'), FIXTURE);
  const out = path.join(dir, 'motion.json');
  probe(['--urls', 'file://' + path.join(dir, 'page.html')], { OUT_JSON: out, MOTION_CAP: '3' });
  const [p] = Object.values(JSON.parse(fs.readFileSync(out, 'utf8')).pages);
  assert.ok(p.capped.droppedNormal > 0, 'moving elements past the cap are counted');
  assert.equal(p.summary.moving, 3, 'only the kept three are compared');
  assert.equal(p.summary.kept, 0, '.polite was dropped, not read as stopped');
});

test('motion-probe fails, and keeps the earlier file, when no page was captured', { skip: skipPw }, () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'motion-')), 'motion.json');
  fs.writeFileSync(out, '{"earlier":true}');
  assert.throws(() => probe(['--urls', 'http://127.0.0.1:1/'], { OUT_JSON: out }), (e) => e.status === 1 && /no page was captured/.test(String(e.stderr)));
  assert.equal(fs.readFileSync(out, 'utf8'), '{"earlier":true}');
});

test('motion-probe finds its package folder when the path has a space', { skip: skipPw }, () => {
  const pkg = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'motion-')), 'my pkg');
  const cap = path.join(pkg, 'tools', 'capture');
  fs.mkdirSync(cap, { recursive: true });
  for (const f of ['motion-probe.mjs', 'motion.mjs', 'safe-url.mjs']) fs.copyFileSync(path.join(here, f), path.join(cap, f));
  fs.writeFileSync(path.join(pkg, 'page.html'), FIXTURE);
  execFileSync(process.execPath, [path.join(cap, 'motion-probe.mjs'), '--urls', 'file://' + path.join(pkg, 'page.html').replace(/ /g, '%20')], { env: { ...process.env, PLAYWRIGHT: PW }, timeout: 120000, stdio: 'pipe' });
  assert.ok(fs.existsSync(path.join(pkg, 'raw', 'motion.json')));
});
