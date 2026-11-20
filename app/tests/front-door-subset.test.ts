import { afterEach, expect, test, vi } from "vitest";
import cases from "../../server/front-door-cases.json";
import { isAllowedHost } from "@/server/request-host";

afterEach(() => vi.unstubAllEnvs());

// server/routes.py and web/proxy.ts share these Host cases. The research app
// keeps a stricter rule on purpose (loopback plus one exact private origin,
// see docs/DEPLOYMENT.md), so it may refuse a host they accept, but it must
// never accept a host they refuse.
const refused = cases.hosts.filter((entry) => !entry.allowed);

test("the app refuses every host the shared front-door cases refuse", () => {
  expect(refused.length).toBeGreaterThan(0);
  for (const { host } of refused)
    expect(isAllowedHost(host || null), JSON.stringify(host)).toBe(false);
});

test("with a private origin configured, it still refuses every one of them", () => {
  vi.stubEnv(
    "DESIGN_RESEARCH_PRIVATE_ORIGIN",
    "https://box.tail123.ts.net:8108",
  );
  expect(isAllowedHost("box.tail123.ts.net:8108")).toBe(true);
  for (const { host } of refused)
    expect(isAllowedHost(host || null), JSON.stringify(host)).toBe(false);
});
