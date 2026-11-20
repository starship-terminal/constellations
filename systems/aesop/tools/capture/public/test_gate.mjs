// A bot check is a boundary: a stub page that shows a challenge is loaded
// once, recorded as blocked and never handed on to be measured or shot.
// Browser-free; run with `node --test` (tools/package_tests.py does).
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { loadOnce, clearChallenge, pageState, recordBlocked } from './gate.mjs';

const CHALLENGE = { title: 'Just a moment...', body: 'Performing security verification' };
const PRODUCT = { title: 'Aesop', body: 'Skin Care Hand and Body Home Fragrance Gifts Stores Customer service My cart' };
const ERROR = { title: 'Aesop', body: 'Something went wrong' };
const TARGET = 'https://www.aesop.com/shop-all/';

// A page whose successive reads return `served` in turn (the last one repeats).
function stubPage(served, { gotoError } = {}) {
  const calls = [];
  let i = 0;
  return {
    calls,
    gotos: () => calls.filter(([k]) => k === 'goto').map(([, u]) => u),
    async goto(url) { calls.push(['goto', url]); if (gotoError && url !== 'about:blank') throw new Error(gotoError); },
    async evaluate() { return served[Math.min(i++, served.length - 1)]; },
    async waitForTimeout(ms) { calls.push(['wait', ms]); },
  };
}

test('a challenge that never clears is blocked after one load, and the tab is left blank', async () => {
  const page = stubPage([CHALLENGE]);
  const r = await loadOnce(page, TARGET, { tries: 3, step: 1 });
  assert.deepEqual(r, { ok: false, reason: 'bot check did not clear' });
  assert.deepEqual(page.gotos(), [TARGET, 'about:blank']);
});

test('an interstitial that clears on its own is the product, still one load', async () => {
  const page = stubPage([CHALLENGE, CHALLENGE, PRODUCT]);
  assert.deepEqual(await loadOnce(page, TARGET, { tries: 5, step: 1 }), { ok: true });
  assert.deepEqual(page.gotos(), [TARGET]);
});

test('a failed navigation is blocked, not retried', async () => {
  const page = stubPage([PRODUCT], { gotoError: 'net::ERR_TIMED_OUT\nmore' });
  const r = await loadOnce(page, TARGET, { tries: 2, step: 1 });
  assert.equal(r.ok, false);
  assert.equal(r.reason, 'load failed: net::ERR_TIMED_OUT');
  assert.deepEqual(page.gotos(), [TARGET, 'about:blank']);
});

test('an error page is blocked', async () => {
  const page = stubPage([ERROR]);
  assert.deepEqual(await loadOnce(page, TARGET, { tries: 2, step: 1 }), { ok: false, reason: 'page served an error' });
});

test('pageState and clearChallenge only read the page', async () => {
  assert.equal(await pageState(stubPage([CHALLENGE])), 'challenge');
  assert.equal(await pageState(stubPage([{ title: '', body: 'x' }])), 'empty');
  assert.equal(await pageState(stubPage([PRODUCT])), 'ok');
  const page = stubPage([CHALLENGE]);
  assert.equal(await clearChallenge(page, { tries: 2, step: 1 }), false);
  assert.ok(page.calls.every(([k]) => k === 'wait'));
});

test('an error message anywhere in the body is found, not only near the top', async () => {
  const long = { title: 'Aesop', body: 'Skin Care '.repeat(80) + 'Something went wrong' };
  assert.equal(await pageState(stubPage([long])), 'error');
});

test('a blocked page is recorded and earlier readings are kept', () => {
  const out = { _meta: { captured: '2026-11-10' }, components: { 'pdp-title': { page: 'pdp', states: { default: {} } } } };
  const before = JSON.stringify(out.components);
  recordBlocked(out, 'pdp', TARGET, 'bot check did not clear', '2026-12-01T00:00:00Z');
  assert.equal(JSON.stringify(out.components), before);
  assert.deepEqual(out._meta.blocked.pdp, { url: TARGET, reason: 'bot check did not clear', run: '2026-12-01T00:00:00Z' });
  assert.equal(out._meta.captured, '2026-11-10');
});

// The scripts themselves: every page load goes through loadOnce (public.mjs
// and vars.mjs directly, measure.mjs through lib.mjs's open()), each run opens one
// context, and nothing reloads, retries or opens a fresh context to get a
// page past the check.
const source = (name) => fs.readFileSync(new URL(name, import.meta.url), 'utf8').replace(/^\s*\/\/.*$/gm, '');

test('lib.mjs open() loads through loadOnce and nothing else navigates', () => {
  const src = source('lib.mjs');
  assert.match(src, /export async function open\([^)]*\)[^]*?loadOnce\(page, url\)/);
  assert.doesNotMatch(src, /\.goto\(/);
});

test('vars.mjs checks the page again after the settle wait, before it writes', () => {
  const src = source('../vars.mjs');
  const wait = src.indexOf('waitForTimeout(6000)');
  assert.ok(wait > 0 && src.indexOf('pageState(page)', wait) > wait);
  assert.ok(src.indexOf('pageState(page)', wait) < src.indexOf('writeFileSync'));
});

test('measure.mjs records desktop and mobile blocks under separate keys', () => {
  assert.match(source('measure.mjs'), /mobile && !key\.startsWith\('mobile-'\) \? `mobile-\$\{key\}` : key/);
});

for (const [name, loader, contexts] of [
  ['measure.mjs', /\bopen\(page, url/, 1],
  ['public.mjs', /loadOnce\(p, target\)/, 1],
  ['../vars.mjs', /loadOnce\(page, BASE/, 0],
]) {
  test(`${name} loads each page once`, () => {
    const src = source(name);
    assert.match(src, loader);
    assert.doesNotMatch(src, /\.goto\(/);
    assert.doesNotMatch(src, /newPageAt|resolvePdp|reloading|clearChallenge/);
    assert.doesNotMatch(src, /for \(let attempt[^\n]*\n[^\n]*(open|loadOnce|goto)\(/);
    assert.equal((src.match(/\.newContext\(/g) || []).length, contexts);
  });
}
