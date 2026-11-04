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
