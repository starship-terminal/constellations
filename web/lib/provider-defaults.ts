// Client-safe provider defaults, shared by the Settings form and the /api/
// routes: the endpoint a provider config means when its base URL is blank.
export const DEFAULT_BASE_URL: Record<string, string> = {
  anthropic: "https://api.anthropic.com",
  openai: "https://api.openai.com/v1",
};

/** The config's base URL, or its wire format's default when blank. The wire
    format defaults to openai, as providerConfig does. Posted JSON is
    untrusted: a non-string base URL counts as blank, and only the listed
    formats (own keys, never Object.prototype's) have a default. */
export const baseUrlOf = (p: { api?: unknown; base_url?: unknown }): string => {
  const typed = typeof p.base_url === "string" ? p.base_url.trim() : "";
  if (typed) return typed;
  const api = typeof p.api === "string" && p.api ? p.api : "openai";
  return Object.prototype.hasOwnProperty.call(DEFAULT_BASE_URL, api) ? DEFAULT_BASE_URL[api] : "";
};
