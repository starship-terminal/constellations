import { NextResponse, type NextRequest } from "next/server";
import { isLoopbackHost } from "@/server/request-host";

// No matcher: Next runs this before every route, including reads and media.
// Host comes from the HTTP request; forwarded headers never grant access.
export function proxy(request: NextRequest) {
  if (!isLoopbackHost(request.headers.get("host"))) {
    return NextResponse.json(
      { error: "This personal research app only accepts loopback hosts." },
      { status: 403 },
    );
  }
  return NextResponse.next();
}
