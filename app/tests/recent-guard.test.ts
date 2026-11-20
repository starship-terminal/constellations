import { describe, expect, it } from "vitest";
import { createInFlightGuard } from "@/components/recent-guard";

// Mirrors how shell.tsx wires the guard to its events.
function wire() {
  const guard = createInFlightGuard();
  const calls: Array<() => void> = [];
  const reload = () => calls.push(guard.start());
  const onEvent = () => {
    if (!guard.busy()) reload();
  };
  return { calls, onEvent, settle: (i: number) => calls[i]() };
}

describe("createInFlightGuard", () => {
  it("is idle until a fetch starts and idle again once it settles", () => {
    const guard = createInFlightGuard();
    expect(guard.busy()).toBe(false);
    const done = guard.start();
    expect(guard.busy()).toBe(true);
    done();
    expect(guard.busy()).toBe(false);
  });
  it("counts a settle once even if it is called twice", () => {
    const guard = createInFlightGuard();
    const a = guard.start();
    guard.start();
    a();
    a();
    expect(guard.busy()).toBe(true);
  });
  it("joins focus and visibilitychange that fire while a fetch runs", () => {
    const w = wire();
    w.onEvent(); // visibilitychange
    w.onEvent(); // focus, same tab switch
    expect(w.calls).toHaveLength(1);
  });
  it("fetches again for a return after the fetch settled, however soon", () => {
    const w = wire();
    w.onEvent();
    w.settle(0);
    w.onEvent(); // a quick second return: a change made elsewhere must show
    expect(w.calls).toHaveLength(2);
  });
});
