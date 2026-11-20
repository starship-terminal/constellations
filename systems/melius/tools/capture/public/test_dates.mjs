// node --test tools/capture/public/test_dates.mjs (tools/test_build_tokens.py runs it too)
import assert from 'node:assert/strict';
import test from 'node:test';
import { startRun, touch, readOk, readFailed } from './dates.mjs';

const committed = () => ({
  _meta: { captured: '2026-11-19', read: '2026-11-19', product: 'Melius' },
  components: {
    'nav-link': { url: 'u', states: { default: { color: 'a' }, hover: { color: 'b' } } },
    'hero-cta': { url: 'u', states: { default: { color: 'c' }, 'focus-visible': { outline: 'ring' } } },
  },
});

test('kept components and states take the earlier date, and the run is only an attempt', () => {
  const out = startRun(committed(), '2026-12-01');
  assert.equal(out._meta.read, '2026-11-19');
  assert.equal(out._meta.lastAttempt, '2026-12-01');
  assert.equal(out.components['nav-link'].read, '2026-11-19');
  assert.equal(out.components['nav-link'].states.hover.read, '2026-11-19');
});

test('a partial rerun dates only what it read', () => {
  const out = startRun(committed(), '2026-12-01');
  const earlier = new Map();
  const c = touch(out, earlier, 'nav-link', { url: 'u2' });
  assert.equal(c.read, '2026-11-19');
  assert.equal(out._meta.read, '2026-11-19');
  readOk(out, c, 'default', { color: 'z' }, '2026-12-01');
  assert.equal(c.read, '2026-12-01');
  assert.equal(c.states.default.read, '2026-12-01');
  assert.equal(out._meta.read, '2026-12-01');
  assert.equal(out._meta.captured, '2026-11-19');
  assert.equal(out.components['hero-cta'].read, '2026-11-19');
});

test('a failed read keeps the earlier reading and date, and redates nothing', () => {
  const out = startRun(committed(), '2026-12-01');
  const earlier = new Map();
  const c = touch(out, earlier, 'hero-cta', { url: 'u' });
  readFailed(c, earlier.get('hero-cta'), 'default', { error: 'timeout', via: 'at rest' }, '2026-12-01');
  readFailed(c, earlier.get('hero-cta'), 'focus-visible', { skipped: 'focus failed', via: 'focus failed' }, '2026-12-01');
  assert.deepEqual(c.states.default, { color: 'c', read: '2026-11-19', recaptureError: 'timeout', recaptureRun: '2026-12-01' });
  assert.equal(c.states['focus-visible'].outline, 'ring');
  assert.equal(c.states['focus-visible'].recaptureSkipped, 'focus failed');
  assert.equal(c.read, '2026-11-19');
  assert.equal(out._meta.read, '2026-11-19');
});

test('a failed read with nothing earlier is recorded as a miss, not a reading', () => {
  const out = startRun({ components: {} }, '2026-12-01');
  const c = touch(out, new Map(), 'new', {});
  readFailed(c, undefined, 'default', { error: 'gone' }, '2026-12-01');
  assert.deepEqual(c.states.default, { error: 'gone', recaptureRun: '2026-12-01' });
  assert.equal(c.read, undefined);
  assert.equal(out._meta.read, undefined);
  assert.equal(out._meta.captured, undefined);
});
