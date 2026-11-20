// Unit tests for the Model provider form's rules (components/provider-form.ts),
// used by Settings.tsx and Chat.tsx. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { afterRemove, afterSave, EMPTY_FORM, latestOnly, sameForm, withField, type ProviderForm } from "./provider-form.ts";

// A provider saved from the docs page's Gemini template, as GET /api/provider returns it.
const GEMINI: ProviderForm = {
  ...EMPTY_FORM,
  api: "openai",
  base_url: "https://generativelanguage.googleapis.com/v1beta/openai",
  key_header: "x-goog-api-key",
  models_url: "https://generativelanguage.googleapis.com/v1beta/models",
  model: "gemini-x",
  name: "gemini",
};

describe("the hidden models URL", () => {
  it("is dropped when the base URL or the API changes, so a new endpoint can be saved", () => {
    assert.equal(withField(GEMINI, "base_url", "https://api.openai.com/v1").models_url, "");
    assert.equal(withField(GEMINI, "api", "anthropic").models_url, "");
  });

  it("is kept for any other edit, or an edit that changes nothing", () => {
    for (const k of ["model", "name", "api_key", "key_header"] as const) assert.equal(withField(GEMINI, k, "x").models_url, GEMINI.models_url, k);
    assert.equal(withField(GEMINI, "base_url", GEMINI.base_url).models_url, GEMINI.models_url);
  });
});

describe("a save reply", () => {
  const sent = { ...GEMINI, api_key: "sk-form-test-1111111111" };

  it("empties the key field when the form still holds what was sent", () => {
    const r = afterSave({ ...sent }, sent);
    assert.equal(r.settled, true);
    assert.equal(r.form.api_key, "");
    assert.equal(r.form.model, sent.model);
  });

  it("leaves a form edited since alone, a newer key or a model chip included", () => {
    const newer = { ...sent, api_key: "sk-form-test-2222222222" };
    assert.deepEqual(afterSave(newer, sent), { form: newer, settled: false });
    const chip = withField(sent, "model", "gemini-y");
    assert.deepEqual(afterSave(chip, sent), { form: chip, settled: false });
  });

  it("compares every field", () => {
    for (const k of Object.keys(EMPTY_FORM) as (keyof ProviderForm)[])
      assert.equal(sameForm(sent, { ...sent, [k]: `${sent[k]}-changed` }), false, k);
    assert.equal(sameForm(sent, { ...sent }), true);
  });
});

describe("a remove reply", () => {
  it("empties an unchanged form", () => {
    assert.deepEqual(afterRemove({ ...GEMINI }, GEMINI), { form: EMPTY_FORM, settled: true });
  });

  it("keeps a replacement typed while the removal was in flight", () => {
    const typed = withField(withField(GEMINI, "base_url", "https://api.openai.com/v1"), "api_key", "sk-form-test-3333333333");
    assert.deepEqual(afterRemove(typed, GEMINI), { form: typed, settled: false });
  });
});

describe("latestOnly", () => {
  it("accepts only the newest request's reply", () => {
    const r = latestOnly();
    const first = r.begin();
    const second = r.begin();
    // The first reply lands after the second request started: ignored.
    assert.equal(r.isLatest(first), false);
    assert.equal(r.isLatest(second), true);
    // A later bump (a save's own reply) outranks a read still in flight.
    r.begin();
    assert.equal(r.isLatest(second), false);
  });
});
