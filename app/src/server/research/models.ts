import { HttpError } from "./http";
export async function discoverModels(
  settings: { provider: "openai" | "anthropic"; baseURL: string | null },
  key: string | undefined,
  request: typeof fetch = fetch,
) {
  if (!key)
    throw new HttpError(
      400,
      "Configure the provider credential on the server first.",
    );
  const base =
    settings.baseURL ||
    (settings.provider === "openai"
      ? "https://api.openai.com/v1"
      : "https://api.anthropic.com/v1");
  let response: Response;
  try {
    response = await request(`${base.replace(/\/$/, "")}/models`, {
      headers:
        settings.provider === "openai"
          ? { Authorization: `Bearer ${key}` }
          : { "x-api-key": key, "anthropic-version": "2023-06-01" },
      signal: AbortSignal.timeout(15000),
      redirect: "error",
    });
  } catch {
    throw new HttpError(
      502,
      "The provider could not be reached. Check the saved base URL and server connection.",
    );
  }
  if (!response.ok)
    throw new HttpError(
      502,
      `Provider connection failed (HTTP ${response.status}). Check the credential and endpoint.`,
    );
  let body: unknown;
  try {
    body = await response.json();
  } catch {
    throw new HttpError(502, "The provider returned an invalid model list.");
  }
  const data = (body as { data?: unknown })?.data;
  if (!Array.isArray(data))
    throw new HttpError(
      502,
      "This endpoint does not support model discovery. Enter a model ID manually.",
    );
  return [
    ...new Set(
      data.flatMap((row) =>
        typeof row?.id === "string" && row.id.length <= 160 ? [row.id] : [],
      ),
    ),
  ].sort();
}
