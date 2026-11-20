import { z } from "zod";
import { isAllowedHost, privateOrigin } from "@/server/request-host";
export class HttpError extends Error {
  constructor(
    public status: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}
/**
 * Refuses a mutation a browser could send from another site: a foreign
 * Origin, `Sec-Fetch-Site: cross-site`, or a body that is not JSON (a
 * cross-site form or `text/plain` POST needs no preflight).
 * `originlessClients` lets a request with neither Origin nor Sec-Fetch-Site
 * through the private origin too: MCP clients send neither header, and a
 * browser on another site always sends one of them.
 */
export function mutationGuard(
  request: Request,
  { originlessClients = false }: { originlessClients?: boolean } = {},
) {
  const actualHost = request.headers.get("host");
  if (actualHost && !isAllowedHost(actualHost)) {
    throw new HttpError(
      403,
      "This personal research app only accepts loopback hosts or its configured private origin.",
    );
  }
  const origin = request.headers.get("origin");
  if (origin) {
    let expectedOrigin: string;
    try {
      const requestUrl = new URL(request.url);
      // Next can normalize Request.url to localhost while the browser uses
      // 127.0.0.1. The actual HTTP Host remains the browser-facing authority.
      // Never trust forwarded-host or forwarded-proto supplied by a client.
      const host = request.headers.get("host");
      if (host && /[\\/\s?#@,]/.test(host)) throw new Error("Invalid Host");
      const publicUrl = host
        ? new URL(`${requestUrl.protocol}//${host}`)
        : requestUrl;
      const configured = privateOrigin();
      expectedOrigin =
        configured && host === configured.host
          ? configured.origin
          : publicUrl.origin;
      const parsedOrigin = new URL(origin);
      if (
        !["http:", "https:"].includes(parsedOrigin.protocol) ||
        parsedOrigin.origin !== origin ||
        origin !== expectedOrigin
      ) {
        throw new Error("Origin mismatch");
      }
    } catch {
      throw new HttpError(
        403,
        "This action requires the same application origin.",
      );
    }
  }
  // Through the private origin every mutation must prove it came from that
  // origin. A browser always sends Origin on these requests, so a missing one
  // is refused there. Loopback requests without Origin (same-machine curl,
  // scripts) stay allowed, because only this machine can reach that Host.
  const configured = privateOrigin();
  if (
    !origin &&
    !originlessClients &&
    configured &&
    actualHost === configured.host &&
    request.headers.get("sec-fetch-site") !== "same-origin"
  )
    throw new HttpError(
      403,
      "This action requires the same application origin.",
    );
  if (request.headers.get("sec-fetch-site") === "cross-site")
    throw new HttpError(403, "Cross-site actions are not allowed.");
  if (
    !request.headers.get("content-type")?.includes("application/json") &&
    request.method !== "DELETE"
  )
    throw new HttpError(415, "Send application/json.");
}
export async function readBody<T>(
  request: Request,
  schema: z.ZodType<T>,
): Promise<T> {
  const text = await request.text();
  if (text.length > 1_000_000)
    throw new HttpError(413, "Request is too large.");
  let value: unknown;
  try {
    value = JSON.parse(text);
  } catch {
    throw new HttpError(400, "Invalid JSON.");
  }
  return schema.parse(value);
}
export function endpoint(fn: () => Promise<Response>) {
  return fn().catch((error: unknown) => {
    if (error instanceof z.ZodError)
      return Response.json(
        {
          error: "Invalid request.",
          issues: error.issues.map((i) => ({
            path: i.path.join("."),
            message: i.message,
          })),
        },
        { status: 400 },
      );
    if (error instanceof HttpError)
      return Response.json(
        { error: error.message, code: error.code },
        { status: error.status },
      );
    console.error(
      "Research request failed:",
      error instanceof Error ? error.name : "unknown error",
    );
    return Response.json(
      { error: "The local research store could not complete this request." },
      { status: 500 },
    );
  });
}
export const identifier = z
  .string()
  .min(1)
  .max(160)
  .regex(/^[a-zA-Z0-9][a-zA-Z0-9:_-]*$/);
export const referenceIds = z
  .array(identifier)
  .max(30)
  .refine(
    (ids) => new Set(ids).size === ids.length,
    "Reference IDs must be unique.",
  );
export const conversationPatch = z
  .object({
    title: z.string().trim().min(1).max(160).optional(),
    archived: z.boolean().optional(),
    pinnedIds: referenceIds.optional(),
    excludedIds: referenceIds.optional(),
  })
  .strict();
