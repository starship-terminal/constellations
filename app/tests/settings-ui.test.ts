import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { afterEach, expect, test, vi } from "vitest";

vi.mock("next/navigation", () => ({
  usePathname: () => "/settings",
  useSearchParams: () => new URLSearchParams("tab=agents"),
  useRouter: () => ({ push: () => {}, replace: () => {} }),
}));
afterEach(() => {
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

test("only the selected settings tab points at a panel", async () => {
  const { SettingsTabList } = await import("@/features/settings");
  const html = renderToStaticMarkup(
    createElement(SettingsTabList, { tab: "agents", onSelect: () => {} }),
  );
  expect(html.match(/aria-controls="[^"]+"/g)).toEqual([
    'aria-controls="settings-panel-agents"',
  ]);
});

test("a refused or missing clipboard reports failure instead of throwing", async () => {
  const { copyText } = await import("@/features/settings");
  const writeText = vi.fn().mockRejectedValue(new Error("NotAllowedError"));
  vi.stubGlobal("navigator", { clipboard: { writeText } });
  await expect(copyText("x")).resolves.toBe(false);
  vi.stubGlobal("navigator", {});
  await expect(copyText("x")).resolves.toBe(false);
  vi.stubGlobal("navigator", {
    clipboard: { writeText: vi.fn().mockResolvedValue(undefined) },
  });
  await expect(copyText("x")).resolves.toBe(true);
});

test("a Copy button shows its result for two seconds, restarts on a click and stops when detached", async () => {
  vi.useFakeTimers();
  const { copyFeedback } = await import("@/features/settings");
  const shown: unknown[] = [];
  let ok = true;
  const feedback = copyFeedback(
    (state) => shown.push(state),
    async () => ok,
  );
  await feedback.copy("Claude", "claude mcp add");
  expect(shown.at(-1)).toEqual({ label: "Claude", ok: true });
  vi.advanceTimersByTime(1500);
  ok = false;
  await feedback.copy("Codex", "[mcp_servers]");
  expect(shown.at(-1)).toEqual({ label: "Codex", ok: false });
  // The second click restarted the two seconds.
  vi.advanceTimersByTime(1500);
  expect(shown.at(-1)).toEqual({ label: "Codex", ok: false });
  vi.advanceTimersByTime(500);
  expect(shown.at(-1)).toBeUndefined();
  const count = shown.length;
  await feedback.copy("swe", "swe mcp add");
  feedback.detach();
  vi.advanceTimersByTime(5000);
  // Leaving the tab cancels the pending reset.
  expect(shown.length).toBe(count + 1);
  // A copy that finishes after leaving changes nothing.
  await feedback.copy("MCP URL", "/api/mcp");
  expect(shown.length).toBe(count + 1);
  // Attached again, as React re-runs an effect, it shows results again.
  feedback.attach();
  await feedback.copy("MCP URL", "/api/mcp");
  expect(shown.at(-1)).toEqual({ label: "MCP URL", ok: false });
});

test("tab keys move along either axis, wrap, and jump to the ends", async () => {
  const { nextTabIndex } = await import("@/features/settings");
  expect(nextTabIndex("ArrowDown", 0, 4)).toBe(1);
  expect(nextTabIndex("ArrowRight", 3, 4)).toBe(0);
  expect(nextTabIndex("ArrowUp", 0, 4)).toBe(3);
  expect(nextTabIndex("ArrowLeft", 2, 4)).toBe(1);
  expect(nextTabIndex("Home", 2, 4)).toBe(0);
  expect(nextTabIndex("End", 0, 4)).toBe(3);
  expect(nextTabIndex("a", 0, 4)).toBe(-1);
});

test("the tab list is a vertical tablist with one tab stop", async () => {
  const { SettingsTabList } = await import("@/features/settings");
  const html = renderToStaticMarkup(
    createElement(SettingsTabList, { tab: "ai", onSelect: () => {} }),
  );
  expect(html).toContain('role="tablist"');
  expect(html).toContain('aria-orientation="vertical"');
  expect(html.match(/tabindex="0"/g)).toHaveLength(1);
});
