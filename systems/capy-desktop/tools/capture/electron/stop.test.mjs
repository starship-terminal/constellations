// node --test stop.test.mjs (test_stop.py runs it from `make test`).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { stopRun } from './stop.mjs';

// A fake run: busy for `busyAfterStop` reads after the click (Infinity: never stops), counting clicks.
function fake({ busy = true, busyAfterStop = 2 } = {}) {
  const s = { clicks: 0, reads: 0, slept: 0, left: busyAfterStop };
  return {
    s,
    running: async () => { s.reads++; if (!busy) return false; if (!s.clicks) return true; return s.left-- > 0; },
    stop: async () => { s.clicks++; },
    wait: async ms => { s.slept += ms; },
  };
}

test('does nothing when no run is going', async () => {
  const f = fake({ busy: false });
  assert.equal(await stopRun(f), false);
  assert.equal(f.s.clicks, 0);
});

test('clicks Stop once and waits until the run reads as stopped', async () => {
  const f = fake({ busyAfterStop: 3 });
  assert.equal(await stopRun({ ...f, interval: 100 }), true);
  assert.equal(f.s.clicks, 1);
  assert.equal(f.s.slept, 400);
});

test('fails loudly when the run is still going after the timeout', async () => {
  const f = fake({ busyAfterStop: Infinity });
  await assert.rejects(stopRun({ ...f, timeout: 1000, interval: 250 }), /did not stop within 1000 ms/);
  assert.equal(f.s.clicks, 1);
  assert.equal(f.s.slept, 1000);
});

test('a run that ends before the click lands counts as stopped', async () => {
  let done = false;
  const f = { running: async () => !done, stop: async () => { done = true; throw new Error('Stop run is gone'); }, wait: async () => {} };
  assert.equal(await stopRun(f), true);
});

test('a failed click on a run that is still going is thrown', async () => {
  const f = { running: async () => true, stop: async () => { throw new Error('Stop run is covered'); }, wait: async () => {} };
  await assert.rejects(stopRun(f), /Stop run is covered/);
});

test('a read that throws before the click is thrown, with no click', async () => {
  let clicks = 0;
  const f = { running: async () => { throw new Error('page closed'); }, stop: async () => { clicks++; }, wait: async () => {} };
  await assert.rejects(stopRun(f), /page closed/);
  assert.equal(clicks, 0);
});

test('a read that throws after the click is thrown', async () => {
  let clicked = false;
  const f = {
    running: async () => { if (clicked) throw new Error('page closed'); return true; },
    stop: async () => { clicked = true; },
    wait: async () => {},
  };
  await assert.rejects(stopRun(f), /page closed/);
});

test('an interval longer than the timeout checks once, then fails', async () => {
  const f = fake({ busyAfterStop: Infinity });
  await assert.rejects(stopRun({ ...f, timeout: 100, interval: 1000 }), /did not stop within 100 ms/);
  assert.equal(f.s.slept, 1000);
});
