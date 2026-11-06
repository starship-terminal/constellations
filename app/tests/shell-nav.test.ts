import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it, vi } from "vitest";

vi.mock("next/navigation", () => ({
  usePathname: () => "/library",
  useSearchParams: () => new URLSearchParams("platform=desktop"),
  useRouter: () => ({ push: () => {}, replace: () => {} }),
}));

describe("Catalog navigation", () => {
  it("offers Desktop beside Web and iOS, and marks it active", async () => {
    const { CatalogNavigation } = await import("@/components/shell");
    const html = renderToStaticMarkup(
      createElement(CatalogNavigation, { onNavigate: () => {} }),
    );
    for (const p of ["web", "mobile", "desktop"])
      expect(html).toContain(`href="/library?platform=${p}"`);
    expect(html).toMatch(
      /class="nav-link active" href="\/library\?platform=desktop"/,
    );
  });
});
