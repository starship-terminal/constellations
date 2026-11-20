import { describe, expect, it } from "vitest";
import { createRecentGuard } from "@/components/recent-guard";

describe("createRecentGuard", () => {
  it("is not fresh before the first mark", () => {
    expect(createRecentGuard(1000, () => 0).fresh()).toBe(false);
  });
  it("is fresh inside the window and stale after it", () => {
    let t = 5000;
    const guard = createRecentGuard(1000, () => t);
    guard.mark();
    t += 999;
    expect(guard.fresh()).toBe(true);
    t += 1;
    expect(guard.fresh()).toBe(false);
  });
  it("lets a focus that follows a visibilitychange reload skip its fetch", () => {
    let t = 0;
    const guard = createRecentGuard(1000, () => t);
    let fetches = 0;
    const reload = () => {
      guard.mark();
      fetches++;
    };
    const onEvent = () => {
      if (!guard.fresh()) reload();
    };
    onEvent(); // visibilitychange
    onEvent(); // focus, same tab switch
    expect(fetches).toBe(1);
    t += 5000;
    onEvent();
    expect(fetches).toBe(2);
  });
});
