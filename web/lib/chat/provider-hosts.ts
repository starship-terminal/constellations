// Which hosts a provider URL may name. The URL comes from the request body
// and the server fetches it with the key attached, so without a list any
// client that reaches /api/ could make this machine GET an internal https
// service or a loopback port. server/chat.py holds the same rules.

/** Model APIs allowed without configuration; each also covers its subdomains. */
export const KNOWN_PROVIDER_HOSTS = [
  "anthropic.com", "openai.com", "openai.azure.com", "generativelanguage.googleapis.com",
  "x.ai", "openrouter.ai", "groq.com", "mistral.ai", "deepseek.com", "together.xyz",
  "fireworks.ai", "cohere.com", "cohere.ai", "perplexity.ai", "cerebras.ai",
];

export const PROVIDER_HOSTS_ENV = "DESIGN_SYSTEMS_PROVIDER_HOSTS";

const strip = (h: string) => h.trim().toLowerCase().replace(/^\[|\]$/g, "").replace(/\.$/, "");

/** Lowercase, no IPv6 brackets or root dot, and parsed the way a request URL
    is, so a listed 0:0:0:0:0:0:0:1 matches a request for [::1]. */
export const bareHost = (h: string) => {
  const s = strip(h);
  if (!s) return s;
  try {
    return strip(new URL(`http://${s.includes(":") ? `[${s}]` : s}/`).hostname);
  } catch {
    return s;
  }
};

const isIp = (h: string) => /^\d{1,3}(\.\d{1,3}){3}$/.test(h) || h.includes(":");
const isLoopback = (h: string) => h === "localhost" || h.endsWith(".localhost") || h === "::1" || /^127\.\d+\.\d+\.\d+$/.test(h);

/** Whether `host` may be fetched as a provider. `listed` is the
    DESIGN_SYSTEMS_PROVIDER_HOSTS value: comma-separated names (each covering
    its subdomains) or exact addresses. Loopback names and IP literals pass
    only when listed exactly, which is how a self-hosted model is opted in. */
export function providerHostAllowed(host: string, listed = ""): boolean {
  const h = bareHost(host);
  const extra = listed.split(",").map(bareHost).filter(Boolean);
  if (extra.includes(h)) return true;
  if (isLoopback(h) || isIp(h)) return false;
  return [...KNOWN_PROVIDER_HOSTS, ...extra].some((k) => !isIp(k) && (h === k || h.endsWith("." + k)));
}
