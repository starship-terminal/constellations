import { expect, test } from "vitest";
import { mutationGuard } from "@/server/research/http";

function request(
  headers: Record<string, string>,
  url = "http://localhost:8845/api/collections",
) {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: "{}",
  });
}

test("same-origin browser mutations use actual Host when Next normalizes the request URL", () => {
  expect(() =>
    mutationGuard(
      request({
        origin: "http://127.0.0.1:8845",
        host: "127.0.0.1:8845",
        "sec-fetch-site": "same-origin",
      }),
    ),
  ).not.toThrow();
  expect(() =>
    mutationGuard(
      request({ origin: "http://localhost:8845", host: "localhost:8845" }),
    ),
  ).not.toThrow();
  expect(() =>
    mutationGuard(request({ origin: "http://[::1]:8845", host: "[::1]:8845" })),
  ).not.toThrow();
});

test("foreign origins, scheme or port mismatches, and spoofed forwarded headers remain blocked", () => {
  for (const origin of [
    "https://evil.test",
    "http://127.0.0.1:9999",
    "https://127.0.0.1:8845",
    "null",
    "http://127.0.0.1:8845/path",
  ]) {
    expect(() =>
      mutationGuard(
        request({
          origin,
          host: "127.0.0.1:8845",
          "x-forwarded-host": "evil.test",
          "x-forwarded-proto": "https",
        }),
      ),
    ).toThrow("same application origin");
  }
  expect(() =>
    mutationGuard(
      request({
        origin: "http://127.0.0.1:8845",
        host: "127.0.0.1:8845",
        "sec-fetch-site": "cross-site",
      }),
    ),
  ).toThrow("Cross-site");
  expect(() =>
    mutationGuard(
      request({ origin: "http://127.0.0.1:8845", host: "evil@127.0.0.1:8845" }),
    ),
  ).toThrow("loopback hosts");
});

test("direct callers without Host retain URL-origin validation and JSON requirements", () => {
  expect(() =>
    mutationGuard(request({ origin: "http://localhost:8845" })),
  ).not.toThrow();
  expect(() =>
    mutationGuard(request({ origin: "http://127.0.0.1:8845" })),
  ).toThrow("same application origin");
  expect(() =>
    mutationGuard(
      new Request("http://localhost:8845/api/collections", {
        method: "POST",
        headers: {
          origin: "http://localhost:8845",
          "content-type": "text/plain",
        },
        body: "{}",
      }),
    ),
  ).toThrow("application/json");
});
