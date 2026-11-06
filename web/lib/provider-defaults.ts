// Client-safe provider defaults, shared by the Settings form and the /api/
// routes: the endpoint a provider config means when its base URL is blank.
export const DEFAULT_BASE_URL: Record<string, string> = {
  anthropic: "https://api.anthropic.com",
  openai: "https://api.openai.com/v1",
};

/** The config's base URL, or its wire format's default when blank. The wire
    format defaults to openai, as providerConfig does. */
export const baseUrlOf = (p: { api?: string; base_url?: string }): string =>
  (p.base_url || "").trim() || DEFAULT_BASE_URL[p.api || "openai"] || "";
