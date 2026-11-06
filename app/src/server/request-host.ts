// This app has no authentication and binds to loopback. Reject attacker-controlled
// DNS names even if their Origin matches Host (the DNS rebinding case).
export function isLoopbackHost(host: string | null): boolean {
  if (!host) return false;
  const match = /^(localhost|127\.0\.0\.1|\[::1\])(?::([0-9]{1,5}))?$/i.exec(
    host,
  );
  return Boolean(
    match && (!match[2] || (Number(match[2]) > 0 && Number(match[2]) <= 65535)),
  );
}

// The optional private deployment is still bound to loopback and published only
// by Tailscale Serve. One exact HTTPS origin grants no trust to forwarded headers.
export function privateOrigin(): URL | null {
  const value = process.env.DESIGN_RESEARCH_PRIVATE_ORIGIN;
  if (!value) return null;
  try {
    const url = new URL(value);
    if (
      url.protocol !== "https:" ||
      !/^[a-z0-9-]+\.[a-z0-9-]+\.ts\.net$/.test(url.hostname) ||
      url.username ||
      url.password ||
      url.pathname !== "/" ||
      url.search ||
      url.hash ||
      value !== url.origin
    )
      return null;
    return url;
  } catch {
    return null;
  }
}

export function isAllowedHost(host: string | null): boolean {
  return (
    isLoopbackHost(host) || Boolean(host && host === privateOrigin()?.host)
  );
}
