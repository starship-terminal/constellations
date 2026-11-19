import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { afterEach, expect, test, vi } from "vitest";

vi.mock("next/navigation", () => ({
  usePathname: () => "/settings",
  useSearchParams: () => new URLSearchParams("tab=agents"),
  useRouter: () => ({ push: () => {}, replace: () => {} }),
}));
afterEach(() => vi.unstubAllGlobals());

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
