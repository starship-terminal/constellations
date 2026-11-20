// node --test tools/capture/public/test_dates.mjs (tools/test_build_tokens.py runs it too)
import assert from 'node:assert/strict';
import test from 'node:test';
import { startRun, markRead } from './dates.mjs';

const committed = () => ({
  _meta: { read: '2026-11-18', tool: 'tools/capture/public/measure.mjs' },
  components: { hero: { run: '2026-11-18', states: { default: { style: {}, run: '2026-11-18' } } } },
});

test('starting a run records the attempt and keeps the earlier read date', () => {
  const out = startRun(committed(), '2026-12-01');
  assert.equal(out._meta.read, '2026-11-18');
  assert.equal(out._meta.lastAttempt, '2026-12-01');
  assert.equal(out.components.hero.run, '2026-11-18');
});

test('only a successful read moves the dates', () => {
  const out = startRun(committed(), '2026-12-01');
  const c = out.components.hero;
  markRead(out, c, 'hover', { style: { color: 'x' } }, '2026-12-01');
  assert.equal(c.states.hover.run, '2026-12-01');
  assert.equal(c.states.default.run, '2026-11-18');
  assert.equal(c.run, '2026-12-01');
  assert.equal(out._meta.read, '2026-12-01');
});

test('an empty file gets no read date until something is read', () => {
  const out = startRun({}, '2026-12-01');
  assert.equal(out._meta.read, undefined);
  assert.deepEqual(out.components, {});
});
