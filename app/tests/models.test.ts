import { test, expect, vi } from "vitest";
import { discoverModels } from "@/server/research/models";
test("model discovery sends only the server key to the configured endpoint and rejects redirects", async () => {
  const request = vi
    .fn<typeof fetch>()
    .mockResolvedValue(
      Response.json({ data: [{ id: "b" }, { id: "a" }, { id: "b" }, {}] }),
    );
  expect(
    await discoverModels(
      { provider: "openai", baseURL: "http://localhost:9999/v1/" },
      "secret",
      request,
    ),
  ).toEqual(["a", "b"]);
  expect(request.mock.calls[0][0]).toBe("http://localhost:9999/v1/models");
  expect(request.mock.calls[0][1]).toMatchObject({
    headers: { Authorization: "Bearer secret" },
    redirect: "error",
  });
});
test("connection errors never expose provider response bodies or keys", async () => {
  const request = vi
    .fn<typeof fetch>()
    .mockResolvedValue(new Response("secret diagnostic", { status: 401 }));
  await expect(
    discoverModels({ provider: "anthropic", baseURL: null }, "secret", request),
  ).rejects.toThrow("HTTP 401");
  await expect(
    discoverModels({ provider: "openai", baseURL: null }, undefined, request),
  ).rejects.toThrow("credential");
});
