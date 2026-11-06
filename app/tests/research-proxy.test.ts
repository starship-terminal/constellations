import { expect, test } from "vitest";
import { NextRequest } from "next/server";
import { proxy } from "@/proxy";
import { mutationGuard } from "@/server/research/http";

for (const path of [
  "/",
  "/api/conversations",
  "/api/collections",
  "/api/settings",
  "/media/systems/example/image.png",
  "/refero-media/shots/example.jpg",
  "/_next/static/example.js",
]) {
  test(`DNS rebinding cannot read ${path}, even with a matching malicious Origin`, async () => {
    const request = new NextRequest(`http://localhost:8845${path}`, {
      headers: {
        host: "evil.test:8845",
        origin: "http://evil.test:8845",
        "x-forwarded-host": "localhost:8845",
      },
    });
    expect(proxy(request).status).toBe(403);
  });
}

test("loopback hosts pass for reads while malformed, missing and lookalike hosts fail", () => {
  for (const host of [
    "localhost",
    "localhost:8845",
    "127.0.0.1:8845",
    "[::1]:8845",
  ]) {
    expect(
      proxy(
        new NextRequest("http://localhost:8845/api/settings", {
          headers: { host },
        }),
      ).headers.get("x-middleware-next"),
    ).toBe("1");
  }
  for (const host of [
    "localhost.evil.test",
    "127.0.0.1.evil.test",
    "evil@localhost:8845",
    "localhost:99999",
    "localhost,evil.test",
    "127.1",
    "",
  ]) {
    expect(
      proxy(
        new NextRequest("http://localhost:8845/api/settings", {
          headers: { host },
        }),
      ).status,
    ).toBe(403);
  }
  expect(
    proxy(new NextRequest("http://localhost:8845/api/settings")).status,
  ).toBe(403);
});

test("matching malicious Host and Origin cannot mutate settings either", () => {
  expect(() =>
    mutationGuard(
      new Request("http://localhost:8845/api/settings", {
        method: "PATCH",
        headers: {
          host: "evil.test:8845",
          origin: "http://evil.test:8845",
          "content-type": "application/json",
        },
        body: "{}",
      }),
    ),
  ).toThrow("loopback hosts");
});
