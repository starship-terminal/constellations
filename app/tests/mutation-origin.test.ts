import { afterEach, expect, test, vi } from "vitest";
import { mutationGuard } from "@/server/research/http";

const privateOrigin = "https://research.tail123.ts.net:8108";
afterEach(() => vi.unstubAllEnvs());
function request(headers: Record<string, string>) {
  return new Request("http://localhost:8845/api/collections", {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: "{}",
  });
}

test("a mutation through the private origin without Origin is refused", () => {
  vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", privateOrigin);
  expect(() =>
    mutationGuard(request({ host: "research.tail123.ts.net:8108" })),
  ).toThrow("same application origin");
  expect(() =>
    mutationGuard(
      request({
        host: "research.tail123.ts.net:8108",
        "sec-fetch-site": "same-origin",
      }),
    ),
  ).not.toThrow();
  expect(() =>
    mutationGuard(
      request({ host: "research.tail123.ts.net:8108", origin: privateOrigin }),
    ),
  ).not.toThrow();
});

test("loopback mutations without Origin stay open, with or without a private origin", () => {
  expect(() =>
    mutationGuard(request({ host: "127.0.0.1:8845" })),
  ).not.toThrow();
  vi.stubEnv("DESIGN_RESEARCH_PRIVATE_ORIGIN", privateOrigin);
  expect(() =>
    mutationGuard(request({ host: "127.0.0.1:8845" })),
  ).not.toThrow();
  expect(() =>
    mutationGuard(request({ host: "localhost:8845" })),
  ).not.toThrow();
});
