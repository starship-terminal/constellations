// Unit tests for the provider host allowlist (server/chat.py's rules, tested
// there by tools/test_agent.py ProviderHostTest). Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { providerHostAllowed } from "./provider-hosts.ts";

const host = (url: string) => new URL(url).hostname;

describe("providerHostAllowed", () => {
  it("passes the known model APIs unlisted", () => {
    for (const url of [
      "https://api.anthropic.com/v1/models",
      "https://api.openai.com/v1/models",
      "https://generativelanguage.googleapis.com/v1beta/openai/models",
      "https://api.x.ai/v1/models",
      "https://my-res.openai.azure.com/openai/models",
      "https://API.OPENAI.COM./v1",
    ])
      assert.ok(providerHostAllowed(host(url)), url);
  });

  it("refuses internal hosts unlisted", () => {
    for (const url of [
      "https://intranet.corp.test/models",
      "https://10.0.0.5/models",
      "https://169.254.169.254/latest/meta-data",
      "https://127.0.0.1:8443/models",
      "https://0x7f.1/models",
      "https://localhost/models",
      "http://[::1]:8000/models",
      "https://evilopenai.com/v1",
      "https://openai.com.evil.test/v1",
    ])
      assert.ok(!providerHostAllowed(host(url)), url);
  });

  it("lets DESIGN_SYSTEMS_PROVIDER_HOSTS opt hosts in", () => {
    const listed = "models.corp.test, 127.0.0.1,[::1]";
    assert.ok(providerHostAllowed(host("https://models.corp.test/v1"), listed));
    assert.ok(providerHostAllowed(host("https://eu.models.corp.test/v1"), listed));
    assert.ok(providerHostAllowed(host("http://127.0.0.1:11434/v1"), listed));
    assert.ok(providerHostAllowed(host("http://[::1]:8000/models"), listed));
    assert.ok(!providerHostAllowed(host("http://127.0.0.2/v1"), listed));
  });

  it("matches a listed IPv6 address in any spelling", () => {
    assert.ok(providerHostAllowed(host("http://[0:0:0:0:0:0:0:1]:11434/v1"), "0:0:0:0:0:0:0:1"));
    assert.ok(providerHostAllowed(host("http://[::1]:11434/v1"), "0:0:0:0:0:0:0:1"));
    assert.ok(providerHostAllowed(host("http://[0:0:0:0:0:0:0:1]/v1"), "[::1]"));
  });
});
