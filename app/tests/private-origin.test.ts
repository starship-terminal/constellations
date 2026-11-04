import { afterEach, expect, test, vi } from "vitest";
import { NextRequest } from "next/server";
import { isAllowedHost, privateOrigin } from "@/server/request-host";
import { proxy } from "@/proxy";
import { mutationGuard } from "@/server/research/http";

const origin = "https://research.tail123.ts.net:8108";
afterEach(() => vi.unstubAllEnvs());

test("private deployment accepts only one explicitly configured tailnet authority", () => {
  expect(isAllowedHost("research.tail123.ts.net:8108")).toBe(false);
  vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", origin);
  expect(privateOrigin()?.origin).toBe(origin);
  for (const host of [
    "localhost:8845",
    "127.0.0.1:8845",
    "research.tail123.ts.net:8108",
  ])
    expect(isAllowedHost(host)).toBe(true);
  for (const host of [
    null,
    "research.tail123.ts.net",
    "research.tail123.ts.net:8109",
    "research.tail123.ts.net.evil.test:8108",
    "evil@research.tail123.ts.net:8108",
    "research.tail123.ts.net:8108,evil.test",
  ])
    expect(isAllowedHost(host)).toBe(false);
  expect(
    proxy(
      new NextRequest("http://localhost:8845/api/settings", {
        headers: { host: "research.tail123.ts.net:8108" },
      }),
    ).headers.get("x-middleware-next"),
  ).toBe("1");
});

test("malformed or public origins never broaden the default loopback policy", () => {
  for (const value of [
    "*",
    "https://example.com",
    "http://research.tail123.ts.net:8108",
    `${origin}/path`,
    `${origin}/`,
    `${origin}?q=1`,
    `${origin}#fragment`,
    "https://user:password@research.tail123.ts.net:8108",
    "https://research.tail123.ts.net:99999",
  ]) {
    vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", value);
    expect(privateOrigin()).toBeNull();
    expect(isAllowedHost("research.tail123.ts.net:8108")).toBe(false);
    expect(isAllowedHost("127.0.0.1:8845")).toBe(true);
  }
});

test("private mutations use configured HTTPS origin without trusting forwarded headers", () => {
  vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", origin);
  function request(
    requestOrigin: string,
    host = "research.tail123.ts.net:8108",
  ) {
    return new Request("http://localhost:8845/api/collections", {
      method: "POST",
      headers: {
        host,
        origin: requestOrigin,
        "content-type": "application/json",
        "x-forwarded-host": "evil.test",
        "x-forwarded-proto": "http",
      },
      body: "{}",
    });
  }
  expect(() => mutationGuard(request(origin))).not.toThrow();
  for (const value of [
    "https://evil.test",
    "http://research.tail123.ts.net:8108",
    "https://research.tail123.ts.net:8109",
    "http://localhost:8845",
  ])
    expect(() => mutationGuard(request(value))).toThrow(
      "same application origin",
    );
  expect(() => mutationGuard(request(origin, "evil.test"))).toThrow(
    "loopback hosts",
  );
});
