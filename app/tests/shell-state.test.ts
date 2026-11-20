import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { expect, test, vi } from "vitest";

vi.mock("next/navigation", () => ({
  usePathname: () => "/library",
  useSearchParams: () => new URLSearchParams(),
  useRouter: () => ({ push: () => {}, replace: () => {} }),
}));

test("history shows no empty state before it has loaded", async () => {
  const { AppShell } = await import("@/components/shell");
  const html = renderToStaticMarkup(createElement(AppShell, null, "page"));
  expect(html).toContain("History");
  expect(html).not.toContain("Your research will appear here.");
});

test("the sidebar init script marks a collapsed sidebar before paint", async () => {
  const { sidebarInitScript } = await import("@/components/shell");
  const run = (stored: string | null) => {
    const root = { dataset: {} as Record<string, string> };
    new Function("localStorage", "document", sidebarInitScript)(
      { getItem: () => stored },
      { documentElement: root },
    );
    return root.dataset.sidebar;
  };
  expect(run("true")).toBe("collapsed");
  expect(run("false")).toBeUndefined();
  expect(run(null)).toBeUndefined();
});
